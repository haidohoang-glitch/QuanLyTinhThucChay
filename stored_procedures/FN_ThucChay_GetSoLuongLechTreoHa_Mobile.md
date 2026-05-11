# Function: `ThucChay_GetSoLuongLechTreoHa_Mobile`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-09-23 14:14:14.910000
- **Ngày sửa cuối**: 2014-11-19 12:17:40.573000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `bigint(8)` | Yes |
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTiet` | `int(4)` | No |
| `@SoLuong` | `int(4)` | No |
| `@DmSanPhamID` | `int(4)` | No |
| `@ViewThucChay` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
--SELECT dbo.[ThucChay_GetSoLuongLechTreoHa_Mobile] ('2014-09-21','NB150114',52341,2000,342,2262)
CREATE FUNCTION [dbo].[ThucChay_GetSoLuongLechTreoHa_Mobile]
(
	-- Add the parameters for the function here
	@NgayThucHien DATETIME
	, @SoHopDong NVARCHAR(50)
	, @HopDongChiTiet INT
	, @SoLuong INT
	, @DmSanPhamID INT
	, @ViewThucChay INT
)
RETURNS bigint
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ResultValue BIGINT, @MinDate DATETIME, @TongSLTC INT, @TongSLHD INT, @HopDongID INT
	DECLARE @v_tongviewthucchay BIGINT, @v_tongviewphanbo BIGINT, @v_viewthucchay BIGINT, @Count_HD_SP INT
	
	DECLARE @DonGiaSauCK FLOAT, @DonGiaHD FLOAT, @ChietKhauHD FLOAT, @ThanhTienTCDT FLOAT, 
	@ThanhTienHD FLOAT, @IsKhuyenMai INT,
	@ThanhTienConLai FLOAT = 0,@SoLuongConLai FLOAT = 0, @ThanhTienKMHD FLOAT = 0, @SoLuongHD FLOAT = 0,
	@DonGiaTheoDonVi FLOAT = 1,@DonViTinh NVARCHAR(50);
			
		
	SELECT			@IsKhuyenMai        = hdct.IsKhuyenMai,
					@DonGiaHD		    = DonGia,
			 		@ChietKhauHD	    = ChietKhau,
					@ThanhTienHD		= hdct.ThanhTien,
					@SoLuongHD          = hdct.SoLuong,
					@DonViTinh			= hdct.DonViTinh
			FROM HopDongChiTiet AS hdct
			WHERE hdct.HopDongChiTietID = @HopDongChiTiet
	--Xet truong hop phan bo khong khuyen mai	
	IF (@IsKhuyenMai = 1 OR @ChietKhauHD = 100)
		BEGIN
			SELECT @ThanhTienTCDT = SUM(tcdt.ThanhTienKM)
			, @HopDongID = max(tcdt.HopDongID)
			FROM ThucChayDaTinhMobile tcdt INNER JOIN HopDongChiTiet hdct
			ON tcdt.HopDongID = hdct.HopDongFK
			AND tcdt.DmSanPhamREF = hdct.DmSanPhamREF
			WHERE hdct.HopDongChiTietID = @HopDongChiTiet
			AND tcdt.NgayThucHien < = @NgayThucHien
			
			SELECT @ThanhTienKMHD = @SoLuongHD * @DonGiaHD
			
			SET @ThanhTienConLai = @ThanhTienKMHD - @ThanhTienTCDT
			
			SET @DonGiaTheoDonVi = @DonGiaHD/ dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(@DonViTinh)
			IF @ThanhTienConLai <=0 
				SET @ResultValue = @ViewThucChay
			ELSE
				BEGIN
					SET @SoLuongConLai = (@ThanhTienConLai/@DonGiaTheoDonVi)
					IF @SoLuongConLai > @ViewThucChay 
						SET @ResultValue = 0
					ELSE
						SET @ResultValue = @SoLuongConLai - @ViewThucChay
				END
			
		END					
	 ELSE 	--Xet truong hop phan bo khuyen mai	
	    BEGIN
			SET @DonGiaSauCK = @DonGiaHD - (@ChietKhauHD*@DonGiaHD/100)
		
			SELECT @ThanhTienTCDT = SUM(tcdt.ThanhTienSauTrietKhauThucChay +tcdt.GiaTriThayDoi)
			, @HopDongID = max(tcdt.HopDongID)
			FROM ThucChayDaTinhMobile tcdt INNER JOIN HopDongChiTiet hdct
			ON tcdt.HopDongID = hdct.HopDongFK
			AND tcdt.DmSanPhamREF = hdct.DmSanPhamREF			
			WHERE hdct.HopDongChiTietID = @HopDongChiTiet
			AND tcdt.NgayThucHien < = @NgayThucHien
			
			
			SET @ThanhTienConLai = @ThanhTienHD - @ThanhTienTCDT
			IF @ThanhTienConLai <=0 
				SET @ResultValue = @ViewThucChay
			ELSE
				BEGIN
					SET @SoLuongConLai = (@ThanhTienConLai/@DonGiaSauCK)
					IF @SoLuongConLai > @ViewThucChay 
						SET @ResultValue = 0
					ELSE
						SET @ResultValue = @SoLuongConLai - @ViewThucChay
				END
				
		END		
		
	
	-- Return the result of the function
	RETURN @ResultValue;

END



```
