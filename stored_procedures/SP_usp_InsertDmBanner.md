# Stored Procedure: `usp_InsertDmBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-10-24 14:36:13.713000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.237000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmBannerID` | `int(4)` | No |
| `@TenBanner` | `nvarchar(100)` | No |
| `@TenBanner_boxapp` | `nvarchar(400)` | No |
| `@LoaiSanPham` | `int(4)` | No |
| `@Active` | `int(4)` | No |
| `@NgayBatDau` | `datetime(8)` | No |
| `@NgayKetThuc` | `datetime(8)` | No |
| `@MoTa` | `nvarchar(8000)` | No |
| `@TenFile` | `nvarchar(400)` | No |
| `@Width` | `nvarchar(40)` | No |
| `@Height` | `nvarchar(40)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_InsertDmBanner]
	@DmBannerID INT,
	@TenBanner NVARCHAR(50),
	@TenBanner_boxapp NVARCHAR(200),
	@LoaiSanPham INT,
	@Active INT,
	@NgayBatDau DATETIME,
	@NgayKetThuc DATETIME,
	@MoTa NVARCHAR(4000),
	@TenFile NVARCHAR(200),
	@Width NVARCHAR(20),
	@Height NVARCHAR(20),
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
	           SELECT [TenBanner]
	           FROM   dbo.DmBanner
	           WHERE  DmBannerID = @DmBannerID
	       )
	   )
	    UPDATE [dbo].[DmBanner]
	    SET    [TenBanner]         = @TenBanner,
	           [TenBanner_boxapp]  = @TenBanner_boxapp,
	           [LoaiSanPham]       = @LoaiSanPham,
	           [Active]            = @Active,
	           [NgayBatDau]        = @NgayBatDau,
	           [NgayKetThuc]       = @NgayKetThuc,
	           [MoTa]              = @MoTa,
	           [TenFile]           = @TenFile,
	           [Width]             = @Width,
	           [Height]            = @Height,
	           [LastModifiedBy]    = @LastModifiedBy,
	           [LastModifiedAt]    = @LastModifiedAt,
	           [DeletedStatus]     = @DeletedStatus,
	           [PrintStatus]       = @PrintStatus,
	           [RecordStatus]      = @RecordStatus
	    WHERE  [DmBannerID]        = @DmBannerID
	ELSE
	    INSERT INTO [dbo].[DmBanner]
	      (
	        [DmBannerID],
	        [TenBanner],
	        [TenBanner_boxapp],
	        [LoaiSanPham],
	        [Active],
	        [NgayBatDau],
	        [NgayKetThuc],
	        [MoTa],
	        [TenFile],
	        [Width],
	        [Height],
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
	        @DmBannerID,
	        @TenBanner,
	        @TenBanner_boxapp,
	        @LoaiSanPham,
	        @Active,
	        @NgayBatDau,
	        @NgayKetThuc,
	        @MoTa,
	        @TenFile,
	        @Width,
	        @Height,
	        @CreatedBy,
	        @CreatedAt,
	        @LastModifiedBy,
	        @LastModifiedAt,
	        @DeletedStatus,
	        @PrintStatus,
	        @RecordStatus
	      )

```
