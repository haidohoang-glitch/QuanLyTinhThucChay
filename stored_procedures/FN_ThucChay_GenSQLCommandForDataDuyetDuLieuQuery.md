# Function: `ThucChay_GenSQLCommandForDataDuyetDuLieuQuery`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-11-09 11:47:08.377000
- **Ngày sửa cuối**: 2014-10-14 10:39:33.330000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `varchar` | Yes |
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
| `@IsPheDuyet` | `int(4)` | No |
| `@IsNoiBo` | `int(4)` | No |
| `@DmHinhThucQuangCaoList` | `nvarchar(400)` | No |
| `@DmBannerREFList` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-28
-- Description:	ThucChay_GenSQLCommandForQuery 
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GenSQLCommandForDataDuyetDuLieuQuery] 
(
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
	@IsPheDuyet INT,
	@IsNoiBo INT,
	@DmHinhThucQuangCaoList NVARCHAR(200),
	@DmBannerREFList NVARCHAR(200)
)
RETURNS VARCHAR(MAX)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Sql NVARCHAR(MAX)
	DECLARE @DauNhay VARCHAR(50)
	DECLARE @FilterString VARCHAR(4000);
	DECLARE @ChucDanhID INT
	DECLARE @GroupPermission INT;
	DECLARE @FixValueName NVARCHAR(50)
	DECLARE @AdmarketValueName NVARCHAR(50)
	
	SET @DauNhay = ''''
	SET @ChucDanhID = dbo.NhanSuGetChucDanhByNhanVien(@TenDangNhap)
	SET @GroupPermission = dbo.NhanSuCheckGroupPermisstion(@TenDangNhap)
	
	SET @FixValueName = @DauNhay + 'Management' + @DauNhay	
	SET @AdmarketValueName = @DauNhay + '-' + @DauNhay
	
	IF @IsPheDuyet = -1
		SET @FilterString = ''
	ELSE
		SET @FilterString = ' AND IsPheDuyet = ' + CONVERT(NVARCHAR(50),@IsPheDuyet) 
		
	IF @IsNoiBo = 1
		SET @FilterString += '' 
	ELSE IF @IsNoiBo = 0
		SET @FilterString += ' AND (UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'NB%' + @DauNhay + ' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'%SH%' + @DauNhay + ' 
		AND SoHopDong NOT LIKE ' + @DauNhay + '%soha%' + @DauNhay + ')'
	
	SET @FilterString = @FilterString + ' AND DangSuDung NOT IN (5001,5002,5003) AND DmWebsiteREF IN (134,182,56,137,254,85) AND '
	SET @FilterString = @FilterString + dbo.GetThucChayFilterString(
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

	SET @Sql = '
		SELECT
			A.DmSanPhamREF, A.TenSanPham, A.SoHopDong,A.HopDongChiTietREF, 
			A.NgayThucHien, A.NgayKyHopDong, 
			A.DonViTinh,A.isKhuyenMai, A.LechBooking,
			A.TenWebsite,A.DmWebsiteREF, A.TenPhongBan, A.DmPhongBanREF, A.TenBoPhan, A.DmBoPhanREF, 
			A.TenNhomLamViec, 
			A.DmNhomLamViecREF,
			A.SysNhanVienREF, A.TenDangNhap,TenNhanVien,
			CAST(A.SoLuongHopDongNoiBo AS BIGINT) AS SoLuongHopDongNoiBo, 
			CAST(A.SoLuongHopDongKhuyenMai AS BIGINT) AS SoLuongHopDongKhuyenMai,
			CAST(A.SoLuongHopDongThucThu AS BIGINT) AS SoLuongHopDongThucThu,
			CAST(A.SoLuongThucChayNoiBo AS BIGINT) AS SoLuongThucChayNoiBo, 
			CAST(A.SoLuongThucChayKhuyenMai AS BIGINT) AS SoLuongThucChayKhuyenMai, 
			CAST(A.SoLuongThucChayThucThu AS BIGINT) AS SoLuongThucChayThucThu,
			A.ThanhTienThucChayNoiBo, A.ThanhTienThucChayKhuyenMai, A.ThanhTienThucChaySauChietKhau,
			(A.ThanhTienThucThu + A.GiaTriThayDoi) AS ThanhTienThucChayThucThu
		FROM
		(
			SELECT
				DmSanPhamREF, TenSanPham, SoHopDong,HopDongChiTietREF, 
				MAX(NgayThucHien) AS NgayThucHien,
				MAX(NgayKyHopDong) AS NgayKyHopDong,
				TenWebsite, DmWebsiteREF, 
				CASE WHEN DmPhongBanREF > 0 THEN TenPhongBan
					 WHEN DmPhongBanREF = 0 THEN ' + @FixValueName + '
					 ELSE ' + @AdmarketValueName + '
				END AS TenPhongBan, 
				DmPhongBanREF, 
				CASE WHEN DmBoPhanREF > 0 THEN TenBoPhan
					 WHEN DmBoPhanREF = 0 THEN ' + @FixValueName + '
					 ELSE ' + @AdmarketValueName + '   
				END AS TenBoPhan, 
				DmBoPhanREF, 
				CASE WHEN DmNhomLamViecREF > 0 THEN TenNhomLamViec
					 WHEN DmNhomLamViecREF = 0 THEN ' + @FixValueName + '
					 ELSE ' + @AdmarketValueName + '   
				END AS TenNhomLamViec, 
				DmNhomLamViecREF,
				SysNhanVienREF,TenDangNhap,TenNhanVien,
				dbo.FormatDonViTinh(DonViTinh) AS DonViTinh,isKhuyenMai,
				CASE WHEN SoLuongDotChayHD <> SoLuongDotChayBooking THEN ' + @DauNhay + 'True' + @DauNhay + '
								ELSE ' + @DauNhay + 'False' + @DauNhay + ' 
				END AS LechBooking,
				SUM(ISNULL(GiaTriThayDoi,0)) AS GiaTriThayDoi,
				CASE WHEN (UPPER(SoHopDong) LIKE ' + @DauNhay +'NB%' + @DauNhay +' OR UPPER(SoHopDong) LIKE ' + @DauNhay +'%SH%' + @DauNhay +' OR UPPER(SoHopDong) LIKE ' + @DauNhay +'%SOHA%' + @DauNhay +') THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
					ELSE 0
				END AS SoLuongHopDongNoiBo,
				CASE WHEN ThanhTienKM > 0 THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
					ELSE 0
				END AS SoLuongHopDongKhuyenMai,
				CASE WHEN (ThanhTienKM = 0 AND UPPER(SoHopDong) NOT LIKE '+ @DauNhay + 'NB%'+ @DauNhay +' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'%SH%' + @DauNhay +' AND UPPER(SoHopDong) NOT LIKE ' + @DauNhay +'%SOHA%' + @DauNhay +') THEN ISNULL(MAX(CAST(SoLuong AS BIGINT)),0) 
					ELSE 0
				END AS SoLuongHopDongThucThu,
				CASE WHEN (UPPER(SoHopDong) LIKE '+ @DauNhay +'NB%'+ @DauNhay +' OR UPPER(SoHopDong) LIKE '+ @DauNhay +'%SH%'+ @DauNhay +' OR UPPER(SoHopDong) LIKE '+ @DauNhay +'%SOHA%'+ @DauNhay +') THEN ISNULL(SUM(CAST(SoLuongThucChay AS BIGINT)),0) 
					ELSE 0
				END AS SoLuongThucChayNoiBo,
				ISNULL(SUM(CAST(SoLuongThucChayKM AS BIGINT)),0) AS SoLuongThucChayKhuyenMai,
				CASE WHEN (UPPER(SoHopDong) NOT LIKE '+ @DauNhay +'NB%'+ @DauNhay +' AND UPPER(SoHopDong) NOT LIKE '+ @DauNhay +'%SH%'+ @DauNhay +' AND UPPER(SoHopDong) NOT LIKE '+ @DauNhay +'%SOHA%'+ @DauNhay +') THEN ISNULL(SUM(CAST(SoLuongThucChay AS BIGINT)),0) 
					ELSE 0
				END AS SoLuongThucChayThucThu,
				CASE WHEN (UPPER(SoHopDong) LIKE '+ @DauNhay +'NB%'+ @DauNhay +' OR UPPER(SoHopDong) LIKE '+ @DauNhay +'%SH%'+ @DauNhay +' OR UPPER(SoHopDong) LIKE '+ @DauNhay +'%SOHA%'+ @DauNhay +') THEN ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) 
					ELSE 0
				END AS ThanhTienThucChayNoiBo,
				ISNULL(SUM(ThanhTienKM),0) AS ThanhTienThucChayKhuyenMai,			
				ISNULL(SUM(ThanhTienSauTrietKhauThucChay),0) AS ThanhTienThucChaySauChietKhau,
				CASE WHEN (UPPER(SoHopDong) NOT LIKE '+ @DauNhay +'NB%'+ @DauNhay +' AND UPPER(SoHopDong) NOT LIKE '+ @DauNhay +'%SH%'+ @DauNhay +' AND UPPER(SoHopDong) NOT LIKE '+ @DauNhay +'%SOHA%'+ @DauNhay +') THEN SUM(ISNULL(ThanhTienSauTrietKhauThucChay,0))  
					ELSE 0
				END AS ThanhTienThucThu
			FROM ThucChayDaTinh 
			WHERE 1=1 '
	SET @Sql += @FilterString
	SET @Sql += '
				AND TrangThaiHopDong <> 3 
			GROUP BY DmSanPhamREF,TenSanPham,SoHopDong,HopDongChiTietREF,dbo.FormatDonViTinh(DonViTinh),SoHopDong,ThanhTienKM,
				isKhuyenMai,SoLuongDotChayHD,SoLuongDotChayBooking,TenWebsite,DmWebsiteREF,TenPhongBan,DmPhongBanREF,
				TenBoPhan, DmBoPhanREF, TenNhomLamViec, DmNhomLamViecREF, SysNhanVienREF, TenDangNhap,TenNhanVien,NgayThucHien
		)A
		WHERE  (SoLuongThucChayNoiBo <> 0 OR SoLuongThucChayKhuyenMai <> 0 OR SoLuongThucChayThucThu <> 0 
						OR ThanhTienThucChayNoiBo <> 0 OR ThanhTienThucChayKhuyenMai <> 0 OR ThanhTienThucChaySauChietKhau <> 0 
						OR GiaTriThayDoi <> 0)
				AND (ThanhTienThucChayNoiBo + ThanhTienThucChaySauChietKhau + GiaTriThayDoi) > 1000
	'

	-- Return the result of the function
	RETURN @Sql

END

```
