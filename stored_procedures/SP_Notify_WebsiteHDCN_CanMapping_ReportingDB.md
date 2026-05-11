# Stored Procedure: `Notify_WebsiteHDCN_CanMapping_ReportingDB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-10-07 15:16:45.547000
- **Ngày sửa cuối**: 2016-10-07 15:16:45.547000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-18
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[Notify_WebsiteHDCN_CanMapping_ReportingDB]
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = CONVERT(DATE,GETDATE())

	SELECT DmWebsiteID, TenWebsite, CreatedBy, CreatedAt
	FROM dbo.DmWebsite
	WHERE CONVERT(DATE,CreatedAt) = @NgayThucHien	
END

```
