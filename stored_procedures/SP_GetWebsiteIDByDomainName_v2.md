# Stored Procedure: `GetWebsiteIDByDomainName_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-02 10:54:04.133000
- **Ngày sửa cuối**: 2018-10-04 14:35:30.683000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TenWebsite` | `nvarchar(100)` | No |
| `@out_ID` | `int(4)` | Yes |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
/*
Declare @id int
EXEC [dbo].[GetWebsiteIDByDomainName_v2] N'kenh14.vn',@id out
*/
CREATE PROCEDURE [dbo].[GetWebsiteIDByDomainName_v2]
(
	@TenWebsite NVARCHAR(50),
	@out_ID INT OUT
)
AS
BEGIN
	DECLARE @ID INT, @DateNow DATETIME
	
	IF(EXISTS(SELECT DmWebsiteReportingdbID FROM dbo.DmWebsiteReportingdb
			WHERE TenWebsite = @TenWebsite AND DeletedStatus = 0))
	BEGIN
		SET @ID = (SELECT TOP (1) DmWebsiteReportingdbID FROM dbo.DmWebsiteReportingdb
						WHERE TenWebsite = @TenWebsite AND DeletedStatus = 0 ORDER BY DmWebsiteReportingdbID
					)
	END
	ELSE
    BEGIN
        INSERT INTO dbo.DmWebsiteReportingdb
	      (
	        TenWebsite,
	        CreatedBy,
	        CreatedAt,
	        LastModifiedBy,
	        LastModifiedAt,
	        DeletedStatus,
	        PrintStatus,
	        RecordStatus,
	        ID
	      )
	    VALUES
	      (
	        @TenWebsite,	-- TenWebsite - nvarchar(200)
	        N'asd',	-- CreatedBy - nvarchar(50)
	        GETDATE(),	-- CreatedAt - datetime
	        N'asd',	-- LastModifiedBy - nvarchar(50)
	        GETDATE(),	-- LastModifiedAt - datetime
	        0,	-- DeletedStatus - int
	        0,	-- PrintStatus - int
	        0,	-- RecordStatus - int
	        N'New' -- ID - nvarchar(50)
	      )		
	    SET @ID = @@IDENTITY
    END
	    
	SET @out_ID = ISNULL(@ID,0)
END



```
