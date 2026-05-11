# Stored Procedure: `sp_ChuSoHuuNhanHang_TimKiem`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 14:53:58.453000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.710000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenChuSoHuu` | `nvarchar(512)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[sp_ChuSoHuuNhanHang_TimKiem]
@TenChuSoHuu NVARCHAR(256)
AS
BEGIN
	SET NOCOUNT ON;
	
	SELECT TOP 50 DmChuSoHuuID AS id,  TenChuSoHuu as ten 
	FROM DmChuSoHuuNhanhang AS t WHERE t.TenChuSoHuu LIKE '%' + @TenChuSoHuu +'%'
END

```
