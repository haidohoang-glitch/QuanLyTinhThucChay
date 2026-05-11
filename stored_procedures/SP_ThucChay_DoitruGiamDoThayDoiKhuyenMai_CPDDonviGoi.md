# Stored Procedure: `ThucChay_DoitruGiamDoThayDoiKhuyenMai_CPDDonviGoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-08-21 16:15:32.950000
- **Ngày sửa cuối**: 2024-08-21 16:15:32.950000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChitietID` | `int(4)` | No |
| `@GhiChu` | `nvarchar(1000)` | No |
| `@ThucChayDaTinhID_op` | `nvarchar(1000)` | Yes |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE  PROCEDURE [dbo].[ThucChay_DoitruGiamDoThayDoiKhuyenMai_CPDDonviGoi]  
	@NgayThucHien DATETIME,
	@HopDongChitietID INT,
	@GhiChu NVARCHAR(500),
	@ThucChayDaTinhID_op NVARCHAR(500) OUTPUT
AS
BEGIN

DECLARE  @NgayDanhSo_GioiHan DATETIME
	, @TongThanhTienThucChay FLOAT = 0
	SET @NgayDanhSo_GioiHan = '2022-01-01'

	DECLARE @Table_op TABLE(ThucChayDaTinhID NVARCHAR(100), HopDongChiTietID INT)

	INSERT INTO [dbo].[ThucChayDaTinh]
           ([ThucChayDaTinhID]
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
           ,[TongViewThucChay]
           ,[TongClickThucChay]
           ,[TongSoBaiViet]
           ,[SoLuongThucChay]
           ,[NgayThucHien]
           ,[GiaTriThayDoi]
           ,[ThanhTienThucChayTruocTrietKhau]
           ,[GiaTriTrietKhauThucChay]
           ,[ThanhTienSauTrietKhauThucChay]
           ,[GiaTriHoaHongThucChay]
           ,[ThanhTienThucThu]
           ,[ThanhTienKM]
           ,[SoLuongThucChayKM]
           ,[SoLuongThucChayLechTreoHa]
           ,[ThanhTienLechTreoHa]
           ,[CreatedAt]
           ,[LastModifiedAt]
           ,[IsPheDuyet]
           ,[PheDuyetBy]
           ,[PheDuyetAt]
           ,[SoLuongThayDoi]
           ,[SoLuongKMThayDoi]
           ,[GiaTriKMThayDoi]
           ,[GhiChu])

    OUTPUT INSERTED.ThucChayDaTinhID, INSERTED.HopDongChiTietREF INTO @Table_op 

	SELECT NEWID() AS [ThucChayDaTinhID]
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
      ,[TongViewThucChay]
      ,[TongClickThucChay]
      ,[TongSoBaiViet]
      ,0 AS [SoLuongThucChay]
      ,@NgayThucHien AS [NgayThucHien]
      ,-SUM([ThanhTienSauTrietKhauThucChay] + [GiaTriThayDoi]) AS [GiaTriThayDoi]
      ,0 AS [ThanhTienThucChayTruocTrietKhau]
      ,0 AS [GiaTriTrietKhauThucChay]
      ,0 AS [ThanhTienSauTrietKhauThucChay]
      ,0 AS [GiaTriHoaHongThucChay]
      ,0 AS [ThanhTienThucThu]
      ,0 AS [ThanhTienKM]
      ,0 AS [SoLuongThucChayKM]
      ,0 AS [SoLuongThucChayLechTreoHa]
      ,0 AS [ThanhTienLechTreoHa]
      ,GETDATE() AS [CreatedAt]
      ,GETDATE() AS [LastModifiedAt]
      ,0 AS [IsPheDuyet]
      ,'' AS [PheDuyetBy]
      ,'' AS [PheDuyetAt]
      ,-SUM([SoLuongThucChay] + [SoLuongThayDoi]) AS [SoLuongThayDoi]
      ,-SUM([SoLuongThucChayKM] + [SoLuongKMThayDoi]) AS [SoLuongKMThayDoi]
      ,-SUM([ThanhTienKM] + [GiaTriKMThayDoi]) AS [GiaTriKMThayDoi]
      ,@GhiChu AS [GhiChu]
  FROM [dbo].[ThucChayDaTinh] tcdt
  WHERE tcdt.HopDongChiTietREF = @HopDongChiTietID
  AND tcdt.NgayThucHien <= @NgayThucHien
  GROUP BY
  [HopDongID]
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
      ,[TongViewThucChay]
      ,[TongClickThucChay]
      ,[TongSoBaiViet]
	  HAVING SUM([ThanhTienSauTrietKhauThucChay] + [GiaTriThayDoi]) <> 0
	  OR SUM([ThanhTienKM] + [GiaTriKMThayDoi]) <> 0

	SET @ThucChayDaTinhID_op = ISNULL((SELECT TOP 1 ThucChayDaTinhID FROM @Table_op ),'')
END

```
