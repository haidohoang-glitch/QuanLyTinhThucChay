# Stored Procedure: `ThucChayDaTinh_GG_FB_InsertGiaTriThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-08 10:00:25.503000
- **Ngày sửa cuối**: 2016-10-24 15:59:09.033000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@PhanBoID` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(100)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(100)` | No |
| `@TongViewThucChay` | `int(4)` | No |
| `@TongClickThucChay` | `int(4)` | No |
| `@SoLuongThucChay` | `int(4)` | No |
| `@ThanhTienThucChay` | `float(8)` | No |
| `@SoLuongThucChayKM` | `int(4)` | No |
| `@ThanhTienThucChayKM` | `float(8)` | No |
| `@DonViTinhSanPham` | `nvarchar(100)` | No |
| `@GhiChu` | `nvarchar(510)` | No |
| `@type` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2015-03-19
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinh_GG_FB_InsertGiaTriThayDoi]
	-- Add the parameters for the stored procedure here
(	
	@NgayThucHien			DATETIME,
	@SoHopDong				NVARCHAR(50),
	@PhanBoID				INT,
	@DmSanPhamREF			INT,
	@TenSanPham				NVARCHAR(50),
	@DmWebsiteREF			INT,
	@TenWebsite				NVARCHAR(50),
	@TongViewThucChay		INT,
	@TongClickThucChay		INT,
	@SoLuongThucChay		INT,
	@ThanhTienThucChay		FLOAT,
	@SoLuongThucChayKM		INT,
	@ThanhTienThucChayKM	FLOAT,
	@DonViTinhSanPham		NVARCHAR(50),
	@GhiChu					NVARCHAR(255),
	@type					NVARCHAR(50)
)
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
		C.HopDongChiTietID AS HopDongChiTietREF,
		--Thong tin ve trang thai
		D.DangSuDung AS DangSuDung, D.IsGiayPhep, D.TrangThaiHopDong,D.IsBanCung, 
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
		ISNULL(C.DanhSachNhanHangREF,'') NhanHang, 
		C.DmNhomNganhREF DmNhomNganhREF, 
		C.TenNhomNganh TenNhomNganh, 
		--Thong tin hinh thuc quang cao
		C.DmLoaiREF AS DmHinhThucQuangCao, 
		C.TenLoai AS TenHinhThucQuangCao, 
		--Thong tin San pham
		@DmSanPhamREF as DmSanPhamREF,
		@TenSanPham as TenSanPham,  
		C.DmNhomWebsiteREF DmNhomWebsiteREF, 
		C.TenNhomWebsite TenNhomWebsite, 
		--C.DmWebsiteREF, 
		--C.TenWebsite, 
		C.DmChuyenMucREF DmChuyenMucREF, 
		C.TenChuyenMuc TenChuyenMuc, 
		C.DmLoaiBannerREF DmLoaiBannerREF, 
		C.TenLoaiBanner TenLoaiBanner, 
		C.DmViTriREF DmViTriREF, 
		C.TenViTri TenViTri, 
		--ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,'Y'),'') DotChayHopDong,
		@type DotChayHopDong,
		C.SoLuong AS SoLuongDotChayHD,
		ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,'N'),0) DotChayBooking,
		dbo.GetSoLuongDotChayBookingByHopDongChiTiet(C.HopDongChiTietID) SoLuongDotChayBooking, 
		--Thong tin ve Tien
		--****haidh chinh sua
		dbo.ThucChay_GetQuantityThucChay(C.DmSanPhamREF,C.SoLuong, C.DonViTinh) AS SoLuong,
		--****haidh chinh sua
		@DonViTinhSanPham DonViTinh, 
		--dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,C.HopDongChiTietID,C.DonGia) as DonGia,
		dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,@PhanBoId,C.DonGia) AS DonGia,
		--****haidh chinh sua 
		ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong, @NgayThucHien, C.HopDongChiTietID),0),
		C.ChietKhau, C.GiamGia, C.ThanhTien,
		C.TiLeTuVan,  C.ChiPhiTuVan,
		C.IsKhuyenMai,  
		C.KhuyenMai,
		--Thuc chay
		0 DmBannerREF,--A.DmBannerREF,
		0 DmChienDichREF,--A.DmChienDichREF,
		@DmWebsiteREF DmWebsiteREF,
		@TenWebsite AS TenWebsite,
		0 TongViewThucChay,
		0 TongClickThucChay,
		0 TongSoBaiViet,
		0 as SoLuongThucChay,
		--Thanhuc Tien Thuc Chay
		@NgayThucHien NgayThucHien,
		@ThanhTienThucChay as GiaTriThayDoi,
		0 as ThanhTienThucChayTruocTrietKhau,
		0 GiaTriTrietKhauThucChay,
		0 ThanhTienSauTrietKhauThucChay,
		0 AS GiaTriHoaHongThucChay,
		@ThanhTienThucChay AS ThanhTienThucThu,
		@ThanhTienThucChayKM as ThanhTienKM,
		@SoLuongThucChayKM as SoLuongThucChayKM,
		0 AS SoLuongLechTreoHa,
		0 AS ThanhTienLechTreoHa,
		GETDATE(),
		GETDATE(),
		0 IsPheDuyet,
		'' PheDuyetBy,
		'' PheDuyetAt,
		@SoLuongThucChay as SoLuongThayDoi,
		0 as SoLuongKMThayDoi,
		0 as GiaTriKMThayDoi,
		@GhiChu as GhiChu
	FROM
		HopDong AS D 
			INNER JOIN HopDongChiTiet C ON C.HopDongFK = D.HopDongID
	WHERE 1=1
		--AND D.TrangThaiHopDong <> 3
		AND C.HopDongChiTietID = @PhanBoID
		AND D.SoHopDong = @SoHopDong
	
	SELECT 1
END

```
