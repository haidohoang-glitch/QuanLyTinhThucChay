# Stored Procedure: `usp_Nhanhang_SyncNhanhang_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:09:48.150000
- **Ngày sửa cuối**: 2014-11-19 12:16:46.977000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenNhanHang` | `nvarchar(2048)` | No |
| `@Ghichu` | `nvarchar(512)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |
| `@FromSystem` | `nvarchar(256)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_Nhanhang_SyncNhanhang_v2]
	@TenNhanHang NVARCHAR(1024),
	@Ghichu NVARCHAR(256),
	@CreatedBy NVARCHAR(50),
	@FromSystem NVARCHAR(128)
AS
	SET NOCOUNT ON;
	
	IF (@TenNhanHang <> '')
	BEGIN
	    DECLARE @NhanhangID INT;
	    DECLARE @NewNhanhanID INT;
	    DECLARE @NhanThayDoiID INT;
	    
	    SELECT @NhanhangID = dnh.DmNhanHangID,
	           @NhanThayDoiID = dnh.DmNhanHangThayDoiID
	    FROM   DmNhanHang dnh
	    WHERE  dnh.TenNhanhang = @TenNhanHang
	    
	    
	    IF (@NhanhangID > 0)
	    BEGIN
	        IF ((@NhanThayDoiID IS NULL) OR (@NhanThayDoiID = 0))
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
	            WHERE  dnh.DmNhanHangID = @NhanhangID
	        END
	        
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
	    END
	    ELSE
	    BEGIN
	        INSERT INTO DmNhanHang (TenNhanHang, Ghichu, CreatedAt, CreatedBy, LastModifiedAt,LastModidfiedBy, DeletedStatus, PrintStatus, RecordStatus, FromSystem)
	        VALUES(@TenNhanHang, @Ghichu, GETDATE(), @CreatedBy,GETDATE(),@CreatedBy, 0, 0, 0, @FromSystem )
	        
	        SET @NewNhanhanID = SCOPE_IDENTITY();
	        
	        SELECT dnh.DmNhanHangID, dnh.TenNhanHang, dnh.DmNghanhHangREF,
					@Ghichu AS [TenNghanhHang]
	               /*[TenNghanhHang] = STUFF(
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
	               )*/
	        FROM   DmNhanHang dnh
	        WHERE  dnh.DmNhanHangID = @NewNhanhanID
	               
	    END
	END
	ELSE
	    SELECT 0 AS DmNhanHangID, '' AS TenNhanHang, '0' AS DmNghanhHangREF, '' AS [TenNghanhHang]

```
