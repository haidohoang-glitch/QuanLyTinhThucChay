# Stored Procedure: `sp_TC_InsertThucTreoThayDoi_CPM`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-19 16:19:10.897000
- **Ngày sửa cuối**: 2022-12-21 15:31:44.237000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTiet` | `int(4)` | No |
| `@NgaythucHien` | `datetime(8)` | No |
| `@GiaTriThayDoi` | `float(8)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(200)` | No |
| `@DmBannerID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_InsertThucChayDaTinh_PR]


CREATE  PROCEDURE [dbo].[sp_TC_InsertThucTreoThayDoi_CPM]
	@HopDongChiTiet INT,
	@NgaythucHien DATETIME,
	@GiaTriThayDoi FLOAT,
	@DmWebsiteREF INT,
	@TenWebsite NVARCHAR(100),
	@DmBannerID INT
AS
BEGIN
	--PRINT @HopDongChiTiet
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
	'CPM_TTR' DotChayHopDong,
	C.SoLuong AS SoLuongDotChayHD,
	'PS THUC TREO CPM' DotChayBooking,
	0 AS SoLuongDotChayBooking, 
	--Thong tin ve Tien
	C.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS SoLuong,
	dbo.ThucChay_GetDonViTinhNotCPD(C.DonViTinh) as DonViTinh, 
	--'VIEW' DonViTinh, 
	dbo.ThucChay_GetDonGiaByNgayThucHien(@NgaythucHien,@HopDongChiTiet,C.DonGia) as DonGia, 
	ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong, @NgaythucHien, @HopDongChiTiet),0) AS DonGiaTheoDonViTinh,
	C.ChietKhau, C.GiamGia, C.ThanhTien,
	C.TiLeTuVan,  C.ChiPhiTuVan,
	C.IsKhuyenMai,  
	C.KhuyenMai,
	--Thuc chay
	@DmBannerID DmBannerREF,--A.DmBannerREF,
	0 DmChienDichREF,--A.DmChienDichREF,
	@DmWebsiteREF DmWebsiteREF,
	@TenWebsite TenWebsite,
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
		SELECT * FROM HopDongChiTiet 
		WHERE 1=1 
		--AND DmSanPhamREF in (231,238,339,342,337,240,370,598,613)
		AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = HopDongChiTiet.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 2 --Nhom Tinh Branding
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
							))
		AND HopDongChiTietID = @HopDongChiTiet
		AND DeletedStatus = 0
		AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](DonViTinhREF, DonViTinh) = 3 --Đơn vị của hình thức CPM
	) C  
	INNER JOIN  
	 ( 
	 	SELECT * FROM HopDong hd 
	    WHERE hd.TrangThaiHopDong != 3
	 ) D on D.HopDongID = C.HopDongFK
	INNER JOIN DmSanPham E ON E.DmSanPhamID = C.DmSanPhamREF
	) TD

END

```
