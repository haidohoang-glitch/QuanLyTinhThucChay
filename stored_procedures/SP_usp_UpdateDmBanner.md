# Stored Procedure: `usp_UpdateDmBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-10-24 14:36:12.973000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.120000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmBannerID` | `int(4)` | No |
| `@TenBanner` | `nvarchar(100)` | No |
| `@TenBanner_boxapp` | `nvarchar(400)` | No |
| `@LoaiSanPham` | `int(4)` | No |
| `@Active` | `int(4)` | No |
| `@NgayBatDau` | `datetime(8)` | No |
| `@NgayKetThuc` | `datetime(8)` | No |
| `@MoTa` | `nvarchar(8000)` | No |
| `@TenFile` | `nvarchar(400)` | No |
| `@Width` | `nvarchar(40)` | No |
| `@Height` | `nvarchar(40)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   MT844
-- Stored Procedure Name: [dbo].[usp_UpdateDmBanner]
-- Create Date: Thursday, October 24, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateDmBanner]
	@DmBannerID int,
	@TenBanner nvarchar(50),
	@TenBanner_boxapp nvarchar(200),
	@LoaiSanPham int,
	@Active int,
	@NgayBatDau datetime,
	@NgayKetThuc datetime,
	@MoTa nvarchar(4000),
	@TenFile nvarchar(200),
	@Width nvarchar(20),
	@Height nvarchar(20),
	@CreatedBy nvarchar(50),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(50),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON

UPDATE [dbo].[DmBanner] SET
	[TenBanner] = @TenBanner,
	[TenBanner_boxapp] = @TenBanner_boxapp,
	[LoaiSanPham] = @LoaiSanPham,
	[Active] = @Active,
	[NgayBatDau] = @NgayBatDau,
	[NgayKetThuc] = @NgayKetThuc,
	[MoTa] = @MoTa,
	[TenFile] = @TenFile,
	[Width] = @Width,
	[Height] = @Height,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[DmBannerID] = @DmBannerID

--endregion

```
