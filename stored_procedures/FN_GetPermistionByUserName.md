# Function: `GetPermistionByUserName`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-12-25 17:19:26.237000
- **Ngày sửa cuối**: 2014-10-14 10:39:35.970000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `varchar` | Yes |
| `@UserName` | `nvarchar(100)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmPhongBanREF` | `int(4)` | No |
| `@DmBoPhanREF` | `int(4)` | No |
| `@DmNhomLamViecREF` | `int(4)` | No |
| `@DmChucDanhREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-12-04
-- Description:	Get permisstion by 
-- =============================================
-- PRINT dbo.GetPermistionByUserName('quynhvtn','','')
CREATE FUNCTION dbo.GetPermistionByUserName 
(
	-- Add the parameters for the function here
	@UserName NVARCHAR(50),
	@StartDate DATETIME,
	@EndDate DATETIME,
	@DmPhongBanREF INT,
	@DmBoPhanREF INT,
	@DmNhomLamViecREF INT,
	@DmChucDanhREF INT
)
RETURNS VARCHAR(MAX)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @SqlCommand VARCHAR(MAX);
	DECLARE @DauNhay VARCHAR(50);
	--DECLARE @DmPhongBanREF INT, @DmBoPhanREF INT, @DmNhomLamViecREF INT, @DmChucDanhREF INT;
	DECLARE @GroupPermision INT	
	DECLARE @ListWebsiteID VARCHAR(200),@ListSanPhamID VARCHAR(200);
	
	SET @SqlCommand = '';
	SET @GroupPermision = dbo.NhanSuCheckGroupPermisstion(@UserName);
	SET @ListWebsiteID = dbo.GetListWebsiteByNhanVien(@UserName);
	SET @ListSanPhamID = dbo.GetListSanPhamByNhanVien(@UserName); 
	
	IF @GroupPermision <> -1 
	BEGIN
		-- Neu co chuc vu
		SET @SqlCommand = @SqlCommand + dbo.GetDieuKienQuanLyByTenDangNhap(@UserName,@DmPhongBanREF ,@DmBoPhanREF ,@DmNhomlamViecREF ,@DmChucDanhREF)
		
		-- Neu la quan ly Website
		IF @ListWebsiteID <> ''
			SET @SqlCommand = @SqlCommand + ' OR DmWebsiteREF IN (' + @ListWebsiteID + ')';
		-- New la quan ly san pham
		IF @ListSanPhamID <> ''
			SET @SqlCommand = @SqlCommand + ' OR DmSanPhamREF IN ' + @ListSanPhamID + ')'; 
	END;
	-- Return the result of the function
	RETURN @SqlCommand

END

```
