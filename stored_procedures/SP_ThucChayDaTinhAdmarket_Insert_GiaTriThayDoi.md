# Stored Procedure: `ThucChayDaTinhAdmarket_Insert_GiaTriThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-10 16:07:03.210000
- **Ngày sửa cuối**: 2016-10-20 10:51:38.423000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongId` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@PhanBoId` | `int(4)` | No |
| `@SanPhamId` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(100)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@SoLuongThayDoiThucChay` | `bigint(8)` | No |
| `@ThanhTienThayDoiThucChay` | `float(8)` | No |
| `@SoLuongThayDoiKhuyenMai` | `bigint(8)` | No |
| `@ThanhTienThayDoiKhuyenMai` | `float(8)` | No |
| `@GhiChu` | `nvarchar(510)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@TenViTri` | `nvarchar(100)` | No |
| `@NhanHang` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-08-28
-- Description:	Insert gia tri thay doi cho san pham Admarket
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinhAdmarket_Insert_GiaTriThayDoi]
	-- Add the parameters for the stored procedure here
	@NgayThucHien				DATETIME,
	@HopDongId					INT,
	@SoHopDong					NVARCHAR(50),
	@PhanBoId					INT,
	@SanPhamId					INT,
	@TenSanPham					NVARCHAR(50),
	@DonViTinh					NVARCHAR(50),
	@SoLuongThayDoiThucChay		BIGINT,
	@ThanhTienThayDoiThucChay	FLOAT,
	@SoLuongThayDoiKhuyenMai	BIGINT,
	@ThanhTienThayDoiKhuyenMai	FLOAT,
	@GhiChu						NVARCHAR(255),
	@DmViTriREF					INT,
	@TenViTri					NVARCHAR(50),	
	@NhanHang					NVARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
	INSERT INTO ThucChayDaTinhAdmarket
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
		@NhanHang NhanHang, 
		'' DmNhomNganhREF, 
		'' TenNhomNganh, 
		--Thong tin hinh thuc quang cao
		C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
		--Thong tin San pham
		@SanPhamId as DmSanPhamREF,
		@TenSanPham as TenSanPham,  
		0 DmNhomWebsiteREF, 
		'' TenNhomWebsite, 
		--C.DmWebsiteREF, 
		--C.TenWebsite, 
		C.DmChuyenMucREF AS DmChuyenMucREF, 
		C.TenChuyenMuc AS TenChuyenMuc, 
		C.DmLoaiBannerREF AS DmLoaiBannerREF, 
		C.TenLoaiBanner AS TenLoaiBanner, 
		@DmViTriREF AS DmViTriREF, 
		@TenViTri AS TenViTri, 
		@GhiChu AS DotChayHopDong,
		0 AS SoLuongDotChayHD,
		'' DotChayBooking,
		0 SoLuongDotChayBooking, 
		--Thong tin ve Tien
		--****haidh chinh sua
		CASE C.DmSanPhamREF
			WHEN 337 THEN C.Soluong*1000
			ELSE C.SoLuong
		END AS SoLuong,
		--****haidh chinh sua
		@DonViTinh AS DonViTinh, 
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
		0 DmWebsiteREF,
		'' AS TenWebsite,
		0 TongViewThucChay,
		0 TongClickThucChay,
		0 TongSoBaiViet,
		0 as SoLuongThucChay,
		--Thanhuc Tien Thuc Chay
		@NgayThucHien NgayThucHien,
		@ThanhTienThayDoiThucChay as GiaTriThayDoi,
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
		@SoLuongThayDoiThucChay as SoLuongThayDoi,
		0 as SoLuongKMThayDoi,
		0 as GiaTriKMThayDoi,
		@GhiChu as GhiChu
	FROM
		HopDong AS D INNER JOIN HopDongChiTiet C ON C.HopDongFK = D.HopDongID
	WHERE 1=1
		AND C.HopDongChiTietID = @PhanBoId
		AND D.HopDongID = @HopDongId
END


/****** Object:  StoredProcedure [dbo].[ThucChayDaTinhBoxAppSSV_InsertByPhanBoID]    Script Date: 9/9/2014 4:30:35 PM ******/
SET ANSI_NULLS ON

```
