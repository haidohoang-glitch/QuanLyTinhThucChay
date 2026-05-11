# Stored Procedure: `sp_Insert_ThucChayDaTinh_ReInsertByHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-10-04 11:06:03.417000
- **Ngày sửa cuối**: 2025-07-19 11:47:32.077000

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

--EXEC [dbo].[sp_Insert_ThucChayDaTinh_ReInsertByHopDong] '2016-07-28'
CREATE PROCEDURE [dbo].[sp_Insert_ThucChayDaTinh_ReInsertByHopDong]
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
	
		IF(@IsThayDoi <> 0 AND (isnull(@GiaTriThucChay,0) <>0 OR isnull(@GiaTriThucChayAd,0) <> 0) AND (@IsExistData > 0 OR @IsExistData1 > 0))
		BEGIN
		-- cap nhat lai du lieu da tinh
		-- 1. Thuc chay da tinh
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
			  ,[DotChayHopDong] [DotChayHopDong]
			  ,0 [SoLuongDotChayHD]
			 -- ,(
				--CASE WHEN (DmHinhThucQuangCao = 13 OR DmLoaiBannerREF = 18) THEN [DotChayBooking]
				--ELSE ''
				--END
			 -- ) AS [DotChayBooking]
			 , [DotChayBooking]
			 , [SoLuongDotChayBooking]
			 -- , (
				--CASE WHEN (DmHinhThucQuangCao = 13 OR DmLoaiBannerREF = 18) THEN [SoLuongDotChayBooking]
				--ELSE 0
				--END
			 -- ) AS  [SoLuongDotChayBooking]
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
			  FROM dbo.[ThucChayDaTinh]
			  where HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietID
			  --AND NgayThucHien >=	ISNULL((SELECT MAX(tc.NgayThucHien) FROM ThucChayDaTinh tc WHERE tc.HopDongID = @HopDongID AND tc.HopDongChiTietREF = @HopDongChiTietID AND tc.NgayThucHien < @NgayThucHien and (tc.GhiChu = 'THAY DOI THONG TIN HOP DONG' OR tc.GhiChu = 'PHAN BO BI XOA' OR tc.GhiChu = 'THAY DOI DANH SACH NHAN HANG')),'2009-01-01')
			  --AND isnull(GhiChu,'') <> 'THAY DOI THONG TIN HOP DONG'
			  --AND isnull(GhiChu,'') <> 'PHAN BO BI XOA'
			  --AND isnull(GhiChu,'') <> 'THAY DOI DANH SACH NHAN HANG'
			  AND NgayThucHien < @NgayThucHien
			  AND  NOT ((DmSanPhamREF IN (141,305,637)) AND NOT (DmHinhThucQuangCao = 13 OR DmLoaiBannerREF = 18))  --Khong lam cho Dang Tin, tuyen bai, adpage
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
			  , [DotChayBooking]
			  , [SoLuongDotChayBooking]
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
		
		------------
		if @IsThayDoi IN (1)	  
	    INSERT INTO ThucChayDaTinh
		SELECT * FROM
		(
			  SELECT newid() AS ID
			  ,tcdt.[HopDongID]
			  ,@SoHopDong_new [SoHopDong]
			  ,@MaSoHopDong_new DmMaHopDongREF
			  ,ISNULL((SELECT TOP (1) hd.TenMaHopDong FROM dbo.HopDong hd WHERE hd.HopDongID = @HopDongID ORDER BY hd.HopDongID),'')TenMaHopDong
			  ,@NgayDanhSo_new NgayDanhSo
			  ,[NgayKyHopDong]
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
			  ,@DmNhanVienREF_new DmNhanVienREF
			  ,ISNULL((SELECT TOP (1) hd.TenDangNhap
			      FROM HopDong hd WHERE hd.HopDongID = @HopDongID ORDER BY hd.HopDongID),'') TenDangNhap
			  ,ISNULL((SELECT TOP (1) e.FULL_NAME FROM asdag2.HRM.dbo.EMPLOYEES e
						WHERE e.ID = @DmNhanVienREF_new ORDER BY e.ID ),'') TenNhanVien
			  ,@DmKhachHangREF_new DmKhachHangREF
			  ,tcdt.[NhanHang] --nhan hang       
			  ,tcdt.[DmNhomNganhREF]
			  ,tcdt.[TenNhomNganh]
			  ,@HinhThucQuangCaoREF_new DmHinhThucQuangCaoREF
			  ,ISNULL((SELECT TOP (1) dhtqc.TenHinhThucQuangCao 
							FROM dbo.DmHinhThucQuangCao dhtqc WHERE dhtqc.DmHinhThucQuangCaoID = @HinhThucQuangCaoREF_new ORDER BY dhtqc.DmHinhThucQuangCaoID),'') TenHinhThucQuangCao
			  ,(case when @DmSanPhamREF_new = 733 then tcdt.[DmSanPhamREF]
				 else @DmSanPhamREF_new
			  end) DmSanPhamREF
			  ,(case when @DmSanPhamREF_new = 733 then tcdt.[TenSanPham]
				 else ISNULL((SELECT TOP (1) dsp.TenSanPham
			                FROM DmSanPham dsp WHERE dsp.DmSanPhamID = @DmSanPhamREF_new ORDER BY dsp.DmSanPhamID),'')
			  end) TenSanPham
			  ,tcdt.[DmNhomWebsiteREF]
			  ,tcdt.[TenNhomWebsite]
			  ,tcdt.[DmChuyenMucREF]
			  ,tcdt.[TenChuyenMuc]
			  ,tcdt.[DmLoaiBannerREF]
			  ,tcdt.[TenLoaiBanner]
			  ,tcdt.[DmViTriREF]
			  ,tcdt.[TenViTri]
			  ,tcdt.[DotChayHopDong] [DotChayHopDong]
			  ,0 [SoLuongDotChayHD]
			  , tcdt.[DotChayBooking]
			  , tcdt.[SoLuongDotChayBooking]
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
			  ,0[TongViewThucChay]
			  ,0[TongClickThucChay]
			  ,0[TongSoBaiViet]
			  ,0 [SoLuongThucChay]
			  ,@NgayThucHien NgayThucHien
			  ,SUM(tcdt.[ThanhTienSauTrietKhauThucChay]+tcdt.[GiaTriThayDoi]) GiaTriThayDoi
			  ,0[ThanhTienThucChayTruocTrietKhau]
			  ,0[GiaTriTrietKhauThucChay]
			  ,0 [ThanhTienSauTrietKhauThucChay]
			  ,0[GiaTriHoaHongThucChay]
			  ,0[ThanhTienThucThu]
			  ,SUM(tcdt.[ThanhTienKM]+tcdt.[GiaTriKMThayDoi]) [ThanhTienKM]
			  ,SUM(tcdt.[SoLuongThucChayKM]+tcdt.[SoLuongKMThayDoi]) [SoLuongThucChayKM]
			  ,0[SoLuongThucChayLechTreoHa]
			  ,0[ThanhTienLechTreoHa]
			  ,getdate()[CreatedAt]
			  ,getdate()[LastModifiedAt]
			  ,0 [IsPheDuyet]
			  ,''[PheDuyetBy]
			  ,''[PheDuyetAt]
			  ,SUM(tcdt.[SoLuongThucChay]+tcdt.[SoLuongThayDoi])[SoLuongThayDoi]
			  ,0[SoLuongKMThayDoi]
			  ,0[GiaTriKMThayDoi]
			  ,('Chay lai thuc chay ' + @Note) Note
			  FROM dbo.[ThucChayDaTinh] tcdt
			  where HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietID
			   --AND NgayThucHien >=	ISNULL((SELECT MAX(tc.NgayThucHien) FROM ThucChayDaTinh tc WHERE tc.HopDongID = @HopDongID AND tc.HopDongChiTietREF = @HopDongChiTietID AND tc.NgayThucHien < @NgayThucHien and (tc.GhiChu = 'THAY DOI THONG TIN HOP DONG' OR tc.GhiChu = 'PHAN BO BI XOA' OR tc.GhiChu = 'THAY DOI DANH SACH NHAN HANG')),'2009-01-01')
			   --AND isnull(GhiChu,'') <> 'THAY DOI THONG TIN HOP DONG'
			   --AND isnull(GhiChu,'') <> 'PHAN BO BI XOA'
			   --AND isnull(GhiChu,'') <> 'THAY DOI DANH SACH NHAN HANG'
			   AND NgayThucHien < @NgayThucHien
			   AND not (NgayThucHien = @NgayThucHien AND GhiChu = @Note)
			   AND NOT (DmSanPhamREF IN (141,305,637) AND NOT (DmHinhThucQuangCao = 13 OR DmLoaiBannerREF = 18)) --Khong lam cho Dang Tin, tuyen bai, adpage
			   AND (@HinhThucQuangCaoREF_new <> 13)
			  GROUP BY
			   tcdt.[HopDongID]
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
			  ,tcdt.[TenDangNhap]
			  ,tcdt.[NhanHang]
			  ,tcdt.[DmNhomNganhREF]
			  ,tcdt.[TenNhomNganh]
			  ,tcdt.[DmNhomWebsiteREF]
			  ,tcdt.[TenNhomWebsite]
			  ,tcdt.[DmChuyenMucREF]
			  ,tcdt.[TenChuyenMuc]
			  ,tcdt.[DmLoaiBannerREF]
			  ,tcdt.[TenLoaiBanner]
			  ,tcdt.[DmViTriREF]
			  ,tcdt.[TenViTri]
			  ,tcdt.[DotChayHopDong]
			  , tcdt.[DotChayBooking]
			  , tcdt.[SoLuongDotChayBooking]
			 -- ,(
				--CASE WHEN (DmHinhThucQuangCao = 13 OR DmLoaiBannerREF = 18) THEN [DotChayBooking]
				--ELSE ''
				--END
			 -- )
			 -- , (
				--CASE WHEN (DmHinhThucQuangCao = 13 OR DmLoaiBannerREF = 18) THEN [SoLuongDotChayBooking]
				--ELSE 0
				--END
			 -- ) 
			 , tcdt.Dmsanphamref
			 , tcdt.tensanpham
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
			  ,ISNULL((SELECT TOP (1) hd.TenMaHopDong FROM dbo.HopDong hd WHERE hd.HopDongID = @HopDongID ORDER BY hd.HopDongID),'')TenMaHopDong
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
			  ,ISNULL((SELECT TOP (1) hd.TenDangNhap
			      FROM dbo.HopDong hd WHERE hd.HopDongID = @HopDongID ORDER BY hd.HopDongID),'') TenDangNhap
			  ,ISNULL((SELECT TOP (1) e.FULL_NAME FROM asdag2.HRM.dbo.EMPLOYEES e
					WHERE e.ID = @DmNhanVienREF_new ORDER BY E.id),'') TenNhanVien
			  ,@DmKhachHangREF_new DmKhachHangREF
			  ,@DsNhanHangREF_new NhanHang --nhan hang       
			  ,[DmNhomNganhREF]
			  ,[TenNhomNganh]
			  ,@HinhThucQuangCaoREF_new DmHinhThucQuangCaoREF
			  ,ISNULL((SELECT TOP (1) dhtqc.TenHinhThucQuangCao 
							FROM dbo.DmHinhThucQuangCao dhtqc WHERE dhtqc.DmHinhThucQuangCaoID = @HinhThucQuangCaoREF_new ORDER BY dhtqc.DmHinhThucQuangCaoID),'') TenHinhThucQuangCao
			  ,(case when @DmSanPhamREF_new = 733 then [DmSanPhamREF]
				 else @DmSanPhamREF_new
			  end) DmSanPhamREF
			  ,(case when @DmSanPhamREF_new = 733 then [TenSanPham]
				 else ISNULL((SELECT TOP (1) dsp.TenSanPham
			                FROM DmSanPham dsp WHERE dsp.DmSanPhamID = @DmSanPhamREF_new ORDER BY dsp.DmSanPhamID),'')
			  end) TenSanPham
			  ,[DmNhomWebsiteREF]
			  ,[TenNhomWebsite]
			  ,[DmChuyenMucREF]
			  ,[TenChuyenMuc]
			  ,[DmLoaiBannerREF]
			  ,[TenLoaiBanner]
			  ,[DmViTriREF]
			  ,[TenViTri]
			  ,[DotChayHopDong] [DotChayHopDong]
			  ,0 [SoLuongDotChayHD]
			  ,[DotChayBooking] AS [DotChayBooking]
			  ,[SoLuongDotChayBooking]AS  [SoLuongDotChayBooking]
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
			  FROM dbo.[ThucChayDaTinh]
			  where HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietID
			   --AND NgayThucHien >=	ISNULL((SELECT MAX(tc.NgayThucHien) FROM ThucChayDaTinh tc WHERE tc.HopDongID = @HopDongID AND tc.HopDongChiTietREF = @HopDongChiTietID AND tc.NgayThucHien < @NgayThucHien and (tc.GhiChu = 'THAY DOI THONG TIN HOP DONG' OR tc.GhiChu = 'PHAN BO BI XOA' OR tc.GhiChu = 'THAY DOI DANH SACH NHAN HANG')),'2009-01-01')
			   --AND isnull(GhiChu,'') <> 'THAY DOI THONG TIN HOP DONG'
			   --AND isnull(GhiChu,'') <> 'PHAN BO BI XOA'
			   --AND isnull(GhiChu,'') <> 'THAY DOI DANH SACH NHAN HANG'
			   AND NgayThucHien < @NgayThucHien
			   AND not (NgayThucHien = @NgayThucHien AND GhiChu = @Note)
			   AND  NOT ((DmSanPhamREF IN (141,305,637)) AND NOT (DmHinhThucQuangCao = 13 OR DmLoaiBannerREF = 18))  --Khong lam cho Dang Tin, tuyen bai, adpage
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
			  ,[DotChayHopDong]
			  ,[DotChayBooking]
			  ,[SoLuongDotChayBooking]
			  ,[Dmsanphamref]
			  ,[Tensanpham]
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

		------------- Admatic
		IF @IsThayDoi IN (5) 
		INSERT INTO ThucChayDaTinh
		SELECT TCDT.* FROM
		(
			  SELECT newid() AS ID
			  ,[HopDongID]
			  ,@SoHopDong_new SoHopDong
			  ,@MaSoHopDong_new DmMaHopDongREF
			  ,[TenMaHopDong]
			  ,@NgayDanhSo_new NgayDanhSoHopDong
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
			  ,@DmNhanVienREF_new SysNhanVienREF
			  ,@TenDangNhap_new TenDangNhap
			  ,TenNhanVien
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
			  ,[DotChayHopDong] [DotChayHopDong]
			  ,0 [SoLuongDotChayHD]
			  ,[DotChayBooking] AS [DotChayBooking]
			  ,[SoLuongDotChayBooking] AS  [SoLuongDotChayBooking]
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
			  ,sum([ThanhTienSauTrietKhauThucChay]+[GiaTriThayDoi]) [GiaTriThayDoi]
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
			  ,sum([SoLuongThucChay]+[SoLuongThayDoi])[SoLuongThayDoi]
			  ,sum(ISNULL([SoLuongThucChayKM],0)+ ISNULL([SoLuongKMThayDoi],0))[SoLuongKMThayDoi]
			  ,sum([ThanhTienKM]+[GiaTriKMThayDoi])[GiaTriKMThayDoi]
			  ,N'sp_Insert_ThucChayDaTinh_ReInsertByHopDong - Admatic - Thay Doi HD' Note
			  FROM dbo.[ThucChayDaTinh] TC
			  where TC.HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietID
			  AND NgayThucHien < @NgayThucHien
			  AND not (NgayThucHien = @NgayThucHien AND TC.GhiChu = @Note)
			  AND NOT (DmSanPhamREF IN (141,305,637) AND NOT (DmHinhThucQuangCao = 13 OR DmLoaiBannerREF = 18))--Khong lam cho Dang Tin, tuyen bai, adpage
			  GROUP BY TC.[HopDongID]
			  ,[TenMaHopDong]
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
		)TCDT
		WHERE TCDT.GiaTriThayDoi <> 0

	END
	
END



```
