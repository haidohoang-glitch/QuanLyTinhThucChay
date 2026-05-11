# Stored Procedure: `ThucChayDaTinh_MuaNgoai_SendThucChayDaTinhAdmarket`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-08-12 16:03:58.300000
- **Ngày sửa cuối**: 2020-09-03 17:07:00.303000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC ThucChayDaTinh_MuaNgoai_SendThucChayDaTinhAdmarket '2015-08-10'
CREATE PROCEDURE [dbo].[ThucChayDaTinh_MuaNgoai_SendThucChayDaTinhAdmarket] 
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	INSERT INTO ThucChayDaTinhAdmarket
	SELECT 
	   NEWID()
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
      ,[GhiChu] FROM ThucChayDaTinh WHERE CONVERT(DATE,NgayThucHien) = CONVERT(DATE,@NgayThucHien)
	  AND (DmSanPhamREF IN (585,144,628,337)
	  AND DmViTriREF IN (100093,100478))

END

```
