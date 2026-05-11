# Function: `ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2017-09-11 15:02:50.350000
- **Ngày sửa cuối**: 2018-08-28 14:45:27.280000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@DonViTinh` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE  FUNCTION [dbo].[ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD]
(
	-- Add the parameters for the function here
	@DonViTinh nvarchar(50)
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @SoLuongTheoDonViTinh FLOAT
	SET @DonViTinh = UPPER(LTRIM(RTRIM(@DonViTinh)))
	SET @SoLuongTheoDonViTinh = (
	        CASE 
	             WHEN @DonViTinh = 'CPM' THEN 1000
				 WHEN @DonViTinh = 'TRUE REACH' THEN 1
	             WHEN (
	                      @DonViTinh = 'CPC'
	                      OR @DonViTinh = N'BÀI'
	                      OR @DonViTinh = N'GÓI'
	                      OR @DonViTinh = N'Ð/V'
	                      OR @DonViTinh = 'CPA'
	                      OR @DonViTinh = 'CPR'
						  OR @DonViTinh = 'TRUE VIEW'
	                  ) THEN 1
	             ELSE 1
	        END
	    )
	
	-- Return the result of the function
	RETURN @SoLuongTheoDonViTinh

END

--SELECT [dbo].[ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD]('VIEW')
```
