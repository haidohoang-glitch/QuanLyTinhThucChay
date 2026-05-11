# Stored Procedure: `usp_InsertDmWebsite`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-07 00:32:33.197000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.223000

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
-- Stored Procedure Name: [dbo].[usp_InsertDmWebsite]
-- Create Date: Thursday, June 06, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_InsertDmWebsite]
	@DmWebsiteID int,
	@TenWebsite nvarchar(200),
	@WebsiteLink nvarchar(255),
	@GhiChu nvarchar(4000),
	@Code nvarchar(200),
	@DmGroupTypeREF int,
	@IsThuongMaiDienTu int,
	@CreatedBy nvarchar(50),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(50),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
AS

SET NOCOUNT ON
if(exists(select * from [DmWebsite] where  DmWebsiteID = @DmWebsiteID))
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
else
INSERT INTO [dbo].[DmWebsite] (
	[DmWebsiteID],
	[TenWebsite],
	[WebsiteLink],
	[GhiChu],
	[Code],
	[DmGroupTypeREF],
	[IsThuongMaiDienTu],
	[CreatedBy],
	[CreatedAt],
	[LastModifiedBy],
	[LastModifiedAt],
	[DeletedStatus],
	[PrintStatus],
	[RecordStatus]
) VALUES (
	@DmWebsiteID,
	@TenWebsite,
	@WebsiteLink,
	@GhiChu,
	@Code,
	@DmGroupTypeREF,
	@IsThuongMaiDienTu,
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
