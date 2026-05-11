# Stored Procedure: `ThucChay_InsertThucChayDaTinh_MobileNoContract`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:21:20.567000
- **Ngày sửa cuối**: 2017-08-04 11:05:24.790000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-04-25
-- Description:	Insert Thuc chay san pham Mobile khong co hop dong
-- =============================================
--
-- EXEC dbo.[ThucChay_InsertThucChayDaTinh_MobileNoContract] '2015-08-08'
--
CREATE PROCEDURE [dbo].[ThucChay_InsertThucChayDaTinh_MobileNoContract] 
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	
	-- Xoa du lieu neu da ton tai
	DELETE FROM ThucChayDaTinh WHERE NgayThucHien = @NgayThucHien AND DmSanPhamREF = 342
	AND (SoHopDong = '-')
	AND NOT (DmHinhThucQuangCao in (13,42) OR DmLoaiBannerREF = 18)
	EXEC ThucChay_InsertToTemp_Mobile @NgayThucHien 
	-- Insert du lieu
	
	
	INSERT INTO ThucChayDaTinh
	SELECT TC.* FROM (
	SELECT 
		NEWID() ThucChayDaTinhID,
		0 HopDongID,
		'-' SoHopDong,
		(CASE WHEN A.IsNoiBo = 1 AND A.UserName <> 'sohagame' THEN 310-- NB
		WHEN A.IsNoiBo = 1 AND A.UserName = 'sohagame' THEN 533 -- SH
		WHEN A.IsNoiBo = 2 THEN ''
		END
		) DmMaHopDongREF,
		(CASE 
		WHEN A.IsNoiBo = 1 AND A.UserName <> 'sohagame' THEN 'NB'
		WHEN A.IsNoiBo = 1 AND A.UserName = 'sohagame' THEN 'SH'
		WHEN A.IsNoiBo = 2 THEN 'ONLINE'		 
		END) TenMaHopDong,
		'1900-01-01 00:00:00.000' NgayDanhSoHopDong, 
		'1900-01-01 00:00:00.000' NgayKyHopDong,
		'' NhanHopDong, 
		'1900-01-01 00:00:00.000' NgayNhanBanFax,
		'1900-01-01 00:00:00.000' NgayNhanHopDongBanCung,
		'1900-01-01 00:00:00.000' NgayChuyenHopDongChoKeToan,
		0 So, 0 Thang, 0 Nam,
		0 GiaTriHopDong, 0 CongNo,
		0 HopDongChiTietID,
		0 DangSuDung, 0 IsGiayPhep,
		1 TrangThaiHopDong, 0 IsBanCung,
		0 DmPhongBanREF, '-' TenPhongBan,
		0 DmBoPhanREF, '-' TenBoPhan,
		0 DmNhomLamViecREF, '-' TenNhom,
		0 DmDiaDiemLamViecREF, '-' TenDiaDiemLamViec,
		ISNULL((SELECT TOP 1 NhanSuSoYeuLyLichID FROM AdminPermisionHDCN WHERE TenDangNhap = A.UserName),0) as SysNhanVienREF, 
		ISNULL(A.UserName,'-') TenDangNhap, 
		ISNULL(A.SaleName,'') TenNhanVien,
		'-' TenKhachHang,
		'0' NhanHang,
		0 DmNhomNganhREF, '' TenNhomNganh,
		(CASE WHEN A.ProductUnitName = 'CPC'  THEN 7 -- CPC				
				ELSE 6 -- CPM
		END)	AS DmHinhThucQuangCao,
		(CASE WHEN A.ProductUnitName = 'CPC'  THEN 'CPC' -- CPC				
				ELSE 'CPM' -- CPM
		END)	AS TenHinhThucQuangCao,                                                                                                                     			 
		342 DmSanPhamREF, N'Mobile' TenSanPham,
		0 DmNhomWebsiteREF, '' TenNhomWebsite,
		0 DmChuyenMucREF, '' TenChuyenMuc,
		0 DmLoaiBannerREF, '' TenLoaiBanner,
		(CASE BannerType WHEN 2 THEN 9021
						WHEN 3 THEN 9024
						WHEN 4 THEN 9023
						WHEN 5 THEN 9022
						WHEN 10 THEN 9025
						WHEN 14 THEN 9046
						WHEN 9 THEN 9125
						WHEN 11 THEN 9126
						WHEN 16 THEN  9137
						WHEN 18 THEN 9165

						
		END) as DmViTriREF, 
		(CASE BannerType WHEN 2 THEN N'Inline'
						WHEN 3 THEN N'Popup'
						WHEN 4 THEN N'Catfish'
						WHEN 5 THEN N'Sponsored Box'
						WHEN 10 THEN N'Medium Banner'
						WHEN 14 THEN N'Inpage full screen'
						WHEN 9 THEN N'Top Banner'
						WHEN 11 THEN N'Insticker'
						WHEN 16 THEN N'Big Article'
						WHEN 18 THEN N'Hook eye'
		END) TenViTri,
		'' DotChayHopDong,
		0 AS SoLuongDotChayHD,
		0  DotChayBooking,
		0 SoLuongDotChayBooking,
		0 SoLuong,
		(Case A.ProductUnitName WHEN 'CPC' THEN 'CLICK'
							   WHEN 'CPM' THEN 'VIEW'
							   END
		)AS  DonViTinh,
		(case A.ProductUnitName WHEN 'CPC' then dbo.ThucChay_GetDonGiaTheoBaoGiaSanPham(NgayThucHien, 342, A.BannerType, A.ProductUnitName)
							   WHEN 'CPM' THEN dbo.ThucChay_GetDonGiaTheoBaoGiaSanPham(NgayThucHien, 342, A.BannerType, A.ProductUnitName)*1000
		
		END) AS DonGia,
		dbo.ThucChay_GetDonGiaTheoBaoGiaSanPham(NgayThucHien, 342, A.BannerType, A.ProductUnitName) DonGiaTheoDonViTinh,
		0 ChietKhau, 0 GiamGia, 0 ThanhTien,
		0 TiLeTuVan, 0 ChiPhiTuVan,
		0 isKhuyenMai, 0 KhuyenMai,
		--Thuc chay
		0 DmBannerREF,--A.DmBannerREF,
		0 DmChienDichREF, --A.DmChienDichREF,
		(SELECT TOP 1 DmWebsiteReportingdbID FROM DmWebsiteReportingdb WHERE DmWebsiteReportingdb.TenWebsite = A.TenWebsite) DmWebsiteREF,
		A.TenWebsite,
		isnull(sum(A.TongViewThucChay),0)TongViewThucChay,
		isnull(sum(A.TongClickThucChay),0)TongClickThucChay,
		0 TongSoBaiViet,
		(CASE WHEN A.ProductUnitName = 'CPC'  THEN  sum(A.TongClickThucChay)-- CPC				
				ELSE sum(A.TongViewThucChay) -- CPM
		END)AS SouongThucChay,
		NgayThucHien NgayThucHien,
		0 GiaTriThayDoi,
		ISNULL(
			(CASE WHEN A.ProductUnitName = 'CPC'  THEN  sum(A.TongClickThucChay) * dbo.ThucChay_GetDonGiaTheoBaoGiaSanPham(NgayThucHien, 342, A.BannerType, A.ProductUnitName)-- CPC				
				ELSE sum(A.TongViewThucChay) *dbo.ThucChay_GetDonGiaTheoBaoGiaSanPham(NgayThucHien, 342, A.BannerType, A.ProductUnitName)
		 END)
		 ,0) AS
		 ThanhTienThucChayTruocChietKhau,
		0 GiaTriChietKhau,
		ISNULL(
		(CASE WHEN A.ProductUnitName = 'CPC'  THEN  sum(A.TongClickThucChay) * dbo.ThucChay_GetDonGiaTheoBaoGiaSanPham(NgayThucHien, 342, A.BannerType, A.ProductUnitName)-- CPC				
				ELSE sum(A.TongViewThucChay) *dbo.ThucChay_GetDonGiaTheoBaoGiaSanPham(NgayThucHien, 342, A.BannerType, A.ProductUnitName)
		 END)
		 ,0) AS ThanhTienSauTrietKhauThucChay,
		0 AS GiaTriHoaHongThucChay,
		ISNULL(
		(CASE WHEN A.ProductUnitName = 'CPC'  THEN  sum(A.TongClickThucChay) * dbo.ThucChay_GetDonGiaTheoBaoGiaSanPham(NgayThucHien, 342, A.BannerType, A.ProductUnitName)-- CPC				
				ELSE sum(A.TongViewThucChay) *dbo.ThucChay_GetDonGiaTheoBaoGiaSanPham(NgayThucHien, 342, A.BannerType, A.ProductUnitName)
		 END)
		 ,0) AS ThanhTienThucThu,
		0 as ThanhTienKM,
		0 as SoLuongThucChayKM,
		0 SoLuongLechTreoHa,
		0 ThanhTienLechTreoHa,
		GETDATE() CreatedAt,
		GETDATE() LastModifiedAt,
		0 IsPheDuyet,
		'' PheDuyetBy,
		'' PheDuyetAt,
		0 SoLuongThayDoi,
		0 SoLuongKMThayDoi,
		0 GiaTriKMThayDoi,
		'' GhiChu
	FROM ThucChay_MobileTemp AS A
	WHERE A.NgayThucHien =   @NgayThucHien
	AND A.TypeProduct = 10
	AND ((A.IsNoiBo = 1 and SoHopDong NOT IN (SELECT hd.SoHopDong FROM HopDong hd))
		OR (A.IsNoiBo = 2 AND SoHopDong = ''))	
	AND A.ProductUnitName IN ('CPC','CPM')	
	AND A.BannerType <> 17
	GROUP BY A.IsNoiBo, A.UserName,A.SaleName,A.ProductUnitName,A.BannerType,TenWebsite, A.NgayThucHien
	)TC
	WHERE TC.SouongThucChay IS NOT NULL
	SELECT '1'
END



```
