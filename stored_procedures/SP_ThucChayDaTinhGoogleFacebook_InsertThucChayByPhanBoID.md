# Stored Procedure: `ThucChayDaTinhGoogleFacebook_InsertThucChayByPhanBoID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-08 10:00:24.687000
- **Ngày sửa cuối**: 2015-04-08 10:00:24.687000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@PhanBoID` | `int(4)` | No |
| `@SanPhamID` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(100)` | No |
| `@ThanhTienThucChay` | `float(8)` | No |
| `@GiaTriThayDoi` | `float(8)` | No |
| `@GhiChu` | `nvarchar(510)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-10-13
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinhGoogleFacebook_InsertThucChayByPhanBoID]
	-- Add the parameters for the stored procedure here
	@NgayThucHien		DATETIME,
	@PhanBoID			INT,
	@SanPhamID			INT,
	@TenSanPham			NVARCHAR(50),
	@ThanhTienThucChay	FLOAT,
	@GiaTriThayDoi		FLOAT,
	@GhiChu				NVARCHAR(255)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
    INSERT INTO ThucChayDaTinh
	SELECT  NEWID(), TD.*, 
		 0 GiaTriTrietKhauThucChay,
		 0 AS ThanhTienSauTrietKhauThucChay,
		 0 AS GiaTriHoaHongThucChay,
		 0 AS ThanhTienThucThu,
		 0 as ThanhTienKM,
		 0 as SoLuongThucChayKM,
		 0 SoLuongLechTreoHa,
		 0 AS ThanhTienLechTreoHa,
		 GETDATE(),
		 GETDATE(),
		 0 IsPheDuyet,
		 '' PheDuyetBy,
		 '' PheDuyetAt,
		 0,0,0,@GhiChu
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
		 @TenSanPham AS TenSanPham,  
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
		 @GhiChu DotChayHopDong,
		 0 AS SoLuongDotChayHD,
		 '' DotChayBooking,
		 0 AS SoLuongDotChayBooking, 
		 --Thong tin ve Tien
		 ISNULL(dbo.ThucChay_GetSoLuongChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,c.HopDongChiTietID),0) AS SoLuong, 
		 C.DonViTinh AS  DonViTinh, 
		 0 as DonGia, 
		 --ISNULL(dbo.ThucChay_GetDonGiaThucTreo_PR(D.NgayKyHopDong, '2014-05-14', C.HopDongChiTietID),0) AS DonGiaTheoDonViTinh,
		 0 AS DonGiaTheoDonViTinh,
		 C.ChietKhau, C.GiamGia, C.ThanhTien,
		 C.TiLeTuVan,  C.ChiPhiTuVan,
		 C.IsKhuyenMai,  
		 C.KhuyenMai,
		 --Thuc chay
		 0 DmBannerREF,--A.DmBannerREF,
		 0 DmChienDichREF,--A.DmChienDichREF,
		 dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(C.DmWebsiteREF) DmWebsiteREF,
		 dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF,C.TenWebsite) TenWebsite,
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
		  WHERE 1=1-- DmSanPhamREF in (141)
		  AND HopDongChiTietID = @PhanBoId
		  --AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](DonViTinhREF, DonViTinh) = 1 --Đơn vị của hình thức CPD 
		 ) C  
		 INNER JOIN HopDong AS D ON D.HopDongID = C.HopDongFK AND D.TrangThaiHopDong <> 3
	 ) TD
END

```
