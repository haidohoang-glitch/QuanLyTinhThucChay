# Stored Procedure: `ThucChayDaTinhBoxappSSV_InsertNoContract`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-08 11:19:07.710000
- **Ngày sửa cuối**: 2015-06-15 15:48:18.047000

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
--
-- EXEC dbo.[ThucChayDaTinhBoxappSSV_InsertNoContract] '2015-06-09'
CREATE PROCEDURE [dbo].[ThucChayDaTinhBoxappSSV_InsertNoContract] 
	-- Add the parameters for the stored procedure here
	@NgayThucHien	DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
	DELETE FROM ThucChayDaTinh WHERE NgayThucHien = @NgayThucHien AND DmSanPhamREF = 375 AND SoHopDong = '-'

    INSERT INTO ThucChayDaTinh
    SELECT 
		NEWID(),
    	HopDongID,
    	'-' AS SoHopDong,
    	DmMaHopDongREF,
    	TenMaHopDong,
    	NgayDanhSoHopDong,
    	NgayKyHopDong,
    	NhanHopDong,
    	NgayNhanBanFax,
    	NgayNhanHopDongBanCung,
    	NgayChuyenHopDongChoKeToan,
    	So,
    	Thang,
    	Nam,
    	GiaTriHopDong,
    	CongNo,
    	HopDongChiTietREF,
    	375 as DangSuDung,
    	IsGiayPhep,
    	TrangThaiHopDong,
    	IsBanCung,
    	DmPhongBanREF,
    	TenPhongBan,
    	DmBoPhanREF,
    	TenBoPhan,
    	DmNhomLamViecREF,
    	TenNhomLamViec,
    	DmDiaDiemLamViecREF,
    	TenDiaDiemLamViec,
    	SysNhanVienREF,
    	TenDangNhap,
    	TenNhanVien,
    	TenKhachHang,
    	NhanHang,
    	DmNhomNganhREF,
    	TenNhomNganh,
    	DmHinhThucQuangCao,
    	TenHinhThucQuangCao,
    	DmSanPhamREF,
    	TenSanPham,
    	DmNhomWebsiteREF,
    	TenNhomWebsite,
    	DmChuyenMucREF,
    	TenChuyenMuc,
    	DmLoaiBannerREF,
    	TenLoaiBanner,
    	DmViTriREF,
    	TenViTri,
    	DotChayHopDong,
    	SoLuongDotChayHD,
    	DotChayBooking,
    	SoLuongDotChayBooking,
    	SoLuong,
    	DonViTinh,
    	DonGia,
    	DonGiaTheoDonVi,
    	ChietKhau,
    	GiamGia,
    	ThanhTien,
    	TiLeTuVan,
    	ChiPhiTuVan,
    	IsKhuyenMai,
    	KhuyenMai,
    	DmBannerREF,
    	DmChienDichREF,
    	DmWebsiteREF,
    	TenWebsite,
    	TongViewThucChay,
    	TongClickThucChay,
    	TongSoBaiViet,
    	SoLuongThucChay,
    	NgayThucHien,
    	GiaTriThayDoi,
    	ThanhTienThucChayTruocTrietKhau,
    	GiaTriTrietKhauThucChay,
    	ThanhTienSauTrietKhauThucChay,
    	GiaTriHoaHongThucChay,
    	ThanhTienThucThu,
    	ThanhTienKM,
    	SoLuongThucChayKM,
    	SoLuongThucChayLechTreoHa,
    	ThanhTienLechTreoHa,
    	CreatedAt,
    	LastModifiedAt,
    	IsPheDuyet,
    	PheDuyetBy,
    	PheDuyetAt,
		0 as SoLuongThayDoi,
		0 as SoLuongKMThayDoi,
		0 as GiaTriKMThayDoi,
		'' as GhiChu
    FROM ThucChayDaTinhBoxAppSSV A
    WHERE A.NgayThucHien = @NgayThucHien
		AND A.HopDongID = 0
		AND A.SoHopDong = ''
		AND A.DmSanPhamREF = 375
END

/****** Object:  StoredProcedure [dbo].[ThucChayDaTinh_BoxappSSV_InsertGiaTriThayDoi]    Script Date: 9/9/2014 4:34:25 PM ******/
SET ANSI_NULLS ON

```
