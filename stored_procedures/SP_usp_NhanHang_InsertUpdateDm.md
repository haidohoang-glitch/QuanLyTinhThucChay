# Stored Procedure: `usp_NhanHang_InsertUpdateDm`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:09:50.830000
- **Ngày sửa cuối**: 2014-11-19 12:16:53.567000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangID` | `int(4)` | No |
| `@TenNhanHang` | `nvarchar(2048)` | No |
| `@DmNghanhHangREF` | `nvarchar(4000)` | No |
| `@NhanSuSoYeuLyLichREF` | `varchar(2000)` | No |
| `@DmNhanHangThayDoiID` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_NhanHang_InsertUpdateDm]
	@DmNhanHangID INT,
	@TenNhanHang NVARCHAR(1024),
	@DmNghanhHangREF NVARCHAR(2000),
	@NhanSuSoYeuLyLichREF VARCHAR(2000),
	@DmNhanHangThayDoiID INT,
	@CreatedBy NVARCHAR(50)
AS
	SET NOCOUNT ON;
	DECLARE @a NVARCHAR(1000) = @DmNghanhHangREF;
	IF EXISTS(
	       SELECT [DmNhanHangID]
	       FROM   [dbo].[DmNhanHang]
	       WHERE  [DmNhanHangID] = @DmNhanHangID
	   )
	BEGIN
	    UPDATE [dbo].[DmNhanHang]
	    SET    [TenNhanHang]           = @TenNhanHang,
	           [DmNghanhHangREF]       = dbo.f_ReturnGroupNghanhHangID(@DmNghanhHangREF,';'),
	           [NhanSuSoYeuLyLichREF]  = dbo.f_ReturnGroupConcatNhansuID(@NhanSuSoYeuLyLichREF, ';'),
	           [DmNhanHangThayDoiID]   = @DmNhanHangThayDoiID,
	           [LastModidfiedBy]       = @CreatedBy,
	           [LastModifiedAt]        = GETDATE()
	    WHERE  [DmNhanHangID]          = @DmNhanHangID
	END
	ELSE
	BEGIN
	    INSERT INTO [dbo].[DmNhanHang]
	      (
	        [TenNhanHang],
	        [DmNghanhHangREF],
	        [NhanSuSoYeuLyLichREF],
	        [DmNhanHangThayDoiID],
	        [CreatedBy],
	        [CreatedAt],
	        [DeletedStatus],
	        [PrintStatus],
	        [RecordStatus]
	      )
	    VALUES
	      (
	        @TenNhanHang,
	        dbo.f_ReturnGroupNghanhHangID(@DmNghanhHangREF,';'),
	        dbo.f_ReturnGroupConcatNhansuID(@NhanSuSoYeuLyLichREF, ';'),
	        @DmNhanHangThayDoiID,
	        @CreatedBy,
	        GETDATE(),
	        0,
	        0,
	        1
	      )
	END

```
