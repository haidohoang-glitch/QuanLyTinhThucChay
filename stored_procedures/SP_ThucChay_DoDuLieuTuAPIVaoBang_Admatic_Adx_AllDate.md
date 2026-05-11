# Stored Procedure: `ThucChay_DoDuLieuTuAPIVaoBang_Admatic_Adx_AllDate`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-10-01 15:30:00.190000
- **Ngày sửa cuối**: 2018-10-01 15:30:00.190000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

--=============================================
-- Author:   Nhat Mai Quy
-- Stored Procedure Name: [dbo].[usp_UpdateNhanSuThuViec]
-- Create Date: Monday, August 19, 2013
-- Description: 
--=============================================
--EXEC [dbo].[job_UpdateThucChayHopDongChiTiet_ChiPhiKhac]
CREATE PROCEDURE [dbo].[ThucChay_DoDuLieuTuAPIVaoBang_Admatic_Adx_AllDate] 
AS
    BEGIN
	
        DECLARE @Count INT= 0
        DECLARE @slsite INT = 0
        DECLARE @v_TenWebsite NVARCHAR(1000)

	
        IF EXISTS ( SELECT  *
                        FROM    dbo.DataThucChay_Adx
                        WHERE   1=1
                               AND domain_ID IS NULL )
            BEGIN

                SET @Count = 0
                SET @slsite = 0
                SET @v_TenWebsite = ''

                SET @slsite = ( SELECT  COUNT(DISTINCT a.TenWebsite)
                                FROM    ( SELECT    [dbo].[GetWebsiteIDByDomainName](domain_name) DmWebsiteREF
                                                  , domain_name AS TenWebsite
                                          FROM      dbo.DataThucChay_Adx
                                          WHERE		1=1
                                                    AND domain_ID IS NULL 
                                        ) a
                                WHERE   a.DmWebsiteREF IS NULL
                              )
                IF ( @slsite > 0 )
                    WHILE @Count < @slsite
                        BEGIN
                            SET @v_TenWebsite = ( SELECT TOP 1
                                                            TenWebsite
                                                  FROM      ( SELECT    [dbo].[GetWebsiteIDByDomainName](domain_name) DmWebsiteREF
                                                                      , domain_name as TenWebsite
                                                              FROM      dbo.DataThucChay_Adx
                                                              WHERE     1=1
                                                                        AND domain_ID IS NULL 
                                                            ) a
                                                  WHERE     a.DmWebsiteREF IS NULL
                                                )
									
                            IF @v_TenWebsite IS NOT NULL
                                BEGIN
                                    INSERT  INTO dbo.DmWebsiteReportingdb
                                            ( TenWebsite
                                            , CreatedBy
                                            , CreatedAt
                                            , LastModifiedBy
                                            , LastModifiedAt
                                            , DeletedStatus
                                            , PrintStatus
                                            , RecordStatus
                                            , ID
													
                                            )
                                    VALUES  ( @v_TenWebsite
                                            ,	-- TenWebsite - nvarchar(200)
                                              N'asd'
                                            ,	-- CreatedBy - nvarchar(50)
                                              GETDATE()
                                            ,	-- CreatedAt - datetime
                                              N'asd'
                                            ,	-- LastModifiedBy - nvarchar(50)
                                              GETDATE()
                                            ,	-- LastModifiedAt - datetime
                                              0
                                            ,	-- DeletedStatus - int
                                              0
                                            ,	-- PrintStatus - int
                                              0
                                            ,	-- RecordStatus - int
                                              N'New' -- ID - nvarchar(50)
													
                                            )	
                                END
                                    

                            SET @Count = @Count + 1
                        END


               --UPDATE THONG TIN WEBSTE SITE
			   UPDATE dbo.DataThucChay_Adx
			   SET domain_ID =  [dbo].[GetWebsiteIDByDomainName](domain_name)
			   WHERE 1=1
               AND domain_ID IS NULL 
            END

    END




```
