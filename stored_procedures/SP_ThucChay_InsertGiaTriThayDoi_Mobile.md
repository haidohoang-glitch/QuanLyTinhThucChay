# Stored Procedure: `ThucChay_InsertGiaTriThayDoi_Mobile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:21:19.243000
- **Ngày sửa cuối**: 2016-03-30 14:14:04.367000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTiet` | `int(4)` | No |
| `@NgaythucHien` | `datetime(8)` | No |
| `@GiaTriThayDoi` | `float(8)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(200)` | No |
| `@BannerType` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--ThucChay_InsertGiaTriThayDoi_Mobile 91102,'2016-02-15',2,56,'dantri.com.vn',

CREATE PROCEDURE [dbo].[ThucChay_InsertGiaTriThayDoi_Mobile]
	@HopDongChiTiet INT,
	@NgaythucHien DATETIME,
	@GiaTriThayDoi FLOAT,
	@DmWebsiteREF INT,
	@TenWebsite NVARCHAR(100),
	@BannerType INT--,
	--@ProductUnitName NVARCHAR(50)
AS
BEGIN	
	INSERT INTO dbo.ThucChayDaTinhMobile
	SELECT  NEWID(), TD.*	
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
	--C.NhanHang, 
	[dbo].[f_ReturnListConcatNhanHangREF_v2] 
	(
		C.HopDongChiTietID,
		@NgaythucHien
	)NhanHang,
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
	'Update Gia tri thay doi Mobile' DotChayHopDong,
	C.SoLuong AS SoLuongDotChayHD,
	'PS Gia tri thay doi Mobile' DotChayBooking,
	0 AS SoLuongDotChayBooking, 
	--Thong tin ve Tien
	C.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS SoLuong,
	(case when C.DonViTinh IN ('CPC','CPM') THEN  C.DonViTinh
	 ELSE C.TenLoai
	 END) AS DonViTinh, -- tuyetnta sửa
	dbo.ThucChay_GetDonGiaTheoDonViTruocChietKhau(C.HopDongChiTietID,dbo.ThucChay_GetDonViTinhMobileByHopDongChiTietID(C.HopDongChiTietID,@NgayThucHien),@BannerType,@NgaythucHien) 
	as DonGia, 
	dbo.ThucChay_GetDonGiaTheoDonViTruocChietKhau(C.HopDongChiTietID,dbo.ThucChay_GetDonViTinhMobileByHopDongChiTietID(C.HopDongChiTietID,@NgayThucHien),@BannerType,@NgaythucHien) 
	AS DonGiaTheoDonViTinh,
	C.ChietKhau, C.GiamGia, C.ThanhTien,
	C.TiLeTuVan,  C.ChiPhiTuVan,
	C.IsKhuyenMai,  
	C.KhuyenMai,
	--Thuc chay
	0 DmBannerREF,--A.DmBannerREF,
	0 DmChienDichREF,--A.DmChienDichREF,
	@DmWebsiteREF DmWebsiteREF,
	@TenWebsite TenWebsite,
	0 TongViewThucChay,
	0 TongClickThucChay,
	0 TongSoBaiViet,
	0 SoLuongThucChay,
	--Thanhuc Tien Thuc Chay
	@NgayThucHien AS NgayThucHien,
	(CASE WHEN C.IsKhuyenMai = 0 THEN @GiaTriThayDoi
		ELSE 0
	END	
	)as GiaTriThayDoi,
	0 as ThanhTienThucChayTruocTrietKhau,
	0 GiaTriTrietKhauThucChay,
	0 AS ThanhTienSauTrietKhauThucChay,
	0 AS GiaTriHoaHongThucChay,
	0 AS ThanhTienThucThu,
	0 as ThanhTienKM,
	0 as SoLuongThucChayKM,
	0 SoLuongLechTreoHa,
	0 ThanhTienLechTreoHa,
	GETDATE() CreatedAt,
	GETDATE() LastModified,
	0 IsPheDuyet,
	'' PheDuyetBy,
	'' PheDuyetAt,
	0 SoLuongThayDoi,
	0 SoLuongKMThayDoi,
	(CASE WHEN C.IsKhuyenMai = 1 THEN @GiaTriThayDoi
		ELSE 0
	END	
	)as GiaTriKMThayDoi,
	'' GhiChu	
	FROM 
	(
		SELECT * FROM HopDongChiTiet WHERE DmSanPhamREF in (342)
		AND HopDongChiTietID = @HopDongChiTiet
		AND DeletedStatus = 0		
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
