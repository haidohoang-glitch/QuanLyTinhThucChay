# Function: `ConCatPhongBan`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-07 18:52:37.780000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.820000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar` | Yes |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ConCatPhongBan]
(
	-- Add the parameters for the function here
	
)
RETURNS nvarchar(max)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ReturnValue nvarchar(max)

	-- Add the T-SQL statements to compute the return value here
	SET @ReturnValue = (SELECT
    stuff(
    (
    select cast(',' as varchar(max)) + U.TenPhongBan
    from DmPhongBan U
    order by U.TenPhongBan
    for xml path('') 
    ), 1, 1, '') AS TenPhongBan
    )

	-- Return the result of the function
	RETURN @ReturnValue

END

```
