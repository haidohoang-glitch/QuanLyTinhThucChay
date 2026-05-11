# Stored Procedure: `usp_SelectAllUser`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-24 08:59:32.817000
- **Ngày sửa cuối**: 2014-11-19 12:16:45.247000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Keyword` | `nvarchar(8000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<SonVM>
-- Create date: <24,05,2014>
-- Description:	<Lấy danh sách tên đăng nhập - hòm thư>
-- usp_SelectAllUser ''
-- =============================================
CREATE proc [dbo].[usp_SelectAllUser] 
	@Keyword NVARCHAR(4000)
AS
BEGIN	
	SELECT TOP 30 A.Username + ' - ' + A.Email AS [text], A.Username + ' - ' + A.Email AS label, A.OxUserREF AS id, A.Username AS [value] FROM AdminUser A
	WHERE A.Email <> '' AND (A.Username LIKE '%' + @Keyword + '%' OR A.Email LIKE '%' + @Keyword + '%')
	ORDER BY A.Email		
END

```
