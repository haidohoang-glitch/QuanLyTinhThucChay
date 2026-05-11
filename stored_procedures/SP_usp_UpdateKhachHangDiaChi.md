# Stored Procedure: `usp_UpdateKhachHangDiaChi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:14:27.730000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.613000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KhachHangDiaChiID` | `int(4)` | No |
| `@KhachHangREF` | `int(4)` | No |
| `@TruSoChinh` | `nvarchar(400)` | No |
| `@ChiNhanh` | `nvarchar(400)` | No |
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
-- Stored Procedure Name: [dbo].[usp_UpdateKhachHangDiaChi]
-- Create Date: Tuesday, August 20, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateKhachHangDiaChi]
	@KhachHangDiaChiID int,
	@KhachHangREF int,
	@TruSoChinh nvarchar(200),
	@ChiNhanh nvarchar(200),
	@CreatedBy nvarchar(50),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(50),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON

UPDATE [dbo].[KhachHangDiaChi] SET
	[KhachHangREF] = @KhachHangREF,
	[TruSoChinh] = @TruSoChinh,
	[ChiNhanh] = @ChiNhanh,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[KhachHangDiaChiID] = @KhachHangDiaChiID

--endregion

```
