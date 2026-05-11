# Stored Procedure: `nhung_TCDTtong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 14:14:24.513000
- **Ngày sửa cuối**: 2026-03-05 14:14:24.513000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_TCDTtong
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;
    SELECT
    CASE WHEN GROUPING(SoHopDong) = 1 THEN N'Tổng' ELSE SoHopDong END       AS SoHopDong,
    CASE WHEN GROUPING(HopDongChiTietREF) = 1 THEN NULL ELSE HopDongChiTietREF END AS HopDongChiTietREF,
    CASE WHEN GROUPING(TenSanPham) = 1 THEN NULL ELSE TenSanPham END       AS TenSanPham,

    dbo.FormatNumber(SUM(SoLuongThucChay + SoLuongThayDoi))                    AS Soluong_TC,
    dbo.FormatNumber(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi))       AS Thanhtien_TC,
    dbo.FormatNumber(SUM(SoLuongThucChayKM + SoLuongKMThayDoi))                AS Soluong_KM,
    dbo.FormatNumber(SUM(ThanhTienKM+GiaTriKMThayDoi))                                         AS ThanhTienKM,
    dbo.FormatNumber(SUM(SoLuongThucChayLechTreoHa))                           AS Soluong_LechTreoHa,
    dbo.FormatNumber(SUM(ThanhTienLechTreoHa))                                 AS ThanhTienLechTreoHa
FROM dbo.ThucChayDaTinh
WHERE HopDongChiTietREF = @HopDongChiTietID
GROUP BY GROUPING SETS
(
    (SoHopDong, HopDongChiTietREF, TenSanPham),  -- chi tiết
    ()                                           -- tổng
)
ORDER BY
    GROUPING(SoHopDong), SoHopDong, TenSanPham;

END

```
