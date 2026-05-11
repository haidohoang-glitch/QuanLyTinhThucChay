# Function: `ThucChay_GetSoLuong_DonViTinh`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-07-01 11:38:03.477000
- **Ngày sửa cuối**: 2014-10-14 10:39:31.810000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@SoLuong` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- ALTER date: <ALTER Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetSoLuong_DonViTinh]
(
	-- Add the parameters for the function here
	@SoLuong INT, 
	@DonViTinh nvarchar(50) 
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @SoNgayTheoDonViTinh INT 
	DECLARE @SoLuongDonViTinh BIGINT 
	SET @DonViTinh = UPPER(LTRIM(RTRIM(@DonViTinh)))
	
	IF(@DonViTinh = 'CPM' or @DonViTinh = 'CPC')
	BEGIN
		SET @SoNgayTheoDonViTinh = 1000
	END
	ELSE
		IF(@DonViTinh = 'PR')
		BEGIN
			SET @SoNgayTheoDonViTinh = 1
		END
		ELSE
			IF(@DonViTinh = 'GOI')
			BEGIN
				SET @SoNgayTheoDonViTinh = 5000
			END
			ELSE			
			BEGIN
				SET @SoNgayTheoDonViTinh = 
				CASE @DonViTinh
					 WHEN N'TUẦN' THEN 7
					 WHEN N'THÁNG' THEN 30
					 WHEN N'NĂM' THEN 365
					 ELSE 1
				END		
			END
	-- Return the result of the function
	SET @SoLuongDonViTinh = @SoNgayTheoDonViTinh * @SoLuong
	RETURN @SoLuongDonViTinh

END

```
