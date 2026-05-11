# Stored Procedure: `nhung_TCDTkhongcoIDtreoPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 14:49:55.190000
- **Ngày sửa cuối**: 2026-03-05 14:49:55.190000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE nhung_TCDTkhongcoIDtreoPR
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;
SELECT DotChayBooking,
SUM(SoLuongThucChay+SoLuongThayDoi) Soluong_TC,
SUM(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi) thanhtien_TC,
SUM(SoLuongThucChayKM+SoLuongKMThayDoi) Soluong_KM,
SUM(ThanhTienKM+GiaTriKMThayDoi) thanhtien_KM
FROM dbo.ThucChayDaTinh 
WHERE HopDongChiTietREF = @HopDongChiTietID
AND DotChayBooking NOT IN (SELECT ThucChayHopDongChiTietPRID FROM dbo.ThucChayHopDongChiTietPR WHERE HopDongChiTietREF = @HopDongChiTietID)
GROUP BY DotChayBooking

END

```
