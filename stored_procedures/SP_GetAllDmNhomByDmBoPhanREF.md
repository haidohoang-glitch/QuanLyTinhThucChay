# Stored Procedure: `GetAllDmNhomByDmBoPhanREF`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-07 09:38:38.107000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.853000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmBoPhanREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[GetAllDmNhomByDmBoPhanREF]
	-- Add the parameters for the stored procedure here
	@DmBoPhanREF int
AS
BEGIN
	select * from dbo.DmNhom where DmBoPhanREF = @DmBoPhanREF and DeletedStatus <> 1
END


--exec [GetAllTableForComboBox] 'DmNgonNgu','','TenNgonNgu'

```
