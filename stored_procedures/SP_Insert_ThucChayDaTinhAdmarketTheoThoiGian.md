# Stored Procedure: `Insert_ThucChayDaTinhAdmarketTheoThoiGian`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-27 17:43:21.580000
- **Ngày sửa cuối**: 2015-03-27 17:43:21.580000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[Insert_ThucChayDaTinhAdmarketTheoThoiGian]
	-- Add the parameters for the stored procedure here
	@FromDate DATETIME,
	@ToDate DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	DELETE FROM ThucChayDaTinhAdmarketTheoThoiGian
	INSERT INTO ThucChayDaTinhAdmarketTheoThoiGian
	SELECT  [ThucChayDaTinhID]
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
      ,[GhiChu]
  FROM [dbo].[ThucChayDaTinhAdmarket]
END

```
