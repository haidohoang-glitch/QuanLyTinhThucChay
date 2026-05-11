# Stored Procedure: `ThucChay_InsertGiaTriThayDoi_SponsorPost`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-30 14:11:03.207000
- **Ngày sửa cuối**: 2014-11-19 12:24:48.737000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgaythucHien` | `datetime(8)` | No |
| `@GiaTriThayDoi` | `float(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [[ThucChay_InsertGiaTriThayDoi_SponsorPost]]


CREATE PROCEDURE [dbo].[ThucChay_InsertGiaTriThayDoi_SponsorPost] 
	@HopDongChiTietID INT,
	@NgaythucHien DATETIME,
	@GiaTriThayDoi FLOAT
AS
BEGIN

	INSERT INTO dbo.ThucChayDaTinh 
	SELECT  NEWID(), TD.*, 
  	0 GiaTriTrietKhauThucChay,
  	0 AS ThanhTienSauTrietKhauThucChay,
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
  	'' PheDuyetAt,
  	0 SoLuongThayDoi,
	 0 SoLuongKMThayDoi,
	 0 GiaTriKMThayDoi,
	 '' GhiChu
  	FROM 
  	(
  	SELECT 
  	--ID Hop Dong
  	D.HopDongID,
  	--Thong tin ve ma so 
  	D.SoHopDong, 
  	D.DmMaHopDongREF, 
  	D.TenMaHopDong, 
  	--Thong tin ve thoi gian
  	D.NgayDanhSoHopDong, D.NgayKyHopDong, 
  	ISNULL(D.NhanHopDong,'') AS NhanHopDong, D.NgayNhanBanFax, D.NgayNhanHopDongBanCung, D.NgayChuyenHopDongChoKeToan, 
  	D.So, D.Thang, D.Nam, 
  	--Thong tin ve gia tri
  	D.GiaTriHopDong, D.CongNo,
  	--Thong tin chi tiet phan bo
  	C.HopDongChiTietID,
  	--Thong tin ve trang thai
  	D.DangSuDung, D.IsGiayPhep, D.TrangThaiHopDong,D.IsBanCung, 
  	--Thong tin ve Nhan vien kinh doanh
  	D.DmPhongBanREF, 
  	ISNULL(D.TenPhongBan, '') AS TenPhongBan, 
  	D.DmBoPhanREF, 
  	ISNULL(D.TenBoPhan,'') AS TenBoPhan, 
  	D.DmNhomLamViecREF, 
  	ISNULL(D.TenNhom, '') AS TenNhom, 
  	D.DmDiaDiemLamViecREF, 
  	D.TenDiaDiemLamViec, 
  	D.SysNhanVienREF, 
  	ISNULL(D.TenDangNhap, '') AS TenDangNhap,  
  	D.TenNhanVien, 
  	--Thong tin ve khach hang
  	--D.DmKhachHangREF, 
  	D.TenKhachHang, 
  	C.NhanHang, 
  	C.DmNhomNganhREF, 
  	C.TenNhomNganh, 
  	--Thong tin hinh thuc quang cao
  	C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
  	--Thong tin San pham
  	c.DmSanPhamREF as DmSanPhamREF,
  	C.TenSanPham,  
  	C.DmNhomWebsiteREF, 
  	C.TenNhomWebsite, 
  	--C.DmWebsiteREF, 
  	--C.TenWebsite, 
  	C.DmChuyenMucREF, 
  	C.TenChuyenMuc,
  	C.DmLoaiBannerREF, 
  	C.TenLoaiBanner, 
  	C.DmViTriREF, 
  	C.TenViTri, 
  	'Sponsor Post' DotChayHopDong,
  	0 AS SoLuongDotChayHD,
  	'PS Update GTTD Sponsor Post' DotChayBooking,
  	0 AS SoLuongDotChayBooking, 
  	--Thong tin ve Tien
  	C.SoLuong, 
  	dbo.FormatDonViTinh(C.DonViTinh) DonViTinh, 
  	C.DonGia, 
  	C.DonGia DonGiaTheoDonViTinh,
  	C.ChietKhau, C.GiamGia, C.ThanhTien,
  	C.TiLeTuVan,  C.ChiPhiTuVan,
  	C.IsKhuyenMai,  
  	C.KhuyenMai,
  	--Thuc chay
  	0 DmBannerREF,--A.DmBannerREF,
  	0 DmChienDichREF,--A.DmChienDichREF,
  	dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(C.DmWebsiteREF) DmWebsiteREF,
  	dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF,C.TenWebsite) TenWebsite,
  	0 TongViewThucChay,
  	0 TongClickThucChay,
  	0 TongSoBaiViet,
  	0 SoLuongThucChay,
  	--Thanhuc Tien Thuc Chay
  	@NgayThucHien AS NgayThucHien,
  	@GiaTriThayDoi as GiaTriThayDoi,
  	0 as ThanhTienThucChayTruocTrietKhau
  	FROM 
  	(
  		SELECT * FROM HopDongChiTiet WHERE DmSanPhamREF in (381) 
  		AND HopDongChiTietID = @HopDongChiTietID
 
  	) C  
  	INNER JOIN  
  	 ( 
  	 	SELECT * FROM HopDong hd 
  	    WHERE hd.TrangThaiHopDong != 3
  	 ) D on D.HopDongID = C.HopDongFK
  --	INNER JOIN DmSanPham E ON E.DmSanPhamID = C.DmSanPhamREF
  	) TD

END




--EXEC [ThucChay_InsertGiaTriThayDoi_SponsorPost] '2013-07-01','2013-07-11'



```
