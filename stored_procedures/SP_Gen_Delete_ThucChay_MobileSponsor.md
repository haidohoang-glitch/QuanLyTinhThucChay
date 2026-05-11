# Stored Procedure: `Gen_Delete_ThucChay_MobileSponsor`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-29 16:59:33.710000
- **Ngày sửa cuối**: 2014-12-29 16:59:33.710000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@TypeProduct` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_Delete_ThucChay_MobileSponsor]
	
@NgayThucHien DateTime,	
@TypeProduct int
AS
BEGIN
delete from ThucChay_Mobiles_Sponsor where  1=1  and NgayThucHien = @NgayThucHien and TypeProduct = @TypeProduct
END

```
