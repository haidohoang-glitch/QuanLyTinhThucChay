# Stored Procedure: `GetAllDataBySQLCommand`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-23 08:52:30.610000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.600000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SQLCommand` | `nvarchar(8000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[GetAllDataBySQLCommand] 
	-- Add the parameters for the stored procedure here
	@SQLCommand nvarchar(4000)
AS
BEGIN
	exec(@SQLCommand)
END

```
