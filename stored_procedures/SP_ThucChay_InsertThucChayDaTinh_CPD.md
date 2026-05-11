# Stored Procedure: `ThucChay_InsertThucChayDaTinh_CPD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-21 15:51:28.507000
- **Ngày sửa cuối**: 2016-03-05 09:44:57.580000

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

--EXEC [ThucChay_InsertThucChayDaTinh]

--DELETE FROM ThucChayDaTinh

CREATE  PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_CPD] 
	@StartDate datetime,
	@EndDate datetime
AS
BEGIN

DECLARE @NgayThucHien DATETIME
set @NgayThucHien = @StartDate
--delete from dbo.ThucChayTemp
--Delete ThucChayDaTinh
DELETE FROM ThucChayDaTinh
WHERE convert(date,NgayThucHien) BETWEEN @StartDate AND @EndDate
AND DmSanPhamREF IN (140,228,564,549) 
AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, DonViTinh) = 1 --Đơn vị của hình thức CPD 

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
	(CASE when ((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) then ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_CPD(@NgayThucHien, TD.HopDongChiTietID),0)
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
	D.HopDongID,
	--Thong tin ve ma so 
	D.SoHopDong, 
	D.DmMaHopDongREF, 
	D.TenMaHopDong, 
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
	--Thong tin ve Tien
	dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,'Y') DotChayHopDong,
	C.SoLuong AS SoLuongDotChayHD,
	dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,'N') DotChayBooking,
	dbo.GetSoLuongDotChayBookingByHopDongChiTiet(C.HopDongChiTietID) SoLuongDotChayBooking,
	ISNULL(dbo.ThucChay_GetSoLuongChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,c.HopDongChiTietID),0) AS SoLuong, 
	dbo.FormatDonViTinh(C.DonViTinh) DonViTinh, 
	dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,c.HopDongChiTietID,C.DonGia) as DonGia, 
	ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong, @NgayThucHien, c.HopDongChiTietID),0) AS DonGiaTheoDonViTinh,
	C.ChietKhau, C.GiamGia, C.ThanhTien,
	C.TiLeTuVan,  C.ChiPhiTuVan,
	C.IsKhuyenMai,  
	C.KhuyenMai,
	--Thuc chay
	0 DmBannerREF,--A.DmBannerREF,
	0 DmChienDichREF,--A.DmChienDichREF,
	dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(C.DmWebsiteREF) DmWebsiteREF,
	--A.DmWebsiteREF,
	dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF,C.TenWebsite) TenWebsite,
	--C.TenWebsite,
	--A.SoHopDong,
	0 TongViewThucChay,
	0 TongClickThucChay,
	0 TongSoBaiViet,
	(CASE when C.IsKhuyenMai=0 then ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_CPD(@NgayThucHien, C.HopDongChiTietID),0)
		else 0
	  END
	) as SoLuongThucChay,
	--Thanh Tien Thuc Chay
	@NgayThucHien AS NgayThucHien,
	--dbo.ThucChay_TinhGiaTriThayDoi(C.DonViTinh,@NgayThucHien,C.HopDongChiTietID,C.HopDongFK,C.ThanhTien,
	--		ISNULL(dbo.ThucChay_GetSoLuongChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,c.HopDongChiTietID),0)) as GiaTriThayDoi,
	0 as GiaTriThayDoi,
	ISNULL(dbo.ThucChay_GetThanhTienChuanThucChay_CPD(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong,@NgayThucHien, c.HopDongChiTietID),0) as ThanhTienThucChayTruocTrietKhau
	FROM 
	(
		SELECT * FROM HopDongChiTiet WHERE DmSanPhamREF in (140,228,564,549)
		AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](DonViTinhREF, DonViTinh) = 1 --Đơn vị của hình thức CPD 
		AND DmLoaiREF <> 13 --Khong tinh thuc chay cho HTQC Mua Ngoai		
		
	) C  
	INNER JOIN  
	 ( 
	 	SELECT * FROM HopDong hd  WHERE hd.TrangThaiHopDong != 3
	 ) D on D.HopDongID = C.HopDongFK
	--INNER JOIN DmSanPham E ON E.DmSanPhamID = C.DmSanPhamREF
	AND dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_CPD(@NgayThucHien, C.HopDongChiTietID) >0	 
	) TD
	
	SET @NgayThucHien = dateadd(d,1,@NgayThucHien)	
end 	 

SELECT '1'
END




--EXEC [ThucChay_InsertThucChayDaTinh_CPD] '2014-04-01','2014-04-01'

```
