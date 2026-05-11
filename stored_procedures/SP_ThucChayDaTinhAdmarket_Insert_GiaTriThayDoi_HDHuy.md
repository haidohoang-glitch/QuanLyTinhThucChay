# Stored Procedure: `ThucChayDaTinhAdmarket_Insert_GiaTriThayDoi_HDHuy`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-10-10 13:50:48.760000
- **Ngày sửa cuối**: 2016-10-10 13:51:06.190000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongId` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@PhanBoId` | `int(4)` | No |
| `@SanPhamId` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(100)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@SoLuongThayDoiThucChay` | `bigint(8)` | No |
| `@ThanhTienThayDoiThucChay` | `float(8)` | No |
| `@SoLuongThayDoiKhuyenMai` | `bigint(8)` | No |
| `@ThanhTienThayDoiKhuyenMai` | `float(8)` | No |
| `@GhiChu` | `nvarchar(510)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@TenViTri` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-08-28
-- Description:	Insert gia tri thay doi cho san pham Admarket
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinhAdmarket_Insert_GiaTriThayDoi_HDHuy]
	-- Add the parameters for the stored procedure here
	@NgayThucHien				DATETIME,
	@HopDongId					INT,
	@SoHopDong					NVARCHAR(50),
	@PhanBoId					INT,
	@SanPhamId					INT,
	@TenSanPham					NVARCHAR(50),
	@DonViTinh					NVARCHAR(50),
	@SoLuongThayDoiThucChay		BIGINT,
	@ThanhTienThayDoiThucChay	FLOAT,
	@SoLuongThayDoiKhuyenMai	BIGINT,
	@ThanhTienThayDoiKhuyenMai	FLOAT,
	@GhiChu						NVARCHAR(255),
	@DmViTriREF					INT,
	@TenViTri					NVARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
	INSERT INTO ThucChayDaTinhAdmarket
    SELECT * FROM
		(
			  SELECT newid() AS ID
			  ,[HopDongID]
			  ,[SoHopDong]
			 , DmMaHopDongREF
			  ,TenMaHopDong
			  ,[NgayDanhSoHopDong] NgayDanhSo
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
			  ,SysNhanVienREF
			  ,TenDangNhap
			  ,TenNhanVien
			  ,TenKhachHang
			 , [NhanHang]
			  ,[DmNhomNganhREF]
			  ,[TenNhomNganh]
			  ,DmHinhThucQuangCao
			  ,TenHinhThucQuangCao
			  ,DmSanPhamREF
			  ,TenSanPham
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
			  ,0[TongViewThucChay]
			  ,0[TongClickThucChay]
			  ,0[TongSoBaiViet]
			  ,0 [SoLuongThucChay]
			  ,@NgayThucHien NgayThucHien
			  ,SUM([ThanhTienSauTrietKhauThucChay]+[GiaTriThayDoi]) GiaTriThayDoi
			  ,0[ThanhTienThucChayTruocTrietKhau]
			  ,0[GiaTriTrietKhauThucChay]
			  ,0 [ThanhTienSauTrietKhauThucChay]
			  ,0[GiaTriHoaHongThucChay]
			  ,0[ThanhTienThucThu]
			  ,SUM([ThanhTienKM]+[GiaTriKMThayDoi]) [ThanhTienKM]
			  ,SUM([SoLuongThucChayKM]+[SoLuongKMThayDoi]) [SoLuongThucChayKM]
			  ,0[SoLuongThucChayLechTreoHa]
			  ,0[ThanhTienLechTreoHa]
			  ,getdate()[CreatedAt]
			  ,getdate()[LastModifiedAt]
			  ,0 [IsPheDuyet]
			  ,''[PheDuyetBy]
			  ,''[PheDuyetAt]
			  ,SUM([SoLuongThucChay]+[SoLuongThayDoi])[SoLuongThayDoi]
			  ,0[SoLuongKMThayDoi]
			  ,0[GiaTriKMThayDoi]
			  ,@GhiChu Note
			  FROM [ThucChayDaTinhAdmarket]
			  where HopDongID = @HopDongId
			  AND HopDongChiTietREF = @PhanBoId
   		      AND NgayThucHien < @NgayThucHien
			  GROUP BY
			    [HopDongID]
			  ,[SoHopDong]
			  , DmMaHopDongREF
			  ,TenMaHopDong
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
			  ,SysNhanVienREF
			  ,TenDangNhap
			  ,TenNhanVien
			  ,TenKhachHang
			 , [NhanHang]
			  ,[DmNhomNganhREF]
			  ,[TenNhomNganh]
			  ,DmHinhThucQuangCao
			  ,TenHinhThucQuangCao
			  ,DmSanPhamREF
			  ,TenSanPham
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
			)TCDT_Admarket
			WHERE ISNULL(TCDT_Admarket.GiaTriThayDoi,0) <> 0
END


/****** Object:  StoredProcedure [dbo].[ThucChayDaTinhBoxAppSSV_InsertByPhanBoID]    Script Date: 9/9/2014 4:30:35 PM ******/
SET ANSI_NULLS ON

```
