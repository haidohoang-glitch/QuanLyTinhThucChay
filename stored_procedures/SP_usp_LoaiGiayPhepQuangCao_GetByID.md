# Stored Procedure: `usp_LoaiGiayPhepQuangCao_GetByID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-22 09:41:51.587000
- **Ngày sửa cuối**: 2014-11-19 12:16:46.230000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmLoaiGiayPhepID` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_LoaiGiayPhepQuangCao_GetByID]
	@DmLoaiGiayPhepID INT
AS
BEGIN
	SELECT A.DmLoaiGiayPhepID,
	       A.TenLoaiGiayPhep,
	       A.Ghichu,
	       A.DeletedStatus
	FROM   DmLoaiGiayPhepQuangCao A
	WHERE  A.DmLoaiGiayPhepID = @DmLoaiGiayPhepID;
END

```
