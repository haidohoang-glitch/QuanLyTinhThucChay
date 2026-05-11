# Stored Procedure: `usp_PhanQuyenNhanHang_Search`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-14 16:27:47.523000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.383000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@PageSize` | `int(4)` | No |
| `@DmNhanHangID` | `nvarchar(8000)` | No |
| `@ThoiGianBatDau` | `nvarchar(40)` | No |
| `@ThoiGianKetThuc` | `nvarchar(40)` | No |
| `@OxUserID` | `nvarchar(8000)` | No |
| `@TinhTrangHieuLuc` | `varchar(10)` | No |
| `@TrangThaiHoatDong` | `varchar(10)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_PhanQuyenNhanHang_Search]
	@PageIndex INT,
	@PageSize INT,
	@DmNhanHangID NVARCHAR(4000),
	@ThoiGianBatDau NVARCHAR(20),
	@ThoiGianKetThuc NVARCHAR(20),
	@OxUserID NVARCHAR(4000),
	@TinhTrangHieuLuc VARCHAR(10),
	@TrangThaiHoatDong VARCHAR(10)
AS
BEGIN
	DECLARE @Sql     NVARCHAR(4000) = '',
	        @Filter  NVARCHAR(4000) = '1=1'
	
	SET @Filter += ' AND A.DeletedStatus = 0 AND B.IsLockPermission = 1 '
	
	IF (@DmNhanHangID IS NOT NULL AND @DmNhanHangID <> '')
	    SET @Filter += ' AND B.DmNhanHangREF IN (' + @DmNhanHangID + ') '   
	
	IF (@OxUserID IS NOT NULL AND @OxUserID <> '')
	    SET @Filter += ' AND B.OxUserREF IN (' + @OxUserID + ') '
	
	IF (@ThoiGianBatDau <> '' AND @ThoigianKetThuc <> '')
	    SET @Filter += ' AND B.ThoiGianHieuLuc BETWEEN ' + '''' + @ThoiGianBatDau 
	        + '''' + ' AND ' + '''' + @ThoigianKetThuc + '''';
	IF (@TinhTrangHieuLuc <> '')
		IF (@TinhTrangHieuLuc = 0)
			SET @Filter += ' AND B.ThoiGianHetHieuLuc IS NOT NULL ';
		    
		 IF (@TinhTrangHieuLuc = 1)
			SET @Filter += ' AND (B.ThoiGianHetHieuLuc IS NULL OR B.ThoiGianHetHieuLuc = '''')';
	
	
	IF (@TrangThaiHoatDong <> '')
	    SET @Filter += ' AND B.KichHoat = ' + @TrangThaiHoatDong;
	
	SELECT @Sql = 
	       '
				WITH FilteredList
					AS
					(
						SELECT [DmPhanQuyenID]
							   , A.DmNhanHangID AS DmNhanHangID
							   , A.TenNhanHang AS TenNhanHang
							   , C.OxUserREF
							   , C.Username
							   , B.LastModifiedBy AS LastModifiedBy
							   , dbo.FormatDate(B.LastModifiedAt) AS LastModifiedAt
							   ,[TenNhanSu]
							   ,[NhanSuREF]
							   ,[MaNhanSu]
							   ,[TenPhongBan]
							   ,[TenBoPhan]
							   ,[TenNhom]
							   ,dbo.FormatDate(B.ThoiGianHieuLuc) AS ThoiGianHieuLuc
							   ,dbo.FormatDate(B.ThoiGianHetHieuLuc) AS ThoiGianHetHieuLuc
							   ,CASE [KichHoat]
									WHEN 1 THEN ''checked''
									WHEN 0 THEN ''''
								END AS KichHoat
							   ,[TenNganhHang] = STUFF(
								   (
									   SELECT ''; '' + n.TenNghanhHang
									   FROM   DmNghanhHang n
									   WHERE n.DeletedStatus <> 1 AND n.DmNghanhHangID IN (SELECT *
																	FROM   dbo.Split(A.DmNghanhHangREF, '',''))
											  FOR XML PATH(''''), TYPE
								   ).value(''.'', ''NVARCHAR(MAX)'')
								   ,
							   1,
							   1,
							   '''')
							   ,ROW_NUMBER() OVER (ORDER BY (B.OxUserREF) DESC) AS STT
							   
						FROM DmNhanHang A
						INNER JOIN PhanQuyenNhanHang B
							ON A.DmNhanHangID = B.DmNhanHangREF
						INNER JOIN AdminUser C
							ON B.OxUserREF = C.OxUserREF
						WHERE ' + @Filter + '										
					)

	SELECT *,(SELECT COUNT(STT) FROM FilteredList) AS TotalRows
	FROM   FilteredList 
	WHERE  STT BETWEEN ' + CAST(((@PageIndex -1) * @PageSize + 1) AS NVARCHAR(50)) 
	       + ' AND ' + CAST((@PageIndex * @PageSize) AS NVARCHAR(50)) + ' ;'; 
	
	--PRINT @SQL;
	EXEC sp_executesql @SQL;
END

```
