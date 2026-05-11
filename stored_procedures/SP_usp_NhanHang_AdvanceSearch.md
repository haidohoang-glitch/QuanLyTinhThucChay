# Stored Procedure: `usp_NhanHang_AdvanceSearch`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-14 16:17:51.310000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.360000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@RecordStatus` | `varchar(10)` | No |
| `@TenNhanhang` | `nvarchar(2048)` | No |
| `@NhanHangCha` | `varchar(200)` | No |
| `@MucDoNhan` | `varchar(500)` | No |
| `@DmKhachhangSohuuREF` | `varchar(500)` | No |
| `@TinhTrangGiayPhep` | `varchar(200)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_NhanHang_AdvanceSearch]
	@PageIndex INT = 1,
	@RecordCount INT = 2,
	@RecordStatus VARCHAR(10),
	@TenNhanhang NVARCHAR(1024),
	@NhanHangCha VARCHAR(200),
	@MucDoNhan VARCHAR(500),
	@DmKhachhangSohuuREF VARCHAR(500),
	@TinhTrangGiayPhep VARCHAR(200)
AS
BEGIN
	SET NOCOUNT ON;
	DECLARE @SQL NVARCHAR(MAX);
	
	DECLARE @Review VARCHAR(20);
	DECLARE @sTenNhanhang NVARCHAR(256);
	SET @TenNhanhang = REPLACE(@TenNhanhang, '''', '''''')
	
	IF (@RecordStatus = '')
	    SET @Review = 'AND RecordStatus >=0'
	ELSE
	    SET @Review = 'AND RecordStatus =' + @RecordStatus;
	
	IF (@TenNhanhang <> '')
	    SET @sTenNhanhang = 'AND TenNhanHang COLLATE  SQL_Latin1_General_CP1_CI_AI LIKE N''%' + @TenNhanhang + '%''';
	ELSE
		SET @sTenNhanhang = ' ';
	
	IF (@NhanHangCha <> '')
	    SET @NhanHangCha = 'AND NhanHangCha IN (' + @NhanHangCha + ') '
	ELSE
	    SET @NhanHangCha = ' ';
	
	IF (@MucDoNhan <> '')
	    SET @MucDoNhan = ' AND MucDoNhan = ' + CAST(@MucDoNhan AS VARCHAR(10))
	ELSE
	    SET @MucDoNhan = ' ';
	
	IF (@DmKhachhangSohuuREF <> '')
	    SET @DmKhachhangSohuuREF = 'AND DmKhachhangSohuuREF IN (' + @DmKhachhangSohuuREF + ')';
	ELSE 
		SET @DmKhachhangSohuuREF = ' ';
	
	IF (@TinhTrangGiayPhep <> '')
	    SET @TinhTrangGiayPhep = ' AND TinhTrangGiayPhep = ' + @TinhTrangGiayPhep;
	ELSE
		SET @TinhTrangGiayPhep = ' ';
	
	SET @SQL = 
	    '
		
	WITH FileredList
	AS
	(
	    SELECT [DmNhanHangID],
	           [TenNhanHang],
			   [MucDoNhan],
	           [DmNghanhHangREF] = STUFF(
			   (
				   SELECT ''; '' + md.TenNghanhHang
				   FROM   DmNghanhHang md
				   WHERE md.DeletedStatus <> 1 AND md.DmNghanhHangID IN (SELECT *
												FROM   dbo.Split(n.DmNghanhHangREF, '',''))
						  FOR XML PATH(''''), TYPE
			   ).value(''.'', ''NVARCHAR(MAX)''),
			   1,
			   1,
			   ''''),
			    (
				   SELECT A.TenNhanHang
				   FROM   DmNhanHang AS A
				   WHERE  A.DmNhanHangID = n.NhanHangCha
			   ) AS TenNhanHangCha
			   ,
	           [NhanSuSoYeuLyLichREF] = STUFF(
			   (
				   SELECT ''; '' + ns.HoVaTen
				   FROM   NhanSuSoYeuLyLich ns
				   WHERE ns.DeletedStatus <> 1 AND  ns.NhanSuSoYeuLyLichID IN (SELECT *
												FROM   dbo.Split(n.NhanSuSoYeuLyLichREF, '',''))
						  FOR XML PATH(''''), TYPE
			   ).value(''.'', ''NVARCHAR(MAX)''),
			   1,
			   1,
			   ''''),
	           [DmNhanHangThayDoiID],
	           GhiChu,
	           DSKhachHangKy = ([dbo].[Fn_LayDanhSachKhachHangByDmNhanHangREF] (n.DmNhanHangID)),
				(
				   SELECT shn.TenKhachHang
				   FROM   KhachHangThongTinChung AS shn
				   WHERE  shn.KhachHangThongTinChungID = DmKhachhangSohuuREF
				) AS DSKhachHangSoHuu,
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
	    WHERE  DeletedStatus <> 1 ' + @sTenNhanhang + ' ' + @Review + ' ' + @MucDoNhan + ' ' + @NhanHangCha + ' ' + @DmKhachhangSohuuREF + ' ' + @TinhTrangGiayPhep  +  '
	)
	 
	SELECT *, (SELECT COUNT(RowNumber) FROM FileredList) AS TotalRows
	FROM   FileredList 
	WHERE  RowNumber BETWEEN ' + CAST(((@PageIndex -1) * @RecordCount + 1) AS NVARCHAR(50)) + ' AND ' + CAST((@PageIndex * @RecordCount) AS NVARCHAR(50)) + ';'; 
	
	--PRINT @SQL;
	EXEC sp_executesql @SQL;
END

```
