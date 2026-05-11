# Stored Procedure: `sp_NhaPhanPhoiNhan_TimKiem`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 14:53:58.850000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.707000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenNhaPhanPhoi` | `nvarchar(512)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[sp_NhaPhanPhoiNhan_TimKiem]
@TenNhaPhanPhoi NVARCHAR(256)
AS
BEGIN
	SET NOCOUNT ON;
	
	SELECT TOP 50 DmNhaPhanPhoiID AS id,  TenNhaPhanPhoi as ten 
	FROM DmNhaPhanPhoiNhanhang AS t WHERE t.TenNhaPhanPhoi LIKE '%' + @TenNhaPhanPhoi +'%'
END

```
