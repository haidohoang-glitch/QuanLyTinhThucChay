# Stored Procedure: `Gen_InsertOrUpdate_ThucChayCPV`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-13 14:55:52.673000
- **Ngày sửa cuối**: 2014-11-19 12:16:53.223000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@typeproduct` | `int(4)` | No |
| `@ProductName` | `nvarchar(400)` | No |
| `@bannerid` | `int(4)` | No |
| `@totalview` | `int(4)` | No |
| `@percent_rate` | `float(8)` | No |
| `@CPV` | `float(8)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucChayCPV] 	
@typeproduct int ,	
@ProductName nvarchar (200) ,	
@bannerid int ,	
@totalview int ,	
@percent_rate float ,	
@CPV float ,	
@NgayThucHien datetime 	
As 	
INSERT INTO [dbo].[ThucChayCPV] (	
[typeproduct],	
[ProductName],	
[bannerid],	
[totalview],	
[percent_rate],	
[CPV],	
[NgayThucHien])	
Values 	
(	
@typeproduct,	
@ProductName,	
@bannerid,	
@totalview,	
@percent_rate,	
@CPV,	
@NgayThucHien)

```
