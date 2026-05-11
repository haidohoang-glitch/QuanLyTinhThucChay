# Stored Procedure: `GetMaxLastModifiedAtByDeletedStatus`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-07-22 16:54:32.413000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.980000

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
CREATE PROCEDURE [dbo].[GetMaxLastModifiedAtByDeletedStatus]
	-- Add the parameters for the stored procedure here
	@TableName nvarchar(50)
AS
BEGIN
	Declare @SQLCommand nvarchar(4000)
	set @SQLCommand = 'Select Dateadd(day,-7,MAX(LastModifiedAt)) from ' + @TableName + ' Where DeletedStatus = 1 '
	
	
	exec(@SQLCommand)
END

```
