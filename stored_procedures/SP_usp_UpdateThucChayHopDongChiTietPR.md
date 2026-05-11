# Stored Procedure: `usp_UpdateThucChayHopDongChiTietPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-07-09 11:13:12.020000
- **Ngày sửa cuối**: 2014-11-19 12:24:44.773000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayHopDongChiTietPRID` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@NhanHang` | `nvarchar(510)` | No |
| `@TenWebsite` | `nvarchar(510)` | No |
| `@ChuyenMuc` | `nvarchar(510)` | No |
| `@TieuDiem` | `int(4)` | No |
| `@KhuyenMai` | `int(4)` | No |
| `@GiaTien` | `int(4)` | No |
| `@ThoiGianBatDau` | `datetime(8)` | No |
| `@Link` | `nvarchar(400)` | No |
| `@GhiChu` | `nvarchar(510)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql


CREATE PROCEDURE [dbo].[usp_UpdateThucChayHopDongChiTietPR]
	@ThucChayHopDongChiTietPRID int,
	@HopDongREF int,
	@HopDongChiTietREF int,
	@NhanHang nvarchar(255),
	@TenWebsite nvarchar(255),
	@ChuyenMuc nvarchar(255),
	@TieuDiem int,
	@KhuyenMai int,
	@GiaTien int,
	@ThoiGianBatDau datetime,
	@Link nvarchar(200),
	@GhiChu nvarchar(255),
	@CreatedBy nvarchar(50),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(50),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON

UPDATE [dbo].[ThucChayHopDongChiTietPR] SET
	[HopDongREF] = @HopDongREF,
	[HopDongChiTietREF] = @HopDongChiTietREF,
	[NhanHang] = @NhanHang,
	[TenWebsite] = @TenWebsite,
	[ChuyenMuc] = @ChuyenMuc,
	[TieuDiem] = @TieuDiem,
	[KhuyenMai] = @KhuyenMai,
	[GiaTien] = @GiaTien,
	[ThoiGianBatDau] = @ThoiGianBatDau,
	[Link] = @Link,
	[GhiChu] = @GhiChu,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[ThucChayHopDongChiTietPRID] = @ThucChayHopDongChiTietPRID

--endregion

```
