# Function: `ThucChay_GetDonGiaChuanTheoDonViTinh_doanhso`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-11-27 10:13:54.950000
- **Ngày sửa cuối**: 2014-10-14 10:39:32.353000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@SoLuong` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@DonGia` | `float(8)` | No |
| `@NgayKyHopDong` | `datetime(8)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietID` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetDonGiaChuanTheoDonViTinh_doanhso]
(
	-- Add the parameters for the function here
	@SoLuong INT, 
	@DonViTinh nvarchar(50), 
	@DonGia FLOAT,
	@NgayKyHopDong DATETIME,
	@NgayThucHien datetime,
	@HopDongChiTietID nvarchar(50)	
)
RETURNS FLOAT
AS
BEGIN
	set @DonGia = dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,@HopDongChiTietID,@DonGia)
	-- Declare the return variable here
	DECLARE @DonGiaTheoDonVi FLOAT
	DECLARE @SoNgayTheoDonViTinh INT 
	SET @DonViTinh = UPPER(LTRIM(RTRIM(@DonViTinh)))
	
	IF(@DonViTinh = 'CPM' or @DonViTinh = 'CPC')
	BEGIN
		SET @DonGiaTheoDonVi = @DonGia/1000
	END
	ELSE
		IF(@DonViTinh = N'BÀI')
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
				
				SET @SoNgayTheoDonViTinh = dbo.ThucChay_GetSoLuongChuanTheoDonViTinh_doanhso(@SoLuong, @DonViTinh, @HopDongChiTietID) 
				
				IF (@SoNgayTheoDonViTinh = 0)
					SET @DonGiaTheoDonVi = 0
				ELSE
					SET @DonGiaTheoDonVi = ROUND((@SoLuong*@DonGia) / @SoNgayTheoDonViTinh,2)
			END
	-- Return the result of the function
	RETURN @DonGiaTheoDonVi

END

```
