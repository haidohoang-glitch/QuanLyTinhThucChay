# Stored Procedure: `AspNet_SqlCacheQueryRegisteredTablesStoredProcedure`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-27 15:52:13.273000
- **Ngày sửa cuối**: 2014-11-19 12:17:54.507000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE dbo.AspNet_SqlCacheQueryRegisteredTablesStoredProcedure 
         AS
         SELECT tableName FROM dbo.AspNet_SqlCacheTablesForChangeNotification   

```
