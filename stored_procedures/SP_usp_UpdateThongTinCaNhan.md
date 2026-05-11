# Stored Procedure: `usp_UpdateThongTinCaNhan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:24.403000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.433000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThongTinCaNhanID` | `int(4)` | No |
| `@MaThongTinCaNhan` | `nvarchar(100)` | No |
| `@HoVaTen` | `nvarchar(400)` | No |
| `@NgaySinh` | `datetime(8)` | No |
| `@GioiTinh` | `int(4)` | No |
| `@SoChungThucCaNhan` | `nvarchar(100)` | No |
| `@NgayCapChungThucCaNhan` | `datetime(8)` | No |
| `@NoiCapChungThucCaNhan` | `nvarchar(400)` | No |
| `@DienThoai` | `nvarchar(100)` | No |
| `@Fax` | `nvarchar(100)` | No |
| `@Email` | `nvarchar(400)` | No |
| `@Website` | `nvarchar(400)` | No |
| `@DmChucDanhREF` | `int(4)` | No |
| `@DiaChiREF` | `int(4)` | No |
| `@Email2` | `nvarchar(400)` | No |
| `@DienThoai2` | `nvarchar(100)` | No |
| `@DienThoai3` | `nvarchar(100)` | No |
| `@GhiChu` | `nvarchar(8000)` | No |
| `@Active` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(2)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(2)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateThongTinCaNhan]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateThongTinCaNhan]
	@ThongTinCaNhanID int,
	@MaThongTinCaNhan nvarchar(50),
	@HoVaTen nvarchar(200),
	@NgaySinh datetime,
	@GioiTinh int,
	@SoChungThucCaNhan nvarchar(50),
	@NgayCapChungThucCaNhan datetime,
	@NoiCapChungThucCaNhan nvarchar(200),
	@DienThoai nvarchar(50),
	@Fax nvarchar(50),
	@Email nvarchar(200),
	@Website nvarchar(200),
	@DmChucDanhREF int,
	@DiaChiREF int,
	@Email2 nvarchar(200),
	@DienThoai2 nvarchar(50),
	@DienThoai3 nvarchar(50),
	@GhiChu nvarchar(4000),
	@Active int,
	@CreatedBy nvarchar(1),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(1),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON

UPDATE [dbo].[ThongTinCaNhan] SET
	[MaThongTinCaNhan] = @MaThongTinCaNhan,
	[HoVaTen] = @HoVaTen,
	[NgaySinh] = @NgaySinh,
	[GioiTinh] = @GioiTinh,
	[SoChungThucCaNhan] = @SoChungThucCaNhan,
	[NgayCapChungThucCaNhan] = @NgayCapChungThucCaNhan,
	[NoiCapChungThucCaNhan] = @NoiCapChungThucCaNhan,
	[DienThoai] = @DienThoai,
	[Fax] = @Fax,
	[Email] = @Email,
	[Website] = @Website,
	[DmChucDanhREF] = @DmChucDanhREF,
	[DiaChiREF] = @DiaChiREF,
	[Email2] = @Email2,
	[DienThoai2] = @DienThoai2,
	[DienThoai3] = @DienThoai3,
	[GhiChu] = @GhiChu,
	[Active] = @Active,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[ThongTinCaNhanID] = @ThongTinCaNhanID

--endregion

```
