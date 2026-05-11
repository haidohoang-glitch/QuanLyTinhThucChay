# Stored Procedure: `ThucChay_InsertThucChayDaTinh_CPD_KhongDotChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:21:23.237000
- **Ngày sửa cuối**: 2022-11-23 16:08:57.190000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE  PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_CPD_KhongDotChay] 
	@StartDate datetime,
	@EndDate datetime
AS
BEGIN

DECLARE @NgayThucHien DATETIME
, @NgayDanhSo_GioiHan DATETIME

set @NgayThucHien = @StartDate
set @NgayDanhSo_GioiHan = '2018-01-01'

DELETE FROM ThucChayDaTinh
WHERE convert(date,NgayThucHien) BETWEEN @StartDate AND @EndDate
AND DmSanPhamREF IN (140,228,564,549,5082) 
AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, DonViTinh) = 1 --Đơn vị của hình thức CPD 
AND DotChayHopDong = 'CPD_KhongDotChay'
AND SoLuongDotChayHD = 0
AND NOT(DmHinhThucQuangCao = 13 OR DmLoaiBannerREF IN (17,18))
AND NgayDanhSoHopDong >= @NgayDanhSo_GioiHan

WHILE(@NgayThucHien <= @EndDate)
BEGIN
	INSERT INTO dbo.ThucChayDaTinh 
	SELECT  NEWID(), TD.*, 
	ISNULL((TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100,0) AS GiaTriTrietKhauThucChay,
	ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) AS ThanhTienSauTrietKhauThucChay,
	ISNULL(((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100,0) AS GiaTriHoaHongThucChay,
	ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100 - ((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0) AS ThanhTienThucThu,
	(CASE when ((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) then TD.ThanhTienThucChayTruocTrietKhau
		else 0
	  END
	) as ThanhTienKM,
	(CASE when ((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) then ISNULL(dbo.ThucChay_GetSoLuongThucChayTinVip(@NgayThucHien, TD.HopDongChiTietID),0)
		else 0
	  END
	) as SoLuongThucChayKM,
	0 SoLuongThucChayLechTreoHa,
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
	D.HopDongID, D.SoHopDong, 
	D.DmMaHopDongREF,D.TenMaHopDong, 
	--Thong tin ve thoi gian
	D.NgayDanhSoHopDong, D.NgayKyHopDong, 
	D.NhanHopDong, D.NgayNhanBanFax, D.NgayNhanHopDongBanCung, D.NgayChuyenHopDongChoKeToan, 
	D.So, D.Thang, D.Nam, 
	--Thong tin ve gia tri
	D.GiaTriHopDong, D.CongNo,
	--Thong tin chi tiet phan bo
	C.HopDongChiTietID,
	--Thong tin ve trang thai
	D.DangSuDung, D.IsGiayPhep, D.TrangThaiHopDong,D.IsBanCung, 
	--Thong tin ve Nhan vien kinh doanh
	D.DmPhongBanREF, ISNULL(D.TenPhongBan, '') AS TenPhongBan, 
	D.DmBoPhanREF, ISNULL(D.TenBoPhan,'') AS TenBoPhan, 
	D.DmNhomLamViecREF,	ISNULL(D.TenNhom, '') AS TenNhom, 
	D.DmDiaDiemLamViecREF,	D.TenDiaDiemLamViec, 
	D.SysNhanVienREF, ISNULL(D.TenDangNhap, '') AS TenDangNhap,  
	D.TenNhanVien, 
	D.TenKhachHang, 
	--C.NhanHang, 
	[dbo].[f_ReturnListConcatNhanHangREF_v2](C.HopDongChiTietID, @NgayThucHien)NhanHang,
	C.DmNhomNganhREF,C.TenNhomNganh, 
	--Thong tin hinh thuc quang cao
	C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
	--Thong tin San pham
	c.DmSanPhamREF as DmSanPhamREF,	C.TenSanPham,  
	C.DmNhomWebsiteREF, C.TenNhomWebsite, 
	C.DmChuyenMucREF, C.TenChuyenMuc,
	C.DmLoaiBannerREF, C.TenLoaiBanner, 
	C.DmViTriREF, C.TenViTri, 
	--Thong tin ve Tien
	'CPD_KhongDotChay' DotChayHopDong,
	0 SoLuongDotChayHD,
	--Thong tin dot chay cua thuc treo ( vi tinh thuc chay theo dot chay va thuc treo hd)	
	dbo.GetDotChayThucTreoByHopDongChiTiet(C.HopDongChiTietID,'Y') DotChayBooking,
	ISNULL([dbo].[GetSoLuongDotChayThucTreoByHopDongChiTiet](C.HopDongChiTietID),0) SoLuongDotChayBooking,
	--0 SoLuongDotChayBooking,
	C.SoLuong AS SoLuong, 
	dbo.FormatDonViTinh(C.DonViTinh) DonViTinh,
	dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,c.HopDongChiTietID,C.DonGia) as DonGia, 
	ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh_CPDKhongDotChay(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong, @NgayThucHien, c.HopDongChiTietID),0) AS DonGiaTheoDonViTinh,
	C.ChietKhau, C.GiamGia, C.ThanhTien,
	C.TiLeTuVan,  C.ChiPhiTuVan,
	C.IsKhuyenMai,  
	C.KhuyenMai,
	--Thuc chay
	0 DmBannerREF,
	0 DmChienDichREF,
	--dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(C.DmWebsiteREF) DmWebsiteREF,
	dbo.[GetDmWebsiteReportingdbIDByDmWebsiteID_CPD](C.DmWebsiteREF) DmWebsiteREF,
	--dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF,C.TenWebsite) TenWebsite,
	dbo.[GetWebsiteLinkByDmWebsiteID_CPD](C.DmWebsiteREF,C.TenWebsite) TenWebsite,
	0 TongViewThucChay,
	0 TongClickThucChay,
	0 TongSoBaiViet,
	(CASE when C.IsKhuyenMai=0 then ISNULL(dbo.ThucChay_GetSoLuongThucChayTinVip(@NgayThucHien, C.HopDongChiTietID),0)
		else 0
	  END
	) as SoLuongThucChay,
	--Thanh Tien Thuc Chay
	@NgayThucHien AS NgayThucHien,
	0 as GiaTriThayDoi,
	ISNULL(dbo.ThucChay_GetThanhTienChuanThucChay_CPDKhongDotChay(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong,@NgayThucHien, c.HopDongChiTietID),0) as ThanhTienThucChayTruocTrietKhau
	FROM 
	(
		SELECT DISTINCT  HopDongChiTiet.* FROM HopDongChiTiet INNER JOIN ThucChayHopDongChiTiet tchdct
		ON HopDongChiTiet.HopDongChiTietID = tchdct.HopDongChiTietREF
		WHERE HopDongChiTiet.DmSanPhamREF in (140,228,564,549,5082)
		AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](HopDongChiTiet.DonViTinhREF, HopDongChiTiet.DonViTinh) = 1 --Đơn vị của hình thức CPD 
		AND HopDongChiTiet.DeletedStatus = 0
		AND tchdct.DeletedStatus = 0
		AND HopDongChiTiet.DmLoaiBannerREF NOT IN (17,18)
		AND HopDongChiTiet.DmLoaiREF <> 13 --Khong tinh thuc chay cho HTQC Mua Ngoai
		AND CONVERT(DATE,tchdct.ThoiGianBatDau)  <= CONVERT(DATE,@NgayThucHien)
		AND CONVERT(DATE,tchdct.ThoiGianKetThuc) >= CONVERT(DATE,@NgayThucHien)
		AND [dbo].[ThucChay_CheckSanPhamCPDKhongDotChay](HopDongChiTiet.HopDongChiTietID, @NgayThucHien) = 1 
	) C  
	INNER JOIN  
	( 
	 	SELECT * FROM HopDong hd  WHERE hd.TrangThaiHopDong <> 3
		AND hd.NgayDanhSoHopDong >= @NgayDanhSo_GioiHan
	) D on D.HopDongID = C.HopDongFK
	) TD
	WHERE 1=1 
	
	SET @NgayThucHien = dateadd(d,1,@NgayThucHien)	
end 	 

--SELECT '1'
END

--EXEC [ThucChay_InsertThucChayDaTinh_CPD_KhongDotChay] '2014-06-15','2014-06-15'

```
