# Stored Procedure: `GetAllColumnsByTableName`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-23 08:52:30.643000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.307000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TableName` | `nvarchar(100)` | No |
| `@FieldNameList` | `nvarchar(8000)` | Yes |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE PROCEDURE [dbo].[GetAllColumnsByTableName] 
(
	-- Add the parameters for the function here
	@TableName nvarchar(50),	
	@FieldNameList nvarchar(4000) out
)

AS
BEGIN
Declare @TableColumn Table
(
	[Name] nvarchar(50)
)
Declare @SQLCommand nvarchar(4000)
Declare @DauNhay nvarchar(50)
Declare @FieldName nvarchar(4000)

Declare @PreTable nvarchar(50)

set @PreTable = @TableName + '.'

set @DauNhay = ''''

set @SQLCommand = '
SELECT [name] 
FROM syscolumns
WHERE 

id = (SELECT id
FROM sysobjects
WHERE type = ' + @DauNhay + 'U' + @DauNhay +
'AND [NAME] = ' + @DauNhay + @TableName + @DauNhay + '
)
and [NAME] <> ' + @DauNhay + @TableName + 'ID' + @DauNhay


Insert into @TableColumn exec(@SQLCommand)

DECLARE Record_Cursor CURSOR FOR 
							Select * from @TableColumn
OPEN Record_Cursor
FETCH NEXT FROM Record_Cursor into @FieldName

set @FieldNameList = @PreTable + @TableName + 'ID'
WHILE @@FETCH_STATUS = 0
BEGIN
set @FieldNameList = @FieldNameList + ',' + @PreTable + @FieldName 
FETCH NEXT FROM Record_Cursor into @FieldName
END

CLOSE Record_Cursor
DEALLOCATE Record_Cursor



END

```
