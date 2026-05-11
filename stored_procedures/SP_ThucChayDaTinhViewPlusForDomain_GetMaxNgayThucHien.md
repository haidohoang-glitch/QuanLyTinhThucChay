# Stored Procedure: `ThucChayDaTinhViewPlusForDomain_GetMaxNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-05-13 18:13:44.363000
- **Ngày sửa cuối**: 2015-05-13 18:13:44.363000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[ThucChayDaTinhViewPlusForDomain_GetMaxNgayThucHien]
AS 
    BEGIN
        SELECT  MAX([NgayThucHien])
        FROM    dbo.ThucChayDaTinhViewPlusForDomain
    END


```
