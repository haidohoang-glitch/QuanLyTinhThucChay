# Stored Procedure: `bi_DeleteDotChayHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-11 09:05:58.850000
- **Ngày sửa cuối**: 2014-11-19 12:16:50.810000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DotChayHopDongChiTietId` | `varchar(50)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[bi_DeleteDotChayHopDongChiTiet]
	@DotChayHopDongChiTietId VARCHAR(50) 
AS
	SET NOCOUNT ON
	UPDATE [dbo].[DotChayHopDongChiTiet]
	SET    DeletedStatus  = 1
	WHERE  DotChayHopDongChiTietID  = CAST(@DotChayHopDongChiTietId AS INT)

```
