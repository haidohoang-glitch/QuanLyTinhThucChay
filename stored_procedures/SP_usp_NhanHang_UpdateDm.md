# Stored Procedure: `usp_NhanHang_UpdateDm`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:09:50.150000
- **Ngày sửa cuối**: 2014-11-19 12:16:46.933000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangID` | `int(4)` | No |
| `@TenNhanHang` | `nvarchar(2048)` | No |
| `@NhanHangCha` | `int(4)` | No |
| `@MucDoNhan` | `int(4)` | No |
| `@DmNghanhHangREF` | `nvarchar(4000)` | No |
| `@TenChienDich` | `nvarchar(1024)` | No |
| `@NhanSuSoYeuLyLichREF` | `nvarchar(4000)` | No |
| `@DmNhanHangThayDoiID` | `int(4)` | No |
| `@DmKhachhangSohuuREF` | `varchar(50)` | No |
| `@DmNhaPhanPhoiREF` | `varchar(50)` | No |
| `@GhiChu` | `nvarchar(512)` | No |
| `@LastModidfiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_NhanHang_UpdateDm]
	@DmNhanHangID INT,
	@TenNhanHang NVARCHAR(1024),
	@NhanHangCha INT,
	@MucDoNhan INT,
	@DmNghanhHangREF NVARCHAR(2000),
	@TenChienDich NVARCHAR(512),
	@NhanSuSoYeuLyLichREF NVARCHAR(2000),
	@DmNhanHangThayDoiID INT,
	@DmKhachhangSohuuREF VARCHAR(50),
	@DmNhaPhanPhoiREF VARCHAR(50),
	@GhiChu NVARCHAR(256),
	@LastModidfiedBy NVARCHAR(50),
	@LastModifiedAt DATETIME,
	@DeletedStatus INT = 0,
	@PrintStatus INT = 0,
	@RecordStatus INT = 1
AS
BEGIN
	SET NOCOUNT ON;
	
	UPDATE [dbo].[DmNhanHang]
	SET    [TenNhanHang]           = @TenNhanHang,
	       [NhanHangCha]           = @NhanHangCha,
	       [MucDoNhan]             = @MucDoNhan,
	       [DmNghanhHangREF]       = @DmNghanhHangREF,
	       [TenChienDich]          = @TenChienDich,
	       [NhanSuSoYeuLyLichREF]  = @NhanSuSoYeuLyLichREF,
	       [DmNhanHangThayDoiID]   = @DmNhanHangThayDoiID,
	       [DmKhachhangSohuuREF]   = @DmKhachhangSohuuREF,
	       [DmNhaPhanPhoiREF]      = @DmNhaPhanPhoiREF,
	       [GhiChu]                = @GhiChu,
	       [LastModidfiedBy]       = @LastModidfiedBy,
	       [LastModifiedAt]        = @LastModifiedAt,
	       [DeletedStatus]         = @DeletedStatus,
	       [PrintStatus]           = @PrintStatus,
	       [RecordStatus]          = @RecordStatus
	WHERE  [DmNhanHangID]          = @DmNhanHangID
END

```
