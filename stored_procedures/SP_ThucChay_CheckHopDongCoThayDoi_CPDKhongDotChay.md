# Stored Procedure: `ThucChay_CheckHopDongCoThayDoi_CPDKhongDotChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-01 14:36:13.897000
- **Ngày sửa cuối**: 2024-08-21 16:10:29.560000

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


CREATE PROCEDURE [dbo].[ThucChay_CheckHopDongCoThayDoi_CPDKhongDotChay] 
	-- Add the parameters for the stored procedure here
	@HopDongREF INT,
	@SoHopDong NVARCHAR(50),
	@HopDongChiTietID INT,
	@NgayThucHien DATETIME,
	@SoLuongHT INT,
	@ThanhTienHDCT FLOAT
AS
BEGIN
 
	DECLARE @ChietKhau FLOAT, @DonGia FLOAT, @DonGiaHT FLOAT, @HopDongChiTietThayDoiGia INT, @HopDongChiTietThayDoiCK INT, @HopDongChiTietThayDoiSL INT
	DECLARE @DotChayHopDongChiTietThayDoi INT, @HopDongChiTiet INT, @ChietKhauSauTD INT
	DECLARE @SoNgayDotChayThayDoi INT, @SoLuong INT, @DonViTinh NVARCHAR(20), @DonGiaTheoDVTinhHT FLOAT
	DECLARE @soluongpbBF INT, @soluongpbHT INT, @SoLuongThucChayHT INT, @SoLuongThucChayBF INT
	
	DECLARE @CONTENT_LOG NVARCHAR(MAX), @NGUON_LOG NVARCHAR(500)
	DECLARE @CountHDTD INT, @GiaTriThayDoi FLOAT, @TongGiaTriThucChayDaTinh FLOAT, @TongGiaTriThucChayDaTinhHT FLOAT
	DECLARE @DonGiaLienKeTruoc FLOAT, @SoLuongThucChay FLOAT, @SoLuongThucChayBfHT INT
	DECLARE @SoNgayLienKeTruoc FLOAT, @ChietKhauHT FLOAT,@DmSanPhamREF INT, @DmWebsiteREF_log INT, @DmWebsiteREF INT, @TenWebsite NVARCHAR(100)

	DECLARE @SoluongKMHT INT, @GiatriKMHT FLOAT, @SoluongKMDatinh INT, @GiatriKMDatinh FLOAT, @SoluongKMThaydoi INT, @GiatriKMThaydoi FLOAT
	DECLARE @Soluongthaydoi FLOAT

	SET @SoNgayDotChayThayDoi = 0
	SET @DmWebsiteREF_log = 0
	SET @DonGiaLienKeTruoc = 0
	SET @CountHDTD = 0
	SET @CONTENT_LOG = ''
	SET @NGUON_LOG = ''
	SET @DotChayHopDongChiTietThayDoi = 0
	SET @HopDongChiTietThayDoiSL = 0
	SET @HopDongChiTietThayDoiGia = 0
	SET @HopDongChiTietThayDoiCK = 0
	SET @SoLuongThucChayHT = 0
	SET @SoLuongThucChayBF = 0
	set @DonGiaTheoDVTinhHT = 0
	SET @ChietKhauHT = 0
	SET @SoLuongThucChayBfHT = 0
	SET @TongGiaTriThucChayDaTinh = 0
	set @TongGiaTriThucChayDaTinhHT = 0
	SET @CountHDTD = ISNULL(@CountHDTD,0)
	SET @soluongpbHT = 0
	SET @soluongpbBF = 0
	
	
	--1. Xác định thông tin đánh số hiện tại
	SELECT @SoLuong = hdct.SoLuong, @DonViTinh = hdct.DonViTinh
	,@ChietKhauHT = hdct.ChietKhau, @DmSanPhamREF = hdct.DmSanPhamREF, @DmWebsiteREF = hdct.DmWebsiteREF
	, @TenWebsite = hdct.TenWebsite
	FROM HopDongChiTiet hdct
	WHERE hdct.HopDongChiTietID = @HopDongChiTietID

	SET @DmSanPhamREF = ISNULL(@DmSanPhamREF,0)
	SET @DmWebsiteREF_log = dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(@DmWebsiteREF)
	SET @TenWebsite = dbo.GetWebsiteLinkByDmWebsiteID(@DmWebsiteREF,@TenWebsite)
		
	--2. Xác định đơn giá, số lượng đánh số chuẩn ở hiện tại
	SET @DonGiaTheoDVTinhHT = ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh_CPDKhongDotChay(@SoLuong,@DonViTinh,@DonGiaHT,@NgayThucHien, @NgayThucHien, @HopDongChiTietID),0)
	SET @SoLuongThucChayHT =  isnull(dbo.[ThucChay_GetSoLuongThucChayBooking_CPDKhongDotChay](@SoLuong ,@DonViTinh ,@HopDongChiTietID ,@NgayThucHien ),0)
	
	--3. Xác định số lượng, giá trị thực chạy đã tính đến hiện tại
	SELECT @SoLuongThucChay = SUM(ISNULL(tcdt.SoLuongThucChay,0))
	     , @TongGiaTriThucChayDaTinh = SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay,0)) +	SUM(ISNULL(tcdt.GiaTriThayDoi,0))
		 , @SoluongKMDatinh = SUM(ISNULL(tcdt.SoLuongThucChayKM,0)) + SUM(ISNULL(tcdt.SoLuongKMThayDoi,0))
		 , @GiatriKMDatinh = SUM(ISNULL(tcdt.ThanhTienKM,0)) +	SUM(ISNULL(tcdt.GiaTriKMThayDoi,0))
	FROM dbo.ThucChayDaTinh tcdt
	WHERE convert(date,tcdt.NgayThucHien) <= @NgayThucHien 
	AND TCDT.HopDongChiTietREF = @HopDongChiTietID

	SET @SoLuongThucChay = ISNULL(@SoLuongThucChay,0)
	SET @TongGiaTriThucChayDaTinh = ISNULL(@TongGiaTriThucChayDaTinh,0)
	SET @SoluongKMDatinh = ISNULL(@SoluongKMDatinh,0)
	SET @GiatriKMDatinh = ISNULL(@GiatriKMDatinh,0)
	
	--4. Xác định số lượng thực chạy, giá trị tính đến hiện tại
	SET @TongGiaTriThucChayDaTinhHT = @SoLuongThucChayHT*((@DonGiaTheoDVTinhHT*(100-@ChietKhauHT))/100)
	SET @SoluongKMHT = IIF(@ChietKhauHT = 100, @SoLuongThucChayHT, 0)
	SET @GiatriKMHT = IIF(@ChietKhauHT = 100, @SoLuongThucChayHT*@DonGiaTheoDVTinhHT, 0)
	SET @SoLuongThucChayHT = IIF(@ChietKhauHT = 100, 0, @SoLuongThucChayHT)

	--5. Đối trừ
	SET @GiaTriThayDoi = @TongGiaTriThucChayDaTinhHT - @TongGiaTriThucChayDaTinh
	SET @GiatriKMThaydoi =  @GiatriKMHT - @GiatriKMDatinh
	SET @Soluongthaydoi = @SoLuongThucChayHT - @SoLuongThucChay
	SET @SoluongKMThaydoi = @SoluongKMHT - @SoluongKMDatinh

	IF (ROUND(@GiatriKMThaydoi, 2) <> 0) OR (@SoluongKMThaydoi <> 0) 
	BEGIN
		--print (N'ThucChay_InsertKhuyenMaiThayDoi_CPDKhongDotChay ')
		EXEC [dbo].ThucChay_InsertKhuyenMaiThayDoi_CPDKhongDotChay   
				@HopDongChiTietID ,@NgaythucHien  ,
				@TongGiaTriThucChayDaTinhHT ,
				@SoLuongThucChayHT ,
				@GiatriKMHT ,
				@SoluongKMHT 
	END
	ELSE
		IF (ROUND(@GiaTriThayDoi, 0) <> 0) OR (@SoLuongThayDoi <> 0)
		BEGIN
			SET @CONTENT_LOG = @CONTENT_LOG + N'[ThucChay_CheckHopDongCoThayDoi_CPDKhongDotChay] (CPD KhongDotChay HĐ Thay đổi số lượng thực chạy đã chạy :' + Convert(NVARCHAR(50),@SoLuongThucChay) + '->' + CONVERT(NVARCHAR(30),@SoLuongThucChayHT) + ');'
			SET @CONTENT_LOG = @CONTENT_LOG + N'[ThucChay_CheckHopDongCoThayDoi_CPDKhongDotChay] (CPD KhongDotChay HĐ Thay đổi tổng giá trị thực chạy :' + Convert(NVARCHAR(50),@TongGiaTriThucChayDaTinh) + '->' + CONVERT(NVARCHAR(30),@TongGiaTriThucChayDaTinhHT) + ');'

			SET @CountHDTD = 
			(
				SELECT COUNT(tcdt.NgayThucHien) FROM ThucChayDaTinh tcdt
				WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
				AND CONVERT(DATE, tcdt.NgayThucHien) = @NgayThucHien
			)

			IF(@CountHDTD >0)
			BEGIN
				UPDATE ThucChayDaTinh
				SET	GiaTriThayDoi = GiaTriThayDoi + @GiaTriThayDoi
				, LastModifiedAt = GETDATE()
				, GhiChu = @CONTENT_LOG
				WHERE HopDongID = @HopDongREF
				AND HopDongChiTietREF = @HopDongChiTietID
				AND NgayThucHien = @NgayThucHien 
			END
			ELSE
				BEGIN
					EXEC [dbo].[ThucChay_InsertThucTreoThayDoi_CPDKhongDotChay] @HopDongChiTietID,@NgaythucHien,@GiaTriThayDoi
				END	
		END
	SELECT 1
END

```
