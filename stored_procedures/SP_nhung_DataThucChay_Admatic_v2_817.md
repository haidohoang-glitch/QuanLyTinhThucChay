# Stored Procedure: `nhung_DataThucChay_Admatic_v2_817`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-10 09:45:30.173000
- **Ngày sửa cuối**: 2026-03-10 09:55:11.153000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_DataThucChay_Admatic_v2_817
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;
SELECT
    CASE 
        WHEN GROUPING(banner_id) = 1 THEN N'Tổng'
        ELSE CAST(banner_id AS NVARCHAR(50))
    END AS banner_id,

    CASE 
        WHEN GROUPING(DmSanPhamREF) = 1 THEN NULL
        ELSE CAST(DmSanPhamREF AS NVARCHAR(50))
    END AS DmSanPhamREF,

    dbo.FormatNumber(SUM(TRY_CONVERT(FLOAT, domain_tt_view)))       AS Tong_Views,
    dbo.FormatNumber(SUM(TRY_CONVERT(FLOAT, domain_tt_click)))     AS Tong_Click,
    dbo.FormatNumber(SUM(TRY_CONVERT(FLOAT, domain_tt_money)))      AS ThanhTienTC,
    dbo.FormatNumber(SUM(TRY_CONVERT(FLOAT, domain_tt_promotion)))  AS ThanhTienKM,
    vat,
	MIN(NgayThucHien) MinNgayThucHien,
	Max( NgayThucHien) MaxNgayThucHien
FROM dbo.DataThucChay_Admatic_v2
WHERE banner_id IN (
    SELECT DmBannerREF
    FROM dbo.ThucChayHopDongChiTiet
    WHERE HopDongChiTietREF = @HopDongChiTietID
      AND DeletedStatus = 0
	  AND DmSanPhamREF = 817

)
AND DmSanPhamREF = 817
AND mktFeeAllocationId = @HopDongChiTietID
GROUP BY GROUPING SETS (
    (banner_id, DmSanPhamREF, vat),  -- dòng chi tiết
    ()                               -- dòng tổng
)
ORDER BY
    GROUPING(banner_id),   -- đảm bảo dòng Tổng ở cuối
    banner_id;
END


```
