# Stored Procedure: `GetJoinTables`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-23 08:52:32.773000
- **Ngày sửa cuối**: 2014-11-19 12:16:54.180000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TableName` | `nvarchar(100)` | No |
| `@JoinedFieldName1` | `nvarchar(100)` | No |
| `@JoinedFieldName2` | `nvarchar(100)` | No |
| `@JoinedFieldName3` | `nvarchar(100)` | No |
| `@JoinedFieldName4` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[GetJoinTables] 
	-- Add the parameters for the stored procedure here
	@TableName nvarchar(50),
	@JoinedFieldName1 nvarchar(50),
	@JoinedFieldName2 nvarchar(50),
	@JoinedFieldName3 nvarchar(50),
	@JoinedFieldName4 nvarchar(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	Declare @FieldName nvarchar(50), @SQL nvarchar(4000), @SQLSelect nvarchar(4000),@SQLCondition nvarchar(4000),@SQLLeftJoin nvarchar(4000)
	Declare	@FieldList nvarchar(4000)

	Declare @JoindedTableName1 nvarchar(50),@JoindedTableName2 nvarchar(50),@JoindedTableName3 nvarchar(50),@JoindedTableName4 nvarchar(50)
	Declare @JoindedTableID1 nvarchar(50),@JoindedTableID2 nvarchar(50),@JoindedTableID3 nvarchar(50),@JoindedTableID4 nvarchar(50)

	Declare @JoindedFieldList1 nvarchar(4000),@JoindedFieldList2 nvarchar(4000),@JoindedFieldList3 nvarchar(4000),@JoindedFieldList4 nvarchar(4000)	
	
	set @JoindedTableName1 = dbo.GetTableNameFromForeignKey(@JoinedFieldName1)
	set @JoindedTableID1 = @JoindedTableName1 + 'ID'

	set @JoindedTableName2 = dbo.GetTableNameFromForeignKey(@JoinedFieldName2)
	set @JoindedTableID2 = @JoindedTableName2 + 'ID'	

	set @JoindedTableName3 = dbo.GetTableNameFromForeignKey(@JoinedFieldName3)
	set @JoindedTableID3 = @JoindedTableName3 + 'ID'

	set @JoindedTableName4 = dbo.GetTableNameFromForeignKey(@JoinedFieldName4)
	set @JoindedTableID4 = @JoindedTableName4 + 'ID'

	
	exec GetAllColumnsByTableName @TableName,@FieldList out

	set @SQLSelect = 'select ' + @FieldList 
	set @SQLCondition = ' where ' + @TableName + '.DeletedStatus <> 1'	
	set @SQLLeftJoin = ' from ' + @TableName 


	if(@JoindedTableName1<>'')
	Begin
		exec GetAllColumnsByTableName @JoindedTableName1,@JoindedFieldList1 out
		set @JoindedFieldList1 = dbo.GetCommonFieldFromTable(@JoindedFieldList1)
		set @SQLSelect = @SQLSelect + ',' + @JoindedFieldList1
		set @SQLLeftJoin = @SQLLeftJoin +  ' left join ' + @JoindedTableName1 + ' on ' + @JoindedTableName1 + '.' + @JoindedTableID1 + '=' +@TableName+'.'+@JoinedFieldName1
		set @SQLCondition = @SQLCondition + ' and ' + @JoindedTableName1+'.DeletedStatus<>1'
	End

	if(@JoindedTableName2<>'')
	Begin
		exec GetAllColumnsByTableName @JoindedTableName2,@JoindedFieldList2 out
		set @JoindedFieldList2 = dbo.GetCommonFieldFromTable(@JoindedFieldList2)
		set @SQLSelect = @SQLSelect + ',' + @JoindedFieldList2
		set @SQLLeftJoin = @SQLLeftJoin +  ' left join ' + @JoindedTableName2 + ' on ' + @JoindedTableName2 + '.' + @JoindedTableID2 + '=' +@TableName+'.'+@JoinedFieldName2
		set @SQLCondition = @SQLCondition + ' and ' + @JoindedTableName2+'.DeletedStatus<>1'
	End


	if(@JoindedTableName3<>'')
	Begin
		exec GetAllColumnsByTableName @JoindedTableName3,@JoindedFieldList3 out
		set @JoindedFieldList3 = dbo.GetCommonFieldFromTable(@JoindedFieldList3)
		set @SQLSelect = @SQLSelect + ',' + @JoindedFieldList3
		set @SQLLeftJoin = @SQLLeftJoin +  ' left join ' + @JoindedTableName3 + ' on ' + @JoindedTableName3 + '.' + @JoindedTableID3 + '=' +@TableName+'.'+@JoinedFieldName3
		set @SQLCondition = @SQLCondition + ' and ' + @JoindedTableName3+'.DeletedStatus<>1'
	End

	if(@JoindedTableName4<>'')
	Begin
		exec GetAllColumnsByTableName @JoindedTableName1,@JoindedFieldList4 out
		set @JoindedFieldList4 = dbo.GetCommonFieldFromTable(@JoindedFieldList4)
		set @SQLSelect = @SQLSelect + ',' + @JoindedFieldList4
		set @SQLLeftJoin = @SQLLeftJoin +  ' left join ' + @JoindedTableName4 + ' on ' + @JoindedTableName4 + '.' + @JoindedTableID4 + '=' +@TableName+'.'+@JoinedFieldName4
		set @SQLCondition = @SQLCondition + ' and ' + @JoindedTableName4+'.DeletedStatus<>1'
	End


	set @SQL = @SQLSelect + @SQLLeftJoin + @SQLCondition

	exec(@SQL)


END

--exec [dbo].[GetJoinTables] 'SysNoiDungWebsite','DmNgonNguREF','SysChucNangFK','SysLoaiTinTucREF',''

--exec [dbo].[GetJoinTables] 'SysNoiDungWebsite','','','',''

```
