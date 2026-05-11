# Stored Procedure: `ThucChayDaTinh_GTTD_DoiTruGiam_ThucChayDaTinh_MuaNgoai_By_ORDER_ThanhTien_GGFB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-10-08 16:33:28.623000
- **Ngày sửa cuối**: 2022-06-03 15:56:56

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@Operating_Order_Id` | `int(4)` | No |
| `@NgayGhiNhanThucChay` | `datetime(8)` | No |
| `@GhiChu` | `nvarchar(4000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMW
-- Create date: 2015-01-12
-- Description:	Insert Thuc chay da tinh mua ngoai by phanBoId
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinh_GTTD_DoiTruGiam_ThucChayDaTinh_MuaNgoai_By_ORDER_ThanhTien_GGFB]
	@HopDongID INT,
	@HopDongChiTietID INT,
	@Operating_Order_Id INT,
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
	  AND (DmSanPhamREF in (306,423,5160,5188,772)  OR DmViTriREF in (100093,100478,100774) )
	  AND DmSanPhamREF <> 585 --Khong phai san pham Adx
	  AND DmChienDichREF = @Operating_Order_Id
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
