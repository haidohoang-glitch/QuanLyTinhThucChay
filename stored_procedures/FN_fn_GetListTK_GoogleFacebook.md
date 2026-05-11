# Function: `fn_GetListTK_GoogleFacebook`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-07-16 14:53:28.957000
- **Ngày sửa cuối**: 2015-07-16 14:53:28.957000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(400)` | Yes |
| `@HopDongID` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[fn_GetListTK_GoogleFacebook]
(
	-- Add the parameters for the function here
	@HopDongID INT,
	@DonViTinh NVARCHAR(50)
)
RETURNS NVARCHAR(200)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ResultVar NVARCHAR(200) SET @ResultVar = ''
	DECLARE @name NVARCHAR(50)
	-- Add the T-SQL statements to compute the return value here
	DECLARE db_cursor CURSOR FOR  
	SELECT hdct.TK_AdMarket 
	FROM HopDong hd INNER JOIN HopDongChiTiet hdct
	ON hd.HopDongID= hdct.HopDongFK
	WHERE hdct.DmSanPhamREF IN (306,423)
	AND hdct.DeletedStatus <> 1
	AND hdct.TrangthaiThucChay <> 3
	AND hd.DeletedStatus <> 1
	AND hd.TrangThaiHopDong <> 3
	AND hd.HopDongID = @HopDongID
	AND hdct.DonViTinh = @DonViTinh
	
	OPEN db_cursor   
	FETCH NEXT FROM db_cursor INTO @name   

	WHILE @@FETCH_STATUS = 0   
	BEGIN   
		   IF @ResultVar = ''
		   BEGIN
		   	   SET @ResultVar = @name
		   END
		   ELSE
		   	BEGIN
		   		IF CHARINDEX(@name,@ResultVar) > 0
		   		SET @ResultVar = @ResultVar
		   		ELSE SET @ResultVar = @ResultVar + ','+ @name
		   	END

		   FETCH NEXT FROM db_cursor INTO @name   
	END   

	CLOSE db_cursor   
	DEALLOCATE db_cursor

	-- Return the result of the function
	RETURN @ResultVar

END

```
