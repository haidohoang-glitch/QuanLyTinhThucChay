# Stored Procedure: `nhung_GetContractByDetailIDnguon`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 11:12:16.780000
- **Ngày sửa cuối**: 2026-03-05 11:23:47.613000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[nhung_GetContractByDetailIDnguon]
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT 
           hd.CONTRACT_NUMBER,
           hd.ID,
           hd.CUSTOMER_ID,       
           hd.ROOT_BRAND_ID,
           hd.TOTAL_VALUE,
           hd.STATUS AS TrangThaiHopDong,
           hd.CREATED_AT,
           hd.LAST_MODIFIED_AT    
    FROM ASDAG2.CONTRACT.dbo.CONTRACTS hd
    JOIN ASDAG2.CONTRACT.dbo.CONTRACT_DETAILS cd 
         ON cd.CONTRACT_ID = hd.ID
         AND cd.DELETED_STATUS = 0
    WHERE cd.ID = @HopDongChiTietID
    AND hd.DELETED_STATUS = 0;

END

```
