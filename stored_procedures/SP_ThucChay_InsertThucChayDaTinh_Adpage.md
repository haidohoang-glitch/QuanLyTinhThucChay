# Stored Procedure: `ThucChay_InsertThucChayDaTinh_Adpage`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-09 15:29:14.290000
- **Ngày sửa cuối**: 2014-10-14 10:39:53.797000

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
-- EXEC ThucChay_InsertThucChayDaTinh_Adpage '2014-05-08'
CREATE PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_Adpage]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	INSERT INTO THucChayDaTinh
	SELECT NEWID(),
					B.HopDongID,
					B.SoHopDong,
					B.DmMaHopDongREF,
					B.TenMaHopDong,
					B.NgayDanhSoHopDong, B.NgayKyHopDong, B.NhanHopDong, B.NgayNhanBanFax,
					B.NgayNhanHopDongBanCung, B.NgayChuyenHopDongChoKeToan,
					B.So, B.Thang, B.Nam,
					B.GiaTriHopDong, B.CongNo,
					0 HopDongChiTietID,
					B.DangSuDung,B.IsGiayPhep,B.TrangThaiHopDong, B.IsBanCung,
					B.DmPhongBanREF, B.TenPhongBan,
					B.DmBoPhanREF, B.TenBoPhan,
					B.DmNhomLamViecREF, B.TenNhom,
					B.DmDiaDiemLamViecREF, B.TenDiaDiemLamViec,
					B.SysNhanVienREF, B.TenDangNhap, B.TenNhanVien,
					B.TenKhachHang,
					''NhanHang,
					0 DmNhomNganhREF, '' TenNhomNganh,
					15 AS DmHinhThucQuangCao, N'Ad-Page' AS TenHinhThucQuangCao,
					A.DmSanPhamREF DmSanPhamREF, A.TenSanPham TenSanPham,
					0 DmNhomWebsiteREF, '' TenNhomWebsite,
					0 DmChuyenMucREF, '' TenChuyenMuc,
					0 DmLoaiBannerREF, '' TenLoaiBanner,
					0 DmViTriREF, '' TenViTri,
					'' DotChayHopDong,
					0 AS SoLuongDotChayHD,
					0 DotChayBooking,
					0 SoLuongDotChayBooking,
					0 SoLuong,
					A.DonViTinh DonViTinh,
					0 as DonGia,
					0 AS DonGiaTheoDonViTinh,
					0 ChietKhau, 0 GiamGia, 0 ThanhTien,
					0 TiLeTuVan, 0 ChiPhiTuVan,
					0 isKhuyenMai, 0 KhuyenMai,
					--Thuc chay
					0 DmBannerREF,--A.DmBannerREF,
					0 DmChienDichREF,--A.DmChienDichREF,
					(SELECT TOP 1 DmWebsiteReportingdbID FROM DmWebsiteReportingdb WHERE DmWebsiteReportingdb.TenWebsite = A.TenWebsite) DmWebsiteREF,
					A.TenWebsite,
					0 TongView,
					0 TongClick,
					0 TongSoBaiViet,
					A.SoLuong SouongThucChay,
					A.NgayThucHien NgayThucHien,
					0 GiaTriThayDoi,
					0 AS ThanhTienThucChayTruocChietKhau,
					0 GiaTriChietKhau,
					A.ThanhTienThucChay AS ThanhTienSauTrietKhauThucChay,
					0 AS GiaTriHoaHongThucChay,
					0 AS ThanhTienThucThu,
					0 as ThanhTienKM,
					0 as SoLuongThucChayKM,
					0 SoLuongLechTreoHa,
					0 ThanhTienLechTreoHa,
					GETDATE(),
					GETDATE(),
					0 IsPheDuyet,
					'' PheDuyetBy,
					'' PheDuyetAt
				FROM ThucChayAdpage AS A
					INNER JOIN HopDong B ON B.SoHopDong=A.SoHopDong
					--INNER JOIN HopDongChiTiet C ON C.HopDongFK = B.HopDongID
				WHERE 1=1
					--B.SoHopDong = @SoHopDong
					AND A.NgayThucHien = @NgayThucHien
					--AND A.SiteID = @SiteId
					--and C.DmSanPhamREF = 305
					AND B.TrangThaiHopDong <> 3
END
```
