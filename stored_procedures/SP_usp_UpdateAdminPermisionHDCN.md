# Stored Procedure: `usp_UpdateAdminPermisionHDCN`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-06 17:01:41.300000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.017000

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
CREATE PROCEDURE [dbo].[usp_UpdateAdminPermisionHDCN]
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

SET NOCOUNT ON

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

--endregion

```
