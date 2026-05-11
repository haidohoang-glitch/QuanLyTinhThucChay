# Function: `ThucChay_GetThanhTienChuanThucChay_CPR_ByDVT_CPR`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-12-11 11:29:52.270000
- **Ngày sửa cuối**: 2016-04-20 13:43:30.877000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@DonViTinh` | `nvarchar(200)` | No |
| `@DonGia` | `float(8)` | No |
| `@SoLuong` | `int(4)` | No |
| `@UV` | `int(4)` | No |
| `@UVNgay` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetThanhTienChuanThucChay_CPR_ByDVT_CPR]
(
	-- Add the parameters for the function here
	@DonViTinh      NVARCHAR(100),
	@DonGia            FLOAT,
	@SoLuong           INT,
	@UV                INT,
	@UVNgay	   INT,
	@HopDongChiTietID  INT,
	@NgayThucHien      DATETIME
)
RETURNS FLOAT
AS

BEGIN
	-- Declare the return variable here
	DECLARE @ThanhTienThucChay      FLOAT,
			@UVThucChayNgay INT=0
	        
	        
	SET @UVThucChayNgay = [dbo].[ThucChay_GetSoLuongThucChayChuanByDonViTinh_CPR] 
	(@UV,@UVNgay
	,@SoLuong,@DonViTinh, @NgayThucHien, @HopDongChiTietID)
	IF (@DonViTinh = 'CPR')
	BEGIN
		SET @ThanhTienThucChay = @UVThucChayNgay * @DonGia

	END
	
	SET @ThanhTienThucChay = ISNULL(@ThanhTienThucChay, 0)
	RETURN @ThanhTienThucChay
END



```
