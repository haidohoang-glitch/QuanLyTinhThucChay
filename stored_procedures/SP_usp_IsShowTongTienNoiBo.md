# Stored Procedure: `usp_IsShowTongTienNoiBo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-24 10:17:25.757000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.313000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Username` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE proc [dbo].[usp_IsShowTongTienNoiBo]
	@Username NVARCHAR(50)
AS
BEGIN
	SELECT PartnerValue FROM AdminUser WHERE Username = @Username
END

```
