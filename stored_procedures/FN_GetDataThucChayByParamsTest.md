# Function: `GetDataThucChayByParamsTest`

- **Loại**: SQL_INLINE_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2014-04-17 15:54:16.310000
- **Ngày sửa cuối**: 2014-10-14 10:39:36.903000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FillterString` | `nvarchar` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--SELECT * FROM [dbo].[GetDataThucChayByParamsTest]('')

CREATE FUNCTION [dbo].[GetDataThucChayByParamsTest]
(	
	@FillterString NVARCHAR(MAX)
)
RETURNS TABLE 
AS
RETURN 
(
	SELECT TOP 1 * FROM AdminUser AS au
		--SELECT
		--	A.DmSanPhamREF, A.TenSanPham, A.SoHopDong,A.HopDongChiTietREF, 
		--	A.NgayThucHien, A.NgayKyHopDong, 
		--	A.DonViTinh,A.isKhuyenMai, A.LechBooking,
		--	A.TenWebsite,A.DmWebsiteREF, A.TenPhongBan, A.DmPhongBanREF, A.TenBoPhan, A.DmBoPhanREF, 
		--	A.TenNhomLamViec, 
		--	A.DmNhomLamViecREF,
		--	A.SysNhanVienREF, A.TenDangNhap,TenNhanVien,DmHinhThucQuangCao,DangSuDung,
		--	GiaTriThayDoi, 
		--	--0 AS LogGiaTriThayDoi,
		--	CAST(A.SoLuongHopDongNoiBo AS BIGINT) AS SoLuongHopDongNoiBo, 
		--	CAST(A.SoLuongHopDongKhuyenMai AS BIGINT) AS SoLuongHopDongKhuyenMai,
		--	CAST(A.SoLuongHopDongThucThu AS BIGINT) AS SoLuongHopDongThucThu,
		--	CAST(A.SoLuongThucChayNoiBo AS BIGINT) AS SoLuongThucChayNoiBo, 
		--	CAST(A.SoLuongThucChayKhuyenMai AS BIGINT) AS SoLuongThucChayKhuyenMai, 
		--	CAST(A.SoLuongThucChayThucThu AS BIGINT) AS SoLuongThucChayThucThu,
		--	A.ThanhTienThucChayNoiBo, A.ThanhTienThucChayKhuyenMai, A.ThanhTienThucChaySauChietKhau,
		--	A.ThanhTienThucThu AS ThanhTienThucChayThucThu
		--FROM
		--(
		--	SELECT
		--		DmSanPhamREF, TenSanPham, SoHopDong,HopDongChiTietREF, 
		--		MAX(NgayThucHien) AS NgayThucHien,
		--		MAX(NgayKyHopDong) AS NgayKyHopDong,
		--		TenWebsite, DmWebsiteREF, 
		--		CASE WHEN DmPhongBanREF > 0 THEN TenPhongBan
		--			 WHEN DmPhongBanREF = 0 THEN 'Management'
		--			 ELSE '-'
		--		END AS TenPhongBan, 
		--		DmPhongBanREF, 
		--		CASE WHEN DmBoPhanREF > 0 THEN TenBoPhan
		--			 WHEN DmBoPhanREF = 0 THEN 'Management'
		--			 ELSE '-'   
		--		END AS TenBoPhan, 
		--		DmBoPhanREF, 
		--		CASE WHEN DmNhomLamViecREF > 0 THEN TenNhomLamViec
		--			 WHEN DmNhomLamViecREF = 0 THEN 'Management'
		--			 ELSE '-'   
		--		END AS TenNhomLamViec, 
		--		DmNhomLamViecREF,
		--		SysNhanVienREF,TenDangNhap,TenNhanVien, DmHinhThucQuangCao, DangSuDung,
		--		SUM(GiaTriThayDoi) AS GiaTriThayDoi,
		--		dbo.FormatDonViTinh(DonViTinh) AS DonViTinh,isKhuyenMai,
		--		CASE WHEN SoLuongDotChayHD <> SoLuongDotChayBooking THEN 'True'
		--						ELSE 'False' 
		--		END AS LechBooking,
		--		CASE WHEN UPPER(SoHopDong) LIKE 'NB%' THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
		--			ELSE 0
		--		END AS SoLuongHopDongNoiBo,
		--		CASE WHEN ThanhTienKM > 0 THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
		--			ELSE 0
		--		END AS SoLuongHopDongKhuyenMai,
		--		CASE WHEN (ThanhTienKM = 0 AND UPPER(SoHopDong) NOT LIKE 'NB%') THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
		--			ELSE 0
		--		END AS SoLuongHopDongThucThu,
		--		CASE WHEN UPPER(SoHopDong) LIKE 'NB%' THEN ISNULL(SUM(CAST(SoLuongThucChay AS BIGINT)),0) 
		--			ELSE 0
		--		END AS SoLuongThucChayNoiBo,
		--		ISNULL(SUM(CAST(SoLuongThucChayKM AS BIGINT)),0) AS SoLuongThucChayKhuyenMai,
		--		CASE WHEN UPPER(SoHopDong) NOT LIKE 'NB%' THEN ISNULL(SUM(CAST(SoLuongThucChay AS BIGINT)),0) 
		--			ELSE 0
		--		END AS SoLuongThucChayThucThu,
		--		CASE WHEN UPPER(SoHopDong) LIKE 'NB%' THEN ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) 
		--			ELSE 0
		--		END AS ThanhTienThucChayNoiBo,
		--		ISNULL(SUM(ThanhTienKM),0) AS ThanhTienThucChayKhuyenMai,			
		--		ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) AS ThanhTienThucChaySauChietKhau,
		--		CASE WHEN UPPER(SoHopDong) NOT LIKE 'NB%' THEN ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) 
		--			ELSE 0
		--		END AS ThanhTienThucThu
		--	FROM ThucChayDaTinh 
		--	WHERE TrangThaiHopDong <> 3   
		--	GROUP BY DmSanPhamREF,TenSanPham,SoHopDong,HopDongChiTietREF,dbo.FormatDonViTinh(DonViTinh),SoHopDong,ThanhTienKM,
		--		isKhuyenMai,SoLuongDotChayHD,SoLuongDotChayBooking,TenWebsite,DmWebsiteREF,TenPhongBan,DmPhongBanREF,
		--		TenBoPhan, DmBoPhanREF, TenNhomLamViec, DmNhomLamViecREF, SysNhanVienREF, TenDangNhap,TenNhanVien,NgayThucHien,DmHinhThucQuangCao,DangSuDung
		--)A
		--WHERE 
		--	SoLuongThucChayNoiBo <> 0 OR SoLuongThucChayKhuyenMai <> 0 OR SoLuongThucChayThucThu <> 0 
		--	OR ThanhTienThucChayNoiBo <> 0 OR ThanhTienThucChayKhuyenMai <> 0 OR ThanhTienThucChaySauChietKhau <> 0 OR GiaTriThayDoi <> 0

)

```
