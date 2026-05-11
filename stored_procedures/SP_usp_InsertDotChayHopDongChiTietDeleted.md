# Stored Procedure: `usp_InsertDotChayHopDongChiTietDeleted`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-08-12 15:01:49.603000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.740000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DotChayHopDongChiTietID` | `int(4)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_InsertDotChayHopDongChiTiet]
-- Create Date: Tuesday, May 28, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_InsertDotChayHopDongChiTietDeleted]
	@DotChayHopDongChiTietID int,
	@LastModifiedAt datetime
AS

SET NOCOUNT ON
if(exists(select * from [DotChayHopDongChiTietDeleted] where [DotChayHopDongChiTietID] = @DotChayHopDongChiTietID))
BEGIN
UPDATE [dbo].[DotChayHopDongChiTietDeleted] SET
	[LastModifiedAt] = @LastModifiedAt
WHERE
	[DotChayHopDongChiTietID] = @DotChayHopDongChiTietID

DELETE FROM dbo.DotChayHopDongChiTiet WHERE DotChayHopDongChiTietID = @DotChayHopDongChiTietID
END
ELSE
BEGIN
INSERT INTO [dbo].[DotChayHopDongChiTietDeleted] (
	[DotChayHopDongChiTietID],
	[LastModifiedAt],
	DeletedStatus
) VALUES (
	@DotChayHopDongChiTietID,
	@LastModifiedAt,
	0
)
DELETE FROM dbo.DotChayHopDongChiTiet WHERE DotChayHopDongChiTietID = @DotChayHopDongChiTietID
END

```
