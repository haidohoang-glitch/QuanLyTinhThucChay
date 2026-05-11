# Function: `fn_getListNhanHang`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2016-03-28 14:39:28.940000
- **Ngày sửa cuối**: 2016-03-31 14:25:58.600000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(1000)` | Yes |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@TenSanPham` | `nvarchar(100)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@DmLoaiBannerREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		DOANNV
-- Create date: 20160328
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[fn_getListNhanHang]
(
	-- Add the parameters for the function here
	@SoHopDong        NVARCHAR(50),
	@TenSanPham       NVARCHAR(50),
	@DonViTinh        NVARCHAR(50),
	@DmLoaiBannerREF  INT
)
RETURNS NVARCHAR(500)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ResultVar NVARCHAR(500) = ''
	DECLARE @DmNhanHangREF NVARCHAR(200)
	-- Add the T-SQL statements to compute the return value here
	DECLARE Cursor_NhanHangGGFB CURSOR  
	FOR
	    SELECT distinct hdct.NhanHang
	    FROM   HopDong hd
	           INNER JOIN HopDongChiTiet hdct
	                ON  hd.HopDongID = hdct.HopDongFK
	    WHERE  hd.SoHopDong = @SoHopDong
	           AND hdct.TenSanPham = @TenSanPham
	           AND hdct.DonViTinh = @DonViTinh
	           AND hdct.DmLoaiBannerREF = @DmLoaiBannerREF
	
	OPEN Cursor_NhanHangGGFB 
	FETCH NEXT FROM Cursor_NhanHangGGFB INTO @DmNhanHangREF   
	
	WHILE @@FETCH_STATUS = 0
	BEGIN
	    IF @ResultVar = ''
	        SET @ResultVar = @ResultVar + @DmNhanHangREF
	    ELSE
	        SET @ResultVar = @ResultVar + ',' + @DmNhanHangREF
	    
	    FETCH NEXT FROM Cursor_NhanHangGGFB INTO @DmNhanHangREF
	END 
	
	CLOSE Cursor_NhanHangGGFB 
	DEALLOCATE Cursor_NhanHangGGFB
	
	-- Return the result of the function
	RETURN @ResultVar
END

```
