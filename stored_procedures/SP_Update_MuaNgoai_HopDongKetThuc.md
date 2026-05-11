# Stored Procedure: `Update_MuaNgoai_HopDongKetThuc`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-12-29 18:08:58.423000
- **Ngày sửa cuối**: 2016-01-12 10:02:43.160000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@GiaTriThayDoi` | `float(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--
--	EXEC dbo.Update_MuaNgoai_HopDongKetThuc '2015-12-28', 71748,560,727272
--
CREATE PROCEDURE [dbo].[Update_MuaNgoai_HopDongKetThuc]
	-- Add the parameters for the stored procedure here
	--@DmSanPhamREF	INT
	@NgayThucHien DATETIME,
	@HopDongChiTietREF INT,
	@DmSanPhamREF INT,
	@GiaTriThayDoi FLOAT
			
AS
BEGIN

	SET NOCOUNT ON;
INSERT INTO thucchaydatinh		
 	SELECT  NEWID(), TD.*, 	
 	0 GiaTriTrietKhauThucChay,	
 	0 AS ThanhTienSauTrietKhauThucChay,	
 	0 AS GiaTriHoaHongThucChay,	
 	0 AS ThanhTienThucThu,	
 	0 as ThanhTienKM,	
 	0 as SoLuongThucChayKM,	
 	0 SoLuongLechTreoHa,	
 	0 ThanhTienLechTreoHa,	
 	GETDATE(),	
 	GETDATE(),	
 	0 IsPheDuyet,	
 	'' PheDuyetBy,	
 	'' PheDuyetAt,1,0,0,''	
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
 	 C.DmLoaiREF AS DmHinhThucQuangCao,-- C.DmLoaiREF
 	C.TenLoai AS TenHinhThucQuangCao, --C.TenLoai	 N'Chi phí khác' 14
 	--Thong tin San pham	
 	@DmSanPhamREF as DmSanPhamREF,	
 	(SELECT TOP 1 dsptc.TenSanPham	
 	   FROM DmSanPhamThucChay dsptc WHERE dsptc.DmSanPhamREF = @DmSanPhamREF AND dsptc.DeletedStatus <> 1)TenSanPham,  	
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
 	'Muangoai_RS2015' DotChayHopDong, --Update Gia tri thay doi GG	
 	0 AS SoLuongDotChayHD,	
 	'Muangoai_RS2015' DotChayBooking,	
 	0 AS SoLuongDotChayBooking, 	
 	--Thong tin ve Tien	
 	ISNULL(dbo.ThucChay_GetSoLuongChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,c.HopDongChiTietID),0) AS SoLuong, 	
 	dbo.FormatDonViTinh(C.DonViTinh) DonViTinh, 	
 	dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,c.HopDongChiTietID,C.DonGia) as DonGia, 	
 	dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,c.HopDongChiTietID,C.DonGia) AS DonGiaTheoDonViTinh,	
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
 		SELECT * FROM HopDongChiTiet WHERE 1=1 --DmSanPhamREF = @DmSanPhamREF
 		AND HopDongChiTietID = @HopDongChiTietREF
 		--AND DmSanPhamREF = @DmSanPhamREF
 		--AND HopDongFK = 16770
		
 	) C  	
 	INNER JOIN  	
 	 ( 	
 	 	SELECT * FROM HopDong hd 
 	    WHERE hd.TrangThaiHopDong != 3	
 	 ) D on D.HopDongID = C.HopDongFK	
 	INNER JOIN DmSanPham E ON E.DmSanPhamID = C.DmSanPhamREF	
 	) TD	
 	----------------------
	UPDATE thucchaydatinh	
	SET NhanHang = ''
	WHERE HopDongChiTietREF = @HopDongChiTietREF
	AND DmSanPhamREF = @DmSanPhamREF
	AND (DmHinhThucQuangCao = 13 OR DmLoaiBannerREF = 18)
	AND NgayThucHien = @NgayThucHien
	AND GiaTriThayDoi <0
		---------------------------------
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
	N'Hop dong ket thuc'NoiDungLog,	
	N'Hop dong ket thuc' NguonLog,	
	''GhiChu,	
	'ThucChay'CreatedBy,	
	getdate()CreatedAt,	
	'ThucChay'LastModifiedBy,	
	getdate()LastModifiedAt,	
	0 DeletedStatus,	
	0 PrintStatus,	
	0 RecordStatus	
FROM dbo.ThucChayDaTinh tcdt WHERE		
 tcdt.NgayThucHien = @NgayThucHien and giatrithaydoi =@GiaTriThayDoi AND HopDongchiTietref = @HopDongChiTietREF	
 AND tcdt.DmSanPhamREF = @DmSanPhamREF
 	END
```
