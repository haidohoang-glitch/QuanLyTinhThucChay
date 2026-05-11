# Stored Procedure: `bi_DeleteThucChayHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-11 08:55:42.390000
- **Ngày sửa cuối**: 2014-11-19 12:16:51.180000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayHopDongChiTietId` | `varchar(50)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[bi_DeleteThucChayHopDongChiTiet]
	@ThucChayHopDongChiTietId VARCHAR(50) 
AS
	SET NOCOUNT ON
	UPDATE [dbo].[ThucChayHopDongChiTiet]
	SET    DeletedStatus  = 1
	WHERE  ThucChayHopDongChiTietID  = CAST(@ThucChayHopDongChiTietId AS INT)

```
