# Stored Procedure: `nhung_Admatic_SP_ASD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 14:11:30.320000
- **Ngày sửa cuối**: 2026-03-05 14:11:30.320000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_Admatic_SP_ASD
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;
    SET XACT_ABORT ON;

    ;WITH HDCT AS 
    (
        SELECT 
            HopDongChiTietID,
            ChietKhau
        FROM dbo.HopDongChiTiet
        WHERE HopDongChiTietID = @HopDongChiTietID
    ),

    Admatic AS 
    (
        SELECT  
            t.DmBannerID,
            SUM(t.SoLuongThucChay) AS Raw_SL_TC,
            SUM(t.SoLuongThucChayKM) AS Raw_SL_KM,
            SUM(t.ThanhTienThucChaySauCK_ChuaVAT) AS Raw_TT
        FROM dbo.ThucChay_ThanhTien_Admatic t
        INNER JOIN dbo.ThucChayHopDongChiTiet map 
            ON t.DmBannerID = map.DmBannerREF 
           AND t.DmSanPhamREF = map.DmSanPhamREF
        WHERE map.HopDongChiTietREF = @HopDongChiTietID
          AND map.DeletedStatus = 0
        GROUP BY t.DmBannerID
    ),

    ASD AS 
    (
        SELECT  
            DmBannerREF,
            SUM(SoLuongThucChay + SoLuongThayDoi) AS Raw_SL_TC,
            SUM(SoLuongThucChayKM + SoLuongKMThayDoi) AS Raw_SL_KM,
            SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS Raw_TT_TC,
            SUM(ThanhTienKM + GiaTriKMThayDoi) AS Raw_TT_KM
        FROM dbo.ThucChayDaTinh
        WHERE HopDongChiTietREF = @HopDongChiTietID
        GROUP BY DmBannerREF
    ),

    Data_Cal AS 
    (
        SELECT
            h.HopDongChiTietID,
            h.ChietKhau,
            a.DmBannerID,

            Val.SL_SP,
            Val.TT_SP,
            Val.SL_ASD,
            Val.TT_ASD,

            Diff.SL AS SL_Diff,
            Diff.TT AS TT_Diff

        FROM HDCT h
        LEFT JOIN Admatic a ON 1 = 1 
        LEFT JOIN ASD d ON d.DmBannerREF = a.DmBannerID

        CROSS APPLY
        (
            SELECT 
                SL_SP  = CASE WHEN h.ChietKhau = 100 THEN a.Raw_SL_KM ELSE a.Raw_SL_TC END,
                TT_SP  = a.Raw_TT, 
                SL_ASD = ISNULL(CASE WHEN h.ChietKhau = 100 THEN d.Raw_SL_KM ELSE d.Raw_SL_TC END,0),
                TT_ASD = ISNULL(CASE WHEN h.ChietKhau = 100 THEN d.Raw_TT_KM ELSE d.Raw_TT_TC END,0)
        ) Val

        CROSS APPLY
        (
            SELECT 
                SL = ROUND(Val.SL_SP - Val.SL_ASD,0),
                TT = ROUND(Val.TT_SP - Val.TT_ASD,0)
        ) Diff
    )

    -- ==============================
    -- CHI TIẾT
    -- ==============================

    SELECT 
        CAST(HopDongChiTietID AS NVARCHAR(50)) AS HopDongChiTietID,
        CAST(ChietKhau AS NVARCHAR(50)) AS ChietKhau,
        CAST(DmBannerID AS NVARCHAR(50)) AS DmBannerID,

        dbo.FormatNumber(SL_SP)  AS Soluong_SP,
        dbo.FormatNumber(TT_SP)  AS Thanhtien_SP,

        dbo.FormatNumber(SL_ASD) AS Soluong_ASD,
        dbo.FormatNumber(TT_ASD) AS Thanhtien_ASD,

        dbo.FormatNumber(SL_Diff) AS SLSP_ASD,
        dbo.FormatNumber(TT_Diff) AS TienSP_ASD,

        CASE 
            WHEN TT_Diff = 0 THEN N'OK'
            WHEN TT_Diff > 0 THEN N'Thiếu tiền'
            WHEN TT_Diff < 0 THEN N'Thừa tiền'
            ELSE N''
        END AS GhiChu,

        1 AS SortOrder
    FROM Data_Cal

    UNION ALL

    -- ==============================
    -- TỔNG CỘNG
    -- ==============================

    SELECT 
        N'' AS HopDongChiTietID,
        N'' AS ChietKhau,
        N'TỔNG CỘNG' AS DmBannerID,

        dbo.FormatNumber(SUM(SL_SP)),
        dbo.FormatNumber(SUM(TT_SP)),

        dbo.FormatNumber(SUM(SL_ASD)),
        dbo.FormatNumber(SUM(TT_ASD)),

        dbo.FormatNumber(SUM(SL_Diff)),
        dbo.FormatNumber(SUM(TT_Diff)),

        CASE 
            WHEN SUM(TT_Diff) = 0 THEN N'OK'
            WHEN SUM(TT_Diff) > 0 THEN N'Thiếu tiền'
            WHEN SUM(TT_Diff) < 0 THEN N'Thừa tiền'
            ELSE N''
        END,

        2 AS SortOrder
    FROM Data_Cal

    ORDER BY SortOrder, DmBannerID

END

```
