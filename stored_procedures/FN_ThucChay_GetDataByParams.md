# Function: `ThucChay_GetDataByParams`

- **Loại**: SQL_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2014-04-17 16:19:45.680000
- **Ngày sửa cuối**: 2014-10-14 10:39:32.560000

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
CREATE FUNCTION dbo.ThucChay_GetDataByParams
(
	@FillterString NVARCHAR(MAX)
)
RETURNS 
@TableResult TABLE 
(
	DmSanPhamREF INT, 
	TenSanPham NVARCHAR(50),
	SoHopDong NVARCHAR(50),
	HopDongChiTietREF INT,
	NgayThucHien DATETIME,
	NgayKyHopDong DATETIME,
	DonViTinh NVARCHAR(50),
	isKhuyenMai INT,
	LechBooking NVARCHAR(50),
	TenWebsite NVARCHAR(50),
	DmWebsiteREF INT,
	TenPhongBan NVARCHAR(50), 
	DmPhongBanREF INT, 
	TenBoPhan NVARCHAR(50), 
	DmBoPhanREF INT,
	TenNhomLamViec NVARCHAR(50),
	DmNhomLamViecREF INT,
	SysNhanVienREF INT,
	TenDangNhap NVARCHAR(50),
	TenNhanVien NVARCHAR(50),
	DmHinhThucQuangCao INT,
	DangSuDung INT,
	GiaTriThayDoi FLOAT,
	SoLuongHopDongNoiBo BIGINT,
	SoLuongHopDongKhuyenMai BIGINT,
	SoLuongHopDongThucThu BIGINT,
	SoLuongThucChayNoiBo BIGINT,
	SoLuongThucChayKhuyenMai BIGINT,
	SoLuongThucChayThucThu BIGINT,
	ThanhTienThucChayNoiBo FLOAT, 
	ThanhTienThucChayKhuyenMai FLOAT,
	ThanhTienThucChaySauChietKhau FLOAT,
	ThanhTienThucChayThucThu FLOAT
)
AS
BEGIN
	DECLARE @Sql NVARCHAR(MAX), @DauNhay NVARCHAR(20) = ''''
	--SET @Sql = '
	--		SELECT
	--		A.DmSanPhamREF, A.TenSanPham, A.SoHopDong,A.HopDongChiTietREF, 
	--		A.NgayThucHien, A.NgayKyHopDong, 
	--		A.DonViTinh,A.isKhuyenMai, A.LechBooking,
	--		A.TenWebsite,A.DmWebsiteREF, A.TenPhongBan, A.DmPhongBanREF, A.TenBoPhan, A.DmBoPhanREF, 
	--		A.TenNhomLamViec, 
	--		A.DmNhomLamViecREF,
	--		A.SysNhanVienREF, A.TenDangNhap,TenNhanVien,DmHinhThucQuangCao,DangSuDung,
	--		GiaTriThayDoi, 
	--		--0 AS LogGiaTriThayDoi,
	--		CAST(A.SoLuongHopDongNoiBo AS BIGINT) AS SoLuongHopDongNoiBo, 
	--		CAST(A.SoLuongHopDongKhuyenMai AS BIGINT) AS SoLuongHopDongKhuyenMai,
	--		CAST(A.SoLuongHopDongThucThu AS BIGINT) AS SoLuongHopDongThucThu,
	--		CAST(A.SoLuongThucChayNoiBo AS BIGINT) AS SoLuongThucChayNoiBo, 
	--		CAST(A.SoLuongThucChayKhuyenMai AS BIGINT) AS SoLuongThucChayKhuyenMai, 
	--		CAST(A.SoLuongThucChayThucThu AS BIGINT) AS SoLuongThucChayThucThu,
	--		A.ThanhTienThucChayNoiBo, A.ThanhTienThucChayKhuyenMai, A.ThanhTienThucChaySauChietKhau,
	--		A.ThanhTienThucThu AS ThanhTienThucChayThucThu
	--	FROM
	--	(
	--		SELECT
	--			DmSanPhamREF, TenSanPham, SoHopDong,HopDongChiTietREF, 
	--			MAX(NgayThucHien) AS NgayThucHien,
	--			MAX(NgayKyHopDong) AS NgayKyHopDong,
	--			TenWebsite, DmWebsiteREF, 
	--			CASE WHEN DmPhongBanREF > 0 THEN TenPhongBan
	--				 WHEN DmPhongBanREF = 0 THEN ' + @DauNhay + 'Management' + @DauNhay + '
	--				 ELSE '-'
	--			END AS TenPhongBan, 
	--			DmPhongBanREF, 
	--			CASE WHEN DmBoPhanREF > 0 THEN TenBoPhan
	--				 WHEN DmBoPhanREF = 0 THEN ' + @DauNhay + 'Management' + @DauNhay + '
	--				 ELSE '-'   
	--			END AS TenBoPhan, 
	--			DmBoPhanREF, 
	--			CASE WHEN DmNhomLamViecREF > 0 THEN TenNhomLamViec
	--				 WHEN DmNhomLamViecREF = 0 THEN ' + @DauNhay + 'Management' + @DauNhay + '
	--				 ELSE '-'   
	--			END AS TenNhomLamViec, 
	--			DmNhomLamViecREF,
	--			SysNhanVienREF,TenDangNhap,TenNhanVien, DmHinhThucQuangCao, DangSuDung,
	--			SUM(GiaTriThayDoi) AS GiaTriThayDoi,
	--			dbo.FormatDonViTinh(DonViTinh) AS DonViTinh,isKhuyenMai,
	--			CASE WHEN SoLuongDotChayHD <> SoLuongDotChayBooking THEN ' + @DauNhay + 'True'  + @DauNhay + '
	--							ELSE '  + @DauNhay + 'False'  + @DauNhay + '
	--			END AS LechBooking,
	--			CASE WHEN UPPER(SoHopDong) LIKE ' + @DauNhay + 'NB%'  + @DauNhay + 'THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
	--				ELSE 0
	--			END AS SoLuongHopDongNoiBo,
	--			CASE WHEN ThanhTienKM > 0 THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
	--				ELSE 0
	--			END AS SoLuongHopDongKhuyenMai,
	--			CASE WHEN (ThanhTienKM = 0 AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay + 'NB%'  + @DauNhay + ') THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
	--				ELSE 0
	--			END AS SoLuongHopDongThucThu,
	--			CASE WHEN UPPER(SoHopDong) LIKE ' + @DauNhay + 'NB%'  + @DauNhay + ' THEN ISNULL(SUM(CAST(SoLuongThucChay AS BIGINT)),0) 
	--				ELSE 0
	--			END AS SoLuongThucChayNoiBo,
	--			ISNULL(SUM(CAST(SoLuongThucChayKM AS BIGINT)),0) AS SoLuongThucChayKhuyenMai,
	--			CASE WHEN UPPER(SoHopDong) NOT LIKE ' + @DauNhay + 'NB%'  + @DauNhay + ' THEN ISNULL(SUM(CAST(SoLuongThucChay AS BIGINT)),0) 
	--				ELSE 0
	--			END AS SoLuongThucChayThucThu,
	--			CASE WHEN UPPER(SoHopDong) LIKE ' + @DauNhay + 'NB%'  + @DauNhay + ' THEN ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) 
	--				ELSE 0
	--			END AS ThanhTienThucChayNoiBo,
	--			ISNULL(SUM(ThanhTienKM),0) AS ThanhTienThucChayKhuyenMai,			
	--			ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) AS ThanhTienThucChaySauChietKhau,
	--			CASE WHEN UPPER(SoHopDong) NOT LIKE ' + @DauNhay + 'NB%'  + @DauNhay + ' THEN ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) 
	--				ELSE 0
	--			END AS ThanhTienThucThu
	--		FROM ThucChayDaTinh 
	--		WHERE TrangThaiHopDong <> 3 ' + @FillterString + '   
	--		GROUP BY DmSanPhamREF,TenSanPham,SoHopDong,HopDongChiTietREF,dbo.FormatDonViTinh(DonViTinh),SoHopDong,ThanhTienKM,
	--			isKhuyenMai,SoLuongDotChayHD,SoLuongDotChayBooking,TenWebsite,DmWebsiteREF,TenPhongBan,DmPhongBanREF,
	--			TenBoPhan, DmBoPhanREF, TenNhomLamViec, DmNhomLamViecREF, SysNhanVienREF, TenDangNhap,TenNhanVien,NgayThucHien,DmHinhThucQuangCao,DangSuDung
	--	)A
	--	WHERE 
	--		SoLuongThucChayNoiBo <> 0 OR SoLuongThucChayKhuyenMai <> 0 OR SoLuongThucChayThucThu <> 0 
	--		OR ThanhTienThucChayNoiBo <> 0 OR ThanhTienThucChayKhuyenMai <> 0 OR ThanhTienThucChaySauChietKhau <> 0 OR GiaTriThayDoi <> 0
	--'
	
	SET @Sql = 'SELECT GETDATE()'
	EXEC @Sql
	--INSERT INTO @TableResult

	
	RETURN
END

```
