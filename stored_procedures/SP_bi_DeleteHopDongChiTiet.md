# Stored Procedure: `bi_DeleteHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-10 18:32:23.453000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.500000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietId` | `varchar(50)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[bi_DeleteHopDongChiTiet]
	@HopDongChiTietId VARCHAR(50) 
AS
	SET NOCOUNT ON
	UPDATE [dbo].[HopDongChiTiet]
	SET    DeletedStatus  = 1
	WHERE  HopDongChiTietID  = CAST(@HopDongChiTietId AS INT)

```
