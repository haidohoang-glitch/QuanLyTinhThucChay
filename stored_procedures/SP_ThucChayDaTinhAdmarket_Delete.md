# Stored Procedure: `ThucChayDaTinhAdmarket_Delete`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 14:54:00.713000
- **Ngày sửa cuối**: 2015-06-26 13:33:41.183000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinhAdmarket_Delete]
	-- Add the parameters for the stored procedure here
	@StartDate datetime
	,@DmSanPhamREF int
AS
BEGIN
	Declare @DmSanPhamREFWell int
	
	SET @DmSanPhamREFWell = (
	        CASE @DmSanPhamREF
	             WHEN 5001 THEN 144
	             WHEN 5002 THEN 299
	             WHEN 5003 THEN 337
	             WHEN 5004 THEN 375
	             else
	             @DmSanPhamREF
	        END
	    ) 
	    
	delete from ThucChayDaTinh 
	where 
	Convert(date,NgayThucHien) =Convert(date,@StartDate)
	and DmSanPhamREF = @DmSanPhamREFWell
END

```
