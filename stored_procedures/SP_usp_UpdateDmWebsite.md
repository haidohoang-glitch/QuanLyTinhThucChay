# Stored Procedure: `usp_UpdateDmWebsite`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-07 00:32:33.450000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.103000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmWebsiteID` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(400)` | No |
| `@WebsiteLink` | `nvarchar(510)` | No |
| `@GhiChu` | `nvarchar(8000)` | No |
| `@Code` | `nvarchar(400)` | No |
| `@DmGroupTypeREF` | `int(4)` | No |
| `@IsThuongMaiDienTu` | `int(4)` | No |
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
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_UpdateDmWebsite]
-- Create Date: Thursday, June 06, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_UpdateDmWebsite]
	@DmWebsiteID int,
	@TenWebsite nvarchar(200),
	@WebsiteLink nvarchar(255),
	@GhiChu nvarchar(4000),
	@Code nvarchar(200),
	@DmGroupTypeREF int,
	@IsThuongMaiDienTu int,
	@CreatedBy nvarchar(1),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(1),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON

UPDATE [dbo].[DmWebsite] SET
	[TenWebsite] = @TenWebsite,
	[WebsiteLink] = @WebsiteLink,
	[GhiChu] = @GhiChu,
	[Code] = @Code,
	[DmGroupTypeREF] = @DmGroupTypeREF,
	[IsThuongMaiDienTu] = @IsThuongMaiDienTu,
	[LastModifiedBy] = @LastModifiedBy,
	[LastModifiedAt] = @LastModifiedAt,
	[DeletedStatus] = @DeletedStatus,
	[PrintStatus] = @PrintStatus,
	[RecordStatus] = @RecordStatus
WHERE
	[DmWebsiteID] = @DmWebsiteID

--endregion

```
