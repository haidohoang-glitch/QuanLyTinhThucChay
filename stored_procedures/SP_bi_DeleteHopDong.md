# Stored Procedure: `bi_DeleteHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-10 14:21:38.193000
- **Ngày sửa cuối**: 2014-11-19 12:16:50.790000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `varchar(50)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[bi_DeleteHopDong]
	@HopDongID VARCHAR(50) 
AS
	SET NOCOUNT ON
	UPDATE [dbo].[HopDong]
	SET    DeletedStatus  = 1
	WHERE  [HopDongID]    = CAST(@HopDongID AS INT)

```
