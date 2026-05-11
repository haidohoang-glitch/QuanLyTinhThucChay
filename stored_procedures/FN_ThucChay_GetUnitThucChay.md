# Function: `ThucChay_GetUnitThucChay`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-12-04 12:11:52.297000
- **Ngày sửa cuối**: 2014-12-04 12:11:52.297000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(100)` | Yes |
| `@sanPhamId` | `int(4)` | No |
| `@donViTinh` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-11-18
-- Description:	Get unit name thucchay by unit name from contract
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetUnitThucChay]
(
	-- Add the parameters for the function here
	@sanPhamId		INT,
	@donViTinh		NVARCHAR(50)
)
RETURNS NVARCHAR(50)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @return	NVARCHAR(50)
	
	IF (@donViTinh = N'Ngày' OR @donViTinh =  N'Tuần' OR @donViTinh = N'Tháng')
		SET @return = N'Ngày'
	ELSE 
		SET @return = @donViTinh

	-- Return the result of the function
	RETURN @return

END

```
