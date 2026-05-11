# Stored Procedure: `usp_NhanHang_InsertUpdatePhanQuyen`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 14:53:58.947000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.603000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangREF` | `int(4)` | No |
| `@OxUserREF` | `int(4)` | No |
| `@TenNhansu` | `nvarchar(510)` | No |
| `@MaNhanSu` | `varchar(50)` | No |
| `@TenPhongBan` | `nvarchar(510)` | No |
| `@TenBoPhan` | `nvarchar(510)` | No |
| `@TenNhom` | `nvarchar(510)` | No |
| `@ThoiGianHieuLuc` | `date(3)` | No |
| `@KichHoat` | `bit(1)` | No |
| `@UserName` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_NhanHang_InsertUpdatePhanQuyen]
	@DmNhanHangREF INT,
	@OxUserREF INT,
	@TenNhansu NVARCHAR(255),
	@MaNhanSu VARCHAR(50),
	@TenPhongBan NVARCHAR(255),
	@TenBoPhan NVARCHAR(255),
	@TenNhom NVARCHAR(255),
	@ThoiGianHieuLuc date,
	@KichHoat BIT,
	@UserName NVARCHAR(50)
AS
BEGIN
	SET NOCOUNT ON;
	
	IF EXISTS(
	       SELECT [DmNhanHangREF],
	              [OxUserREF]
	       FROM   [dbo].[PhanQuyenNhanHang]
	       WHERE  [DmNhanHangREF] = @DmNhanHangREF
	              AND [OxUserREF] = @OxUserREF
	   )
	BEGIN
	    UPDATE [dbo].[PhanQuyenNhanHang]
	    SET    [TenNhansu]        = @TenNhansu,
	           [MaNhanSu]         = @MaNhanSu,
	           [TenPhongBan]      = @TenPhongBan,
	           [TenBoPhan]        = @TenBoPhan,
	           [TenNhom]          = @TenNhom,
	           [ThoiGianHieuLuc]  = @ThoiGianHieuLuc,
	           [KichHoat]         = @KichHoat,
	           [LastModifiedBy]   = @UserName,
	           [LastModifiedAt]   = getdate()
	    WHERE  [DmNhanHangREF]    = @DmNhanHangREF
	           AND [OxUserREF]    = @OxUserREF
	END
	ELSE
	BEGIN
	    INSERT INTO [dbo].[PhanQuyenNhanHang]
	      (
	        [DmNhanHangREF],
	        [OxUserREF],
	        [TenNhansu],
	        [MaNhanSu],
	        [TenPhongBan],
	        [TenBoPhan],
	        [TenNhom],
	        [ThoiGianHieuLuc],
	        [KichHoat],
	        [CreatedBy],
	        [CreatedAt],
			[LastModifiedBy],
			[LastModifiedAt]
	      )
	    VALUES
	      (
	        @DmNhanHangREF,
	        @OxUserREF,
	        @TenNhansu,
	        @MaNhanSu,
	        @TenPhongBan,
	        @TenBoPhan,
	        @TenNhom,
	        @ThoiGianHieuLuc,
	        @KichHoat,
	        @UserName,
	        getdate(),
			@UserName,
			getdate()
	      )
	END
END

```
