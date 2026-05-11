# Stored Procedure: `AspNet_SqlCachePollingStoredProcedure`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-27 15:52:13.260000
- **Ngày sửa cuối**: 2014-11-19 12:17:54.480000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE dbo.AspNet_SqlCachePollingStoredProcedure AS
         SELECT tableName, changeId FROM dbo.AspNet_SqlCacheTablesForChangeNotification
         RETURN 0

```
