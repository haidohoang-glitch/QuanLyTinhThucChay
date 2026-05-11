# Stored Procedure: `CheckExitsTable`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-01 16:10:24.167000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.860000

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
CREATE PROCEDURE [dbo].[CheckExitsTable]
	-- Add the parameters for the stored procedure here
	@TableName nvarchar(50)
AS
BEGIN
IF (EXISTS (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = @TableName))
	select 1
else
	select 0
END

```
