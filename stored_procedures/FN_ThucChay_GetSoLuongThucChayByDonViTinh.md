# Function: `ThucChay_GetSoLuongThucChayByDonViTinh`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-05-29 09:18:16.480000
- **Ngày sửa cuối**: 2014-10-14 10:39:31.003000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@TongViewThucChay` | `float(8)` | No |
| `@TongClickThucChay` | `float(8)` | No |
| `@TongSoBaiViet` | `float(8)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetSoLuongThucChayByDonViTinh] 
(
	-- Add the parameters for the function here
	@TongViewThucChay FLOAT,
	@TongClickThucChay FLOAT,
	@TongSoBaiViet FLOAT,
	@DonViTinh NVARCHAR(50)
)
RETURNS FLOAT
AS
BEGIN
	DECLARE @SoLuongThucChay FLOAT
	SET @DonViTinh = UPPER(LTRIM(RTRIM(@DonViTinh)))
	
	IF(@DonViTinh = N'BÀI')--PR
		SET @SoLuongThucChay = @TongSoBaiViet
	ELSE--CPC
		IF(@DonViTinh = N'CPC' OR @DonViTinh = N'GÓI')
			SET @SoLuongThucChay = @TongClickThucChay
		ELSE--CPD
			IF(@DonViTinh = N'TUẦN' OR @DonViTinh = N'THÁNG' OR @DonViTinh = N'NGÀY' OR @DonViTinh = N'NĂM')	
			BEGIN		
				IF(@TongViewThucChay>5000)
					SET  @SoLuongThucChay = 1
				ELSE
					SET  @SoLuongThucChay = 0
			END
			ELSE --CPM
				SET  @SoLuongThucChay = @TongViewThucChay
	-- Return the result of the function
	RETURN @SoLuongThucChay

END

```
