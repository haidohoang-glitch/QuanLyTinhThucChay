# Stored Procedure: `Rpt_JobsDailyWebsiteProduct`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-11-13 11:19:40.900000
- **Ngày sửa cuối**: 2014-11-13 11:19:40.900000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--EXEC [Rpt_JobsDailyWebsiteProduct]
CREATE  PROCEDURE [dbo].[Rpt_JobsDailyWebsiteProduct]
AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @FromDate DATETIME, @NgayThucChay DATETIME
	SET @NgayThucHien = convert(date,DATEADD(DAY,-1,GETDATE()))
	SET @NgayThucChay =
	(
		SELECT MAX(rwp.NgayThucHien) FROM ThucChayDaTinh rwp	
	)
	
	SET @FromDate =
	(
		SELECT MAX(rwp.NgayThucHien) FROM rptWebsiteProduct rwp	
	)
	SET @FromDate = ISNULL(@FromDate,'2010-01-01')
	IF(@NgayThucChay > @FromDate)
	 SET @NgayThucHien = @NgayThucChay
	ELSE
	 SET @NgayThucHien = @FromDate
	EXEC [dbo].[Rpt_InsertWebsiteProduct] @FromDate, @NgayThucHien
END
```
