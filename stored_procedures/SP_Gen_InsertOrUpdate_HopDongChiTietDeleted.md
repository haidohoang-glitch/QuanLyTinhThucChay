# Stored Procedure: `Gen_InsertOrUpdate_HopDongChiTietDeleted`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-26 09:34:58.940000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.687000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietDeletedID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_HopDongChiTietDeleted]
	@HopDongChiTietDeletedID INT ,
	@HopDongChiTietID INT ,
	@NgayThucHien DATETIME ,
	@CreatedBy NVARCHAR(200) ,
	@CreatedAt DATETIME ,
	@LastModifiedBy NVARCHAR(200) ,
	@LastModifiedAt DATETIME ,
	@DeletedStatus INT ,
	@PrintStatus INT ,
	@RecordStatus INT
AS
BEGIN
	IF (
	       EXISTS(
	           SELECT *
	           FROM   [HopDongChiTietDeleted]
	           WHERE  [HopDongChiTietDeletedID] = @HopDongChiTietDeletedID
	       )
	   )
	    UPDATE [dbo].[HopDongChiTietDeleted]
	    SET    [HopDongChiTietID]         = @HopDongChiTietID,
	           [NgayThucHien]             = @NgayThucHien,
	           [CreatedBy]                = @CreatedBy,
	           [CreatedAt]                = @CreatedAt,
	           [LastModifiedBy]           = @LastModifiedBy,
	           [LastModifiedAt]           = @LastModifiedAt,
	           [DeletedStatus]            = @DeletedStatus,
	           [PrintStatus]              = @PrintStatus,
	           [RecordStatus]             = @RecordStatus
	    WHERE  [HopDongChiTietDeletedID]  = @HopDongChiTietDeletedID
	ELSE
	    INSERT INTO [dbo].[HopDongChiTietDeleted]
	      (
	        [HopDongChiTietDeletedID],
	        [HopDongChiTietID],
	        [NgayThucHien],
	        [CreatedBy],
	        [CreatedAt],
	        [LastModifiedBy],
	        [LastModifiedAt],
	        [DeletedStatus],
	        [PrintStatus],
	        [RecordStatus]
	      )
	    VALUES
	      (
	        @HopDongChiTietDeletedID,
	        @HopDongChiTietID,
	        @NgayThucHien,
	        @CreatedBy,
	        @CreatedAt,
	        @LastModifiedBy,
	        @LastModifiedAt,
	        @DeletedStatus,
	        @PrintStatus,
	        @RecordStatus
	      )
	      
	      UPDATE HopDongChiTiet
	      SET DeletedStatus = 1
	      , LastModifiedBy = @LastModifiedBy
	      , LastModifiedAt = @NgayThucHien
	      WHERE HopDongChiTietID = @HopDongChiTietID
	      	
END

```
