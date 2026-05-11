# Stored Procedure: `Gen_InsertOrUpdate_HopDongHanThanhToanLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-24 09:55:14.553000
- **Ngày sửa cuối**: 2016-03-24 11:45:56.763000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongHanThanhToanLogID` | `int(4)` | No |
| `@HopDongHanThanhToanREF` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@LanThanhToan` | `nvarchar(400)` | No |
| `@NgayThanhToan` | `datetime(8)` | No |
| `@SoTien` | `float(8)` | No |
| `@NgayDuKienXuatHoaDon` | `datetime(8)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@ActionType` | `int(4)` | No |
| `@UserLog` | `nvarchar(400)` | No |
| `@LogTime` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_HopDongHanThanhToanLog]
	@HopDongHanThanhToanLogID INT ,
	@HopDongHanThanhToanREF INT ,
	@HopDongREF INT ,
	@LanThanhToan NVARCHAR(200) ,
	@NgayThanhToan DATETIME ,
	@SoTien FLOAT ,
	@NgayDuKienXuatHoaDon DATETIME ,
	@CreatedAt DATETIME ,
	@CreatedBy NVARCHAR(200) ,
	@LastModifiedAt DATETIME ,
	@LastModifiedBy NVARCHAR(200) ,
	@ActionType INT ,
	@UserLog NVARCHAR(200) ,
	@LogTime DATETIME
AS
BEGIN
	IF (
	       EXISTS(
	           SELECT *
	           FROM   [HopDongHanThanhToanLog]
	           WHERE  [HopDongHanThanhToanLogID] = @HopDongHanThanhToanLogID
	       )
	   )
	    UPDATE [dbo].[HopDongHanThanhToanLog]
	    SET    [HopDongHanThanhToanREF]    = @HopDongHanThanhToanREF,
	           [HopDongREF]                = @HopDongREF,
	           [LanThanhToan]              = @LanThanhToan,
	           [NgayThanhToan]             = @NgayThanhToan,
	           [SoTien]                    = @SoTien,
	           [NgayDuKienXuatHoaDon]      = @NgayDuKienXuatHoaDon,
	           [CreatedAt]                 = @CreatedAt,
	           [CreatedBy]                 = @CreatedBy,
	           [LastModifiedAt]            = @LastModifiedAt,
	           [LastModifiedBy]            = @LastModifiedBy,
	           [ActionType]                = @ActionType,
	           [UserLog]                   = @UserLog,
	           [LogTime]                   = @LogTime
	    WHERE  [HopDongHanThanhToanLogID]  = @HopDongHanThanhToanLogID
	ELSE
	    INSERT INTO [dbo].[HopDongHanThanhToanLog]
	      (
	        [HopDongHanThanhToanLogID],
	        [HopDongHanThanhToanREF],
	        [HopDongREF],
	        [LanThanhToan],
	        [NgayThanhToan],
	        [SoTien],
	        [NgayDuKienXuatHoaDon],
	        [CreatedAt],
	        [CreatedBy],
	        [LastModifiedAt],
	        [LastModifiedBy],
	        [ActionType],
	        [UserLog],
	        [LogTime]
	      )
	    VALUES
	      (
	        @HopDongHanThanhToanLogID,
	        @HopDongHanThanhToanREF,
	        @HopDongREF,
	        @LanThanhToan,
	        @NgayThanhToan,
	        @SoTien,
	        @NgayDuKienXuatHoaDon,
	        @CreatedAt,
	        @CreatedBy,
	        @LastModifiedAt,
	        @LastModifiedBy,
	        @ActionType,
	        @UserLog,
	        @LogTime
	      )
	      
	      IF(@ActionType = 3)
	      BEGIN
	      	UPDATE HopDongHanThanhToan
	      	SET DeletedStatus = 1
	      	, LastModifiedAt = @LogTime
	      	, LastModifiedBy = @UserLog
	      	WHERE HopDongHanThanhToanID = @HopDongHanThanhToanREF
	      END
END
	
```
