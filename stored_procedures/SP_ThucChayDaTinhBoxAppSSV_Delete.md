# Stored Procedure: `ThucChayDaTinhBoxAppSSV_Delete`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 14:53:57.197000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.690000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinhBoxAppSSV_Delete]
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime
AS
BEGIN
	Declare @DmSanPhamREFWell int
	
	    
	delete from  dbo.ThucChayDaTinhBoxAppSSV
	where 
	Convert(date,NgayThucHien) >=Convert(date,@NgayThucHien)
	and DmSanPhamREF = 375
	
END

```
