# Stored Procedure: `ThucChay_v2_Get_List_Customer_Level_1_vNew`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-29 12:01:14.650000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.533000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@PageSize` | `int(4)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@AdvertisingType` | `nvarchar(8000)` | No |
| `@LstProduct` | `nvarchar(8000)` | No |
| `@LstBanner` | `nvarchar(8000)` | No |
| `@LstContract` | `nvarchar(8000)` | No |
| `@LstCustomer` | `nvarchar(8000)` | No |
| `@LstUnit` | `nvarchar(8000)` | No |
| `@MaxRecords` | `int(4)` | Yes |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<SonVM>
-- Create date: <13, 05, 2014>
-- Description:	<Danh sách Hợp đồng>

-- ThucChay_v2_Get_List_Customer_Level_1_vNew 1, 20, '2014-05-10', '2014-05-10', NULL, NULL, NULL, NULL, NULL, ''
-- ThucChay_v2_Get_List_Customer_Level_1_vNew 1, 20, '2014-05-10', '2014-05-10', NULL, NULL, NULL, NULL, NULL, N'''VIEW'''	
-- SELECT dbo.ThucChay_v2_Get_Filter_String('2014-05-10', '2014-05-10', NULL, NULL, NULL, NULL, NULL, NULL)
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_v2_Get_List_Customer_Level_1_vNew]
(	
	@PageIndex			INT,
	@PageSize			INT,
	@StartDate			DATETIME	   = NULL,
	@EndDate			DATETIME	   = NULL,
	@AdvertisingType	NVARCHAR(4000) = NULL,
	@LstProduct			NVARCHAR(4000) = NULL,
	@LstBanner			NVARCHAR(4000) = NULL,
	@LstContract		NVARCHAR(4000) = NULL,
	@LstCustomer		NVARCHAR(4000) = NULL,
	@LstUnit			NVARCHAR(4000) = NULL,
	@MaxRecords			INT OUT
)
AS
BEGIN
	DECLARE @Sql        NVARCHAR(4000) = '',				
			@Filter		NVARCHAR(4000) = '',			
			@Sign		NVARCHAR(9)    = '''',
			@Params		NVARCHAR(4000),
			@Lbound		INT,
			@Ubound		INT
      
    SET @PageIndex = ABS(@PageIndex)
    SET @PageSize  = ABS(@PageSize)
    
    IF @PageIndex < 1 SET @PageIndex = 1
    IF @PageSize  < 1 SET @PageSize  = 1
    
    SET @Lbound = ((@PageIndex - 1) * @PageSize + 1)
    SET @Ubound = (@PageIndex * @PageSize)
        
	-- 1. Filter --
	--====================================================================================================================================--
	SELECT @Filter = dbo.ThucChay_v2_Get_Filter_String(@StartDate, @EndDate, @AdvertisingType, @LstProduct, @LstBanner, @LstContract, @LstCustomer, @LstUnit)
	
	--PRINT @Filter
	
	-- 2. List & TotalRecords -- 		
	--====================================================================================================================================--						
	-- 2.1 TotalRecords --
	SELECT @Sql = '
					SELECT @MaxRecords = COUNT(*) FROM
					(
						SELECT T1.ID, T1.GroupFieldName
						FROM
						(
							SELECT B.DmKhachHangREF AS ID, B.TenKhachHang AS GroupFieldName,							
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
							GROUP BY B.DmKhachHangREF, B.TenKhachHang, A.TenMaHopDong	
						) T1
						GROUP BY T1.ID, T1.GroupFieldName
					) T2'
					
	--PRINT (@Sql) 				
					
    EXEC sp_executesql @Sql, @Params = N'@MaxRecords INT OUTPUT', @MaxRecords = @MaxRecords OUTPUT
    --SELECT @MaxRecords AS MaxRecords            
			
	-- 2.2 List  -- 		
	--====================================================================================================================================--						    
	SELECT @Sql = '
					SELECT 
						STT, ID, GroupFieldName, 						
						ThanhTienNoiBo		AS ThanhTienNoiBo,
						ThanhTienKhuyenMai  AS ThanhTienKhuyenMai,
						ThanhTienThucThu	AS ThanhTienThucThu,
						GiaTriThayDoi		AS GiaTriThayDoi
					FROM
					(
						SELECT	
							ROW_NUMBER() OVER (ORDER BY (T1.GroupFieldName) ASC) AS STT,
							T1.ID, T1.GroupFieldName,
							SUM(ThanhTienNoiBo)									 AS ThanhTienNoiBo,
							SUM(ThanhTienKhuyenMai)								 AS ThanhTienKhuyenMai,
							SUM(ThanhTienThucThu + GiaTriThayDoi)				 AS ThanhTienThucThu,
							SUM(GiaTriThayDoi)									 AS GiaTriThayDoi
						FROM
						(
							SELECT B.DmKhachHangREF AS ID, B.TenKhachHang AS GroupFieldName,							
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
							GROUP BY B.DmKhachHangREF, B.TenKhachHang, A.TenMaHopDong	
						) T1
						GROUP BY T1.ID, T1.GroupFieldName
					) T2
					WHERE T2.STT BETWEEN ' + CONVERT(VARCHAR(9), @Lbound) + ' AND ' + CONVERT(VARCHAR(9), @Ubound) 	
				
	SELECT @Params = '@PageIndex		INT,
					  @PageSize			INT,
					  @StartDate		DATETIME,
					  @EndDate			DATETIME,
					  @AdvertisingType	INT,
					  @LstProduct		NVARCHAR(4000),
					  @LstBanner		NVARCHAR(4000),
					  @LstContract		NVARCHAR(4000),
					  @LstCustomer		NVARCHAR(4000),
					  @LstUnit			NVARCHAR(4000)'
	
	PRINT (@Sql) 				
		
	EXEC sp_executesql @Sql, @Params, 
					   @PageIndex, @PageSize,
					   @StartDate, @EndDate, 	
					   @AdvertisingType,
					   @LstProduct, @LstBanner,
					   @LstContract, @LstCustomer, @LstUnit
					   
END

```
