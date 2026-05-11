# Stored Procedure: `usp_UpdateDmBoPhan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-20 16:13:03.013000
- **Ngày sửa cuối**: 2014-10-14 10:39:39.957000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmBoPhanID` | `int(4)` | No |
| `@MaBoPhan` | `nvarchar(100)` | No |
| `@TenBoPhan` | `nvarchar(400)` | No |
| `@DmPhongBanREF` | `int(4)` | No |
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
-- Stored Procedure Name: [dbo].[usp_UpdateDmBoPhan]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateDmBoPhan]
	@DmBoPhanID int,
	@MaBoPhan nvarchar(50),
	@TenBoPhan nvarchar(200),
	@DmPhongBanREF int,
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

UPDATE [dbo].[DmBoPhan] SET
	[MaBoPhan] = @MaBoPhan,
	[TenBoPhan] = @TenBoPhan,
	[DmPhongBanREF] = @DmPhongBanREF,
	[GhiChu] = @GhiChu,
	[Active] = @Active,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[DmBoPhanID] = @DmBoPhanID

--endregion


```
