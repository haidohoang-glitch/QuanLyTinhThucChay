# Stored Procedure: `nhung_TCDT_Nhan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 14:15:48.110000
- **Ngày sửa cuối**: 2026-03-05 14:15:48.110000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_TCDT_Nhan
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;
SELECT
    CASE WHEN GROUPING(SoHopDong) = 1 THEN N'Tổng' ELSE SoHopDong END       AS SoHopDong,
    CASE WHEN GROUPING(HopDongChiTietREF) = 1 THEN NULL ELSE HopDongChiTietREF END AS HopDongChiTietREF,
	NhanHang,
    dbo.FormatNumber(SUM(SoLuongThucChay + SoLuongThayDoi))                    AS Soluong_TC,
    dbo.FormatNumber(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi))       AS Thanhtien_TC,
    dbo.FormatNumber(SUM(SoLuongThucChayKM + SoLuongKMThayDoi))                AS Soluong_KM,
    dbo.FormatNumber(SUM(ThanhTienKM))                                         AS ThanhTienKM
FROM dbo.ThucChayDaTinh
WHERE HopDongChiTietREF = @HopDongChiTietID
GROUP BY GROUPING SETS
(
    (SoHopDong, HopDongChiTietREF, NhanHang),  -- chi tiết
    ()                                           -- tổng
)
ORDER BY
    GROUPING(SoHopDong), SoHopDong, NhanHang;

END

```
