# Stored Procedure: `MigrateData_ThucChayDaTinh_MuaNgoai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-05-11 11:35:14.840000
- **Ngày sửa cuối**: 2020-05-30 09:53:33.547000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMW
-- Create date: 2015-01-12
-- Description:	Insert Thuc chay da tinh mua ngoai by phanBoId
-- =============================================
/*
EXEC [dbo].[MigrateData_ThucChayDaTinh_MuaNgoai]
	'2015-01-24',
	'2020-05-22'

	--TRUNCATE TABLE [ThucChayDaTinh_MuaNgoai]
*/

CREATE PROCEDURE [dbo].[MigrateData_ThucChayDaTinh_MuaNgoai]
	@FromDate		DATETIME,
	@ToDate			DATETIME
	
AS
BEGIN
	DECLARE @NgayGioiHanTinh DATETIME  = '2013-01-01';
	DECLARE @NgayThucHien DATETIME;
	DECLARE @GhiChu Nvarchar(Max) = N'Migrate Data lãi Thực chạy mua ngoài cho ThucChayDaTinh_MuaNgoai';


	INSERT INTO [dbo].[ThucChayDaTinh_MuaNgoai]
           ([HopDongREF]
           ,[SoHopDong]
           ,[DmMaHopDongREF]
           ,[NgayDanhSoHopDong]
           ,[TrangThaiHopDong]
           ,[DmNhanVienREF]
           ,[TenDangNhap]
           ,[DmPhongBanREF]
           ,[DmBoPhanREF]
           ,[DmNhomLamViecREF]
           ,[DmDiaDiemLamViecREF]
           ,[DmKhachHangREF]
           ,[HopDongChiTietREF]
           ,[LstDmNhanHangREF]
           ,[LstDmNhomNganhREF]
           ,[DmHinhThucQuangCaoREF]
           ,[DmSanPhamREF]
           ,[DmChuyenMucREF]
           ,[DmLoaiBannerREF]
           ,[DmViTriREF]
           ,[SoLuong]
           ,[DonViTinhREF]
           ,[DonGia]
           ,[ChietKhau]
           ,[ThanhTien]
           ,[IsKhuyenMai]
           ,[KhuyenMai]
           ,[ThucChayMuaNgoaiChiTietREF]
		   ,[TongTienDuToanMuaSauCK] 
		   ,[TongTienDuToanLaiMuaSauCK]
           ,[ChietKhauMua]
           ,[DmBannerREF]
           ,[DmChienDichREF]
           ,[DmWebsiteREF]
           ,[TenWebsite]
           ,[NgayThucHien]
           ,[NgayBatDau]
           ,[NgayKetThuc]
           ,[DonViTinhThucChay]
           ,[DonGiaTheoDonViTinhTC]
           ,[TongViewClickThucChay]
           ,[TongSoBaiVietChiPhiThucChay]
           ,[SoLuongThucChay]
           ,[TongThanhTienThucChayBanSauCK]
           ,[TongThanhTienThucChayMuaSauCK]
           ,[ThanhTienLaiThucChaySauCK]
           ,[ThanhTienLaiThucChayKM]
           ,[SoLuongThucChayKM]
           ,[SoLuongThucChayLechTreoHa]
           ,[ThanhTienLechTreoHa]
           ,[GiaTriThayDoiLaiSauCK]
           ,[SoLuongThayDoi]
           ,[SoLuongKMThayDoi]
           ,[GiaTriKMLaiThayDoi]
           ,[GhiChu]
           ,[CreatedAt]
           ,[LastModifiedAt])

     SELECT tcmn.HopDongID, tcmn.SoHopDong, tcmn.DmMaHopDongREF, tcmn.NgayDanhSoHopDong
		, tcmn.TrangThaiHopDong, tcmn.SysNhanVienREF, tcmn.TenDangNhap
		, tcmn.DmPhongBanREF, tcmn.DmBoPhanREF, tcmn.DmNhomLamViecREF, tcmn.DmDiaDiemLamViecREF, tcmn.DmKhachHangREF
		, tcmn.HopDongChiTietID, tcmn.DanhSachNhanHangREF, tcmn.DmNhomNganhREF
		, tcmn.DmLoaiREF, tcmn.DmSanPhamREF, tcmn.DmChuyenMucREF, tcmn.DmLoaiBannerREF
		, tcmn.DmViTriREF, tcmn.SoLuong, tcmn.DonViTinhREF, tcmn.DonGia
		, tcmn.ChietKhau, tcmn.ThanhTien, tcmn.IsKhuyenMai, tcmn.KhuyenMai
		, tcmn.ThucChayMuaNgoaiChiTietID
		, tcmn.TongTienDuToanMuaSauCK
		, tcmn.TongTienDuToanLaiMuaSauCK, tcmn.ChietKhauMuaNgoai, tcmn.DmBannerREF
		, tcmn.DmChienDichREF
		, tcmn.DmWebsiteREF
		, tcmn.TenWebsite
		, tcmn.NgayThucHien
		, tcmn.NgayBatDau
		, tcmn.NgayKetThuc
		, tcmn.DonViTinhThucChay
		, tcmn.DonGiaMuaTheoDonViTinhTC
		, tcmn.TongViewClickThucChay
		, tcmn.TongBaiVietChiPhiThucChay
		, tcmn.SoLuongThucChay
		, tcmn.ThanhTienThucChayBanSauCK
		, tcmn.TongThanhTienThucChayMuaSauCK
		, tcmn.ThanhTienLaiThucChaySauCK
		, tcmn.ThanhTienLaiThucChayKM
		, tcmn.SoLuongThucChayKM
		, tcmn.SoLuongThucChayLechTreoHa
		, tcmn.ThanhTienLaiThucChayLechTreoHa
		, tcmn.GiaTriThayDoiLaiSauCK
		, tcmn.SoLuongThayDoi
		, tcmn.SoLuongKMThayDoi
		, tcmn.GiaTriKMThayDoi
		, tcmn.GhiChu
		, tcmn.CreatedAt
		, tcmn.LastModifiedAt	
	FROM
	(
		SELECT hd.HopDongID, hd.SoHopDong, hd.DmMaHopDongREF, hd.NgayDanhSoHopDong
		, hd.TrangThaiHopDong, hd.SysNhanVienREF, hd.TenDangNhap
		, hd.DmPhongBanREF, hd.DmBoPhanREF, hd.DmNhomLamViecREF, hd.DmDiaDiemLamViecREF, hd.DmKhachHangREF
		, hdct.HopDongChiTietID, ISNULL(hdct.DanhSachNhanHangREF,'') AS DanhSachNhanHangREF, hdct.DmNhomNganhREF
		, hdct.DmLoaiREF, hdct.DmSanPhamREF, hdct.DmChuyenMucREF, hdct.DmLoaiBannerREF
		, hdct.DmViTriREF, hdct.SoLuong, hdct.DonViTinhREF, hdct.DonGia
		, hdct.ChietKhau, hdct.ThanhTien, hdct.IsKhuyenMai, hdct.KhuyenMai
		, tcmn.ThucChayMuaNgoaiChiTietID
		, tcmn.TongTienDuToanMuaSauCK
		, tcmn.TongTienDuToanLaiMuaSauCK
		, tcmn.ChietKhauMuaNgoai, 0 AS DmBannerREF
		, 0 AS DmChienDichREF
		, dbo.GetDmWebsiteReportingdbIDByDmWebsiteID(hdct.DmWebsiteREF) DmWebsiteREF
		, dbo.GetWebsiteLinkByDmWebsiteID(hdct.DmWebsiteREF,hdct.TenWebsite) TenWebsite
		, CONVERT(DATE,tcmn.NgayChot) AS NgayThucHien
		, CONVERT(Date,tcmn.TuNgay) AS NgayBatDau
		, CONVERT(DATE,tcmn.DenNgay) AS NgayKetThuc
		,  (SELECT TOP(1) TenDonViTinh FROM dbo.DmDonViTinh
									WHERE DmDonViTinhID = tcmn.DmDonViTinhREF
									AND DeletedStatus = 0
									ORDER BY DmDonViTinhID
		) AS DonViTinhThucChay
		, (CASE WHEN ISNULL(tcmn.SoLuongThucChay,0) <> 0 THEN (tcmn.ThanhTienMuaNgoaiTruocCK*(100-tcmn.ChietKhauMuaNgoai)/100)/ISNULL(tcmn.SoLuongThucChay,0)
			ELSE (tcmn.ThanhTienMuaNgoaiTruocCK*(100-tcmn.ChietKhauMuaNgoai)/100)
		END) AS DonGiaMuaTheoDonViTinhTC
		, 0 AS TongViewClickThucChay
		, 0 AS TongBaiVietChiPhiThucChay
		, (CASE WHEN hdct.ChietKhau <> 100 THEN ISNULL(tcmn.SoLuongThucChay,0)
			ELSE 0 
		END) AS SoLuongThucChay
		, ISNULL(tcmn.ThanhTienThucChayBanSauCK,0) ThanhTienThucChayBanSauCK
		, (tcmn.ThanhTienMuaNgoaiTruocCK*(100-tcmn.ChietKhauMuaNgoai)/100) AS TongThanhTienThucChayMuaSauCK
		, (CASE WHEN hdct.ChietKhau <> 100 THEN tcmn.ThanhTienLaiThucChaySauCK
		ELSE 0
		END) AS ThanhTienLaiThucChaySauCK
		, (CASE WHEN hdct.ChietKhau = 100 THEN tcmn.ThanhTienLaiThucChaySauCK
		ELSE 0
		END) AS ThanhTienLaiThucChayKM
		, (CASE WHEN hdct.ChietKhau = 100 THEN ISNULL(tcmn.SoLuongThucChay,0)
		ELSE 0
		END) AS SoLuongThucChayKM
		, 0 AS SoLuongThucChayLechTreoHa
		, 0 AS ThanhTienLaiThucChayLechTreoHa
		, 0 AS GiaTriThayDoiLaiSauCK
		, 0 AS SoLuongThayDoi
		, 0 AS SoLuongKMThayDoi
		, 0 AS GiaTriKMThayDoi
		, @GhiChu AS GhiChu
		, Getdate() AS CreatedAt
		, GetDate() AS LastModifiedAt
		FROM
		(
			SELECT tcmn.*, ISNULL(mn.ThanhTienSauCKMua,0) AS [TongTienDuToanMuaSauCK], ISNULL(mn.ThanhTienLaiSauCK,0) AS [TongTienDuToanLaiMuaSauCK]
			FROM dbo.ThucChayMuaNgoaiChiTiet tcmn
			INNER JOIN dbo.HopDongChiTiet_MuaNgoai mn on mn.HopDongChiTietID = tcmn.HopDongChiTietREF
			WHERE 1=1 
			--AND Status = 2 --trang thai duyet thanh toan
			AND tcmn.TrangThaiTinhThucChay = 1
			AND CONVERT(DATE,ISNULL(tcmn.NgayChot,'1900-01-01')) BETWEEN @FromDate AND @ToDate
			--AND tcmn.TuNgay >= @NgayGioiHanTinh
			AND tcmn.DeletedStatus = 0
		)tcmn
		INNER JOIN 
		(SELECT ct.* FROM dbo.HopDongChiTiet ct 
			WHERE ct.DeletedStatus = 0
			AND (ct.DmLoaiREF = 13 OR ct.DmLoaiBannerREF = 18)
		)hdct ON hdct.HopDongFK = tcmn.HopDongREF AND hdct.HopDongChiTietID = tcmn.HopDongChiTietREF
		INNER JOIN HopDong hd on hd.HopDongID = hdct.HopDongFK
	
	)tcmn WHERE 1=1
	AND tcmn.HopDongChiTietID NOT IN (SELECT  DISTINCT hopdongchiTietID FROM MuaNgoaiChot_TinhBoSung_2016)
	AND tcmn.HopDongID NOT IN (SELECT HopDongID from HopDong where TrangThaiHopDong = 3) --tuyetnta bổ sung ngày 30/5/2020
	SELECT 1;
END

--select * from ThucChayDaTinh_MuaNgoai
```
