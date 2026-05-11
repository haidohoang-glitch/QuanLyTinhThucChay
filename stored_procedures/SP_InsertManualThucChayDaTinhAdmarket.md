# Stored Procedure: `InsertManualThucChayDaTinhAdmarket`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-04 10:52:54.513000
- **Ngày sửa cuối**: 2018-05-24 11:10:16.820000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@GiaTriThayDoi` | `float(8)` | No |
| `@GiaTriKhuyenMai` | `float(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@ThanhTienSTCK` | `float(8)` | No |
| `@GhiChu` | `nvarchar(400)` | No |
| `@Tk` | `nvarchar(100)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@NhanHang` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[InsertManualThucChayDaTinhAdmarket]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME, 
	@SoHopDong NVARCHAR(50), 
	@HopDongChiTietID INT, 
	@GiaTriThayDoi FLOAT, 
	@GiaTriKhuyenMai FLOAT,
	@DmSanPhamREF INT, 
	@ThanhTienSTCK FLOAT,
	@GhiChu nvarchar(200),
	@Tk NVARCHAR(50), 
	@DmViTriREF int, 
	@NhanHang nvarchar(50)
AS
BEGIN
	DECLARE @DonViTinh NVARCHAR(50),@DmWebsiteREF INT, @TenWebsite NVARCHAR(50),@SoLuongThucChay INT,@TenViTri nvarchar(50),@SoLuongThayDoi INT
     SET @SoLuongThucChay =1
     SET @SoLuongThayDoi =0
	 IF @DmSanPhamREF = 144 set @TenViTri = 'CPC Admarket' else if  @DmSanPhamREF = 628 set @TenViTri = '' else if @DmViTriREF = 1  SET @TenViTri = 'ADX' ELSE IF @DmViTriREF = 2 SET @TenViTri = 'AdX Mobile' else  SET @TenViTri = 'AdX Ecommerce'
	 SET @DonViTinh = 'CPC'

	 ---------------------
	 INSERT INTO dbo.ThucChayDaTinhAdmarket
	SELECT  NEWID() thucchaydatinhid, TD.*, 
	ISNULL((TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100,0) AS GiaTriTrietKhauThucChay,
	ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) AS ThanhTienSauTrietKhauThucChay,	
	ISNULL(((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100,0) AS GiaTriHoaHongThucChay,
	ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100 - ((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0) AS ThanhTienThucThu,
	--(CASE when ((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) then TD.ThanhTienThucChayTruocTrietKhau
	--	else 0
	--  END
	--) AS
	@GiaTriKhuyenMai ThanhTienKM,
	0 as SoLuongThucChayKM,
	0 SoLuongLechTreoHa,
	0 ThanhTienLechTreoHa,
	GETDATE() createdat,
	GETDATE() lastmodifiedat,
	0 IsPheDuyet,
	'' PheDuyetBy,
	'' PheDuyetAt,
	@SoLuongThayDoi SoLuongThayDoi,
	0 SoLuongKMThayDoi,
	0 GiaTriKMThayDoi,
    @GhiChu GhiChu	
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
	D.NhanHopDong, D.NgayNhanBanFax, D.NgayNhanHopDongBanCung, D.NgayChuyenHopDongChoKeToan, 
	D.So, D.Thang, D.Nam, 
	--Thong tin ve gia tri
	D.GiaTriHopDong, D.CongNo,
	--Thong tin chi tiet phan bo
	C.HopDongChiTietID,
	--Thong tin ve trang thai
	D.DangSuDung, D.IsGiayPhep, 2 TrangThaiHopDong,D.IsBanCung, 
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
	C.DmNhomNganhREF, 
	C.TenNhomNganh, 
	--Thong tin hinh thuc quang cao
	C.DmLoaiREF AS DmHinhThucQuangCao, C.TenLoai AS TenHinhThucQuangCao, 
	--Thong tin San pham
	c.DmSanPhamREF as DmSanPhamREF,
	E.TenSanPham,  
	C.DmNhomWebsiteREF, 
	C.TenNhomWebsite, 
	--C.DmWebsiteREF, 
	--C.TenWebsite, 
	C.DmChuyenMucREF, 
	C.TenChuyenMuc,
	C.DmLoaiBannerREF, 
	C.TenLoaiBanner, 
	@DmViTriREF DmViTriREF, 
	@TenViTri TenViTri, 
	'' DotChayHopDong,
	0 AS SoLuongDotChayHD,
	--'' DotChayBooking,
	dbo.ThucChay_GetListThucTreoIDByHopDongChiTietREF(@NgayThucHien,'2013-01-01',c.HopDongChiTietID) DotChayBooking,
	0 AS SoLuongDotChayBooking, 
	--Thong tin ve Tien
	C.SoLuong AS SoLuong, 
	--isnull(C.DonViTinh, N'đ/v') 
	@DonViTinh as DonViTinh, 
	C.DonGia as DonGia, 
	--ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,C.DonGia,D.NgayKyHopDong, @NgayThucHien, c.HopDongChiTietID),0) AS DonGiaTheoDonViTinh,
	C.DonGia AS DonGiaTheoDonViTinh,
	C.ChietKhau, C.GiamGia, C.ThanhTien,
	C.TiLeTuVan,  C.ChiPhiTuVan,
	C.IsKhuyenMai,  
	C.KhuyenMai,
	--Thuc chay
	0 DmBannerREF,--A.DmBannerREF,
	0 DmChienDichREF,--A.DmChienDichREF,
	--dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(C.DmWebsiteREF) DmWebsiteREF,
	826 DmWebsiteREF,
	--A.DmWebsiteREF,
	--dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF,C.TenWebsite) TenWebsite,
	'(Blanks)' TenWebsite,
	--C.TenWebsite,
	--A.SoHopDong,
	0 TongViewThucChay,
	0 TongClickThucChay,
	0 TongSoBaiViet,
	@SoLuongThucChay SoLuongThucChay,
	--Thanhuc Tien Thuc Chay
	@NgayThucHien AS NgayThucHien,
	@GiaTriThayDoi as GiaTriThayDoi,	 
	@ThanhTienSTCK as ThanhTienThucChayTruocTrietKhau
	FROM 
	(
		SELECT * FROM HopDongChiTiet 
			WHERE HopDongChiTietID = @HopDongChiTietID
						AND DmSanPhamREF = @DmSanPhamREF
						AND TK_AdMarket = @Tk
				AND RecordStatus = 0
	) C  
	INNER JOIN  
	 ( 
	 	SELECT * FROM HopDong hd 
	 	WHERE 1=1-- hd.TrangThaiHopDong <> 3	    
	       AND hd.SOHOPDONG = @SoHopDong
	       AND hd.DeletedStatus = 0
	 ) D on D.HopDongID = C.HopDongFK
	INNER JOIN DmSanPham E ON E.DmSanPhamID = C.DmSanPhamREF
	
	) TD
	
END

```
