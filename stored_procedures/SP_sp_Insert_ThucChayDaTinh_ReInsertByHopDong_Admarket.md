# Stored Procedure: `sp_Insert_ThucChayDaTinh_ReInsertByHopDong_Admarket`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-10-04 11:12:53.587000
- **Ngày sửa cuối**: 2025-07-19 11:47:47.360000

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
| `@Note` | `nvarchar(100)` | No |
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

--EXEC [dbo].[sp_Insert_ThucChayDaTinh_ReInsertByHopDong_Admarket] '2016-07-28'
CREATE PROCEDURE [dbo].[sp_Insert_ThucChayDaTinh_ReInsertByHopDong_Admarket]
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
	@Note NVARCHAR(50), 
	@IsThayDoi INT,
	@GiaTriThucChay FLOAT,
	@GiaTriThucChayAd FLOAT, 
	@IsExistData INT ,
	@IsExistData1 INT  

AS
BEGIN
		IF(@IsThayDoi IN (1,2,3) AND (isnull(@GiaTriThucChay,0) <>0 OR isnull(@GiaTriThucChayAd,0) <> 0) AND (@IsExistData > 0 OR @IsExistData1 > 0))
		BEGIN
			--if @IsThayDoi = 1 SET @Note = 'THAY DOI THONG TIN HOP DONG'
			--if @IsThayDoi = 2 SET @Note = 'PHAN BO BI XOA'
			--if @IsThayDoi = 3 SET @Note = 'THAY DOI DANH SACH NHAN HANG'
			--if @IsThayDoi = 4 SET @Note = 'HUY HOP DONG'
			-- 2. Thuc chay da tinh admarket
			INSERT INTO ThucChayDaTinhAdmarket
			SELECT * FROM
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
				  ,-sum([SoLuongThucChayKM]+[SoLuongKMThayDoi])[SoLuongKMThayDoi]
				  ,-sum([ThanhTienKM]+[GiaTriKMThayDoi])[GiaTriKMThayDoi]
				  ,@Note + ' giam ' Note
				  FROM [ThucChayDaTinhAdmarket]
				  where HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietID
				  --AND NgayThucHien >=	ISNULL((SELECT MAX(tc.NgayThucHien) FROM ThucChayDaTinh tc WHERE tc.HopDongID = @HopDongID AND tc.HopDongChiTietREF = @HopDongChiTietID AND tc.NgayThucHien < @NgayThucHien and (tc.GhiChu = 'THAY DOI THONG TIN HOP DONG' OR tc.GhiChu = 'PHAN BO BI XOA' OR tc.GhiChu = 'THAY DOI DANH SACH NHAN HANG')),'2009-01-01')
				  --AND isnull(GhiChu,'') <> 'THAY DOI THONG TIN HOP DONG'
				  --AND isnull(GhiChu,'') <> 'PHAN BO BI XOA'
				  --AND isnull(GhiChu,'') <> 'THAY DOI DANH SACH NHAN HANG'
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
			)TCDT_Admarket
			WHERE TCDT_Admarket.GiaTriThayDoi <> 0

		if @IsThayDoi IN (1)	  
	
	    INSERT INTO ThucChayDaTinhAdmarket
		SELECT * FROM
		(
			  SELECT newid() AS ID
			  ,[HopDongID]
			  ,@SoHopDong_new [SoHopDong]
			  ,@MaSoHopDong_new MaSoHopDong
			  ,ISNULL((SELECT TOP (1) hd.TenMaHopDong FROM dbo.HopDong hd WHERE hd.HopDongID = @HopDongID ORDER BY hd.HopDongID),''
						   )TenMaHopDong
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
			      FROM HopDong hd WHERE hd.HopDongID = @HopDongID )TenDangNhap
			  ,ISNULL((SELECT nssyll.HoVaTen
							FROM NhanSuSoYeuLyLich nssyll WHERE nssyll.NhanSuSoYeuLyLichID = @DmNhanVienREF_new
							),'') AS TenNhanVien
			  ,@DmKhachHangREF_new DmKhachHangREF
			 , [NhanHang]
			  ,[DmNhomNganhREF]
			  ,[TenNhomNganh]
			  ,@HinhThucQuangCaoREF_new HinhThucQuangCaoREF
			  ,(SELECT dhtqc.TenHinhThucQuangCao 
							FROM DmHinhThucQuangCao dhtqc WHERE dhtqc.DmHinhThucQuangCaoID = @HinhThucQuangCaoREF_new
							)TenHinhThucQuangCao
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
			  ,(@Note + ' Chay lai thuc chay tang') Note
			  FROM [ThucChayDaTinhAdmarket]
			  where HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietID
			   --AND NgayThucHien >=	ISNULL((SELECT MAX(tc.NgayThucHien) FROM ThucChayDaTinh tc WHERE tc.HopDongID = @HopDongID AND tc.HopDongChiTietREF = @HopDongChiTietID AND tc.NgayThucHien < @NgayThucHien and (tc.GhiChu = 'THAY DOI THONG TIN HOP DONG' OR tc.GhiChu = 'PHAN BO BI XOA' OR tc.GhiChu = 'THAY DOI DANH SACH NHAN HANG')),'2009-01-01')
			   --AND isnull(GhiChu,'') <> 'THAY DOI THONG TIN HOP DONG'
			   --AND isnull(GhiChu,'') <> 'PHAN BO BI XOA'
			   --AND isnull(GhiChu,'') <> 'THAY DOI DANH SACH NHAN HANG'
			   AND NgayThucHien < @NgayThucHien
			  GROUP BY
			   [HopDongID]
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
			  ,[NhanHang]
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
			)TCDT_Admarket
			WHERE ISNULL(TCDT_Admarket.GiaTriThayDoi,0) <> 0


		

		END

	
END



```
