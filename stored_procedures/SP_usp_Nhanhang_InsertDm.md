# Stored Procedure: `usp_Nhanhang_InsertDm`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-25 17:09:50.493000
- **Ngày sửa cuối**: 2014-11-19 12:16:46.703000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangID` | `int(4)` | Yes |
| `@TenNhanHang` | `nvarchar(2048)` | No |
| `@NhanHangCha` | `int(4)` | No |
| `@MucDoNhan` | `int(4)` | No |
| `@DmNghanhHangREF` | `nvarchar(4000)` | No |
| `@TenChienDich` | `nvarchar(1024)` | No |
| `@NhanSuSoYeuLyLichREF` | `nvarchar(4000)` | No |
| `@DmNhanHangThayDoiID` | `int(4)` | No |
| `@DmKhachhangKyREF` | `nvarchar(4000)` | No |
| `@DmKhachhangSohuuREF` | `varchar(50)` | No |
| `@DmNhaPhanPhoiREF` | `varchar(50)` | No |
| `@Ghichu` | `nvarchar(512)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModidfiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |
| `@FromSystem` | `nvarchar(256)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_Nhanhang_InsertDm]
	@DmNhanHangID INT OUTPUT,
	@TenNhanHang NVARCHAR(1024),
	@NhanHangCha INT,
	@MucDoNhan INT ,
	@DmNghanhHangREF NVARCHAR(2000),	
	@TenChienDich NVARCHAR(512),
	@NhanSuSoYeuLyLichREF NVARCHAR(2000),
	@DmNhanHangThayDoiID INT,
	@DmKhachhangKyREF NVARCHAR(2000),
	@DmKhachhangSohuuREF VARCHAR(50),
	@DmNhaPhanPhoiREF VARCHAR(50),
	@Ghichu NVARCHAR(256),
	@CreatedBy NVARCHAR(50),
	@CreatedAt DATETIME,
	@LastModidfiedBy NVARCHAR(50),
	@LastModifiedAt DATETIME,
	@DeletedStatus INT,
	@PrintStatus INT,
	@RecordStatus INT,
	@FromSystem NVARCHAR(128)
AS
BEGIN
	SET NOCOUNT ON;
	
	    INSERT INTO [dbo].[DmNhanHang]
	      (
	        [TenNhanHang],
	        [NhanHangCha],
	        [MucDoNhan],
	        [DmNghanhHangREF],
	        TenChienDich,
	        [NhanSuSoYeuLyLichREF],
	        [DmNhanHangThayDoiID],
	        [DmKhachhangKyREF],
			[DmKhachhangSohuuREF],
			[DmNhaPhanPhoiREF],
			[Ghichu],
			--[HopdongChitietREF],
	        [CreatedBy],
	        [CreatedAt],
	        [LastModidfiedBy],
	        [LastModifiedAt],
	        [DeletedStatus],
	        [PrintStatus],
	        [RecordStatus],
	        [FromSystem]
	      )
	    VALUES
	      (
	        @TenNhanHang,
	        @NhanHangCha,
	        @MucDoNhan,
	        @DmNghanhHangREF,
	        @TenChienDich,
	        /*dbo.f_ReturnGroupConcatNhansuID(@NhanSuSoYeuLyLichREF, ';'),*/
			'',
	        @DmNhanHangThayDoiID,
	        '',/*dbo.f_ReturnGroupKhachHangID(@DmKhachhangKyREF,';'),*/	        
			@DmKhachhangSohuuREF,
			@DmNhaPhanPhoiREF,
			@Ghichu,
			@CreatedBy,
	        @CreatedAt,
	        @LastModidfiedBy,
	        @LastModifiedAt,
	        @DeletedStatus,
	        @PrintStatus,
	        @RecordStatus,
	        @FromSystem
	      )
	      
	      SELECT @DmNhanHangID = SCOPE_IDENTITY()
END

```
