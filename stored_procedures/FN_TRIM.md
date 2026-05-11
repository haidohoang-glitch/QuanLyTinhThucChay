# Function: `TRIM`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-09-03 17:20:14.303000
- **Ngày sửa cuối**: 2014-10-14 10:39:28.710000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar` | Yes |
| `@InpurtString` | `nvarchar` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-09-03
-- Description:	Trim space
-- =============================================
CREATE FUNCTION [dbo].[TRIM]
(
	-- Add the parameters for the function here
	@InpurtString NVARCHAR(MAX)
)
RETURNS NVARCHAR(MAX)
AS
BEGIN
	-- Return the result of the function
	RETURN LTRIM(RTRIM(@InpurtString))

END

```
