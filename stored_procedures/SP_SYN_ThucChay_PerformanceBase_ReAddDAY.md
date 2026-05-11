# Stored Procedure: `SYN_ThucChay_PerformanceBase_ReAddDAY`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-04-14 11:08:51.240000
- **Ngày sửa cuối**: 2020-06-08 09:11:38.137000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
/*
EXEC [dbo].[SYN_ThucChay_PerformanceBase_ReAddDAY] @NgayThucHien = '2018-04-15'
*/
CREATE PROCEDURE [dbo].[SYN_ThucChay_PerformanceBase_ReAddDAY]
    @NgayThucHien DATETIME 
AS
BEGIN
	--XOA THONG TIN THUC CHAY TRUOC KHI CAP NHAT
	DELETE FROM dbo.DataThucChay_PerformanceBase_ReAddDay
	WHERE NGAYTHUCHIEN = @NgayThucHien

	-------------------THONG TIN DU LIEU READD DAY------------------------------------
	INSERT INTO  [dbo].[DataThucChay_PerformanceBase_ReAddDay]
	(
	    [CONTRACT_NUMBER],
	    [USER_ID],
	    [USER_NAME],
	    [IS_NOIBO],
	    [NGAYTHUCHIEN],
	    [BASE_DATE],
	    [DMSANPHAMREF],
	    [ADX_TYPE],
	    [DOMAIN_ID],
	    [DOMAIN_NAME],
	    [TOTAL_MONEY],
	    [TOTAL_CLICK],
	    [TOTAL_VIEW],
	    [CREATED_AT],
	    [CREATED_BY],
	    [DELETED_STATUS]
	)
	
	SELECT  (SELECT TOP (1) contract FROM  [asd14].ABM_Data_Partner.[dbo].[RE_ADD] WHERE id = DM.re_add_id ORDER BY id) AS contract
	, CONVERT(INT,ISNULL(DM.user_id,0)) AS user_id
	, DM.username
	, CONVERT(INT,ISNULL(DM.isnoibo,0)) isnoibo
	, DM.created_date
	, CONVERT(DATE,ISNULL(DM.base_dt,'1900-01-01'))base_dt 
	, (CASE WHEN DM.adx_type IN ( N'mobx', N'adx',N'ecomx') THEN 585 --Adx
		WHEN DM.adx_type = N'cpc' THEN 144 --CPC Admarket
		ELSE 0
	END) AS DmSanPhamREF
	, DM.adx_type
	, ISNULL(dbo.GetWebsiteIDByDomainName(DM.domain),0) AS Domain_id
	, DM.domain
	, DM.money totalMoneys
	, DM.click totalclick
	, DM.[view] totalviews 
	, GETDATE()
	, 'API_READD_DAY'
	, 0
	FROM [asd14].ABM_Data_Partner.dbo.DOMAIN DM
	WHERE ISNULL(re_add_id,0) <> 0
	AND base_dt IS NOT NULL
	AND created_date = @NgayThucHien
END



```
