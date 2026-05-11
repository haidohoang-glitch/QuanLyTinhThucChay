# Stored Procedure: `ThucChayDaTinhGoogleFacebook_InsertThucChayChiPhiKhac`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-08 10:00:22.413000
- **Ngày sửa cuối**: 2015-04-08 10:00:22.413000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
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
-- Description:	Insert thuc chay cho san pham chi phi khac
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinhGoogleFacebook_InsertThucChayChiPhiKhac] 
	-- Add the parameters for the stored procedure here
	@NgayThucHien		DATETIME,
	@HopDongID			INT,
	@SoHopDong			NVARCHAR(50),
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
	SELECT 
		NEWID(),
    	@HopDongID AS HopDongID,
    	@SoHopDong AS SoHopDong,
    	DmMaHopDongREF,
    	TenMaHopDong,
    	NgayDanhSoHopDong,
    	NgayKyHopDong,
    	NhanHopDong,
    	NgayNhanBanFax,
    	NgayNhanHopDongBanCung,
    	NgayChuyenHopDongChoKeToan,
    	So,
    	Thang,
    	Nam,
    	GiaTriHopDong,
    	CongNo,
    	@PhanBoID AS HopDongChiTietREF,
    	DangSuDung,
    	IsGiayPhep,
    	TrangThaiHopDong,
    	IsBanCung,
    	DmPhongBanREF,
    	TenPhongBan,
    	DmBoPhanREF,
    	TenBoPhan,
    	DmNhomLamViecREF,
    	A.TenNhom,
    	DmDiaDiemLamViecREF,
    	TenDiaDiemLamViec,
    	SysNhanVienREF,
    	TenDangNhap,
    	TenNhanVien,
    	TenKhachHang,
    	NhanHopDong,
    	0 AS DmNhomNganhREF,
    	'' AS TenNhomNganh,
    	14 AS DmHinhThucQuangCao,
    	N'Chi phí khác' AS TenHinhThucQuangCao,
    	@SanPhamID AS DmSanPhamREF,
    	@TenSanPham AS TenSanPham,
    	0 AS DmNhomWebsiteREF,
    	'' AS TenNhomWebsite,
    	0 AS DmChuyenMucREF,
    	'' AS TenChuyenMuc,
    	0 AS DmLoaiBannerREF,
    	'' AS TenLoaiBanner,
    	0 AS DmViTriREF,
    	'' AS TenViTri,
    	@GhiChu AS DotChayHopDong,
    	0 AS SoLuongDotChayHD,
    	'' AS DotChayBooking,
    	0 AS SoLuongDotChayBooking,
    	1 AS SoLuong,
    	N'Gói' AS DonViTinh,
    	0 AS DonGia,
    	0 AS DonGiaTheoDonVi,
    	0 AS ChietKhau,
    	0 AS GiamGia,
    	0 AS ThanhTien,
    	0 AS TiLeTuVan,
    	0 AS ChiPhiTuVan,
    	0 AS IsKhuyenMai,
    	'' AS KhuyenMai,
    	0 AS DmBannerREF,
    	0 AS DmChienDichREF,
    	0 AS DmWebsiteREF,
    	'' AS TenWebsite,
    	0 AS TongViewThucChay,
    	0 AS TongClickThucChay,
    	0 AS TongSoBaiViet,
    	0 AS SoLuongThucChay,
    	@NgayThucHien AS NgayThucHien,
    	@GiaTriThayDoi AS GiaTriThayDoi,
    	0 AS ThanhTienThucChayTruocTrietKhau,
    	0 AS GiaTriTrietKhauThucChay,
    	@ThanhTienThucChay AS ThanhTienSauTrietKhauThucChay,
    	0 AS GiaTriHoaHongThucChay,
    	@ThanhTienThucCHay AS ThanhTienThucThu,
    	0 AS ThanhTienKM,
    	0 AS SoLuongThucChayKM,
    	0 AS SoLuongThucChayLechTreoHa,
    	0 AS ThanhTienLechTreoHa,
    	GETDATE() AS CreatedAt,
    	GETDATE() AS LastModifiedAt,
    	0 AS IsPheDuyet,
    	NULL PheDuyetBy,
    	NULL PheDuyetAt,
		0 as SoLuongThayDoi,
		0 as SoLuongKMThayDoi,
		0 as GiaTriKMThayDoi,
		@GhiChu as GhiChu
    FROM HopDong A
    WHERE 1 = 1
		AND A.HopDongID = @HopDongID
END

```
