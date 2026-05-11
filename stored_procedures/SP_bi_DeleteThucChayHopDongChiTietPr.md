# Stored Procedure: `bi_DeleteThucChayHopDongChiTietPr`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-11 08:37:31.110000
- **Ngày sửa cuối**: 2014-11-19 12:17:54.470000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayHopDongChiTietPrId` | `varchar(50)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[bi_DeleteThucChayHopDongChiTietPr]
	@ThucChayHopDongChiTietPrId VARCHAR(50) 
AS
	SET NOCOUNT ON
	UPDATE [dbo].[ThucChayHopDongChiTietPr]
	SET    DeletedStatus  = 1
	WHERE  ThucChayHopDongChiTietPrID  = CAST(@ThucChayHopDongChiTietPrId AS INT)

```
