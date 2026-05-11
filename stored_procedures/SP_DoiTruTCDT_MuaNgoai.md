# Stored Procedure: `DoiTruTCDT_MuaNgoai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-01-12 16:52:29.067000
- **Ngày sửa cuối**: 2021-01-12 17:04:22.923000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ID` | `nvarchar(100)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@GhiChu` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql

--[DoiTruTCDT] '2021-01-08',1028603,604370,631,N'Xử lý thực chạy 2021 về 2020'
      CREATE Procedure [dbo].[DoiTruTCDT_MuaNgoai]
	  @ID nvarchar(50),
	  @NgayThucHien datetime,
	  @HopDongID int, @HopDongChiTietID int, @DmSanPhamREF int,@GhiChu nvarchar(200)
	  as
	  begin
	  Insert into ThucChayDaTinh_MuaNgoai
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
      ,@NgayThucHien[NgayThucHien]
      ,[NgayBatDau]
      ,[NgayKetThuc]
      ,[DonViTinhThucChay]
      ,[DonGiaTheoDonViTinhTC]
      ,[TongViewClickThucChay]
      ,[TongSoBaiVietChiPhiThucChay]
      ,0[SoLuongThucChay]
      ,[TongThanhTienThucChayBanSauCK]
      ,[TongThanhTienThucChayMuaSauCK]
      ,0[ThanhTienLaiThucChaySauCK]
      ,0[ThanhTienLaiThucChayKM]
      ,0[SoLuongThucChayKM]
      ,0[SoLuongThucChayLechTreoHa]
      ,0[ThanhTienLechTreoHa]
      ,-([ThanhTienLaiThucChaySauCK]+[GiaTriThayDoiLaiSauCK])[GiaTriThayDoiLaiSauCK]
      ,-([SoLuongThucChay]+[SoLuongThayDoi])[SoLuongThayDoi]
      ,0[SoLuongKMThayDoi]
      ,0[GiaTriKMLaiThayDoi]
      ,@GhiChu[GhiChu]
      ,getdate()[CreatedAt]
      ,getdate()[LastModifiedAt]
  FROM [dbo].[ThucChayDaTinh_MuaNgoai]
  where HopDongREF = @HopDongID and HopDongChiTietREF = @HopDongChiTietID and DmSanPhamREF = @DmSanPhamREF and ID = @ID
  
  end

```
