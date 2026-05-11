# Stored Procedure: `ThucChay_InsertThucChayDaTinh_SP_TMDT_BySoHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:21:22.753000
- **Ngày sửa cuối**: 2016-03-30 14:28:56.370000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_InsertThucChayDaTinh]



CREATE PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_SP_TMDT_BySoHopDong] 
	@StartDate datetime,
	@EndDate DATETIME,
	@SoHopDong NVARCHAR(50)
AS
BEGIN

DECLARE @NgayThucHien DATETIME
set @NgayThucHien = @StartDate

-- Tin vip	241
-- Box nổi bật	264
-- Box sản phẩm Hot	300
-- Siêu chăm sóc	268
-- Tin vip xuyên trang	248
-- sàn BĐS	270
-- Tin nổi bật	243
-- Top giao dịch hot 244
-- Tin đính 249

DELETE FROM ThucChayDaTinh
WHERE convert(date,NgayThucHien) BETWEEN @StartDate AND @EndDate
AND DmSanPhamREF IN (241,264,300,268,248,270,243,244,249) 
AND SoHopDong = @SoHopDong
AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, DonViTinh) = 1 --Đơn vị của hình thức CPD 

WHILE(@NgayThucHien <= @EndDate)
BEGIN
	INSERT INTO dbo.ThucChayDaTinh 
	SELECT * FROM 
	(
	SELECT  NEWID() ThucChayDaTinhID, TD.*, 
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
	GETDATE() CreatedAt,
	GETDATE() LastModifiedAt,
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
	--C.NhanHang, 
	[dbo].[f_ReturnListConcatNhanHangREF_v2] 
	(
		C.HopDongChiTietID,
		@NgayThucHien
	)NhanHang,
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
	dbo.GetDotChayThucTreoByHopDongChiTiet(C.HopDongChiTietID,'N') DotChayHopDong,
	ISNULL(dbo.ThucChay_GetSoLuongChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,c.HopDongChiTietID),0) AS SoLuongDotChayHD,
	dbo.GetDotChayThucTreoByHopDongChiTiet(C.HopDongChiTietID,'Y') DotChayBooking,
	isnull(dbo.[ThucChay_GetSoLuongChuan_TinVIP](@NgayThucHien, C.HopDongChiTietID),0) SoLuongDotChayBooking,
	C.SoLuong AS SoLuong, 
	dbo.FormatDonViTinh(C.DonViTinh) DonViTinh, 
	dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,c.HopDongChiTietID,C.DonGia) as DonGia, 
	ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh_TinVIP(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong, @NgayThucHien, c.HopDongChiTietID),0) AS DonGiaTheoDonViTinh,
	C.ChietKhau, C.GiamGia, C.ThanhTien,
	C.TiLeTuVan,  C.ChiPhiTuVan,
	C.IsKhuyenMai,  
	C.KhuyenMai,
	--Thuc chay
	0 DmBannerREF,
	0 DmChienDichREF,
	dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(C.DmWebsiteREF) DmWebsiteREF,
	dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF,C.TenWebsite) TenWebsite,
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
	ISNULL(dbo.ThucChay_GetThanhTienChuanThucChay_TinVip(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong,@NgayThucHien, c.HopDongChiTietID),0) as ThanhTienThucChayTruocTrietKhau
	FROM 
	(
		SELECT DISTINCT hdct.* FROM HopDongChiTiet hdct INNER JOIN ThucChayHopDongChiTiet tchdct 
		ON hdct.HopDongChiTietID = hdct.HopDongChiTietID
		WHERE hdct.DeletedStatus = 0
		AND tchdct.DeletedStatus = 0
		AND hdct.DmLoaiREF <> 13 --Khong tinh thuc chay cho HTQC Mua Ngoai
		AND hdct.DmSanPhamREF in (241,264,300,268,248,270,243,244,249)
		AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) = 1 --Đơn vị của hình thức CPD 
		AND CONVERT(DATE,tchdct.ThoiGianBatDau)  <= CONVERT(DATE,@NgayThucHien)
		AND CONVERT(DATE,tchdct.ThoiGianKetThuc) >= CONVERT(DATE,@NgayThucHien) 
	) C  
	INNER JOIN  
	 ( 
	 	SELECT * FROM HopDong hd  WHERE hd.TrangThaiHopDong != 3
	 	AND hd.SoHopDong = @SoHopDong
	 ) D on D.HopDongID = C.HopDongFK
	) TD
	)A
	WHERE (A.SoLuongThucChay >0 OR A.SoLuongThucChayKM >0 OR A.SoLuongThucChayLechTreoHa >0)
	SET @NgayThucHien = dateadd(d,1,@NgayThucHien)	
end 	 

SELECT '1'
END


--EXEC [ThucChay_InsertThucChayDaTinh_SP_TMDT_BySoHopDong] '2014-04-01','2014-04-01', 'QC123344'

```
