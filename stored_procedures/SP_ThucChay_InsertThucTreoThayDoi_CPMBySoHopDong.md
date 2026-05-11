# Stored Procedure: `ThucChay_InsertThucTreoThayDoi_CPMBySoHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-13 14:02:27.940000
- **Ngày sửa cuối**: 2017-05-16 17:03:45.213000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongREF` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmSanphamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(200)` | No |
| `@HopDongChiTiet` | `int(4)` | No |
| `@NgaythucHien` | `datetime(8)` | No |
| `@GiaTriThayDoi` | `float(8)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(200)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_InsertThucChayDaTinh_PR]

--ALTER TABLE ThucChayDaTinh 
--ADD SoLuongThayDoi INT NOT NULL DEFAULT 0
--,SoLuongKMThayDoi INT NOT NULL DEFAULT 0
--,GiaTriKMThayDoi FLOAT NOT NULL DEFAULT 0
--,GhiChu NVARCHAR(200) 


--ALTER TABLE ThucChayDaTinhAdmarket 
--ADD SoLuongThayDoi INT NOT NULL DEFAULT 0
--,SoLuongKMThayDoi INT NOT NULL DEFAULT 0
--,GiaTriKMThayDoi FLOAT NOT NULL DEFAULT 0
--,GhiChu NVARCHAR(200) 



CREATE  PROCEDURE [dbo].[ThucChay_InsertThucTreoThayDoi_CPMBySoHopDong]
	@HopDongREF INT,
	@SoHopDong NVARCHAR(50),
	@DmSanphamREF INT,
	@TenSanPham NVARCHAR(100),
	@HopDongChiTiet INT,
	@NgaythucHien DATETIME,
	@GiaTriThayDoi FLOAT,
	@DmWebsiteREF INT,
	@TenWebsite NVARCHAR(100)
AS
BEGIN
	PRINT @HopDongChiTiet
	INSERT INTO dbo.ThucChayDaTinh 
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
	'' PheDuyetAt,
	0 SoLuongThayDoi,
	0 SoLuongKMThayDoi,
	0 GiaTriKMThayDoi,
	'' GhiChu	
	FROM 
	(
	SELECT 
	--ID Hop Dong
	C.HopDongID,
	--Thong tin ve ma so 
	C.SoHopDong, 
	C.DmMaHopDongREF, 
	C.TenMaHopDong, 
	--Thong tin ve thoi gian
	C.NgayDanhSoHopDong, C.NgayKyHopDong, 
	ISNULL(C.NhanHopDong,'') AS NhanHopDong, C.NgayNhanBanFax, C.NgayNhanHopDongBanCung, C.NgayChuyenHopDongChoKeToan, 
	C.So, C.Thang, C.Nam, 
	--Thong tin ve gia tri
	C.GiaTriHopDong, C.CongNo,
	--Thong tin chi tiet phan bo
	0 HopDongChiTietID,
	--Thong tin ve trang thai
	C.DangSuDung, C.IsGiayPhep, C.TrangThaiHopDong,C.IsBanCung, 
	--Thong tin ve Nhan vien kinh doanh
	C.DmPhongBanREF, 
	ISNULL(C.TenPhongBan, '') AS TenPhongBan, 
	C.DmBoPhanREF, 
	ISNULL(C.TenBoPhan,'') AS TenBoPhan, 
	C.DmNhomLamViecREF, 
	ISNULL(C.TenNhom, '') AS TenNhom, 
	C.DmDiaDiemLamViecREF, 
	C.TenDiaDiemLamViec, 
	C.SysNhanVienREF, 
	ISNULL(C.TenDangNhap, '') AS TenDangNhap,  
	C.TenNhanVien, 
	--Thong tin ve khach hang
	--C.DmKhachHangREF, 
	C.TenKhachHang, 
	'' NhanHang, 
	0 DmNhomNganhREF, 
	'' TenNhomNganh, 
	--Thong tin hinh thuc quang cao
	0 AS DmHinhThucQuangCao, '' AS TenHinhThucQuangCao, 
	--Thong tin San pham
	@DmSanphamREF as DmSanPhamREF,
	@TenSanPham as TenSanPham,  
	0 DmNhomWebsiteREF, 
	'' TenNhomWebsite, 
	0 DmChuyenMucREF, 
	'' TenChuyenMuc,
	0 DmLoaiBannerREF, 
	'' TenLoaiBanner, 
	0 DmViTriREF, 
	'' TenViTri, 
	'CPM_TTR' DotChayHopDong,
	0 AS SoLuongDotChayHD,
	'PS THUC TREO CPM' DotChayBooking,
	0 AS SoLuongDotChayBooking, 
	--Thong tin ve Tien
	C.SoLuong*1000 AS SoLuong,
	(CASE when (UPPER(C.DonViTinh) = 'CPM') then 'VIEW'
		when (UPPER(C.DonViTinh) = 'CPC') then 'CLICK'
		else 'CPA'
	  END
	) as DonViTinh, 
	--'VIEW' DonViTinh, 
	C.DonGia as DonGia, 
	C.DonGiaSauCK AS DonGiaTheoDonViTinh,
	0 ChietKhau, 0 GiamGia, C.ThanhTien,
	0 TiLeTuVan,  0 ChiPhiTuVan,
	0 IsKhuyenMai,  
	'' KhuyenMai,
	--Thuc chay
	0 DmBannerREF,--A.DmBannerREF,
	0 DmChienDichREF,--A.DmChienDichREF,
	@DmWebsiteREF DmWebsiteREF,
	@TenWebsite TenWebsite,
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
		SELECT (case when HDCT.DmSanPhamREF=231 then 3
					 when HDCT.DmSanPhamREF=238 then 4
					 when HDCT.DmSanPhamREF=339 then 5
					 when HDCT.DmSanPhamREF=342 then 6
					 when HDCT.DmSanPhamREF=337 then 7
					 when HDCT.DmSanPhamREF=240 then 8
					 when HDCT.DmSanPhamREF=598 then 14
					 when HDCT.DmSanPhamREF=613 then 15
					else 9
				end) as type_product, hd.SoHopDong, 
				hd.HopDongID,
		--Thong tin ve ma so 
		hd.DmMaHopDongREF, 
		hd.TenMaHopDong, 
		--Thong tin ve thoi gian
		hd.NgayDanhSoHopDong, hd.NgayKyHopDong, 
		hd.NhanHopDong, hd.NgayNhanBanFax, hd.NgayNhanHopDongBanCung, hd.NgayChuyenHopDongChoKeToan, 
		hd.So, hd.Thang, hd.Nam, 
		--Thong tin ve gia tri
		hd.GiaTriHopDong, hd.CongNo,
		--Thong tin chi tiet phan bo
		--Thong tin ve trang thai
		hd.DangSuDung, hd.IsGiayPhep, hd.TrangThaiHopDong,hd.IsBanCung, 
		--Thong tin ve Nhan vien kinh doanh
		hd.DmPhongBanREF, 
		ISNULL(hd.TenPhongBan, '') AS TenPhongBan, 
		hd.DmBoPhanREF, 
		ISNULL(hd.TenBoPhan,'') AS TenBoPhan, 
		hd.DmNhomLamViecREF, 
		ISNULL(hd.TenNhom, '') AS TenNhom, 
		hd.DmDiaDiemLamViecREF, 
		hd.TenDiaDiemLamViec, 
		hd.SysNhanVienREF, 
		ISNULL(hd.TenDangNhap, '') AS TenDangNhap,  
		hd.TenNhanVien, 
		--Thong tin ve khach hang
		--D.DmKhachHangREF, 
		hd.TenKhachHang,
		SUM(hdct.SoLuong) soluongdotchayHD,
		SUM(hdct.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)) soluong,
		SUM(hdct.ThanhTien) ThanhTien, 
		MAX(dbo.dbo.ThucChay_GetDonViTinhNotCPD(hdct.DonViTinh)) as DonViTinh,
		MAX(hdct.ThanhTien/(hdct.SoLuong*dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh))) DonGiaSauCK,
		MAX(hdct.DonGia/dbo.ThucChay_GetSoLuongChuanTheoDonViTinhNotCPD(hdct.DonViTinh)) DonGia					
		FROM HopDong hd
		INNER JOIN HopDongChiTiet hdct ON HD.HopDongID = HDCT.HopDongFK
		WHERE HDCT.DmSanPhamREF IN (231,238,339,342,337,240,370,598,613,732)
		AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) = 3 --Đơn vị của hình thức CPM
		AND hd.HopDongID = @HopDongREF
		AND hdct.DeletedStatus = 0
		GROUP BY HDCT.DmSanPhamREF,  HD.SoHopDong,
		hd.HopDongID,
		--Thong tin ve ma so 
		hd.DmMaHopDongREF, 
		hd.TenMaHopDong, 
		--Thong tin ve thoi gian
		hd.NgayDanhSoHopDong, hd.NgayKyHopDong, 
		hd.NhanHopDong, hd.NgayNhanBanFax, hd.NgayNhanHopDongBanCung, hd.NgayChuyenHopDongChoKeToan, 
		hd.So, hd.Thang, hd.Nam, 
		--Thong tin ve gia tri
		hd.GiaTriHopDong, hd.CongNo,
		--Thong tin chi tiet phan bo
		--Thong tin ve trang thai
		hd.DangSuDung, hd.IsGiayPhep, hd.TrangThaiHopDong,hd.IsBanCung, 
		--Thong tin ve Nhan vien kinh doanh
		hd.DmPhongBanREF, 
		hd.TenPhongBan, 
		hd.DmBoPhanREF, 
		hd.TenBoPhan, 
		hd.DmNhomLamViecREF, 
		hd.TenNhom, 
		hd.DmDiaDiemLamViecREF, 
		hd.TenDiaDiemLamViec, 
		hd.SysNhanVienREF, 
		hd.TenDangNhap,  
		hd.TenNhanVien, 
		hd.TenKhachHang
	) C  
	
	) TD

END

```
