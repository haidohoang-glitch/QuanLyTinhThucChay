# Stored Procedure: `ThucChay_InsertThucChayDaTinh_PR_GoiHD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-12-31 10:55:14.870000
- **Ngày sửa cuối**: 2019-12-05 15:01:15.357000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [ThucChay_InsertThucChayDaTinh_PR_GoiHD] '2015-01-15','2015-01-15'


CREATE PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_PR_GoiHD] 
	@StartDate datetime,
	@EndDate datetime
AS
BEGIN

DECLARE @NgayThucHien DATETIME, @NgayGioiHanTinh DATETIME
set @NgayThucHien = Convert(date,@StartDate)
SET @NgayGioiHanTinh = '2014-01-01'
--set @EndDate = CONVERT(date,@StartDate)

DELETE FROM dbo.ThucChayDaTinh
WHERE NgayThucHien BETWEEN @StartDate AND @EndDate
AND DmSanPhamREF IN (141,245,250,637,305)
AND NOT (DmHinhThucQuangCao = 13 or DmLoaiBannerREF = 18)

WHILE(@NgayThucHien <= @EndDate)
BEGIN

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
		CONVERT(BIGINT,ISNULL(D.GiaTien,0))*CONVERT(BIGINT,ISNULL(D.SoLuong,0)) as ThanhTienThucChayTruocTrietKhau,
		ISNULL((CONVERT(float,ISNULL(D.GiaTien,0))*CONVERT(float,ISNULL(D.SoLuong,0)) * CONVERT(float,D.ChietKhau))/100,0) AS GiaTriTrietKhauThucChay,
		CONVERT(float,(100 - D.ChietKhau))*CONVERT(float,(ISNULL(D.GiaTien,0)*ISNULL(D.SoLuong,0)))/100 AS ThanhTienSauTrietKhauThucChay,	
		(CONVERT(float,(100 - D.ChietKhau))*CONVERT(float,(ISNULL(D.GiaTien,0)*ISNULL(D.SoLuong,0)))/100)*ISNULL(hdct.TiLeTuVan,0)/100 AS GiaTriHoaHongThucChay,
		(
			CASE WHEN (D.KhuyenMai = 1 OR D.ChietKhau = 100 OR D.GiaTien = 0 OR D.SoLuong = 0) THEN 0
			ELSE (100 - hdct.TiLeTuVan)/(CONVERT(float,(100 - D.ChietKhau))*CONVERT(float,(ISNULL(D.GiaTien,0)*ISNULL(D.SoLuong,0)))/100)
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
		'' GhiChu	
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
			----, 0 HopDongChiTietID
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
			FROM ThucChayHopDongChiTietPR tchdctp 
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
				 HopDong D  WHERE D.TrangThaiHopDong != 3  AND D.Nam >=2013
			) A ON A.HopDongID = tchdctp.HopDongREF          
			WHERE tchdctp.DeletedStatus <> 1
				AND tchdctp.RecordStatus = 0
				AND tchdctp.DmHinhThucQuangCaoREF <> 0
				AND tchdctp.DmSanPhamREF <> 0	
				AND tchdctp.ThoiGianBatDau >= @NgayGioiHanTinh
				AND (   CASE 
							   WHEN tchdctp.CreatedAt >= tchdctp.LastModifiedAt THEN CONVERT(DATE,tchdctp.CreatedAt)
							   ELSE CONVERT(DATE,tchdctp.LastModifiedAt)
						  END
					) = @NgayThucHien     
		)D
		INNER JOIN HopDongChiTiet hdct ON hdct.HopDongChiTietID = D.HopDongChiTietID
		AND hdct.DmLoaiREF = D.DmHinhThucQuangCaoREF AND hdct.DmSanPhamREF = D.DmSanPhamREF
		--AND hdct.HopDongFK = 40582
		) TD
	)A               
	
	--EXEC [ThucChay_UpdateThucChayHopDongChiTietPR_GoiHD] @NgayThucHien
	EXEC [ThucChay_UpdateThucChayHopDongChiTietPR_GoiHD_v2] @NgayThucHien
	SET @NgayThucHien = dateadd(d,1,@NgayThucHien)	
end 	 

SELECT '1'
END

```
