# Stored Procedure: `usp_UpdateDmNhanHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-18 15:22:49.383000
- **Ngày sửa cuối**: 2014-11-19 12:16:53.637000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangID` | `int(4)` | No |
| `@TenNhanHang` | `nvarchar(100)` | No |
| `@DmNghanhHangREF` | `nvarchar(4000)` | No |
| `@NhanSuSoYeuLyLichREF` | `varchar(2000)` | No |
| `@DmNhanHangThayDoiID` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModidfiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_UpdateDmNhanHang]
	@DmNhanHangID INT,
	@TenNhanHang NVARCHAR(50),
	@DmNghanhHangREF NVARCHAR(2000),
	@NhanSuSoYeuLyLichREF VARCHAR(2000),
	@DmNhanHangThayDoiID INT,
	@CreatedBy NVARCHAR(50),
	@CreatedAt DATETIME,
	@LastModidfiedBy NVARCHAR(50),
	@LastModifiedAt DATETIME,
	@DeletedStatus INT = 0,
	@PrintStatus INT = 0,
	@RecordStatus INT = 1
AS
	SET NOCOUNT ON;
	
	UPDATE [dbo].[DmNhanHang]
	SET    [TenNhanHang]           = @TenNhanHang,
	       [DmNghanhHangREF]       = dbo.f_ReturnGroupNghanhHangID(@DmNghanhHangREF, ','),
	       [NhanSuSoYeuLyLichREF]  = dbo.f_ReturnGroupConcatNhansuID(@NhanSuSoYeuLyLichREF, ','),
	       [DmNhanHangThayDoiID]   = @DmNhanHangThayDoiID,
	       [LastModidfiedBy]       = @LastModidfiedBy,
	       [LastModifiedAt]        = @LastModifiedAt,
	       [DeletedStatus]         = @DeletedStatus,
	       [PrintStatus]           = @PrintStatus,
	       [RecordStatus]          = @RecordStatus
	WHERE  [DmNhanHangID]          = @DmNhanHangID

```
