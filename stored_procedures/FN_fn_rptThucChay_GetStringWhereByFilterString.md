# Function: `fn_rptThucChay_GetStringWhereByFilterString`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-03-27 17:42:58
- **Ngày sửa cuối**: 2015-03-27 17:42:58

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar` | Yes |
| `@sWhere` | `nvarchar(1000)` | No |
| `@DmSanPhamREFList` | `nvarchar(1000)` | No |
| `@DmWebsiteREFList` | `nvarchar(1000)` | No |
| `@SoHopDongList` | `nvarchar(1000)` | No |
| `@PhongBanREFList` | `nvarchar(1000)` | No |
| `@BoPhanREFList` | `nvarchar(1000)` | No |
| `@NhomREFList` | `nvarchar(1000)` | No |
| `@TenNhanVienList` | `nvarchar(1000)` | No |
| `@DmHinhThucQuangCaoList` | `nvarchar(1000)` | No |
| `@DmBannerREFList` | `nvarchar(1000)` | No |
| `@DonViTinhList` | `nvarchar(1000)` | No |
| `@sWhereSecurity` | `nvarchar(1000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
-- select [dbo].[fn_rptThucChay_GetStringWhereByFilterString] ('1=1','','','','','','','','','','',' AND 1=1')
CREATE FUNCTION [dbo].[fn_rptThucChay_GetStringWhereByFilterString]
(
	@sWhere                 NVARCHAR(500),
    @DmSanPhamREFList		NVARCHAR(500),
	@DmWebsiteREFList		NVARCHAR(500),
	@SoHopDongList			NVARCHAR(500),
	@PhongBanREFList		NVARCHAR(500),
	@BoPhanREFList			NVARCHAR(500),
	@NhomREFList			NVARCHAR(500),
	@TenNhanVienList		NVARCHAR(500),
	@DmHinhThucQuangCaoList NVARCHAR(500),
	@DmBannerREFList		NVARCHAR(500),
	@DonViTinhList			NVARCHAR(500),
	@sWhereSecurity			NVARCHAR(500)
)
RETURNS NVARCHAR(MAX)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @sWhereChay NVARCHAR(MAX);
	SET @sWhereChay =  '1=1 '
	-- Add the T-SQL statements to compute the return value here
	IF @DmSanPhamREFList <> ''
		SET @sWhereChay+= ' AND DmSanPhamREF in (' + @DmSanPhamREFList + ')'
		
	IF @DmWebsiteREFList <> ''
		SET @sWhereChay+= ' AND DmWebsiteREF in (' + @DmWebsiteREFList + ')'
		
	IF @PhongBanREFList <>  ''
		SET @sWhereChay+= ' AND PhongBanREF in (' + @PhongBanREFList + ')'
		
	IF @BoPhanREFList <>''
		SET @sWhereChay+= ' AND BoPhanREF in (' + @BoPhanREFList + ')'
		
	IF @NhomREFList <>''
		SET @sWhereChay+= ' AND NhomREF in (' + @NhomREFList + ')'
		
	IF @DmHinhThucQuangCaoList <> ''
		SET @sWhereChay+= ' AND DmHinhThucQuangCaoREF in (' + @DmHinhThucQuangCaoList + ')'
		
	IF @DmBannerREFList <> ''
		SET @sWhereChay+= ' AND DmViTriBannerREF in (' + @DmBannerREFList + ')'
		
	IF @SoHopDongList <> ''
		SET @sWhereChay+= ' AND SoHopDong in (' + @SoHopDongList + ')'
		
	IF @TenNhanVienList <> ''
		SET @sWhereChay+= ' AND UserName in (' + @TenNhanVienList + ')'
		
	IF @DonViTinhList <> ''
		SET @sWhereChay+= ' AND TenDonViTinh in (' + @DonViTinhList + ')'
		
	-- Return the result of the function
	SET @sWhereChay += ' AND ' + @sWhere +@sWhereSecurity
	
	return @sWhereChay;

END

```
