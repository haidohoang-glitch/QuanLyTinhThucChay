# Function: `FormatStringUpper`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-09 04:57:11.920000
- **Ngày sửa cuối**: 2017-05-26 09:55:35.680000

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
CREATE FUNCTION [dbo].[FormatStringUpper]
(
	-- Add the parameters for the function here
	@TenField nvarchar(50)
)
RETURNS nvarchar(50)
AS
BEGIN


	-- Return the result of the function
	RETURN Upper((RTrim(LTrim(@TenField))))

END

```
