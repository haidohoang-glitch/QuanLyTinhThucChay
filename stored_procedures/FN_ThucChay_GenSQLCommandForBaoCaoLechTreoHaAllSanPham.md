# Function: `ThucChay_GenSQLCommandForBaoCaoLechTreoHaAllSanPham`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-07-17 08:28:13.693000
- **Ngày sửa cuối**: 2014-10-14 10:39:33.367000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar` | Yes |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREFList` | `nvarchar(8000)` | No |
| `@DmWebsiteREFList` | `nvarchar(8000)` | No |
| `@SoHopDongList` | `nvarchar(8000)` | No |
| `@DmPhongBanREFList` | `nvarchar(8000)` | No |
| `@DmBoPhanREFList` | `nvarchar(8000)` | No |
| `@DmNhomLamViecREFList` | `nvarchar(8000)` | No |
| `@TenNhanVienList` | `nvarchar(8000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@DmPhongBanREF` | `int(4)` | No |
| `@DmBoPhanREF` | `int(4)` | No |
| `@DmNhomlamViecREF` | `int(4)` | No |
| `@DmChucDanhREF` | `int(4)` | No |
| `@DmHinhThucQuangCaoList` | `nvarchar(4000)` | No |
| `@DmBannerREFList` | `nvarchar(4000)` | No |
| `@DonViTinhList` | `nvarchar(1024)` | No |
| `@IsShowNoiBo` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-04-11
-- Description:	Gen SQL Command for bao cao lech treo ha theo san pham, hop dong
-- =============================================
--
-- PRINT dbo.ThucChay_GenSQLCommandForBaoCaoLechTreoHaTheoAllSanPham('',0)
-- 

