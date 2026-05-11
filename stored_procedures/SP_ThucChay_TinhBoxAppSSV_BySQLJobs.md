# Stored Procedure: `ThucChay_TinhBoxAppSSV_BySQLJobs`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-24 15:51:41.267000
- **Ngày sửa cuối**: 2017-03-01 14:44:37.807000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC dbo.ThucChay_TinhBoxAppSSV_BySQLJobs
CREATE PROCEDURE [dbo].[ThucChay_TinhBoxAppSSV_BySQLJobs]
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @StartDate	DATETIME,
			@EndDate	DATETIME
			
	SET @StartDate = (
		SELECT MAX(NgayThucHien) 
		FROM ThucChayDaTinh AS tcdt
		WHERE tcdt.DmSanPhamREF = 375
	)
	
	SET @StartDate = DATEADD(dd, 1, @StartDate);
			
	SET @EndDate = GETDATE();
	SET @EndDate = DATEADD(dd,-1,@EndDate);

	--SET @StartDate = '2017-02-24'
	--SET @EndDate ='2017-02-26'
	-- Tinh thuc chay BoxApp SSV
	EXEC dbo.ThucChayDaTinh_ExcInsertThucChayDaTinhBoxAppSSV @StartDate, @EndDate
END

```
