# Stored Procedure: `usp_ChuSoHuuNhanHang_Delete`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 14:53:58.890000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.403000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmChuSoHuuID` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_ChuSoHuuNhanHang_Delete]
	@DmChuSoHuuID INT
AS
BEGIN
	SET NOCOUNT ON;
	
	DELETE 
	FROM   [dbo].[DmChuSoHuuNhanhang]
	WHERE  [DmChuSoHuuID] = @DmChuSoHuuID
END

```
