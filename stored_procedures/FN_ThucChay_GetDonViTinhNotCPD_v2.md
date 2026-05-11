# Function: `ThucChay_GetDonViTinhNotCPD_v2`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2025-03-07 17:11:23.090000
- **Ngày sửa cuối**: 2025-03-07 17:11:23.090000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(100)` | Yes |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@TenLoai` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql


				-- =============================================
create  FUNCTION [dbo].[ThucChay_GetDonViTinhNotCPD_v2]
(
	@DonViTinh nvarchar(50),
	@TenLoai NVARCHAR(50)= NULL
)
RETURNS NVARCHAR(50)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @DonViTinhChuan NVARCHAR(50)
	SET @DonViTinh = UPPER(LTRIM(RTRIM(@DonViTinh)))

	IF @TenLoai IS NULL
	BEGIN   
		SET @DonViTinhChuan = (
				CASE 
					 WHEN @DonViTinh = 'CPM' THEN 'VIEW'
					 WHEN @DonViTinh = N'TRUE REACH' THEN 'VIEW'
					 WHEN @DonViTinh = 'CPC' THEN 'CLICK'
					 WHEN (
							  @DonViTinh = N'BÀI'
							  OR @DonViTinh = N'GÓI'
							  OR @DonViTinh = N'Ð/V'
						  ) THEN @DonViTinh
					 ELSE @DonViTinh
				END
			)
	END
	ELSE -- trangtth 
	BEGIN
	    SET @DonViTinhChuan = (
				CASE	WHEN @DonViTinh = 'CPC'
						THEN 'CLICK'
						WHEN @DonViTinh = 'CPM'
						THEN 'VIEW'
						WHEN @DonViTinh = 'CPV'
						THEN 'CPV'
						ELSE (  CASE
								WHEN @DonViTinh = N'Gói' AND @TenLoai = 'CPC'
								THEN 'CLICK'
								WHEN @DonViTinh = N'Gói' AND @TenLoai = 'CPM'
								THEN 'VIEW'
								ELSE @DonViTinh
								END )
                END  )
	END
	RETURN @DonViTinhChuan

END

```
