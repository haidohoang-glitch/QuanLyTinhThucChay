# Stored Procedure: `nhung_ThongtintreoChiphi_nguon`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 15:39:52.810000
- **Ngày sửa cuối**: 2026-03-06 15:39:52.810000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_ThongtintreoChiphi_nguon
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;

SELECT 
    Id,
    Contract_Id,
    Contract_Detail_Id,
    Product_Id,
    Brand_Id,
    Brand_Name,
    Quantity,
    UnitName,
    dbo.FormatNumber(UnitPrice)    AS DonGia,
    Discount,
    dbo.FormatNumber(TotalMoney)  AS Thanhtien,
    DeletedStatus,
    RecordStatus,
    CreatedAt,
    CreatedBy,
    LastModifiedAt,
    LastModifiedBy,
    SyncId
FROM ASDAG2.ThucTreo.dbo.ThucTreo_ChiPhi
WHERE Contract_Detail_Id = @HopDongChiTietID
  AND DeletedStatus = 0
  AND RecordStatus in (1,2,3)

UNION ALL

SELECT
    NULL AS Id,
    NULL AS Contract_Id,
    NULL AS Contract_Detail_Id,
    NULL AS Product_Id,
    NULL AS Brand_Id,
    N'TỔNG' AS Brand_Name,
    NULL AS Quantity,
    NULL AS UnitName,
    NULL AS DonGia,
    NULL AS Discount,
    dbo.FormatNumber(SUM(TotalMoney)) AS Thanhtien,
    NULL AS DeletedStatus,
    NULL AS RecordStatus,
    NULL AS CreatedAt,
    NULL AS CreatedBy,
    NULL AS LastModifiedAt,
    NULL AS LastModifiedBy,
    NULL AS SyncId
FROM ASDAG2.ThucTreo.dbo.ThucTreo_ChiPhi
WHERE Contract_Detail_Id = @HopDongChiTietID
  AND DeletedStatus = 0;

END 

```
