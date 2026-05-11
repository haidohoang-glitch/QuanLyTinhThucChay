# Stored Procedure: `ThucChayDaTinhMuaNgoai_InsertByPhanBoId_test`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-11-08 15:55:50.070000
- **Ngày sửa cuối**: 2017-11-08 15:55:50.070000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ngayThucHien` | `datetime(8)` | No |
| `@phanBoId` | `int(4)` | No |
| `@soLuongThucChay` | `int(4)` | No |
| `@thanhTienThucChayMuaNgoaiTruocCK` | `float(8)` | No |
| `@thanhTienThucChay` | `float(8)` | No |
| `@soLuongThayDoi` | `int(4)` | No |
| `@giaTriThayDoi` | `float(8)` | No |
| `@soLuongKhuyenMai` | `int(4)` | No |
| `@thanhTienKhuyenMai` | `float(8)` | No |
| `@soLuongKMThayDoi` | `int(4)` | No |
| `@giaTriKMThayDoi` | `float(8)` | No |
| `@donViTinhThucChay` | `nvarchar(100)` | No |
| `@ghiChu` | `nvarchar(1024)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMW
-- Create date: 2015-01-12
-- Description:	Insert Thuc chay da tinh mua ngoai by phanBoId
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinhMuaNgoai_InsertByPhanBoId_test]
	-- Add the parameters for the stored procedure here
	@ngayThucHien						DATETIME,
	@phanBoId							INT,
	@soLuongThucChay					INT,
	--@chietKhauMuaNgoai					INT,
	@thanhTienThucChayMuaNgoaiTruocCK	FLOAT,
	@thanhTienThucChay					FLOAT,
	@soLuongThayDoi						INT,
	@giaTriThayDoi						FLOAT,
	@soLuongKhuyenMai					INT,
	@thanhTienKhuyenMai					FLOAT,
	@soLuongKMThayDoi					INT,
	@giaTriKMThayDoi					FLOAT,
	@donViTinhThucChay					NVARCHAR(50),
	@ghiChu								NVARCHAR(512)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    
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
		C.DanhSachNhanHangREF NhanHang, 
		'' DmNhomNganhREF, 
		'' TenNhomNganh, 
		--Thong tin hinh thuc quang cao
		C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
		--Thong tin San pham
		C.DmSanPhamREF,
		C.TenSanPham,  
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
		@GhiChu AS DotChayHopDong,
		0 AS SoLuongDotChayHD,
		'' DotChayBooking,
		0 SoLuongDotChayBooking, 
		--Thong tin ve Tien
		--****haidh chinh sua
		ISNULL(dbo.ThucChayMuaNgoai_GetSoLuongByDonViTinh(C.SoLuong,C.DonViTinh),0) AS SoLuong,
		--****haidh chinh sua
		@donViTinhThucChay AS DonViTinh, 
		dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,C.HopDongChiTietID,C.DonGia) as DonGia,		
		--****haidh chinh sua
		CASE WHEN dbo.ThucChayMuaNgoai_GetSoLuongByDonViTinh(C.SoLuong,C.DonViTinh) > 0 THEN  
					(C.ThanhTien/dbo.ThucChayMuaNgoai_GetSoLuongByDonViTinh(C.SoLuong,C.DonViTinh))
			 ELSE 0
		END AS DonGiaTheoDonViTinh,
		C.ChietKhau ChietKhau, C.GiamGia GiamGia, C.ThanhTien ThanhTien,
		C.TiLeTuVan TiLeTuVan,  C.ChiPhiTuVan ChiPhiTuVan,
		C.IsKhuyenMai IsKhuyenMai,  
		C.KhuyenMai KhuyenMai,
		--Thuc chay
		0 DmBannerREF,--A.DmBannerREF,
		0 DmChienDichREF,--A.DmChienDichREF,
		dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(C.DmWebsiteREF) DmWebsiteREF,
		dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF,C.TenWebsite) TenWebsite,
		0 TongViewThucChay,
		0 TongClickThucChay,
		0 TongSoBaiViet,
		@soLuongThucChay as SoLuongThucChay,
		--Thanhuc Tien Thuc Chay
		@ngayThucHien NgayThucHien,
		@giaTriThayDoi as GiaTriThayDoi,
		--@chietKhauMuaNgoai as ChietKhauMuaNgoai,
		@thanhTienThucChayMuaNgoaiTruocCK as ThanhTienThucChayTruocTrietKhau,
		(@thanhTienThucChayMuaNgoaiTruocCK - @thanhTienThucChay) GiaTriTrietKhauThucChay,
		@thanhTienThucChay ThanhTienSauTrietKhauThucChay,
		0 AS GiaTriHoaHongThucChay,
		@thanhTienThucChay AS ThanhTienThucThu,
		@thanhTienKhuyenMai as ThanhTienKM,
		@soLuongKhuyenMai as SoLuongThucChayKM,
		0 AS SoLuongLechTreoHa,
		0 AS ThanhTienLechTreoHa,
		GETDATE() AS CreatedAt,
		GETDATE() AS LastModifiedAt,
		0 IsPheDuyet,
		'' PheDuyetBy,
		'' PheDuyetAt,
		@soLuongThayDoi as SoLuongThayDoi,
		@soLuongKMThayDoi as SoLuongKMThayDoi,
		@giaTriKMThayDoi as GiaTriKMThayDoi,
		@GhiChu as GhiChu
	FROM
		HopDong AS D INNER JOIN HopDongChiTiet C ON C.HopDongFK = D.HopDongID
	WHERE 1=1
		AND C.HopDongChiTietID = @PhanBoId
END

```
