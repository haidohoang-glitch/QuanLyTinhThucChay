# Stored Procedure: `AspNet_SqlCacheUpdateChangeIdStoredProcedure`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-27 15:52:13.267000
- **Ngày sửa cuối**: 2014-11-19 12:17:54.497000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@tableName` | `nvarchar(900)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE dbo.AspNet_SqlCacheUpdateChangeIdStoredProcedure 
             @tableName NVARCHAR(450) 
         AS

         BEGIN 
             UPDATE dbo.AspNet_SqlCacheTablesForChangeNotification WITH (ROWLOCK) SET changeId = changeId + 1 
             WHERE tableName = @tableName
         END
   

```
