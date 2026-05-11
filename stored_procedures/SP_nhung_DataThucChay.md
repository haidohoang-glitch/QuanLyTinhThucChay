# Stored Procedure: `nhung_DataThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 17:10:13.467000
- **Ngày sửa cuối**: 2026-03-05 17:10:13.467000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE dbo.nhung_DataThucChay
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;
SELECT
    CASE 
        WHEN GROUPING(bannerid) = 1 THEN N'Tổng'
        ELSE CAST(bannerid AS NVARCHAR(50))
    END AS bannerid,

    CASE 
        WHEN GROUPING(DmSanPhamREF) = 1 THEN NULL
        ELSE CAST(DmSanPhamREF AS NVARCHAR(50))
    END AS DmSanPhamREF,

    dbo.FormatNumber(SUM(TRY_CONVERT(FLOAT, TongViewThucChay)))       AS Tong_Views,
    dbo.FormatNumber(SUM(TRY_CONVERT(FLOAT, TongClickThucChay)))     AS Tong_Click,
	MIN(NgayThucHien) MinNgayThucHien,
	Max( NgayThucHien) MaxNgayThucHien
FROM dbo.DataThucChay
WHERE bannerid IN (
    SELECT DmBannerREF
    FROM dbo.ThucChayHopDongChiTiet
    WHERE HopDongChiTietREF = @HopDongChiTietID
      AND DeletedStatus = 0
)
GROUP BY GROUPING SETS (
    (bannerid, DmSanPhamREF),  -- dòng chi tiết
    ()                               -- dòng tổng
)
ORDER BY
    GROUPING(bannerid),   -- đảm bảo dòng Tổng ở cuối
    bannerid;

END

```
