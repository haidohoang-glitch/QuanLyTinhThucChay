# Stored Procedure: `usp_UpdateDmBoPhanNghiepVu`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-16 11:39:38.397000
- **Ngày sửa cuối**: 2014-10-14 10:39:39.933000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmBoPhanNghiepVuID` | `nvarchar(100)` | No |
| `@DmPhongBanFK` | `nvarchar(100)` | No |
| `@TenBoPhanNghiepVu` | `nvarchar(100)` | No |
| `@DmNgonNguREF` | `nvarchar(100)` | No |
| `@GhiChu` | `nvarchar(8000)` | No |
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
-- Stored Procedure Name: [dbo].[usp_UpdateDmBoPhanNghiepVu]
-- Create Date: Thursday, December 16, 2010
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateDmBoPhanNghiepVu]
	@DmBoPhanNghiepVuID nvarchar(50),
	@DmPhongBanFK nvarchar(50),
	@TenBoPhanNghiepVu nvarchar(50),
	@DmNgonNguREF nvarchar(50),
	@GhiChu nvarchar(4000),
	@CreatedBy nvarchar(50),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(50),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON

UPDATE [dbo].[DmBoPhanNghiepVu] SET
	[DmPhongBanFK] = @DmPhongBanFK,
	[TenBoPhanNghiepVu] = @TenBoPhanNghiepVu,
	[DmNgonNguREF] = @DmNgonNguREF,
	[GhiChu] = @GhiChu,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[DmBoPhanNghiepVuID] = @DmBoPhanNghiepVuID

--endregion

```
