# Stored Procedure: `sp_Insert_ThucChayDaTinh_ReInsertByHopDong_NhanHang_PR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2019-05-31 16:19:10.997000
- **Ngày sửa cuối**: 2019-05-31 16:59:15.020000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@ThucChayHopDongChiTietPRID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [sp_Insert_ThucChayDaTinh_ReInsertByHopDong_NhanHang_PR] '2019-05-30', 40969,	91354
CREATE PROCEDURE [dbo].[sp_Insert_ThucChayDaTinh_ReInsertByHopDong_NhanHang_PR]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@HopDongID INT,
	@DmSanPhamREF INT,
	@ThucChayHopDongChiTietPRID INT
AS
BEGIN
		-- SET NOCOUNT ON added to prevent extra result sets from
		-- interfering with SELECT statements.
		 DECLARE @GhiChu NVARCHAR(200) ='NH_TREO_TD: ', @DmNhanThucChayDaTinh NVARCHAR(200) = ''
		 DECLARE @DmNhanHangNew NVARCHAR(200)

		 SET @DmNhanThucChayDaTinh = 
		 ISNULL((
			SELECT TOP (1) ISNULL(NhanHang,'') FROM dbo.ThucChayDaTinh
			WHERE 1=1
			AND DmSanPhamREF IN (141,637)
			AND NgayThucHien < @NgayThucHien
			AND HopDongID = @HopDongID
			AND DmSanPhamREF = @DmSanPhamREF
			AND DotChayBooking = CONVERT(NVARCHAR(50),@ThucChayHopDongChiTietPRID)
			ORDER BY NgayThucHien DESC, LastModifiedAt DESC
		 ),'')
		 
	

		 SELECT @DmNhanHangNew = COALESCE(@DmNhanHangNew + ',', '') + ISNULL(CAST(T.DmNhanHangREF AS VARCHAR(1000)),'')
		 FROM   (
					SELECT DISTINCT DmNhanHangREF FROM dbo.ThucChayHopDongChiTietPR
					WHERE  1=1
					AND HopDongREF = @HopDongID AND DeletedStatus = 0
					AND DmSanPhamREF = @DmSanPhamREF
					AND ThucChayHopDongChiTietPRID = @ThucChayHopDongChiTietPRID
				) T         
 
		SET @DmNhanHangNew = ISNULL(@DmNhanHangNew,'');
		

		IF(@DmNhanThucChayDaTinh <> @DmNhanHangNew)
		BEGIN
			PRINT 'vao day'
			PRINT @ThucChayHopDongChiTietPRID
			--DOI TRU GIAM
			INSERT INTO dbo.ThucChayDaTinh
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
				,@GhiChu + 'UPdate nhan hang theo thuc treo PR'
				FROM dbo.[ThucChayDaTinh]
				where HopDongID = @HopDongID AND DmSanPhamREF IN (141,637)
				AND NgayThucHien >=	ISNULL((SELECT MAX(tc.NgayThucHien) FROM dbo.ThucChayDaTinh tc WHERE tc.HopDongID = @HopDongID AND tc.DmSanPhamREF IN (141,637) AND tc.NgayThucHien < @NgayThucHien and tc.GhiChu = 'UPdate nhan hang theo thuc treo PR' ),'2009-01-01')
				AND NgayThucHien < @NgayThucHien
				AND DotChayBooking = CONVERT(NVARCHAR(50),@ThucChayHopDongChiTietPRID)
				AND DmSanPhamREF = @DmSanPhamREF
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
				,ISNULL((SELECT dmhdc.TenMaHopDong
							FROM dbo.DmMaHopDongChuan dmhdc WHERE dmhdc.DmMaHopDongID = DmMaHopDongREF),'')TenMaHopDong
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
				,(SELECT nssyll.HoVaTen
							FROM NhanSuSoYeuLyLich nssyll WHERE nssyll.NhanSuSoYeuLyLichID = SysNhanVienREF)
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
				,[DmWebsiteREF]
				,[TenWebsite]
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
				,@GhiChu +'Chay lai thuc chay thay doi nhan hang pr: ' + CONVERT(NVARCHAR(50),@ThucChayHopDongChiTietPRID)
				FROM dbo.[ThucChayDaTinh]
				where HopDongID = @HopDongID AND DmSanPhamREF IN (141,637)
				AND NgayThucHien >=	ISNULL((SELECT MAX(tc.NgayThucHien) FROM dbo.ThucChayDaTinh tc WHERE tc.HopDongID = @HopDongID AND tc.DmSanPhamREF IN (141,637) AND tc.NgayThucHien < @NgayThucHien and tc.GhiChu = 'UPdate nhan hang theo thuc treo PR' ),'2009-01-01')
				AND isnull(GhiChu,'') <> 'UPdate nhan hang theo thuc treo PR'
				AND DotChayBooking = CONVERT(NVARCHAR(50),@ThucChayHopDongChiTietPRID)
				AND NgayThucHien < @NgayThucHien
				AND DmSanPhamREF = @DmSanPhamREF
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

		
	END
		
		
END



```
