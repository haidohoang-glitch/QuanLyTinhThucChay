# Stored Procedure: `mytest`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-08 11:23:14.523000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.710000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@varname` | `nvarchar(200)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[mytest]
	-- Add the parameters for the stored procedure here
	@varname nvarchar(100)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT @varname;
END

```
