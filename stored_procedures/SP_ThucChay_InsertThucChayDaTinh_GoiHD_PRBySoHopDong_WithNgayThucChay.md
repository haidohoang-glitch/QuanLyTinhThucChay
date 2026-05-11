# Stored Procedure: `ThucChay_InsertThucChayDaTinh_GoiHD_PRBySoHopDong_WithNgayThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-12-27 11:47:25.177000
- **Ngày sửa cuối**: 2018-01-05 11:20:11.263000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(100)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_InsertThucChayDaTinh_GoiHD_PRBySoHopDong_WithNgayThucChay] 'QC100000', '2015-01-15', 141


CREATE PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_GoiHD_PRBySoHopDong_WithNgayThucChay] 
	@SoHopDong NVARCHAR(50),
	@NgayThucHien DateTime,
	@DmSanPhamREF INT
AS
BEGIN

DECLARE @NgayGioiHanTinh DATETIME, @HopDongREF INT

SET @NgayGioiHanTinh = '2013-01-01'


SET @HopDongREF = (SELECT TOP 1 hd.HopDongID FROM HopDong hd WHERE hd.SoHopDong = @SoHopDong)

INSERT INTO dbo.ThucChayDaTinh 
	SELECT NEWID(), A.* FROM (
	SELECT distinct	TD.*
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
		D.HopDongChiTietID,
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
		D.DmNhanHangREF AS NhanHang, 
		0 DmNhomNganhREF, 
		'' TenNhomNganh, 
		--Thong tin hinh thuc quang cao
		hdct.DmLoaiREF AS DmHinhThucQuangCao, hdct.TenLoai AS TenHinhThucQuangCao, 
		--Thong tin San pham
		hdct.DmSanPhamREF as DmSanPhamREF,
		hdct.TenSanPham,  
		0 DmNhomWebsiteREF, 
		'' TenNhomWebsite, 
		D.DmChuyenMucREF, 
		D.TenChuyenMuc,
		hdct.DmLoaiBannerREF, 
		hdct.TenLoaiBanner, 
		D.DmViTriREF, 
		D.TenViTri, 
		'' DotChayHopDong,
		0 AS SoLuongDotChayHD,
		--'' DotChayBooking,
		D.ThucChayHopDongChiTietPRID DotChayBooking,
		0 AS SoLuongDotChayBooking, 
		--Thong tin ve Tien
		hdct.SoLuong AS SoLuong, 
		dbo.FormatDonViTinh(hdct.DonViTinh) DonViTinh, 
		hdct.DonGia as DonGia, 
		D.GiaTien AS DonGiaTheoDonViTinh,
		D.ChietKhau, hdct.GiamGia, hdct.ThanhTien,
		hdct.TiLeTuVan,  hdct.ChiPhiTuVan,
		D.KhuyenMai IsKhuyenMai,  
		'' KhuyenMai,
		--Thuc chay
		0 DmBannerREF,--A.DmBannerREF,
		0 DmChienDichREF,--A.DmChienDichREF,
		dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(D.DmWebsiteREF) DmWebsiteREF,
		dbo.GetWebsiteLinkByDmWebsiteID(D.DmWebsiteREF,D.TenWebsite) TenWebsite,
		0 TongViewThucChay,
		0 TongClickThucChay,
		0 TongSoBaiViet,
		(CASE when D.KhuyenMai=0 AND D.ChietKhau <> 100 THEN ISNULL(D.SoLuong,0) 
			else 0
		  END
		) 
		as SoLuongThucChay,
		--Thanhuc Tien Thuc Chay
		@NgayThucHien AS NgayThucHien,
		0 as GiaTriThayDoi,
		ISNULL(D.GiaTien,0)*ISNULL(D.SoLuong,0) as ThanhTienThucChayTruocTrietKhau,
		ISNULL((ISNULL(D.GiaTien,0)*ISNULL(D.SoLuong,0) * D.ChietKhau)/100,0) AS GiaTriTrietKhauThucChay,
		CONVERT(FLOAT,(100 - D.ChietKhau))*CONVERT(FLOAT,(ISNULL(D.GiaTien,0)*ISNULL(D.SoLuong,0)))/100 AS ThanhTienSauTrietKhauThucChay,	
		(CONVERT(FLOAT,(100 - D.ChietKhau))*CONVERT(FLOAT,(ISNULL(D.GiaTien,0)*ISNULL(D.SoLuong,0)))/100)*ISNULL(hdct.TiLeTuVan,0)/100 AS GiaTriHoaHongThucChay,
		(
			CASE WHEN (D.KhuyenMai = 1 OR D.ChietKhau = 100 OR D.GiaTien = 0 OR D.SoLuong = 0) THEN 0
			ELSE (100 - hdct.TiLeTuVan)/(CONVERT(FLOAT,(100 - D.ChietKhau))*CONVERT(FLOAT,(ISNULL(D.GiaTien,0)*ISNULL(D.SoLuong,0)))/100)
			END	
		) 
		 AS ThanhTienThucThu,
		(
			CASE WHEN D.KhuyenMai = 1 OR D.ChietKhau = 100 THEN ISNULL(D.GiaTien,0)*ISNULL(D.SoLuong,0)
			ELSE 0
			END	
		) as ThanhTienKM,
		(
			CASE WHEN D.KhuyenMai = 1 OR D.ChietKhau = 100 THEN ISNULL(D.SoLuong,0)
			ELSE 0
			END	
		) AS SoLuongThucChayKM,
		0 SoLuongLechTreoHa,
		0 ThanhTienLechTreoHa,
		GETDATE()CreatedAt,
		GETDATE()LastModifiedAt,
		0 IsPheDuyet,
		'' PheDuyetBy,
		'' PheDuyetAt,
		0 SoLuongThayDoi,
		0 SoLuongKMThayDoi,
		0 GiaTriKMThayDoi,
		'Xu ly sai lech thuc treo va hop dong dang tin' GhiChu	
		FROM 
		 (
			--SELECT A.*, tchdctp.ThucChayHopDongChiTietPRID ,tchdctp.HopDongChiTietREF HopDongChiTietREF_PR
			--, [dbo].[fn_Get_HopDongChiTietID_For_PR]
			--(
			--	tchdctp.HopDongREF ,
			--	tchdctp.ChietKhau,
			--	tchdctp.ThucChayHopDongChiTietPRID,
			--	tchdctp.HopDongChiTietREF,
			--	tchdctp.DmHinhThucQuangCaoREF,
			--	tchdctp.DmSanPhamREF
			--) HopDongChiTietID
			SELECT A.*, tchdctp.ThucChayHopDongChiTietPRID ,tchdctp.HopDongChiTietREF HopDongChiTietREF_PR
			, [dbo].[fn_Get_HopDongChiTietID_For_PR_v2]
			(
				tchdctp.HopDongREF ,
				tchdctp.ChietKhau,
				tchdctp.ThucChayHopDongChiTietPRID,
				tchdctp.HopDongChiTietREF,
				tchdctp.DmHinhThucQuangCaoREF,
				tchdctp.DmSanPhamREF,
				tchdctp.DmWebsiteREF,
				tchdctp.GiaTien
			) HopDongChiTietID
			, tchdctp.NhanHang
			, tchdctp.TenWebsite
			, tchdctp.ChuyenMuc
			, tchdctp.TieuDiem
			, tchdctp.KhuyenMai
			, tchdctp.GiaTien
			, tchdctp.ThoiGianBatDau
			, tchdctp.CreatedAt
			, tchdctp.LastModifiedAt
			, tchdctp.RecordStatus
			, tchdctp.DmWebsiteREF
			, tchdctp.DmChuyenMucREF
			, tchdctp.TenChuyenMuc
			, tchdctp.DmNhanHangREF
			, tchdctp.DmHinhThucQuangCaoREF
			, tchdctp.TenHinhThucQuangCao
			, tchdctp.DmSanPhamREF
			, tchdctp.SoLuong
			, tchdctp.ChietKhau
			, tchdctp.DmViTriREF
			, tchdctp.TenViTri
			, tchdctp.ThucChayHopDongChiTietPrREF 
			FROM (select * from ThucChayHopDongChiTietPR where HopDongREF = @HopDongREF) tchdctp 
			INNER JOIN		
			(SELECT --ID Hop Dong
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
				D.TenKhachHang
			 FROM 
				(select * from  HopDong where HopDongID = @HopDongREF) D  WHERE D.TrangThaiHopDong != 3  AND D.Nam >=2013
			) A ON A.HopDongID = tchdctp.HopDongREF          
			WHERE tchdctp.DeletedStatus <> 1
				AND tchdctp.RecordStatus = 0	
				AND tchdctp.ThoiGianBatDau >= @NgayGioiHanTinh
				--AND (   CASE 
				--			   WHEN tchdctp.CreatedAt >= tchdctp.LastModifiedAt THEN CONVERT(DATE,tchdctp.CreatedAt)
				--			   ELSE CONVERT(DATE,tchdctp.LastModifiedAt)
				--		  END
				--	) < @NgayThucHien     
		)D
		INNER JOIN (select * from HopDongChiTiet where HopDongFK = @HopDongREF) hdct ON hdct.HopDongChiTietID = D.HopDongChiTietID
		AND hdct.DmSanPhamREF = D.DmSanPhamREF AND D.DmHinhThucQuangCaoREF = hdct.DmLoaiREF
		WHERE 1=1 --D.SoHopDong = @SoHopDong
		AND hdct.DmSanPhamREF = @DmSanPhamREF
		) TD
	)A 
	
	EXEC [ThucChay_UpdateThucChayHopDongChiTietPR_GoiHD_ByHopDong] @NgayThucHien, @HopDongREF	 

SELECT '1'
END

```
