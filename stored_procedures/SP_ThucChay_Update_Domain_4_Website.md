# Stored Procedure: `ThucChay_Update_Domain_4_Website`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-06-22 16:50:53.830000
- **Ngày sửa cuối**: 2020-06-08 09:14:28.703000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
/*
EXEC [dbo].[ThucChay_Update_Domain_4_Website] 
*/
CREATE PROCEDURE [dbo].[ThucChay_Update_Domain_4_Website] 	
As 	

BEGIN
    DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = DATEADD(DAY,-1,@NgayThucHien)
	--SET @NgayThucHien = '2018-06-15'
	CREATE TABLE #ThucChay_domain(    
		DOMAIN_ID  int
    ,	DOMAIN_NAME nvarchar(500)
    ,   WEBSITE_ID int
    ,   WEBSITE_NAME nvarchar(500)
    ,   CREATED_BY  nvarchar(50)
    ,	CREATED_AT  datetime
	,   LASTMODIFIED_BY  nvarchar(50)
	,	LASTMODIFIED_AT  datetime
    ,   DELETED_STATUS smallint
    ,   RECORD_STATUS  int
	,	NOTE nvarchar(500)
	,	[STATUS] SMALLINT
	  )

	CREATE TABLE #dm_domain_main(    
		WEBSITE_ID int
    ,   WEBSITE_NAME nvarchar(500)
   )

	  INSERT INTO #ThucChay_domain
	  (
	      DOMAIN_ID,
	      DOMAIN_NAME,
	      WEBSITE_ID,
	      WEBSITE_NAME,
	      CREATED_BY,
	      CREATED_AT,
	      LASTMODIFIED_BY,
	      LASTMODIFIED_AT,
	      DELETED_STATUS,
	      RECORD_STATUS,
	      NOTE,
		  [STATUS]
	  )
	SELECT	DmWebsiteREF,
			TenWebsite ,
			DmWebsiteREF,
			TenWebsite,
			'ASD' AS Created_by,
			GETDATE() CreatedAt,
			'ASD' AS LastModified_by,
			GETDATE() LastModified_at,
			0 Deleted_Status,
			0 Record_Status,
			'' note,
			0 AS statuss
	FROM dbo.ThucChay
	WHERE TypeProduct >0
	AND NgayThucHien = @NgayThucHien
	--AND NgayThucHien >= '2019-01-01'
	GROUP BY DmWebsiteREF,
			TenWebsite ,
			DmWebsiteREF,
			TenWebsite
	
	--DANH SACH WEBSITE CUA DOMAIN
	INSERT INTO #dm_domain_main
	(
	    WEBSITE_ID,
	    WEBSITE_NAME
	)
	SELECT WEBSITE_ID, WEBSITE_NAME FROM dbo.DM_DOMAIN
	WHERE WEBSITE_NAME <>''
	GROUP BY WEBSITE_ID, WEBSITE_NAME

    UPDATE #ThucChay_domain 
    SET    [STATUS] = 1
    FROM  #ThucChay_domain t INNER JOIN dbo.DM_DOMAIN dc
    ON t.DOMAIN_ID = dc.DOMAIN_ID



	--Cap nhat thong tin website
	UPDATE #ThucChay_domain
	SET WEBSITE_ID = ISNULL((SELECT TOP (1) D.WEBSITE_ID FROM #dm_domain_main D
							WHERE ( DOMAIN_NAME LIKE D.WEBSITE_NAME + '%' OR DOMAIN_NAME LIKE '%.' +  D.WEBSITE_NAME) ORDER BY D.WEBSITE_ID),DOMAIN_ID)
	, WEBSITE_NAME = ISNULL((SELECT TOP (1) D.WEBSITE_NAME FROM #dm_domain_main D
							WHERE ( DOMAIN_NAME LIKE D.WEBSITE_NAME + '%' OR DOMAIN_NAME LIKE '%.' +  D.WEBSITE_NAME) ORDER BY D.WEBSITE_ID),DOMAIN_NAME)
	WHERE [STATUS] = 0

	INSERT INTO dbo.DM_DOMAIN
	(
	    DOMAIN_ID,
	    DOMAIN_NAME,
	    WEBSITE_ID,
	    WEBSITE_NAME,
	    CREATED_BY,
	    CREATED_AT,
	    LASTMODIFIED_BY,
	    LASTMODIFIED_AT,
	    DELETED_STATUS,
	    RECORD_STATUS,
	    NOTE
	)
	SELECT  DOMAIN_ID,
	      DOMAIN_NAME,
	      WEBSITE_ID,
	      WEBSITE_NAME,
	      CREATED_BY,
	      CREATED_AT,
	      LASTMODIFIED_BY,
	      LASTMODIFIED_AT,
	      DELETED_STATUS,
	      RECORD_STATUS,
	      NOTE 
	FROM #ThucChay_domain              
	WHERE [STATUS] = 0                  
 
END

```
