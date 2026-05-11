# Stored Procedure: `Rpt_DanhSachWebsiteSanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-07-30 14:54:01.927000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.300000

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
-- Rpt_DanhSachWebsiteSanPham '2014-01-01', '2014-01-05', '' 
-- =============================================
CREATE PROCEDURE [dbo].[Rpt_DanhSachWebsiteSanPham] 
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
							ROW_NUMBER() OVER (ORDER BY A.DmWebsiteREF DESC) STT,
							A.TenWebsite, 				
							dbo.FormatNumber(SUM(A.Adpage)) Adpage,
							dbo.FormatNumber(SUM(A.SponsoredPost)) SponsoredPost,
							dbo.FormatNumber(SUM(A.DangTin)) DangTin,
							dbo.FormatNumber(SUM(A.BalloonAds)) BalloonAds,
							dbo.FormatNumber(SUM(A.TVCOnline)) TVCOnline,
							dbo.FormatNumber(SUM(A.CPMMass)) CPMMass,
							dbo.FormatNumber(SUM(A.Mobile)) Mobile,
							dbo.FormatNumber(SUM(A.BannerCPD)) BannerCPD,
							dbo.FormatNumber(SUM(A.BannerCPDChuyentrang)) BannerCPDChuyentrang,
							dbo.FormatNumber(SUM(A.BoxappCPD)) BoxappCPD,
							dbo.FormatNumber(SUM(A.BoxappCPM)) BoxappCPM,
							dbo.FormatNumber(SUM(A.BoxappSelfServing)) BoxappSelfServing,
							dbo.FormatNumber(SUM(A.BoxappMultiBrand)) BoxappMultiBrand,
							dbo.FormatNumber(SUM(A.CPCAdmarket)) CPCAdmarket,
							dbo.FormatNumber(SUM(A.CPCPlus)) CPCPlus,
							dbo.FormatNumber(SUM(A.CPA)) CPA,
							dbo.FormatNumber(SUM(A.CPMAdmarket)) CPMAdmarket,
							dbo.FormatNumber(SUM(A.GoogleAds)) GoogleAds,
							dbo.FormatNumber(SUM(A.SPKhac)) SPKhac							
					FROM rptWebsiteProduct A
					WHERE ' + @Filter + '
					GROUP BY A.TenWebsite, A.DmWebsiteREF
					
					
					'
					
	
	SELECT @Params = '@StartDate		DATETIME,
					  @EndDate			DATETIME,					  
					  @LstWebsite		NVARCHAR(4000)'
	
	PRINT @Sql
		
	EXEC sp_executesql @Sql, @Params, @StartDate, @EndDate, @LstWebsite
END

```
