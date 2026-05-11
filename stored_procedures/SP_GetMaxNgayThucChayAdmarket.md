# Stored Procedure: `GetMaxNgayThucChayAdmarket`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-07-17 10:00:50.700000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.263000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AdmarketProductID` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[GetMaxNgayThucChayAdmarket]
-- Add the parameters for the stored procedure here
	@AdmarketProductID NVARCHAR(50)
AS
BEGIN
	DECLARE @SQLCommand NVARCHAR(400)
	DECLARE @AdmarketProductIDTemp NVARCHAR(50)
	SET @AdmarketProductIDTemp = @AdmarketProductID
	
	SET @AdmarketProductIDTemp = (
        CASE @AdmarketProductID
             WHEN '5001' THEN '144'
             WHEN '5002' THEN '299'
             WHEN '5003' THEN '337'
             WHEN '5004' THEN '375'
             else
             @AdmarketProductID 
        END
    ) 
	
	SET @SQLCommand = 'SELECT MAX(NgayThucHien) FROM dbo.ThucChayDaTinh WHERE DmSanPhamREF IN (' + @AdmarketProductIDTemp + ')'
	
	IF(@AdmarketProductID = '5004')
	BEGIN
		SET @SQLCommand += ' AND DmHinhThucQuangCao = 26'
	END
	
	EXEC (@SQLCommand)
END

```
