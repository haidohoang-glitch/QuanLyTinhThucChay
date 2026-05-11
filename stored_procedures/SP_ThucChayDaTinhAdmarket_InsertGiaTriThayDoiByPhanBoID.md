# Stored Procedure: `ThucChayDaTinhAdmarket_InsertGiaTriThayDoiByPhanBoID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-11-08 11:31:14.863000
- **Ngày sửa cuối**: 2015-12-28 15:40:22.153000

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
| `@SoLuongLechTreoHa` | `int(4)` | No |
| `@ThanhTienLechTreoHa` | `float(8)` | No |
| `@TypeInsert` | `int(4)` | No |
| `@DonViTinhSanPham` | `nvarchar(100)` | No |
| `@GhiChu` | `nvarchar(510)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@TenViTri` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-06-24
-- Description:	Insert Thuc chay da tinh Boxapp SSV theo website, san pham
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinhAdmarket_InsertGiaTriThayDoiByPhanBoID]
	-- Add the parameters for the stored procedure here
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
	@SoLuongLechTreoHa		INT,
	@ThanhTienLechTreoHa	FLOAT,
	@TypeInsert				INT, -- 1: ThucChay; 2: KhuyenMai; 3 LechTreoHa
	@DonViTinhSanPham		NVARCHAR(50),
	@GhiChu					NVARCHAR(255),
	@DmViTriREF				INT,
	@TenViTri				NVARCHAR(50)
AS
BEGIN
	DECLARE @TypeDonViTinh		INT = 0 -- 1: CPC/CPM; 0: Goi
	PRINT 'PhanBoID: ' + CONVERT(NVARCHAR(50),@PhanBoID);
	
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
		C.HopDongChiTietID AS HopDongChiTietREF,
		--Thong tin ve trang thai
		CASE @DmSanPhamREF
			WHEN 144 THEN 5001
			WHEN 299 THEN 5002
			WHEN 337 THEN 5003
			ELSE 0 -- AdX
		END AS DangSuDung, D.IsGiayPhep, D.TrangThaiHopDong,D.IsBanCung, 
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
		C.NhanHang NhanHang, 
		'' DmNhomNganhREF, 
		'' TenNhomNganh, 
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
		@DmViTriREF DmViTriREF, 
		@TenViTri TenViTri, 
		@GhiChu DotChayHopDong,
		C.SoLuong AS SoLuongDotChayHD,
		0 DotChayBooking,
		0 SoLuongDotChayBooking, 
		--Thong tin ve Tien
		--****haidh chinh sua
		C.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(C.DonViTinh) AS SoLuong,
		--****haidh chinh sua
		@DonViTinhSanPham DonViTinh, 
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
		@TongViewThucChay TongViewThucChay,
		@TongClickThucChay TongClickThucChay,
		0 TongSoBaiViet,
		0 as SoLuongThucChay,
		--Thanhuc Tien Thuc Chay
		@NgayThucHien NgayThucHien,
		@ThanhTienThucChay as GiaTriThayDoi,
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
		@SoLuongThucChay as SoLuongThayDoi,
		@SoLuongThucChayKM as SoLuongKMThayDoi,
		@ThanhTienThucChayKM as GiaTriKMThayDoi,
		@GhiChu as GhiChu
	FROM
		HopDong AS D 
			INNER JOIN HopDongChiTiet C ON C.HopDongFK = D.HopDongID
	WHERE D.TrangThaiHopDong <> 3
		AND C.HopDongChiTietID = @PhanBoID
		AND D.SoHopDong = @SoHopDong
END

SET ANSI_NULLS ON

```
