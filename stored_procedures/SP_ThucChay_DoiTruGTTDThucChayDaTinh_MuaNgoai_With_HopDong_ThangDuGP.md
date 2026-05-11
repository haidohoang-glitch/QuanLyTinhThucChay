# Stored Procedure: `ThucChay_DoiTruGTTDThucChayDaTinh_MuaNgoai_With_HopDong_ThangDuGP`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-10-19 16:53:10.460000
- **Ngày sửa cuối**: 2023-01-10 11:00:03.697000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@ThucChay_PerformanceBase_ThayDoi_ID` | `int(4)` | No |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@ThucChayDaTinh_MuaNgoai_ID_output` | `bigint(8)` | Yes |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*

*/
CREATE PROCEDURE [dbo].[ThucChay_DoiTruGTTDThucChayDaTinh_MuaNgoai_With_HopDong_ThangDuGP]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME, 
	@ThucChay_PerformanceBase_ThayDoi_ID INT,
	@HopDongID INT,
	@HopDongChiTietID INT, 
	@DmSanPhamREF INT, 
	@GhiChu nvarchar(200),
	@ThucChayDaTinh_MuaNgoai_ID_output BIGINT OUTPUT
AS
BEGIN
	DECLARE @Table_ouput TABLE(ThucChayDaTinh_MuaNgoai_ID BIGINT, HopDongID INT)
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

	OUTPUT INSERTED.ID, INSERTED.[HopDongREF] INTO @Table_ouput

	SELECT tcdtm.[HopDongREF]
      ,tcdtm.[SoHopDong]
      ,tcdtm.[DmMaHopDongREF]
      ,tcdtm.[NgayDanhSoHopDong]
      ,tcdtm.[TrangThaiHopDong]
      ,tcdtm.[DmNhanVienREF]
      ,tcdtm.[TenDangNhap]
      ,tcdtm.[DmPhongBanREF]
      ,tcdtm.[DmBoPhanREF]
      ,tcdtm.[DmNhomLamViecREF]
      ,tcdtm.[DmDiaDiemLamViecREF]
      ,tcdtm.[DmKhachHangREF]
      ,tcdtm.[HopDongChiTietREF]
      ,tcdtm.[LstDmNhanHangREF]
      ,tcdtm.[LstDmNhomNganhREF]
      ,tcdtm.[DmHinhThucQuangCaoREF]
      ,tcdtm.[DmSanPhamREF]
      ,tcdtm.[DmChuyenMucREF]
      ,tcdtm.[DmLoaiBannerREF]
      ,tcdtm.[DmViTriREF]
      ,tcdtm.[SoLuong]
      ,tcdtm.[DonViTinhREF]
      ,tcdtm.[DonGia]
      ,tcdtm.[ChietKhau]
      ,tcdtm.[ThanhTien]
      ,tcdtm.[IsKhuyenMai]
      ,tcdtm.[KhuyenMai]
      ,tcdtm.[ThucChayMuaNgoaiChiTietREF]
      ,tcdtm.[TongTienDuToanMuaSauCK]
      ,tcdtm.[TongTienDuToanLaiMuaSauCK]
      ,tcdtm.[ChietKhauMua]
      ,tcdtm.[DmBannerREF]
      ,tcdtm.[DmChienDichREF]
      ,tcdtm.[DmWebsiteREF]
      ,tcdtm.[TenWebsite]
      ,@NgayThucHien AS [NgayThucHien]
      ,tcdtm.[NgayBatDau]
      ,tcdtm.[NgayKetThuc]
      ,tcdtm.[DonViTinhThucChay]
      ,tcdtm.[DonGiaTheoDonViTinhTC]
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
      ,-SUM(tcdtm.[ThanhTienLaiThucChaySauCK] + tcdtm.[GiaTriThayDoiLaiSauCK]) AS [GiaTriThayDoiLaiSauCK]
      ,-SUM(tcdtm.[SoLuongThucChay] + tcdtm.[SoLuongThayDoi]) AS [SoLuongThayDoi]
      ,-SUM(tcdtm.[SoLuongThucChayKM] + tcdtm.[SoLuongKMThayDoi]) AS [SoLuongKMThayDoi]
      ,-SUM(tcdtm.[ThanhTienLaiThucChayKM] + tcdtm.[GiaTriKMLaiThayDoi]) [GiaTriKMLaiThayDoi]
	  ,@GhiChu AS GhiChu
	  ,GETDATE() AS [CreatedAt]
      ,GETDATE() AS [LastModifiedAt]
  FROM [dbo].[ThucChayDaTinh_MuaNgoai] tcdtm
  WHERE tcdtm.[HopDongREF] = @HopDongID
  AND tcdtm.[HopDongChiTietREF] = @HopDongChiTietID
  AND tcdtm.[DmSanPhamREF] = @DmSanPhamREF
  AND tcdtm.[ThucChayMuaNgoaiChiTietREF] = @ThucChay_PerformanceBase_ThayDoi_ID
  AND tcdtm.NgayThucHien < @NgayThucHien 
  GROUP BY  tcdtm.[HopDongREF]
      ,tcdtm.[SoHopDong]
      ,tcdtm.[DmMaHopDongREF]
      ,tcdtm.[NgayDanhSoHopDong]
      ,tcdtm.[TrangThaiHopDong]
      ,tcdtm.[DmNhanVienREF]
      ,tcdtm.[TenDangNhap]
      ,tcdtm.[DmPhongBanREF]
      ,tcdtm.[DmBoPhanREF]
      ,tcdtm.[DmNhomLamViecREF]
      ,tcdtm.[DmDiaDiemLamViecREF]
      ,tcdtm.[DmKhachHangREF]
      ,tcdtm.[HopDongChiTietREF]
      ,tcdtm.[LstDmNhanHangREF]
      ,tcdtm.[LstDmNhomNganhREF]
      ,tcdtm.[DmHinhThucQuangCaoREF]
      ,tcdtm.[DmSanPhamREF]
      ,tcdtm.[DmChuyenMucREF]
      ,tcdtm.[DmLoaiBannerREF]
      ,tcdtm.[DmViTriREF]
      ,tcdtm.[SoLuong]
      ,tcdtm.[DonViTinhREF]
      ,tcdtm.[DonGia]
      ,tcdtm.[ChietKhau]
      ,tcdtm.[ThanhTien]
      ,tcdtm.[IsKhuyenMai]
      ,tcdtm.[KhuyenMai]
      ,tcdtm.[ThucChayMuaNgoaiChiTietREF]
      ,tcdtm.[TongTienDuToanMuaSauCK]
      ,tcdtm.[TongTienDuToanLaiMuaSauCK]
      ,tcdtm.[ChietKhauMua]
      ,tcdtm.[DmBannerREF]
      ,tcdtm.[DmChienDichREF]
      ,tcdtm.[DmWebsiteREF]
      ,tcdtm.[TenWebsite]
      ,tcdtm.[NgayBatDau]
      ,tcdtm.[NgayKetThuc]
      ,tcdtm.[DonViTinhThucChay]
      ,tcdtm.[DonGiaTheoDonViTinhTC]

	  SET @ThucChayDaTinh_MuaNgoai_ID_output = ISNULL((SELECT TOP 1 ThucChayDaTinh_MuaNgoai_ID FROM  @Table_ouput),0)
END

```
