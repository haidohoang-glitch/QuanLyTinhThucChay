# Stored Procedure: `ThucChayDaTinh_BoxappSSV_InsertGiaTriThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:27:59.630000
- **Ngày sửa cuối**: 2016-03-17 09:27:59.630000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongId` | `int(4)` | No |
| `@PhanBoId` | `int(4)` | No |
| `@SanPhamId` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(100)` | No |
| `@WebsiteId` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(100)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@SoLuongThayDoiThucChay` | `float(8)` | No |
| `@GiaTriThayDoiThucChay` | `float(8)` | No |
| `@SoLuongThayDoiKhuyenMai` | `float(8)` | No |
| `@GiaTriThayDoiKhuyenMai` | `float(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-08-26
-- Description:	Insert gia tri thay doi
-- =============================================
--EXEC dbo.ThucChayDaTinh_BoxappSSV_InsertGiaTriThayDoi '2014-11-25', 27077, 60790, 375, 'Box App Self-serving', 83, 'genk.vn', 'VIEW', 322531, 1221941.81,0,0
CREATE PROCEDURE [dbo].[ThucChayDaTinh_BoxappSSV_InsertGiaTriThayDoi] 
	-- Add the parameters for the stored procedure here
	@NgayThucHien				DATETIME,
	@HopDongId					INT,
	@PhanBoId					INT,
	@SanPhamId					INT,
	@TenSanPham					NVARCHAR(50),
	@WebsiteId					INT,
	@TenWebsite					nvarchar(50),
	@DonViTinh					NVARCHAR(50),
	@SoLuongThayDoiThucChay		FLOAT,
	@GiaTriThayDoiThucChay		FLOAT,
	@SoLuongThayDoiKhuyenMai	FLOAT,
	@GiaTriThayDoiKhuyenMai		FLOAT
AS
BEGIN
	INSERT INTO ThucChayDaTinh
	SELECT DISTINCT
		NEWID() ThucChayDaTinhID,
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
		@PhanBoId AS HopDongChiTietREF,
		--Thong tin ve trang thai
		D.DangSuDung, D.IsGiayPhep, 
		2 AS TrangThaiHopDong,
		D.IsBanCung, 
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
		C.DanhSachNhanHangREF AS  NhanHang, 
		C.DmNhomNganhREF AS DmNhomNganhREF, 
		C.TenNhomNganh AS  TenNhomNganh, 
		--Thong tin hinh thuc quang cao
		C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
		--Thong tin San pham
		@SanPhamId as DmSanPhamREF,
		C.TenSanPham as TenSanPham,  
		0 DmNhomWebsiteREF, 
		'' TenNhomWebsite, 
		--C.DmWebsiteREF, 
		--C.TenWebsite, 
		C.DmChuyenMucREF AS DmChuyenMucREF, 
		C.TenChuyenMuc AS TenChuyenMuc, 
		C.DmLoaiBannerREF AS DmLoaiBannerREF, 
		C.TenLoaiBanner AS TenLoaiBanner, 
		C.DmViTriREF AS DmViTriREF, 
		C.TenViTri AS TenViTri, 
		N'UPDATE_GTTD' DotChayHopDong,
		0 AS SoLuongDotChayHD,
		'' DotChayBooking,
		0 SoLuongDotChayBooking, 
		--Thong tin ve Tien
		--****haidh chinh sua
		--C.SoLuong*1000 AS SoLuong,
		C.SoLuong AS SoLuong,
		--****haidh chinh sua
		@DonViTinh DonViTinh, 
		--dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,C.HopDongChiTietID,C.DonGia) as DonGia,
		C.DonGia AS DonGia,
		--****haidh chinh sua 
		0 AS DonGiaTheoDonViTinh,
		C.ChietKhau ChietKhau, C.GiamGia GiamGia, C.ThanhTien ThanhTien,
		C.TiLeTuVan TiLeTuVan,  C.ChiPhiTuVan ChiPhiTuVan,
		C.IsKhuyenMai IsKhuyenMai,  
		C.KhuyenMai KhuyenMai,
		--Thuc chay
		0 DmBannerREF,--A.DmBannerREF,
		0 DmChienDichREF,--A.DmChienDichREF,
		@WebsiteId AS DmWebsiteREF,
		@TenWebsite AS TenWebsite,
		0 TongViewThucChay,
		0 TongClickThucChay,
		0 TongSoBaiViet,
		@SoLuongThayDoiThucChay as SoLuongThucChay,
		--Thanhuc Tien Thuc Chay
		@NgayThucHien NgayThucHien,
		@GiaTriThayDoiThucChay as GiaTriThayDoi,
		0 as ThanhTienThucChayTruocTrietKhau,
		0 GiaTriTrietKhauThucChay,
		0 ThanhTienSauTrietKhauThucChay,
		0 AS GiaTriHoaHongThucChay,
		0 AS ThanhTienThucThu,
		0 as ThanhTienKM,
		0 as SoLuongThucChayKM,
		0 AS SoLuongLechTreoHa,
		0 AS ThanhTienLechTreoHa,
		GETDATE(),
		GETDATE(),
		0 IsPheDuyet,
		'' PheDuyetBy,
		'' PheDuyetAt,
		0 as SoLuongThayDoi,
		0 as SoLuongKMThayDoi,
		0 as GiaTriKMThayDoi,
		'' as GhiChu
	FROM
		HopDong AS D INNER JOIN HopDongChiTiet C ON C.HopDongFK = D.HopDongID
	WHERE 1 = 1
		AND C.HopDongChiTietID = @PhanBoId
		AND D.HopDongID = @HopDongId
END

```
