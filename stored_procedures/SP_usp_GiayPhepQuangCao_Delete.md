# Stored Procedure: `usp_GiayPhepQuangCao_Delete`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-22 09:41:53.213000
- **Ngày sửa cuối**: 2014-11-19 12:16:48.543000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@GiayPhepQuangCaoID` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_GiayPhepQuangCao_Delete]
	@GiayPhepQuangCaoID INT
AS
BEGIN
	SET NOCOUNT ON;
	
	UPDATE [dbo].[GiayPhepQuangCaoNhan]
	SET    DeletedStatus = 1
	WHERE  [GiayPhepQuangCaoID] = @GiayPhepQuangCaoID;
END

```
