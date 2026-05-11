# Stored Procedure: `ThucChayDaTinhAdmarket_InsertNoContractByProduct`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-11 15:02:54.847000
- **Ngày sửa cuối**: 2021-06-29 14:04:39.383000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(100)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(510)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoLuongThucChay` | `int(4)` | No |
| `@SoLuongThhucChayKM` | `int(4)` | No |
| `@ThanhTienThucChay` | `float(8)` | No |
| `@ThanhTienThucChayKM` | `float(8)` | No |
| `@DmMaHopDongREF` | `int(4)` | No |
| `@TenMaHopDong` | `nvarchar(100)` | No |
| `@GhiChu` | `nvarchar(510)` | No |
| `@GiaTriThayDoi` | `float(8)` | No |
| `@SoLuongThayDoi` | `int(4)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@TenViTri` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: 2014-07-16
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinhAdmarket_InsertNoContractByProduct]
	-- Add the parameters for the stored procedure here	
	@DmSanPhamREF			INT,
	@TenSanPham				NVARCHAR(50),
	@DonViTinh				NVARCHAR(50),
	@DmWebsiteREF			INT,
	@TenWebsite				NVARCHAR(255),
	@NgayThucHien			DATETIME,
	@SoLuongThucChay		INT,
	@SoLuongThhucChayKM		INT,
	@ThanhTienThucChay		FLOAT,
	@ThanhTienThucChayKM	FLOAT,
	@DmMaHopDongREF			INT,
	@TenMaHopDong			NVARCHAR(50),
	@GhiChu					NVARCHAR(255),
	@GiaTriThayDoi			FLOAT,
	@SoLuongThayDoi			INT,
	@DmViTriREF				INT,
	@TenViTri				NVARCHAR(50)--,
	--@NhanHang				NVARCHAR(50)
AS
BEGIN	
	
	INSERT INTO ThucChayDaTinhAdmarket
	SELECT  
		NEWID(), 
		0 HopDongID,
		'-' SoHopDong, 
		@DmMaHopDongREF DmMaHopDongREF, 
		@TenMaHopDong TenMaHopDong, 
		'' NgayDanhSoHopDong, 
		'' NgayKyHopDong, 
		'' NhanHopDong, 
		'' NgayNhanBanFax, 
		'' NgayNhanHopDongBanCung, 
		'' NgayChuyenHopDongChoKeToan, 
		0 So, 0 Thang, 0 Nam, 
		0 GiaTriHopDong, 0 CongNo,
		0 HopDongChiTietID,
		0 DangSuDung,
		0 IsGiayPhep, 
		1 TrangThaiHopDong,
		0 IsBanCung, 
		0 DmPhongBanREF, 
		''TenPhongBan, 
		0 DmBoPhanREF, 
		''TenBoPhan, 
		0 DmNhomLamViecREF, 
		''TenNhom, 
		0 DmDiaDiemLamViecREF, 
		'' TenDiaDiemLamViec, 
		0 SysNhanVienREF, 
		'' TenDangNhap,  
		'' TenNhanVien, 
		'' TenKhachHang, 
		--@NhanHang 
		''NhanHang, 
		0 DmNhomNganhREF, 
		'' TenNhomNganh, 
		0 DmHinhThucQuangCao, 
		'' TenHinhThucQuangCao, 
		@DmSanPhamREF DmSanPhamREF,
		@TenSanPham TenSanPham,  
		0 DmNhomWebsiteREF, 
		'' TenNhomWebsite, 
		0 DmChuyenMucREF, 
		'' TenChuyenMuc,
		0 DmLoaiBannerREF, 
		'' TenLoaiBanner, 
		@DmViTriREF DmViTriREF, 
		@TenViTri TenViTri, 
		@GhiChu AS DotChayHopDong,
		0 AS SoLuongDotChayHD,
		'' DotChayBooking,
		0 AS SoLuongDotChayBooking, 
		0 SoLuong,
		@DonViTinh, 
		0 DonGia, 
		0 DonGiaTheoDonViTinh,
		0 ChietKhau, 0 GiamGia, 0 ThanhTien,
		0 TiLeTuVan,  0 ChiPhiTuVan,
		0 IsKhuyenMai,  
		'' KhuyenMai,
		0 DmBannerREF,
		0 DmChienDichREF,
		@DmWebsiteREF DmWebsiteREF,
		@TenWebsite TenWebsite,
		0 TongViewThucChay,
		0 TongClickThucChay,
		0 TongSoBaiViet,
		@SoLuongThucChay as SoLuongThucChay,
		@NgayThucHien AS NgayThucHien,
		@ThanhTienThucChay as GiaTriThayDoi,
		0 as ThanhTienThucChayTruocTrietKhau,
		0 GiaTriTrietKhauThucChay,
		0 AS ThanhTienSauTrietKhauThucChay,
		0 AS GiaTriHoaHongThucChay,
		0 AS ThanhTienThucThu,
		@ThanhTienThucChayKM as ThanhTienKM,
		@SoLuongThhucChayKM as SoLuongThucChayKM,
		0 SoLuongLechTreoHa,
		0 ThanhTienLechTreoHa,
		GETDATE(),
		GETDATE(),
		0 IsPheDuyet,
		'' PheDuyetBy,
		'' PheDuyetAt,
		0 as SoLuongThayDoi,
		0 as SoLuongKMThayDoi,
		0 as GiaTriKMThayDoi,
		@GhiChu as GhiChu
END




```
