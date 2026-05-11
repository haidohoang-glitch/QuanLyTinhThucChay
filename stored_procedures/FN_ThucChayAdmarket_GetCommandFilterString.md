# Function: `ThucChayAdmarket_GetCommandFilterString`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-12-25 17:19:23.640000
- **Ngày sửa cuối**: 2014-10-14 10:39:28.840000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar` | Yes |
| `@GroupFieldName` | `nvarchar(100)` | No |
| `@DmSanPhamREFList` | `nvarchar(8000)` | No |
| `@DmWebsiteREFList` | `nvarchar(8000)` | No |
| `@SoHopDongList` | `nvarchar(8000)` | No |
| `@DmPhongBanREFList` | `varchar(2000)` | No |
| `@DmBoPhanREFList` | `varchar(2000)` | No |
| `@DmNhomLamViecREFList` | `varchar(2000)` | No |
| `@TenNhanVienList` | `varchar(2000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-12-18
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChayAdmarket_GetCommandFilterString]
(
	@GroupFieldName NVARCHAR(50),
	@DmSanPhamREFList nvarchar(4000),
	@DmWebsiteREFList nvarchar(4000),
	@SoHopDongList nvarchar(4000),
	@DmPhongBanREFList VARCHAR(2000),
	@DmBoPhanREFList VARCHAR(2000),
	@DmNhomLamViecREFList VARCHAR(2000),
	@TenNhanVienList varchar(2000)
)
RETURNS nvarchar(max)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @SqlFilterString nvarchar(max);
	DECLARE @DauNhay nvarchar(50) = '''';

	SET @SqlFilterString = '';
	
	IF @DmSanPhamREFList <> ''
		SET @SqlFilterString += ' AND DmSanPhamREF IN (' + @DmSanPhamREFList + ')';
		
	IF @DmWebsiteREFList <> '' 
		SET @SqlFilterString += ' AND 1 <> 1';
		
	IF (@GroupFieldName = 'TenNhanVien' AND @SoHopDongList <> '')
		SET @SqlFilterString += ' AND 1 <> 1';
	ELSE IF (@GroupFieldName = 'SoHopDong' AND @SoHopDongList <> '')
		SET @SqlFilterString += ' AND SoHopDong IN (' + @SoHopDongList + ')';

	IF @DmPhongBanREFList <> '' 
	BEGIN
		IF @DmPhongBanREFList = 'NULL'
			SET @SqlFilterString += ' AND DmPhongBanREF IS NULL';
		ELSE
			SET @SqlFilterString += ' AND DmPhongBanREF IN (' + @DmPhongBanREFList + ')';
	END
	
	IF @DmBoPhanREFList <> '' 
	BEGIN
		IF @DmBoPhanREFList = 'NULL'
			SET @SqlFilterString += ' AND DmBoPhanREF IS NULL ';
		ELSE
			SET @SqlFilterString += ' AND DmBoPhanREF IN (' + @DmBoPhanREFList + ')';
	END
		
	IF @DmNhomLamViecREFList <> ''
	BEGIN
		IF @DmNhomLamViecREFList = 'NULL'
			SET @SqlFilterString += ' AND DmNhomLamViecREF IS NULL';
		ELSE
			SET @SqlFilterString += ' AND DmNhomLamViecREF IN (' + @DmNhomLamViecREFList + ')';
	END 
	
	IF @TenNhanVienList <> '' 
		SET @SqlFilterString += ' AND TenDangNhap IN (' + @TenNhanVienList + ')';

	-- Return the result of the function
	RETURN @SqlFilterString;

END
```
