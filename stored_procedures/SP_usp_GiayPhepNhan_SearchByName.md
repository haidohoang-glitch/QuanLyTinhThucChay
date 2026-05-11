# Stored Procedure: `usp_GiayPhepNhan_SearchByName`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-22 09:41:49.323000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.313000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@DmNhanhangID` | `varchar(200)` | No |
| `@NhanHangCha` | `varchar(200)` | No |
| `@MucDoNhan` | `varchar(100)` | No |
| `@NganhHangID` | `varchar(200)` | No |
| `@ChuSoHuu` | `varchar(200)` | No |
| `@TenGiayPhep` | `nvarchar(1000)` | No |
| `@LoaiGiayPhepID` | `varchar(200)` | No |
| `@ThoiGianBatDau` | `varchar(20)` | No |
| `@ThoiGianKetThuc` | `varchar(20)` | No |
| `@TinhTrangPheDuyet` | `varchar(200)` | No |
| `@UserName` | `varchar(200)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_GiayPhepNhan_SearchByName]
	@PageIndex INT = 1,
	@RecordCount INT = 2,
	@DmNhanhangID VARCHAR(200),
	@NhanHangCha VARCHAR(200),
	@MucDoNhan VARCHAR(100),
	@NganhHangID VARCHAR(200),
	@ChuSoHuu VARCHAR(200),
	@TenGiayPhep NVARCHAR(500),
	@LoaiGiayPhepID VARCHAR(200),
	@ThoiGianBatDau VARCHAR(20),
	@ThoiGianKetThuc VARCHAR(20),
	@TinhTrangPheDuyet VARCHAR(200),
	@UserName VARCHAR(200)
AS
BEGIN
	SET NOCOUNT ON;
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
	
	IF (@LoaiGiayPhepID <> '')
	    SET @LoaiGiayPhepID = ' AND DmLoaiGiayPhepREF  IN (' + @LoaiGiayPhepID + ')';
	ELSE
	SET @LoaiGiayPhepID = ' ';
	
	IF (@MucDoNhan <> '')
	    SET @MucDoNhan = ' AND MucDoNhan = ' + @MucDoNhan;
	ELSE
	SET @MucDoNhan = ' ';
	
	IF (@NganhHangID <> '')
	    SET @NganhHangID = ' AND DmNghanhHangREF IN  (SELECT * FROM dbo.[Split]('''+@NganhHangID+''','','')) '
	ELSE
	SET @NganhHangID = ' ';			
	
	IF (@ChuSoHuu <> '')
	    SET @ChuSoHuu = ' AND DmKhachhangSohuuREF  IN (' + @ChuSoHuu + ')';
	ELSE
	SET @ChuSoHuu = ' ';
	
	IF (@TenGiayPhep <> '')
	    SET @TenGiayPhep =  ' AND gp.TenGiayPhep COLLATE  SQL_Latin1_General_CP1_CI_AI LIKE N''%' + @TenGiayPhep + '%''';
	ELSE
	SET @TenGiayPhep = ' ';
	
	IF (@ThoiGianBatDau <> '' AND @ThoigianKetThuc <> '')
	    SET @Thoigian = ' AND gp.ThoiGianHieuLuc BETWEEN ' + '''' + @ThoiGianBatDau + '''' + ' AND ' + '''' + @ThoigianKetThuc + '''';
	ELSE
	SET @Thoigian = ' ';
	
	IF (@TinhTrangPheDuyet <> '')
	    SET @TinhTrangPheDuyet = ' AND gp.RecordStatus = ' + @TinhTrangPheDuyet;
	ELSE
	SET @TinhTrangPheDuyet = ' ';
	
	IF (@UserName <> '')
	    SET @UserName = ' AND gp.CreatedBy = ''' + @UserName + '''';
	ELSE
	SET @UserName = ' ';
	
	
	SET @SQL = 
	    N'
		
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
			    ,[TenNhanHangCha] =(
									   SELECT A.TenNhanHang
									   FROM   DmNhanHang AS A
									   WHERE  A.DmNhanHangID = n.NhanHangCha
									) 
			   ,[DmNhanHangThayDoiID]
	           ,gp.[GhiChu]
	           ,[DSKhachHangSoHuu] =(
									   SELECT shn.TenKhachHang
									   FROM   KhachHangThongTinChung AS shn
									   WHERE  shn.KhachHangThongTinChungID = DmKhachhangSohuuREF
									)
	            ,gp.[TenGiayPhep] 
				,CONVERT(VARCHAR(10), gp.[ThoiGianHieuLuc], 103) AS ThoiGianHieuLuc 
				,gp.[DuongDanFile]
				,gp.[GiayPhepQuangCaoID]
				,gp.[TenFile]
				,[cssDownload] = (CASE 
								WHEN gp.[TenFile] IS NULL THEN ''''								
							ELSE
								''splashy-download''
							 END)
				,gp.[LastModifiedBy] 
			   	,ISNULL(CONVERT(VARCHAR(10), gp.LastModifiedAt, 103), CONVERT(VARCHAR(10), n.LastModifiedAt, 103)) AS  LastModifiedAt
				,n.LastModifiedAt AS LastModifiedAt1
				,[Review] = ISNULL((CASE gp.[RecordStatus]
								WHEN 3 THEN N''Từ Chối''
								WHEN 2 THEN N''Đã Duyệt''
								WHEN 1 THEN N''Chờ Duyệt''
								WHEN 0 THEN N''Nháp''
							END),N''Đã Duyệt'')
				,gp.[RecordStatus]			 
				,ROW_NUMBER() OVER(ORDER BY n.[LastModifiedAt] DESC) AS [RowNumber]
	    FROM   DmNhanHang n LEFT JOIN GiayPhepQuangCaoNhan gp ON n.DmNhanHangID = gp.DmNhanHangREF
	    WHERE n.RecordStatus = 1 AND n.DeletedStatus <> 1 AND n.TinhTrangGiayPhep IS NOT NULL ' 
	    + @strNhanhangID + ' ' + @NhanHangCha + ' ' + @MucDoNhan + ' ' + @ChuSoHuu 
	    + ' ' + @TenGiayPhep + ' ' + @Thoigian + ' ' + @NganhHangID + ' ' + @TinhTrangPheDuyet + ' ' + @UserName 
		+ ' ' + @LoaiGiayPhepID +
	    '
	) 
	SELECT *,(SELECT COUNT(RowNumber) FROM FileredList) AS TotalRows
	FROM   FileredList 
	WHERE  RowNumber BETWEEN ' + CAST(((@PageIndex -1) * @RecordCount + 1) AS NVARCHAR(50)) 
	    + ' AND ' + CAST((@PageIndex * @RecordCount) AS NVARCHAR(50)) + '  ;'; 
	
	PRINT @SQL;
	
	EXEC sp_executesql @SQL;
END

```
