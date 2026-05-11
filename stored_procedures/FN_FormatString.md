# Function: `FormatString`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-09 04:23:47.187000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.273000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(100)` | Yes |
| `@TenField` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION FormatString
(
	-- Add the parameters for the function here
	@TenField nvarchar(50)
)
RETURNS nvarchar(50)
AS
BEGIN


	-- Return the result of the function
	RETURN RTrim(LTrim(@TenField))

END

```
