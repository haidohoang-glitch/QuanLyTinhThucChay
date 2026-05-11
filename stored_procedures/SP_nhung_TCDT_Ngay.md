# Stored Procedure: `nhung_TCDT_Ngay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 14:16:30.303000
- **Ngày sửa cuối**: 2026-03-05 14:16:30.303000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_TCDT_Ngay
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;
SELECT
    CASE 
        WHEN GROUPING(NgayThucHien) = 1 THEN N'Tổng'
        ELSE CONVERT(NVARCHAR(10), NgayThucHien, 120)
    END AS NgayThucHien,

    dbo.FormatNumber(SUM(SoLuongThucChay + SoLuongThayDoi))              AS Soluong_TC,
    dbo.FormatNumber(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)) AS Thanhtien_TC,
    dbo.FormatNumber(SUM(SoLuongThucChayKM + SoLuongKMThayDoi))          AS Soluong_KM,
    dbo.FormatNumber(SUM(ThanhTienKM))                                   AS ThanhTienKM
FROM dbo.ThucChayDaTinh
WHERE HopDongChiTietREF = @HopDongChiTietID
GROUP BY GROUPING SETS
(
    (NgayThucHien),  -- chi tiết theo ngày
    ()               -- tổng
)
ORDER BY
    GROUPING(NgayThucHien),  -- 0 = chi tiết, 1 = tổng  → tổng xuống cuối
    NgayThucHien DESC;       -- ngày mới nhất lên trước


END

```
