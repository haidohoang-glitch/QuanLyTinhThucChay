# Stored Procedure: `Rpt_DanhSachWebsiteSanPham_TotalValue`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 14:54:02.380000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.297000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@LstWebsite` | `nvarchar(8000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<SonVM>
-- Create date: <2014, 06, 10>
-- Description:	<Description,,>
-- Rpt_DanhSachWebsiteSanPham_TotalValue '2014-01-01', '2014-01-05', '' 
-- =============================================
CREATE PROCEDURE [dbo].[Rpt_DanhSachWebsiteSanPham_TotalValue] 
	@StartDate	DATETIME,
	@EndDate	DATETIME,
	@LstWebsite NVARCHAR(4000)
AS
BEGIN			
	DECLARE @SQL		NVARCHAR(MAX),
			@Params		NVARCHAR(4000),
			@Filter		NVARCHAR(4000)  = '1=1',
			@Sign		NVARCHAR(10)	= ''''				
	
	Set @Filter += ' AND CONVERT(DATE, A.NgayThucHien) Between ' + 
						@Sign + CONVERT(NVARCHAR(30), @StartDate) + @Sign + ' AND ' + 
						@Sign + CONVERT(NVARCHAR(30), @EndDate)+ @Sign
													
	IF (@LstWebsite IS NOT NULL AND @LstWebsite <> '')
		SET @Filter += 'AND DmWebsiteREF IN (' + @LstWebsite + ')' 
		
	SELECT @SQL = '	
					SELECT 
						dbo.FormatNumber(SUM(T.Adpage)) Adpage,
						dbo.FormatNumber(SUM(T.SponsoredPost)) SponsoredPost,
						dbo.FormatNumber(SUM(T.DangTin)) DangTin,
						dbo.FormatNumber(SUM(T.BalloonAds)) BalloonAds,
						dbo.FormatNumber(SUM(T.TVCOnline)) TVCOnline,
						dbo.FormatNumber(SUM(T.CPMMass)) CPMMass,
						dbo.FormatNumber(SUM(T.Mobile)) Mobile,
						dbo.FormatNumber(SUM(T.BannerCPD)) BannerCPD,
						dbo.FormatNumber(SUM(T.BannerCPDChuyentrang)) BannerCPDChuyentrang,
						dbo.FormatNumber(SUM(T.BoxappCPD)) BoxappCPD,
						dbo.FormatNumber(SUM(T.BoxappCPM)) BoxappCPM,
						dbo.FormatNumber(SUM(T.BoxappSelfServing)) BoxappSelfServing,
						dbo.FormatNumber(SUM(T.BoxappMultiBrand)) BoxappMultiBrand,
						dbo.FormatNumber(SUM(T.CPCAdmarket)) CPCAdmarket,
						dbo.FormatNumber(SUM(T.CPCPlus)) CPCPlus,
						dbo.FormatNumber(SUM(T.CPA)) CPA,
						dbo.FormatNumber(SUM(T.CPMAdmarket)) CPMAdmarket,
						dbo.FormatNumber(SUM(T.GoogleAds)) GoogleAds,
						dbo.FormatNumber(SUM(T.SPKhac)) SPKhac	
					FROM 					
					(
						SELECT 								
								SUM(A.Adpage) Adpage,
								SUM(A.SponsoredPost) SponsoredPost,
								SUM(A.DangTin) DangTin,
								SUM(A.BalloonAds) BalloonAds,
								SUM(A.TVCOnline) TVCOnline,
								SUM(A.CPMMass) CPMMass,
								SUM(A.Mobile) Mobile,
								SUM(A.BannerCPD) BannerCPD,
								SUM(A.BannerCPDChuyentrang) BannerCPDChuyentrang,
								SUM(A.BoxappCPD) BoxappCPD,
								SUM(A.BoxappCPM) BoxappCPM,
								SUM(A.BoxappSelfServing) BoxappSelfServing,
								SUM(A.BoxappMultiBrand) BoxappMultiBrand,
								SUM(A.CPCAdmarket) CPCAdmarket,
								SUM(A.CPCPlus) CPCPlus,
								SUM(A.CPA) CPA,
								SUM(A.CPMAdmarket) CPMAdmarket,
								SUM(A.GoogleAds) GoogleAds,
								SUM(A.SPKhac) SPKhac						
						FROM rptWebsiteProduct A
						WHERE ' + @Filter + '
						GROUP BY A.TenWebsite, A.DmWebsiteREF
					) T'					
	
	SELECT @Params = '@StartDate		DATETIME,
					  @EndDate			DATETIME,					  
					  @LstWebsite		NVARCHAR(4000)'
	
	PRINT @Sql
		
	EXEC sp_executesql @Sql, @Params, @StartDate, @EndDate, @LstWebsite
END

```
