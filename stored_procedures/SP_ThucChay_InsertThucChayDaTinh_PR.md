# Stored Procedure: `ThucChay_InsertThucChayDaTinh_PR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-07-05 13:42:14.097000
- **Ngày sửa cuối**: 2015-12-04 14:33:17.397000

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

--EXEC [ThucChay_InsertThucChayDaTinh_PR] '2015-01-15','2015-01-15'


CREATE PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_PR] 
	@StartDate datetime,
	@EndDate datetime
AS
BEGIN

DECLARE @NgayThucHien DATETIME, @NgayGioiHanTinh DATETIME
set @NgayThucHien = Convert(date,@StartDate)
SET @NgayGioiHanTinh = '2013-01-01'
--set @EndDate = CONVERT(date,@StartDate)

DELETE FROM ThucChayDaTinh
WHERE NgayThucHien BETWEEN @StartDate AND @EndDate
AND DmSanPhamREF IN (141,245,250,637,305)
AND NOT (DmHinhThucQuangCao = 13 or DmLoaiBannerREF = 18)

WHILE(@NgayThucHien <= @EndDate)
BEGIN

	INSERT INTO dbo.ThucChayDaTinh 
	SELECT NEWID(), A.* FROM (
	SELECT -- NEWID(), 
	distinct
	TD.*, 
	ISNULL((TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100,0) AS GiaTriTrietKhauThucChay,
	ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) AS ThanhTienSauTrietKhauThucChay,	
	ISNULL(((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100,0) AS GiaTriHoaHongThucChay,
	ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100 - ((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0) AS ThanhTienThucThu,
	(CASE when ((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) then TD.ThanhTienThucChayTruocTrietKhau
		else 0
	  END
	) as ThanhTienKM,
	(CASE when ((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) then ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_PR(@NgayThucHien,@NgayGioiHanTinh ,TD.HopDongChiTietID, TD.DmWebsiteREF),0)
		else 0
	  END
	) as SoLuongThucChayKM,
	0 SoLuongLechTreoHa,
	0 ThanhTienLechTreoHa,
	GETDATE()CreatedAt,
	GETDATE()LastModifiedAt,
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
	E.TenSanPham,  
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
	'' DotChayHopDong,
	0 AS SoLuongDotChayHD,
	--'' DotChayBooking,
	dbo.ThuChay_ConCatThuChayHopDongChiTietPR(@NgayThucHien,@NgayGioiHanTinh,c.HopDongChiTietID, F.DmWebsiteREF) DotChayBooking,
	0 AS SoLuongDotChayBooking, 
	--Thong tin ve Tien
	ISNULL(dbo.ThucChay_GetSoLuongChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,c.HopDongChiTietID),0) AS SoLuong, 
	dbo.FormatDonViTinh(C.DonViTinh) DonViTinh, 
	dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,c.HopDongChiTietID,C.DonGia) as DonGia, 
	--ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong, @NgayThucHien, c.HopDongChiTietID),0) AS DonGiaTheoDonViTinh,
	ISNULL(dbo.ThucChay_GetDonGiaThucTreo_PR(D.NgayKyHopDong, @NgayThucHien, C.HopDongChiTietID),0) AS DonGiaTheoDonViTinh,
	C.ChietKhau, C.GiamGia, C.ThanhTien,
	C.TiLeTuVan,  C.ChiPhiTuVan,
	C.IsKhuyenMai,  
	C.KhuyenMai,
	--Thuc chay
	0 DmBannerREF,--A.DmBannerREF,
	0 DmChienDichREF,--A.DmChienDichREF,
	dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(F.DmWebsiteREF) DmWebsiteREF,
	--A.DmWebsiteREF,
	dbo.GetWebsiteLinkByDmWebsiteID(F.DmWebsiteREF,F.TenWebsite) TenWebsite,
	--C.TenWebsite,
	--A.SoHopDong,
	0 TongViewThucChay,
	0 TongClickThucChay,
	0 TongSoBaiViet,
	(CASE when C.IsKhuyenMai=0 then ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_PR(@NgayThucHien, @NgayGioiHanTinh ,C.HopDongChiTietID,F.DmWebsiteREF),0)
		else 0
	  END
	) 
	as SoLuongThucChay,
	--Thanhuc Tien Thuc Chay
	@NgayThucHien AS NgayThucHien,
	0 as GiaTriThayDoi,
	ISNULL(dbo.ThucChay_GetThanhTienChuanThucChay_PR(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong,@NgayThucHien, @NgayGioiHanTinh ,c.HopDongChiTietID, F.DmWebsiteREF),0) as ThanhTienThucChayTruocTrietKhau
	FROM 
	(
		SELECT * FROM HopDongChiTiet WHERE DmSanPhamREF in (141,245,250,637,305) --PR
		--AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](DonViTinhREF, DonViTinh) = 2 --Đơn vị của hình thức Bài
		AND NOT (DmLoaiREF = 13 OR HopDongChiTiet.DmLoaiBannerREF = 18)
	) C  
	INNER JOIN  
	 ( 
	 	SELECT * FROM HopDong hd 
	    WHERE hd.TrangThaiHopDong != 3
	    AND hd.Nam >=2013
	   --    AND hd.SOHOPDONG IN ('DT740212'
				--)
	 ) D on D.HopDongID = C.HopDongFK
		 INNER JOIN
	 (
		SELECT * FROM ThucChayHopDongChiTietPR tchdctp 
		WHERE tchdctp.DeletedStatus <> 1
		AND tchdctp.RecordStatus = 0	
		--AND tchdctp.HopDongChiTietREF = 76655
		AND tchdctp.ThoiGianBatDau >= @NgayGioiHanTinh
		 AND (   CASE 
                                   WHEN tchdctp.CreatedAt >= tchdctp.LastModifiedAt THEN CONVERT(DATE,tchdctp.CreatedAt)
                                   ELSE CONVERT(DATE,tchdctp.LastModifiedAt)
                              END
                          ) = @NgayThucHien
	)
	F ON C.HopDongChiTietID = F.HopDongChiTietREF AND C.HopDongFK = F.HopDongREF
	INNER JOIN DmSanPham E ON E.DmSanPhamID = C.DmSanPhamREF			
	AND dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_PR(@NgayThucHien, @NgayGioiHanTinh ,C.HopDongChiTietID,F.DmWebsiteREF) >0	 
	) TD
	)A
	
	EXEC [ThucChay_UpdateThucChayHopDongChiTietPR] @NgayThucHien
	
	SET @NgayThucHien = dateadd(d,1,@NgayThucHien)	
end 	 

SELECT '1'
END

```
