# Stored Procedure: `ThucChay_InsertThucChayDaTinh_SponsorPost`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-11-04 17:14:05.887000
- **Ngày sửa cuối**: 2015-04-08 15:58:06.080000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@TenWebsite` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@TypeProduct` | `int(4)` | No |
| `@ProductUnitName` | `nvarchar(100)` | No |
| `@BannerType` | `int(4)` | No |
| `@TongViewThucChay` | `int(4)` | No |
| `@TongClickThucChay` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_InsertThucChayDaTinh]

--[ThucChay_InsertThucChayDaTinh_SponsorPost] '2015-04-07','DT1420315','afamily.vn', 74638 ,-1,'CPC',4,34754,8
CREATE PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_SponsorPost] 
	@NgayThucHien DATETIME,
	@SoHopDong NVARCHAR(50),
	@TenWebsite NVARCHAR(50),
	@HopDongChiTietID INT,	
	@TypeProduct INT,
	@ProductUnitName NVARCHAR(50),
	@BannerType INT,
	@TongViewThucChay INT,
	@TongClickThucChay INT
	
AS
BEGIN

INSERT INTO dbo.ThucChayDaTinhSponsorPost 
SELECT TC.* FROM (
	SELECT  NEWID() ThucChayDaTinhID, TD.*, 
	ISNULL(((TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) AS GiaTriTrietKhauThucChay,
	ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) AS ThanhTienSauTrietKhauThucChay,
	ISNULL((((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0) AS GiaTriHoaHongThucChay,
	ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100 - ((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0) AS ThanhTienThucThu,
	(CASE when ((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) then TD.ThanhTienThucChayTruocTrietKhau
		else 0
	  END
	) as ThanhTienKM,
	(CASE when (((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100))AND (TD.DonViTinh = 'VIEW')) 
			then ISNULL(dbo.ThucChay_GetSoLuongThucChayKMMobile(TD.HopDongChiTietREF,1,TD.DonGiaTheoDonViTinh,TD.NgayThucHien,TD.TongViewThucChay),0)
		  when (((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100))AND (TD.DonViTinh = 'CLICK')) 
			then ISNULL(dbo.ThucChay_GetSoLuongThucChayKMMobile(TD.HopDongChiTietREF,1,TD.DonGiaTheoDonViTinh,TD.NgayThucHien,TD.TongClickThucChay),0)
		else 0
	  END
	) as SoLuongThucChayKM,
	(CASE when (TD.DonViTinh = 'VIEW') then dbo.ThucChay_GetSoLuongLechTreoHaThucChayMobile(TD.HopDongChiTietREF,TD.DonGiaTheoDonViTinh,TD.NgayThucHien,TD.TongViewThucChay)
		when  (TD.DonViTinh = 'CLICK') then dbo.ThucChay_GetSoLuongLechTreoHaThucChayMobile(TD.HopDongChiTietREF,TD.DonGiaTheoDonViTinh,TD.NgayThucHien,TD.TongClickThucChay)
		else 0
	  END
	)AS SoLuongLechTreoHa,
	(CASE when (TD.DonViTinh = 'VIEW') then dbo.ThucChay_GetSoLuongLechTreoHaThucChayMobile(TD.HopDongChiTietREF,TD.DonGiaTheoDonViTinh,TD.NgayThucHien,TD.TongViewThucChay)*TD.DonGiaTheoDonViTinh*(100-TD.ChietKhau)/100
		when  (TD.DonViTinh = 'CLICK') then dbo.ThucChay_GetSoLuongLechTreoHaThucChayMobile(TD.HopDongChiTietREF,TD.DonGiaTheoDonViTinh,TD.NgayThucHien,TD.TongClickThucChay)*TD.DonGiaTheoDonViTinh*(100-TD.ChietKhau)/100
		else 0
	  END
	)AS ThanhTienLechTreoHa,
	GETDATE() CreatedAt,
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
	D.NhanHopDong, D.NgayNhanBanFax, D.NgayNhanHopDongBanCung, D.NgayChuyenHopDongChoKeToan, 
	D.So, D.Thang, D.Nam, 
	--Thong tin ve gia tri
	D.GiaTriHopDong, D.CongNo,
	--Thong tin chi tiet phan bo
	C.HopDongChiTietID HopDongChiTietREF,
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
	dbo.GetProductIDByTypeProduct(@TypeProduct) as DmSanPhamREF,
	dbo.GetProductNameByTypeProduct(@TypeProduct) as TenSanPham,  
	C.DmNhomWebsiteREF, 
	C.TenNhomWebsite, 
	C.DmChuyenMucREF, 
	C.TenChuyenMuc, 
	C.DmLoaiBannerREF, 
	C.TenLoaiBanner, 
	C.DmViTriREF, 
	C.TenViTri, 
	ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,'Y'),'') DotChayHopDong,
	C.SoLuong AS SoLuongDotChayHD,
	ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,'N'),0) DotChayBooking,
	0 SoLuongDotChayBooking,
	--Thong tin ve Tien
	--****haidh chinh sua
	C.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS SoLuong,
	'CLICK'AS DonViTinh,	
	dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,C.HopDongChiTietID,C.DonGia) as DonGia,
	dbo.ThucChay_GetDonGiaTheoDonViTruocChietKhau(C.HopDongChiTietID,@ProductUnitName,@BannerType,@NgayThucHien)
	AS DonGiaTheoDonViTinh,
	C.ChietKhau, C.GiamGia, C.ThanhTien,
	C.TiLeTuVan,  C.ChiPhiTuVan,
	C.IsKhuyenMai,  
	C.KhuyenMai,
	----Thuc chay
	0 DmBannerREF,--A.DmBannerREF,
	0 DmChienDichREF,--A.DmChienDichREF,
	(SELECT TOP 1 DmWebsiteReportingdbID FROM DmWebsiteReportingdb WHERE DmWebsiteReportingdb.TenWebsite = @TenWebsite) DmWebsiteREF,
	@TenWebsite TenWebsite,
	@TongViewThucChay TongViewThucChay,
	@TongClickThucChay TongClickThucChay,
	0 TongSoBaiViet,
	dbo.[ThucChay_GetSoLuongThucChayMobile](@HopDongChiTietID, 
											dbo.ThucChay_GetDonGiaTheoDonViTruocChietKhau(C.HopDongChiTietID,'CPC',@BannerType,@NgayThucHien),
											@NgayThucHien, 
											@TongViewThucChay,
											@TongClickThucChay,
											dbo.ThucChay_GetDonViTinhSponsorByHopDongChiTietID(C.HopDongChiTietID,@NgayThucHien)) 
	as SoLuongThucChay,
	@NgayThucHien NgayThucHien,
	0 as GiaTriThayDoi,
	ISNULL(dbo.ThucChay_GetThanhTienChuanThucChay_Mobile(@NgayThucHien,@HopDongChiTietID, @ProductUnitName,@BannerType,														 
														 @TongViewThucChay,
														 @TongClickThucChay),0) as ThanhTienThucChayTruocTrietKhau	
		
	FROM HopDongChiTiet C
	 INNER JOIN  HopDong D on D.HopDongID = C.HopDongFK	  
	WHERE C.HopDongChiTietID = @HopDongChiTietID  
	 AND D.TrangThaiHopDong != 3
	 AND C.DeletedStatus = 0
	 AND C.DmSanPhamREF IN (381)
	) TD		
)TC
WHERE (TC.SoLuongThucChay >0 OR TC.SoLuongThucChayKM > 0 OR TC.SoLuongLechTreoHa > 0)
AND (TC.SoLuongThucChay IS NOT NULL OR TC.SoLuongThucChayKM IS NOT NULL OR TC.SoLuongLechTreoHa IS NOT NULL)
END



```
