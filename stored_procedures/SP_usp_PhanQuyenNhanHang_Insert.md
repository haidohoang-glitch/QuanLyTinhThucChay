# Stored Procedure: `usp_PhanQuyenNhanHang_Insert`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-14 16:12:50.717000
- **Ngày sửa cuối**: 2014-11-19 12:16:46.540000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmPhanQuyenID` | `int(4)` | Yes |
| `@DmNhanHangREF` | `int(4)` | No |
| `@OxUserREF` | `int(4)` | No |
| `@NhanSuREF` | `int(4)` | No |
| `@TenNhansu` | `nvarchar(510)` | No |
| `@MaNhanSu` | `varchar(50)` | No |
| `@TenPhongBan` | `nvarchar(510)` | No |
| `@TenBoPhan` | `nvarchar(510)` | No |
| `@TenNhom` | `nvarchar(510)` | No |
| `@ThoiGianHieuLuc` | `date(3)` | No |
| `@KichHoat` | `bit(1)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_PhanQuyenNhanHang_Insert]
	@DmPhanQuyenID INT OUTPUT,
	@DmNhanHangREF INT,
	@OxUserREF INT,
	@NhanSuREF INT,
	@TenNhansu NVARCHAR(255),
	@MaNhanSu VARCHAR(50),
	@TenPhongBan NVARCHAR(255),
	@TenBoPhan NVARCHAR(255),
	@TenNhom NVARCHAR(255),
	@ThoiGianHieuLuc date,
	@KichHoat BIT,
	@CreatedBy NVARCHAR(50)
AS
BEGIN
	SET NOCOUNT ON;
	
	INSERT INTO [dbo].[PhanQuyenNhanHang]
	  (
	    [DmNhanHangREF],
	    [OxUserREF],
	    [NhanSuREF],
	    [TenNhansu],
	    [MaNhanSu],
	    [TenPhongBan],
	    [TenBoPhan],
	    [TenNhom],
	    [ThoiGianHieuLuc],
	    [KichHoat],
	    [IsLockPermission],
	    [CreatedBy],
	    [CreatedAt],
	    [LastModifiedBy],
	    [LastModifiedAt]
	  )
	VALUES
	  (
	    @DmNhanHangREF,
	    @OxUserREF,
	    @NhanSuREF,
	    @TenNhansu,
	    @MaNhanSu,
	    @TenPhongBan,
	    @TenBoPhan,
	    @TenNhom,
	    @ThoiGianHieuLuc,
	    @KichHoat,
	    1,
	    @CreatedBy,
	    GETDATE(),
	    @CreatedBy,
	    GETDATE()
	  )
	
	SELECT @DmPhanQuyenID = SCOPE_IDENTITY()
END

```
