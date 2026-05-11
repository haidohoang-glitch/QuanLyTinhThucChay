# Stored Procedure: `usp_LoaiGiayPhepQuangCao_Update`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-22 09:41:50.813000
- **Ngày sửa cuối**: 2014-11-19 12:16:46.080000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmLoaiGiayPhepID` | `int(4)` | No |
| `@TenLoaiGiayPhep` | `nvarchar(510)` | No |
| `@Ghichu` | `nvarchar(1024)` | No |
| `@LastModifiedBy` | `varchar(50)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_LoaiGiayPhepQuangCao_Update]
	@DmLoaiGiayPhepID INT,
	@TenLoaiGiayPhep NVARCHAR(255),
	@Ghichu NVARCHAR(512),
	@LastModifiedBy VARCHAR(50),
	@LastModifiedAt DATETIME
AS
BEGIN
	SET NOCOUNT ON;
	
	UPDATE [dbo].[DmLoaiGiayPhepQuangCao]
	SET    [TenLoaiGiayPhep] = @TenLoaiGiayPhep,
	       [Ghichu] = @Ghichu,
	       [LastModifiedBy] = @LastModifiedBy,
	       [LastModifiedAt] = @LastModifiedAt
	WHERE  [DmLoaiGiayPhepID] = @DmLoaiGiayPhepID;
END

```
