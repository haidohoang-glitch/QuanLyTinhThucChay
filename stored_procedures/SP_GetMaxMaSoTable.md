# Stored Procedure: `GetMaxMaSoTable`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-23 08:52:30.820000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.003000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TableName` | `nvarchar(100)` | No |
| `@ColumnName` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
--exec [GetMaxMaSoTable] 'DmNgonNgu','MaNgonNgu'
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[GetMaxMaSoTable] 
	-- Add the parameters for the stored procedure here
	@TableName nvarchar(50),
	@ColumnName nvarchar(50)	
AS
BEGIN
	Declare @MaSo nvarchar(50)
	Declare @MaxMaSo int
	Declare @SQL nvarchar(4000)

	set @SQL = 'select @MaxMaSo=Max(Convert(int,'+@ColumnName+')) from '+ @TableName+' where [DeletedStatus] <> 1' 
	EXEC sp_executesql @SQL, N'@MaxMaSo int output', @MaxMaSo output

	if(@MaxMaSo is null)
		set @MaxMaSo = 1
	else
		set @MaxMaSo = @MaxMaSo +1

	if(@MaxMaSo/10 >=1)
		set @MaSo = Convert(varchar(10),@MaxMaSo)
	else
		set @MaSo = convert(varchar(1),'0')+convert(varchar(1),@MaxMaSo)

	select @MaSo 

END

```