CREATE FUNCTION [dbo].[ThucChay_GenSQLCommandForBaoCaoLechTreoHaAllSanPham]
(
	-- Add the parameters for the function here
	@StartDate datetime,
	@EndDate datetime,
	@DmSanPhamREFList nvarchar(4000),
	@DmWebsiteREFList nvarchar(4000),
	@SoHopDongList nvarchar(4000),
	@DmPhongBanREFList nvarchar(4000),
	@DmBoPhanREFList nvarchar(4000),
	@DmNhomLamViecREFList nvarchar(4000),
	@TenNhanVienList nvarchar(4000),
	@TenDangNhap NVARCHAR(50),
	@DmPhongBanREF int,
	@DmBoPhanREF int,
	@DmNhomlamViecREF int,
	@DmChucDanhREF INT,
	@DmHinhThucQuangCaoList NVARCHAR(2000),
	@DmBannerREFList NVARCHAR(2000),
	@DonViTinhList	NVARCHAR(512),
	@IsShowNoiBo	INT -- -1: all, 1: noi bo
)
RETURNS NVARCHAR(MAX)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @SqlCommand		NVARCHAR(MAX),
			@FilterString	NVARCHAR(MAX),
			@DauNhay		NVARCHAR(10)
			
	SET @DauNhay = '''';
	SET @SqlCommand = '';
	SET @FilterString = ' AND '
	
	SET @FilterString +=  dbo.GetThucChayFilterString(
														@StartDate ,
														@EndDate ,
														@DmSanPhamREFList ,
														@DmWebsiteREFList ,
														@SoHopDongList ,
														@DmPhongBanREFList ,
														@DmBoPhanREFList ,
														@DmNhomLamViecREFList ,
														@TenNhanVienList,
														@TenDangNhap,
														@DmPhongBanREF,
														@DmBoPhanREF,
														@DmNhomLamViecREF,
														@DmChucDanhREF,
														@DmHinhThucQuangCaoList,
														@DmBannerREFList
	)
	
	IF @DonViTinhList <> ''
		SET @FilterString += ' AND DonViTinh IN (' + @DonViTinhList + ')';	
													
	SET @FilterString += ' AND ('
	SET @FilterString += ' ('
	SET @FilterString += dbo.GetSecurityDataByTenDangNhap(@StartDate,@EndDate,@TenDangNhap,'NgayThucHien','TenDangNhap');
	SET @FilterString += ' )'
	
	SET @FilterString += ' OR ('
	SET @FilterString += dbo.GetSecurityWebsiteProduct(@StartDate,@EndDate,@TenDangNhap,'NgayThucHien','TenDangNhap','DmSanPhamREF','DmWebsiteREF');
	SET @FilterString += ' )'
	
	SET @FilterString += ' )'
	
	IF @IsShowNoiBo = 0
		SET @FilterString += ' AND TenMaHopDong NOT LIKE N' + @DauNhay + 'NB%' + @DauNhay
		SET @FilterString += ' AND TenMaHopDong NOT LIKE N' + @DauNhay + 'SH%' + @DauNhay  
		SET @FilterString += ' AND SoHopDong NOT LIKE N' + @DauNhay + 'soha%' + @DauNhay 		

	SET @SqlCommand = '
		SELECT 
			A.DmSanPhamREF, A.TenSanPham, A.SoHopDong, A.DonViTinh, A.HopDongChiTietREF,
			(SELECT SUM(hdct.SoLuong) 
			 FROM HopDongChiTiet hdct 
			 WHERE hdct.HopDongFK = A.HopDongID 
				AND hdct.DmSanPhamREF = A.DmSanPhamREF 
				AND dbo.FormatDonViTinh(hdct.DonViTinh) = A.DonViTinh 
				AND hdct.IsKhuyenMai <> 1 ) AS SoLuongHopDong,
			(SELECT TOP 1 (hdct.ThanhTien) 
			 FROM HopDongChiTiet hdct 
			 WHERE hdct.HopDongFK = A.HopDongID 
				AND hdct.DmSanPhamREF = A.DmSanPhamREF 
				AND dbo.FormatDonViTinh(hdct.DonViTinh) = A.DonViTinh 
				AND hdct.IsKhuyenMai <> 1 ) AS ThanhTienHopDong,
			(SELECT SUM(tc.SoLuongThucChay) 
			 FROM ThucChayDaTinh tc 
			 WHERE tc.HopDongID = A.HopDongID 
				AND DmSanPhamREF = A.DmSanPhamREF 
				AND tc.DonViTinh = A.DonViTinh 
				AND tc.HopDongChiTietREF = A.HopDongChiTietREF
				AND tc.NgayThucHien <= ' + @DauNhay + CONVERT(NVARCHAR(50), @StartDate) + @DauNhay + 
			') AS SoLuongThucChay,
			(SELECT SUM(tc.ThanhTienSauTrietKhauThucChay + tc.GiaTriThayDoi) 
			 FROM ThucChayDaTinh tc 
			 WHERE tc.HopDongID = A.HopDongID 
				AND DmSanPhamREF = A.DmSanPhamREF 
				AND tc.DonViTinh = A.DonViTinh 
				AND tc.HopDongChiTietREF = A.HopDongChiTietREF
				AND tc.NgayThucHien <= ' + @DauNhay + CONVERT(NVARCHAR(50), @EndDate) + @DauNhay + 
			') AS ThanhTienThucChay ,
			SUM(A.SoLuongThucChayKM) AS SoLuongThucChayKM,
			SUM(A.ThanhTienKM) AS ThanhTienKM,
			SUM(A.SoLuongThucChayLechTreoHa) AS SoLuongThucChayLechTreoHa,
			SUM(A.ThanhTienLechTreoHa) AS ThanhTienLechTreoHa
		FROM
		(
			SELECT 		 
				tcdt.DmSanPhamREF, tcdt.TenSanPham, tcdt.HopDongChiTietREF,
				tcdt.SoHopDong, tcdt.HopDongID, tcdt.DonViTinh,								
				SUM(tcdt.SoLuongThucChayKM) AS SoLuongThucChayKM, 
				SUM(tcdt.ThanhTienKM) AS ThanhTienKM,
				SUM(tcdt.SoLuongThucChayLechTreoHa) AS SoLuongThucChayLechTreoHa, 
				SUM(tcdt.ThanhTienLechTreoHa) AS ThanhTienLechTreoHa
			FROM ThucChayDaTinh AS tcdt
			WHERE 1 = 1 
				AND (tcdt.SoLuongThucChayLechTreoHa > 0 OR tcdt.ThanhTienLechTreoHa > 0)' + @FilterString + '
			GROUP BY 
				tcdt.DmSanPhamREF, tcdt.TenSanPham, tcdt.HopDongChiTietREF,
				tcdt.SoHopDong, tcdt.HopDongID, tcdt.DonViTinh
		)A
		GROUP BY 
			A.DmSanPhamREF, A.TenSanPham, A.SoHopDong, A.HopDongID, A.DonViTinh, A.HopDongChiTietREF
		'

	-- Return the result of the function
	RETURN @SqlCommand;

END

```
