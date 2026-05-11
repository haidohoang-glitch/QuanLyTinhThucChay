# Stored Procedure: `sp_Insert_ThucChayDaTinh_ReInsertByHopDong_Manual`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-01-07 10:35:13.233000
- **Ngày sửa cuối**: 2017-01-07 10:35:38.153000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@SoHopDong_new` | `nvarchar(100)` | No |
| `@NgayDanhSo_new` | `datetime(8)` | No |
| `@DmNhanVienREF_new` | `int(4)` | No |
| `@DmKhachHangREF_new` | `nvarchar(400)` | No |
| `@DmSanPhamREF_new` | `int(4)` | No |
| `@DsNhanHangREF_new` | `nvarchar(400)` | No |
| `@HinhThucQuangCaoREF_new` | `int(4)` | No |
| `@TenDangNhap_new` | `nvarchar(100)` | No |
| `@MaSoHopDong_new` | `int(4)` | No |
| `@Note` | `nvarchar` | No |
| `@IsThayDoi` | `int(4)` | No |
| `@GiaTriThucChay` | `float(8)` | No |
| `@GiaTriThucChayAd` | `float(8)` | No |
| `@IsExistData` | `int(4)` | No |
| `@IsExistData1` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [dbo].[sp_Insert_ThucChayDaTinh_ReInsertByHopDong_Manual] '2016-07-28'
CREATE PROCEDURE [dbo].[sp_Insert_ThucChayDaTinh_ReInsertByHopDong_Manual]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@HopDongID INT,
	@HopDongChiTietID INT,
	@SoHopDong_new NVARCHAR(50),
	@NgayDanhSo_new DATETIME,
	@DmNhanVienREF_new INT,
	@DmKhachHangREF_new NVARCHAR(200),
	@DmSanPhamREF_new INT,
	@DsNhanHangREF_new NVARCHAR(200),
	@HinhThucQuangCaoREF_new INT, 
	@TenDangNhap_new NVARCHAR(50),
	@MaSoHopDong_new INT , 
	@Note NVARCHAR(max), 
	@IsThayDoi INT,
	@GiaTriThucChay FLOAT,
	@GiaTriThucChayAd FLOAT,
	@IsExistData INT ,
	@IsExistData1 INT  

AS
BEGIN
	

		IF(@IsThayDoi <> 4) --haidh 11/10/2016 Bo check hop dong Huy di vi da co ham chay roi.
		INSERT INTO ThucChayDaTinh
		SELECT TCDT.* FROM
		(
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
			  ,'' [DotChayHopDong]
			  ,0 [SoLuongDotChayHD]
			  ,'' [DotChayBooking]
			  ,0 [SoLuongDotChayBooking]
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
			  ,@NgayThucHien NgayThucHien
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
			  ,@Note Note
			  FROM [ThucChayDaTinh]
			  where HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietID
			  --AND NgayThucHien >=	ISNULL((SELECT MAX(tc.NgayThucHien) FROM ThucChayDaTinh tc WHERE tc.HopDongID = @HopDongID AND tc.HopDongChiTietREF = @HopDongChiTietID AND tc.NgayThucHien < @NgayThucHien and (tc.GhiChu = 'THAY DOI THONG TIN HOP DONG' OR tc.GhiChu = 'PHAN BO BI XOA' OR tc.GhiChu = 'THAY DOI DANH SACH NHAN HANG')),'2009-01-01')
			  --AND isnull(GhiChu,'') <> 'THAY DOI THONG TIN HOP DONG'
			  --AND isnull(GhiChu,'') <> 'PHAN BO BI XOA'
			  --AND isnull(GhiChu,'') <> 'THAY DOI DANH SACH NHAN HANG'
			  AND NgayThucHien < @NgayThucHien
			  AND DmSanPhamREF NOT IN (141,305,637) --Khong lam cho Dang Tin, tuyen bai, adpage
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
		)TCDT
		WHERE TCDT.GiaTriThayDoi <> 0
		
			--THAY DOI THONG TIN NHAN HANG
		if @IsThayDoi IN (3)	  
	    INSERT INTO ThucChayDaTinh
		SELECT * FROM
		(
			  SELECT newid() AS ID
			  ,[HopDongID]
			  ,[SoHopDong]
			  ,@MaSoHopDong_new DmMaHopDongREF
			  ,ISNULL((SELECT dmhdc.TenMaHopDong
			               FROM DmMaHopDongChuan dmhdc WHERE dmhdc.DmMaHopDongID = @MaSoHopDong_new),'')TenMaHopDong
			  ,@NgayDanhSo_new NgayDanhSo
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
			  ,@DmNhanVienREF_new DmNhanVienREF
			  ,(SELECT hd.TenDangNhap
			      FROM HopDong hd WHERE hd.HopDongID = @HopDongID ) TenDangNhap
			  ,(SELECT nssyll.HoVaTen
							FROM NhanSuSoYeuLyLich nssyll WHERE nssyll.NhanSuSoYeuLyLichID = @DmNhanVienREF_new) TenNhanVien
			  ,@DmKhachHangREF_new DmKhachHangREF
			  ,@DsNhanHangREF_new NhanHang --nhan hang       
			  ,[DmNhomNganhREF]
			  ,[TenNhomNganh]
			  ,@HinhThucQuangCaoREF_new DmHinhThucQuangCaoREF
			  ,(SELECT dhtqc.TenHinhThucQuangCao 
							FROM DmHinhThucQuangCao dhtqc WHERE dhtqc.DmHinhThucQuangCaoID = @HinhThucQuangCaoREF_new)TenHinhThucQuangCao
			  ,@DmSanPhamREF_new DmSanPhamREF
			  ,(SELECT dsp.TenSanPham
			                FROM DmSanPham dsp WHERE dsp.DmSanPhamID = @DmSanPhamREF_new) TenSanPham
			  ,[DmNhomWebsiteREF]
			  ,[TenNhomWebsite]
			  ,[DmChuyenMucREF]
			  ,[TenChuyenMuc]
			  ,[DmLoaiBannerREF]
			  ,[TenLoaiBanner]
			  ,[DmViTriREF]
			  ,[TenViTri]
			  ,'' [DotChayHopDong]
			  ,0 [SoLuongDotChayHD]
			  ,'' [DotChayBooking]
			  ,0 [SoLuongDotChayBooking]
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
			  ,@NgayThucHien NgayThucHien
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
			  ,('Chay lai thuc chay ' + @Note) Note
			  FROM [ThucChayDaTinh]
			  where HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietID
			   --AND NgayThucHien >=	ISNULL((SELECT MAX(tc.NgayThucHien) FROM ThucChayDaTinh tc WHERE tc.HopDongID = @HopDongID AND tc.HopDongChiTietREF = @HopDongChiTietID AND tc.NgayThucHien < @NgayThucHien and (tc.GhiChu = 'THAY DOI THONG TIN HOP DONG' OR tc.GhiChu = 'PHAN BO BI XOA' OR tc.GhiChu = 'THAY DOI DANH SACH NHAN HANG')),'2009-01-01')
			   --AND isnull(GhiChu,'') <> 'THAY DOI THONG TIN HOP DONG'
			   --AND isnull(GhiChu,'') <> 'PHAN BO BI XOA'
			   --AND isnull(GhiChu,'') <> 'THAY DOI DANH SACH NHAN HANG'
			   AND NgayThucHien < @NgayThucHien
			   AND DmSanPhamREF NOT IN (141,305,637) --Khong lam cho Dang Tin, tuyen bai, adpage
			  GROUP BY
			   [HopDongID]
			  ,[SoHopDong]
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
			  ,[TenDangNhap]
			  ,[DmNhomNganhREF]
			  ,[TenNhomNganh]
			  ,[DmNhomWebsiteREF]
			  ,[TenNhomWebsite]
			  ,[DmChuyenMucREF]
			  ,[TenChuyenMuc]
			  ,[DmLoaiBannerREF]
			  ,[TenLoaiBanner]
			  ,[DmViTriREF]
			  ,[TenViTri]
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
		)TCDT
		WHERE TCDT.GiaTriThayDoi <> 0
	
END



```
