# Stored Procedure: `ThucChay_CheckInMappingWebsiteReportingDb`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-06-10 15:37:44.653000
- **Ngày sửa cuối**: 2022-06-06 17:09:10.533000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_CheckInMappingWebsiteReportingDb]
AS
BEGIN
	DECLARE @NgayThucHien Datetime, @Count int = 0, @slsite int = 0, @v_TenWebsite nvarchar(200)
	    SET @Count = 0
		SET @slsite = 0
		SET @v_TenWebsite = ''
		
		SET @NgayThucHien = DateAdd(day,-2,getdate())

		--1. THUC HIEN CHECK XEM DOMAIN WEBSITE TAO CO TREN TABLE dbo.DmWebsiteReportingdb, NEU CHUA CO THI TAO
		SET @slsite = ( SELECT  COUNT(DISTINCT a.DoMainWebsite)
                                        FROM    ( SELECT    [dbo].[GetWebsiteIDByDomainName](DoMainWebsite) DmWebsiteREF ,
                                                            DoMainWebsite
                                                  FROM      dbo.DmWebsite
                                                  WHERE     CONVERT(DATE, LastmodifiedAt) >= @NgayThucHien
                                                            AND DeletedStatus = 0
															and DoMainWebsite is not null
                                                ) a
                                        WHERE   a.DmWebsiteREF IS NULL
                                      )
        IF ( @slsite > 0 )
            WHILE @Count < @slsite
                BEGIN
                    SET @v_TenWebsite = ( SELECT TOP (1)
                                                DoMainWebsite
                                            FROM
                                                ( SELECT
                                                [dbo].[GetWebsiteIDByDomainName](TenWebsite) DmWebsiteREF ,
                                                DoMainWebsite
                                                FROM      dbo.DmWebsite
                                                 WHERE     CONVERT(DATE, LastmodifiedAt) >= @NgayThucHien
                                                            AND DeletedStatus = 0
															and DoMainWebsite is not null
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
		
		--2. CHECK XEM CHUNG SITE NAO CHƯA MAPPING THI THUC HIEN TAO DU LIEU MAPPING
		INSERT INTO WebsiteMapping_HDCN_Reporting
		(DmWebsiteID, WebsiteLink, DmWebsiteReportingdbID, CREATED_AT, LASTMODIFIED_AT)
		SELECT DISTINCT W.DmWebsiteID AS DmWebsiteID_S, W.DomainWebsite, W.DmWebsiteReportingdbID AS DmWebsiteReportingdbID_S , GETDATE(), GETDATE() FROM WebsiteMapping_HDCN_Reporting M
		RIGHT JOIN
		(
			SELECT    [dbo].[GetWebsiteIDByDomainName](DoMainWebsite) AS DmWebsiteReportingdbID ,
					   DmWebsiteID,
					   DoMainWebsite
            FROM      dbo.DmWebsite
            WHERE    1=1 
					--AND  CONVERT(DATE, LastmodifiedAt) >= @NgayThucHien
                    AND DeletedStatus = 0
					and DoMainWebsite is not null
		)W ON M.DmWebsiteID = W.DmWebsiteID OR M.DmWebsiteReportingdbID = W.DmWebsiteReportingdbID
		WHERE (W.DmWebsiteID IS NOT NULL AND W.DmWebsiteReportingdbID IS NOT NULL)
		AND (M.DmWebsiteID IS NULL AND M.DmWebsiteReportingdbID IS NULL)


END


```
