# Function: `GetDonViTinhAdmarketByDmSanPhamREF`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-09-06 10:40:51.083000
- **Ngày sửa cuối**: 2014-10-14 10:39:36.513000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(100)` | Yes |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[GetDonViTinhAdmarketByDmSanPhamREF]
(
	-- Add the parameters for the function here
	@DmSanPhamREF INT
)
RETURNS NVARCHAR(50)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @DonViTinh NVARCHAR(50)
	
	SET @DonViTinh = ''
	
	IF(@DmSanPhamREF = 144 OR @DmSanPhamREF = 299)SET @DonViTinh = 'CPC'
	ELSE
		IF(@DmSanPhamREF = 337 OR @DmSanPhamREF = 370)SET @DonViTinh = 'View'
	
	-- Return the result of the function
	RETURN @DonViTinh

END

```
