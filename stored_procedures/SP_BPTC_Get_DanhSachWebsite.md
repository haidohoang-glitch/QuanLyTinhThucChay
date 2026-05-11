# Stored Procedure: `BPTC_Get_DanhSachWebsite`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:50.873000
- **Ngày sửa cuối**: 2015-06-11 18:17:50.873000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Keyword` | `nvarchar(510)` | No |

## Definition (Source Code)

```sql

CREATE PROC [dbo].[BPTC_Get_DanhSachWebsite] ( @Keyword NVARCHAR(255) )
AS 
    BEGIN
        DECLARE @RecordCound INT = 100
        SELECT TOP ( @RecordCound )
                A.DmWebsiteReportingdbID AS [value] ,
                A.TenWebsite AS [text]
        FROM    DmWebsiteReportingdb A
        WHERE   A.TenWebsite LIKE N'' + @Keyword + '%'
                AND A.DeletedStatus = 0
                AND A.TenWebsite <> ''
                AND A.TenWebsite IS NOT NULL
        ORDER BY A.TenWebsite
    END

```
