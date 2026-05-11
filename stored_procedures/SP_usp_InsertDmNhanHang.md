# Stored Procedure: `usp_InsertDmNhanHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-27 10:21:32.400000
- **Ngày sửa cuối**: 2014-11-19 12:16:53.540000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
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
CREATE PROCEDURE [dbo].[usp_InsertDmNhanHang]
	@TenNhanHang NVARCHAR(50),
	@DmNghanhHangREF NVARCHAR(2000),
	@NhanSuSoYeuLyLichREF VARCHAR(2000),
	@DmNhanHangThayDoiID INT,
	@CreatedBy NVARCHAR(50),
	@CreatedAt DATETIME,
	@LastModidfiedBy NVARCHAR(50),
	@LastModifiedAt DATETIME,
	@DeletedStatus INT,
	@PrintStatus INT,
	@RecordStatus INT
AS
BEGIN
	SET NOCOUNT ON;
	
	INSERT INTO [dbo].[DmNhanHang]
	  (
	    [TenNhanHang],
	    [DmNghanhHangREF],
	    [NhanSuSoYeuLyLichREF],
	    [DmNhanHangThayDoiID],
	    [CreatedBy],
	    [CreatedAt],
	    [LastModidfiedBy],
	    [LastModifiedAt],
	    [DeletedStatus],
	    [PrintStatus],
	    [RecordStatus]
	  )
	VALUES
	  (
	    @TenNhanHang,
	    dbo.f_ReturnGroupNghanhHangID(@DmNghanhHangREF, ','),
	    dbo.f_ReturnGroupConcatNhansuID(@NhanSuSoYeuLyLichREF, ','),
	    @DmNhanHangThayDoiID,
	    @CreatedBy,
	    @CreatedAt,
	    @LastModidfiedBy,
	    @LastModifiedAt,
	    @DeletedStatus,
	    @PrintStatus,
	    @RecordStatus
	  )
END

```
