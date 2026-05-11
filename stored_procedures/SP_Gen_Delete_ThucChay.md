# Stored Procedure: `Gen_Delete_ThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-11 15:02:50.717000
- **Ngày sửa cuối**: 2017-09-11 15:02:50.737000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@TypeProduct` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_Delete_ThucChay]
	
@NgayThucHien DateTime,	
@TypeProduct int
AS
BEGIN
delete from ThucChay where  1=1  and NgayThucHien = @NgayThucHien and TypeProduct = @TypeProduct
END


```
