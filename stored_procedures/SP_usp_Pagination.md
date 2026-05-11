# Stored Procedure: `usp_Pagination`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-09 12:41:26.487000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.373000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@datasrc` | `nvarchar(400)` | No |
| `@orderBy` | `nvarchar(400)` | No |
| `@fieldlist` | `nvarchar(400)` | No |
| `@filter` | `nvarchar(400)` | No |
| `@pageNum` | `int(4)` | No |
| `@pageSize` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<SONVM>
-- Create date: <10/2013>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[usp_Pagination]
  @datasrc nvarchar(200)
 ,@orderBy nvarchar(200)
 ,@fieldlist nvarchar(200) = '*'
 ,@filter nvarchar(200) = ''
 ,@pageNum int = 1
 ,@pageSize int = NULL
AS
  SET NOCOUNT ON
  DECLARE
     @STMT nvarchar(max)         -- SQL to execute
    ,@recct int                  -- total # of records (for GridView paging interface)

  IF LTRIM(RTRIM(@filter)) = '' SET @filter = '1 = 1'
  IF @pageSize IS NULL BEGIN
    SET @STMT =  'SELECT   ' + @fieldlist +
                 'FROM     ' + @datasrc +
                 'WHERE    ' + @filter +
                 'ORDER BY ' + @orderBy
    EXEC (@STMT)                 -- return requested records
  END ELSE BEGIN
    --SET @STMT =  'SELECT   @recct = COUNT(*)
    --              FROM     ' + @datasrc + '
    --              WHERE    ' + @filter
    --EXEC sp_executeSQL @STMT, @params = N'@recct INT OUTPUT', @recct = @recct OUTPUT
    --SELECT @recct AS recct       -- return the total # of records

    DECLARE
      @lbound int,
      @ubound int

    SET @pageNum = ABS(@pageNum)
    SET @pageSize = ABS(@pageSize)
    IF @pageNum < 1 SET @pageNum = 1
    IF @pageSize < 1 SET @pageSize = 1
    SET @lbound = ((@pageNum - 1) * @pageSize)
    SET @ubound = @lbound + @pageSize + 1
    IF @lbound >= @recct BEGIN
      SET @ubound = @recct + 1
      SET @lbound = @ubound - (@pageSize + 1) -- return the last page of records if                                               
											  -- no records would be on the
                                              -- specified page
    END
    SET @STMT =  'SELECT  ' + @fieldlist + '
                  FROM    (
                            SELECT  ROW_NUMBER() OVER(ORDER BY ' + @orderBy + ') AS row, *
                            FROM    ' + @datasrc + '
                            WHERE   ' + @filter + '
                          ) AS tbl
                  WHERE
                          row > ' + CONVERT(varchar(9), @lbound) + ' AND
                          row < ' + CONVERT(varchar(9), @ubound)
    PRINT (@STMT)
    EXEC (@STMT)                 -- return requested records
  END

```
