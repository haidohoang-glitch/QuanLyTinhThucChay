# Stored Procedure: `PhanQuyenNhanHang_Search`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-22 17:02:55.477000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.963000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@PageSize` | `int(4)` | No |
| `@DmNhanHangID` | `nvarchar(8000)` | No |
| `@OxUserID` | `nvarchar(8000)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[PhanQuyenNhanHang_Search]
	@PageIndex		INT,
	@PageSize		INT,
	@DmNhanHangID	NVARCHAR(4000),
	@OxUserID		NVARCHAR(4000)
AS
BEGIN	   
	DECLARE @Sql        NVARCHAR(4000) = '',				
			@Filter		NVARCHAR(4000) = '1=1',			
			@Params		NVARCHAR(4000),			
			@Lbound		INT, 
			@Ubound		INT,
			@MaxRecords	INT									
			
    SET @PageIndex = ABS(@PageIndex)
    SET @PageSize  = ABS(@PageSize)
    
    IF @PageIndex < 1 SET @PageIndex = 1
    IF @PageSize  < 1 SET @PageSize  = 10
    
    SET @Lbound = ((@PageIndex - 1) * @PageSize + 1)
    SET @Ubound = (@PageIndex * @PageSize)
    
    -- 1.1 Filter --	
    --====================================================================================================================================--							
    -- 1.1 DeleteStatus = 0 --	
    SET @Filter += ' AND A.DeletedStatus = 0'
    
    -- 1.2 DmNhanHangId --	
	IF (@DmNhanHangID IS NOT NULL AND @DmNhanHangID <> '')
		SET @Filter += ' AND B.DmNhanHangREF IN (' + @DmNhanHangID + ') '   
	
	-- 1.2 OxUserId --	
	IF (@OxUserID IS NOT NULL AND @OxUserID <> '')
		SET @Filter += ' AND B.OxUserREF IN (' + @OxUserID + ') '
		 
	-- 2 Execute Query --		
	--====================================================================================================================================--							
	SELECT @Sql = '
					SELECT * FROM
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
					) T						
					WHERE T.STT BETWEEN ' + CONVERT(VARCHAR(9), @Lbound) + ' AND ' + CONVERT(VARCHAR(9), @Ubound) 	
					
					
	SELECT @Params = '@PageIndex		INT,
					  @PageSize			INT,
					  @DmNhanHangID		INT,
					  @OxUserID			INT'					  							
					  
	PRINT (@Sql) 				
		
	EXEC sp_executesql @Sql, @Params, 
					   @PageIndex, @PageSize,
					   @DmNhanHangID, @OxUserID 						   					   
END

```
