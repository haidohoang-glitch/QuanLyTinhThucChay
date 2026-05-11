# Stored Procedure: `sp_get_authen_key_PerformanceBaseAPI`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2023-07-19 14:58:00.887000
- **Ngày sửa cuối**: 2023-07-19 14:58:00.887000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@date` | `varchar(10)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[sp_get_authen_key_PerformanceBaseAPI]
@date VARCHAR(10) =NULL --'2023-07-13'
AS
BEGIN

	SET @date = ISNULL(@date, CONVERT(VARCHAR(10),GETDATE() - 1,120))
	PRINT @date;
	SELECT LOWER( CONVERT(NVARCHAR(32),HashBytes('MD5', '6i020mwer5bukujssx9n5imljinyq6'+  @date),2))
END

```
