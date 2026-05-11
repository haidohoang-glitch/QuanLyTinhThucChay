# Function: `GetDieuKienQuanLyByTenDangNhap`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-09-25 17:01:10.200000
- **Ngày sửa cuối**: 2014-10-14 10:39:36.707000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@DmPhongBanREF` | `int(4)` | No |
| `@DmBoPhanREF` | `int(4)` | No |
| `@DmNhomlamViecREF` | `int(4)` | No |
| `@DmChucDanhREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[GetDieuKienQuanLyByTenDangNhap]
(
	-- Add the parameters for the function here
	@TenDangNhap NVARCHAR(50),
	@DmPhongBanREF int,
	@DmBoPhanREF int,
	@DmNhomlamViecREF int,
	@DmChucDanhREF int
	
)
RETURNS nvarchar(4000)
AS
BEGIN

	-- Declare the return variable here
	DECLARE @Sql NVARCHAR(4000)
	DECLARE @DauNhay NVARCHAR(50)
		
	SET @DauNhay=''''
	
	SET @Sql= 'TenDangNhap = ' + @DauNhay + @TenDangNhap +  @DauNhay
			
	IF (@DmChucDanhREF = 3 OR @DmChucDanhREF = 6) -- Trưởng phòng, phó phòng
	BEGIN
		SET @Sql= @Sql + ' OR ' + 'DmPhongBanREF = ' + Convert(nvarchar(50),@DmPhongBanREF)	 
	END
	ELSE IF (@DmChucDanhREF = 7) -- Trưởng bộ phận
	BEGIN
		SET @Sql= @Sql + ' OR ' + 'DmBoPhanREF = ' + Convert(nvarchar(50),@DmBoPhanREF)
	END
	ELSE IF (@DmChucDanhREF = 1) -- Trưởng nhóm
	BEGIN
		SET @Sql= @Sql + ' OR ' +'DmNhomlamViecREF = ' + Convert(nvarchar(50),@DmNhomlamViecREF)
	END
							
	  
	-- Return the result of the function
	RETURN @Sql

END

```
