# Stored Procedure: `ThucChayGGFBInput_Insert`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-07-08 17:52:02.717000
- **Ngày sửa cuối**: 2018-11-07 15:53:49.790000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DanhSachTaiKhoan` | `nvarchar(400)` | No |
| `@SoLuongHopDong` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoLuongThucChay` | `int(4)` | No |
| `@ThanhTienThucChay` | `float(8)` | No |
| `@NguoiCapNhat` | `nvarchar(100)` | No |
| `@GhiChu` | `nvarchar(1000)` | No |
| `@DmSanPhamREF` | `nvarchar(100)` | No |
| `@DmLoaiBannerREF` | `int(4)` | No |
| `@TenLoaiBanner` | `nvarchar(200)` | No |
| `@GiaTriThanhToan` | `float(8)` | No |
| `@NgayThanhToan` | `nvarchar(100)` | No |
| `@ChenhLech` | `float(8)` | No |
| `@ThanhTienHopDong` | `float(8)` | No |
| `@NhanHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [dbo].[ThucChayGGFBInput_Insert]  'NB050515','Noi bo',1,'Gói','2015-06-10',200,200000,'asd','','Facebook Ads'
CREATE PROCEDURE [dbo].[ThucChayGGFBInput_Insert]
	-- Add the parameters for the stored procedure here
	@SoHopDong NVARCHAR(50),
	@DanhSachTaiKhoan NVARCHAR(200),
	@SoLuongHopDong INT ,
	@DonViTinh NVARCHAR(50),
	@NgayThucHien DATETIME,
	@SoLuongThucChay INT,
	@ThanhTienThucChay FLOAT,
	@NguoiCapNhat NVARCHAR(50),
	@GhiChu NVARCHAR(500),
	@DmSanPhamREF NVARCHAR(50),
	@DmLoaiBannerREF INT,
	@TenLoaiBanner NVARCHAR(100),
	@GiaTriThanhToan FLOAT,
	@NgayThanhToan NVARCHAR(50),
	@ChenhLech FLOAT,
	@ThanhTienHopDong FLOAT,
	@NhanHopDong NVARCHAR(50)
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
    -- xu ly nhan hang
    DECLARE @NhanHangREF NVARCHAR(200)
    DECLARE @DmNhanhangChuan NVARCHAR(200) = ''
    DECLARE @name NVARCHAR(200)
    IF isnull(@NhanHopDong,'') = '' SET @NhanHopDong = '0'
    
    SET @NhanHangREF = (SELECT TOP 1 item FROM dbo.ArrayToTable(dbo.Array(@NhanHopDong,',')))
    
    IF ISNUMERIC(@NhanHangREF) =0
		BEGIN
			
			DECLARE db_cursor CURSOR FOR  
			SELECT TOP 1 item FROM dbo.ArrayToTable(dbo.Array(@NhanHopDong,',')) 

			OPEN db_cursor   
			FETCH NEXT FROM db_cursor INTO @name   

			WHILE @@FETCH_STATUS = 0   
			BEGIN  
				IF(@DmNhanhangChuan = '') 
					SET @DmNhanhangChuan = @DmNhanhangChuan +  (SELECT TOP 1 DmNhanHangID FROM [192.168.23.217].BRAND.dbo.DmNhanHang WHERE TenNhanHang = @name AND deletedstatus = 0)
				ELSE
					SET @DmNhanhangChuan  = @DmNhanhangChuan + ',' +  (SELECT TOP 1 DmNhanHangID FROM [192.168.23.217].BRAND.dbo.DmNhanHang WHERE TenNhanHang = @name AND deletedstatus = 0)

				   FETCH NEXT FROM db_cursor INTO @name   
			END   

			CLOSE db_cursor   
			DEALLOCATE db_cursor
			
			
			SET @NhanHopDong = 
			(
	    	SELECT TOP 1 hdct.DanhSachNhanHangREF
	    	FROM HopDong hd INNER JOIN HopDongChiTiet hdct 
	    	ON hd.HopDongID = hdct.HopDongFK WHERE hd.SoHopDong = @SoHopDong AND hdct.NhanHang = @NhanHopDong
	    	)
		END
    -- Insert statements for procedure here
	IF EXISTS (SELECT ThucChayGGFBInputID FROM ThucChayGGFBInput tcg WHERE tcg.SoHopDong = @SoHopDong AND Convert(date,tcg.NgayThucHien) = Convert(date,@NgayThucHien) AND tcg.DonViTinh = @DonViTinh AND tcg.DmLoaiBannerREF = @DmLoaiBannerREF AND DmSanPhamREF = @DmSanPhamREF )
	BEGIN
		UPDATE ThucChayGGFBInput
		SET
			-- ThucChayGGFBInputID = ? -- this column value is auto-generated
			SoLuongThucChay = @SoLuongThucChay,
			ThanhTienThucChay = @ThanhTienThucChay,
			NguoiCapNhat = @NguoiCapNhat,
			ChenhLech = @ChenhLech,
			NgayThanhToan = convert(datetime, @NgayThanhToan, 103),
			GiaTriThanhToan = @GiaTriThanhToan,
			GhiChu = @GhiChu,
			NhanHopDong = @NhanHopDong,
			ThanhTienHopDong = @ThanhTienHopDong
		WHERE SoHopDong = @SoHopDong AND convert(date,NgayThucHien) = convert(date,@NgayThucHien) AND DonViTinh = @DonViTinh AND DmLoaiBannerREF = @DmLoaiBannerREF AND DmSanPhamREF = @DmSanPhamREF 
	END
	ELSE
		BEGIN
			INSERT INTO ThucChayGGFBInput
			(
				-- ThucChayGGFBInputID -- this column value is auto-generated
				SoHopDong,
				DanhSachTaiKhoan,
				SoLuongHopDong,
				DonViTinh,
				NgayThucHien,
				SoLuongThucChay,
				ThanhTienThucChay,
				NguoiCapNhat,
				GhiChu,
				DmSanPhamREF,
				DmLoaiBannerREF,
				TenLoaiBanner,
				GiaTriThanhToan,
				NgayThanhToan,
				ChenhLech,
				ThanhTienHopDong,
				NhanHopDong
			)
			VALUES
			(
				@SoHopDong,
				@DanhSachTaiKhoan,
				@SoLuongHopDong,
				@DonViTinh,
				CONVERT(DATE,@NgayThucHien),
				@SoLuongThucChay,
				@ThanhTienThucChay,
				@NguoiCapNhat,
				@GhiChu,
				@DmSanPhamREF,
				@DmLoaiBannerREF,
				@TenLoaiBanner,
				@GiaTriThanhToan,
				convert(datetime, @NgayThanhToan, 103),
				@ChenhLech,
				@ThanhTienHopDong,
				@NhanHopDong
			)
		END
	SELECT 1
END



```
