# Stored Procedure: `ThucChayDaTinhAdmarket_InsertNoContractByProduct_PhanBo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-02-06 11:06:08.670000
- **Ngày sửa cuối**: 2024-06-29 11:22:18.983000

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
| `@NhanHang` | `nvarchar(100)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@Data_Type` | `smallint(2)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		doannv
-- Create date: 2014-07-16
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinhAdmarket_InsertNoContractByProduct_PhanBo]
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
	@TenViTri				NVARCHAR(50),
	@NhanHang				NVARCHAR(50),
	@HopDongChiTietREF		INT,
	@Data_Type				SMALLINT
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
		@NhanHang NhanHang, 
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
		@GhiChu AS DotChayHopDong, -- Thuc_Chay_Admarket_PhanBo_online : dung cho phanbo <> 0
		@HopDongChiTietREF AS SoLuongDotChayHD, --Luu hopdongchitietid : dung cho phanbo <> 0
		'' DotChayBooking,
		@Data_Type AS SoLuongDotChayBooking, --LOAI DU LIEU ONLINE CAN CẢNH BAO 2,3: canh bao dl tra ve vuot qua gt hop dong; 1: Hopdong ko co phabo phu hop tinh, 0 online bt
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
		@GiaTriThayDoi as GiaTriThayDoi,
		0 as ThanhTienThucChayTruocTrietKhau,
		0 GiaTriTrietKhauThucChay,
		@ThanhTienThucChay AS ThanhTienSauTrietKhauThucChay,
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
		@SoLuongThayDoi as SoLuongThayDoi,
		0 as SoLuongKMThayDoi,
		0 as GiaTriKMThayDoi,
		@GhiChu as GhiChu
END




```
