# Stored Procedure: `ThucChaySponsor_InsertToTemp`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-01 15:53:36.217000
- **Ngày sửa cuối**: 2015-04-01 15:53:36.217000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@shd` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhaMQ
-- Create date: 2014-05-20
-- Description:	Insert Thucchay Mobile to Temp table 
-- =============================================
-- EXEC dbo.ThucChayMobile_InsertToTemp '2014-05-21 00:00:00.000', '2014-05-21 00:00:00.000'
CREATE PROCEDURE [dbo].[ThucChaySponsor_InsertToTemp] 
	-- Add the parameters for the stored procedure here
	@StartDate	DATETIME,
	@EndDate	DATETIME,
	@shd NVARCHAR(50)
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
	-- Delete if exists
	DELETE ThucChaySponsorTemp WHERE dt BETWEEN @StartDate AND @EndDate AND typeproduct = -1

	-- Insert Data to temp table
	INSERT INTO ThucChaySponsorTemp
    SELECT 
		T.typeproduct,T.ProductId,T.ProductName,T.[Contract],T.CampaignId,T.BannerId,T.BannerType,T.SiteId,T.SiteName,T.dt,
		SUM(T.TotalView) TotalView, SUM(T.TotalClick) TotalClick, T.UnitId, T.UnitName,
		T.Activate,T.Expire, T.UserName,T.SaleName,T.Email, T.HopDongChiTietREF
	FROM
	(
		SELECT 
			tcm.typeproduct,tcm.DmSanPhamREF ProductId, tcm.TenSanPham ProductName, 
			dbo.ThucChay_FormatSoHopDong(tcm.SoHopDong) [Contract], 
			1111 CampaignId, 1111 BannerId,
			--CASE WHEN (tcm.BannerType = 2 OR tcm.BannerType = 5) THEN 9021
			--	 --WHEN tcm.BannerType = 3 THEN 9024
			--	 ELSE 9023
			--END BannerType,
			tcm.BannerType,
			1111 SiteId,
			dbo.ThucChay_FormatDomainName(tcm.TenWebsite) SiteName, tcm.NgayThucHien dt,
			tcm.TongViewThucChay TotalView, tcm.TongClickThucChay TotalClick, 
			tcm.ProductUnitID as UnitID,
			CASE WHEN tcm.ProductUnitID = 1 THEN 'CLICK'
				 ELSE 'VIEW'
			END UnitName,
			tcm.NgayThucHien Activate,tcm.NgayThucHien Expire,tcm.UserName,tcm.SaleName,tcm.Email, tcm.HopDongChiTietREF
			
		FROM [ABM_Data_Release].dbo.ThucChay AS tcm
		WHERE tcm.TypeProduct = -1
			AND tcm.NgayThucHien BETWEEN @StartDate AND @EndDate 
			AND dbo.ThucChay_FormatSoHopDong(tcm.SoHopDong) = @shd
	)T
	GROUP BY T.typeproduct,T.ProductId,T.ProductName,T.[Contract],T.CampaignId,T.BannerId,T.BannerType,T.UnitId,T.UnitName,T.SiteId,T.SiteName,T.dt,
			T.Activate,T.Expire, T.UserName,T.SaleName,T.Email, T.HopDongChiTietREF
END

```
