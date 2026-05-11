# Function: `ThucChay_GenSQLCommandForDistinctLechTreoHaQuery`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-10-10 16:52:55.890000
- **Ngày sửa cuối**: 2014-10-14 10:39:33.297000

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

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-09-02
-- Description:	ThucChay_GenSQLCommandForQuery 
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GenSQLCommandForDistinctLechTreoHaQuery] 
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
	@DmChucDanhREF int
)
RETURNS VARCHAR(MAX)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Sql VARCHAR(MAX)
	DECLARE @DauNhay VARCHAR(50)
	DECLARE @FilterString VARCHAR(4000);
	DECLARE @ChucDanhID INT
	DECLARE @GroupPermission INT;
	DECLARE @DmHinhThucQuangCaoList NVARCHAR(200) = '';
	DECLARE @DmBannerREFList NVARCHAR(200) = '';
	
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

	SET @Sql = '
		SELECT DISTINCT
				DmSanPhamREF, TenSanPham, SoHopDong,
				TenWebsite, DmWebsiteREF, 
				TenPhongBan, DmPhongBanREF, 
				TenBoPhan, DmBoPhanREF, 
				TenNhomLamViec, DmNhomLamViecREF,
				TenDangNhap,TenNhanVien
			FROM ThucChayDaTinh 
			WHERE 1=1 AND '
		SET @Sql += @FilterString
		SET @Sql += '
				AND TrangThaiHopDong <> 3
				AND SoLuongThucChayLechTreoHa > 0
	'

	-- Return the result of the function
	RETURN @Sql

END

```
