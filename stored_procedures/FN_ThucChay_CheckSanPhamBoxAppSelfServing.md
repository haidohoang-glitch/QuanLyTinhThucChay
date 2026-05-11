# Function: `ThucChay_CheckSanPhamBoxAppSelfServing`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-08-14 09:49:21.613000
- **Ngày sửa cuối**: 2014-10-14 10:39:33.873000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@DmSanPhamID` | `int(4)` | No |
| `@TenBanner` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-11-13
-- Description:	Check phân bổ là khuyến mại hay không
-- =============================================

--select [dbo].[ThucChay_CheckSanPhamBoxAppSelfServing] (370,'300x250')

CREATE FUNCTION [dbo].[ThucChay_CheckSanPhamBoxAppSelfServing] 
(
	@DmSanPhamID INT,
	@TenBanner NVARCHAR(50)
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @IsBoxAppSelfServing INT
	SET @IsBoxAppSelfServing = 0
	IF((@DmSanPhamID = 370)AND(@TenBanner IN ('300x250','300x385')))
		SET @IsBoxAppSelfServing = 1
	-- Return the result of the function
	RETURN @IsBoxAppSelfServing

END

```
