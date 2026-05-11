# Stored Procedure: `SYN_ThucChay_PerformanceBase_CURRENTDAY`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-04-14 10:33:06.910000
- **Ngày sửa cuối**: 2020-06-08 09:12:09.107000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
/*
EXEC [dbo].[SYN_ThucChay_PerformanceBase_CURRENTDAY] @NgayThucHien = CONVERT(DATE,DATEADD(DAY,-1,GETDATE()))
*/

CREATE PROCEDURE [dbo].[SYN_ThucChay_PerformanceBase_CURRENTDAY]
    @NgayThucHien DATETIME 
AS
BEGIN
	--XOA THONG TIN THUC CHAY TRUOC KHI CHAY CAP NHAT
	DELETE FROM dbo.DataThucChay_PerformanceBase_CurrentDay
	WHERE NGAYTHUCHIEN = @NgayThucHien

	--CHECK THONG TIN DOMAIN 
	DECLARE @Count INT,@slsite INT, @v_TenWebsite NVARCHAR(500)
	SET @Count = 0
    SET @slsite = 0
    SET @v_TenWebsite =''
    
    SET @slsite = ( SELECT  COUNT(DISTINCT a.TenWebsite)
					FROM    ( SELECT    [dbo].[GetWebsiteIDByDomainName](domain) AS DmWebsiteREF ,
                                    domain AS TenWebsite
                            FROM [asd14].ABM_Data_Partner.dbo.DOMAIN
                            WHERE    created_date = @NgayThucHien
                                  
                        ) a
                WHERE   a.DmWebsiteREF IS NULL
                )
    IF ( @slsite > 0 )
    WHILE @Count < @slsite
        BEGIN
            SET @v_TenWebsite = ( SELECT TOP (1)
                                        TenWebsite
                                    FROM
                                        ( 
											SELECT
											[dbo].[GetWebsiteIDByDomainName](domain) AS DmWebsiteREF ,
											domain AS TenWebsite
											FROM [asd14].ABM_Data_Partner.dbo.DOMAIN											
											WHERE created_date = @NgayThucHien
                                        ) a
                                    WHERE
                                        a.DmWebsiteREF IS NULL
										ORDER BY a.DmWebsiteREF
                                )
    									
    		IF @v_TenWebsite IS NOT NULL
    			BEGIN
    				INSERT  INTO dbo.DmWebsiteReportingdb
    						( TenWebsite ,
    							CreatedBy ,
    							CreatedAt ,
    							LastModifiedBy ,
    							LastModifiedAt ,
    							DeletedStatus ,
    							PrintStatus ,
    							RecordStatus ,
    							ID
    						)
    				VALUES  ( @v_TenWebsite ,	-- TenWebsite - nvarchar(200)
    							N'asd' ,	-- CreatedBy - nvarchar(50)
    							GETDATE() ,	-- CreatedAt - datetime
    							N'asd' ,	-- LastModifiedBy - nvarchar(50)
    							GETDATE() ,	-- LastModifiedAt - datetime
    							0 ,	-- DeletedStatus - int
    							0 ,	-- PrintStatus - int
    							0 ,	-- RecordStatus - int
    							N'New' -- ID - nvarchar(50)
    						)	
    			END
                                        
    
            SET @Count = @Count + 1
        END

	--------THONG TIN DU LIEU CURRENT DAY--------------------------
	---LAY TOAN BO DU LIEU DOMAIN VOI CONTRACT_ID <> 0
	INSERT INTO [dbo].[DataThucChay_PerformanceBase_CurrentDay]
	(
	    [CONTRACT_NUMBER],
	    [USER_ID],
	    [USER_NAME],
	    [IS_NOIBO],
	    [NGAYTHUCHIEN],
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
	
	SELECT CT.contract
	, CONVERT(INT,ISNULL(DM.user_id,0)) AS user_id
	, DM.username
	, CONVERT(INT,ISNULL(DM.isnoibo,0)) AS isnoibo
	, DM.created_date
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
	, 'API_CURRENT_DAY'
	, 0
	FROM [asd14].ABM_Data_Partner.dbo.CONTRACTS CT
	INNER JOIN
	(
		SELECT * FROM [asd14].ABM_Data_Partner.dbo.DOMAIN
		WHERE contract_id <> 0
		AND re_add_id = 0
		AND created_date = @NgayThucHien
	)DM ON CT.Id = DM.contract_id

	---LAY DU LIEU CUA PHAN CON LAI ONLINE CUA DOMAIN
	INSERT INTO [dbo].[DataThucChay_PerformanceBase_CurrentDay]
	(
	    [CONTRACT_NUMBER],
	    [USER_ID],
	    [USER_NAME],
	    [IS_NOIBO],
	    [NGAYTHUCHIEN],
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
	SELECT '' contract
	, CONVERT(INT,ISNULL(DM.user_id,0))user_id
	, DM.username
	, CONVERT(INT,ISNULL(DM.isnoibo,0))isnoibo
	, DM.created_date
	, (CASE WHEN DM.adx_type IN ( N'mobx', N'adx',N'ecomx') THEN 585 --Adx
		WHEN DM.adx_type = N'cpc' THEN 144 --CPC Admarket
		ELSE 0
	END) AS DmSanPhamREF
	, DM.adx_type 
	, ISNULL(dbo.GetWebsiteIDByDomainName(DM.domain),0) AS Domain_id
	, DM.domain
	, (DM.totalMoneys - ISNULL(CT.totalMoneys,0))totalMoneys
	, (DM.totalclick - ISNULL(CT.totalclick,0))totalclick
	, (DM.totalviews - ISNULL(CT.totalviews,0))totalviews
	, GETDATE()
	, 'API_CURRENT_DAY'
	, 0
		FROM 
	(
		SELECT user_id, username, domain, isnoibo
		, SUM(CONVERT(BIGINT,money))totalMoneys
		, SUM(CONVERT(BIGINT, click))totalclick
		, SUM(CONVERT(BIGINT, [view]))totalviews
		, created_date
		, adx_type FROM [asd14].ABM_Data_Partner.dbo.DOMAIN
		WHERE contract_id = 0
		AND re_add_id = 0
		AND created_date = @NgayThucHien
		GROUP BY user_id, username, domain, created_date
		, adx_type, isnoibo
	)DM
	LEFT JOIN 
	(
		SELECT user_id, username, domain, isnoibo
		, SUM(CONVERT(BIGINT,money))totalMoneys
		, SUM(CONVERT(BIGINT, click))totalclick
		, SUM(CONVERT(BIGINT, [view]))totalviews
		, created_date
		, adx_type FROM [asd14].ABM_Data_Partner.dbo.DOMAIN
		WHERE contract_id <> 0
		AND re_add_id = 0
		AND created_date = @NgayThucHien
		GROUP BY user_id, username, domain, created_date
		, adx_type, isnoibo
	)CT ON CT.adx_type = DM.adx_type AND CT.created_date = DM.created_date
	AND CT.domain = DM.domain AND CT.user_id = DM.user_id AND CT.username = DM.username
	AND CT.isnoibo = DM.isnoibo
END



```
