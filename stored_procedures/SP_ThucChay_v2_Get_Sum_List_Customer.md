# Stored Procedure: `ThucChay_v2_Get_Sum_List_Customer`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-05-14 15:21:43.823000
- **Ngày sửa cuối**: 2014-11-19 12:16:47.693000

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

-- ThucChay_v2_Get_Sum_List_Customer '2014-05-10', '2014-05-10', NULL, NULL, NULL, NULL, NULL, NULL
-- ThucChay_v2_Get_Sum_List_Customer '2014-05-10', '2014-05-10', NULL, NULL, NULL, NULL, NULL, N'''VIEW'''
-- SELECT dbo.ThucChay_v2_Get_Filter_String('2014-05-10', '2014-05-10', NULL, NULL, NULL, NULL, NULL, NULL)
-- SELECT dbo.ThucChay_v2_Get_Filter_String('2014-05-10', '2014-05-10', NULL, NULL, NULL, NULL, NULL, N'''VIEW''')
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_v2_Get_Sum_List_Customer]
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
			@Params		NVARCHAR(4000)								
              
	-- 1. Filter --
	--====================================================================================================================================--
	SELECT @Filter = dbo.ThucChay_v2_Get_Filter_String(@StartDate, @EndDate, @AdvertisingType, @LstProduct, @LstBanner, @LstContract, @LstCustomer, @LstUnit)
	
	--PRINT @Filter
	
	-- 2. List Sum -- 		
	--====================================================================================================================================--
	--
	DECLARE @TempTable AS TABLE (
			ThanhTienNoiBo	FLOAT,
			ThanhTienKhuyenMai FLOAT,
			ThanhTienThucThu	FLOAT,
			ThanhTienThucThuNB	FLOAT,
			ThanhTienThucThuTC	FLOAT
	)
									        
	SELECT @Sql = '					
		SELECT							
			SUM(ThanhTienNoiBo) 		AS ThanhTienNoiBo,
			SUM(ThanhTienKhuyenMai)  	AS ThanhTienKhuyenMai,
			SUM(ThanhTienThucThu)		AS ThanhTienThucThu,
			SUM(ThanhTienNoiBo + GiaTriThayDoiNB)	AS ThanhTienThucThuNB,
			SUM(ThanhTienThucThu + GiaTriThayDoiTC)	AS ThanhTienThucThuTC
		FROM
		(
			SELECT 							
					CASE WHEN (UPPER(A.TenMaHopDong) LIKE ' + @Sign + 'NB%' + @Sign + ' OR UPPER(A.TenMaHopDong) LIKE ' + @Sign + '%SH%' + @Sign + ' OR UPPER(A.TenMaHopDong) LIKE ' + @Sign + '%SOHA%' + @Sign + ') THEN 
							ISNULL(SUM(A.ThanhTienSauTrietKhauThucChay), 0) 
						ELSE 0
					END AS ThanhTienNoiBo,
					ISNULL(SUM(A.ThanhTienKM),0) AS ThanhTienKhuyenMai,			
					CASE WHEN (UPPER(A.TenMaHopDong) NOT LIKE ' + @Sign + 'NB%' + @Sign + ' AND UPPER(A.TenMaHopDong) NOT LIKE ' + @Sign + '%SH%' + @Sign + ' AND UPPER(A.TenMaHopDong) NOT LIKE ' + @Sign + '%SOHA%' + @Sign + ')  THEN 
							ISNULL(SUM(A.ThanhTienSauTrietKhauThucChay),0) 
						ELSE 0
					END AS ThanhTienThucThu,
					CASE WHEN (UPPER(A.TenMaHopDong) LIKE ' + @Sign + 'NB%' + @Sign + ' OR UPPER(A.TenMaHopDong) LIKE ' + @Sign + '%SH%' + @Sign + ' OR UPPER(A.TenMaHopDong) LIKE ' + @Sign + '%SOHA%' + @Sign + ') THEN 
							ISNULL(SUM(A.GiaTriThayDoi), 0) 
						ELSE 0
					END AS GiaTriThayDoiNB,
					CASE WHEN (UPPER(A.TenMaHopDong) NOT LIKE ' + @Sign + 'NB%' + @Sign + ' AND UPPER(A.TenMaHopDong) NOT LIKE ' + @Sign + '%SH%' + @Sign + ' AND UPPER(A.TenMaHopDong) NOT LIKE ' + @Sign + '%SOHA%' + @Sign + ')  THEN 
							ISNULL(SUM(A.GiaTriThayDoi),0) 
						ELSE 0
					END AS GiaTriThayDoiTC
			FROM ThucChayDaTinh A INNER JOIN HopDong B
			ON A.HopDongID = B.HopDongID
			WHERE ' + @Filter + ' 							
			GROUP BY A.TenMaHopDong	
		) T1'
									
	SELECT @Params = '@StartDate		DATETIME,
					  @EndDate			DATETIME,
					  @AdvertisingType	INT,
					  @LstProduct		NVARCHAR(4000),
					  @LstBanner		NVARCHAR(4000),
					  @LstContract		NVARCHAR(4000),
					  @LstCustomer		NVARCHAR(4000),
					  @LstUnit			NVARCHAR(4000)'
	
	PRINT (@Sql) 				
	
	INSERT INTO @TempTable	
	EXEC sp_executesql @Sql, @Params, 					   
					   @StartDate, @EndDate, 	
					   @AdvertisingType,
					   @LstProduct, @LstBanner,
					   @LstContract, @LstCustomer, @LstUnit;
					   
	SELECT @SqlAdmarket = '					
		SELECT							
			SUM(ThanhTienNoiBo) 		AS ThanhTienNoiBo,
			SUM(ThanhTienKhuyenMai)  	AS ThanhTienKhuyenMai,
			SUM(ThanhTienThucThu)		AS ThanhTienThucThu,
			SUM(ThanhTienNoiBo + GiaTriThayDoiNB)	AS ThanhTienThucThuNB,
			SUM(ThanhTienThucThu + GiaTriThayDoiTC)	AS ThanhTienThucThuTC
		FROM
		(
			SELECT 							
					CASE WHEN (UPPER(A.TenMaHopDong) LIKE ' + @Sign + 'NB%' + @Sign + ' OR UPPER(A.TenMaHopDong) LIKE ' + @Sign + '%SH%' + @Sign + ' OR UPPER(A.TenMaHopDong) LIKE ' + @Sign + '%SOHA%' + @Sign + ') THEN 
							ISNULL(SUM(A.ThanhTienSauTrietKhauThucChay), 0) 
						ELSE 0
					END AS ThanhTienNoiBo,
					ISNULL(SUM(A.ThanhTienKM),0) AS ThanhTienKhuyenMai,			
					CASE WHEN (UPPER(A.TenMaHopDong) NOT LIKE ' + @Sign + 'NB%' + @Sign + ' AND UPPER(A.TenMaHopDong) NOT LIKE ' + @Sign + '%SH%' + @Sign + ' AND UPPER(A.TenMaHopDong) NOT LIKE ' + @Sign + '%SOHA%' + @Sign + ')  THEN 
							ISNULL(SUM(A.ThanhTienSauTrietKhauThucChay),0) 
						ELSE 0
					END AS ThanhTienThucThu,
					CASE WHEN (UPPER(A.TenMaHopDong) LIKE ' + @Sign + 'NB%' + @Sign + ' OR UPPER(A.TenMaHopDong) LIKE ' + @Sign + '%SH%' + @Sign + ' OR UPPER(A.TenMaHopDong) LIKE ' + @Sign + '%SOHA%' + @Sign + ') THEN 
							ISNULL(SUM(A.GiaTriThayDoi), 0) 
						ELSE 0
					END AS GiaTriThayDoiNB,
					CASE WHEN (UPPER(A.TenMaHopDong) NOT LIKE ' + @Sign + 'NB%' + @Sign + ' AND UPPER(A.TenMaHopDong) NOT LIKE ' + @Sign + '%SH%' + @Sign + ' AND UPPER(A.TenMaHopDong) NOT LIKE ' + @Sign + '%SOHA%' + @Sign + ')  THEN 
							ISNULL(SUM(A.GiaTriThayDoi),0) 
						ELSE 0
					END AS GiaTriThayDoiTC
			FROM ThucChayDaTinhAdmarket A INNER JOIN HopDong B
			ON A.HopDongID = B.HopDongID
			WHERE ' + @Filter + ' 							
			GROUP BY A.TenMaHopDong	
		) T1'					   
					   
	PRINT (@SqlAdmarket) 				
	
	INSERT INTO @TempTable	
	EXEC sp_executesql @SqlAdmarket, @Params, 					   
					   @StartDate, @EndDate, 	
					   @AdvertisingType,
					   @LstProduct, @LstBanner,
					   @LstContract, @LstCustomer, @LstUnit;
					   						
	SELECT 
		SUM(ThanhTienNoiBo) AS ThanhTienNoiBo,
		SUM(ThanhTienKhuyenMai) AS ThanhTienKhuyenMai,
		SUM(ThanhTienThucThu) AS ThanhTienThucThu,
		SUM(ThanhTienThucThuNB) AS ThanhTienThucThuNB,
		SUM(ThanhTienThucThuTC) AS ThanhTienThucThuTC
	FROM @TempTable
					   
END

```
