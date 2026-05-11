# Stored Procedure: `ThucChayDaTinh_GTTD_DoiTruGiam_ThucChayDaTinh_MuaNgoai_ThanhTien_GGFB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-08-27 14:22:24.463000
- **Ngày sửa cuối**: 2020-09-22 10:23:28.750000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@NgayGhiNhanThucChay` | `datetime(8)` | No |
| `@GhiChu` | `nvarchar(4000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMW
-- Create date: 2015-01-12
-- Description:	Insert Thuc chay da tinh mua ngoai by phanBoId
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinh_GTTD_DoiTruGiam_ThucChayDaTinh_MuaNgoai_ThanhTien_GGFB]
	@HopDongID INT,
	@HopDongChiTietID INT,
	@DmSanPhamREF INT,
	@NgayGhiNhanThucChay DATETIME,
	@GhiChu NVARCHAR(2000)
AS
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
	
END

```
