# Stored Procedure: `ThucChayDaTinh_UpdateBoxAppSSV`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-01 09:45:17.690000
- **Ngày sửa cuối**: 2014-11-19 12:16:58.983000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-03-22
-- Description:	Update thong tin hop dong cho san pham Boxapp SSV
-- =============================================

-- EXEC dbo.ThucChayDaTinh_UpdateBoxAppSSV '2014-04-20','2014-04-20'
CREATE PROCEDURE [dbo].[ThucChayDaTinh_UpdateBoxAppSSV] 
	-- Add the parameters for the stored procedure here
	@StartDate DATETIME,
	@EndDate DATETIME
AS
BEGIN
	DECLARE @NgayThucHien DATETIME;
	SET @NgayThucHien = @StartDate
	
	WHILE @NgayThucHien <= @EndDate
	BEGIN
		UPDATE [dbo].[ThucChayDaTinh]
		   SET 	
				[HopDongID]						= B.HopDongID
				,[SoHopDong] 					= B.SoHopDong
				,[DmMaHopDongREF]				= B.DmMaHopDongREF
				,[TenMaHopDong]					= B.TenMaHopDong
				,[NgayDanhSoHopDong] 			= B.NgayDanhSoHopDong
				,[NgayKyHopDong]	   			= B.NgayKyHopDong
				,[NhanHopDong]					= B.NhanHopDong
				,[NgayNhanBanFax] 				= B.NgayNhanBanFax
				,[NgayNhanHopDongBanCung]		= B.NgayNhanHopDongBanCung
				,[NgayChuyenHopDongChoKeToan] 	= B.NgayChuyenHopDongChoKeToan
				,[So] 							= B.So 
				,[Thang]						= B.Thang 
				,[Nam]							= B.Nam
				,[GiaTriHopDong]				= B.GiaTriHopDong
				,[CongNo]						= B.CongNo
				,[HopDongChiTietREF]			= C.HopDongChiTietID
				--,[DangSuDung]					= 5004
				,[IsGiayPhep]					= B.IsGiayPhep
				,[TrangThaiHopDong]				= B.TrangThaiHopDong
				,[IsBanCung]					= B.IsBanCung
				,[DmPhongBanREF]				= B.DmPhongBanREF
				,[TenPhongBan]					= B.TenPhongBan
				,[DmBoPhanREF]					= B.DmBoPhanREF
				,[TenBoPhan]					= B.TenBoPhan
				,[DmNhomLamViecREF]				= B.DmNhomLamViecREF 
				,[TenNhomLamViec]				= B.TenNhom
				,[DmDiaDiemLamViecREF]			= B.DmDiaDiemLamViecREF 
				,[TenDiaDiemLamViec]			= B.TenDiaDiemLamViec
				,[SysNhanVienREF]				= B.SysNhanVienREF
				,[TenDangNhap]					= B.TenDangNhap 
				,[TenNhanVien] 					= B.TenNhanVien
				,[TenKhachHang] 				= B.TenKhachHang
				,[NhanHang]						= C.NhanHang
				,[DmNhomNganhREF]				= C.DmNhomNganhREF 
				,[TenNhomNganh]					= C.TenNhomNganh
				,[DmHinhThucQuangCao] 			= 26 --AS DmHinhThucQuangCao, 
				,[TenHinhThucQuangCao] 			= N'Self-serving' --AS TenHinhThucQuangCao,
				--,[DmSanPhamREF] 				= C.DmSanPhamREF 
				--,[TenSanPham]					= C.TenSanPham
				,[DmNhomWebsiteREF] 			= C.DmNhomWebsiteREF
				,[TenNhomWebsite] 				= C.TenNhomWebsite
				,[DmChuyenMucREF] 				= C.DmChuyenMucREF
				,[TenChuyenMuc] 				= C.TenChuyenMuc
				,[DmLoaiBannerREF] 				= C.DmLoaiBannerREF 
				,[TenLoaiBanner] 				= C.TenLoaiBanner
				,[DmViTriREF] 					= C.DmViTriREF 
				,[TenViTri] 					= C.TenViTri
				,[DotChayHopDong] 				= ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,'Y'),'') --DotChayHopDong
				,[SoLuongDotChayHD] 			= C.SoLuong --AS SoLuongDotChayHD
				,[DotChayBooking] 				= ISNULL(dbo.GetDotChayBookingByHopDongChiTiet(C.HopDongChiTietID,'N'),0) --DotChayBooking
				,[SoLuongDotChayBooking] 		= dbo.GetSoLuongDotChayBookingByHopDongChiTiet(C.HopDongChiTietID) --SoLuongDotChayBooking
				,[SoLuong] 						= C.SoLuong*1000 --SoLuong
				,[DonViTinh] 					= 'View'--,DonViTinh
				,[DonGia] 						= dbo.ThucChay_GetDonGiaByNgayThucHien(@NgayThucHien,C.HopDongChiTietID,C.DonGia) --as DonGia
				,[DonGiaTheoDonVi] 				= ISNULL(dbo.ThucChay_GetDonGiaChuanTheoDonViTinh(C.SoLuong,C.DonViTinh,C.DonGia,B.NgayKyHopDong, @NgayThucHien, C.HopDongChiTietID),0) --AS DonGiaTheoDonViTinh
				,[ChietKhau] 					= C.ChietKhau 
				,[GiamGia] 						= C.GiamGia 
				,[ThanhTien] 					= C.ThanhTien
				,[TiLeTuVan] 					= C.TiLeTuVan 
				,[ChiPhiTuVan] 					= C.ChiPhiTuVan
				,[IsKhuyenMai] 					= C.isKhuyenMai 
				,[KhuyenMai] 					= C.KhuyenMai
		FROM ThucChayDaTinh A
			INNER JOIN HopDong B ON B.SoHopDong = A.SoHopDong
			INNER JOIN HopDongChiTiet C ON C.HopDongFK = B.HopDongID
		WHERE 1=1
			--AND A.SoHopDong = 'QC1331213'
			AND A.NgayThucHien = @NgayThucHien
			AND A.DmSanPhamREF = 375
			AND C.DmSanPhamREF = 375
			AND A.DangSuDung = 5004
			
		SET @NgayThucHien = DATEADD(d,1,@NgayThucHien);
	END
END

```
