# Stored Procedure: `usp_InsertDmBoPhanNghiepVu`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-16 11:38:07.960000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.273000

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
-- Stored Procedure Name: [dbo].[usp_InsertDmBoPhanNghiepVu]
-- Create Date: Thursday, December 16, 2010
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_InsertDmBoPhanNghiepVu]
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
if(exists(select * from DmBoPhanNghiepVu where DmBoPhanNghiepVuID = @DmBoPhanNghiepVuID))
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
else
INSERT INTO [dbo].[DmBoPhanNghiepVu] (
	[DmBoPhanNghiepVuID],
	[DmPhongBanFK],
	[TenBoPhanNghiepVu],
	[DmNgonNguREF],
	[GhiChu],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
) VALUES (
	@DmBoPhanNghiepVuID,
	@DmPhongBanFK,
	@TenBoPhanNghiepVu,
	@DmNgonNguREF,
	@GhiChu,
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
