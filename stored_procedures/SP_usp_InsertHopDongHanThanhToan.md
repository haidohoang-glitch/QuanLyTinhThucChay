# Stored Procedure: `usp_InsertHopDongHanThanhToan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:18.123000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.860000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongHanThanhToanID` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@LanThanhToan` | `int(4)` | No |
| `@NgayThanhToan` | `datetime(8)` | No |
| `@SoTien` | `float(8)` | No |
| `@NgayDuDinhThanhToan` | `datetime(8)` | No |
| `@GiaTriDaThanhToan` | `float(8)` | No |
| `@GhiChu` | `nvarchar(8000)` | No |
| `@Active` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_InsertHopDongHanThanhToan]
	@HopDongHanThanhToanID INT,
	@HopDongREF INT,
	@LanThanhToan INT,
	@NgayThanhToan DATETIME,
	@SoTien FLOAT,
	@NgayDuDinhThanhToan DATETIME,
	@GiaTriDaThanhToan FLOAT,
	@GhiChu NVARCHAR(4000),
	@Active INT,
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
	           SELECT [HopDongREF]
	           FROM   dbo.HopDongHanThanhToan
	           WHERE  HopDongHanThanhToanID = @HopDongHanThanhToanID
	       )
	   )
	    UPDATE [dbo].[HopDongHanThanhToan]
	    SET    [HopDongREF]             = @HopDongREF,
	           [LanThanhToan]           = @LanThanhToan,
	           [NgayThanhToan]          = @NgayThanhToan,
	           [SoTien]                 = @SoTien,
	           [NgayDuDinhThanhToan]    = @NgayDuDinhThanhToan,
	           [GiaTriDaThanhToan]      = @GiaTriDaThanhToan,
	           [GhiChu]                 = @GhiChu,
	           [Active]                 = @Active,
	           [LastModifiedBy]         = @LastModifiedBy,
	           [LastModifiedAt]         = @LastModifiedAt,
	           [DeletedStatus]          = @DeletedStatus,
	           [PrintStatus]            = @PrintStatus,
	           [RecordStatus]           = @RecordStatus
	    WHERE  [HopDongHanThanhToanID]  = @HopDongHanThanhToanID
	ELSE
	    INSERT INTO [dbo].[HopDongHanThanhToan]
	      (
	        [HopDongHanThanhToanID],
	        [HopDongREF],
	        [LanThanhToan],
	        [NgayThanhToan],
	        [SoTien],
	        [NgayDuDinhThanhToan],
	        [GiaTriDaThanhToan],
	        [GhiChu],
	        [Active],
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
	        @HopDongHanThanhToanID,
	        @HopDongREF,
	        @LanThanhToan,
	        @NgayThanhToan,
	        @SoTien,
	        @NgayDuDinhThanhToan,
	        @GiaTriDaThanhToan,
	        @GhiChu,
	        @Active,
	        @CreatedBy,
	        @CreatedAt,
	        @LastModifiedBy,
	        @LastModifiedAt,
	        @DeletedStatus,
	        @PrintStatus,
	        @RecordStatus
	      )

```
