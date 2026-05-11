# Function: `fn_GetListWhereReport`

- **Loại**: SQL_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2015-03-26 11:48:37.897000
- **Ngày sửa cuối**: 2015-03-26 11:48:37.897000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |
| `@StartTableName` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
-- --SELECT * FROM dbo.[fn_GetListWhereReport] ('2013-01-01','2014-09-15','HopDong')
CREATE FUNCTION [dbo].[fn_GetListWhereReport]
(	
	-- Add the parameters for the function here
	@FromDate DATETIME,
	@ToDate DATETIME,
	@StartTableName NVARCHAR(200)
)
RETURNS @ReturnTable TABLE 
   (
   	 STT INT,
   	 TableName NVARCHAR(200),
   	 sWhere NVARCHAR(200)
	)
AS
BEGIN
	DECLARE  @i INT SET @i =1
	DECLARE @TableTime TABLE 
      (
      	stt INT,
	    FromDate DATETIME,
		Todate DATETIME,
		isNam INT,
		isQuy INT,
		isThang INT,
		isNgay INT ,
		Nam INT,
		Quy INT,
		Thang INT
      )
      INSERT INTO  @TableTime
      SELECT ROW_NUMBER() OVER(ORDER BY @FromDate) AS stt,* FROM dbo.fn_getTableTime(@FromDate,@ToDate) fgtt 
      WHILE @i <=(SELECT COUNT(*) FROM @TableTime)
		  BEGIN
	      	     IF (SELECT isNam FROM @TableTime WHERE stt = @i) = 1
	      	         INSERT INTO @ReturnTable
	      	         (
	      	         	STT,
	      	         	TableName,
	      	         	sWhere
	      	         )
	      	         VALUES
	      	         (
	      	         	@i,
	      	         	@StartTableName +'_'+'Nam',
	      	         	' Nam = CAST('''+CAST((SELECT Nam FROM @TableTime WHERE stt = @i) AS NVARCHAR(10))+''' as int) '
	      	         )
	      	     ELSE 
	      	     	IF (SELECT isQuy FROM @TableTime WHERE stt = @i) = 1
	      	     	INSERT INTO @ReturnTable
	      	         (
	      	         	STT,
	      	         	TableName,
	      	         	sWhere
	      	         )
	      	         VALUES
	      	         (
	      	         	@i,
	      	         	@StartTableName +'_'+'Quy',
	      	         	' Nam = CAST('''+CAST((SELECT Nam FROM @TableTime WHERE stt = @i) AS NVARCHAR(10))+''' as int)
	      	         	AND Quy = CAST('''+CAST((SELECT Quy FROM @TableTime WHERE stt = @i) AS NVARCHAR(10))+''' as int) '
	      	         )
	      	         ELSE
	      	         	IF (SELECT isThang FROM @TableTime WHERE stt = @i) = 1
	      	         	INSERT INTO @ReturnTable
	      				(
	      					
	      	         		STT,
	      	         		TableName,
	      	         		sWhere
	      	            )
	      				 VALUES
	      				 (
	      				 	@i,
	      	         		@StartTableName +'_'+'Thang',
	      	         		' Nam = CAST('''+CAST((SELECT Nam FROM @TableTime WHERE stt = @i) AS NVARCHAR(10))+''' as int)
	      	         		AND Thang = CAST('''+CAST((SELECT Thang FROM @TableTime WHERE stt = @i) AS NVARCHAR(10))+''' as int) '
	      				 )
	      				ELSE
	      				INSERT INTO @ReturnTable
	      	            (
	      	         		STT,
	      	         		TableName,
	      	         		sWhere
	      	            )
	      	             VALUES
	      	            (
	      	            @i,
	      	         	@StartTableName +'_'+'Ngay',
	      	            'NgayThucHien BETWEEN '''+CONVERT(NVARCHAR(50),(SELECT tt.FromDate FROM @TableTime tt WHERE stt = @i))+''' AND  '''+CONVERT(NVARCHAR(50),(SELECT tt.Todate FROM @TableTime tt WHERE stt =@i))+''' '
	      	            )	
	      	    SET @i += 1
		  END
RETURN 
END

```
