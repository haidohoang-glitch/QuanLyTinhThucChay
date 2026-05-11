# Stored Procedure: `ThucChayDaTinhBoxAppSSV_InsertBySanPhamWebsite`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-24 11:41:13.433000
- **Ngày sửa cuối**: 2014-10-14 10:39:49.193000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
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

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-06-24
-- Description:	Insert Thuc chay da tinh Boxapp SSV theo website, san pham
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinhBoxAppSSV_InsertBySanPhamWebsite]
	-- Add the parameters for the stored procedure here
	@NgayThucHien			DATETIME,
	@SoHopDong				NVARCHAR(50),
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
	@TypeInsert				INT -- 1: ThucChay; 2: KhuyenMai; 3 LechTreoHa
AS
BEGIN
	DECLARE @TypeDonViTinh		INT = 0 -- 1: CPC/CPM; 0: Goi

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
		0 AS HopDongChiTietREF,
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
		'' NhanHang, 
		'' DmNhomNganhREF, 
		'' TenNhomNganh, 
		--Thong tin hinh thuc quang cao
		26 AS DmHinhThucQuangCao, 'Self-serving' AS TenHinhThucQuangCao, 
		--Thong tin San pham
		@DmSanPhamREF as DmSanPhamREF,
		@TenSanPham as TenSanPham,  
		0 DmNhomWebsiteREF, 
		'' TenNhomWebsite, 
		--C.DmWebsiteREF, 
		--C.TenWebsite, 
		0 DmChuyenMucREF, 
		'' TenChuyenMuc, 
		0 DmLoaiBannerREF, 
		'' TenLoaiBanner, 
		0 DmViTriREF, 
		'' TenViTri, 
		'' DotChayHopDong,
		0 AS SoLuongDotChayHD,
		'' DotChayBooking,
		0 SoLuongDotChayBooking, 
		--Thong tin ve Tien
		--****haidh chinh sua
		0 AS SoLuong,
		--****haidh chinh sua
		'VIEW' DonViTinh, 
		--dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,C.HopDongChiTietID,C.DonGia) as DonGia,
		0 AS DonGia,
		--****haidh chinh sua 
		0 AS DonGiaTheoDonViTinh,
		0 ChietKhau, 0 GiamGia, 0 ThanhTien,
		0 TiLeTuVan,  0 ChiPhiTuVan,
		0 IsKhuyenMai,  
		'' KhuyenMai,
		--Thuc chay
		0 DmBannerREF,--A.DmBannerREF,
		0 DmChienDichREF,--A.DmChienDichREF,
		@DmWebsiteREF DmWebsiteREF,
		@TenWebsite AS TenWebsite,
		@TongViewThucChay TongViewThucChay,
		@TongClickThucChay TongClickThucChay,
		0 TongSoBaiViet,
		@SoLuongThucChay as SoLuongThucChay,
		--Thanhuc Tien Thuc Chay
		@NgayThucHien NgayThucHien,
		0 as GiaTriThayDoi,
		0 as ThanhTienThucChayTruocTrietKhau,
		0 GiaTriTrietKhauThucChay,
		@ThanhTienThucChay ThanhTienSauTrietKhauThucChay,
		0 AS GiaTriHoaHongThucChay,
		@ThanhTienThucChay AS ThanhTienThucThu,
		@ThanhTienThucChayKM as ThanhTienKM,
		@SoLuongThucChayKM as SoLuongThucChayKM,
		@SoLuongLechTreoHa AS SoLuongLechTreoHa,
		@ThanhTienLechTreoHa AS ThanhTienLechTreoHa,
		GETDATE(),
		GETDATE(),
		0 IsPheDuyet,
		'' PheDuyetBy,
		'' PheDuyetAt 
	FROM
		HopDong AS D 
	WHERE D.TrangThaiHopDong <> 3
		AND D.SoHopDong = @SoHopDong
END

```
