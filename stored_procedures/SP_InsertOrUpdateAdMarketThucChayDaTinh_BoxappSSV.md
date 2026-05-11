# Stored Procedure: `InsertOrUpdateAdMarketThucChayDaTinh_BoxappSSV`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-07 16:05:26.980000
- **Ngày sửa cuối**: 2014-11-20 14:00:48.090000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@siteid` | `int(4)` | No |
| `@domain` | `nvarchar(200)` | No |
| `@ttc` | `int(4)` | No |
| `@ttv` | `int(4)` | No |
| `@money` | `float(8)` | No |
| `@tienkm` | `float(8)` | No |
| `@TenSanpham` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@contract` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[InsertOrUpdateAdMarketThucChayDaTinh_BoxappSSV] (
    @NgayThucHien  DATETIME,
    @siteid        INT,
    @domain        NVARCHAR(100),
    @ttc           INT,
    @ttv           INT,
    @money         FLOAT,
    @tienkm		   FLOAT,
    @TenSanpham    NVARCHAR(50),
    @DmSanPhamREF  INT,
	@contract	   NVARCHAR(50)
)
AS
BEGIN
	DECLARE @ThucChayDaTinhID INT
	SET @ThucChayDaTinhID = 0
	--Truoc Thue
	SET @money = ROUND(@money / 1.1, 2)
	
	--Check Website
	SET @siteid = dbo.GetWebsiteIDByDomainName(@domain)
	
	IF @siteid IS NULL
	BEGIN
	    INSERT INTO dbo.DmWebsiteReportingdb
	      (
	        TenWebsite,
	        CreatedBy,
	        CreatedAt,
	        LastModifiedBy,
	        LastModifiedAt,
	        DeletedStatus,
	        PrintStatus,
	        RecordStatus,
	        ID
	      )
	    VALUES
	      (
	        @domain,	-- TenWebsite - nvarchar(200)
	        N'asd',	-- CreatedBy - nvarchar(50)
	        GETDATE(),	-- CreatedAt - datetime
	        N'asd',	-- LastModifiedBy - nvarchar(50)
	        GETDATE(),	-- LastModifiedAt - datetime
	        0,	-- DeletedStatus - int
	        0,	-- PrintStatus - int
	        0,	-- RecordStatus - int
	        N'New' -- ID - nvarchar(50)
	      )		
	    SET @siteid = @@IDENTITY
	END	
	

	    INSERT INTO dbo.ThucChayDaTinhBoxAppSSV
	      (
	        ThucChayDaTinhID,
	        HopDongID,
	        SoHopDong,
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
	        HopDongChiTietREF,
	        DangSuDung,
	        IsGiayPhep,
	        TrangThaiHopDong,
	        IsBanCung,
	        DmPhongBanREF,
	        TenPhongBan,
	        DmBoPhanREF,
	        TenBoPhan,
	        DmNhomLamViecREF,
	        TenNhomLamViec,
	        DmDiaDiemLamViecREF,
	        TenDiaDiemLamViec,
	        SysNhanVienREF,
	        TenDangNhap,
	        TenNhanVien,
	        TenKhachHang,
	        NhanHang,
	        DmNhomNganhREF,
	        TenNhomNganh,
	        DmHinhThucQuangCao,
	        TenHinhThucQuangCao,
	        DmSanPhamREF,
	        TenSanPham,
	        DmNhomWebsiteREF,
	        TenNhomWebsite,
	        DmChuyenMucREF,
	        TenChuyenMuc,
	        DmLoaiBannerREF,
	        TenLoaiBanner,
	        DmViTriREF,
	        TenViTri,
	        DotChayHopDong,
	        SoLuongDotChayHD,
	        DotChayBooking,
	        SoLuong,
	        DonViTinh,
	        DonGia,
	        DonGiaTheoDonVi,
	        ChietKhau,
	        GiamGia,
	        ThanhTien,
	        TiLeTuVan,
	        ChiPhiTuVan,
	        IsKhuyenMai,
	        KhuyenMai,
	        DmBannerREF,
	        DmChienDichREF,
	        DmWebsiteREF,
	        TenWebsite,
	        TongViewThucChay,
	        TongClickThucChay,
	        TongSoBaiViet,
	        SoLuongThucChay,
	        NgayThucHien,
	        GiaTriThayDoi,
	        ThanhTienThucChayTruocTrietKhau,
	        GiaTriTrietKhauThucChay,
	        ThanhTienSauTrietKhauThucChay,
	        GiaTriHoaHongThucChay,
	        ThanhTienThucThu,
	        ThanhTienKM,
	        CreatedAt
	      )
	    VALUES
	      (
	        NEWID(),	-- ThucChayDaTinhID - nvarchar(50)
	        0,	-- HopDongID - int
	        @contract,	-- SoHopDong - nvarchar(50)
	        0,	-- DmMaHopDongREF - int
	        N'',	-- TenMaHopDong - nvarchar(50)
	        '2013-07-17 02:05:51',	-- NgayDanhSoHopDong - datetime
	        '2013-07-17 02:05:51',	-- NgayKyHopDong - datetime
	        N'',	-- NhanHopDong - nvarchar(50)
	        '2013-07-17 02:05:51',	-- NgayNhanBanFax - datetime
	        '2013-07-17 02:05:51',	-- NgayNhanHopDongBanCung - datetime
	        '2013-07-17 02:05:51',	-- NgayChuyenHopDongChoKeToan - datetime
	        N'',	-- So - nvarchar(50)
	        0,	-- Thang - int
	        0,	-- Nam - int
	        0.0,	-- GiaTriHopDong - float
	        0.0,	-- CongNo - float
	        0,	-- HopDongChiTietREF - int
	        5004,	-- DangSuDung - int
	        0,	-- IsGiayPhep - int
	        0,	-- TrangThaiHopDong - int
	        0,	-- IsBanCung - int
	        -1,	-- DmPhongBanREF - int
	        N'-',	-- TenPhongBan - nvarchar(50)
	        -1,	-- DmBoPhanREF - int
	        N'-',	-- TenBoPhan - nvarchar(50)
	        -1,	-- DmNhomLamViecREF - int
	        N'-',	-- TenNhomLamViec - nvarchar(50)
	        0,	-- DmDiaDiemLamViecREF - int
	        N'',	-- TenDiaDiemLamViec - nvarchar(50)
	        0,	-- SysNhanVienREF - int
	        N'-',	-- TenDangNhap - nvarchar(25)
	        N'-',	-- TenNhanVien - nvarchar(100)
	        N'',	-- TenKhachHang - nvarchar(255)
	        N'',	-- NhanHang - nvarchar(255)
	        0,	-- DmNhomNganhREF - int
	        N'',	-- TenNhomNganh - nvarchar(50)
	        26,	-- DmHinhThucQuangCao - int
	        N'Self-serving',	-- TenHinhThucQuangCao - nvarchar(50)
	        @DmSanPhamREF,	-- DmSanPhamREF - int
	        @TenSanPham,	-- TenSanPham - nvarchar(100)
	        0,	-- DmNhomWebsiteREF - int
	        N'',	-- TenNhomWebsite - nvarchar(100)
	        0,	-- DmChuyenMucREF - int
	        N'',	-- TenChuyenMuc - nvarchar(100)
	        0,	-- DmLoaiBannerREF - int
	        N'',	-- TenLoaiBanner - nvarchar(50)
	        0,	-- DmViTriREF - int
	        N'',	-- TenViTri - nvarchar(50)
	        N'',	-- DotChayHopDong - nvarchar(1000)
	        0,	-- SoLuongDotChayHD - int
	        N'',	-- DotChayBooking - nvarchar(1000)
	        0,	-- SoLuong - int
	        'View',	-- DonViTinh - nvarchar(50)
	        0.0,	-- DonGia - float
	        0.0,	-- DonGiaTheoDonVi - float
	        0.0,	-- ChietKhau - float
	        0.0,	-- GiamGia - float
	        0.0,	-- ThanhTien - float
	        0.0,	-- TiLeTuVan - float
	        0.0,	-- ChiPhiTuVan - float
	        0,	-- IsKhuyenMai - int
	        N'',	-- KhuyenMai - nvarchar(50)
	        0,	-- DmBannerREF - int
	        0,	-- DmChienDichREF - int
	        @siteid,	-- DmWebsiteREF - int
	        @domain,	-- TenWebsite - nvarchar(255)
	        @ttv,	-- TongViewThucChay - float
	        @ttc,	-- TongClickThucChay - float
	        0.0,	-- TongSoBaiViet - float
	        @ttv,	-- SoLuongThucChay - float
	        @NgayThucHien,	-- NgayThucHien - datetime
	        0.0,	-- GiaTriThayDoi - float
	        0.0,	-- ThanhTienThucChayTruocTrietKhau - float
	        0.0,	-- GiaTriTrietKhauThucChay - float
	        @money,	-- ThanhTienSauTrietKhauThucChay - float	        
	        0.0,	-- GiaTriHoaHongThucChay - float
	        0.0,	-- ThanhTienThucThu - float
	        @tienkm	, -- ThanhTienKM - float
	        GETDATE()
	      )

END

```
