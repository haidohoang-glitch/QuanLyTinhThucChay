# Stored Procedure: `Gen_InsertOrUpdate_GGFB_ByNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-10-24 15:10:30.363000
- **Ngày sửa cuối**: 2025-10-24 16:24:04.097000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_GGFB_ByNgayThucHien] 	
	@FromDate DATETIME ,
	@ToDate DATETIME
AS	
BEGIN
	PRINT 'LAY DU LIEU GGFB'
	EXEC [dbo].[Gen_InsertOrUpdate_Operating_Order_GGFB_ByNgayThucHien] 	
	@FromDate = @FromDate,
	@ToDate = @ToDate

	EXEC [dbo].[Gen_InsertOrUpdate_Operating_Order_log_GGFB_ByNgayThucHien] 	
	@FromDate = @FromDate,
	@ToDate = @ToDate

	EXEC [dbo].[Gen_InsertOrUpdate_Operating_Result_GGFB_ByNgayThucHien] 	
	@FromDate = @FromDate,
	@ToDate = @ToDate

	EXEC [dbo].[Gen_InsertOrUpdate_Operating_Result_Log_GGFB_ByNgayThucHien] 	
	@FromDate = @FromDate,
	@ToDate = @ToDate

	EXEC [dbo].[Gen_InsertOrUpdate_Operating_Result_Map_Order_GGFB_ByNgayThucHien] 	
	@FromDate = @FromDate,
	@ToDate = @ToDate

	EXEC [dbo].[Gen_InsertOrUpdate_Operating_Result_Map_Order_Log_GGFB_ByNgayThucHien] 	
	@FromDate = @FromDate,
	@ToDate = @ToDate

	EXEC [dbo].[Gen_InsertOrUpdate_Operating_Result_Quantity_GGFB_ByNgayThucHien] 	
	@FromDate = @FromDate,
	@ToDate = @ToDate

	EXEC [dbo].[Gen_InsertOrUpdate_Operating_Result_Quantity_Log_GGFB_ByNgayThucHien] 	
	@FromDate = @FromDate,
	@ToDate = @ToDate

END

```
