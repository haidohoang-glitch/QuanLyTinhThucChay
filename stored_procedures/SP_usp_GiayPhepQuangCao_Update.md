# Stored Procedure: `usp_GiayPhepQuangCao_Update`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-22 09:41:51.943000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.320000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@GiayPhepQuangCaoID` | `int(4)` | No |
| `@TenGiayPhep` | `nvarchar(510)` | No |
| `@DmLoaiGiayPhepREF` | `int(4)` | No |
| `@DmNhanHangREF` | `int(4)` | No |
| `@ThoiGianHieuLuc` | `date(3)` | No |
| `@DuongDanFile` | `nvarchar(510)` | No |
| `@TenFile` | `nvarchar(510)` | No |
| `@GhiChu` | `nvarchar(1024)` | No |
| `@DataLocked` | `bit(1)` | No |
| `@LastModifiedBy` | `varchar(50)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |
| `@SubmitedBy` | `varchar(50)` | No |
| `@SubmitedAt` | `datetime(8)` | No |
| `@ApprovedBy` | `varchar(50)` | No |
| `@ApprovedAt` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_GiayPhepQuangCao_Update]
	@GiayPhepQuangCaoID INT,
	@TenGiayPhep NVARCHAR(255),
	@DmLoaiGiayPhepREF INT,
	@DmNhanHangREF INT,
	@ThoiGianHieuLuc date,
	@DuongDanFile NVARCHAR(255),
	@TenFile NVARCHAR(255),
	@GhiChu NVARCHAR(512),
	@DataLocked BIT,
	@LastModifiedBy VARCHAR(50),
	@LastModifiedAt DATETIME,
	@DeletedStatus INT,
	@PrintStatus INT,
	@RecordStatus INT,
	@SubmitedBy VARCHAR(50),
	@SubmitedAt DATETIME,
	@ApprovedBy VARCHAR(50),
	@ApprovedAt DATETIME
AS
BEGIN
	SET NOCOUNT ON
	
	UPDATE [dbo].[GiayPhepQuangCaoNhan]
	SET    [TenGiayPhep] = @TenGiayPhep,
	       [DmLoaiGiayPhepREF] = @DmLoaiGiayPhepREF,
	       [DmNhanHangREF] = @DmNhanHangREF,
	       [ThoiGianHieuLuc] = @ThoiGianHieuLuc,
	       [DuongDanFile] = @DuongDanFile,
	       [TenFile] = @TenFile,
	       [GhiChu] = @GhiChu,
	       [DataLocked] = @DataLocked,
	       [LastModifiedBy] = @LastModifiedBy,
	       [LastModifiedAt] = @LastModifiedAt,
	       [DeletedStatus] = @DeletedStatus,
	       [PrintStatus] = @PrintStatus,
	       [RecordStatus] = @RecordStatus,
	       [SubmitedBy] = @SubmitedBy,
	       [SubmitedAt] = @SubmitedAt,
	       [ApprovedBy] = @ApprovedBy,
	       [ApprovedAt] = @ApprovedAt
	WHERE  [GiayPhepQuangCaoID] = @GiayPhepQuangCaoID
END

```
