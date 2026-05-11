# Stored Procedure: `Gen_Delete_ThucChayDaTinhBoxAppSSV`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 13:51:12.047000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.607000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_Delete_ThucChayDaTinhBoxAppSSV]
	
@NgayThucHien DateTime
AS
BEGIN
delete from ThucChayDaTinhBoxAppSSV where  1=1  and NgayThucHien = @NgayThucHien
END

```
