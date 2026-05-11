# Function: `ThucChay_GetDonGiaTheoDonViTinh`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-05-29 08:21:38.510000
- **Ngày sửa cuối**: 2014-10-14 10:39:32.250000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@SoLuong` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@DonGia` | `float(8)` | No |
| `@NgayKyHopDong` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetDonGiaTheoDonViTinh]
(
	-- Add the parameters for the function here
	@SoLuong INT, 
	@DonViTinh nvarchar(50), 
	@DonGia FLOAT,
	@NgayKyHopDong datetime
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @DonGiaTheoDonVi FLOAT
	DECLARE @SoNgayTheoDonViTinh INT 
	SET @DonViTinh = UPPER(LTRIM(RTRIM(@DonViTinh)))
	
	IF(@DonViTinh = 'CPM' or @DonViTinh = 'CPC')
	BEGIN
		SET @DonGiaTheoDonVi = @DonGia/1000
	END
	ELSE
		IF(@DonViTinh = 'PR')
		BEGIN
			SET @DonGiaTheoDonVi = @DonGia
		END
		ELSE
			IF(@DonViTinh = 'GOI')
			BEGIN
				SET @SoLuong = 5000
				SET @DonGiaTheoDonVi = @DonGia
			END
			ELSE			
			BEGIN
				SET @SoNgayTheoDonViTinh = 
				CASE @DonViTinh
					 WHEN N'TUẦN' THEN 7
					 WHEN N'THÁNG' THEN dbo.GetDaysInMonth(@NgayKyHopDong)
					 WHEN N'NĂM' THEN dbo.GetDaysInYear(@NgayKyHopDong)
					 ELSE 1
				END		
				SET @DonGiaTheoDonVi = ROUND(@DonGia / @SoNgayTheoDonViTinh,2)
			END
	-- Return the result of the function
	RETURN @DonGiaTheoDonVi

END

```
