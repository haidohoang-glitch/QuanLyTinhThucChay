# Function: `ThucChay_GetDonViTinhNotCPD`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-03-11 16:13:34.767000
- **Ngày sửa cuối**: 2018-08-28 14:42:49.110000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(100)` | Yes |
| `@DonViTinh` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE  FUNCTION [dbo].[ThucChay_GetDonViTinhNotCPD]
(
	-- Add the parameters for the function here
	@DonViTinh nvarchar(50)
)
RETURNS NVARCHAR(50)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @DonViTinhChuan NVARCHAR(50)
	SET @DonViTinh = UPPER(LTRIM(RTRIM(@DonViTinh)))
	SET @DonViTinhChuan = (
	        CASE 
	             WHEN @DonViTinh = 'CPM' THEN 'VIEW'
	             WHEN @DonViTinh = 'CPC' THEN 'CLICK'
	             WHEN (
	                      @DonViTinh = N'BÀI'
	                      OR @DonViTinh = N'GÓI'
	                      OR @DonViTinh = N'Ð/V'
	                  ) THEN @DonViTinh
	             ELSE @DonViTinh
	        END
	    )
	
	-- Return the result of the function
	RETURN @DonViTinhChuan

END

```
