# Stored Procedure: `ThucChayViewPlusUsers_Delete`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-05-13 18:13:43.367000
- **Ngày sửa cuối**: 2015-06-26 17:13:41.187000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[ThucChayViewPlusUsers_Delete]
    (
      @NgayThucHien DATETIME
    )
AS 
    BEGIN
        SET NOCOUNT ON ;
	
        DELETE  FROM ThucChayViewPlusForUsers
        WHERE   CONVERT(DATE,NgayThucHien) = CONVERT(DATE, @NgayThucHien)	
      	
    END


```
