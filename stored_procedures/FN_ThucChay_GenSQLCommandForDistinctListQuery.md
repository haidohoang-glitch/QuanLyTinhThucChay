# Function: `ThucChay_GenSQLCommandForDistinctListQuery`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-10-10 16:52:55.667000
- **Ngày sửa cuối**: 2014-10-14 10:39:33.263000

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
| `@DmHinhThucQuangCaoList` | `nvarchar(400)` | No |
| `@DmBannerREFList` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql

--EXEC [dbo].[ThucChay_GetDistinctDanhMuc]
--	-- Add the parameters for the stored procedure here
--	@GroupFieldName = 'TenSanPham',
--	@StartDate = '1/1/0001 12:00:00 AM',
--	@EndDate = '1/1/0001 12:00:00 AM',
--	@DmSanPhamREFList ='',
--	@DmWebsiteREFList ='',
--	@SoHopDongList ='',
--	@DmPhongBanREFList ='',
--	@DmBoPhanREFList ='',
--	@DmNhomLamViecREFList ='',
--	@TenNhanVienList =''

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GenSQLCommandForDistinctListQuery] 
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
	@DmBannerREFList NVARCHAR(200)
)
RETURNS VARCHAR(MAX)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Sql NVARCHAR(MAX)
	DECLARE @DauNhay NVARCHAR(50)
	DECLARE @FilterString NVARCHAR(4000);
	DECLARE @ChucDanhID INT
	DECLARE @GroupPermission INT;
	
	SET @DauNhay = ''''
	SET @ChucDanhID = dbo.NhanSuGetChucDanhByNhanVien(@TenDangNhap)
	SET @GroupPermission = dbo.NhanSuCheckGroupPermisstion(@TenDangNhap)	
	
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

	SET @Sql = '
		SELECT DISTINCT
				DmSanPhamREF, TenSanPham, SoHopDong,
				TenWebsite, DmWebsiteREF, 
				TenPhongBan, DmPhongBanREF, 
				TenBoPhan, DmBoPhanREF, 
				TenNhomLamViec, DmNhomLamViecREF,
				TenDangNhap,TenNhanVien
			FROM ThucChayDaTinh 
			WHERE '
		SET @Sql += @FilterString
		SET @Sql += '
				AND TrangThaiHopDong <> 3
				AND (ThanhTienSauTrietKhauThucChay > 0 OR ThanhTienKM > 0 OR GiaTriThayDoi <> 0 OR SoLuongThucChay > 0)
	'

	-- Return the result of the function
	RETURN @Sql

END

```
