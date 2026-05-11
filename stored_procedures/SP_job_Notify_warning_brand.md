# Stored Procedure: `job_Notify_warning_brand`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-04 16:55:05.777000
- **Ngày sửa cuối**: 2016-11-18 16:42:41.233000

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
EXEC [dbo].[job_Notify_warning_brand]	
*/
CREATE PROCEDURE [dbo].[job_Notify_warning_brand]
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = CONVERT(date,DATEADD(DAY,-1,CONVERT(DATE,GETDATE())))

	EXEC [dbo].[Notify_warning_brand_input] @NgayThucHien

END

```
