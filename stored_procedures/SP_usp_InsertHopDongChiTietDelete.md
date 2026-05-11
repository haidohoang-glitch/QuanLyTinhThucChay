# Stored Procedure: `usp_InsertHopDongChiTietDelete`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-27 16:28:20.150000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.753000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_InsertHopDongChiTietDelete]
	@HopDongChiTietID int,
	@LastModifiedAt datetime
AS

SET NOCOUNT ON

if(exists(select * from [dbo].[HopDongChiTietDelete] where HopDongChiTietID = @HopDongChiTietID))
UPDATE [dbo].[HopDongChiTietDelete] SET
	[LastModifiedAt] = @LastModifiedAt
WHERE
	[HopDongChiTietID] = @HopDongChiTietID
else
INSERT INTO [dbo].[HopDongChiTietDelete] (
	[HopDongChiTietID],
	[LastModifiedAt]
) VALUES (
	@HopDongChiTietID,
	@LastModifiedAt
	)

```
