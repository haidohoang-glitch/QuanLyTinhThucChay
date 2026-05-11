# Stored Procedure: `ThucChay_v2_Get_List_Customer_Level_2_TotalRow`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-19 09:09:34.513000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.720000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@AdvertisingType` | `nvarchar(8000)` | No |
| `@LstProduct` | `nvarchar(8000)` | No |
| `@LstBanner` | `nvarchar(8000)` | No |
| `@LstContract` | `nvarchar(8000)` | No |
| `@LstCustomer` | `nvarchar(8000)` | No |
| `@LstUnit` | `nvarchar(8000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<SonVM>
-- Create date: <13, 05, 2014>
-- Description:	<Danh sách Hợp đồng>

-- ThucChay_v2_Get_List_Customer_Level_2_TotalRow '2014-05-10', '2014-05-10', NULL, NULL, NULL, NULL, 6671
-- ThucChay_v2_Get_List_Customer_Level_2_TotalRow '2014-05-10', '2014-05-10', NULL, NULL, NULL, NULL, 6671, N'''VIEW'''		
-- SELECT dbo.ThucChay_v2_Get_Filter_String('2014-05-10', '2014-05-10', NULL, NULL, NULL, NULL, NULL, NULL)
-- SELECT dbo.ThucChay_v2_Get_Filter_String('2014-05-10', '2014-05-10', NULL, NULL, NULL, NULL, NULL, N'''VIEW''')
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_v2_Get_List_Customer_Level_2_TotalRow]
(	
	@StartDate			DATETIME	   = NULL,
	@EndDate			DATETIME	   = NULL,
	@AdvertisingType	NVARCHAR(4000) = NULL,
	@LstProduct			NVARCHAR(4000) = NULL,
	@LstBanner			NVARCHAR(4000) = NULL,
	@LstContract		NVARCHAR(4000) = NULL,
	@LstCustomer		NVARCHAR(4000) = NULL,
	@LstUnit			NVARCHAR(4000) = NULL
)
AS
BEGIN
	DECLARE @Sql        NVARCHAR(4000) = '',	
			@SqlAdmarket        NVARCHAR(4000) = '',			
			@Filter		NVARCHAR(4000) = '',			
			@Sign		NVARCHAR(9)    = '''',
			@Params		NVARCHAR(4000),
			@MaxRecords	INT					
      
	-- 1. Filter --
	--====================================================================================================================================--
	SELECT @Filter = dbo.ThucChay_v2_Get_Filter_String(@StartDate, @EndDate, @AdvertisingType, @LstProduct, @LstBanner, @LstContract, @LstCustomer, @LstUnit)
	
	--PRINT @Filter
	
	-- 2. TotalRecords -- 		
	--====================================================================================================================================--						
	-- 2.1 TotalRecords --
	
	DECLARE @TempTable AS TABLE (
		ID				INT,
		GroupFieldName	NVARCHAR(2000)	
	);
	
	SELECT @Params = '
					  @StartDate		DATETIME,
					  @EndDate			DATETIME,
					  @AdvertisingType	INT,
					  @LstProduct		NVARCHAR(4000),
					  @LstBanner		NVARCHAR(4000),
					  @LstContract		NVARCHAR(4000),
					  @LstCustomer		NVARCHAR(4000),
					  @LstUnit			NVARCHAR(4000)'
	
	SELECT @Sql = '				
					SELECT T1.ID, T1.GroupFieldName
					FROM
					(
						SELECT B.HopDongID AS ID, B.SoHopDong AS GroupFieldName,								
								CASE WHEN (UPPER(A.TenMaHopDong) LIKE ' + @Sign + 'NB%' + @Sign + ' OR UPPER(A.TenMaHopDong) LIKE ' + @Sign + '%SH%' + @Sign + ' OR UPPER(A.TenMaHopDong) LIKE ' + @Sign + '%SOHA%' + @Sign + ') THEN 
								ISNULL(SUM(A.ThanhTienSauTrietKhauThucChay), 0) 
								ELSE 0
								END AS ThanhTienNoiBo,
								ISNULL(SUM(A.ThanhTienKM),0) AS ThanhTienKhuyenMai,			
								CASE WHEN (UPPER(A.TenMaHopDong) NOT LIKE ' + @Sign + 'NB%' + @Sign + ' AND UPPER(A.TenMaHopDong) NOT LIKE ' + @Sign + '%SH%' + @Sign + ' AND UPPER(A.TenMaHopDong) NOT LIKE ' + @Sign + '%SOHA%' + @Sign + ')  THEN 
										ISNULL(SUM(A.ThanhTienSauTrietKhauThucChay),0) 
									ELSE 0
								END AS ThanhTienThucThu,
								SUM(A.GiaTriThayDoi) AS GiaTriThayDoi  
						FROM ThucChayDaTinh A INNER JOIN HopDong B
						ON A.HopDongID = B.HopDongID
						WHERE ' + @Filter + ' 							
						GROUP BY B.HopDongID, B.SoHopDong, A.TenMaHopDong
					) T1
					GROUP BY T1.ID, T1.GroupFieldName'
					
	--PRINT (@Sql) 	
	INSERT INTO @TempTable	
	EXEC sp_executesql @Sql, @Params, 					   
					   @StartDate, @EndDate, 	
					   @AdvertisingType,
					   @LstProduct, @LstBanner,
					   @LstContract, @LstCustomer, @LstUnit;		
					   
	SELECT @SqlAdmarket = '				
					SELECT T1.ID, T1.GroupFieldName
					FROM
					(
						SELECT B.HopDongID AS ID, B.SoHopDong AS GroupFieldName,								
								CASE WHEN (UPPER(A.TenMaHopDong) LIKE ' + @Sign + 'NB%' + @Sign + ' OR UPPER(A.TenMaHopDong) LIKE ' + @Sign + '%SH%' + @Sign + ' OR UPPER(A.TenMaHopDong) LIKE ' + @Sign + '%SOHA%' + @Sign + ') THEN 
								ISNULL(SUM(A.ThanhTienSauTrietKhauThucChay), 0) 
								ELSE 0
								END AS ThanhTienNoiBo,
								ISNULL(SUM(A.ThanhTienKM),0) AS ThanhTienKhuyenMai,			
								CASE WHEN (UPPER(A.TenMaHopDong) NOT LIKE ' + @Sign + 'NB%' + @Sign + ' AND UPPER(A.TenMaHopDong) NOT LIKE ' + @Sign + '%SH%' + @Sign + ' AND UPPER(A.TenMaHopDong) NOT LIKE ' + @Sign + '%SOHA%' + @Sign + ')  THEN 
										ISNULL(SUM(A.ThanhTienSauTrietKhauThucChay),0) 
									ELSE 0
								END AS ThanhTienThucThu,
								SUM(A.GiaTriThayDoi) AS GiaTriThayDoi  
						FROM ThucChayDaTinhAdmarket A INNER JOIN HopDong B
						ON A.HopDongID = B.HopDongID
						WHERE ' + @Filter + ' 							
						GROUP BY B.HopDongID, B.SoHopDong, A.TenMaHopDong
					) T1
					GROUP BY T1.ID, T1.GroupFieldName'
					
	--PRINT (@Sql) 	
	INSERT INTO @TempTable	
	EXEC sp_executesql @SqlAdmarket, @Params, 					   
					   @StartDate, @EndDate, 	
					   @AdvertisingType,
					   @LstProduct, @LstBanner,
					   @LstContract, @LstCustomer, @LstUnit;						   	
					
    SELECT COUNT(T.ID) 	AS MaxRecords
	FROM
	(			   
		SELECT DISTINCT ID, GroupFieldName
		FROM @TempTable 
	)T	    
END

```
