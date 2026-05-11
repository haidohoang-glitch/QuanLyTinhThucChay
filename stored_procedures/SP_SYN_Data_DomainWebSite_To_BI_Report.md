# Stored Procedure: `SYN_Data_DomainWebSite_To_BI_Report`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-06-30 10:13:44.560000
- **Ngày sửa cuối**: 2020-09-22 15:39:47.627000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[SYN_Data_DomainWebSite_To_BI_Report]
AS
BEGIN

	DECLARE @Table_DM_DOMAIN TABLE(
		  ID int
	    , DOMAIN_ID INT
	    , DOMAIN_NAME NVARCHAR(100)
		, WEBSITE_ID INT
	    , WEBSITE_NAME nvarchar(100)
        , STATUS_UPDATE SMALLINT
		)

	INSERT @Table_DM_DOMAIN
	(
	    ID,
	    DOMAIN_ID,
	    DOMAIN_NAME,
	    WEBSITE_ID,
	    WEBSITE_NAME,
	    STATUS_UPDATE
	)
	SELECT  ID,DOMAIN_ID,DOMAIN_NAME,WEBSITE_ID,WEBSITE_NAME, 0 AS STATUS_UPDATE
			FROM ABM_Data_ThucChay.dbo.DM_DOMAIN
			WHERE DELETED_STATUS = 0

	--CHECK THÔNG TIN UPDATE/INSERT
	UPDATE @Table_DM_DOMAIN
	SET STATUS_UPDATE = 1
	FROM @Table_DM_DOMAIN A
	INNER JOIN [192.168.23.150].BI_Report.dbo.DM_DOMAIN B ON A.ID = B.ID
	AND A.DOMAIN_ID = B.DOMAIN_ID AND A.WEBSITE_ID = B.WEBSITE_ID


	--INSERT DL Mới
	INSERT INTO [192.168.23.150].BI_Report.dbo.DM_DOMAIN
	(
	    ID,
	    DOMAIN_ID,
	    DOMAIN_NAME,
	    WEBSITE_ID,
	    WEBSITE_NAME
	)
	SELECT 
	    ID,
	    DOMAIN_ID,
	    DOMAIN_NAME,
	    WEBSITE_ID,
	    WEBSITE_NAME
	FROM @Table_DM_DOMAIN WHERE STATUS_UPDATE = 0  
	-- Update dữ liệu sửa bên ABM
	UPDATE [192.168.23.150].BI_Report.dbo.DM_DOMAIN
	SET 
		DOMAIN_ID		= b.DOMAIN_ID
	    ,DOMAIN_NAME	= b.DOMAIN_NAME
	    ,WEBSITE_ID		= b.WEBSITE_ID
	    ,WEBSITE_NAME	= b.WEBSITE_NAME
	FROM  [192.168.23.150].BI_Report.dbo.DM_DOMAIN a JOIN ABM_Data_ThucChay.dbo.DM_DOMAIN b ON a.ID = b.ID
	WHERE ISNULL(b.LASTMODIFIED_AT,'1900-01-01') >=   DATEADD (DAY,-1,GETDATE())


END
```
