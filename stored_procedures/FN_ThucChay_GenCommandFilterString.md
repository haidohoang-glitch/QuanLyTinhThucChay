# Function: `ThucChay_GenCommandFilterString`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-07-17 08:28:08.310000
- **Ngày sửa cuối**: 2014-10-14 10:39:33.633000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar` | Yes |
| `@DmSanPhamREFList` | `nvarchar(4000)` | No |
| `@DmWebSiteREFList` | `nvarchar(4000)` | No |
| `@SoHopDongList` | `nvarchar(400)` | No |
| `@DmPhongBanREFList` | `nvarchar(4000)` | No |
| `@DmBoPhanREFList` | `nvarchar(4000)` | No |
| `@DmNhomLamViecREFList` | `nvarchar(4000)` | No |
| `@TenNhanVienList` | `nvarchar(4000)` | No |
| `@DmHinhThucQuangCaoList` | `nvarchar(510)` | No |
| `@DmBannerREFList` | `nvarchar(510)` | No |
| `@DonViTinhList` | `nvarchar(510)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GenCommandFilterString]
(
	-- Add the parameters for the function here
	@DmSanPhamREFList NVARCHAR(2000),
	@DmWebSiteREFList NVARCHAR(2000),
	@SoHopDongList NVARCHAR(200),
	@DmPhongBanREFList NVARCHAR(2000),
	@DmBoPhanREFList NVARCHAR(2000),
	@DmNhomLamViecREFList NVARCHAR(2000),
	@TenNhanVienList Nvarchar(2000),
	@DmHinhThucQuangCaoList	NVARCHAR(255),
	@DmBannerREFList		NVARCHAR(255),
	@DonViTinhList			NVARCHAR(255)
)
RETURNS NVARCHAR(MAX)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @FilterSQLCommand NVARCHAR(MAX);
	SET @FilterSQLCommand = '';

	if(@DmSanPhamREFList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and A.DmSanPhamREF in (' + @DmSanPhamREFList + ') 
			AND B.DmSanPhamREF IN (' + @DmSanPhamREFList + ')'
	if(@DmWebsiteREFList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and A.DmWebsiteREF in (' + @DmWebsiteREFList + ') 
			AND B.DmWebsiteREF IN (' + @DmWebSiteREFList + ')'				
	if(@SoHopDongList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and A.SoHopDong in (' + @SoHopDongList + ') 
			AND B.SoHopDong IN (' + @SoHopDongList + ')'
	if(@DmPhongBanREFList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and B.DmPhongBanREF in (' + @DmPhongBanREFList + ')' 
	if(@DmBoPhanREFList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and B.DmBoPhanREF in (' + @DmBoPhanREFList + ')' 
	if(@DmNhomLamViecREFList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and B.DmNhomLamViecREF in (' + @DmNhomLamViecREFList + ')'
		
	IF @TenNhanVienList <> ''
		SET @FilterSQLCommand += ' AND B.TenDangNhap IN (' + @TenNhanVienList + ')'
	
	IF @DmHinhThucQuangCaoList <> '' AND @DmHinhThucQuangCaoList <> '-1'
		SET @FilterSQLCommand += ' AND DmHinhThucQuangCao IN (' + @DmHinhThucQuangCaoList + ')';
		
	IF @DmBannerREFList <> ''
		SET @FilterSQLCommand += ' AND DmViTriREF IN (' + @DmBannerREFList + ')';
		
	IF @DonViTinhList <> ''	
		SET @FilterSQLCommand += ' AND DonViTinh IN (' + @DonViTinhList + ')';	
		
	-- Return the result of the function
	RETURN @FilterSQLCommand

END


```
