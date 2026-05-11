# Stored Procedure: `job_Notify_warning_brand_calc`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-04 16:54:21.787000
- **Ngày sửa cuối**: 2016-11-08 10:52:51.040000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
EXEC [dbo].[job_Notify_warning_brand_calc]	
*/
CREATE PROCEDURE [dbo].[job_Notify_warning_brand_calc]
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = DATEADD(DAY,-1,CONVERT(DATE,GETDATE())) 

	EXEC [dbo].[Notify_warning_brand_calc] @NgayThucHien

END

```
