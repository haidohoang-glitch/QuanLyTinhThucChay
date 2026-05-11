# Stored Procedure: `usp_PhanQuyenNhanHang_Update`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-14 16:27:56.430000
- **Ngày sửa cuối**: 2014-10-14 16:27:56.430000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmPhanQuyenID` | `int(4)` | No |
| `@DmNhanHangREF` | `int(4)` | No |
| `@OxUserREF` | `int(4)` | No |
| `@NhanSuREF` | `int(4)` | No |
| `@TenNhanSu` | `nvarchar(510)` | No |
| `@MaNhanSu` | `varchar(50)` | No |
| `@TenPhongBan` | `nvarchar(510)` | No |
| `@TenBoPhan` | `nvarchar(510)` | No |
| `@TenNhom` | `nvarchar(510)` | No |
| `@ThoiGianHieuLuc` | `date(3)` | No |
| `@ThoiGianHetHieuLuc` | `date(3)` | No |
| `@KichHoat` | `bit(1)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_PhanQuyenNhanHang_Update]
	@DmPhanQuyenID INT,
	@DmNhanHangREF INT,
	@OxUserREF INT,
	@NhanSuREF INT,
	@TenNhanSu NVARCHAR(255),
	@MaNhanSu VARCHAR(50),
	@TenPhongBan NVARCHAR(255),
	@TenBoPhan NVARCHAR(255),
	@TenNhom NVARCHAR(255),
	@ThoiGianHieuLuc date,
	@ThoiGianHetHieuLuc date,
	@KichHoat BIT,
	@CreatedBy NVARCHAR(50),
	@CreatedAt DATETIME,
	@LastModifiedBy NVARCHAR(50),
	@LastModifiedAt DATETIME
AS
BEGIN
	SET NOCOUNT ON;
	
	UPDATE [dbo].[PhanQuyenNhanHang]
	SET    [DmNhanHangREF]       = @DmNhanHangREF,
	       [OxUserREF]           = @OxUserREF,
	       [NhanSuREF]           = @NhanSuREF,
	       [TenNhanSu]           = @TenNhanSu,
	       [MaNhanSu]            = @MaNhanSu,
	       [TenPhongBan]         = @TenPhongBan,
	       [TenBoPhan]           = @TenBoPhan,
	       [TenNhom]             = @TenNhom,
	       [ThoiGianHieuLuc]     = @ThoiGianHieuLuc,
	       [ThoiGianHetHieuLuc]  = @ThoiGianHetHieuLuc,
	       [KichHoat]            = @KichHoat,
	       [CreatedBy]           = @CreatedBy,
	       [CreatedAt]           = @CreatedAt,
	       [LastModifiedBy]      = @LastModifiedBy,
	       [LastModifiedAt]      = @LastModifiedAt
	WHERE  [DmPhanQuyenID]       = @DmPhanQuyenID
END

```
