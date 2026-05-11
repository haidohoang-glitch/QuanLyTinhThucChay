# Function: `fn_CheckTienGoogleFacebook_Doannv`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-07-16 14:53:29.017000
- **Ngày sửa cuối**: 2015-07-24 14:44:43.417000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `nvarchar(100)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@DmLoaiBannerREF` | `nvarchar(100)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[fn_CheckTienGoogleFacebook_Doannv]
(
	-- Add the parameters for the function here
	@SoHopDong NVARCHAR(50),
	@DmSanPhamREF NVARCHAR(50),
	@NgayThucHien DATETIME,
	@DmLoaiBannerREF NVARCHAR(50),
	@DonViTinh NVARCHAR(50)
)
RETURNS INT 
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ResultVar INT SET @ResultVar =0
	DECLARE @ThanhTienInput FLOAT
	DECLARE @ThanhTienThucChay FLOAT
	DECLARE @SoLuongInput INT
	DECLARE @SoLuongThucChay INT
	DECLARE @DonViTinhThucChay NVARCHAR(20)
	-- Add the T-SQL statements to compute the return value here
	-- Don vi tinh thuc chay
	IF @DmLoaiBannerREF <> 1 AND @DmLoaiBannerREF <> 16
		BEGIN
			SET @DonViTinhThucChay = (SELECT TenLoaiBanner FROM DmLoaiBanner dlb WHERE dlb.DmLoaiBannerID = @DmLoaiBannerREF)
			IF @DonViTinhThucChay = N'Chi phí' OR @DonViTinhThucChay = N'Chi phí quản lý'
			SET @DonViTinhThucChay =  N'Gói'
			IF @DonViTinhThucChay = N'Thời gian' 
			SET @DonViTinhThucChay =  N'Ngày'
		END
	ELSE
		BEGIN
			IF isnull(@DonViTinh,'') <> '' 
			BEGIN
			SET @DonViTinhThucChay = @DonViTinh
			IF @DonViTinhThucChay = N'Tuần' OR @DonViTinhThucChay = N'Tháng' OR @DonViTinhThucChay = N'Năm'
			SET @DonViTinhThucChay = N'Ngày'
			IF @DonViTinhThucChay ='CPC' SET @DonViTinhThucChay = 'Click'
			END
			ELSE  SET @DonViTinhThucChay = N'Gói'
		END
	-- tinh tien
	
	SET @ThanhTienInput = (SELECT isnull(tcg.ThanhTienThucChay,0)
	                            FROM ThucChayGGFBInput tcg WHERE tcg.SoHopDong = @SoHopDong 
	                            AND tcg.DmSanPhamREF = @DmSanPhamREF 
	                            AND tcg.DmLoaiBannerREF = @DmLoaiBannerREF
	                            AND tcg.DonViTinh = @DonViTinh
	                            AND CONVERT(date,tcg.NgayThucHien) = CONVERT(Date,@NgayThucHien))
	   --PRINT(@ThanhTienInput)                         
	SET @ThanhTienInput = ROUND(isnull(@ThanhTienInput,0),-1)
	
	SET @ThanhTienThucChay = (SELECT isnull(SUM(isnull(tcdt.ThanhTienSauTrietKhauThucChay,0) + isnull(tcdt.GiaTriThayDoi,0)),0)
	                                 FROM ThucChayDaTinh tcdt WHERE tcdt.SoHopDong = @SoHopDong
								AND tcdt.TenSanPham = @DmSanPhamREF
								AND tcdt.DmLoaiBannerREF = @DmLoaiBannerREF
								AND tcdt.DonViTinh = @DonViTinhThucChay)
	SET @ThanhTienThucChay = ROUND(isnull(@ThanhTienThucChay,0),-1)
	 --PRINT(@ThanhTienThucChay) 
	-- tinhs so luong
	SET @SoLuongInput = (SELECT isnull(tcg.SoLuongThucChay,0)
	                            FROM ThucChayGGFBInput tcg WHERE tcg.SoHopDong = @SoHopDong 
	                            AND tcg.DmSanPhamREF = @DmSanPhamREF 
	                            AND tcg.DmLoaiBannerREF = @DmLoaiBannerREF
	                            AND tcg.DonViTinh = @DonViTinh
	                            AND CONVERT(date,tcg.NgayThucHien) = CONVERT(Date,@NgayThucHien))
	 --PRINT(@SoLuongInput)                             
	--SET @SoLuongInput = ROUND(isnull(@SoLuongInput,0),-1)
	
	SET @SoLuongThucChay = (SELECT isnull(SUM(isnull(tcdt.SoLuongThucChay,0) + isnull(tcdt.SoLuongThayDoi,0)),0)
	                                 FROM ThucChayDaTinh tcdt WHERE tcdt.SoHopDong = @SoHopDong
								AND tcdt.TenSanPham = @DmSanPhamREF
								AND tcdt.DmLoaiBannerREF = @DmLoaiBannerREF
								AND tcdt.DonViTinh = @DonViTinhThucChay)
	--PRINT(@SoLuongThucChay)  	
	--SET @SoLuongThucChay = ROUND(isnull(@SoLuongThucChay,0),-1)
	-- Return the result of the function
	IF(@SoLuongInput = @SoLuongThucChay AND @ThanhTienInput = @ThanhTienThucChay)
	 SET @ResultVar = 0 -- khong tinh toan
	ELSE
		IF @SoLuongInput >= @SoLuongThucChay AND @ThanhTienInput > @ThanhTienThucChay
			SET @ResultVar = 1
		ELSE
		IF @SoLuongInput <= @SoLuongThucChay AND @ThanhTienInput < @ThanhTienThucChay
			SET @ResultVar = 2
		ELSE
		IF @SoLuongInput >= @SoLuongThucChay AND @ThanhTienInput < @ThanhTienThucChay
			SET @ResultVar = 3
		ELSE
		IF @SoLuongInput <= @SoLuongThucChay AND @ThanhTienInput > @ThanhTienThucChay
			SET @ResultVar = 4
	SET @ResultVar = ISNULL(@ResultVar,0)
	RETURN @ResultVar

END

```
