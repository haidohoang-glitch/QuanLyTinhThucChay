# Stored Procedure: `sp_TenChienDich_TimKiem`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 14:53:58.500000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.703000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenChienDich` | `nvarchar(512)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[sp_TenChienDich_TimKiem]
@TenChienDich NVARCHAR(256)
AS
BEGIN
	SET NOCOUNT ON;
	
	SELECT TOP 50 DmChienDichID AS id,  TenChienDich as ten 
	FROM DmChienDichNhanhang AS t WHERE t.TenChienDich LIKE '%' + @TenChienDich +'%'
END

```
