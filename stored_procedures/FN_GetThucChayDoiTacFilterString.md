# Function: `GetThucChayDoiTacFilterString`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-11-09 11:47:07.103000
- **Ngày sửa cuối**: 2014-10-14 10:39:35.270000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREFList` | `nvarchar(8000)` | No |
| `@DmWebsiteREFList` | `nvarchar(8000)` | No |
| `@SoHopDongList` | `nvarchar(8000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-16
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[GetThucChayDoiTacFilterString]
(
	-- Add the parameters for the function here
	@StartDate datetime,
	@EndDate datetime,
	@DmSanPhamREFList nvarchar(4000),
	@DmWebsiteREFList nvarchar(4000),
	@SoHopDongList nvarchar(4000),
	@TenDangNhap NVARCHAR(50)
)
RETURNS NVARCHAR(4000)
AS
BEGIN
	Declare @DauNhay nvarchar(50)
	Declare @FilterSQLCommand nvarchar(4000)
	DECLARE @ChucDanhID INT
	DECLARE @GroupPermission INT;
	DECLARE @PhongID INT, @BoPhanID INT, @NhomLamViecID INT
	DECLARE @ListWebsiteID nvarchar(200), @ListSanPhamID nvarchar(200), @ListTenNhanVien nvarchar(2000)
	DECLARE @ToUserName NVARCHAR(50), @ToanTu nvarchar(50)
	
	SET @ToUserName = (SELECT ToUserName FROM MappingUser A WHERE A.FromUserName = @TenDangNhap)
	
	IF @ToUserName IS NOT NULL
		SET @TenDangNhap = @ToUserName
	
	SET @GroupPermission = dbo.NhanSuCheckGroupPermisstion(@TenDangNhap)
	
	set @DauNhay = ''''
	SET @ListWebsiteID = dbo.GetListWebsiteByNhanVien(@TenDangNhap)
	
	set @FilterSQLCommand = ' AND CONVERT(DATE,NgayThucHien) Between ' + @DauNhay + Convert(nvarchar(50),@StartDate) + @DauNhay + ' and '+ @DauNhay + Convert(nvarchar(50),@EndDate)+@DauNhay
	
	SET @FilterSQLCommand += ' AND DmWebsiteREF IN (134,182,56,137,254,85) '
	
	--Set quyen theo dieu kien tim kiem	
	if(@DmSanPhamREFList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and DmSanPhamREF in (' + @DmSanPhamREFList + ')'
	if(@DmWebsiteREFList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and DmWebsiteREF in (' + @DmWebsiteREFList + ')'				
	if(@SoHopDongList <> '')
		set @FilterSQLCommand = @FilterSQLCommand + ' and SoHopDong in (' + @SoHopDongList + ')'
		
	--IF @TenDangNhap <> ''
	--	SET @FilterSQLCommand += ' AND TenDangNhap IN (' + @TenDangNhap + ')'
	if(@GroupPermission <> -1)		
	BEGIN		
		if(@ListWebsiteID <> '') set @FilterSQLCommand = @FilterSQLCommand + ' AND (DmWebsiteREF in (' + @ListWebsiteID + '))'
		
		IF(@ListWebsiteID='') SET @FilterSQLCommand = @FilterSQLCommand + ' AND TenDangNhap = ' + @DauNhay + @TenDangNhap + @DauNhay;
	END		
	-- Return the result of the function
	RETURN @FilterSQLCommand

END


```
