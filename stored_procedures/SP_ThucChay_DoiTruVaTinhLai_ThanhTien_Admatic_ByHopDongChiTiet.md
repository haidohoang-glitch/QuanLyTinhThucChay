# Stored Procedure: `ThucChay_DoiTruVaTinhLai_ThanhTien_Admatic_ByHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-01-18 15:41:37.030000
- **Ngày sửa cuối**: 2022-01-18 15:45:05.037000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@pSoHopDong` | `nvarchar(200)` | No |
| `@pHopDongChiTietID` | `int(4)` | No |
| `@pDmSanPhamREF` | `int(4)` | No |
| `@pStartDate` | `datetime(8)` | No |
| `@pEndDate` | `datetime(8)` | No |
| `@pNgayGhiNhanThucChay` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
EXEC [dbo].[ThucChay_DoiTruVaTinhLai_ThanhTien_Admatic] 
	'QC2110718',
	23455,
	821,
	'2018-07-18' ,
	'2018-07-29' ,
	@pNgayGhiNhanThucChay DATET
*/

CREATE PROCEDURE [dbo].[ThucChay_DoiTruVaTinhLai_ThanhTien_Admatic_ByHopDongChiTiet] 
	@pSoHopDong NVARCHAR(100),
	@pHopDongChiTietID INT,
	@pDmSanPhamREF INT,
	@pStartDate datetime,
	@pEndDate DATETIME,
	@pNgayGhiNhanThucChay DATETIME
AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @NgayDanhSoGioiHan DATETIME
	DECLARE @SoHopDong NVARCHAR(50), @HopDongID INT, @DmSanPhamREF INT, @HopDongChiTietID INT, @TenWebsite NVARCHAR(50), @DmWebsiteREF INT, @DmBannerREF INT
	DECLARE @GhiChu_DoiTruThucChay NVARCHAR(1000), @Ghichu_TinhLaiThucChay NVARCHAR(1000)

	SET @NgayDanhSoGioiHan = '2020-07-20'
	SET @SoHopDong = @pSoHopDong
	SET @DmSanPhamREF = @pDmSanPhamREF
	SET @HopDongChiTietID = @pHopDongChiTietID
	SET @HopDongID = (SELECT TOP (1) HopDongID FROM dbo.HopDong WHERE SoHopDong = @SoHopDong ORDER BY HopDongID)

	SET @GhiChu_DoiTruThucChay = N'Doi tru thuc chay thanhtien_admatic cho SoHopDong: ' + @SoHopDong
	SET @Ghichu_TinhLaiThucChay = N'Tinh lai thuc chay thanhtien_admatic cho SoHopDong: ' + @SoHopDong


	SET @NgayThucHien = convert(date,@pStartDate)

	DELETE FROM dbo.ThucChay_ThanhTien_Admatic_temp WHERE 1=1

	--CAP NHAT THONG TIN BANNER NATIVE ADS
	EXEC [ThucChay_Insert_And_Update_HopDongChiTietAndBanner_ThanhTien_Admatic] @NgayThucHien = @NgayThucHien
	EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner_ThanhTien_Admatic_NgayThucHien]	@NgayThucHien = @NgayThucHien

	
	WHILE(@NgayThucHien <= @pEndDate)
	BEGIN
		
		--THUC HIEN DOI TRU THUC CHAY THEO NGAYTHUCHIEN
		EXEC [dbo].[ThucChay_Insert_GTTD_DoiTruGiam_ThucChayDaTinh_ByHD_ThanhTien_Admatic] 
		@FromDate = @NgayThucHien,
		@ToDate = @NgayThucHien,
		@NgayGhiNhanThucChay = @NgayThucHien,
		@HopDongID = @HopDongID,
		@HopDongChiTietID = @HopDongChiTietID,
		@DmSanPhamREF = @DmSanPhamREF,
		@GhiChu = @GhiChu_DoiTruThucChay

	INSERT INTO [dbo].[ThucChay_ThanhTien_Admatic_temp]
           ([ThucChay_ThanhTien_AdmaticID], [SoHopDong]
           ,[TypeProduct]
           ,[DmSanPhamREF]
           ,[TenSanPham]
           ,[TenNhanHang]
           ,[DmNhanHangREF]
           ,[DmBannerID]
           ,[DmWebsiteID]
           ,[TenWebsite]
           ,[DmViTriBannerSanPhamID]
           ,[TenViTriBannerSanPham]
           ,[SoLuongThucChay]
           ,[SoLuongThucChayKM]
           ,[DonViTinh]
           ,[ThanhTienThucChaySauCK_ChuaVAT]
           ,[ThanhTienThucChayKM]
           ,[NgayThucHien]
           ,[CreatedAt]
           ,[CreatedBy]
           ,[LastModifiedAt]
           ,[LastModifiedBy]
           ,[DeletedStatus])
 

		SELECT tc.[ThucChay_ThanhTien_AdmaticID], tc.[SoHopDong]
           , tc.[TypeProduct]
           , tc.[DmSanPhamREF]
           , tc.[TenSanPham]
           , tc.[TenNhanHang]
           , tc.[DmNhanHangREF]
           , tc.[DmBannerID]
           , tc.[DmWebsiteID]
           , tc.[TenWebsite]
           , tc.[DmViTriBannerSanPhamID]
           , tc.[TenViTriBannerSanPham]
           , tc.[SoLuongThucChay]
           , tc.[SoLuongThucChayKM]
           , tc.[DonViTinh]
           , tc.[ThanhTienThucChaySauCK_ChuaVAT]
           , tc.[ThanhTienThucChayKM]
           , tc.[NgayThucHien]
           , tc.[CreatedAt]
           , tc.[CreatedBy]
           , tc.[LastModifiedAt]
           , tc.[LastModifiedBy]
           , tc.[DeletedStatus] from dbo.[ThucChay_ThanhTien_Admatic] tc
		INNER JOIN (SELECT hd.* FROM dbo.HopDong hd 
						WHERE hd.TrangThaiHopDong NOT IN (0,3) 
						AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan 
						AND hd.SoHopDong = @SoHopDong
					) hd
		ON hd.SoHopDong = tc.SoHopDong
		WHERE CONVERT(DATE,tc.NgayThucHien) = CONVERT(DATE,@NgayThucHien)
		AND tc.[DmWebsiteID] <> 0

		
		DECLARE R_Cursor_TinhLai_Admatic CURSOR FOR 
		SELECT distinct A.SoHopDong, A.DmSanPhamREF, A.DmWebsiteID, A.TenWebsite, A.DmBannerID
		  FROM
			(
				SELECT TC.SoHopDong, TC.DmSanPhamREF, TC.DmWebsiteID, TC.TenWebsite, TC.DmBannerID 
				FROM 
				(SELECT tct.SoHopDong, tct.DmSanPhamREF, tct.DmWebsiteID, tct.TenWebsite, tct.DmBannerID
								FROM dbo.[ThucChay_ThanhTien_Admatic_temp] tct
								WHERE tct.SoHopDong = @SoHopDong
				)TC
				INNER JOIN 
				(	SELECT HopDongREF, HopDongChiTietREF, DmSanPhamREF , DmBannerREF as DmBannerID, TiLeThucChayHDCTSoVoiBanner 
					FROM dbo.ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic
					WHERE HopDongREF = @HopDongID
					AND HopDongChiTietREF = @HopDongChiTietID
					AND DeletedStatus = 0
				)tt ON CONVERT(NVARCHAR(100),tc.DmBannerID) = tt.DmBannerID
				WHERE 1=1 --THEM DK chi tinh khi san pham chay va treo trung nhau hoac sp hopdong = 733 haidh comment 24/11/2020
				AND EXISTS(SELECT TOP (1) hdct.HopDongChiTietID FROM dbo.HopDongChiTiet hdct 
					WHERE hdct.HopDongChiTietID = @HopDongChiTietID
					AND hdct.DmLoaiREF = 42
					AND hdct.DeletedStatus = 0
					AND NOT (hdct.DmLoaiREF = 42 AND hdct.DmLoaiNenTangREF = 9) --INVENTORY ADMAITC
					AND (hdct.DmSanPhamREF = 733 Or hdct.DmSanPhamREF = tc.DmSanPhamREF)
					Order BY hdct.HopDongChiTietID
				)
			)A
		ORDER BY A.SoHopDong, A.DmSanPhamREF	

		OPEN R_Cursor_TinhLai_Admatic

		-- Perform the first fetch.
		FETCH NEXT FROM R_Cursor_TinhLai_Admatic into @SoHopDong, @DmSanPhamREF, @DmWebsiteREF, @TenWebsite, @DmBannerREF
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
				--TINH THUC CHAY CHO SAN PHAM NATIVE ADS
				--print 'nhay vao day'
				SET @HopDongID = (SELECT TOP (1) hd.HopDongID FROM dbo.HopDong hd WHERE hd.SoHopDong = @SoHopDong ORDER BY hd.HopDongID)

				EXEC [dbo].[ThucChay_Insert_TinhLai_ThucChayDaTinh_ByHD_ThanhTien_Admatic] 
					@NgayThucHien = @NgayThucHien,
					@SoHopDong = @SoHopDong,
					@HopDongID = @HopDongID,
					@HopDongChiTietID = @HopDongChiTietID,
					@DmSanPhamREF = @DmSanPhamREF,
					@DmWebsiteREF = @DmWebsiteREF, 
					@DmBannerID = @DmBannerREF,
					@GhiChu = @Ghichu_TinhLaiThucChay
			FETCH NEXT FROM R_Cursor_TinhLai_Admatic into @SoHopDong, @DmSanPhamREF, @DmWebsiteREF, @TenWebsite, @DmBannerREF
			END

		CLOSE R_Cursor_TinhLai_Admatic
		DEALLOCATE R_Cursor_TinhLai_Admatic

		SET @NgayThucHien = DATEADD(d,1,@NgayThucHien)
		--DELETE FROM dbo.ThucChay_ThanhTien_Admatic_temp
	END 
	--CAP NHAT LAI THONG TIN NGAY THUC HIEN CHO GIA TRI DOI TRU, TINH LAI THUC CHAY
	UPDATE dbo.ThucChayDaTinh
	SET NgayThucHien = @pNgayGhiNhanThucChay
	WHERE HopDongID = @HopDongID
	AND HopDongChiTietREF = @pHopDongChiTietID
	AND CONVERT(DATE,CreatedAt) = CONVERT(DATE,GETDATE())
	AND (GhiChu = @GhiChu_DoiTruThucChay OR GhiChu = @Ghichu_TinhLaiThucChay)

	--DAY DU LIEU SANG THUCCHAYDATINH_ADMARKET NEU LA SAN PHAM ADX
	INSERT INTO [dbo].[ThucChayDaTinhAdmarket]
           ([ThucChayDaTinhID]
           ,[HopDongID]
           ,[SoHopDong]
           ,[DmMaHopDongREF]
           ,[TenMaHopDong]
           ,[NgayDanhSoHopDong]
           ,[NgayKyHopDong]
           ,[NhanHopDong]
           ,[NgayNhanBanFax]
           ,[NgayNhanHopDongBanCung]
           ,[NgayChuyenHopDongChoKeToan]
           ,[So]
           ,[Thang]
           ,[Nam]
           ,[GiaTriHopDong]
           ,[CongNo]
           ,[HopDongChiTietREF]
           ,[DangSuDung]
           ,[IsGiayPhep]
           ,[TrangThaiHopDong]
           ,[IsBanCung]
           ,[DmPhongBanREF]
           ,[TenPhongBan]
           ,[DmBoPhanREF]
           ,[TenBoPhan]
           ,[DmNhomLamViecREF]
           ,[TenNhomLamViec]
           ,[DmDiaDiemLamViecREF]
           ,[TenDiaDiemLamViec]
           ,[SysNhanVienREF]
           ,[TenDangNhap]
           ,[TenNhanVien]
           ,[TenKhachHang]
           ,[NhanHang]
           ,[DmNhomNganhREF]
           ,[TenNhomNganh]
           ,[DmHinhThucQuangCao]
           ,[TenHinhThucQuangCao]
           ,[DmSanPhamREF]
           ,[TenSanPham]
           ,[DmNhomWebsiteREF]
           ,[TenNhomWebsite]
           ,[DmChuyenMucREF]
           ,[TenChuyenMuc]
           ,[DmLoaiBannerREF]
           ,[TenLoaiBanner]
           ,[DmViTriREF]
           ,[TenViTri]
           ,[DotChayHopDong]
           ,[SoLuongDotChayHD]
           ,[DotChayBooking]
           ,[SoLuongDotChayBooking]
           ,[SoLuong]
           ,[DonViTinh]
           ,[DonGia]
           ,[DonGiaTheoDonVi]
           ,[ChietKhau]
           ,[GiamGia]
           ,[ThanhTien]
           ,[TiLeTuVan]
           ,[ChiPhiTuVan]
           ,[IsKhuyenMai]
           ,[KhuyenMai]
           ,[DmBannerREF]
           ,[DmChienDichREF]
           ,[DmWebsiteREF]
           ,[TenWebsite]
           ,[TongViewThucChay]
           ,[TongClickThucChay]
           ,[TongSoBaiViet]
           ,[SoLuongThucChay]
           ,[NgayThucHien]
           ,[GiaTriThayDoi]
           ,[ThanhTienThucChayTruocTrietKhau]
           ,[GiaTriTrietKhauThucChay]
           ,[ThanhTienSauTrietKhauThucChay]
           ,[GiaTriHoaHongThucChay]
           ,[ThanhTienThucThu]
           ,[ThanhTienKM]
           ,[SoLuongThucChayKM]
           ,[SoLuongThucChayLechTreoHa]
           ,[ThanhTienLechTreoHa]
           ,[CreatedAt]
           ,[LastModifiedAt]
           ,[IsPheDuyet]
           ,[PheDuyetBy]
           ,[PheDuyetAt]
           ,[SoLuongThayDoi]
           ,[SoLuongKMThayDoi]
           ,[GiaTriKMThayDoi]
           ,[GhiChu] )
    SELECT NEWID() AS ThucChayDaTinhAdmarket
		   ,tcdt.[HopDongID]
           ,tcdt.[SoHopDong]
           ,tcdt.[DmMaHopDongREF]
           ,tcdt.[TenMaHopDong]
           ,tcdt.[NgayDanhSoHopDong]
           ,tcdt.[NgayKyHopDong]
           ,tcdt.[NhanHopDong]
           ,tcdt.[NgayNhanBanFax]
           ,tcdt.[NgayNhanHopDongBanCung]
           ,tcdt.[NgayChuyenHopDongChoKeToan]
           ,tcdt.[So]
           ,tcdt.[Thang]
           ,tcdt.[Nam]
           ,tcdt.[GiaTriHopDong]
           ,tcdt.[CongNo]
           ,tcdt.[HopDongChiTietREF]
           ,tcdt.[DangSuDung]
           ,tcdt.[IsGiayPhep]
           ,tcdt.[TrangThaiHopDong]
           ,tcdt.[IsBanCung]
           ,tcdt.[DmPhongBanREF]
           ,tcdt.[TenPhongBan]
           ,tcdt.[DmBoPhanREF]
           ,tcdt.[TenBoPhan]
           ,tcdt.[DmNhomLamViecREF]
           ,tcdt.[TenNhomLamViec]
           ,tcdt.[DmDiaDiemLamViecREF]
           ,tcdt.[TenDiaDiemLamViec]
           ,tcdt.[SysNhanVienREF]
           ,tcdt.[TenDangNhap]
           ,tcdt.[TenNhanVien]
           ,tcdt.[TenKhachHang]
           ,tcdt.[NhanHang]
           ,tcdt.[DmNhomNganhREF]
           ,tcdt.[TenNhomNganh]
           ,tcdt.[DmHinhThucQuangCao]
           ,tcdt.[TenHinhThucQuangCao]
           ,tcdt.[DmSanPhamREF]
           ,tcdt.[TenSanPham]
           ,tcdt.[DmNhomWebsiteREF]
           ,tcdt.[TenNhomWebsite]
           ,tcdt.[DmChuyenMucREF]
           ,tcdt.[TenChuyenMuc]
           ,tcdt.[DmLoaiBannerREF]
           ,tcdt.[TenLoaiBanner]
           ,tcdt.[DmViTriREF]
           ,tcdt.[TenViTri]
           ,tcdt.[DotChayHopDong]
           ,tcdt.[SoLuongDotChayHD]
           ,tcdt.[DotChayBooking]
           ,tcdt.[SoLuongDotChayBooking]
           ,tcdt.[SoLuong]
           ,tcdt.[DonViTinh]
           ,tcdt.[DonGia]
           ,tcdt.[DonGiaTheoDonVi]
           ,tcdt.[ChietKhau]
           ,tcdt.[GiamGia]
           ,tcdt.[ThanhTien]
           ,tcdt.[TiLeTuVan]
           ,tcdt.[ChiPhiTuVan]
           ,tcdt.[IsKhuyenMai]
           ,tcdt.[KhuyenMai]
           ,tcdt.[DmBannerREF]
           ,tcdt.[DmChienDichREF]
           ,tcdt.[DmWebsiteREF]
           ,tcdt.[TenWebsite]
           ,tcdt.[TongViewThucChay]
           ,tcdt.[TongClickThucChay]
           ,tcdt.[TongSoBaiViet]
           ,tcdt.[SoLuongThucChay]
           ,tcdt.[NgayThucHien]
           ,tcdt.[GiaTriThayDoi]
           ,tcdt.[ThanhTienThucChayTruocTrietKhau]
           ,tcdt.[GiaTriTrietKhauThucChay]
           ,tcdt.[ThanhTienSauTrietKhauThucChay]
           ,tcdt.[GiaTriHoaHongThucChay]
           ,tcdt.[ThanhTienThucThu]
           ,tcdt.[ThanhTienKM]
           ,tcdt.[SoLuongThucChayKM]
           ,tcdt.[SoLuongThucChayLechTreoHa]
           ,tcdt.[ThanhTienLechTreoHa]
           ,GETDATE() AS [CreatedAt]
           ,GETDATE() AS [LastModifiedAt]
           ,tcdt.[IsPheDuyet]
           ,tcdt.[PheDuyetBy]
           ,tcdt.[PheDuyetAt]
           ,tcdt.[SoLuongThayDoi]
           ,tcdt.[SoLuongKMThayDoi]
           ,tcdt.[GiaTriKMThayDoi]
		   ,N'can du lieu Adx - Admatic, ' + tcdt.[GhiChu] 
	FROM dbo.ThucChayDaTinh tcdt
	WHERE tcdt.HopDongID = @HopDongID
	AND tcdt.HopDongChiTietREF = @pHopDongChiTietID
	AND tcdt.NgayThucHien = @pNgayGhiNhanThucChay
	AND tcdt.DmSanPhamREF = 585 --Adx
	AND tcdt.[DmHinhThucQuangCao] = 42 --Admatic
	AND CONVERT(DATE,tcdt.CreatedAt) = CONVERT(DATE,GETDATE())
	AND (tcdt.GhiChu = @GhiChu_DoiTruThucChay OR tcdt.GhiChu = @Ghichu_TinhLaiThucChay)

	SELECT '1'
END


```
