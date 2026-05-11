# Stored Procedure: `ThucChayDaTinh_MuaNgoai_InsertThucChayLaiMuaNgoai_DoiTruGiam`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-05-19 16:03:18.100000
- **Ngày sửa cuối**: 2026-01-02 09:51:34.790000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@ThucChayMuaNgoaiChiTietID` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@ghiChu` | `nvarchar(1024)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMW
-- Create date: 2015-01-12
-- Description:	Insert Thuc chay da tinh mua ngoai by phanBoId
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinh_MuaNgoai_InsertThucChayLaiMuaNgoai_DoiTruGiam]
	@NgayThucHien						DATETIME,
	@ThucChayMuaNgoaiChiTietID			INT,
	@HopDongREF							INT,
	@HopDongChiTietREF					INT,
	@ghiChu								NVARCHAR(512)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	DECLARE @MaxNgayThucChay DATETIME
	--XAC DINH NGAY TINH THUC CHAY GAN NHAT
	SET @MaxNgayThucChay = ISNULL((
							SELECT MAX(tc.NgayThucHien) AS MaxNgayThucHien FROM dbo.ThucChayDaTinh_MuaNgoai tc
							WHERE  tc.HopDongREF = @HopDongREF 
							AND tc.NgayThucHien  <= @NgayThucHien
							AND tc.HopDongChiTietREF = @HopDongChiTietREF
							AND tc.ThucChayMuaNgoaiChiTietREF = @ThucChayMuaNgoaiChiTietID 
						),'1900-01-01')

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
		  ,@NgayThucHien AS [NgayThucHien]
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
	  WHERE ThucChayMuaNgoaiChiTietREF = @ThucChayMuaNgoaiChiTietID
	  AND HopDongREF = @HopDongREF
	  AND HopDongChiTietREF = @HopDongChiTietREF
	  AND NgayThucHien <= @MaxNgayThucChay
	  
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
	
END

```
