# Stored Procedure: `ThucChay_InsertThucChayDaTinh_CPDBySoHopDongDotChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:21:23.057000
- **Ngày sửa cuối**: 2020-12-15 15:15:29.853000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================


CREATE  PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_CPDBySoHopDongDotChay] 
	@StartDate datetime,
	@EndDate DATETIME,
	@SoHopDong NVARCHAR(50),
	@DmSanPhamREF INT
AS
BEGIN

DECLARE @NgayThucHien DATETIME
set @NgayThucHien = @StartDate

DELETE FROM ThucChayDaTinh
WHERE convert(date,NgayThucHien) BETWEEN @StartDate AND @EndDate
AND DmSanPhamREF = @DmSanPhamREF 
AND SoHopDong = @SoHopDong
AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, DonViTinh) = 1 --Đơn vị của hình thức CPD

WHILE(@NgayThucHien <= @EndDate)
BEGIN

	
	INSERT INTO dbo.ThucChayDaTinh 
	SELECT  NEWID(), TD.*, 
	ISNULL((TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100,0) AS GiaTriTrietKhauThucChay,
	ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) AS ThanhTienSauTrietKhauThucChay,
	ISNULL(((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100,0) AS GiaTriHoaHongThucChay,
	ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100 - ((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0) AS ThanhTienThucThu,
	(CASE when TD.IsKhuyenMai=1 then TD.ThanhTienThucChayTruocTrietKhau
		else 0
	  END
	) as ThanhTienKM,
	(CASE when TD.IsKhuyenMai=1 then ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_CPDDotChay(@NgayThucHien, TD.HopDongChiTietID),0)
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
	D.DmMaHopDongREF, D.TenMaHopDong, 
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
	D.TenNhanVien, D.TenKhachHang, 
	--C.NhanHang, 
	[dbo].[f_ReturnListConcatNhanHangREF_v2](C.HopDongChiTietID, @NgayThucHien) NhanHang,
	C.DmNhomNganhREF, C.TenNhomNganh, 
	--Thong tin hinh thuc quang cao
	C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
	--Thong tin San pham
	c.DmSanPhamREF as DmSanPhamREF,	C.TenSanPham,  
	C.DmNhomWebsiteREF, C.TenNhomWebsite, 
	C.DmChuyenMucREF,	C.TenChuyenMuc,
	C.DmLoaiBannerREF,  C.TenLoaiBanner, 
	C.DmViTriREF, 	C.TenViTri, 
	--Thong tin ve Tien
	dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,'Y') DotChayHopDong,
	ISNULL(dbo.ThucChay_GetSoLuongChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,c.HopDongChiTietID),0)AS SoLuongDotChayHD,
	--Thong tin dot chay cua thuc treo ( vi tinh thuc chay theo dot chay va thuc treo hd)	
	dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,'N') DotChayBooking,
	ISNULL([dbo].[GetSoLuongDotChayThucTreoByHopDongChiTiet](C.HopDongChiTietID),0) SoLuongDotChayBooking,
	C.SoLuong  AS SoLuong, 
	dbo.FormatDonViTinh(C.DonViTinh) DonViTinh, 
	dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,c.HopDongChiTietID,C.DonGia) as DonGia, 
	ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong, @NgayThucHien, c.HopDongChiTietID),0) AS DonGiaTheoDonViTinh,
	C.ChietKhau, C.GiamGia, C.ThanhTien,
	C.TiLeTuVan,  C.ChiPhiTuVan,
	C.IsKhuyenMai,  C.KhuyenMai,
	--Thuc chay
	0 DmBannerREF,
	0 DmChienDichREF,
	dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(C.DmWebsiteREF) DmWebsiteREF,
	dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF,C.TenWebsite) TenWebsite,
	0 TongViewThucChay,
	0 TongClickThucChay,
	0 TongSoBaiViet,
	(CASE when C.IsKhuyenMai=0 then ISNULL(dbo.ThucChay_GetSoLuongThucChayChuanByDonViTinh_CPDDotChay(@NgayThucHien, C.HopDongChiTietID),0)
		else 0
	  END
	) as SoLuongThucChay,
	--Thanh Tien Thuc Chay
	@NgayThucHien AS NgayThucHien,
	0 GiaTriThayDoi, --check lai ai cho them gttd nay????
	--dbo.ThucChay_TinhGiaTriThayDoi(C.DonViTinh,@NgayThucHien,C.HopDongChiTietID,C.HopDongFK,C.ThanhTien,
	--		ISNULL(dbo.ThucChay_GetSoLuongChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,c.HopDongChiTietID),0)) as GiaTriThayDoi,
	ISNULL(dbo.ThucChay_GetThanhTienChuanThucChay_CPD(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong,@NgayThucHien, c.HopDongChiTietID),0) as ThanhTienThucChayTruocTrietKhau
	FROM 
	(
		SELECT DISTINCT  HopDongChiTiet.* FROM HopDongChiTiet INNER JOIN DotChayHopDongChiTiet dchdct 
		ON HopDongChiTiet.HopDongChiTietID = dchdct.HopDongChiTietREF
		WHERE DmSanPhamREF in (140,228,564,549,5082)
		AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](DonViTinhREF, DonViTinh) = 1 --Đơn vị của hình thức CPD 
		AND HopDongChiTiet.DeletedStatus = 0
		AND dchdct.DeletedStatus = 0
		AND HopDongChiTiet.DmLoaiREF <> 13 --Khong tinh thuc chay cho HTQC Mua Ngoai
		AND CONVERT(DATE,dchdct.ThoiGianBatDau)  <= CONVERT(DATE,@NgayThucHien)
		AND CONVERT(DATE,dchdct.ThoiGianKetThuc) >= CONVERT(DATE,@NgayThucHien)
	) C  
	INNER JOIN  
	 ( 
	 	SELECT * FROM HopDong hd 
	    WHERE hd.TrangThaiHopDong != 3
	       AND hd.SOHOPDONG = @SoHopDong
	 ) D on D.HopDongID = C.HopDongFK
	) TD
	WHERE 1= 1
	--AND TD.SoLuongThucChay >0
	
	SET @NgayThucHien = dateadd(d,1,@NgayThucHien)	
end 	 

SELECT '1'
END
--EXEC [ThucChay_InsertThucChayDaTinh_CPDBySoHopDongDotChay] '2016-04-26','2016-04-26', 'QC2050416', 140

```
