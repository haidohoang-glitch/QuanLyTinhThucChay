# Stored Procedure: `usp_GiayPhepQuangCao_UpdateRecordStatus`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-22 09:41:51.687000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.273000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@GiayPhepQuangCaoID` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `varchar(50)` | No |
| `@SubmitedBy` | `varchar(50)` | No |
| `@SubmitedAt` | `datetime(8)` | No |
| `@ApprovedBy` | `varchar(50)` | No |
| `@ApprovedAt` | `datetime(8)` | No |
| `@GhiChu` | `nvarchar(1024)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_GiayPhepQuangCao_UpdateRecordStatus]
	@GiayPhepQuangCaoID INT,
	@RecordStatus INT,
	@LastModifiedAt DATETIME,
	@LastModifiedBy VARCHAR(50),
	@SubmitedBy VARCHAR(50),
	@SubmitedAt DATETIME,
	@ApprovedBy VARCHAR(50),
	@ApprovedAt DATETIME,
	@GhiChu NVARCHAR(512)
AS
BEGIN
	SET NOCOUNT ON
	
	UPDATE [dbo].[GiayPhepQuangCaoNhan]
	SET    [RecordStatus]        = @RecordStatus,
	       [LastModifiedAt]      = @LastModifiedAt,
	       [LastModifiedBy]      = @LastModifiedBy,
	       [SubmitedBy]          = @SubmitedBy,
	       [SubmitedAt]          = @SubmitedAt,
	       [ApprovedBy]          = @ApprovedBy,
	       [ApprovedAt]          = @ApprovedAt,
	       [GhiChu]              = @GhiChu
	WHERE  [GiayPhepQuangCaoID]  = @GiayPhepQuangCaoID
END

```
