# Stored Procedure: `Rpt_NhanHang_DanhSach_Nhan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-22 17:42:36.777000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.260000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@Keyword` | `nvarchar(8000)` | No |

## Definition (Source Code)

```sql
CREATE  PROC [dbo].[Rpt_NhanHang_DanhSach_Nhan]
	@StartDate DATETIME,
	@EndDate DATETIME,
	@Keyword NVARCHAR(4000)	
AS
BEGIN
	DECLARE @Sql NVARCHAR(4000)
	SET @Sql = 'SELECT DmNhanHangId, TenNhanHang FROM DmNhanHang dnh
				WHERE (' + @Keyword + ') AND dnh.DeletedStatus <> 1
				ORDER BY dnh.TenNhanHang ASC'	
	PRINT @Sql 
	EXEC (@Sql)	
END

```
