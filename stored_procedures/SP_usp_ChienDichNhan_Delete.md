# Stored Procedure: `usp_ChienDichNhan_Delete`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 14:53:58.480000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.420000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmChienDichID` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_ChienDichNhan_Delete]
	@DmChienDichID INT
AS
BEGIN
	SET NOCOUNT ON;
	
	DELETE 
	FROM   [dbo].[DmChienDichNhanhang]
	WHERE  [DmChienDichID] = @DmChienDichID
END

```
