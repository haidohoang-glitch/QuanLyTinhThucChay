# Stored Procedure: `usp_DeleteDotChayHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-29 03:14:32.640000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.083000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DotChayHopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
--=============================================
-- Author:   Administrator
-- Stored Procedure Name: [dbo].[usp_DeleteDotChayHopDongChiTiet]
-- Create Date: Tuesday, May 28, 2013
-- Description: 
--=============================================

CREATE PROCEDURE [dbo].[usp_DeleteDotChayHopDongChiTiet]
	@DotChayHopDongChiTietID int
AS

SET NOCOUNT ON

Update [dbo].[DotChayHopDongChiTiet]
Set DeletedStatus = 1
WHERE
	[DotChayHopDongChiTietID] = @DotChayHopDongChiTietID

```
