# Stored Procedure: `ThucChayDaTinhAdX_Delete`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 14:54:00.867000
- **Ngày sửa cuối**: 2015-02-06 11:44:47.627000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinhAdX_Delete]
	-- Add the parameters for the stored procedure here
	@StartDate datetime
AS
BEGIN
	    
	delete from ThucChayDaTinhAdX 
	where 
	Convert(date,NgayThucHien) >=Convert(date,@StartDate)
	
	delete from ThucChayDaTinhAdXForDomain
	where 
	Convert(date,NgayThucHien) >=Convert(date,@StartDate)	
END
```
