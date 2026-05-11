# Stored Procedure: `GetAllTableForComboBox`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-23 08:52:30.587000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.607000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TableName` | `nvarchar(100)` | No |
| `@TenMaSo` | `nvarchar(100)` | No |
| `@TenChiTiet` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[GetAllTableForComboBox] 
	-- Add the parameters for the stored procedure here
	@TableName nvarchar(50),
	@TenMaSo nvarchar(50),
	@TenChiTiet nvarchar(50)
AS
BEGIN
	Declare @SQLCommand nvarchar(4000)
	Declare @FieldList nvarchar(4000)
	set @FieldList = @TableName + 'ID'

	if(@TenMaSo <> '')
	Begin
		set @FieldList = @FieldList + ',' + @TenMaSo
	end
	if(@TenChiTiet <> '')
		set @FieldList = @FieldList + ',' + @TenChiTiet

	set @SQLCommand = 'Select '+ @FieldList + ' from '+@TableName+' Where DeletedStatus <> 1 Order By '+@TenChiTiet
	exec(@SQLCommand)
END


--exec [GetAllTableForComboBox] 'DmNgonNgu','','TenNgonNgu'

```
