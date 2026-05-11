# Stored Procedure: `usp_ChienDichNhan_GetAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 14:54:02.667000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.973000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@TenChienDich` | `nvarchar(2048)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_ChienDichNhan_GetAll]
	@PageIndex INT = 1,
	@RecordCount INT = 2,
	@TenChienDich NVARCHAR(1024)
	
AS
BEGIN
	SET NOCOUNT ON;
	--SET TRANSACTION ISOLATION LEVEL READ COMMITTED
	DECLARE @SQL NVARCHAR(MAX);
	
	DECLARE @sTenChienDich NVARCHAR(256);
	set @TenChienDich = replace(@TenChienDich,'''', '''''')
	
	IF (@TenChienDich <> '')
		SET @sTenChienDich = 'AND TenChienDich COLLATE  SQL_Latin1_General_CP1_CI_AI LIKE N''%'+ @TenChienDich +'%''';
	ELSE
		SET @sTenChienDich = ' ';
		
		
	SET @SQL = '
		
	WITH FileredList
	AS
	(
	    SELECT [DmChienDichID],
	           [TenChienDich],
	           [Ghichu],
	           [CreatedBy],
	           [CreatedAt],
	           [LastModidfiedBy],
	           CONVERT(VARCHAR(10), LastModifiedAt, 103) AS  LastModifiedAt,
	           [DeletedStatus],
	           [PrintStatus],
	           [RecordStatus],
	           ROW_NUMBER() OVER(ORDER BY [LastModifiedAt] DESC) AS [RowNumber]
	    FROM   DmChienDichNhanhang n
	    WHERE  DeletedStatus <> 1 '+ @sTenChienDich +'
	) 
	SELECT *
	FROM   FileredList 
	WHERE  RowNumber BETWEEN '+ CAST(((@PageIndex -1) * @RecordCount + 1) AS NVARCHAR(50)) +' AND '+ CAST((@PageIndex * @RecordCount) AS NVARCHAR(50))+';';	
	
	EXEC sp_executesql @SQL;
	
END

```
