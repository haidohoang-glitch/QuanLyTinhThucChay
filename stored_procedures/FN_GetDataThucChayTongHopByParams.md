# Function: `GetDataThucChayTongHopByParams`

- **Loại**: SQL_INLINE_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2014-04-11 17:23:26.963000
- **Ngày sửa cuối**: 2014-11-20 11:52:15.650000

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
CREATE FUNCTION [dbo].[GetDataThucChayTongHopByParams]
(	
	-- Add the parameters for the function here
	@StartDate datetime,
	@EndDate datetime
)
RETURNS TABLE 
AS
RETURN 
(
	SELECT
			A.DmSanPhamREF, A.TenSanPham, A.SoHopDong,A.HopDongChiTietREF, A.NgayThucHien, A.NgayKyHopDong, 
			A.isKhuyenMai, A.LechBooking,
			A.TenWebsite,A.DmWebsiteREF, 
			CASE WHEN DmPhongBanREF > 0 THEN TenPhongBan
					 WHEN DmPhongBanREF = 0 THEN 'Management'
					 ELSE '-'
				END AS TenPhongBan, 
				DmPhongBanREF, 
				CASE WHEN DmBoPhanREF > 0 THEN TenBoPhan
					 WHEN DmBoPhanREF = 0 THEN 'Management'
					 ELSE '-'   
				END AS TenBoPhan, 
				DmBoPhanREF, 
				CASE WHEN DmNhomLamViecREF > 0 THEN TenNhomLamViec
					 WHEN DmNhomLamViecREF = 0 THEN 'Management'
					 ELSE '-'   
				END AS TenNhomLamViec, 
			A.DmNhomLamViecREF,
			A.SysNhanVienREF, A.TenDangNhap,TenNhanVien,
			DmHinhThucQuangCao,DangSuDung,DonViTinh,
			A.GiaTriThayDoi,
			A.ThanhTienThucChayNoiBo, A.ThanhTienThucChayKhuyenMai, A.ThanhTienThucChaySauChietKhau,
			A.ThanhTienThucThu AS ThanhTienThucThu,
			A.GiaTriThayDoiNB, A.GiaTriThayDoiTC
		FROM
		(
			SELECT
				DmSanPhamREF, TenSanPham, SoHopDong,HopDongChiTietREF, 
				MAX(NgayThucHien) AS NgayThucHien, MAX(NgayKyHopDong) AS NgayKyHopDong,
				TenWebsite, DmWebsiteREF, TenPhongBan, DmPhongBanREF, TenBoPhan, DmBoPhanREF, TenNhomLamViec, DmNhomLamViecREF,
				SysNhanVienREF,TenDangNhap,TenNhanVien,isKhuyenMai,DmHinhThucQuangCao,DangSuDung,DonViTinh,
				CASE WHEN SoLuongDotChayHD <> SoLuongDotChayBooking THEN 'True'
								ELSE 'False' 
				END AS LechBooking,
				SUM(GiaTriThayDoi) AS GiaTriThayDoi,
				CASE WHEN (UPPER(TenMaHopDong) LIKE 'NB%' OR UPPER(TenMaHopDong) LIKE '%SH%' OR SoHopDong LIKE '%soha%') THEN ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) 
					ELSE 0
				END AS ThanhTienThucChayNoiBo,
				ISNULL(SUM(ThanhTienKM),0) AS ThanhTienThucChayKhuyenMai,			
				ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) AS ThanhTienThucChaySauChietKhau,
				CASE WHEN (UPPER(TenMaHopDong) NOT LIKE 'NB%' AND UPPER(TenMaHopDong) NOT LIKE '%SH%' AND SoHopDong NOT LIKE '%soha%') THEN ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) 
					ELSE 0
				END AS ThanhTienThucThu,
				CASE WHEN (UPPER(TenMaHopDong) LIKE 'NB%' OR UPPER(TenMaHopDong) LIKE '%SH%' OR SoHopDong LIKE '%soha%') THEN ISNULL(SUM(GiaTriThayDoi),0) 
					ELSE 0
				END AS GiaTriThayDoiNB,
				CASE WHEN (UPPER(TenMaHopDong) NOT LIKE 'NB%' AND UPPER(TenMaHopDong) NOT LIKE '%SH%' AND SoHopDong NOT LIKE '%soha%') THEN ISNULL(SUM(GiaTriThayDoi),0) 
					ELSE 0
				END AS GiaTriThayDoiTC
			FROM ThucChayDaTinh 
			WHERE 1=1 and CONVERT(DATE,NgayThucHien) Between @StartDate AND @EndDate
				AND TrangThaiHopDong <> 3
				AND DangSuDung <> 5004
			GROUP BY DmSanPhamREF,TenSanPham,SoHopDong,TenMaHopDong,HopDongChiTietREF,TenMaHopDong,ThanhTienKM,
				isKhuyenMai,SoLuongDotChayHD,SoLuongDotChayBooking,TenWebsite,DmWebsiteREF,TenPhongBan,DmPhongBanREF,
				TenBoPhan, DmBoPhanREF, TenNhomLamViec, DmNhomLamViecREF, SysNhanVienREF, TenDangNhap,TenNhanVien,NgayThucHien,
				DmHinhThucQuangCao,DangSuDung,DonViTinh
		)A
		WHERE  ThanhTienThucChayNoiBo <> 0 OR ThanhTienThucChayKhuyenMai <> 0 OR ThanhTienThucChaySauChietKhau <> 0 OR GiaTriThayDoi <> 0 
)

```
