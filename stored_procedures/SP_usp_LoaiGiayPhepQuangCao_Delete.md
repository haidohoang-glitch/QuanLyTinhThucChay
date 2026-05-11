# Stored Procedure: `usp_LoaiGiayPhepQuangCao_Delete`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-22 09:41:51.617000
- **Ngày sửa cuối**: 2014-11-19 12:16:46.263000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmLoaiGiayPhepID` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_LoaiGiayPhepQuangCao_Delete]
	@DmLoaiGiayPhepID INT
AS
BEGIN
	UPDATE DmLoaiGiayPhepQuangCao
	SET    DeletedStatus = 1
	WHERE  DmLoaiGiayPhepID = @DmLoaiGiayPhepID;
END

```
