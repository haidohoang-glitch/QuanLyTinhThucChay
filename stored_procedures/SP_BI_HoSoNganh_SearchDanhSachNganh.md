# Stored Procedure: `BI_HoSoNganh_SearchDanhSachNganh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-25 16:17:14.957000
- **Ngày sửa cuối**: 2015-06-25 16:17:14.957000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Keyword` | `nvarchar(600)` | No |

## Definition (Source Code)

```sql
CREATE  PROCEDURE [dbo].[BI_HoSoNganh_SearchDanhSachNganh] ( @Keyword NVARCHAR(300) )
AS 
    BEGIN
        SELECT  *
        FROM    ( SELECT    DmNganhHangREF AS NganhHangID ,
                            TenNganhHang ,
                            TenNganhHang + ' (Level='
                            + CONVERT(NVARCHAR(50), Levels) + ')' TenNganhHangShow ,
                            STT
                  FROM      dbo.DmCaseNganhHang
                ) A
        WHERE   A.TenNganhHang LIKE '%' + @Keyword + '%'
        ORDER BY A.STT ,
                A.TenNganhHang
    END

```
