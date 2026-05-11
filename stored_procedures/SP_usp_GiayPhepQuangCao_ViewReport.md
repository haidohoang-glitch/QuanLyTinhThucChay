# Stored Procedure: `usp_GiayPhepQuangCao_ViewReport`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-14 16:26:41.527000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.347000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@DmNhanHangID` | `varchar(500)` | No |
| `@NhanhangCha` | `varchar(500)` | No |
| `@MucDoNhan` | `varchar(200)` | No |
| `@DmKhachHangSoHuuREF` | `nvarchar(1000)` | No |
| `@TenGiayPhep` | `nvarchar(400)` | No |
| `@LoaiGiayPhepID` | `varchar(200)` | No |
| `@ThoiGianBatDau` | `varchar(20)` | No |
| `@ThoigianKetThuc` | `varchar(20)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_GiayPhepQuangCao_ViewReport]
	@PageIndex INT = 1,
	@RecordCount INT = 2,
	@DmNhanHangID VARCHAR(500),
	@NhanhangCha VARCHAR(500),
	@MucDoNhan VARCHAR(200),
	@DmKhachHangSoHuuREF NVARCHAR(500),
	@TenGiayPhep NVARCHAR(200),
	@LoaiGiayPhepID VARCHAR(200),
	@ThoiGianBatDau VARCHAR(20),
	@ThoigianKetThuc VARCHAR(20)
AS
BEGIN
	DECLARE @SQL            NVARCHAR(MAX);
	DECLARE @strNhanhangID  VARCHAR(200);
	DECLARE @Thoigian       VARCHAR(200);
	
	IF (@DmNhanhangID <> '')
	    SET @strNhanhangID = ' AND DmNhanHangID  IN (' + @DmNhanhangID + ')';
	ELSE
	SET @strNhanhangID = ' ';
	
	IF (@NhanHangCha <> '')
	    SET @NhanHangCha = ' AND NhanHangCha  IN (' + @NhanHangCha + ')';
	ELSE
	SET @NhanHangCha = ' ';
	
	IF (@MucDoNhan <> '')
	    SET @MucDoNhan = ' AND MucDoNhan = ' + @MucDoNhan;
	ELSE
	SET @MucDoNhan = ' ';
	
	IF (@DmKhachHangSoHuuREF <> '')
	    SET @DmKhachHangSoHuuREF = ' AND DmKhachhangSohuuREF  IN (' + @DmKhachHangSoHuuREF 
	        + ')';
	ELSE
	SET @DmKhachHangSoHuuREF = ' ';
	
	IF (@TenGiayPhep <> '')
	    SET @TenGiayPhep = 
	        ' AND gp.TenGiayPhep COLLATE  SQL_Latin1_General_CP1_CI_AI LIKE N''%' 
	        + @TenGiayPhep + '%''';
	ELSE
	SET @TenGiayPhep = ' ';
		
	IF (@LoaiGiayPhepID <> '')
	    SET @LoaiGiayPhepID = ' AND DmLoaiGiayPhepREF  IN (' + @LoaiGiayPhepID + ')';
	ELSE
	SET @LoaiGiayPhepID = ' ';
	
	
	IF (@ThoiGianBatDau <> '' AND @ThoigianKetThuc <> '')
	    SET @Thoigian = ' AND gp.ThoiGianHieuLuc BETWEEN ' + '''' + @ThoiGianBatDau 
	        + '''' + ' AND ' + '''' + @ThoigianKetThuc + '''';
	ELSE
	SET @Thoigian = ' ';    			
	
	SET @SQL = 
	    '
		
	WITH FileredList
	AS
	(
	    SELECT [DmNhanHangID]
	           ,[TenNhanHang]
			   ,[MucDoNhan]
	           ,[DmNghanhHangREF] = STUFF(
				   (
					   SELECT ''; '' + md.TenNghanhHang
					   FROM   DmNghanhHang md
					   WHERE md.DeletedStatus <> 1 AND md.DmNghanhHangID IN (SELECT *
													FROM   dbo.Split(n.DmNghanhHangREF, '',''))
							  FOR XML PATH(''''), TYPE
				   ).value(''.'', ''NVARCHAR(MAX)''), 1, 1,''''
				)
			    ,[TenNhanCha] =(
									   SELECT A.TenNhanHang
									   FROM   DmNhanHang AS A
									   WHERE  A.DmNhanHangID = n.NhanHangCha
									) 
			   ,[DmNhanHangThayDoiID]
	           ,gp.[GhiChu]
	           ,[ChuSoHuu] =(
									   SELECT shn.TenKhachHang
									   FROM   KhachHangThongTinChung AS shn
									   WHERE  shn.KhachHangThongTinChungID = DmKhachhangSohuuREF
									)
	            ,gp.[TenGiayPhep] 
				,CONVERT(VARCHAR(10), gp.[ThoiGianHieuLuc], 103) AS ThoiGianHieuLuc 
				,gp.[DuongDanFile]
				,gp.[TenFile]
				,[cssDownload] = (CASE 
								WHEN gp.[TenFile] IS NULL THEN ''''								
							ELSE
								''splashy-download''
							 END)
				,gp.[LastModifiedBy]
			   	,CONVERT(VARCHAR(10), gp.LastModifiedAt, 103) AS  LastModifiedAt
				,[Review] = (CASE gp.[RecordStatus]
								WHEN 3 THEN ''block.png''
								WHEN 2 THEN ''check.png''
								WHEN 1 THEN ''block.png''
								WHEN 0 THEN ''block.png''
							ELSE
								''1x1.png''
							 END)
				,ROW_NUMBER() OVER(ORDER BY [DmNhanHangID] DESC) AS [RowNumber]
	    FROM GiayPhepQuangCaoNhan gp  LEFT JOIN DmNhanHang n  ON n.DmNhanHangID = gp.DmNhanHangREF
	    WHERE n.RecordStatus = 1 AND n.DeletedStatus <> 1 AND gp.RecordStatus = 2 ' 
	    + @strNhanhangID + ' ' + @NhanHangCha + ' ' + @MucDoNhan + ' ' + @DmKhachHangSoHuuREF 
	    + ' ' + @TenGiayPhep + ' ' + @Thoigian + ' ' + @LoaiGiayPhepID +
	    '
	) 
	SELECT *,(SELECT COUNT(RowNumber) FROM FileredList) AS TotalRows
	FROM   FileredList 
	WHERE  RowNumber BETWEEN ' + CAST(((@PageIndex -1) * @RecordCount + 1) AS NVARCHAR(50)) 
	    + ' AND ' + CAST((@PageIndex * @RecordCount) AS NVARCHAR(50)) + 
	    ' ORDER BY  DmNhanHangID DESC ;'; 
	
	--PRINT @SQL;
	EXEC sp_executesql @SQL;
END

```
