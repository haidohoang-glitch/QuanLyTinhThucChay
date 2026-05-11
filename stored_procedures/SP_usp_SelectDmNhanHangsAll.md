# Stored Procedure: `usp_SelectDmNhanHangsAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-27 10:17:16.313000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.390000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@RecordStatus` | `varchar(10)` | No |
| `@TenNhanhang` | `nvarchar(2048)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_SelectDmNhanHangsAll]
	@PageIndex INT = 1,
	@RecordCount INT = 2,
	@RecordStatus VARCHAR(10),
	@TenNhanhang NVARCHAR(1024)
	
AS
BEGIN
	SET NOCOUNT ON;
	--SET TRANSACTION ISOLATION LEVEL READ COMMITTED
	DECLARE @SQL NVARCHAR(MAX);
	
	DECLARE @Review VARCHAR(20);
	DECLARE @sTenNhanhang NVARCHAR(256);
	
	IF (@RecordStatus = '')
	    SET @Review = 'AND RecordStatus >=0'
	ELSE
	    SET @Review = 'AND RecordStatus =' + @RecordStatus;
	
	IF (@TenNhanhang <> '')
		SET @sTenNhanhang = 'AND TenNhanHang COLLATE  SQL_Latin1_General_CP1_CI_AI LIKE N''%'+ @TenNhanhang +'%''';
	ELSE
		SET @sTenNhanhang = ' ';
		
	SET @SQL = '
		
	WITH FileredList
	AS
	(
	    SELECT [DmNhanHangID],
	           [TenNhanHang],
	           [DmNghanhHangREF] = STUFF(
			   (
				   SELECT '', '' + md.TenNghanhHang
				   FROM   DmNghanhHang md
				   WHERE md.DeletedStatus <> 1 AND md.DmNghanhHangID IN (SELECT *
												FROM   dbo.Split(n.DmNghanhHangREF, '',''))
						  FOR XML PATH(''''), TYPE
			   ).value(''.'', ''NVARCHAR(MAX)''),
			   1,
			   1,
			   ''''),
	           [NhanSuSoYeuLyLichREF] = STUFF(
			   (
				   SELECT ''; '' + ns.HoVaTen
				   FROM   NhanSuSoYeuLyLichFull ns
				   WHERE ns.DeletedStatus <> 1 AND  ns.NhanSuSoYeuLyLichID IN (SELECT *
												FROM   dbo.Split(n.NhanSuSoYeuLyLichREF, '',''))
						  FOR XML PATH(''''), TYPE
			   ).value(''.'', ''NVARCHAR(MAX)''),
			   1,
			   1,
			   ''''),
	           [DmNhanHangThayDoiID],
	           [CreatedBy],
	           [CreatedAt],
	           [LastModidfiedBy],
	           CONVERT(VARCHAR(10), LastModifiedAt, 103) AS  LastModifiedAt,
	           [DeletedStatus],
	           [PrintStatus],
	           [RecordStatus],
	           CASE [RecordStatus]
	                WHEN 1 THEN ''check.png''
	                WHEN 0 THEN ''block.png''
	           END AS Review,
	           ROW_NUMBER() OVER(ORDER BY [LastModifiedAt] DESC) AS [RowNumber]
	    FROM   DmNhanHang n
	    WHERE  DeletedStatus <> 1 '+ @sTenNhanhang + ' ' + @Review +'
	) 
	SELECT *
	FROM   FileredList 
	WHERE  RowNumber BETWEEN '+ CAST(((@PageIndex -1) * @RecordCount + 1) AS NVARCHAR(50)) +' AND '+ CAST((@PageIndex * @RecordCount) AS NVARCHAR(50))+';';	
	
	--SELECT *
	--FROM   FileredList
	--WHERE  RowNumber BETWEEN (@PageIndex -1) * @RecordCount + 1 AND (@PageIndex * @RecordCount);
	
	--PRINT @SQL;
	
	EXEC sp_executesql @SQL;
	
END

```
