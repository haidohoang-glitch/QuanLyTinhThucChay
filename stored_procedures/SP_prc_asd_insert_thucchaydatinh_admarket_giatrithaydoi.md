# Stored Procedure: `prc_asd_insert_thucchaydatinh_admarket_giatrithaydoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-11 15:02:51.743000
- **Ngày sửa cuối**: 2017-09-11 15:02:51.770000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(100)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@GhiChu` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		DOANNV
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[prc_asd_insert_thucchaydatinh_admarket_giatrithaydoi]
	-- Add the parameters for the stored procedure here
	@SoHopDong nvarchar(50),
	@NgayThucHien DATETIME,
	@DmSanPhamREF int,
	@GhiChu nvarchar(200)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	declare @HopDongChiTietREF int ,@HopDongID int

	select @HopDongID = hopdongid from hopdong where sohopdong = @SoHopDong and deletedstatus = 0 

	DECLARE db_cursor CURSOR FOR  
	SELECT hopdongchitietid 
	FROM hopdongchitiet
	WHERE hopdongfk = @HopDongID

	OPEN db_cursor   
	FETCH NEXT FROM db_cursor INTO @HopDongChiTietREF   

	WHILE @@FETCH_STATUS = 0   
	BEGIN   
		   SELECT NEWID()[ThucChayDaTinhID]
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
				  ,-SUM([TongViewThucChay])[TongViewThucChay]
				  ,-SUM([TongClickThucChay])[TongClickThucChay]
				  ,0[TongSoBaiViet]
				  ,-SUM([SoLuongThucChay])[SoLuongThucChay]
				  ,@NgayThucHien[NgayThucHien]
				  ,-SUM(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi)[GiaTriThayDoi]
				  ,-SUM([ThanhTienThucChayTruocTrietKhau])[ThanhTienThucChayTruocTrietKhau]
				  ,-SUM([GiaTriTrietKhauThucChay])[GiaTriTrietKhauThucChay]
				  ,0[ThanhTienSauTrietKhauThucChay]
				  ,-SUM([GiaTriHoaHongThucChay])[GiaTriHoaHongThucChay]
				  ,-SUM([ThanhTienThucThu])[ThanhTienThucThu]
				  ,-SUM([ThanhTienKM])[ThanhTienKM]
				  ,-SUM([SoLuongThucChayKM])[SoLuongThucChayKM]
				  ,-SUM([SoLuongThucChayLechTreoHa])[SoLuongThucChayLechTreoHa]
				  ,-SUM([ThanhTienLechTreoHa])[ThanhTienLechTreoHa]
				  ,GETDATE()[CreatedAt]
				  ,GETDATE()[LastModifiedAt]
				  ,0[IsPheDuyet]
				  ,''[PheDuyetBy]
				  ,''[PheDuyetAt]
				  ,0[SoLuongThayDoi]
				  ,-SUM([SoLuongKMThayDoi])[SoLuongKMThayDoi]
				  ,-SUM([GiaTriKMThayDoi])[GiaTriKMThayDoi]
				  ,@GhiChu [GhiChu]
				  FROM [dbo].[ThucChayDaTinhAdmarket]
				  WHERE HopDongChiTietREF = @HopDongChiTietREF
				  AND DmSanPhamREF = @DmSanPhamREF
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

		   FETCH NEXT FROM db_cursor INTO @HopDongChiTietREF   
	END   

	CLOSE db_cursor   
	DEALLOCATE db_cursor
	
END


```
