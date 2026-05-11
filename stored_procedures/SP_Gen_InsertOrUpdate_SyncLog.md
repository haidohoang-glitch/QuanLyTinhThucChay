# Stored Procedure: `Gen_InsertOrUpdate_SyncLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-11 15:02:50.803000
- **Ngày sửa cuối**: 2017-09-11 15:02:50.817000

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
| `@SQLServerTableName` | `nvarchar(400)` | No |
| `@SQLServerStoreProcedure` | `nvarchar(400)` | No |
| `@SQLServerParametersStoreProcedure` | `nvarchar(400)` | No |
| `@Parameters` | `nvarchar(400)` | No |
| `@SQLServerKeys` | `nvarchar(400)` | No |
| `@IsMoveData` | `nvarchar(400)` | No |
| `@KichAt` | `nvarchar(400)` | No |
| `@SQLParametersAdjusting` | `nvarchar(400)` | No |
| `@IsModifiedSQLTableStructure` | `nvarchar(400)` | No |
| `@SQLServerIP` | `nvarchar(400)` | No |
| `@SQLDatabaseName` | `nvarchar(400)` | No |
| `@TimeTotal` | `int(4)` | No |
| `@Content` | `nvarchar(400)` | No |
| `@RecordStatus` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_SyncLog] 	
@ProductID nvarchar (200) ,	
@HinhThucQuangCaoID nvarchar (200) ,	
@ProductName nvarchar (200) ,	
@ProductGroup nvarchar (200) ,	
@MySQLTableName nvarchar (200) ,	
@MySQLStoreProcedure nvarchar (200) ,	
@MySQLDatabase nvarchar (200) ,	
@MySQLServer nvarchar (200) ,	
@SQLServerTableName nvarchar (200) ,	
@SQLServerStoreProcedure nvarchar (200) ,	
@SQLServerParametersStoreProcedure nvarchar (200) ,	
@Parameters nvarchar (200) ,	
@SQLServerKeys nvarchar (200) ,	
@IsMoveData nvarchar (200) ,	
@KichAt nvarchar (200) ,	
@SQLParametersAdjusting nvarchar (200) ,	
@IsModifiedSQLTableStructure nvarchar (200) ,	
@SQLServerIP nvarchar (200) ,	
@SQLDatabaseName nvarchar (200) ,	
@TimeTotal int ,	
@Content nvarchar (200) ,	
@RecordStatus int ,	
@CreatedBy nvarchar (200) ,	
@CreatedAt datetime 	
As 	
INSERT INTO [dbo].[SyncLog] (	
[ProductID],	
[HinhThucQuangCaoID],	
[ProductName],	
[ProductGroup],	
[MySQLTableName],	
[MySQLStoreProcedure],	
[MySQLDatabase],	
[MySQLServer],	
[SQLServerTableName],	
[SQLServerStoreProcedure],	
[SQLServerParametersStoreProcedure],	
[Parameters],	
[SQLServerKeys],	
[IsMoveData],	
[KichAt],	
[SQLParametersAdjusting],	
[IsModifiedSQLTableStructure],	
[SQLServerIP],	
[SQLDatabaseName],	
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
@SQLServerTableName,	
@SQLServerStoreProcedure,	
@SQLServerParametersStoreProcedure,	
@Parameters,	
@SQLServerKeys,	
@IsMoveData,	
@KichAt,	
@SQLParametersAdjusting,	
@IsModifiedSQLTableStructure,	
@SQLServerIP,	
@SQLDatabaseName,	
@TimeTotal,	
@Content,	
@RecordStatus,	
@CreatedBy,	
@CreatedAt)

```
