# Stored Procedure: `nhung_TCDT_Performance`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 16:19:31.563000
- **Ngày sửa cuối**: 2026-03-05 16:19:31.563000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_TCDT_Performance 
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        'TCDT' AS TCDT,

        CASE WHEN GROUPING(SoHopDong) = 1 THEN N'Tổng'
             ELSE SoHopDong END AS SoHopDong,

        CASE WHEN GROUPING(HopDongChiTietREF) = 1 THEN NULL ELSE HopDongChiTietREF END AS HopDongChiTietREF,
        CASE WHEN GROUPING(DotChayHopDong) = 1 THEN NULL ELSE DotChayHopDong END AS DotChayHopDong,
        CASE WHEN GROUPING(DotChayBooking) = 1 THEN NULL ELSE DotChayBooking END AS DotChayBooking,
        CASE WHEN GROUPING(TenSanPham) = 1 THEN NULL ELSE TenSanPham END AS TenSanPham,
        CASE WHEN GROUPING(TenViTri) = 1 THEN NULL ELSE TenViTri END AS TenViTri,
        CASE WHEN GROUPING(NhanHang) = 1 THEN NULL ELSE NhanHang END AS NhanHang,
        CASE WHEN GROUPING(SoLuongDotChayBooking) = 1 THEN NULL ELSE SoLuongDotChayBooking END AS SoLuongDotChayBooking,

        dbo.FormatNumber(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)) AS Thanhtien_TC

    FROM dbo.ThucChayDaTinh
    WHERE HopDongChiTietREF = @HopDongChiTietID

    GROUP BY GROUPING SETS
    (
        (SoHopDong, HopDongChiTietREF, DotChayHopDong, TenSanPham, TenViTri, NhanHang, DotChayBooking, SoLuongDotChayBooking),
        ()
    )

    ORDER BY
        GROUPING(SoHopDong),
        SoHopDong,
        DotChayHopDong,
        DotChayBooking,
        TenSanPham;

END

```
