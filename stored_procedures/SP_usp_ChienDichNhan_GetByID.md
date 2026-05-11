# Stored Procedure: `usp_ChienDichNhan_GetByID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 14:53:58.903000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.417000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmChienDichID` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_ChienDichNhan_GetByID]
	@DmChienDichID INT
AS
BEGIN
	SET NOCOUNT ON;
	SELECT cd.DmChienDichID,
	       cd.TenChienDich,
	       cd.Ghichu
	FROM   DmChienDichNhanhang cd
	WHERE  cd.DmChienDichID = @DmChienDichID
END

```
