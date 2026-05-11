# Stored Procedure: `GetAllTable`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-23 08:52:30.590000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.610000

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
CREATE PROCEDURE [dbo].[GetAllTable] 
	-- Add the parameters for the stored procedure here
	@TableName nvarchar(50)
AS
BEGIN
	Declare @SQLCommand nvarchar(4000)
	set @SQLCommand = 'Select * from '+@TableName+' Where DeletedStatus <> 1 Order By LastModifiedAt Desc'
	exec(@SQLCommand)
END

```
