# Function: `ThucChay_GetThanhTienChuanThucChay_Admatic`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2016-12-05 10:32:27.090000
- **Ngày sửa cuối**: 2019-11-09 10:00:59.517000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@SoLuongHD` | `bigint(8)` | No |
| `@DonGiaHD` | `float(8)` | No |
| `@ThanhTien` | `float(8)` | No |
| `@ChietKhau` | `float(8)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@DonGia` | `float(8)` | No |
| `@NgayKyHopDong` | `datetime(8)` | No |
| `@TongViewThucChay` | `float(8)` | No |
| `@TongClickThucChay` | `float(8)` | No |
| `@TongTrueViewThucChay` | `float(8)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietID` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetThanhTienChuanThucChay_Admatic]
(
	-- Add the parameters for the function here
	@SoLuongHD BIGINT, 
	@DonGiaHD FLOAT,	
	@ThanhTien FLOAT,	
	@ChietKhau FLOAT,
	@DonViTinh NVARCHAR(50), 
	@DonGia FLOAT,
	@NgayKyHopDong DATETIME,
	@TongViewThucChay FLOAT,
	@TongClickThucChay FLOAT,
	@TongTrueViewThucChay FLOAT,
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
	DECLARE @intHopDongChiTietID INT, @ChenhLechTienThucChay FLOAT =0
	set @intHopDongChiTietID = CONVERT(INT, @HopDongChiTietID) 
	
	SET @DonViTinh = UPPER(@DonViTinh)
	IF(@DonViTinh = 'CPM')--TINH THUC CHAY THEO VIEW
	BEGIN
		SET @DonGiaTheoDonVi = @DonGia/1000 --Don vi tinh theo CPM
		SET @SoLuongThucChay = [dbo].[ThucChay_GetSoLuongThucChay_Admatic_v1] (	@TongViewThucChay ,	@TongClickThucChay, @TongTrueViewThucChay ,@DonGia,@DonViTinh ,@NgayThucHien 
		,	@intHopDongChiTietID,@SoLuongHD ,@DonGiaHD ,	@ThanhTien ,	@ChietKhau )
	END
	IF(@DonViTinh = 'CPC')--TINH THUC CHAY THEO CLICK
	BEGIN
		SET @DonGiaTheoDonVi = @DonGia --Don vi tinh theo CPC
		SET @SoLuongThucChay = [dbo].[ThucChay_GetSoLuongThucChay_Admatic_v1] (	@TongViewThucChay ,	@TongClickThucChay , @TongTrueViewThucChay,@DonGia,@DonViTinh ,@NgayThucHien 
		,	@intHopDongChiTietID,@SoLuongHD ,@DonGiaHD ,	@ThanhTien ,	@ChietKhau )
	END
	IF(@DonViTinh = 'TRUE VIEW')--TINH THUC CHAY THEO True View
	BEGIN
		SET @DonGiaTheoDonVi = @DonGia --Don vi tinh theo True View
		SET @SoLuongThucChay = [dbo].[ThucChay_GetSoLuongThucChay_Admatic_v1] (	@TongViewThucChay ,	@TongClickThucChay,@TongTrueViewThucChay ,@DonGia,@DonViTinh ,@NgayThucHien 
		,	@intHopDongChiTietID,@SoLuongHD ,@DonGiaHD ,	@ThanhTien ,	@ChietKhau )
	END
	
	SET @DonGiaTheoDonVi = ISNULL(@DonGiaTheoDonVi,0)
	SET @SoLuongThucChay = ISNULL(@SoLuongThucChay,0)

	SET @ThanhTienThucChay = @DonGiaTheoDonVi * @SoLuongThucChay
	--HAIDH :TH HOP DONG TINH LE GIA TRI THUC CHAY (DONGIA*1 > SO TIEN CHENH LECH)
	SET @ChenhLechTienThucChay = 
	(
		SELECT SUM(ThanhTien-ThanhtienThucChay) 
		FROM dbo.AdmaticThuTuChayHopDongChiTiet 
		WHERE HopDongChiTietID = @intHopDongChiTietID
	)
	IF (@ChenhLechTienThucChay <100 AND @ChenhLechTienThucChay >0 AND @SoLuongThucChay =0)
		SET @ThanhTienThucChay = @ChenhLechTienThucChay

	RETURN @ThanhTienThucChay

END

```
