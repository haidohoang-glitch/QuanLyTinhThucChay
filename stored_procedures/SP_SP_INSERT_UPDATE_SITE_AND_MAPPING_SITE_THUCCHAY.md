# Stored Procedure: `SP_INSERT_UPDATE_SITE_AND_MAPPING_SITE_THUCCHAY`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-03-13 15:27:27.960000
- **Ngày sửa cuối**: 2017-03-13 15:30:08.643000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmWebsiteID_HDCN` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(600)` | No |
| `@DmWebsiteID_ThucChay` | `int(4)` | No |
| `@Site_domain` | `nvarchar(800)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [dbo].[sp_suggest_site_domain]  'WEBSITE', 'dantri'

CREATE  PROCEDURE [dbo].[SP_INSERT_UPDATE_SITE_AND_MAPPING_SITE_THUCCHAY]
    @DmWebsiteID_HDCN INT,
	@TenWebsite NVARCHAR(300),
	@DmWebsiteID_ThucChay INT,
	@Site_domain NVARCHAR(400),
	@CreatedBy	NVARCHAR(50)
AS
BEGIN   
	--1.INSERT OR UPDATE THONG TIN SITE HDCN DmWebsite
	IF(EXISTS(SELECT * FROM DmWebsite WHERE DmWebsiteID = @DmWebsiteID_HDCN))
	BEGIN
		UPDATE dbo.DmWebsite
		SET LastModifiedBy = @CreatedBy
		WHERE DmWebsiteID = @DmWebsiteID_HDCN
	END
	ELSE
	BEGIN
		INSERT dbo.DmWebsite
		        ( DmWebsiteID ,
		          TenWebsite ,
		          WebsiteLink ,
		          GhiChu ,
		          Code ,
		          DmGroupTypeREF ,
		          IsThuongMaiDienTu ,
		          CreatedBy ,
		          CreatedAt ,
		          LastModifiedBy ,
		          LastModifiedAt ,
		          DeletedStatus ,
		          PrintStatus ,
		          RecordStatus ,
		          DomainWebsite
		        )
		VALUES  ( @DmWebsiteID_HDCN , -- DmWebsiteID - int
		         @TenWebsite , -- TenWebsite - nvarchar(200)
		          @Site_domain , -- WebsiteLink - nvarchar(255)
		          N'' , -- GhiChu - nvarchar(4000)
		          N'' , -- Code - nvarchar(200)
		          0 , -- DmGroupTypeREF - int
		          0 , -- IsThuongMaiDienTu - int
		          @CreatedBy , -- CreatedBy - nvarchar(50)
		          GETDATE() , -- CreatedAt - datetime
		          @CreatedBy , -- LastModifiedBy - nvarchar(50)
		          GETDATE() , -- LastModifiedAt - datetime
		          0 , -- DeletedStatus - int
		          0 , -- PrintStatus - int
		          0 , -- RecordStatus - int
		          @Site_domain  -- DomainWebsite - nvarchar(200)
		        )
	END		
	IF(EXISTS(SELECT * FROM dbo.WebsiteMapping_HDCN_Reporting WHERE DmWebsiteID = @DmWebsiteID_HDCN AND DmWebsiteReportingdbID = @DmWebsiteID_ThucChay))
	BEGIN
		UPDATE dbo.WebsiteMapping_HDCN_Reporting
		SET WebsiteLink = @Site_domain
		WHERE DmWebsiteID = @DmWebsiteID_HDCN AND DmWebsiteReportingdbID = @DmWebsiteID_ThucChay
	END
	ELSE
    BEGIN
    	INSERT dbo.WebsiteMapping_HDCN_Reporting
    	        ( DmWebsiteID ,
    	          WebsiteLink ,
    	          DmWebsiteReportingdbID
    	        )
    	VALUES  ( @DmWebsiteID_HDCN , -- DmWebsiteID - int
    	          @Site_domain , -- WebsiteLink - nvarchar(200)
    	          @DmWebsiteID_ThucChay  -- DmWebsiteReportingdbID - int
    	        )
    END
END



```
