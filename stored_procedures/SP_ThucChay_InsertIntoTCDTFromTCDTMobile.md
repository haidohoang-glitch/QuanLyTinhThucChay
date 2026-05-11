# Stored Procedure: `ThucChay_InsertIntoTCDTFromTCDTMobile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-07-07 10:26:51.783000
- **Ngày sửa cuối**: 2017-01-19 09:58:35.330000

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
CREATE PROCEDURE [dbo].[ThucChay_InsertIntoTCDTFromTCDTMobile] 
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
    UPDATE thucchaydatinhmobile SET
	ThanhTienSauTrietKhauThucChay = SoLuongThucChay * DonGiaTheoDonVi * (1- ChietKhau/100)
	, ThanhTienThucChayTruocTrietKhau = SoLuongThucChay * DonGiaTheoDonVi 
	, ThanhTienThucThu = SoLuongThucChay * DonGiaTheoDonVi * (1- ChietKhau/100)
	, ThanhTienKM = SoLuongThucChayKM  *DonGiaTheoDonVi
	, ThanhTienLechTreoHa = SoLuongThucChayLechTreoHa* DonGiaTheoDonVi 
	--Xoa du lieu truoc khi insert
	DELETE FROM thucchaydatinhmobile WHERE DonViTinh IN ('CPM','CPC') AND ThanhTienSauTrietKhauThucChay = 0 AND GiaTriThayDoi = 0 AND NgayThucHien =@NgayThucHien
		DELETE FROM ThucChayDaTinh 
		WHERE NgayThucHien = @NgayThucHien AND DmSanPhamREF = 342 
		AND NOT(DmHinhThucQuangCao IN(42,13) or DmLoaiBannerREF IN (17,18))
		AND HopDongChiTietREF IN (
			SELECT HopDongChiTietID FROM dbo.HopDongChiTiet
			WHERE DmSanPhamREF = 342
			AND DeletedStatus = 0
			AND DmLoaiNenTangREF <> 8
		)
		--Insert du lieu tu bang ThucChayDaTinhMobile 
		INSERT INTO ThucChayDaTinh
		SELECT
			newid() ThucChayDaTinhID,
			HopDongID,
			SoHopDong,
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
			DangSuDung,
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
			SoLuongThayDoi,
			SoLuongKMThayDoi,
			GiaTriKMThayDoi,
			GhiChu
		 
		FROM ThucChayDaTinhMobile tcdtm WHERE NgayThucHien = @NgayThucHien AND DmSanPhamREF = 342 AND DmHinhThucQuangCao <> 13
		AND tcdtm.GiaTriThayDoi= 0
		
		INSERT INTO thucchaydatinh 
	SELECT * FROM ThucChayDaTinhMobile tcdtm WHERE tcdtm.GiaTriThayDoi <> 0 AND tcdtm.NgayThucHien = @NgayThucHien

END

```
