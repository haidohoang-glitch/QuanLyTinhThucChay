# Stored Procedure: `usp_InsertHopDongThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-03 14:33:34.230000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.830000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongThayDoiID` | `int(4)` | No |
| `@HopDongFK` | `int(4)` | No |
| `@LoaiThayDoi` | `int(4)` | No |
| `@NgayThayDoi` | `datetime(8)` | No |
| `@NganhHang` | `nvarchar(400)` | No |
| `@NhanHopDong` | `nvarchar(100)` | No |
| `@GiaTriHopDong` | `float(8)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_InsertHopDongThayDoi]
	@HopDongThayDoiID INT,
	@HopDongFK INT,
	@LoaiThayDoi INT,
	@NgayThayDoi DATETIME,
	@NganhHang NVARCHAR(200),
	@NhanHopDong NVARCHAR(50),
	@GiaTriHopDong FLOAT,
	@CreatedBy NVARCHAR(50),
	@CreatedAt DATETIME,
	@LastModifiedBy NVARCHAR(50),
	@LastModifiedAt DATETIME,
	@DeletedStatus INT,
	@PrintStatus INT,
	@RecordStatus INT
AS
	SET NOCOUNT ON
	IF (
	       EXISTS(
	           SELECT [HopDongFK]
	           FROM   [HopDongThayDoi]
	           WHERE  [HopDongThayDoiID] = @HopDongThayDoiID
	       )
	   )
	    UPDATE [dbo].[HopDongThayDoi]
	    SET    [HopDongFK]         = @HopDongFK,
	           [LoaiThayDoi]       = @LoaiThayDoi,
	           [NgayThayDoi]       = @NgayThayDoi,
	           [NganhHang]         = @NganhHang,
	           [NhanHopDong]       = @NhanHopDong,
	           [GiaTriHopDong]     = @GiaTriHopDong,
	           [LastModifiedBy]    = @LastModifiedBy,
	           [LastModifiedAt]    = @LastModifiedAt,
	           [DeletedStatus]     = @DeletedStatus,
	           [PrintStatus]       = @PrintStatus,
	           [RecordStatus]      = @RecordStatus
	    WHERE  [HopDongThayDoiID]  = @HopDongThayDoiID
	ELSE
	    INSERT INTO [dbo].[HopDongThayDoi]
	      (
	        [HopDongThayDoiID],
	        [HopDongFK],
	        [LoaiThayDoi],
	        [NgayThayDoi],
	        [NganhHang],
	        [NhanHopDong],
	        [GiaTriHopDong],
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
	        @HopDongThayDoiID,
	        @HopDongFK,
	        @LoaiThayDoi,
	        @NgayThayDoi,
	        @NganhHang,
	        @NhanHopDong,
	        @GiaTriHopDong,
	        @CreatedBy,
	        @CreatedAt,
	        @LastModifiedBy,
	        @LastModifiedAt,
	        @DeletedStatus,
	        @PrintStatus,
	        @RecordStatus
	      )

```
