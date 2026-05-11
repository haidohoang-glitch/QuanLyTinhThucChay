# Stored Procedure: `sp_Insert_ThucChayDaTinh_ReInsertByHopDong_ThucTreoThayDoi_CPD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2025-12-18 11:36:19.967000
- **Ngày sửa cuối**: 2025-12-18 11:42:55.763000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@PhanBoID` | `int(4)` | No |
| `@NhanHangMoi` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [dbo].[sp_Insert_ThucChayDaTinh_ReInsertByHopDong_ThucTreoThayDoi_CPD] '2016-09-29', 40969,	91354
CREATE PROCEDURE [dbo].[sp_Insert_ThucChayDaTinh_ReInsertByHopDong_ThucTreoThayDoi_CPD]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@HopDongID INT,
	@PhanBoID INT,
	@NhanHangMoi INT
	
AS
BEGIN
		-- SET NOCOUNT ON added to prevent extra result sets from
		-- interfering with SELECT statements.
		 DECLARE @GhiChu NVARCHAR(200) ='THUC_TREO_TD CPD: THAY DOI THONG TIN NHAN HANG ', @CONTENT_LOG NVARCHAR(300), @DmNhanThucChayDaTinh NVARCHAR(200) = ''
		 ----CAI NAY DUNG CHO CHOT CUOI NAM 2016
		 DECLARE @IsHaveBanner SMALLINT = 0, @DmBannerID NVARCHAR(100) = 0
		 DECLARE @DmNhanHangNew NVARCHAR(200), @DmWebsiteREF int, @TenWebsite nvarchar(200) = N''

		 SET @DmNhanHangNew = CAST(@NhanHangMoi AS NVARCHAR(200))
		 --CHECK THONG TIN DMNHANHANG BI TRUNG NHAU GIUA THUCCHAYDATINH VA LOG THUC TREO
		 SET @DmNhanThucChayDaTinh = 
		 ISNULL((
			SELECT TOP 1 NhanHang FROM dbo.ThucChayDaTinh
			WHERE HopDongChiTietREF = @PhanBoID
			AND NgayThucHien < @NgayThucHien
			ORDER BY NgayThucHien DESC, LastModifiedAt DESC
		 ),'')
		 
		

		 IF(@DmNhanThucChayDaTinh <> @DmNhanHangNew)
			BEGIN
				PRINT 'vao day'
			--DOI TRU GIAM
			   INSERT INTO ThucChayDaTinh
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
				  ,@GhiChu + 'DOI TRU GIAM Phanbo'
				  FROM dbo.[ThucChayDaTinh]
				  WHERE HopDongID = @HopDongID AND HopDongChiTietREF = @PhanBoID
				  AND NgayThucHien < @NgayThucHien
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
			INSERT INTO ThucChayDaTinh
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
				  ,@GhiChu +'Chay lai thuc chay phan bo'
				  FROM (SELECT * FROM dbo.[ThucChayDaTinh] WHERE TRY_CAST(DotChayBooking AS INT) IS NOT NULL) tcdt
				  where HopDongID = @HopDongID AND HopDongChiTietREF = @PhanBoID
				   AND NgayThucHien < @NgayThucHien
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



```
