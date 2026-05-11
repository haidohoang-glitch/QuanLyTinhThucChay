# Stored Procedure: `TablePaging_Select`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-06 18:20:13.050000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.403000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@LastModifiedBy` | `nvarchar(100)` | No |
| `@TableName` | `nvarchar(100)` | No |
| `@IsManager` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[TablePaging_Select]
	-- Add the parameters for the stored procedure here
	@PageIndex Int,
	@RecordCount Int,
	@LastModifiedBy nvarchar(50),
	@TableName nvarchar(50),
	@IsManager int
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
    -- statements for procedure here
	declare @StartIndex Int
	declare @MaxRecords Int
	declare @i Int
	declare @PageCount Int
	declare @ApproximatedNumber float
	declare @SQL nvarchar(2000)

	set @ApproximatedNumber=0.49999
	set @i=1

	set @SQL = 
	CASE @TableName
	  WHEN 'TienAnCa' THEN 
		'select @MaxRecords=count(distinct Thang) from TienAnCa where [DeletedStatus] <> 1'
		ELSE 
		'select @MaxRecords=count(*) from '+ @TableName+' where [DeletedStatus] <> 1'
	END

	if(@IsManager <> 1)
	begin
		set @SQL = @SQL + 'and LastModifiedBy = ' + ''''+ @LastModifiedBy + ''''
	end
	

	EXEC sp_executesql @SQL, N'@MaxRecords int output', @MaxRecords output
	
	set @PageCount = round(convert(float,@MaxRecords)/@RecordCount+@ApproximatedNumber,0)
	SET @StartIndex = (@PageIndex - 1)*@RecordCount + 1
	Set @MaxRecords = @PageIndex*@RecordCount	


	if(@IsManager=1)		
		if(@PageCount>=@PageIndex)
			set @SQL = 	'SELECT * FROM 
			(SELECT *, ROW_NUMBER() OVER(ORDER BY LastModifiedAt DeSC) AS rownum from '+@TableName+' where [DeletedStatus] <> 1 and [DeletedStatus] <> 3) as VitualTable '+
			'WHERE rownum between '+ Convert(nvarchar(50),@StartIndex) + ' and ' + Convert(nvarchar(50),@MaxRecords)
		else
			set @SQL = 	'SELECT * FROM '+@TableName + ' where [DeletedStatus] <> 1 and [DeletedStatus] <> 3'
	else
		if(@PageCount>=@PageIndex)
			set @SQL = 	'SELECT * FROM 
			(SELECT *, ROW_NUMBER() OVER(ORDER BY LastModifiedAt DeSC) AS rownum from '+@TableName+' where [DeletedStatus] <> 1 and [DeletedStatus] <> 3 and LastModifiedBy = '+'''' +@LastModifiedBy+'''' +') as VitualTable '+
			'WHERE rownum between '+ Convert(nvarchar(50),@StartIndex) + ' and ' + Convert(nvarchar(50),@MaxRecords)
		else
			set @SQL = 'select * from '+@TableName+' where [DeletedStatus] <> 1 and [DeletedStatus] <> 3 and LastModifiedBy = ' +''''+ @LastModifiedBy +''''	

	EXEC sp_executesql @SQL


END

```
