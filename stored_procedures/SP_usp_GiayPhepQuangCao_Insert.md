# Stored Procedure: `usp_GiayPhepQuangCao_Insert`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-22 09:41:52.680000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.403000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenGiayPhep` | `nvarchar(510)` | No |
| `@DmLoaiGiayPhepREF` | `int(4)` | No |
| `@DmNhanHangREF` | `int(4)` | No |
| `@ThoiGianHieuLuc` | `date(3)` | No |
| `@DuongDanFile` | `nvarchar(510)` | No |
| `@TenFile` | `nvarchar(510)` | No |
| `@GhiChu` | `nvarchar(1024)` | No |
| `@DataLocked` | `bit(1)` | No |
| `@CreatedBy` | `varchar(50)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `varchar(50)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |
| `@SubmitedBy` | `varchar(50)` | No |
| `@SubmitedAt` | `datetime(8)` | No |
| `@ApprovedBy` | `varchar(50)` | No |
| `@ApprovedAt` | `datetime(8)` | No |
| `@GiayPhepQuangCaoID` | `int(4)` | Yes |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_GiayPhepQuangCao_Insert]
	@TenGiayPhep NVARCHAR(255),
	@DmLoaiGiayPhepREF INT,
	@DmNhanHangREF INT,
	@ThoiGianHieuLuc date,
	@DuongDanFile NVARCHAR(255),
	@TenFile NVARCHAR(255),
	@GhiChu NVARCHAR(512),
	@DataLocked BIT,
	@CreatedBy VARCHAR(50),
	@CreatedAt DATETIME,
	@LastModifiedBy VARCHAR(50),
	@LastModifiedAt DATETIME,
	@DeletedStatus INT,
	@PrintStatus INT,
	@RecordStatus INT,
	@SubmitedBy VARCHAR(50),
	@SubmitedAt DATETIME,
	@ApprovedBy VARCHAR(50),
	@ApprovedAt DATETIME,
	@GiayPhepQuangCaoID INT OUTPUT
AS
BEGIN
	SET NOCOUNT ON;
	
	INSERT INTO [dbo].[GiayPhepQuangCaoNhan]
	  (
	    [TenGiayPhep],
	    [DmLoaiGiayPhepREF],
	    [DmNhanHangREF],
	    [ThoiGianHieuLuc],
	    [DuongDanFile],
	    [TenFile],
	    [GhiChu],
	    [DataLocked],
	    [CreatedBy],
	    [CreatedAt],
	    [LastModifiedBy],
	    [LastModifiedAt],
	    [DeletedStatus],
	    [PrintStatus],
	    [RecordStatus],
	    [SubmitedBy],
	    [SubmitedAt],
	    [ApprovedBy],
	    [ApprovedAt]
	  )
	VALUES
	  (
	    @TenGiayPhep,
	    @DmLoaiGiayPhepREF,
	    @DmNhanHangREF,
	    @ThoiGianHieuLuc,
	    @DuongDanFile,
	    @TenFile,
	    @GhiChu,
	    @DataLocked,
	    @CreatedBy,
	    @CreatedAt,
	    @LastModifiedBy,
	    @LastModifiedAt,
	    @DeletedStatus,
	    @PrintStatus,
	    @RecordStatus,
	    @SubmitedBy,
	    @SubmitedAt,
	    @ApprovedBy,
	    @ApprovedAt
	  )
	
	SELECT @GiayPhepQuangCaoID = SCOPE_IDENTITY();
END

```
