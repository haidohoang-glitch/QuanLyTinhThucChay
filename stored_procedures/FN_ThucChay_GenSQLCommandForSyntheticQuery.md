# Function: `ThucChay_GenSQLCommandForSyntheticQuery`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-09-25 17:01:11.253000
- **Ngày sửa cuối**: 2014-10-14 10:39:33.063000

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
| `@DmHinhThucQuangCaoList` | `nvarchar(400)` | No |
| `@DmBannerREFList` | `nvarchar(400)` | No |
| `@DonViTinhList` | `nvarchar(510)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-09-17
-- Description:	ThucChay_GenSQLCommandForSummeryQuery 
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GenSQLCommandForSyntheticQuery] 
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
	@DmHinhThucQuangCaoList NVARCHAR(200),
	@DmBannerREFList NVARCHAR(200),
	@DonViTinhList		NVARCHAR(255)
)
RETURNS NVARCHAR(MAX)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Sql NVARCHAR(MAX)
	DECLARE @DauNhay NVARCHAR(50)
	DECLARE @FilterString NVARCHAR(4000);
	DECLARE @ChucDanhID INT
	DECLARE @GroupPermission INT;
	DECLARE @FixValueName NVARCHAR(50)
	DECLARE @AdmarketValueName NVARCHAR(50)
	
	SET @DauNhay = ''''
	SET @ChucDanhID = dbo.NhanSuGetChucDanhByNhanVien(@TenDangNhap)
	SET @GroupPermission = dbo.NhanSuCheckGroupPermisstion(@TenDangNhap)
	
	SET @FixValueName = @DauNhay + 'Management' + @DauNhay	
	SET @AdmarketValueName = @DauNhay + '-' + @DauNhay		
																	
	SET @FilterString =  dbo.GetThucChayFilterString(
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
													
	SET @FilterString += ' AND ('
	SET @FilterString += ' ('
	SET @FilterString += dbo.GetSecurityDataByTenDangNhap(@StartDate,@EndDate,@TenDangNhap,'NgayThucHien','TenDangNhap');
	SET @FilterString += ' )'
	
	SET @FilterString += ' OR ('
	SET @FilterString += dbo.GetSecurityWebsiteProduct(@StartDate,@EndDate,@TenDangNhap,'NgayThucHien','TenDangNhap','DmSanPhamREF','DmWebsiteREF');
	SET @FilterString += ' )'
	
	SET @FilterString += ' )'	
	
	IF @DonViTinhList <> ''
		SET @FilterString += ' AND DonViTinh IN (' + @DonViTinhList + ')';
	
	SET @Sql = '
		SELECT * FROM dbo.GetDataThucChayTongHopByParams('+ @DauNhay  + CONVERT(VARCHAR(50),@StartDate) + @DauNhay + ',' + @DauNhay  + CONVERT(VARCHAR(50),@EndDate) + @DauNhay + ')'
		
	SET @Sql += '
		WHERE ' + @FilterString													

	-- Return the result of the function
	RETURN @Sql

END

```
