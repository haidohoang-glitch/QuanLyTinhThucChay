# Stored Procedure: `BC_PhanBoKhongHopDong_D1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-10-24 14:02:19.247000
- **Ngày sửa cuối**: 2025-10-24 14:05:21.867000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[BC_PhanBoKhongHopDong_D1]
AS
BEGIN
    SET NOCOUNT ON;

    /* ======================================================
       BÁO CÁO PHÂN BỔ KHÔNG HỢP ĐỒNG (D-1, NO HĐ KÝ)
       - Chỉ lấy ngày hôm qua (D-1)
       - Chỉ lấy tài khoản không có số hợp đồng (NULL / '' / 'BLANK')
       - Loại trừ banlist
       - Gộp theo user để tính tổng view / click / tiền
       ====================================================== */

    -------------------------------------------------
    -- 1. Chuẩn bị khoảng thời gian hôm qua
    -------------------------------------------------
    DECLARE @today      DATE      = CAST(GETDATE() AS DATE); 
    DECLARE @d1_start   DATETIME2 = DATEADD(DAY, -1, @today);  -- hôm qua 00:00
    DECLARE @d1_end     DATETIME2 = @today;                    -- hôm nay 00:00

    -------------------------------------------------
    -- 2. Danh sách username loại trừ
    -------------------------------------------------
    DECLARE @Banlist TABLE (username SYSNAME PRIMARY KEY);
    INSERT INTO @Banlist (username) VALUES
         (N'DUCTRUNG123'),
         (N'RODEX'),
         (N'DUOCADX1'),
         (N'TRUNGMYADX'),
         (N'TRUNGMYADXTAIKHOAN2'),
         (N'THIETBICAMTAY'),
         (N'ZENTOHCM'),
         (N'ZENTOMIENTRUNG'),
         (N'ARENAAPROTRAIN'),
         (N'bontam');

    -------------------------------------------------
    -- 3. Lọc dữ liệu phân bổ KHÔNG có số HĐ trong ngày hôm qua
    --    -> đổ vào temp table #A
    -------------------------------------------------
    IF OBJECT_ID('tempdb..#A') IS NOT NULL DROP TABLE #A;

    SELECT
        p.user_id,
        p.username,
		p.tennhanhang,
        -- ép contract_number rỗng/null thành 'BLANK' chỉ để tham khảo
        ISNULL(NULLIF(LTRIM(RTRIM(p.contract_number)), ''), N'BLANK') AS SoHopDong_SP,
        SUM(TRY_CONVERT(DECIMAL(19,4), p.domain_tt_view))  AS tong_view,
        SUM(TRY_CONVERT(DECIMAL(19,4), p.domain_tt_click)) AS tong_click,
        SUM(TRY_CONVERT(DECIMAL(19,4), p.domain_tt_money)) AS tong_tien,
        p.createdAt
    INTO #A
    FROM dbo.ThucChayAdmarket_PhanBo AS p
    LEFT JOIN @Banlist b
        ON p.username COLLATE Latin1_General_CI_AI
         = b.username COLLATE Latin1_General_CI_AI
    WHERE
          (
              NULLIF(LTRIM(RTRIM(p.contract_number)), '') IS NULL
              OR UPPER(LTRIM(RTRIM(p.contract_number))) = N'BLANK'
          )
      AND ISNULL(p.username, '') <> ''        -- tránh username rỗng
      AND b.username IS NULL                  -- không nằm trong banlist
      AND p.createdAt >= @d1_start
      AND p.createdAt <  @d1_end              -- chỉ D-1
    GROUP BY 
        p.user_id,
        p.username,
        p.contract_number,
        p.createdAt,
		p.tennhanhang
    HAVING 
        SUM(TRY_CONVERT(DECIMAL(19,4), p.domain_tt_money)) > 0;

    -- Index tạm để ORDER BY chạy mượt nếu dữ liệu to
    CREATE INDEX IX_A_user ON #A(user_id);

    -------------------------------------------------
    -- 4. Kết quả báo cáo cuối (giống output bạn đang xem)
    -------------------------------------------------
    SELECT
        A.username                    AS TaiKhoan,
		A.tennhanhang				  AS NhanHang,
        FORMAT(A.tong_view,  '#,##0') AS TongView,
        FORMAT(A.tong_click,'#,##0')  AS TongClick,
        FORMAT(A.tong_tien,  '#,##0') AS TongTien_Online,
        CONVERT(DATE, A.createdAt)    AS NgayPhatSinh
    FROM #A AS A
    ORDER BY A.username DESC;

    -------------------------------------------------
    -- 5. Cleanup
    -------------------------------------------------
    DROP TABLE #A;
END

```
