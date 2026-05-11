# Stored Procedure: `ThucChay_Insert_GTTD_ThuocTinh_DoiTruGiamTinhLai_ThanhTien_GGFB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-12-01 16:20:59.843000
- **Ngày sửa cuối**: 2020-12-01 16:23:41.510000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayGhiNhanThucChay` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

/*
[dbo].[ThucChay_Insert_GTTD_DoiTruGiam_ThucChayDaTinh_ByHD_ThanhTien_GGFB] 
	@NgayGhiNhanThucChay DATETIME,
	@HopDongID INT,
	@HopDongChiTietID INT,
	@DmSanPhamREF INT,
	@GhiChu NVARCHAR(1000)
*/


CREATE  PROCEDURE [dbo].[ThucChay_Insert_GTTD_ThuocTinh_DoiTruGiamTinhLai_ThanhTien_GGFB] 
	@NgayGhiNhanThucChay DATETIME,
	@HopDongID INT,
	@HopDongChiTietID INT
AS
BEGIN
		DECLARE @GhiChuTinhLai NVARCHAR(1000),
			@GhiChu NVARCHAR(1000)

		DECLARE @DanhSachNhanHang_new nvarchar(100)
		SET @GhiChu = N'Doi tru ggfb thay doi thuoc tinh: ' + convert(nvarchar(100), @HopDongChiTietID) + convert(nvarchar(100),@NgayGhiNhanThucChay,103)
		SET @GhiChuTinhLai = N'Tinh lai ggfb thay doi thuoc tinh: ' + convert(nvarchar(100), @HopDongChiTietID) + convert(nvarchar(100),@NgayGhiNhanThucChay,103)

		SELECT Top (1) @DanhSachNhanHang_new = hdct.DanhSachNhanHangREF FROM dbo.HopDongChiTiet hdct
		WHERE hdct.HopDongChiTietID = @HopDongChiTietID
		ORDER BY hdct.HopDongChiTietID

		SET @DanhSachNhanHang_new = ISNULL(@DanhSachNhanHang_new,'')

		--1. DOI TRU GIAM CHO dbo.ThucChayDaTinh
		INSERT INTO dbo.ThucChayDaTinh
		(
		    ThucChayDaTinhID,
		    HopDongID,
		    SoHopDong,
		    DmMaHopDongREF,
		    TenMaHopDong,
		    NgayDanhSoHopDong,
		    NgayKyHopDong,
		    NhanHopDong,
		    NgayNhanBanFax,
		    NgayNhanHopDongBanCung,
		    NgayChuyenHopDongChoKeToan,
		    So,
		    Thang,
		    Nam,
		    GiaTriHopDong,
		    CongNo,
		    HopDongChiTietREF,
		    DangSuDung,
		    IsGiayPhep,
		    TrangThaiHopDong,
		    IsBanCung,
		    DmPhongBanREF,
		    TenPhongBan,
		    DmBoPhanREF,
		    TenBoPhan,
		    DmNhomLamViecREF,
		    TenNhomLamViec,
		    DmDiaDiemLamViecREF,
		    TenDiaDiemLamViec,
		    SysNhanVienREF,
		    TenDangNhap,
		    TenNhanVien,
		    TenKhachHang,
		    NhanHang,
		    DmNhomNganhREF,
		    TenNhomNganh,
		    DmHinhThucQuangCao,
		    TenHinhThucQuangCao,
		    DmSanPhamREF,
		    TenSanPham,
		    DmNhomWebsiteREF,
		    TenNhomWebsite,
		    DmChuyenMucREF,
		    TenChuyenMuc,
		    DmLoaiBannerREF,
		    TenLoaiBanner,
		    DmViTriREF,
		    TenViTri,
		    DotChayHopDong,
		    SoLuongDotChayHD,
		    DotChayBooking,
		    SoLuongDotChayBooking,
		    SoLuong,
		    DonViTinh,
		    DonGia,
		    DonGiaTheoDonVi,
		    ChietKhau,
		    GiamGia,
		    ThanhTien,
		    TiLeTuVan,
		    ChiPhiTuVan,
		    IsKhuyenMai,
		    KhuyenMai,
		    DmBannerREF,
		    DmChienDichREF,
		    DmWebsiteREF,
		    TenWebsite,
		    TongViewThucChay,
		    TongClickThucChay,
		    TongSoBaiViet,
		    SoLuongThucChay,
		    NgayThucHien,
		    GiaTriThayDoi,
		    ThanhTienThucChayTruocTrietKhau,
		    GiaTriTrietKhauThucChay,
		    ThanhTienSauTrietKhauThucChay,
		    GiaTriHoaHongThucChay,
		    ThanhTienThucThu,
		    ThanhTienKM,
		    SoLuongThucChayKM,
		    SoLuongThucChayLechTreoHa,
		    ThanhTienLechTreoHa,
		    CreatedAt,
		    LastModifiedAt,
		    IsPheDuyet,
		    PheDuyetBy,
		    PheDuyetAt,
		    SoLuongThayDoi,
		    SoLuongKMThayDoi,
		    GiaTriKMThayDoi,
		    GhiChu
		)
		SELECT NEWID() AS ThucChayDaTinhID,
		    HopDongID,
		    SoHopDong,
		    DmMaHopDongREF,
		    TenMaHopDong,
		    NgayDanhSoHopDong,
		    NgayKyHopDong,
		    NhanHopDong,
		    NgayNhanBanFax,
		    NgayNhanHopDongBanCung,
		    NgayChuyenHopDongChoKeToan,
		    So,
		    Thang,
		    Nam,
		    GiaTriHopDong,
		    CongNo,
		    HopDongChiTietREF,
		    DangSuDung,
		    IsGiayPhep,
		    TrangThaiHopDong,
		    IsBanCung,
		    DmPhongBanREF,
		    TenPhongBan,
		    DmBoPhanREF,
		    TenBoPhan,
		    DmNhomLamViecREF,
		    TenNhomLamViec,
		    DmDiaDiemLamViecREF,
		    TenDiaDiemLamViec,
		    SysNhanVienREF,
		    TenDangNhap,
		    TenNhanVien,
		    TenKhachHang,
		    NhanHang,
		    DmNhomNganhREF,
		    TenNhomNganh,
		    DmHinhThucQuangCao,
		    TenHinhThucQuangCao,
		    DmSanPhamREF,
		    TenSanPham,
		    DmNhomWebsiteREF,
		    TenNhomWebsite,
		    DmChuyenMucREF,
		    TenChuyenMuc,
		    DmLoaiBannerREF,
		    TenLoaiBanner,
		    DmViTriREF,
		    TenViTri,
		    DotChayHopDong,
		    0 SoLuongDotChayHD,
		    DotChayBooking ,
		    SoLuongDotChayBooking ,
		    SoLuong,
		    DonViTinh,
		    DonGia,
		    DonGiaTheoDonVi,
		    ChietKhau,
		    GiamGia,
		    ThanhTien,
		    TiLeTuVan,
		    ChiPhiTuVan,
		    IsKhuyenMai,
		    KhuyenMai,
		    DmBannerREF,
		    DmChienDichREF,
		    DmWebsiteREF,
		    TenWebsite,
		    0 TongViewThucChay,
		    0 TongClickThucChay,
		    0 TongSoBaiViet,
		    0 AS SoLuongThucChay,
		    @NgayGhiNhanThucChay AS NgayThucHien,
		    -SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS GiaTriThayDoi,
		    0 AS ThanhTienThucChayTruocTrietKhau,
		    0 AS GiaTriTrietKhauThucChay,
		    0 AS ThanhTienSauTrietKhauThucChay,
		    0 AS GiaTriHoaHongThucChay,
		    0 AS ThanhTienThucThu,
		    0 AS ThanhTienKM,
		    0 AS SoLuongThucChayKM,
		    -SUM(SoLuongThucChayLechTreoHa) AS SoLuongThucChayLechTreoHa,
		    -SUM(ThanhTienLechTreoHa) AS ThanhTienLechTreoHa,
		    GETDATE() CreatedAt,
		    GETDATE() LastModifiedAt,
		    0 IsPheDuyet,
		    '' PheDuyetBy,
		    '' PheDuyetAt,
		    -SUM(SoLuongThucChay + SoLuongThayDoi) AS SoLuongThayDoi,
		    -SUM(SoLuongThucChayKM + SoLuongKMThayDoi) AS SoLuongKMThayDoi,
		    -SUM(ThanhTienKM + GiaTriKMThayDoi) AS GiaTriKMThayDoi,
		    @GhiChu GhiChu 
			FROM dbo.ThucChayDaTinh
			WHERE HopDongID = @HopDongID
			AND HopDongChiTietREF = @HopDongChiTietID
			AND not (DmHinhThucQuangCao IN(13) OR DmLoaiBannerREF IN (18))
			AND DmChienDichREF <> 0 --LOAI TRU TRUONG HOP GHI NHAN THEO CHI PHI
			--AND DmChienDichREF in (1,2) --DOI TRU CUA GGFB TINH THEO SOLUONG THUC TE VA THEO SAN LUONG CHOT
			AND NgayThucHien <= @NgayGhiNhanThucChay
			GROUP BY
			HopDongID,
		    SoHopDong,
		    DmMaHopDongREF,
		    TenMaHopDong,
		    NgayDanhSoHopDong,
		    NgayKyHopDong,
		    NhanHopDong,
		    NgayNhanBanFax,
		    NgayNhanHopDongBanCung,
		    NgayChuyenHopDongChoKeToan,
		    So,
		    Thang,
		    Nam,
		    GiaTriHopDong,
		    CongNo,
		    HopDongChiTietREF,
		    DangSuDung,
		    IsGiayPhep,
		    TrangThaiHopDong,
		    IsBanCung,
		    DmPhongBanREF,
		    TenPhongBan,
		    DmBoPhanREF,
		    TenBoPhan,
		    DmNhomLamViecREF,
		    TenNhomLamViec,
		    DmDiaDiemLamViecREF,
		    TenDiaDiemLamViec,
		    SysNhanVienREF,
		    TenDangNhap,
		    TenNhanVien,
		    TenKhachHang,
		    NhanHang,
		    DmNhomNganhREF,
		    TenNhomNganh,
		    DmHinhThucQuangCao,
		    TenHinhThucQuangCao,
		    DmSanPhamREF,
		    TenSanPham,
		    DmNhomWebsiteREF,
		    TenNhomWebsite,
		    DmChuyenMucREF,
		    TenChuyenMuc,
		    DmLoaiBannerREF,
		    TenLoaiBanner,
		    DmViTriREF,
		    TenViTri,
			DotChayHopDong,
			DotChayBooking ,
		    SoLuongDotChayBooking ,
		    SoLuong,
		    DonViTinh,
		    DonGia,
		    DonGiaTheoDonVi,
		    ChietKhau,
		    GiamGia,
		    ThanhTien,
		    TiLeTuVan,
		    ChiPhiTuVan,
		    IsKhuyenMai,
		    KhuyenMai,
		    DmBannerREF,
		    DmChienDichREF,
		    DmWebsiteREF,
		    TenWebsite
			HAVING (SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) <> 0 OR SUM(ThanhTienKM + GiaTriKMThayDoi) <> 0)

		--2. DOI TRU GIAM CHO [ThucChayDaTinh_MuaNgoai]
		INSERT INTO [dbo].[ThucChayDaTinh_MuaNgoai]
           ([HopDongREF]
           ,[SoHopDong]
           ,[DmMaHopDongREF]
           ,[NgayDanhSoHopDong]
           ,[TrangThaiHopDong]
           ,[DmNhanVienREF]
           ,[TenDangNhap]
           ,[DmPhongBanREF]
           ,[DmBoPhanREF]
           ,[DmNhomLamViecREF]
           ,[DmDiaDiemLamViecREF]
           ,[DmKhachHangREF]
           ,[HopDongChiTietREF]
           ,[LstDmNhanHangREF]
           ,[LstDmNhomNganhREF]
           ,[DmHinhThucQuangCaoREF]
           ,[DmSanPhamREF]
           ,[DmChuyenMucREF]
           ,[DmLoaiBannerREF]
           ,[DmViTriREF]
           ,[SoLuong]
           ,[DonViTinhREF]
           ,[DonGia]
           ,[ChietKhau]
           ,[ThanhTien]
           ,[IsKhuyenMai]
           ,[KhuyenMai]
           ,[ThucChayMuaNgoaiChiTietREF]
           ,[TongTienDuToanMuaSauCK]
           ,[TongTienDuToanLaiMuaSauCK]
           ,[ChietKhauMua]
           ,[DmBannerREF]
           ,[DmChienDichREF]
           ,[DmWebsiteREF]
           ,[TenWebsite]
           ,[NgayThucHien]
           ,[NgayBatDau]
           ,[NgayKetThuc]
           ,[DonViTinhThucChay]
           ,[DonGiaTheoDonViTinhTC]
           ,[TongViewClickThucChay]
           ,[TongSoBaiVietChiPhiThucChay]
           ,[SoLuongThucChay]
           ,[TongThanhTienThucChayBanSauCK]
           ,[TongThanhTienThucChayMuaSauCK]
           ,[ThanhTienLaiThucChaySauCK]
           ,[ThanhTienLaiThucChayKM]
           ,[SoLuongThucChayKM]
           ,[SoLuongThucChayLechTreoHa]
           ,[ThanhTienLechTreoHa]
           ,[GiaTriThayDoiLaiSauCK]
           ,[SoLuongThayDoi]
           ,[SoLuongKMThayDoi]
           ,[GiaTriKMLaiThayDoi]
           ,[GhiChu]
           ,[CreatedAt]
           ,[LastModifiedAt])
   
	  SELECT [HopDongREF]
		  ,[SoHopDong]
		  ,[DmMaHopDongREF]
		  ,[NgayDanhSoHopDong]
		  ,[TrangThaiHopDong]
		  ,[DmNhanVienREF]
		  ,[TenDangNhap]
		  ,[DmPhongBanREF]
		  ,[DmBoPhanREF]
		  ,[DmNhomLamViecREF]
		  ,[DmDiaDiemLamViecREF]
		  ,[DmKhachHangREF]
		  ,[HopDongChiTietREF]
		  ,[LstDmNhanHangREF]
		  ,[LstDmNhomNganhREF]
		  ,[DmHinhThucQuangCaoREF]
		  ,[DmSanPhamREF]
		  ,[DmChuyenMucREF]
		  ,[DmLoaiBannerREF]
		  ,[DmViTriREF]
		  ,[SoLuong]
		  ,[DonViTinhREF]
		  ,[DonGia]
		  ,[ChietKhau]
		  ,[ThanhTien]
		  ,[IsKhuyenMai]
		  ,[KhuyenMai]
		  ,[ThucChayMuaNgoaiChiTietREF]
		  ,[TongTienDuToanMuaSauCK]
		  ,[TongTienDuToanLaiMuaSauCK]
		  ,[ChietKhauMua]
		  ,[DmBannerREF]
		  ,[DmChienDichREF]
		  ,[DmWebsiteREF]
		  ,[TenWebsite]
		  ,@NgayGhiNhanThucChay AS [NgayThucHien]
		  ,'' [NgayBatDau]
		  ,'' [NgayKetThuc]
		  ,[DonViTinhThucChay]
		  ,[DonGiaTheoDonViTinhTC]
		  ,0 AS [TongViewClickThucChay]
		  ,0 AS [TongSoBaiVietChiPhiThucChay]
		  ,0 AS [SoLuongThucChay]
		  ,0 AS [TongThanhTienThucChayBanSauCK]
		  ,0 AS [TongThanhTienThucChayMuaSauCK]
		  ,0 AS [ThanhTienLaiThucChaySauCK]
		  ,0 AS [ThanhTienLaiThucChayKM]
		  ,0 AS [SoLuongThucChayKM]
		  ,0 AS [SoLuongThucChayLechTreoHa]
		  ,0 AS [ThanhTienLechTreoHa]
		  ,-SUM([ThanhTienLaiThucChaySauCK] + [GiaTriThayDoiLaiSauCK]) AS [GiaTriThayDoiLaiSauCK]
		  ,-SUM([SoLuongThucChay] + [SoLuongThayDoi]) AS [SoLuongThayDoi]
		  ,-SUM([SoLuongThucChayKM] + [SoLuongKMThayDoi]) AS [SoLuongKMThayDoi]
		  ,-SUM([ThanhTienLaiThucChayKM] + [GiaTriKMLaiThayDoi]) AS [GiaTriKMLaiThayDoi]
		  ,@ghiChu AS [GhiChu]
		  ,GETDATE() AS [CreatedAt] 
		  ,GETDATE() AS[LastModifiedAt]
	  FROM [dbo].[ThucChayDaTinh_MuaNgoai]
	  WHERE 1=1
	  AND HopDongREF = @HopDongID
	  AND HopDongChiTietREF = @HopDongChiTietID
	  --AND DmSanPhamREF = @DmSanPhamREF
	  AND NgayThucHien <= @NgayGhiNhanThucChay
	GROUP BY 
		 [HopDongREF]
		  ,[SoHopDong]
		  ,[DmMaHopDongREF]
		  ,[NgayDanhSoHopDong]
		  ,[TrangThaiHopDong]
		  ,[DmNhanVienREF]
		  ,[TenDangNhap]
		  ,[DmPhongBanREF]
		  ,[DmBoPhanREF]
		  ,[DmNhomLamViecREF]
		  ,[DmDiaDiemLamViecREF]
		  ,[DmKhachHangREF]
		  ,[HopDongChiTietREF]
		  ,[LstDmNhanHangREF]
		  ,[LstDmNhomNganhREF]
		  ,[DmHinhThucQuangCaoREF]
		  ,[DmSanPhamREF]
		  ,[DmChuyenMucREF]
		  ,[DmLoaiBannerREF]
		  ,[DmViTriREF]
		  ,[SoLuong]
		  ,[DonViTinhREF]
		  ,[DonGia]
		  ,[ChietKhau]
		  ,[ThanhTien]
		  ,[IsKhuyenMai]
		  ,[KhuyenMai]
		  ,[ThucChayMuaNgoaiChiTietREF]
		  ,[TongTienDuToanMuaSauCK]
		  ,[TongTienDuToanLaiMuaSauCK]
		  ,[ChietKhauMua]
		  ,[DmBannerREF]
		  ,[DmChienDichREF]
		  ,[DmWebsiteREF]
		  ,[TenWebsite]
		  ,[DonViTinhThucChay]
		  ,[DonGiaTheoDonViTinhTC]
		HAVING (SUM([ThanhTienLaiThucChaySauCK] + [GiaTriThayDoiLaiSauCK])  <> 0 OR SUM([ThanhTienLaiThucChayKM] + [GiaTriKMLaiThayDoi]) <> 0)

		--3. DOI TRU TANG CHO THONG TIN THAY DOI
		INSERT INTO dbo.ThucChayDaTinh
		(
		    ThucChayDaTinhID,
		    HopDongID,
		    SoHopDong,
		    DmMaHopDongREF,
		    TenMaHopDong,
		    NgayDanhSoHopDong,
		    NgayKyHopDong,
		    NhanHopDong,
		    NgayNhanBanFax,
		    NgayNhanHopDongBanCung,
		    NgayChuyenHopDongChoKeToan,
		    So,
		    Thang,
		    Nam,
		    GiaTriHopDong,
		    CongNo,
		    HopDongChiTietREF,
		    DangSuDung,
		    IsGiayPhep,
		    TrangThaiHopDong,
		    IsBanCung,
		    DmPhongBanREF,
		    TenPhongBan,
		    DmBoPhanREF,
		    TenBoPhan,
		    DmNhomLamViecREF,
		    TenNhomLamViec,
		    DmDiaDiemLamViecREF,
		    TenDiaDiemLamViec,
		    SysNhanVienREF,
		    TenDangNhap,
		    TenNhanVien,
		    TenKhachHang,
		    NhanHang,
		    DmNhomNganhREF,
		    TenNhomNganh,
		    DmHinhThucQuangCao,
		    TenHinhThucQuangCao,
		    DmSanPhamREF,
		    TenSanPham,
		    DmNhomWebsiteREF,
		    TenNhomWebsite,
		    DmChuyenMucREF,
		    TenChuyenMuc,
		    DmLoaiBannerREF,
		    TenLoaiBanner,
		    DmViTriREF,
		    TenViTri,
		    DotChayHopDong,
		    SoLuongDotChayHD,
		    DotChayBooking,
		    SoLuongDotChayBooking,
		    SoLuong,
		    DonViTinh,
		    DonGia,
		    DonGiaTheoDonVi,
		    ChietKhau,
		    GiamGia,
		    ThanhTien,
		    TiLeTuVan,
		    ChiPhiTuVan,
		    IsKhuyenMai,
		    KhuyenMai,
		    DmBannerREF,
		    DmChienDichREF,
		    DmWebsiteREF,
		    TenWebsite,
		    TongViewThucChay,
		    TongClickThucChay,
		    TongSoBaiViet,
		    SoLuongThucChay,
		    NgayThucHien,
		    GiaTriThayDoi,
		    ThanhTienThucChayTruocTrietKhau,
		    GiaTriTrietKhauThucChay,
		    ThanhTienSauTrietKhauThucChay,
		    GiaTriHoaHongThucChay,
		    ThanhTienThucThu,
		    ThanhTienKM,
		    SoLuongThucChayKM,
		    SoLuongThucChayLechTreoHa,
		    ThanhTienLechTreoHa,
		    CreatedAt,
		    LastModifiedAt,
		    IsPheDuyet,
		    PheDuyetBy,
		    PheDuyetAt,
		    SoLuongThayDoi,
		    SoLuongKMThayDoi,
		    GiaTriKMThayDoi,
		    GhiChu
		)
		SELECT NEWID() AS ThucChayDaTinhID,
		    HopDongID,
		    SoHopDong,
		    DmMaHopDongREF,
		    TenMaHopDong,
		    NgayDanhSoHopDong,
		    NgayKyHopDong,
		    NhanHopDong,
		    NgayNhanBanFax,
		    NgayNhanHopDongBanCung,
		    NgayChuyenHopDongChoKeToan,
		    So,
		    Thang,
		    Nam,
		    GiaTriHopDong,
		    CongNo,
		    HopDongChiTietREF,
		    DangSuDung,
		    IsGiayPhep,
		    TrangThaiHopDong,
		    IsBanCung,
		    DmPhongBanREF,
		    TenPhongBan,
		    DmBoPhanREF,
		    TenBoPhan,
		    DmNhomLamViecREF,
		    TenNhomLamViec,
		    DmDiaDiemLamViecREF,
		    TenDiaDiemLamViec,
		    SysNhanVienREF,
		    TenDangNhap,
		    TenNhanVien,
		    TenKhachHang,
		    @DanhSachNhanHang_new AS NhanHang,
		    DmNhomNganhREF,
		    TenNhomNganh,
		    DmHinhThucQuangCao,
		    TenHinhThucQuangCao,
		    DmSanPhamREF,
		    TenSanPham,
		    DmNhomWebsiteREF,
		    TenNhomWebsite,
		    DmChuyenMucREF,
		    TenChuyenMuc,
		    DmLoaiBannerREF,
		    TenLoaiBanner,
		    DmViTriREF,
		    TenViTri,
		    DotChayHopDong,
		    0 SoLuongDotChayHD,
		    DotChayBooking ,
		    SoLuongDotChayBooking ,
		    SoLuong,
		    DonViTinh,
		    DonGia,
		    DonGiaTheoDonVi,
		    ChietKhau,
		    GiamGia,
		    ThanhTien,
		    TiLeTuVan,
		    ChiPhiTuVan,
		    IsKhuyenMai,
		    KhuyenMai,
		    DmBannerREF,
		    DmChienDichREF,
		    DmWebsiteREF,
		    TenWebsite,
		    0 TongViewThucChay,
		    0 TongClickThucChay,
		    0 TongSoBaiViet,
		    0 AS SoLuongThucChay,
		    @NgayGhiNhanThucChay AS NgayThucHien,
		    -SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS GiaTriThayDoi,
		    0 AS ThanhTienThucChayTruocTrietKhau,
		    0 AS GiaTriTrietKhauThucChay,
		    0 AS ThanhTienSauTrietKhauThucChay,
		    0 AS GiaTriHoaHongThucChay,
		    0 AS ThanhTienThucThu,
		    0 AS ThanhTienKM,
		    0 AS SoLuongThucChayKM,
		    -SUM(SoLuongThucChayLechTreoHa) AS SoLuongThucChayLechTreoHa,
		    -SUM(ThanhTienLechTreoHa) AS ThanhTienLechTreoHa,
		    GETDATE() CreatedAt,
		    GETDATE() LastModifiedAt,
		    0 IsPheDuyet,
		    '' PheDuyetBy,
		    '' PheDuyetAt,
		    -SUM(SoLuongThucChay + SoLuongThayDoi) AS SoLuongThayDoi,
		    -SUM(SoLuongThucChayKM + SoLuongKMThayDoi) AS SoLuongKMThayDoi,
		    -SUM(ThanhTienKM + GiaTriKMThayDoi) AS GiaTriKMThayDoi,
		    @GhiChuTinhLai GhiChu 
			FROM dbo.ThucChayDaTinh
			WHERE HopDongID = @HopDongID
			AND HopDongChiTietREF = @HopDongChiTietID
			AND not (DmHinhThucQuangCao IN(13) OR DmLoaiBannerREF IN (18))
			AND DmChienDichREF <> 0 --LOAI TRU TRUONG HOP GHI NHAN THEO CHI PHI
			--AND DmChienDichREF in (1,2) --DOI TRU CUA GGFB TINH THEO SOLUONG THUC TE VA THEO SAN LUONG CHOT
			AND NgayThucHien <= @NgayGhiNhanThucChay
			AND GhiChu <> @GhiChu
			GROUP BY
			HopDongID,
		    SoHopDong,
		    DmMaHopDongREF,
		    TenMaHopDong,
		    NgayDanhSoHopDong,
		    NgayKyHopDong,
		    NhanHopDong,
		    NgayNhanBanFax,
		    NgayNhanHopDongBanCung,
		    NgayChuyenHopDongChoKeToan,
		    So,
		    Thang,
		    Nam,
		    GiaTriHopDong,
		    CongNo,
		    HopDongChiTietREF,
		    DangSuDung,
		    IsGiayPhep,
		    TrangThaiHopDong,
		    IsBanCung,
		    DmPhongBanREF,
		    TenPhongBan,
		    DmBoPhanREF,
		    TenBoPhan,
		    DmNhomLamViecREF,
		    TenNhomLamViec,
		    DmDiaDiemLamViecREF,
		    TenDiaDiemLamViec,
		    SysNhanVienREF,
		    TenDangNhap,
		    TenNhanVien,
		    TenKhachHang,
		    DmNhomNganhREF,
		    TenNhomNganh,
		    DmHinhThucQuangCao,
		    TenHinhThucQuangCao,
		    DmSanPhamREF,
		    TenSanPham,
		    DmNhomWebsiteREF,
		    TenNhomWebsite,
		    DmChuyenMucREF,
		    TenChuyenMuc,
		    DmLoaiBannerREF,
		    TenLoaiBanner,
		    DmViTriREF,
		    TenViTri,
			DotChayHopDong,
			DotChayBooking ,
		    SoLuongDotChayBooking ,
		    SoLuong,
		    DonViTinh,
		    DonGia,
		    DonGiaTheoDonVi,
		    ChietKhau,
		    GiamGia,
		    ThanhTien,
		    TiLeTuVan,
		    ChiPhiTuVan,
		    IsKhuyenMai,
		    KhuyenMai,
		    DmBannerREF,
		    DmChienDichREF,
		    DmWebsiteREF,
		    TenWebsite
			HAVING (SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) <> 0 OR SUM(ThanhTienKM + GiaTriKMThayDoi) <> 0)

		--4. DOI TRU TANG CHO THONG TIN THAY DOI
		INSERT INTO [dbo].[ThucChayDaTinh_MuaNgoai]
           ([HopDongREF]
           ,[SoHopDong]
           ,[DmMaHopDongREF]
           ,[NgayDanhSoHopDong]
           ,[TrangThaiHopDong]
           ,[DmNhanVienREF]
           ,[TenDangNhap]
           ,[DmPhongBanREF]
           ,[DmBoPhanREF]
           ,[DmNhomLamViecREF]
           ,[DmDiaDiemLamViecREF]
           ,[DmKhachHangREF]
           ,[HopDongChiTietREF]
           ,[LstDmNhanHangREF]
           ,[LstDmNhomNganhREF]
           ,[DmHinhThucQuangCaoREF]
           ,[DmSanPhamREF]
           ,[DmChuyenMucREF]
           ,[DmLoaiBannerREF]
           ,[DmViTriREF]
           ,[SoLuong]
           ,[DonViTinhREF]
           ,[DonGia]
           ,[ChietKhau]
           ,[ThanhTien]
           ,[IsKhuyenMai]
           ,[KhuyenMai]
           ,[ThucChayMuaNgoaiChiTietREF]
           ,[TongTienDuToanMuaSauCK]
           ,[TongTienDuToanLaiMuaSauCK]
           ,[ChietKhauMua]
           ,[DmBannerREF]
           ,[DmChienDichREF]
           ,[DmWebsiteREF]
           ,[TenWebsite]
           ,[NgayThucHien]
           ,[NgayBatDau]
           ,[NgayKetThuc]
           ,[DonViTinhThucChay]
           ,[DonGiaTheoDonViTinhTC]
           ,[TongViewClickThucChay]
           ,[TongSoBaiVietChiPhiThucChay]
           ,[SoLuongThucChay]
           ,[TongThanhTienThucChayBanSauCK]
           ,[TongThanhTienThucChayMuaSauCK]
           ,[ThanhTienLaiThucChaySauCK]
           ,[ThanhTienLaiThucChayKM]
           ,[SoLuongThucChayKM]
           ,[SoLuongThucChayLechTreoHa]
           ,[ThanhTienLechTreoHa]
           ,[GiaTriThayDoiLaiSauCK]
           ,[SoLuongThayDoi]
           ,[SoLuongKMThayDoi]
           ,[GiaTriKMLaiThayDoi]
           ,[GhiChu]
           ,[CreatedAt]
           ,[LastModifiedAt])
   
	  SELECT [HopDongREF]
		  ,[SoHopDong]
		  ,[DmMaHopDongREF]
		  ,[NgayDanhSoHopDong]
		  ,[TrangThaiHopDong]
		  ,[DmNhanVienREF]
		  ,[TenDangNhap]
		  ,[DmPhongBanREF]
		  ,[DmBoPhanREF]
		  ,[DmNhomLamViecREF]
		  ,[DmDiaDiemLamViecREF]
		  ,[DmKhachHangREF]
		  ,[HopDongChiTietREF]
		  ,@DanhSachNhanHang_new AS [LstDmNhanHangREF]
		  ,[LstDmNhomNganhREF]
		  ,[DmHinhThucQuangCaoREF]
		  ,[DmSanPhamREF]
		  ,[DmChuyenMucREF]
		  ,[DmLoaiBannerREF]
		  ,[DmViTriREF]
		  ,[SoLuong]
		  ,[DonViTinhREF]
		  ,[DonGia]
		  ,[ChietKhau]
		  ,[ThanhTien]
		  ,[IsKhuyenMai]
		  ,[KhuyenMai]
		  ,[ThucChayMuaNgoaiChiTietREF]
		  ,[TongTienDuToanMuaSauCK]
		  ,[TongTienDuToanLaiMuaSauCK]
		  ,[ChietKhauMua]
		  ,[DmBannerREF]
		  ,[DmChienDichREF]
		  ,[DmWebsiteREF]
		  ,[TenWebsite]
		  ,@NgayGhiNhanThucChay AS [NgayThucHien]
		  ,'' [NgayBatDau]
		  ,'' [NgayKetThuc]
		  ,[DonViTinhThucChay]
		  ,[DonGiaTheoDonViTinhTC]
		  ,0 AS [TongViewClickThucChay]
		  ,0 AS [TongSoBaiVietChiPhiThucChay]
		  ,0 AS [SoLuongThucChay]
		  ,0 AS [TongThanhTienThucChayBanSauCK]
		  ,0 AS [TongThanhTienThucChayMuaSauCK]
		  ,0 AS [ThanhTienLaiThucChaySauCK]
		  ,0 AS [ThanhTienLaiThucChayKM]
		  ,0 AS [SoLuongThucChayKM]
		  ,0 AS [SoLuongThucChayLechTreoHa]
		  ,0 AS [ThanhTienLechTreoHa]
		  ,-SUM([ThanhTienLaiThucChaySauCK] + [GiaTriThayDoiLaiSauCK]) AS [GiaTriThayDoiLaiSauCK]
		  ,-SUM([SoLuongThucChay] + [SoLuongThayDoi]) AS [SoLuongThayDoi]
		  ,-SUM([SoLuongThucChayKM] + [SoLuongKMThayDoi]) AS [SoLuongKMThayDoi]
		  ,-SUM([ThanhTienLaiThucChayKM] + [GiaTriKMLaiThayDoi]) AS [GiaTriKMLaiThayDoi]
		  ,@GhiChuTinhLai AS [GhiChu]
		  ,GETDATE() AS [CreatedAt] 
		  ,GETDATE() AS[LastModifiedAt]
	  FROM [dbo].[ThucChayDaTinh_MuaNgoai]
	  WHERE 1=1
	  AND HopDongREF = @HopDongID
	  AND HopDongChiTietREF = @HopDongChiTietID
	  AND NgayThucHien <= @NgayGhiNhanThucChay
	  AND [GhiChu] <> @ghiChu
	GROUP BY 
		 [HopDongREF]
		  ,[SoHopDong]
		  ,[DmMaHopDongREF]
		  ,[NgayDanhSoHopDong]
		  ,[TrangThaiHopDong]
		  ,[DmNhanVienREF]
		  ,[TenDangNhap]
		  ,[DmPhongBanREF]
		  ,[DmBoPhanREF]
		  ,[DmNhomLamViecREF]
		  ,[DmDiaDiemLamViecREF]
		  ,[DmKhachHangREF]
		  ,[HopDongChiTietREF]
		  ,[LstDmNhomNganhREF]
		  ,[DmHinhThucQuangCaoREF]
		  ,[DmSanPhamREF]
		  ,[DmChuyenMucREF]
		  ,[DmLoaiBannerREF]
		  ,[DmViTriREF]
		  ,[SoLuong]
		  ,[DonViTinhREF]
		  ,[DonGia]
		  ,[ChietKhau]
		  ,[ThanhTien]
		  ,[IsKhuyenMai]
		  ,[KhuyenMai]
		  ,[ThucChayMuaNgoaiChiTietREF]
		  ,[TongTienDuToanMuaSauCK]
		  ,[TongTienDuToanLaiMuaSauCK]
		  ,[ChietKhauMua]
		  ,[DmBannerREF]
		  ,[DmChienDichREF]
		  ,[DmWebsiteREF]
		  ,[TenWebsite]
		  ,[DonViTinhThucChay]
		  ,[DonGiaTheoDonViTinhTC]
		HAVING (SUM([ThanhTienLaiThucChaySauCK] + [GiaTriThayDoiLaiSauCK])  <> 0 OR SUM([ThanhTienLaiThucChayKM] + [GiaTriKMLaiThayDoi]) <> 0)
	
END

```
