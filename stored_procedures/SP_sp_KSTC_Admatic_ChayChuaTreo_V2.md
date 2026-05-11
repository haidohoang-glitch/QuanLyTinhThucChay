# Stored Procedure: `sp_KSTC_Admatic_ChayChuaTreo_V2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-07-27 16:46:34.260000
- **Ngày sửa cuối**: 2025-10-22 13:43:44.853000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:      <Author>
-- Create date: <Create Date>
-- Description: Admatic - SP đã chạy nhưng chưa treo (V2)
-- =============================================
CREATE PROCEDURE [dbo].[sp_KSTC_Admatic_ChayChuaTreo_V2]
AS
BEGIN
    SET NOCOUNT ON;

    ------------------------------------------------------------
    -- 0) Map Contract_Id -> SoHopDong (tránh gọi UDF theo dòng)
    ------------------------------------------------------------
    IF OBJECT_ID('tempdb..#MAP') IS NOT NULL DROP TABLE #MAP;
    SELECT 
        M.Contract_Id,
        SoHopDong     = H.SoHopDong,
        SoHopDong_key = UPPER(LTRIM(RTRIM(H.SoHopDong)))
    INTO #MAP
    FROM (
        SELECT DISTINCT Contract_Id
        FROM [ASDAG2].ThucTreo.dbo.ThucTreo   -- nếu là linked server: [Server].[DB].[schema].[object]
        WHERE Product_Formality_Id = 42
          AND Deleted_Status = 0
          AND Contract_Detail_Id NOT IN (0, -1)
    ) AS M
    JOIN dbo.HopDong AS H
      ON H.HopDongID = M.Contract_Id
    WHERE H.SoHopDong IS NOT NULL
      AND H.TrangThaiHopDong NOT IN (0,3);

    CREATE UNIQUE CLUSTERED INDEX CX_MAP ON #MAP(Contract_Id);
    CREATE NONCLUSTERED INDEX IX_MAP_SHD ON #MAP(SoHopDong_key);

    ------------------------------------------------------------
    -- 1) #A: Admatic - tổng hợp thực chạy theo banner + sản phẩm
    ------------------------------------------------------------
    IF OBJECT_ID('tempdb..#A') IS NOT NULL DROP TABLE #A;

    SELECT
        SoHopDong_SP   = t.SoHopDong,
        SoHopDong_key  = UPPER(LTRIM(RTRIM(t.SoHopDong))),
        DmBannerID     = t.DmBannerID,
        PB_SP          = t.HopDongChiTietREF,
        SP_SP          = t.DmSanPhamREF,
        ThanhtienTC_SP = SUM(COALESCE(t.ThanhTienThucChaySauCK_ChuaVAT, 0.0)),
        ThanhtienKM_SP = SUM(COALESCE(t.ThanhTienThucChayKM, 0.0))
    INTO #A
    FROM dbo.ThucChay_ThanhTien_Admatic AS t
    WHERE
          t.SoHopDong NOT IN ('hd_demo','','HD DEMO','hd_king_test2','HD SELFSERVE','TEST','HD TEST','DEMO','HD PROG')
      AND t.SoHopDong NOT LIKE '%demo%' ESCAPE '\'
      AND t.SoHopDong NOT LIKE '%test%' ESCAPE '\'
      AND t.DmSanPhamREF <> 5312
      AND EXISTS (
            SELECT 1
            FROM dbo.HopDong h
            WHERE h.SoHopDong = t.SoHopDong
              AND h.TrangThaiHopDong NOT IN (0,3)
      )
    GROUP BY t.SoHopDong, t.DmBannerID, t.HopDongChiTietREF, t.DmSanPhamREF
    HAVING
          SUM(COALESCE(t.ThanhTienThucChaySauCK_ChuaVAT, 0.0)) <> 0
       OR SUM(COALESCE(t.ThanhTienThucChayKM, 0.0)) <> 0;

    CREATE CLUSTERED INDEX CX_A ON #A(SoHopDong_key, DmBannerID, PB_SP);
    CREATE NONCLUSTERED INDEX IX_A_SP ON #A(SP_SP);

    ------------------------------------------------------------
    -- 2) #B: Treo (ASD) - dùng mapping #MAP, không gọi UDF
    ------------------------------------------------------------
    IF OBJECT_ID('tempdb..#B') IS NOT NULL DROP TABLE #B;

    SELECT
        TT.Banner_Id,
        SoHopDong_treo = M.SoHopDong,
        SoHopDong_key  = M.SoHopDong_key,
        TT.Contract_Detail_Id,
        TT.Contract_Id,
        TT.TenBanner
    INTO #B
    FROM [ASDAG2].ThucTreo.dbo.ThucTreo AS TT
    JOIN #MAP AS M
      ON M.Contract_Id = TT.Contract_Id
    WHERE
        TT.Product_Formality_Id = 42
        AND TT.Deleted_Status = 0
        AND TT.Contract_Detail_Id NOT IN (0,-1);

    CREATE CLUSTERED INDEX CX_B ON #B(SoHopDong_key, Banner_Id);
    CREATE NONCLUSTERED INDEX IX_B_CD ON #B(Contract_Id, Contract_Detail_Id);

    ------------------------------------------------------------
    -- 3) #D: HĐ + HĐCT (đẩy filter sớm để giảm rows)
    ------------------------------------------------------------
    IF OBJECT_ID('tempdb..#D') IS NOT NULL DROP TABLE #D;

    SELECT 
        hd.SoHopDong,
        hd.HopDongID,
        hdct.HopDongChiTietID,
        hdct.DmSanPhamREF,
        hdct.DonViTinh,
        hdct.SoLuong,
        hdct.DonGia,
        hdct.ChietKhau,
        hdct.ThanhTien,
        hdct.DmLoaiNenTangREF,
        hdct.TenSanPham
    INTO #D
    FROM dbo.HopDongChiTiet AS hdct
    JOIN dbo.HopDong AS hd
      ON hd.HopDongID = hdct.HopDongFK
    WHERE hdct.DmLoaiNenTangREF <> 9
      AND (hdct.DonViTinh IS NULL OR hdct.DonViTinh NOT LIKE N'Bài');

    CREATE CLUSTERED INDEX CX_D ON #D(SoHopDong, DmSanPhamREF);

    ------------------------------------------------------------
    -- 4) KẾT QUẢ: SP đã chạy nhưng CHƯA được treo (ghép đúng cặp banner)
    ------------------------------------------------------------
    ;WITH C AS (
        SELECT
            A.SoHopDong_SP,
            A.DmBannerID,
            A.PB_SP,
            A.SP_SP,
            A.ThanhtienTC_SP,
            A.ThanhtienKM_SP,
            B.Contract_Id,
            B.Contract_Detail_Id,
            B.Banner_Id,
            B.TenBanner
        FROM #A AS A
        LEFT JOIN #B AS B
          ON  A.SoHopDong_key = B.SoHopDong_key
          AND A.DmBannerID    = B.Banner_Id
        WHERE B.Banner_Id IS NULL
    )
    SELECT 
        D.SoHopDong,
        D.HopDongID,
        D.HopDongChiTietID,
        D.DmSanPhamREF,
        D.TenSanPham,
        D.SoLuong                              AS SoLuong_HĐ,
        dbo.FormatNumber(D.DonGia)             AS DonGia_HĐ,
        dbo.FormatNumber(D.ChietKhau)          AS ChietKhau_HĐ,
        dbo.FormatNumber(
            CASE WHEN COALESCE(D.ChietKhau,0) = 100 
                 THEN D.SoLuong * D.DonGia 
                 ELSE D.ThanhTien 
            END
        )                                       AS Thanhtien_HĐ,
        C.DmBannerID                            AS Banner_SP,
        dbo.FormatNumber(C.ThanhtienTC_SP)      AS ThanhtienTC_SP,
        dbo.FormatNumber(C.ThanhtienKM_SP)      AS ThanhtienKM_SP,
        C.Banner_Id                             AS Banner_Treo,
        CASE 
            WHEN C.Banner_Id IS NULL 
            THEN CONCAT(
                 N'Chạy ', dbo.FormatNumber(
                     CASE WHEN COALESCE(D.ChietKhau,0)=100 
                          THEN C.ThanhtienKM_SP ELSE C.ThanhtienTC_SP END
                 ),
                 N' – chưa treo'
            )
        END                                     AS Ghi_Chu
    FROM C
    LEFT JOIN #D AS D
      ON C.SP_SP = D.DmSanPhamREF 
     AND C.SoHopDong_SP = D.SoHopDong
    WHERE D.SoHopDong IS NOT NULL
	AND D.SoHopDong NOT IN ('QC2050724','QC1400623','QC3681222','QC3491120')
    ORDER BY 
        TRY_CONVERT(INT, RIGHT(D.SoHopDong, 2)) DESC,  -- sắp theo 2 ký tự cuối (số)
        D.SoHopDong;                                   -- tie-breaker

END

```
