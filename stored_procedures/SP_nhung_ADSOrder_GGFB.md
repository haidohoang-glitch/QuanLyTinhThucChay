# Stored Procedure: `nhung_ADSOrder_GGFB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 17:09:43.970000
- **Ngày sửa cuối**: 2026-03-06 17:09:43.970000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE nhung_ADSOrder_GGFB
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

SELECT Id,
Contract_Id,
Contract_Detail_Id, 
dbo.FormatNumber(Money_Turnover) AS Ngansach, 
Status,
IsDeleted,
CreationTime,
CreatedBy,
LastModificationTime,
LastModifiedBy,
Team
FROM dbo.ADS_Operating_Order 
WHERE Contract_Detail_Id = @HopDongChiTietID
AND IsDeleted = 0

END

```
