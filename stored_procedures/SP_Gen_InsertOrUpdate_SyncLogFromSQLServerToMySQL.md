# Stored Procedure: `Gen_InsertOrUpdate_SyncLogFromSQLServerToMySQL`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-18 11:57:18.147000
- **Ngày sửa cuối**: 2015-03-18 11:57:18.147000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ProductID` | `nvarchar(400)` | No |
| `@HinhThucQuangCaoID` | `nvarchar(400)` | No |
| `@ProductName` | `nvarchar(400)` | No |
| `@ProductGroup` | `nvarchar(400)` | No |
| `@MySQLTableName` | `nvarchar(400)` | No |
| `@MySQLStoreProcedure` | `nvarchar(400)` | No |
| `@MySQLDatabase` | `nvarchar(400)` | No |
| `@MySQLServer` | `nvarchar(400)` | No |
| `@MySQLParametersStoreProcedure` | `nvarchar(400)` | No |
| `@MySQLKeys` | `nvarchar(400)` | No |
| `@SQLServerTableName` | `nvarchar(400)` | No |
| `@SQLServerStoreProcedure` | `nvarchar(400)` | No |
| `@SQLServerIP` | `nvarchar(400)` | No |
| `@SQLDatabaseName` | `nvarchar(400)` | No |
| `@Parameters` | `nvarchar(400)` | No |
| `@IsMoveData` | `nvarchar(400)` | No |
| `@KichAt` | `nvarchar(400)` | No |
| `@MySQLParametersAdjusting` | `nvarchar(400)` | No |
| `@IsModifiedMySQLTableStructure` | `nvarchar(400)` | No |
| `@RecordTotal` | `int(4)` | No |
| `@TimeTotal` | `int(4)` | No |
| `@Content` | `nvarchar(400)` | No |
| `@RecordStatus` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |

## Definition (Source Code)

```sql
Create PROCEDURE [dbo].[Gen_InsertOrUpdate_SyncLogFromSQLServerToMySQL] 	
@ProductID nvarchar (200) ,	
@HinhThucQuangCaoID nvarchar (200) ,	
@ProductName nvarchar (200) ,	
@ProductGroup nvarchar (200) ,	
@MySQLTableName nvarchar (200) ,	
@MySQLStoreProcedure nvarchar (200) ,	
@MySQLDatabase nvarchar (200) ,	
@MySQLServer nvarchar (200) ,	
@MySQLParametersStoreProcedure nvarchar (200) ,	
@MySQLKeys nvarchar (200) ,	
@SQLServerTableName nvarchar (200) ,	
@SQLServerStoreProcedure nvarchar (200) ,	
@SQLServerIP nvarchar (200) ,	
@SQLDatabaseName nvarchar (200) ,	
@Parameters nvarchar (200) ,	
@IsMoveData nvarchar (200) ,	
@KichAt nvarchar (200) ,	
@MySQLParametersAdjusting nvarchar (200) ,	
@IsModifiedMySQLTableStructure nvarchar (200) ,	
@RecordTotal int ,	
@TimeTotal int ,	
@Content nvarchar (200) ,	
@RecordStatus int ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime 	
As 	
INSERT INTO [dbo].[SyncLogFromSQLServerToMySQL] (	
[ProductID],	
[HinhThucQuangCaoID],	
[ProductName],	
[ProductGroup],	
[MySQLTableName],	
[MySQLStoreProcedure],	
[MySQLDatabase],	
[MySQLServer],	
[MySQLParametersStoreProcedure],	
[MySQLKeys],	
[SQLServerTableName],	
[SQLServerStoreProcedure],	
[SQLServerIP],	
[SQLDatabaseName],	
[Parameters],	
[IsMoveData],	
[KichAt],	
[MySQLParametersAdjusting],	
[IsModifiedMySQLTableStructure],	
[RecordTotal],	
[TimeTotal],	
[Content],	
[RecordStatus],	
[CreatedBy],	
[CreatedAt])	
Values 	
(	
@ProductID,	
@HinhThucQuangCaoID,	
@ProductName,	
@ProductGroup,	
@MySQLTableName,	
@MySQLStoreProcedure,	
@MySQLDatabase,	
@MySQLServer,	
@MySQLParametersStoreProcedure,	
@MySQLKeys,	
@SQLServerTableName,	
@SQLServerStoreProcedure,	
@SQLServerIP,	
@SQLDatabaseName,	
@Parameters,	
@IsMoveData,	
@KichAt,	
@MySQLParametersAdjusting,	
@IsModifiedMySQLTableStructure,	
@RecordTotal,	
@TimeTotal,	
@Content,	
@RecordStatus,	
@CreatedBy,	
@CreatedAt)
```
