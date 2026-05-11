# Stored Procedure: `ThucChay_GetListWebSite`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-11-20 17:39:09.850000
- **Ngày sửa cuối**: 2014-11-19 12:16:55.117000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-11-18
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_GetListWebSite]
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    SELECT DISTINCT 
		DmWebsiteREF,
		TenWebsite
    FROM 
		ThucChayDaTinh
    ORDER BY 
		TenWebsite
END

```
