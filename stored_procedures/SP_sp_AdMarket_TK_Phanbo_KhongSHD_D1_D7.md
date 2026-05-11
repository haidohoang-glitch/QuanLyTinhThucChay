# Stored Procedure: `sp_AdMarket_TK_Phanbo_KhongSHD_D1_D7`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-10-22 14:22:26.297000
- **Ngày sửa cuối**: 2025-11-05 10:55:42.007000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NamTu` | `int(4)` | No |
| `@DmSanPhamRef` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.sp_AdMarket_TK_Phanbo_KhongSHD_D1_D7
(
    @NamTu         INT = 2020,
    @DmSanPhamRef  INT = 585
)
AS
BEGIN
    SET NOCOUNT ON;

    /* ========================================================= 
       Báo cáo TK phân bổ KHÔNG số HĐ + cảnh báo phát sinh ngày D-1 & D-7
       - Tối ưu SARGable (lọc createdAt theo khoảng thời gian)
       - Vật hoá vào #temp + tạo index tạm để join nhanh
       - Định dạng số tiền/số lượng cho dễ đọc trong kết quả cuối
       ========================================================= */

    -- ==== Mốc thời gian: hôm qua (D-1) & 7 ngày trước (D-7) ====
    DECLARE @today    date      = CAST(GETDATE() AS date);
    DECLARE @d1_start datetime2 = DATEADD(day, -1, @today); -- D-1 00:00
    DECLARE @d1_end   datetime2 = @today;                   -- D-1 24:00 (mốc đầu ngày hôm nay)
    DECLARE @d7_start datetime2 = DATEADD(day, -7, @today); -- D-7 00:00
    DECLARE @d7_end   datetime2 = DATEADD(day, -6, @today); -- D-7 24:00 (mốc cách đây 6 ngày)

    -- ==== Danh sách username loại trừ (anti-join) ====
    DECLARE @Banlist TABLE (username sysname PRIMARY KEY);
    INSERT INTO @Banlist (username) VALUES
         (N'DUCTRUNG123')
        ,(N'RODEX')
        ,(N'DUOCADX1')
        ,(N'TRUNGMYADX')
        ,(N'TRUNGMYADXTAIKHOAN2')
        ,(N'THIETBICAMTAY')
        ,(N'ZENTOHCM')
        ,(N'ZENTOMIENTRUNG')
        ,(N'ARENAAPROTRAIN');

    /* =========================================================
       #A: Phân bổ KHÔNG có số HĐ (contract_number trống / 'BLANK')
           + chỉ lấy phát sinh đúng ngày D-1 hoặc D-7
           + loại trừ các username trong banlist
       ========================================================= */
    IF OBJECT_ID('tempdb..#A') IS NOT NULL DROP TABLE #A;

    SELECT
        p.[user_id],
        p.username,
        p.contract_number,
        SUM(TRY_CONVERT(DECIMAL(19,4), p.domain_tt_view))   AS tong_view,
        SUM(TRY_CONVERT(DECIMAL(19,4), p.domain_tt_click))  AS tong_click,
        SUM(TRY_CONVERT(DECIMAL(19,4), p.domain_tt_money))  AS tong_tien
        --p.createdAt
    INTO #A
    FROM dbo.ThucChayAdmarket_PhanBo AS p
    LEFT JOIN @Banlist b
      ON p.username COLLATE Latin1_General_CI_AI = b.username COLLATE Latin1_General_CI_AI
    WHERE
        (
            NULLIF(LTRIM(RTRIM(p.contract_number)), '') IS NULL
            OR p.contract_number COLLATE Latin1_General_CI_AI = N'BLANK'
        )
        AND ISNULL(p.username, '') <> ''
        AND b.username IS NULL
        AND p.createdAt >= @d7_start 
		AND p.createdAt <  @d1_end     
    GROUP BY 
        p.[user_id], 
        p.username, 
        p.contract_number
        --p.createdAt
    HAVING 
        SUM(TRY_CONVERT(DECIMAL(19,4), p.domain_tt_money)) > 0;

    CREATE INDEX IX_A_user ON #A(user_id);

    /* =========================================================
       #C: Chi tiết HĐ ký theo sản phẩm / điều kiện lọc
       - Lấy các dòng Hợp Đồng Chi Tiết (HĐCT) hợp lệ
       - Map sang thông tin TK_AdMarket
       ========================================================= */
    IF OBJECT_ID('tempdb..#C') IS NOT NULL DROP TABLE #C;

    SELECT 
        hd.NgayDanhSoHopDong,
        hd.SoHopDong,
        hdct.HopDongChiTietID,
        hdct.SoLuong,
        hdct.DonGia,
        hdct.ChietKhau,
        hdct.ThanhTien,
        hdct.TK_AdMarketID,
        hdct.TK_AdMarket
    INTO #C
    FROM dbo.HopDongChiTiet AS hdct
    JOIN dbo.HopDong AS hd
      ON hd.HopDongID = hdct.HopDongFK
    WHERE
        hdct.DeletedStatus = 0
        AND hd.TrangThaiHopDong NOT IN (0, 3)              -- loại HĐ nháp/hủy
        AND hdct.DmLoaiREF IN (26, 5010, 5038, 5000)       -- các loại hình QC liên quan AdMarket
        AND hdct.DmSanPhamREF = @DmSanPhamRef              -- filter theo sản phẩm cần theo dõi
        AND hd.Nam >= @NamTu;                              -- chỉ lấy từ năm @NamTu trở đi

    CREATE INDEX IX_C_TK ON #C(TK_AdMarketID);

    /* =========================================================
       #D: Tổng giá trị thực chạy đã tính cho từng HĐCT
       - Gom các phát sinh thực chạy (đã tính) để so đối chiếu HĐ ký
       ========================================================= */
    IF OBJECT_ID('tempdb..#D') IS NOT NULL DROP TABLE #D;

    SELECT 
        d.HopDongChiTietREF,
        SUM(
            ISNULL(d.ThanhTienSauTrietKhauThucChay,0) 
          + ISNULL(d.GiaTriThayDoi,0)
        ) AS TongThucChay
    INTO #D
    FROM dbo.ThucChayDaTinhAdmarket AS d
    WHERE 
        d.DmHinhThucQuangCao IN (26, 5010, 5038, 5000)
    GROUP BY 
        d.HopDongChiTietREF;

    CREATE INDEX IX_D_REF ON #D(HopDongChiTietREF);

    /* =========================================================
       Kết quả cuối cùng:
       - Ghép #C (HĐ ký) với #D (Thực chạy) và #A (phát sinh KHÔNG số HĐ)
       - Định dạng số cho dễ đọc
       - Gắn ghi chú chênh lệch
       ========================================================= */
    SELECT
        C.TK_AdMarketID,
        C.TK_AdMarket,

        A.contract_number AS SoHopDong_SP,

        FORMAT(A.tong_view,  '#,##0')                           AS tong_view_SP,
        FORMAT(A.tong_click, '#,##0')                           AS tong_click_SP,
        FORMAT(A.tong_tien,  '#,##0')                           AS tong_tien_SP,

        --CONVERT(date, A.createdAt)                              AS NgayPhatSinh,

        C.SoHopDong,
        C.HopDongChiTietID,
        C.SoLuong,
        FORMAT(C.DonGia, '#,##0')                               AS DonGia,
        C.ChietKhau,
        FORMAT(C.ThanhTien, '#,##0')                            AS ThanhTien_HDky,
        FORMAT(ISNULL(D.TongThucChay,0), '#,##0')               AS ThanhTien_ThucChay,
        FORMAT(C.ThanhTien - ISNULL(D.TongThucChay,0), '#,##0') AS TienTC_thieu_HDKy,

        CASE 
            WHEN D.TongThucChay IS NULL 
                THEN N'Phân bổ chưa có thực chạy'
            WHEN C.ThanhTien - ISNULL(D.TongThucChay,0) < 0 
                THEN N'Phân bổ vượt thực chạy so với HĐ ký'
            WHEN C.ThanhTien - ISNULL(D.TongThucChay,0) > 0 
                THEN N'Phân bổ chưa đủ thực chạy so với HĐ ký'
            ELSE N'Khớp thực chạy và HĐ ký'
        END AS Ghichu
    FROM #C AS C
    LEFT JOIN #D AS D 
        ON D.HopDongChiTietREF = C.HopDongChiTietID
    JOIN #A AS A 
        ON A.user_id = C.TK_AdMarketID
    WHERE 
        (C.ThanhTien - ISNULL(D.TongThucChay,0)) > 1000
		AND C.ChietKhau <> 100
    ORDER BY 
        C.TK_AdMarket, 
        C.NgayDanhSoHopDong DESC, 
        C.SoHopDong DESC
    OPTION (RECOMPILE);
END

```
