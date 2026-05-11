# Stored Procedure: `nhung_ThucChay_ThanhTien_Admatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 14:06:55.877000
- **Ngày sửa cuối**: 2026-04-16 11:05:20.360000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[nhung_ThucChay_ThanhTien_Admatic]
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        CASE 
            WHEN GROUPING(DmBannerID) = 1 THEN N'Tổng'
            ELSE CAST(DmBannerID AS NVARCHAR(50))
        END AS DmBannerID,

        sohopdong,

        CASE 
            WHEN GROUPING(DmSanPhamREF) = 1 THEN NULL
            ELSE CAST(DmSanPhamREF AS NVARCHAR(50))
        END AS DmSanPhamREF,

        dbo.FormatNumber(SUM(SoLuongThucChay))                AS SoLuongThucChay,
        dbo.FormatNumber(SUM(ThanhTienThucChaySauCK_ChuaVAT)) AS ThanhTienThucChaySauCK_ChuaVAT,
        dbo.FormatNumber(SUM(SoLuongThucChayKM))              AS SoLuongThucChay_KM,
        dbo.FormatNumber(SUM(ThanhTienThucChayKM))            AS ThanhTienKM_ChuaVAT,
        MIN(NgayThucHien)                                     AS MinNgayThucHien,
        MAX(NgayThucHien)                                     AS MaxNgayThucHien

    FROM dbo.ThucChay_ThanhTien_Admatic t
    WHERE EXISTS (
        SELECT 1
        FROM dbo.ThucChayHopDongChiTiet c
        WHERE c.HopDongChiTietREF = @HopDongChiTietID
          AND c.DeletedStatus = 0
          AND c.DmBannerREF  = t.DmBannerID
          AND c.DmSanPhamREF = t.DmSanPhamREF
    )

    GROUP BY GROUPING SETS (
        (sohopdong, DmBannerID, DmSanPhamREF),
        (sohopdong)  -- 🔥 tổng theo từng HĐ
    )

    ORDER BY 
        sohopdong,
        GROUPING(DmBannerID), -- tổng nằm dưới từng HĐ
        DmBannerID,
        DmSanPhamREF;
END
```
