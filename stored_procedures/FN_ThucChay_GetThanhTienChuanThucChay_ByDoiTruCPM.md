# Function: `ThucChay_GetThanhTienChuanThucChay_ByDoiTruCPM`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2023-08-15 15:56:18.813000
- **Ngày sửa cuối**: 2023-08-15 15:56:35.940000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@SoLuong` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@DonGia` | `float(8)` | No |
| `@NgayKyHopDong` | `datetime(8)` | No |
| `@TongViewThucChay` | `float(8)` | No |
| `@TongClickThucChay` | `float(8)` | No |
| `@TongSoBaiViet` | `float(8)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietID` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetThanhTienChuanThucChay_ByDoiTruCPM]
(
	-- Add the parameters for the function here
	@SoLuong INT, 
	@DonViTinh nvarchar(50), 
	@DonGia FLOAT,
	@NgayKyHopDong DATETIME,
	@TongViewThucChay FLOAT,
	@TongClickThucChay FLOAT,
	@TongSoBaiViet FLOAT,
	@NgayThucHien datetime,
	@HopDongChiTietID nvarchar(50)	
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ThanhTienThucChay FLOAT
	DECLARE @DonGiaTheoDonVi FLOAT
	DECLARE @SoLuongThucChay FLOAT
	DECLARE @intHopDongChiTietID INT
	set @intHopDongChiTietID = CONVERT(INT, @HopDongChiTietID) 
	
	SET @DonViTinh = UPPER(@DonViTinh)
	IF(@DonViTinh = 'CPM')--TINH THUC CHAY THEO VIEW
	BEGIN
		SET @DonGiaTheoDonVi = dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(@SoLuong,@DonViTinh,@DonGia,@NgayKyHopDong,@NgayThucHien,@HopDongChiTietID)
		--SET @SoLuongThucChay = dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh(@TongViewThucChay,@SoLuong,@DonViTinh, @NgayThucHien,@intHopDongChiTietID)	
		SET @SoLuongThucChay = dbo.[ThucChay_GetSoLuongThucChayChuanByDonViTinh_ByDoiTruCPM](@TongViewThucChay,@SoLuong,@DonViTinh, @NgayThucHien,@intHopDongChiTietID)
	END
	ELSE
		IF(@DonViTinh = 'CPC')--TINH THUC CHAY THEO CLICK
		BEGIN
			SET @DonGiaTheoDonVi = dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(@SoLuong,@DonViTinh,@DonGia,@NgayKyHopDong,@NgayThucHien,@HopDongChiTietID)
			--SET @SoLuongThucChay = dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh(@TongClickThucChay,@SoLuong,@DonViTinh, @NgayThucHien,@intHopDongChiTietID)
			SET @SoLuongThucChay = dbo.[ThucChay_GetSoLuongThucChayChuanByDonViTinh_ByDoiTruCPM](@TongClickThucChay,@SoLuong,@DonViTinh, @NgayThucHien,@intHopDongChiTietID)
		END
		ELSE
			BEGIN--CHO NAY CHUA BIET TINH THEO NAO CHO CAC SP KHAC
				SET @DonGiaTheoDonVi = dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(@SoLuong,@DonViTinh,@DonGia,@NgayKyHopDong,@NgayThucHien,@HopDongChiTietID)
				--SET @SoLuongThucChay = dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh(@TongClickThucChay,@SoLuong,@DonViTinh, @NgayThucHien,@intHopDongChiTietID)
				SET @SoLuongThucChay = dbo.[ThucChay_GetSoLuongThucChayChuanByDonViTinh_ByDoiTruCPM](@TongSoBaiViet,@SoLuong,@DonViTinh, @NgayThucHien,@intHopDongChiTietID)
			END
	
	
	SET @ThanhTienThucChay = @DonGiaTheoDonVi * @SoLuongThucChay
	

	RETURN @ThanhTienThucChay

END

```
