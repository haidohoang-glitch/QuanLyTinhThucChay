# Stored Procedure: `prc_asd_insert_thucchaydatinh_admarket_hopdonghuy_chitiet_PhanBO`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-02-06 11:00:55.340000
- **Ngày sửa cuối**: 2024-02-28 11:34:28.013000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@GhiChu` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		DOANNV
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[prc_asd_insert_thucchaydatinh_admarket_hopdonghuy_chitiet_PhanBO]
	-- Add the parameters for the stored procedure here
	@HopDongID int,
	@NgayThucHien DATETIME,
	@GhiChu nvarchar(200)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure hre
	declare @HopDongChiTietREF int 

	
	DECLARE db_cursor CURSOR FOR  
	SELECT hdct.hopdongchitietid 
	FROM dbo.hopdongchitiet hdct
	WHERE hdct.hopdongfk = @HopDongID and hdct.DmSanPhamREF in (585,628,144)

	OPEN db_cursor   
	FETCH NEXT FROM db_cursor INTO @HopDongChiTietREF   

	WHILE @@FETCH_STATUS = 0   
	BEGIN   
		   insert into thucchaydatinhadmarket
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
