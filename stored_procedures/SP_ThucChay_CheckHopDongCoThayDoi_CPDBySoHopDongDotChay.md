# Stored Procedure: `ThucChay_CheckHopDongCoThayDoi_CPDBySoHopDongDotChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-16 16:49:16.027000
- **Ngày sửa cuối**: 2024-07-29 15:05:56.703000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongREF` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoLuongHT` | `int(4)` | No |
| `@ThanhTienHDCT` | `float(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--
--EXEC [ThucChay_CheckHopDongCoThayDoi_CPDBySoHopDongDotChay] 1025352,'QC3260523',699190,'2023-06-27',2,0
CREATE PROCEDURE [dbo].[ThucChay_CheckHopDongCoThayDoi_CPDBySoHopDongDotChay] 
	@HopDongREF INT,
	@SoHopDong NVARCHAR(50),
	@HopDongChiTietID INT,
	@NgayThucHien DATETIME,
	@SoLuongHT INT,
	@ThanhTienHDCT FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @SoNgayDotChayThayDoi INT, @SoLuong INT, @DonViTinh NVARCHAR(20), @DonGiaTheoDVTinhHT FLOAT
	
	DECLARE @CONTENT_LOG NVARCHAR(MAX), @NGUON_LOG NVARCHAR(500), @SoLuongThucChayHTBooking INT
	DECLARE @CountHDTD INT, @GiaTriThayDoi FLOAT, @DonGiaHT FLOAT, @SoLuongThayDoi FLOAT, @SoLuongThucChayDaTinh FLOAT
	DECLARE @DonGiaLienKeTruoc FLOAT, @DmSanPhamREF INT, @DmWebsiteREF INT
	DECLARE @ChietKhauHT FLOAT, @TongGTThanhtienThucChayDatinh FLOAT, @TongGTThanhTienHienTai FLOAT

	SET @SoNgayDotChayThayDoi = 0
	SET @DonGiaLienKeTruoc = 0
	SET @CountHDTD = 0
	SET @CONTENT_LOG = ''
	SET @NGUON_LOG = ''
	SET @SoLuongThucChayHTBooking = 0
	set @DonGiaTheoDVTinhHT = 0
	SET @ChietKhauHT = 0
	SET @TongGTThanhtienThucChayDatinh = 0
	
	SET @CountHDTD = ISNULL(@CountHDTD,0)
	--1. GET SO LUONG DOT CHAY CUA LAN THAY DOI TAI NGAY THUC HIEN
	--print Convert(nvarchar(100),getdate(),130)
	SELECT @SoLuong = hdct.SoLuong, @DonViTinh = hdct.DonViTinh, @DonGiaHT = hdct.DonGia
			,@ChietKhauHT = hdct.ChietKhau, @DmSanPhamREF = hdct.DmSanPhamREF
			, @DmWebsiteREF = hdct.DmWebsiteREF
	FROM HopDongChiTiet hdct
	WHERE hdct.HopDongChiTietID = @HopDongChiTietID
	--print Convert(nvarchar(100),getdate(),130)
	SET @DonGiaTheoDVTinhHT = ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(@SoLuong,@DonViTinh,@DonGiaHT,@NgayThucHien, @NgayThucHien, @HopDongChiTietID),0)
	--TINH SO LUONG THUC CHAY DU TREN BOOKING HIEN TAI
	--print Convert(nvarchar(100),getdate(),130)
	set @SoLuongThucChayHTBooking = dbo.[ThucChay_GetSoLuongThucChayBooking_CPDDotChay](@SoLuongHT ,@DonViTinh ,@HopDongChiTietID ,@NgayThucHien )	
	--print Convert(nvarchar(100),getdate(),130)
	SET @DmSanPhamREF = ISNULL(@DmSanPhamREF,0)
	SET @DmWebsiteREF = dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(@DmWebsiteREF)
	--TONG GIA TRI THUC CHAY HIEN TAI
	IF (@ChietKhauHT <> 100)
	BEGIN
		SET @TongGTThanhTienHienTai = round(@SoLuongThucChayHTBooking*(@DonGiaTheoDVTinhHT*(100-@ChietKhauHT)/100),0)

		--TONG GIA TRI THUC CHAY DEN NGAY THUC HIEN

		SELECT @TongGTThanhtienThucChayDatinh = sum(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0) + ISNULL(TCDT.GiaTriThayDoi,0)) 
				, @SoLuongThucChayDaTinh = sum(ISNULL(tcdt.SoLuongThucChay,0) + ISNULL(tcdt.SoLuongThayDoi,0))
				FROM ThucChayDaTinh tcdt
				WHERE convert(date,tcdt.NgayThucHien) <= @NgayThucHien 
				AND TCDT.HopDongChiTietREF = @HopDongChiTietID
		SET @TongGTThanhtienThucChayDatinh = ISNULL(@TongGTThanhtienThucChayDatinh,0)

		SET @SoLuongThucChayDaTinh = ISNULL(@SoLuongThucChayDaTinh,0)
	END
	ELSE
	BEGIN
		SET @TongGTThanhTienHienTai = round(@SoLuongThucChayHTBooking*@DonGiaTheoDVTinhHT,0)

		--TONG GIA TRI THUC CHAY DEN NGAY THUC HIEN

		SELECT @TongGTThanhtienThucChayDatinh = sum(ISNULL(tcdt.ThanhTienKM,0) + ISNULL(TCDT.GiaTriKMThayDoi,0)) 
				, @SoLuongThucChayDaTinh = sum(ISNULL(tcdt.SoLuongThucChayKM,0) + ISNULL(tcdt.SoLuongKMThayDoi,0))
				FROM ThucChayDaTinh tcdt
				WHERE convert(date,tcdt.NgayThucHien) <= @NgayThucHien 
				AND TCDT.HopDongChiTietREF = @HopDongChiTietID

		SET @TongGTThanhtienThucChayDatinh = ISNULL(@TongGTThanhtienThucChayDatinh,0)

		SET @SoLuongThucChayDaTinh = ISNULL(@SoLuongThucChayDaTinh,0)
		SET @ThanhTienHDCT = @SoLuong*@DonGiaHT
	END
	
	
	----print Convert(nvarchar(100),getdate(),130)
	
	-----select @TongGTThanhTienHienTai, @TongGTThanhtienThucChayDatinh,@ThanhTienHDCT,@TongGTThanhtienThucChayDatinh
	IF((@TongGTThanhTienHienTai <> @TongGTThanhtienThucChayDatinh) AND (ABS(@ThanhTienHDCT - @TongGTThanhtienThucChayDatinh)>1))
	
	BEGIN
	--print 'nhay vao day'
		SET @CountHDTD = 
		(
			SELECT COUNT(tcdt.NgayThucHien) FROM ThucChayDaTinh tcdt
			WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
			AND CONVERT(DATE, tcdt.NgayThucHien) = @NgayThucHien
		)
		SET @CONTENT_LOG = @CONTENT_LOG + N'HĐ có sự thay đổi về giá trị thực chạy, Giá trị thực chạy trước:' + convert(nvarchar(50),CONVERT(bigint,@TongGTThanhtienThucChayDatinh))
		 + N' Gia trị thực chạy hiện tại:' + CONVERT(NVARCHAR(50),CONVERT(bigint,@TongGTThanhTienHienTai))
		SET @NGUON_LOG = @NGUON_LOG + 'HopDongSo:' + CONVERT(NVARCHAR(50),@HopDongChiTietID) + ' Ngaythuchien:' + CONVERT(NVARCHAR(50),@NgayThucHien)	
		SET @GiaTriThayDoi = @TongGTThanhTienHienTai - @TongGTThanhtienThucChayDatinh
		SET @SoLuongThayDoi = @SoLuongThucChayHTBooking - @SoLuongThucChayDaTinh
	
		
		IF(@CountHDTD >0)
		BEGIN
			--UPDATE GIA TRI THAY DOI
			IF (@ChietKhauHT <> 100)
			BEGIN
				UPDATE ThucChayDaTinh
				SET	GiaTriThayDoi = GiaTriThayDoi + @GiaTriThayDoi
					, SoLuongThayDoi =  SoLuongThayDoi + @SoLuongThayDoi
				, LastModifiedAt = GETDATE()
				, ghichu = ghichu +', ' + 'SP:[ThucChay_CheckHopDongCoThayDoi_CPDBySoHopDongDotChay] ,' + @CONTENT_LOG 
				WHERE HopDongID = @HopDongREF
				AND HopDongChiTietREF = @HopDongChiTietID
				AND NgayThucHien = @NgayThucHien 
			END
			ELSE
			BEGIN
				UPDATE ThucChayDaTinh
				SET	GiaTriKMThayDoi = GiaTriKMThayDoi + @GiaTriThayDoi
					, SoLuongKMThayDoi =  SoLuongKMThayDoi + @SoLuongThayDoi
				, LastModifiedAt = GETDATE()
				, ghichu =  ghichu +', ' + 'SP:[ThucChay_CheckHopDongCoThayDoi_CPDBySoHopDongDotChay] ,' + @CONTENT_LOG 
				WHERE HopDongID = @HopDongREF
				AND HopDongChiTietREF = @HopDongChiTietID
				AND NgayThucHien = @NgayThucHien 
			END
			
		END
		ELSE
			BEGIN
				--print'[ThucChay_InsertThucTreoThayDoi_CPD]'
				EXEC [dbo].[ThucChay_InsertThucTreoThayDoi_CPD] @HopDongChiTietID ,@NgaythucHien,@GiaTriThayDoi, @SoLuongThayDoi
			END	
	END
END

```
