# Stored Procedure: `usp_LoaiGiayPhepQuangCao_Insert`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-22 09:41:51.360000
- **Ngày sửa cuối**: 2014-11-19 12:16:46.200000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenLoaiGiayPhep` | `nvarchar(510)` | No |
| `@Ghichu` | `nvarchar(1024)` | No |
| `@CreatedBy` | `varchar(50)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `varchar(50)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |
| `@DmLoaiGiayPhepID` | `int(4)` | Yes |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_LoaiGiayPhepQuangCao_Insert]
	@TenLoaiGiayPhep NVARCHAR(255),
	@Ghichu NVARCHAR(512),
	@CreatedBy VARCHAR(50),
	@CreatedAt DATETIME,
	@LastModifiedBy VARCHAR(50),
	@LastModifiedAt DATETIME,
	@DeletedStatus INT,
	@PrintStatus INT,
	@RecordStatus INT,
	@DmLoaiGiayPhepID INT OUTPUT
AS
BEGIN
	SET NOCOUNT ON;
	
	INSERT INTO [dbo].[DmLoaiGiayPhepQuangCao]
	  (
	    [TenLoaiGiayPhep],
	    [Ghichu],
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
	    @TenLoaiGiayPhep,
	    @Ghichu,
	    @CreatedBy,
	    @CreatedAt,
	    @LastModifiedBy,
	    @LastModifiedAt,
	    @DeletedStatus,
	    @PrintStatus,
	    @RecordStatus
	  )
	
	SELECT @DmLoaiGiayPhepID = SCOPE_IDENTITY();
END

```
