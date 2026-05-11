# Stored Procedure: `usp_Pagination_Count`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-09 12:41:40.917000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.367000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@datasrc` | `nvarchar(400)` | No |
| `@filter` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_Pagination_Count]
  @datasrc nvarchar(200)  
 ,@filter nvarchar(200) = '' 
AS
BEGIN
  DECLARE
     @STMT nvarchar(max)         -- SQL to execute
    ,@recct int                  -- total # of records (for GridView paging interface)

  IF LTRIM(RTRIM(@filter)) = '' SET @filter = '1 = 1'  
  
	SET @STMT =  'SELECT   @recct = COUNT(*)
				  FROM     ' + @datasrc + '
				  WHERE    ' + @filter
	EXEC sp_executeSQL @STMT, @params = N'@recct INT OUTPUT', @recct = @recct OUTPUT
	SELECT @recct AS recct       -- return the total # of records
END

```
