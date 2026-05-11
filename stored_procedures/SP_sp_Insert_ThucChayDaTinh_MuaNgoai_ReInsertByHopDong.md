# Stored Procedure: `sp_Insert_ThucChayDaTinh_MuaNgoai_ReInsertByHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-05-22 16:48:11.627000
- **Ngày sửa cuối**: 2025-07-19 11:49:34.403000

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
| `@IsExistData` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [dbo].[sp_Insert_ThucChayDaTinh_ReInsertByHopDong] '2016-07-28'
CREATE PROCEDURE [dbo].[sp_Insert_ThucChayDaTinh_MuaNgoai_ReInsertByHopDong]
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
	@IsExistData INT 
AS
BEGIN
	--PRINT 'HELLO'
	DECLARE @v_DmKhachHangREF_new int = 0

	SET @v_DmKhachHangREF_new =
	ISNULL((SELECT top (1) DmKhachHangREF  FROM HopDong hd
	WHERE hd.HopDongID = @HopDongID ORDER BY hd.HopDongID),0)

	IF(@IsThayDoi <> 0 AND @GiaTriThucChay <> 0 AND @IsExistData >0)
	BEGIN
		--1. CO THAY DOI THONG TIN LIEN QUAN DEN THUCCHAYDATINH_MUANGOAI
		IF(@IsThayDoi <> 4)
		BEGIN
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
  

		SELECT 
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
			   ,@NgayThucHien AS [NgayThucHien]
			   ,[NgayBatDau]
			   ,[NgayKetThuc]
			   ,[DonViTinhThucChay]
			   ,[DonGiaTheoDonViTinhTC]
			   ,0 AS [TongViewClickThucChay]
			   ,0 AS [TongSoBaiVietChiPhiThucChay]
			   ,0 AS [SoLuongThucChay]
			   ,[TongThanhTienThucChayBanSauCK]
			   ,[TongThanhTienThucChayMuaSauCK]
			   ,0 AS [ThanhTienLaiThucChaySauCK]
			   ,0 AS [ThanhTienLaiThucChayKM]
			   ,0 AS [SoLuongThucChayKM]
			   ,0 AS [SoLuongThucChayLechTreoHa]
			   ,0 AS [ThanhTienLechTreoHa]
			   ,-SUM([ThanhTienLaiThucChaySauCK] + [GiaTriThayDoiLaiSauCK]) AS [GiaTriThayDoiLaiSauCK]
			   ,-SUM([SoLuongThucChay] + [SoLuongThayDoi]) AS [SoLuongThayDoi]
			   ,-SUM([SoLuongThucChayKM] + [SoLuongKMThayDoi]) AS [SoLuongKMThayDoi]
			   ,-SUM([ThanhTienLaiThucChayKM] + [GiaTriKMLaiThayDoi]) AS [GiaTriKMLaiThayDoi]
			   ,@Note AS [GhiChu]
			   ,GETDATE() AS [CreatedAt]
			   ,GETDATE() AS [LastModifiedAt]
			   FROM dbo.ThucChayDaTinh_MuaNgoai 
			   WHERE HopDongREF = @HopDongID
			   AND HopDongChiTietREF = @HopDongChiTietID
			   AND NgayThucHien < @NgayThucHien
			   --AND (DmHinhThucQuangCaoREF = 13 OR DmLoaiBannerREF = 18)
			   AND (([ThanhTienLaiThucChaySauCK] + [GiaTriThayDoiLaiSauCK]) <> 0  OR ([ThanhTienLaiThucChayKM] + [GiaTriKMLaiThayDoi])  <> 0)
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
			   ,[NgayBatDau]
			   ,[NgayKetThuc]
			   ,[DonViTinhThucChay]
			   ,[DonGiaTheoDonViTinhTC]
			   ,[TongThanhTienThucChayBanSauCK]
			   ,[TongThanhTienThucChayMuaSauCK]
		END
		--2. THAY DOI THONG TIN HOP DONG
		IF(@IsThayDoi = 1)
		BEGIN
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
  

		SELECT 
				[HopDongREF]
			   , @SoHopDong_new [SoHopDong]
			   , @MaSoHopDong_new AS [DmMaHopDongREF]
			   , @NgayDanhSo_new AS [NgayDanhSoHopDong]
			   , [TrangThaiHopDong]
			   , @DmNhanVienREF_new AS [DmNhanVienREF]
			   , ISNULL((SELECT TOP (1) hd.TenDangNhap
			      FROM HopDong hd WHERE hd.HopDongID = @HopDongID ORDER BY hd.HopDongID),'') AS [TenDangNhap]
			   , ISNULL((SELECT TOP (1) hd.[DmPhongBanREF]
			      FROM HopDong hd WHERE hd.HopDongID = @HopDongID ORDER BY hd.HopDongID),0) AS [DmPhongBanREF]
			   , ISNULL((SELECT TOP (1) hd.[DmBoPhanREF]
			      FROM HopDong hd WHERE hd.HopDongID = @HopDongID ORDER BY hd.HopDongID),0) AS [DmBoPhanREF]
			   , ISNULL((SELECT TOP (1) hd.[DmNhomLamViecREF]
			      FROM HopDong hd WHERE hd.HopDongID = @HopDongID ORDER BY hd.HopDongID),0) AS [DmNhomLamViecREF]
			   , ISNULL((SELECT TOP (1) hd.[DmDiaDiemLamViecREF]
			      FROM HopDong hd WHERE hd.HopDongID = @HopDongID ORDER BY hd.HopDongID),0) AS [DmDiaDiemLamViecREF]
			   , @v_DmKhachHangREF_new AS [DmKhachHangREF]
			   ,[HopDongChiTietREF]
			   ,[LstDmNhanHangREF]
			   ,[LstDmNhomNganhREF]
			   , @HinhThucQuangCaoREF_new AS [DmHinhThucQuangCaoREF]
			   , @DmSanPhamREF_new AS [DmSanPhamREF]
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
			   ,@NgayThucHien AS [NgayThucHien]
			   ,[NgayBatDau]
			   ,[NgayKetThuc]
			   ,[DonViTinhThucChay]
			   ,[DonGiaTheoDonViTinhTC]
			   ,0 AS [TongViewClickThucChay]
			   ,0 AS [TongSoBaiVietChiPhiThucChay]
			   ,0 AS [SoLuongThucChay]
			   ,[TongThanhTienThucChayBanSauCK]
			   ,[TongThanhTienThucChayMuaSauCK]
			   ,0 AS [ThanhTienLaiThucChaySauCK]
			   ,0 AS [ThanhTienLaiThucChayKM]
			   ,0 AS [SoLuongThucChayKM]
			   ,0 AS [SoLuongThucChayLechTreoHa]
			   ,0 AS [ThanhTienLechTreoHa]
			   ,SUM([ThanhTienLaiThucChaySauCK] + [GiaTriThayDoiLaiSauCK]) AS [GiaTriThayDoiLaiSauCK]
			   ,SUM([SoLuongThucChay] + [SoLuongThayDoi]) AS [SoLuongThayDoi]
			   ,SUM([SoLuongThucChayKM] + [SoLuongKMThayDoi]) AS [SoLuongKMThayDoi]
			   ,SUM([ThanhTienLaiThucChayKM] + [GiaTriKMLaiThayDoi]) AS [GiaTriKMLaiThayDoi]
			   ,N'Chạy lại tính giá trị thay đổi TTHĐ lãi MN (MuaNgoai_ReInsertByHopDong) ' + @Note AS [GhiChu]
			   ,GETDATE() AS [CreatedAt]
			   ,GETDATE() AS [LastModifiedAt]
			   FROM dbo.ThucChayDaTinh_MuaNgoai 
			   WHERE HopDongREF = @HopDongID
			   AND HopDongChiTietREF = @HopDongChiTietID
			   AND NgayThucHien < @NgayThucHien
			   --AND (DmHinhThucQuangCaoREF = 13 OR DmLoaiBannerREF = 18)
			   AND (([ThanhTienLaiThucChaySauCK] + [GiaTriThayDoiLaiSauCK]) <> 0  OR ([ThanhTienLaiThucChayKM] + [GiaTriKMLaiThayDoi])  <> 0)
			   GROUP BY
			  [HopDongREF]
			   ,[TrangThaiHopDong]
			   ,[HopDongChiTietREF]
			   ,[LstDmNhanHangREF]
			   ,[LstDmNhomNganhREF]
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
			   ,[NgayBatDau]
			   ,[NgayKetThuc]
			   ,[DonViTinhThucChay]
			   ,[DonGiaTheoDonViTinhTC]
			   ,[TongThanhTienThucChayBanSauCK]
			   ,[TongThanhTienThucChayMuaSauCK]
		END
		--3. THAY DOI THONG TIN NHAN HANG
		IF(@IsThayDoi = 3)
		BEGIN
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
  

		SELECT 
				[HopDongREF]
			   , @SoHopDong_new [SoHopDong]
			   , @MaSoHopDong_new AS [DmMaHopDongREF]
			   , @NgayDanhSo_new AS [NgayDanhSoHopDong]
			   , [TrangThaiHopDong]
			   , @DmNhanVienREF_new AS [DmNhanVienREF]
			   , ISNULL((SELECT TOP (1) hd.TenDangNhap
			      FROM HopDong hd WHERE hd.HopDongID = @HopDongID ORDER BY hd.HopDongID),'') AS [TenDangNhap]
			   , ISNULL((SELECT TOP (1) hd.[DmPhongBanREF]
			      FROM HopDong hd WHERE hd.HopDongID = @HopDongID ORDER BY hd.HopDongID),0) AS [DmPhongBanREF]
			   , ISNULL((SELECT TOP (1) hd.[DmBoPhanREF]
			      FROM HopDong hd WHERE hd.HopDongID = @HopDongID ORDER BY hd.HopDongID),0) AS [DmBoPhanREF]
			   , ISNULL((SELECT TOP (1) hd.[DmNhomLamViecREF]
			      FROM HopDong hd WHERE hd.HopDongID = @HopDongID ORDER BY hd.HopDongID),0) AS [DmNhomLamViecREF]
			   , ISNULL((SELECT TOP (1) hd.[DmDiaDiemLamViecREF]
			      FROM HopDong hd WHERE hd.HopDongID = @HopDongID ORDER BY hd.HopDongID),0) AS [DmDiaDiemLamViecREF]
			   , @v_DmKhachHangREF_new AS [DmKhachHangREF]
			   ,[HopDongChiTietREF]
			   ,@DsNhanHangREF_new AS [LstDmNhanHangREF]
			   ,'' AS [LstDmNhomNganhREF]
			   , @HinhThucQuangCaoREF_new AS [DmHinhThucQuangCaoREF]
			   , @DmSanPhamREF_new AS [DmSanPhamREF]
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
			   ,@NgayThucHien AS [NgayThucHien]
			   ,[NgayBatDau]
			   ,[NgayKetThuc]
			   ,[DonViTinhThucChay]
			   ,[DonGiaTheoDonViTinhTC]
			   ,0 AS [TongViewClickThucChay]
			   ,0 AS [TongSoBaiVietChiPhiThucChay]
			   ,0 AS [SoLuongThucChay]
			   ,[TongThanhTienThucChayBanSauCK]
			   ,[TongThanhTienThucChayMuaSauCK]
			   ,0 AS [ThanhTienLaiThucChaySauCK]
			   ,0 AS [ThanhTienLaiThucChayKM]
			   ,0 AS [SoLuongThucChayKM]
			   ,0 AS [SoLuongThucChayLechTreoHa]
			   ,0 AS [ThanhTienLechTreoHa]
			   ,SUM([ThanhTienLaiThucChaySauCK] + [GiaTriThayDoiLaiSauCK]) AS [GiaTriThayDoiLaiSauCK]
			   ,SUM([SoLuongThucChay] + [SoLuongThayDoi]) AS [SoLuongThayDoi]
			   ,SUM([SoLuongThucChayKM] + [SoLuongKMThayDoi]) AS [SoLuongKMThayDoi]
			   ,SUM([ThanhTienLaiThucChayKM] + [GiaTriKMLaiThayDoi]) AS [GiaTriKMLaiThayDoi]
			   ,N'Chạy lại tính giá trị thay đổi TTNHANHANG lãi MN (MuaNgoai_ReInsertByHopDong) ' + @Note AS [GhiChu]
			   ,GETDATE() AS [CreatedAt]
			   ,GETDATE() AS [LastModifiedAt]
			   FROM dbo.ThucChayDaTinh_MuaNgoai 
			   WHERE HopDongREF = @HopDongID
			   AND HopDongChiTietREF = @HopDongChiTietID
			   AND NgayThucHien < @NgayThucHien
			   --AND (DmHinhThucQuangCaoREF = 13 OR DmLoaiBannerREF = 18)  --Khong lam cho Dang Tin, tuyen bai, adpage
			   AND (([ThanhTienLaiThucChaySauCK] + [GiaTriThayDoiLaiSauCK]) <> 0  OR ([ThanhTienLaiThucChayKM] + [GiaTriKMLaiThayDoi])  <> 0)
			   GROUP BY
			  [HopDongREF]
			   ,[TrangThaiHopDong]
			   ,[HopDongChiTietREF]
			   ,[LstDmNhomNganhREF]
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
			   ,[NgayBatDau]
			   ,[NgayKetThuc]
			   ,[DonViTinhThucChay]
			   ,[DonGiaTheoDonViTinhTC]
			   ,[TongThanhTienThucChayBanSauCK]
			   ,[TongThanhTienThucChayMuaSauCK]
		END
	END
	
END



```
