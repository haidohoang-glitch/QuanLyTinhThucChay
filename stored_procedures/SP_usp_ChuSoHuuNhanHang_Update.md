# Stored Procedure: `usp_ChuSoHuuNhanHang_Update`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 14:53:58.600000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.393000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmChuSoHuuID` | `int(4)` | No |
| `@TenChuSoHuu` | `nvarchar(512)` | No |
| `@Ghichu` | `nvarchar(2048)` | No |
| `@LastModidfiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_ChuSoHuuNhanHang_Update]
	@DmChuSoHuuID INT,
	@TenChuSoHuu NVARCHAR(256),
	@Ghichu NVARCHAR(1024),
	@LastModidfiedBy NVARCHAR(50),
	@LastModifiedAt DATETIME,
	@DeletedStatus INT,
	@PrintStatus INT,
	@RecordStatus INT
AS
BEGIN
	SET NOCOUNT ON;
	
	UPDATE [dbo].[DmChuSoHuuNhanhang]
	SET    [TenChuSoHuu]      = @TenChuSoHuu,
	       [Ghichu]           = @Ghichu,
	       [LastModidfiedBy]  = @LastModidfiedBy,
	       [LastModifiedAt]   = @LastModifiedAt,
	       [DeletedStatus]    = @DeletedStatus,
	       [PrintStatus]      = @PrintStatus,
	       [RecordStatus]     = @RecordStatus
	WHERE  [DmChuSoHuuID]     = @DmChuSoHuuID
END

```
