# Stored Procedure: `Select_TablePageNumber`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-23 08:52:30.540000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.750000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@RecordCount` | `int(4)` | No |
| `@LastModifiedBy` | `nvarchar(100)` | No |
| `@TableName` | `nvarchar(100)` | No |
| `@IsManager` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Select_TablePageNumber] 
	-- Add the parameters for the stored procedure here
	@RecordCount Int,
	@LastModifiedBy nvarchar(50),
	@TableName nvarchar(50),
	@IsManager int
AS
BEGIN	
	declare @i Int
	declare @MaxRecords Int
	declare @PageCount Int
	declare @ApproximatedNumber float
	declare @SQL nvarchar(2000)

	declare @PageTable Table(
		PageIndex int,
		PageName nvarchar(50)
	)
	set @SQL = 'select @MaxRecords=count(*) from '+ @TableName+' where [DeletedStatus] <> 1' 
	set @ApproximatedNumber=0.49999
	set @i=1

	if(@IsManager <> 1)
	begin
		set @SQL = @SQL + 'and LastModifiedBy = ' + ''''+ @LastModifiedBy + ''''
	end

	EXEC sp_executesql @SQL, N'@MaxRecords int output', @MaxRecords output
	print @SQL
	set @PageCount = round(convert(float,@MaxRecords)/@RecordCount+@ApproximatedNumber,0)
	
	while(@i<=@PageCount)
	begin
		insert into @PageTable ([PageIndex],[PageName]) values (@i,Convert(nvarchar(50),@i))
		set @i = @i +1
	end
	insert into @PageTable ([PageIndex],[PageName]) values (@i,N'Tất cả')
	select [PageIndex],[PageName],@MaxRecords as MaxRecords from @PageTable
END



--exec [Select_TablePageNumber] '10','phuongld','DmNgonNgu','1'

```
