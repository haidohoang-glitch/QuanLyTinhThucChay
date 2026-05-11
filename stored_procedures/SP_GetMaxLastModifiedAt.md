# Stored Procedure: `GetMaxLastModifiedAt`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-01 21:10:48.157000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.983000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TableName` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[GetMaxLastModifiedAt]
	-- Add the parameters for the stored procedure here
	@TableName nvarchar(50)
AS
BEGIN
	Declare @SQLCommand nvarchar(4000)
	--set @SQLCommand = 'Select Dateadd(hour,-8,MAX(LastModifiedAt)) from ' + @TableName + ' Where DeletedStatus <> 1 '
	
	set @SQLCommand = 'Select Dateadd(day,-1,MAX(LastModifiedAt)) from ' + @TableName + ' Where DeletedStatus <> 1 '
	
	exec(@SQLCommand)
END


--EXEC [GetMaxLastModifiedAt] 'HopDong'

```
