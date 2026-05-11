# Stored Procedure: `sp_Insert_ThucChayDaTinh_ReInsertByHopDong_ThucTreoThayDoi_dev`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-06-04 09:53:59.763000
- **Ngày sửa cuối**: 2025-06-04 10:47:19.700000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@PhanBoID` | `int(4)` | No |
| `@ThucChayHopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [dbo].[sp_Insert_ThucChayDaTinh_ReInsertByHopDong_ThucTreoThayDoi_dev] '2025-06-03', 1065447,755111,624477
CREATE PROCEDURE [dbo].[sp_Insert_ThucChayDaTinh_ReInsertByHopDong_ThucTreoThayDoi_dev]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@HopDongID INT,
	@PhanBoID INT,
	@ThucChayHopDongChiTietID INT
AS
BEGIN
		-- SET NOCOUNT ON added to prevent extra result sets from
		-- interfering with SELECT statements.
		 DECLARE @GhiChu NVARCHAR(200) ='THUC_TREO_TD: ', @CONTENT_LOG NVARCHAR(300), @DmNhanThucChayDaTinh NVARCHAR(200) = ''
		 ----CAI NAY DUNG CHO CHOT CUOI NAM 2016
		 DECLARE @IsHaveBanner SMALLINT = 0, @DmBannerID NVARCHAR(100) = 0
		 DECLARE @DmNhanHangNew NVARCHAR(200), @DmWebsiteREF int, @TenWebsite nvarchar(200) = N''

		 --CHECK THONG TIN DMNHANHANG BI TRUNG NHAU GIUA THUCCHAYDATINH VA LOG THUC TREO
		 SET @DmNhanThucChayDaTinh = 
		 ISNULL((
			SELECT TOP 1 NhanHang FROM dbo.ThucChayDaTinh
			WHERE HopDongChiTietREF = @PhanBoID
			AND NgayThucHien < @NgayThucHien
			ORDER BY NgayThucHien DESC, LastModifiedAt DESC
		 ),'')
		 
		 --XET CO BANNER cho sản phảm chạy co banner treo
		 SET @IsHaveBanner = ISNULL((SELECT COUNT(HopDongChiTietID) FROM dbo.HopDongChiTiet
						WHERE HopDongChiTietID = @PhanBoID 
						AND DmSanPhamREF IN (231,238,339,240,598,613,370,680,735,821) 
						AND not (DmLoaiREF IN(13,42) OR DmLoaiBannerREF IN (17,18))
						AND ISNULL(DmLoaiNenTangREF,0) <> 8),0)

		 SELECT @DmNhanHangNew = COALESCE(@DmNhanHangNew + ',', '') + ISNULL(CAST(T.DmNhanHangREF AS VARCHAR(1000)),'')
		 FROM   (
					SELECT DISTINCT DmNhanHangREF FROM dbo.ThucChayHopDongChiTiet
					WHERE  1=1
					AND HopDongChiTietREF = @PhanBoID AND DeletedStatus = 0
					AND ThucChayHopDongChiTietID = @ThucChayHopDongChiTietID
				) T         
 
		SELECT top 1 @DmWebsiteREF = DmWebsiteREF
					, @TenWebsite = TenWebsite 
		FROM dbo.ThucChayHopDongChiTiet
					WHERE  1=1
					AND HopDongChiTietREF = @PhanBoID AND DeletedStatus = 0
					AND ThucChayHopDongChiTietID = @ThucChayHopDongChiTietID
					AND LoaiThucTreo = N'ChiPhi'
		
		SET @DmNhanHangNew = ISNULL(@DmNhanHangNew,'');

		IF(@IsHaveBanner = 0)--khong can check website
		BEGIN
		    IF((@DmNhanThucChayDaTinh <> @DmNhanHangNew) or (@DmWebsiteREF <> 265))
			BEGIN
				PRINT 'vao day'
			--DOI TRU GIAM
			   --INSERT INTO ThucChayDaTinh
				  SELECT newid() AS ID
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
				  ,0[TongViewThucChay]
				  ,0[TongClickThucChay]
				  ,0[TongSoBaiViet]
				  ,0[SoLuongThucChay]
				  ,@NgayThucHien
				  ,-sum([ThanhTienSauTrietKhauThucChay]+[GiaTriThayDoi]) [GiaTriThayDoi]
				  ,0[ThanhTienThucChayTruocTrietKhau]
				  ,0[GiaTriTrietKhauThucChay]
				  ,0[ThanhTienSauTrietKhauThucChay]
				  ,0[GiaTriHoaHongThucChay]
				  ,0[ThanhTienThucThu]
				  ,0[ThanhTienKM]
				  ,0[SoLuongThucChayKM]
				  ,0[SoLuongThucChayLechTreoHa]
				  ,0[ThanhTienLechTreoHa]
				  ,getdate()[CreatedAt]
				  ,getdate()[LastModifiedAt]
				  ,0 [IsPheDuyet]
				  ,''[PheDuyetBy]
				  ,''[PheDuyetAt]
				  ,-sum([SoLuongThucChay]+[SoLuongThayDoi])[SoLuongThayDoi]
				  ,-sum(ISNULL([SoLuongThucChayKM],0)+ ISNULL([SoLuongKMThayDoi],0))[SoLuongKMThayDoi]
				  ,-sum([ThanhTienKM]+[GiaTriKMThayDoi])[GiaTriKMThayDoi]
				  ,@GhiChu + 'UPdate NhanHang hoac Website theo thuc treo'
				  FROM (SELECT * FROM dbo.[ThucChayDaTinh] WHERE TRY_CAST(DotChayBooking AS INT) IS NOT NULL) tcdt
				  where HopDongID = @HopDongID AND HopDongChiTietREF = @PhanBoID
				 -- AND NgayThucHien >=	ISNULL((SELECT MAX(tc.NgayThucHien) FROM dbo.ThucChayDaTinh tc WHERE tc.HopDongID = @HopDongID AND tc.HopDongChiTietREF = @PhanBoID AND tc.NgayThucHien < @NgayThucHien and tc.GhiChu = 'UPdate nhan hang theo thuc treo' ),'2009-01-01')
				  AND NgayThucHien < @NgayThucHien
				  AND DotChayBooking = @ThucChayHopDongChiTietID
				  GROUP BY [HopDongID]
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
		

			---------DOI TRU TANG GIA TRI THAY DOI
			--INSERT INTO ThucChayDaTinh
				  SELECT newid() AS ID
				  ,[HopDongID]
				  ,[SoHopDong]
				  ,DmMaHopDongREF
				  ,ISNULL((SELECT top 1 hd.TenMaHopDong FROM dbo.HopDong hd WHERE hd.HopDongID = @HopDongID),'')TenMaHopDong
				  ,NgayDanhSoHopDong
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
				  ,SysNhanVienREF
				  ,ISNULL((SELECT TOP (1) hd.TenDangNhap
					  FROM dbo.HopDong hd WHERE hd.HopDongID = @HopDongID ORDER BY hd.HopDongID),'') TenDangNhap
				  ,ISNULL((SELECT TOP (1) e.TenNhanVien FROM dbo.hopdong e
					WHERE e.hopdongid = @HopDongID ORDER BY e.HopDongID ),'') TenNhanVien
				  ,TenKhachHang
				  ,@DmNhanHangNew --nhanhang
				  ,[DmNhomNganhREF]
				  ,[TenNhomNganh]
				  ,DmHinhThucQuangCao
				  ,ISNULL((SELECT TOP (1) dhtqc.TenHinhThucQuangCao 
								FROM dbo.DmHinhThucQuangCao dhtqc WHERE dhtqc.DmHinhThucQuangCaoID = DmHinhThucQuangCao ORDER BY dhtqc.DmHinhThucQuangCaoID),'') TenHinhThucQuangCao
				  ,DmSanPhamREF
				  ,ISNULL((SELECT TOP (1) dsp.TenSanPham
								FROM dbo.DmSanPham dsp WHERE dsp.DmSanPhamID = DmSanPhamREF ORDER BY dsp.DmSanPhamID),'') TenSanPham
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
				  ,dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(@DmWebsiteREF) DmWebsiteREF 
				  ,dbo.GetWebsiteLinkByDmWebsiteID(@DmWebsiteREF, @TenWebsite) TenWebsite
				  ,0[TongViewThucChay]
				  ,0[TongClickThucChay]
				  ,0[TongSoBaiViet]
				  ,0 [SoLuongThucChay]
				  ,@NgayThucHien
				  ,SUM([ThanhTienSauTrietKhauThucChay]+[GiaTriThayDoi]) GiaTriThayDoi
				  ,0[ThanhTienThucChayTruocTrietKhau]
				  ,0[GiaTriTrietKhauThucChay]
				  ,0 [ThanhTienSauTrietKhauThucChay]
				  ,0[GiaTriHoaHongThucChay]
				  ,0[ThanhTienThucThu]
				  ,SUM([ThanhTienKM]+[GiaTriKMThayDoi]) [ThanhTienKM]
				  ,SUM([SoLuongThucChayKM]+[SoLuongKMThayDoi]) [SoLuongThucChayKM]
				  ,0[SoLuongThucChayLechTreoHa]
				  ,0[ThanhTienLechTreoHa]
				  ,getdate()[CreatedAt]
				  ,getdate()[LastModifiedAt]
				  ,0 [IsPheDuyet]
				  ,''[PheDuyetBy]
				  ,''[PheDuyetAt]
				  ,SUM([SoLuongThucChay]+[SoLuongThayDoi])[SoLuongThayDoi]
				  ,0[SoLuongKMThayDoi]
				  ,0[GiaTriKMThayDoi]
				  ,@GhiChu +'Chay lai thuc chay'
				  FROM (SELECT * FROM dbo.[ThucChayDaTinh] WHERE TRY_CAST(DotChayBooking AS INT) IS NOT NULL) tcdt
				  where HopDongID = @HopDongID AND HopDongChiTietREF = @PhanBoID
				   --AND NgayThucHien >=	ISNULL((SELECT MAX(tc.NgayThucHien) FROM dbo.ThucChayDaTinh tc WHERE tc.HopDongID = @HopDongID AND tc.HopDongChiTietREF = @PhanBoID AND tc.NgayThucHien < @NgayThucHien and tc.GhiChu = 'UPdate nhan hang theo thuc treo' ),'2009-01-01')
				   AND isnull(GhiChu,'') <> 'UPdate nhan hang theo thuc treo'
				   --AND isnull(GhiChu,'') <> 'PHAN BO BI XOA'
				   --AND isnull(GhiChu,'') <> 'THAY DOI DANH SACH NHAN HANG'
				   AND NgayThucHien < @NgayThucHien
				   AND tcdt.DotChayBooking = @ThucChayHopDongChiTietID
				   GROUP BY [HopDongID]
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
				  --,DmWebsiteREF
				  --,TenWebsite
				 

		
		END
		END
		ELSE
		BEGIN
			SET @DmBannerID = ISNULL((SELECT TOP (1) DmBannerREF FROM dbo.ThucChayHopDongChiTiet 
							WHERE ThucChayHopDongChiTietID = @ThucChayHopDongChiTietID ORDER BY ThucChayHopDongChiTietID),'')

		      IF((@DmNhanThucChayDaTinh <> @DmNhanHangNew) or (@DmWebsiteREF <> 265))
				BEGIN
					PRINT 'vao day'
				--DOI TRU GIAM
				   --INSERT INTO ThucChayDaTinh
					  SELECT newid() AS ID
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
					  ,0[TongViewThucChay]
					  ,0[TongClickThucChay]
					  ,0[TongSoBaiViet]
					  ,0[SoLuongThucChay]
					  ,@NgayThucHien
					  ,-sum([ThanhTienSauTrietKhauThucChay]+[GiaTriThayDoi]) [GiaTriThayDoi]
					  ,0[ThanhTienThucChayTruocTrietKhau]
					  ,0[GiaTriTrietKhauThucChay]
					  ,0[ThanhTienSauTrietKhauThucChay]
					  ,0[GiaTriHoaHongThucChay]
					  ,0[ThanhTienThucThu]
					  ,0[ThanhTienKM]
					  ,0[SoLuongThucChayKM]
					  ,0[SoLuongThucChayLechTreoHa]
					  ,0[ThanhTienLechTreoHa]
					  ,getdate()[CreatedAt]
					  ,getdate()[LastModifiedAt]
					  ,0 [IsPheDuyet]
					  ,''[PheDuyetBy]
					  ,''[PheDuyetAt]
					  ,-sum([SoLuongThucChay]+[SoLuongThayDoi])[SoLuongThayDoi]
					  ,-sum(ISNULL([SoLuongThucChayKM],0)+ ISNULL([SoLuongKMThayDoi],0))[SoLuongKMThayDoi]
					  ,-sum([ThanhTienKM]+[GiaTriKMThayDoi])[GiaTriKMThayDoi]
					  ,@GhiChu + 'UPdate NhanHang hoac Website theo thuc treo'
					  FROM (SELECT * FROM dbo.[ThucChayDaTinh] WHERE TRY_CAST(DotChayBooking AS INT) IS NOT NULL) tcdt
					  where HopDongID = @HopDongID AND HopDongChiTietREF = @PhanBoID
					  AND NgayThucHien >=	ISNULL((SELECT MAX(tc.NgayThucHien) FROM dbo.ThucChayDaTinh tc WHERE tc.HopDongID = @HopDongID AND tc.HopDongChiTietREF = @PhanBoID AND tc.NgayThucHien < @NgayThucHien and tc.GhiChu = 'UPdate nhan hang theo thuc treo' ),'2009-01-01')
					  AND NgayThucHien < @NgayThucHien
					  AND CONVERT(NVARCHAR(50),DmBannerREF) = @DmBannerID
					  --AND tcdt.DotChayBooking = @ThucChayHopDongChiTietID
					  GROUP BY [HopDongID]
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
		

				---------DOI TRU TANG GIA TRI THAY DOI
				--INSERT INTO ThucChayDaTinh
					  SELECT newid() AS ID
					  ,[HopDongID]
					  ,[SoHopDong]
					  ,DmMaHopDongREF
					  ,ISNULL((SELECT top 1 TenMaHopDong FROM dbo.HopDong hd WHERE hd.HopDongID = @HopDongID),'')TenMaHopDong
					  ,NgayDanhSoHopDong
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
					  ,SysNhanVienREF
					  ,(SELECT hd.TenDangNhap
						  FROM dbo.HopDong hd WHERE hd.HopDongID = @HopDongID )
					   ,ISNULL((SELECT TOP (1) e.TenNhanVien FROM dbo.hopdong e
						WHERE e.hopdongid = @HopDongID ORDER BY e.HopDongID ),'') TenNhanVien
					  ,TenKhachHang
					  ,@DmNhanHangNew --nhanhang
					  ,[DmNhomNganhREF]
					  ,[TenNhomNganh]
					  ,DmHinhThucQuangCao
					  ,(SELECT dhtqc.TenHinhThucQuangCao 
									FROM DmHinhThucQuangCao dhtqc WHERE dhtqc.DmHinhThucQuangCaoID = DmHinhThucQuangCao)
					  ,DmSanPhamREF
					  ,(SELECT dsp.TenSanPham
									FROM DmSanPham dsp WHERE dsp.DmSanPhamID = DmSanPhamREF)
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
					  ,dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(@DmWebsiteREF) DmWebsiteREF 
					  ,dbo.GetWebsiteLinkByDmWebsiteID(@DmWebsiteREF, @TenWebsite) TenWebsite
					  ,0[TongViewThucChay]
					  ,0[TongClickThucChay]
					  ,0[TongSoBaiViet]
					  ,0 [SoLuongThucChay]
					  ,@NgayThucHien
					  ,SUM([ThanhTienSauTrietKhauThucChay]+[GiaTriThayDoi]) GiaTriThayDoi
					  ,0[ThanhTienThucChayTruocTrietKhau]
					  ,0[GiaTriTrietKhauThucChay]
					  ,0 [ThanhTienSauTrietKhauThucChay]
					  ,0[GiaTriHoaHongThucChay]
					  ,0[ThanhTienThucThu]
					  ,SUM([ThanhTienKM]+[GiaTriKMThayDoi]) [ThanhTienKM]
					  ,SUM([SoLuongThucChayKM]+[SoLuongKMThayDoi]) [SoLuongThucChayKM]
					  ,0[SoLuongThucChayLechTreoHa]
					  ,0[ThanhTienLechTreoHa]
					  ,getdate()[CreatedAt]
					  ,getdate()[LastModifiedAt]
					  ,0 [IsPheDuyet]
					  ,''[PheDuyetBy]
					  ,''[PheDuyetAt]
					  ,SUM([SoLuongThucChay]+[SoLuongThayDoi])[SoLuongThayDoi]
					  ,0[SoLuongKMThayDoi]
					  ,0[GiaTriKMThayDoi]
					  ,@GhiChu +'Chay lai thuc chay'
					  FROM (SELECT * FROM dbo.[ThucChayDaTinh] WHERE TRY_CAST(DotChayBooking AS INT) IS NOT NULL) tcdt
					  where HopDongID = @HopDongID AND HopDongChiTietREF = @PhanBoID
					   AND NgayThucHien >=	ISNULL((SELECT MAX(tc.NgayThucHien) FROM dbo.ThucChayDaTinh tc WHERE tc.HopDongID = @HopDongID AND tc.HopDongChiTietREF = @PhanBoID AND tc.NgayThucHien < @NgayThucHien and tc.GhiChu = 'UPdate nhan hang theo thuc treo' ),'2009-01-01')
					   AND CONVERT(NVARCHAR(50),DmBannerREF) = @DmBannerID
					   AND NgayThucHien < @NgayThucHien
					   --AND tcdt.DotChayBooking = @ThucChayHopDongChiTietID
					   GROUP BY [HopDongID]
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
					 

			
			END
		END
		
END



```
