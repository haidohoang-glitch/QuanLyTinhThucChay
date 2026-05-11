# Stored Procedure: `nhung_TCDTMuaNgoai_IDtreo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 16:57:24.307000
- **Ngày sửa cuối**: 2026-03-06 16:58:17.167000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE nhung_TCDTMuaNgoai_IDtreo
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

SELECT
    DotChayBooking,
    dbo.FormatNumber(SUM(SoLuongThucChay + SoLuongThayDoi)) AS soluongTC,
    dbo.FormatNumber(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)) AS ThanhtienTC,
    dbo.FormatNumber(SUM(SoLuongThucChayKM + SoLuongKMThayDoi)) AS soluongKM,
    dbo.FormatNumber(SUM(ThanhTienKM + GiaTriKMThayDoi)) AS ThanhtienKM
FROM dbo.ThucChayDaTinh
WHERE HopDongChiTietREF = @HopDongChiTietID
GROUP BY DotChayBooking

UNION ALL

SELECT
    N'TỔNG' AS DotChayBooking,
    dbo.FormatNumber(SUM(SoLuongThucChay + SoLuongThayDoi)) AS soluongTC,
    dbo.FormatNumber(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)) AS ThanhtienTC,
    dbo.FormatNumber(SUM(SoLuongThucChayKM + SoLuongKMThayDoi)) AS soluongKM,
    dbo.FormatNumber(SUM(ThanhTienKM + GiaTriKMThayDoi)) AS ThanhtienKM
FROM dbo.ThucChayDaTinh
WHERE HopDongChiTietREF = @HopDongChiTietID

ORDER BY DotChayBooking ASC;

END 

```
