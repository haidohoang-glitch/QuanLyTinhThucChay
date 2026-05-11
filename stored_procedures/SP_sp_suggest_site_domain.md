# Stored Procedure: `sp_suggest_site_domain`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-03-13 15:14:05.607000
- **Ngày sửa cuối**: 2017-03-13 15:14:40.863000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@KeyName` | `nvarchar(200)` | No |
| `@KeyWord` | `nvarchar(1000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [dbo].[sp_suggest_site_domain]  'WEBSITE', 'dantri'

CREATE  PROCEDURE [dbo].[sp_suggest_site_domain]
    (
      @KeyName NVARCHAR(100) ,
      @KeyWord NVARCHAR(500)
    )
AS
    BEGIN
        DECLARE @v_KeyName NVARCHAR(100) ,
            @v_KeyWord NVARCHAR(300)
        DECLARE @TableDmMuc TABLE
            (
              [value] INT ,
              [text] NVARCHAR(300)
            )  
        DECLARE @top INT
        SET @v_KeyName = UPPER(@KeyName)
        SET @v_KeyWord = @KeyWord
        SET @top = 20
	-- 
	----THONG TIN TRANG THAI DAU MOI CRM
 --       IF ( @v_KeyName = 'TRANGTHAIDAUMOI' )
 --           BEGIN
 --               SELECT  NAME [value] ,
 --                       DISPLAY_NAME [text]
 --               FROM    [SplendidCRM].dbo.vwTERMINOLOGY_List
 --               WHERE   1 = 1
 --                       AND LIST_NAME = 'lead_status_dom'
 --                       AND LANG = 'vi-VN'
 --                       AND NAME LIKE N'%' + @v_KeyWord + '%'
		
 --           END
	-- thong tin hop dong thay doi ban salary
	if ( @v_KeyName = 'WEBSITE' )
	begin
	  SELECT TOP 20
                        A.DmWebsiteReportingdbID AS [value] ,
                        A.TenWebsite AS [text]
                FROM    ( SELECT    dnh.DmWebsiteReportingdbID ,
                                    dnh.TenWebsite ,
                                    PATINDEX('%' + UPPER(@v_KeyWord) + '%',
                                             UPPER(dnh.TenWebsite)) stt ,
                                    PATINDEX('%' + REVERSE(UPPER(@v_KeyWord))
                                             + '%',
                                             REVERSE(UPPER(dnh.TenWebsite))) stt1
                          FROM      dbo.DmWebsiteReportingdb dnh
                          WHERE     PATINDEX('%' + UPPER(@v_KeyWord) + '%',
                                             UPPER(dnh.TenWebsite) COLLATE SQL_Latin1_General_CP1_CI_AI) <> 0
                                    AND dnh.DeletedStatus = 0
                        ) A
                ORDER BY stt ,
                        stt1
	end
		
    END



```
