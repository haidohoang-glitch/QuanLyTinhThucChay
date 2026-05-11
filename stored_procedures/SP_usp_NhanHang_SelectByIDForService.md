# Stored Procedure: `usp_NhanHang_SelectByIDForService`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:09:47.273000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.407000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangID` | `varchar(1000)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_NhanHang_SelectByIDForService]
	@DmNhanHangID VARCHAR(1000)
AS
BEGIN
	SET NOCOUNT ON;
	
	DECLARE @Result NVARCHAR(MAX);
	DECLARE @NhanThayDoiID INT;
	
	IF (@DmNhanHangID <> '')
	BEGIN
	    SELECT @NhanThayDoiID = dnh.DmNhanHangThayDoiID
	    FROM   DmNhanHang dnh
	    WHERE  dnh.DmNhanHangID = @DmNhanHangID
	    
	    IF (@NhanThayDoiID > 0)
	    BEGIN
	        SELECT @NhanThayDoiID AS DmNhanHangID, dnh.TenNhanHang, dnh.DmNghanhHangREF,
	               [TenNghanhHang] = STUFF(
	                   (
	                       SELECT ';' + md.TenNghanhHang
	                       FROM   DmNghanhHang md
	                       WHERE  md.DeletedStatus <> 1
	                              AND md.DmNghanhHangID IN (SELECT *
	                                                        FROM   dbo.Split(dnh.DmNghanhHangREF, ','))
	                                  FOR XML PATH(''), TYPE
	                   ).value('.', 'NVARCHAR(MAX)'),
	                   1,
	                   1,
	                   ''
	               )
	        FROM   DmNhanHang dnh
	        WHERE  dnh.DmNhanHangID = @NhanThayDoiID
	    END
	    ELSE
	    BEGIN
	        SELECT dnh.DmNhanHangID, dnh.TenNhanHang, dnh.DmNghanhHangREF,
	               [TenNghanhHang] = STUFF(
	                   (
	                       SELECT ';' + md.TenNghanhHang
	                       FROM   DmNghanhHang md
	                       WHERE  md.DeletedStatus <> 1
	                              AND md.DmNghanhHangID IN (SELECT *
	                                                        FROM   dbo.Split(dnh.DmNghanhHangREF, ','))
	                                  FOR XML PATH(''), TYPE
	                   ).value('.', 'NVARCHAR(MAX)'),
	                   1,
	                   1,
	                   ''
	               )
	        FROM   DmNhanHang dnh
	        WHERE  dnh.DmNhanHangID = @DmNhanHangID
	    END
	END
	ELSE
		SELECT 0 AS DmNhanHangID, '' AS TenNhanHang, '0' AS DmNghanhHangREF, '' AS [TenNghanhHang]
END

```
