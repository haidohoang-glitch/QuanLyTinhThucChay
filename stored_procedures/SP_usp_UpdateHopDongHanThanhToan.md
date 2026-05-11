# Stored Procedure: `usp_UpdateHopDongHanThanhToan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:18.517000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.147000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongHanThanhToanID` | `int(4)` | No |
| `@HopDongREF` | `int(4)` | No |
| `@LanThanhToan` | `int(4)` | No |
| `@NgayThanhToan` | `datetime(8)` | No |
| `@SoTien` | `float(8)` | No |
| `@NgayDuDinhThanhToan` | `datetime(8)` | No |
| `@GiaTriDaThanhToan` | `float(8)` | No |
| `@GhiChu` | `nvarchar(8000)` | No |
| `@Active` | `int(4)` | No |
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
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateHopDongHanThanhToan]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateHopDongHanThanhToan]
	@HopDongHanThanhToanID int,
	@HopDongREF int,
	@LanThanhToan int,
	@NgayThanhToan datetime,
	@SoTien float,
	@NgayDuDinhThanhToan datetime,
	@GiaTriDaThanhToan float,
	@GhiChu nvarchar(4000),
	@Active int,
	@CreatedBy nvarchar(50),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(50),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON

UPDATE [dbo].[HopDongHanThanhToan] SET
	[HopDongREF] = @HopDongREF,
	[LanThanhToan] = @LanThanhToan,
	[NgayThanhToan] = @NgayThanhToan,
	[SoTien] = @SoTien,
	[NgayDuDinhThanhToan] = @NgayDuDinhThanhToan,
	[GiaTriDaThanhToan] = @GiaTriDaThanhToan,
	[GhiChu] = @GhiChu,
	[Active] = @Active,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[HopDongHanThanhToanID] = @HopDongHanThanhToanID

--endregion

```
