# Stored Procedure: `InsertOrUpdateAdXAdmarketForDomain`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-27 08:25:24.390000
- **Ngày sửa cuối**: 2015-02-03 19:25:34.360000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@siteid` | `int(4)` | No |
| `@domain` | `nvarchar(200)` | No |
| `@ttc` | `int(4)` | No |
| `@ttv` | `int(4)` | No |
| `@money` | `float(8)` | No |
| `@promotion` | `float(8)` | No |
| `@TenSanpham` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@type` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@TenViTri` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[InsertOrUpdateAdXAdmarketForDomain] (
    @NgayThucHien	DATETIME,
    @siteid			INT,
    @domain			NVARCHAR(100),
    @ttc			INT,
    @ttv			INT,
    @money			FLOAT,
    @promotion		FLOAT,
    @TenSanpham		NVARCHAR(50),
    @DmSanPhamREF	INT,
    @type			INT, -- 0: Thuc chay khach hang; 1: Thuc chay noi bo; -1: all
    @DonViTinh		nvarchar(50), --CPC hoac View
    @DmViTriREF     INT,
    @TenViTri       nvarchar(50)
)
AS
BEGIN
	DECLARE @ThucChayDaTinhID INT
	SET @ThucChayDaTinhID = 0
	DECLARE @TenSanphamWell NVARCHAR(50)
	SET @TenSanphamWell = @TenSanpham
	DECLARE @DmSanPhamREFWell INT
	SET @DmSanPhamREFWell = @DmSanPhamREF

	Declare @SoLuong int 
	if(@DonViTinh = 'CPC') 
		set @SoLuong = @ttc
	else
		set @SoLuong = @ttv
	
	    
	DECLARE @DmHinhThucQuangCao INT, @TenHinhThucQuangCao NVARCHAR(50)
	DECLARE @DmMaHopDongREF	INT = 0,
			@TenMaHopDong	NVARCHAR(50) = ''
	

	SET @DmHinhThucQuangCao = 26
	SET @TenHinhThucQuangCao = 'Self-serving'

	
	--Truoc Thue
	SET @money = ROUND(@money / 1.1, 0)
	set @promotion = ROUND(@promotion / 1.1, 0)	
		
	-- Noi bo
	IF @type = 1
	BEGIN
		SET @DmMaHopDongREF = 310;
		SET @TenMaHopDong	= 'NB';
		--set @money = @promotion
		--set @promotion = 0
	END
		
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

		INSERT INTO dbo.ThucChayDaTinhAdXForDomain
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
			CreatedAt,
			LastModifiedAt
		  )
		VALUES
		  (
			NEWID(),	-- ThucChayDaTinhID - nvarchar(50)
			0,	-- HopDongID - int
			N'-',	-- SoHopDong - nvarchar(50)
			@DmMaHopDongREF,	-- DmMaHopDongREF - int
			@TenMaHopDong,	-- TenMaHopDong - nvarchar(50)
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
			@DmSanPhamREF,	-- DangSuDung - int
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
			@DmHinhThucQuangCao,	-- DmHinhThucQuangCao - int
			@TenHinhThucQuangCao,	-- TenHinhThucQuangCao - nvarchar(50)
			@DmSanPhamREFWell,	-- DmSanPhamREF - int
			@TenSanphamWell,	-- TenSanPham - nvarchar(100)
			0,	-- DmNhomWebsiteREF - int
			N'',	-- TenNhomWebsite - nvarchar(100)
			0,	-- DmChuyenMucREF - int
			N'',	-- TenChuyenMuc - nvarchar(100)
			0,	-- DmLoaiBannerREF - int
			N'',	-- TenLoaiBanner - nvarchar(50)
			@DmViTriREF,	-- DmViTriREF - int
			@TenViTri,	-- TenViTri - nvarchar(50)
			N'',	-- DotChayHopDong - nvarchar(1000)
			0,	-- SoLuongDotChayHD - int
			N'',	-- DotChayBooking - nvarchar(1000)
			0,	-- SoLuong - int
			@DonViTinh,	-- DonViTinh - nvarchar(50)
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
			@SoLuong,	-- SoLuongThucChay - float
			@NgayThucHien,	-- NgayThucHien - datetime
			0.0,	-- GiaTriThayDoi - float
			0.0,	-- ThanhTienThucChayTruocTrietKhau - float
			0.0,	-- GiaTriTrietKhauThucChay - float
			@money,	-- ThanhTienSauTrietKhauThucChay - float
			0.0,	-- GiaTriHoaHongThucChay - float
			0.0,	-- ThanhTienThucThu - float
			@promotion,
			GETDATE(),
			GETDATE()
		  )

END

--select * from ThucChayDaTinhAdXForDomain

```
