# Stored Procedure: `ThucChay_InsertThucChayDaTinh_BoxGiaVang_ByHopDongID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2019-11-12 15:43:17.960000
- **Ngày sửa cuối**: 2019-11-12 15:43:22.720000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_InsertThucChayDaTinh_BoxGiaVang] '2016-09-07','2016-09-30'
CREATE  PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_BoxGiaVang_ByHopDongID] 
	@StartDate datetime,
	@EndDate DATETIME,
	@HopDongID INT
AS
BEGIN
--DECLARE @StartDate DATETIME, @EndDate DATETIME
--SET @StartDate = '2014-01-01'
--SET @EndDate = '2014-01-02'
DECLARE @NgayThucHien DATETIME, @NgayGioiHanTinh DATETIME
SET @NgayGioiHanTinh = '2013-01-01'
set @NgayThucHien = @StartDate

--delete from dbo.ThucChayTemp
--DELETE FROM ThucChayDaTinh
--WHERE convert(date,NgayThucHien) BETWEEN @StartDate AND @EndDate
--AND DmSanPhamREF IN (385) 
--------------
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
	'' DotChayHopDong,
	isnull(dbo.ThucChay_GetSoLuongNgayThucTreo(C.HopDongChiTietID),0) AS SoLuongDotChayHD,
	(SELECT ThucChayHopDongChiTiet.ThucChayHopDongChiTietID 
		FROM ThucChayHopDongChiTiet 
		WHERE HopDongChiTietREF = C.HopDongChiTietID
		AND DeletedStatus = 0  
	)
	 DotChayBooking,
	'' SoLuongDotChayBooking,
	isnull(dbo.ThucChay_GetSoLuongNgayThucTreo(C.HopDongChiTietID),0) AS SoLuong, 
	dbo.FormatDonViTinh(C.DonViTinh) DonViTinh, 
	C.DonGia as DonGia, 
	(C.DonGia/isnull(dbo.ThucChay_GetSoLuongNgayThucTreo(C.HopDongChiTietID),0))
	AS DonGiaTheoDonViTinh,
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
	(CASE when C.IsKhuyenMai=0 THEN ISNULL(dbo.ThucChay_GetSoLuongThucChayBoxGiaVang(@NgayThucHien, C.HopDongChiTietID),0) 
		else 0
	  END
	) as SoLuongThucChay,
	--Thanh Tien Thuc Chay
	@NgayThucHien AS NgayThucHien,	
	0 as GiaTriThayDoi,
	ISNULL(((C.SoLuong*C.DonGia)/isnull(dbo.ThucChay_GetSoLuongNgayThucTreo(C.HopDongChiTietID),0))
			* ISNULL(dbo.ThucChay_GetSoLuongThucChayBoxGiaVang(@NgayThucHien, C.HopDongChiTietID),0),0)
		as ThanhTienThucChayTruocTrietKhau
	FROM 
	(
		SELECT * FROM dbo.HopDongChiTiet 
		WHERE DmSanPhamREF in (385,5005 ,5006,5007 
		, 5082 --Box tài trợ thông tin 
		) 
		AND DeletedStatus = 0 
		AND DmLoaiREF <> 13 --Khong tinh thuc chay cho HTQC Mua Ngoai
		AND ISNULL(dbo.ThucChay_GetSoLuongThucChayBoxGiaVang(@NgayThucHien, HopDongChiTietID),0) >0	 		
	) C  
	INNER JOIN  
	 ( 
	 	SELECT * FROM dbo.HopDong hd 
	    WHERE hd.TrangThaiHopDong <> 3
			AND hd.DeletedStatus = 0
			--AND hd.SoHopDong = 'QC2870916'
			AND hd.HopDongID = @HopDongID
	 ) D on D.HopDongID = C.HopDongFK
	) TD	
	SET @NgayThucHien = dateadd(d,1,@NgayThucHien)	
end 	
END

```
