# Stored Procedure: `usp_InsertAdminPermisionHDCN`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-06 17:01:42.017000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.250000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@AdminPermisionHDCNID` | `int(4)` | No |
| `@NhanSuSoYeuLyLichID` | `int(4)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@AdminGroupId` | `int(4)` | No |
| `@KhoaNguoiDung` | `int(4)` | No |
| `@ThoiGianDangNhap` | `datetime(8)` | No |
| `@SalerID` | `int(4)` | No |
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
-- Stored Procedure Name: [dbo].[usp_InsertAdminPermisionHDCN]
-- Create Date: Friday, September 06, 2013
-- Description: 
--=============================================



CREATE PROCEDURE [dbo].[usp_InsertAdminPermisionHDCN]
	@AdminPermisionHDCNID int,
	@NhanSuSoYeuLyLichID int,
	@TenDangNhap nvarchar(50),
	@AdminGroupId int,
	@KhoaNguoiDung int,
	@ThoiGianDangNhap datetime,
	@SalerID int,
	@CreatedBy nvarchar(50),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(50),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS
IF(EXISTS(SELECT * FROM AdminPermisionHDCN WHERE TenDangNhap = @TenDangNhap))
UPDATE [dbo].[AdminPermisionHDCN] SET
	[NhanSuSoYeuLyLichID] = @NhanSuSoYeuLyLichID,
	[TenDangNhap] = @TenDangNhap,
	[AdminGroupId] = @AdminGroupId,
	[KhoaNguoiDung] = @KhoaNguoiDung,
	[ThoiGianDangNhap] = @ThoiGianDangNhap,
	[SalerID] = @SalerID,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[AdminPermisionHDCNID] = @AdminPermisionHDCNID
ELSE

INSERT INTO [dbo].[AdminPermisionHDCN] (
	[AdminPermisionHDCNID],
	[NhanSuSoYeuLyLichID],
	[TenDangNhap],
	[AdminGroupId],
	[KhoaNguoiDung],
	[ThoiGianDangNhap],
	[SalerID],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
) VALUES (
	@AdminPermisionHDCNID,
	@NhanSuSoYeuLyLichID,
	@TenDangNhap,
	@AdminGroupId,
	@KhoaNguoiDung,
	@ThoiGianDangNhap,
	@SalerID,
	@CreatedBy,
	@CreatedAt,
	@LastModifiedBy,
	@LastModifiedAt,
	@DeletedStatus,
	@PrintStatus,
	@RecordStatus
)

--endregion

```
