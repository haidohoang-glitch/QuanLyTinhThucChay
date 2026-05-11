# Stored Procedure: `usp_report_LoaiGiayPhepQuangCao`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-08-22 09:41:50.553000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.397000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangID` | `varchar(200)` | No |
| `@NhanhangCha` | `varchar(200)` | No |
| `@MucDoNhan` | `varchar(100)` | No |
| `@DmKhachHangSoHuuREF` | `varchar(100)` | No |
| `@TenGiayPhep` | `nvarchar(400)` | No |
| `@LoaiGiayPhepID` | `varchar(200)` | No |
| `@ThoiGianBatDau` | `varchar(20)` | No |
| `@ThoigianKetThuc` | `varchar(20)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_report_LoaiGiayPhepQuangCao]
	@DmNhanHangID VARCHAR(200),
	@NhanhangCha VARCHAR(200),
	@MucDoNhan VARCHAR(100),
	@DmKhachHangSoHuuREF VARCHAR(100),
	@TenGiayPhep NVARCHAR(200),
	@LoaiGiayPhepID VARCHAR(200),
	@ThoiGianBatDau VARCHAR(20),
	@ThoigianKetThuc VARCHAR(20)
AS
BEGIN
	DECLARE @SQL NVARCHAR(MAX);
	
	SET @SQL = 
	    '
		SELECT nhan.TenNhanHang,
		   nhan.DmNhanHangID,
		   TenNhanCha = (
			   SELECT A.TenNhanHang
			   FROM   DmNhanhang AS A
			   WHERE  A.DmNhanHangID = nhan.NhanHangCha
		   ),
		   ChuSoHuu = (
			   SELECT B.TenKhachHang
			   FROM   KhachHangThongTinChung AS B
			   WHERE  B.KhachHangThongTinChungID = nhan.DmKhachhangSohuuREF
		   ),
		   nhan.MucDoNhan,
		   gp.TenGiayPhep,
		   gp.TenFile,
		   CONVERT(VARCHAR(10), gp.ThoiGianHieuLuc, 103) AS  ThoiGianHieuLuc,
		   CASE gp.RecordStatus
					WHEN 1 THEN ''block.png''
	                WHEN 2 THEN ''check.png''
	                WHEN 1 THEN ''block.png''
	                WHEN 0 THEN ''block.png''
	           END AS Review,
	         CASE gp.RecordStatus
					WHEN 3 THEN ''''
	                WHEN 2 THEN ''x''
	                WHEN 1 THEN ''''
	                WHEN 0 THEN ''''
	           END AS PheDuyet   
	        
		FROM GiayPhepQuangCaoNhan gp
		   LEFT JOIN DmNhanHang AS nhan
				ON  nhan.DmNhanHangID = gp.DmNhanHangREF
		WHERE 1 = 1 '
	SET @SQL = @SQL + ' AND nhan.RecordStatus = 1 AND nhan.DeletedStatus <> 1 AND gp.RecordStatus = 2'
	
	IF (LEN(@DmNhanHangID) > 0)
	    SET @SQL = @SQL + ' AND nhan.DmNhanHangID IN (' + @DmNhanHangID + ')'
	
	IF (@NhanhangCha <> '')
	    SET @SQL = @SQL + ' AND nhan.NhanHangCha IN (' + @NhanhangCha + ')'   
	
	IF (@MucDoNhan <> '')
	    SET @SQL = @SQL + ' AND nhan.MucDoNhan = ' + CAST(@MucDoNhan AS VARCHAR(10))
	
	IF (@DmKhachHangSoHuuREF <> '')
	    SET @SQL = @SQL + ' AND nhan.DmKhachhangSohuuREF = ' + CAST(@DmKhachHangSoHuuREF AS VARCHAR(10))
	
	IF (@TenGiayPhep <> '' OR @TenGiayPhep IS NOT NULL)
	    SET @SQL = @SQL + 
	        ' AND gp.TenGiayPhep COLLATE  SQL_Latin1_General_CP1_CI_AI LIKE N''%'
	        + @TenGiayPhep + '%''';
			
	IF (@LoaiGiayPhepID <> '' )	
		SET @SQL = @SQL + ' AND DmLoaiGiayPhepREF  IN (' + CAST(@LoaiGiayPhepID AS VARCHAR(100))+ ')';
		
	IF (@ThoiGianBatDau <> '' AND @ThoigianKetThuc <> '')
	    SET @SQL = @SQL + ' AND gp.ThoiGianHieuLuc BETWEEN ' + ''''+@ThoiGianBatDau +''''  + ' AND ' + ''''+@ThoigianKetThuc+''''
	    
	    
SET @SQL = @SQL + ' ORDER BY  nhan.DmNhanHangID DESC'
	--PRINT @SQL;
	EXEC sp_executesql @SQL;
END

```
