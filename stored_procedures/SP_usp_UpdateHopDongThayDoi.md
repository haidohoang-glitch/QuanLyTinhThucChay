# Stored Procedure: `usp_UpdateHopDongThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-03 14:33:32.717000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.140000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongThayDoiID` | `int(4)` | No |
| `@HopDongFK` | `int(4)` | No |
| `@LoaiThayDoi` | `int(4)` | No |
| `@NgayThayDoi` | `datetime(8)` | No |
| `@NganhHang` | `nvarchar(400)` | No |
| `@NhanHopDong` | `nvarchar(100)` | No |
| `@GiaTriHopDong` | `float(8)` | No |
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
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_UpdateHopDongThayDoi]
-- Create Date: Monday, June 03, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateHopDongThayDoi]
	@HopDongThayDoiID int,
	@HopDongFK int,
	@LoaiThayDoi int,
	@NgayThayDoi datetime,
	@NganhHang nvarchar(200),
	@NhanHopDong nvarchar(50),
	@GiaTriHopDong float,
	@CreatedBy nvarchar(50),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(50),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON

UPDATE [dbo].[HopDongThayDoi] SET
	[HopDongFK] = @HopDongFK,
	[LoaiThayDoi] = @LoaiThayDoi,
	[NgayThayDoi] = @NgayThayDoi,
	[NganhHang] = @NganhHang,
	[NhanHopDong] = @NhanHopDong,
	[GiaTriHopDong] = @GiaTriHopDong,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[HopDongThayDoiID] = @HopDongThayDoiID

--endregion

```
