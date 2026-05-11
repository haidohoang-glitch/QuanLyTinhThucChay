# Stored Procedure: `update_thucchay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-01-07 14:36:39.233000
- **Ngày sửa cuối**: 2017-04-21 16:55:38.390000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(100)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@GhiChu` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
CREATE PROC [dbo].[update_thucchay]
 @SoHopDong NVARCHAR(50),
@HopDongChiTietID INT
,@NgayThucHien DATETIME
,@GhiChu NVARCHAR(200)
AS
BEGIN
DECLARE @SoLuongThucChay INT, @ThanhTienTTCK FLOAT , @GiaTriThayDoi INT
, @DonViTinh NVARCHAR(50), @NoiDungLog NVARCHAR(100), @SoLuongThayDoi INT, @DmWebsiteREF INT, @TenWebsite NVARCHAR(50),@ThanhTienSTCK FLOAT, @NhanHang NVARCHAR(50)
, @a FLOAT , @b FLOAT, @DmSanPhamREF INT, @a1 FLOAT , @b1 FLOAT

   SET @a1 = (SELECT (CASE WHEN DonViTinh = 'CPM' THEN soluong*1000
					          ELSE soluong END) FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID)
							  SET @b1 =  (SELECT SUM(SoLuongThucChay) FROM dbo.ThucChayDaTinh WHERE HopDongChiTietREF = @HopDongChiTietID AND NgayThucHien<=@NgayThucHien)
   SET @SoLuongThucChay = @a1 - @b1
   SET @SoLuongThayDoi =0-0
   SET @ThanhTienSTCK =0
   SET @a =  (SELECT ThanhTien FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID)
   SET @b = (SELECT SUM(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi) FROM dbo.ThucChayDaTinh WHERE HopDongChiTietREF = @HopDongChiTietID AND NgayThucHien<=@NgayThucHien)
   set @GiaTriThayDoi =    @a- @b

   SET @NhanHang = (SELECT TOP 1 NhanHang FROM thucchaydatinh WHERE HopDongChiTietREF = @HopDongChiTietID AND NhanHang <> '0'ORDER BY NgayThucHien DESC)
SET @DmSanPhamREF = (SELECT DmSanPhamREF FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID)
--SET @TK_Admarket = 'trinh1518'
SET @DonViTinh = (SELECT (CASE WHEN DonViTinh = 'CPM' THEN 'VIEW' 
					          WHEN DonViTinh ='CPC' THEN 'CLICK' ELSE DonViTinh END) FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID)
SET @dmwebsiteREF = 826

SET @TenWebsite = '(Blanks)'

SET @NoiDungLog = N''

	INSERT INTO dbo.ThucChayDaTinh
	SELECT  NEWID() thucchaydatinhid, TD.*, 
	ISNULL((TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100,0) AS GiaTriTrietKhauThucChay,
	ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100),0) AS ThanhTienSauTrietKhauThucChay,	
	ISNULL(((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100,0) AS GiaTriHoaHongThucChay,
	ISNULL((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100 - ((TD.ThanhTienThucChayTruocTrietKhau - (TD.ThanhTienThucChayTruocTrietKhau * TD.ChietKhau)/100) * TD.TiLeTuVan)/100),0) AS ThanhTienThucThu,
	(CASE when ((TD.IsKhuyenMai=1) OR (TD.ChietKhau = 100)) then TD.ThanhTienThucChayTruocTrietKhau
		else 0
	  END
	) as ThanhTienKM,
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
	C.DmViTriREF, 
	C.TenViTri, 
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
	@DmWebsiteREF DmWebsiteREF,
	--A.DmWebsiteREF,
	--dbo.GetWebsiteLinkByDmWebsiteID(C.DmWebsiteREF,C.TenWebsite) TenWebsite,
	@Tenwebsite TenWebsite,
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
						--AND TK_AdMarket = @TK_Admarket
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
	
INSERT INTO dbo.ThucChay_LogNNTinhGiaTriThayDoi

SELECT
	newid() ThuChay_LogNNTinhGiaTriThayDoiID,
	HopDongID HopDongREF,
	SoHopDong,
	HopDongChiTietREF,
	DmSanPhamREF,
	DmWebsiteREF,
	NgayThucHien,
	GiaTriThayDoi,
	0 GiaSauCK1,
	0 Soluong1,
	0 GiaSauCK2,
	0 Soluong2,
	@NoiDungLog NoiDungLog,
	N'ThucChay' NguonLog,
	''GhiChu,
	'ThucChay'CreatedBy,
	getdate()CreatedAt,
	'ThucChay'LastModifiedBy,
	getdate()LastModifiedAt,
	0 DeletedStatus,
	0 PrintStatus,
	0 RecordStatus
FROM dbo.ThucChayDaTinh tcdt WHERE
 tcdt.NgayThucHien = @NgayThucHien and giatrithaydoi <> 0 AND HopDongchiTietref = @HopDongChiTietID 

 end
```
