# Stored Procedure: `ThucChay_TinhAdmarket_BySQLJobs`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-16 14:35:17.750000
- **Ngày sửa cuối**: 2017-06-29 16:53:08.387000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_TinhAdmarket_BySQLJobs] 
CREATE PROCEDURE [dbo].[ThucChay_TinhAdmarket_BySQLJobs] 
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
		FROM ThucChayDaTinhAdmarket AS tcdt
		WHERE tcdt.DmSanPhamREF IN (144,299,337,585)
		AND NOT(tcdt.DmHinhThucQuangCao = 13 OR tcdt.DmLoaiBannerREF = 18)
	)
	
	SET @StartDate = DATEADD(dd, 1, @StartDate);
			
	SET @EndDate = GETDATE();
	SET @EndDate = DATEADD(dd,-1,@EndDate);
	
	--SET @StartDate= '2017-06-28'
	--SET @EndDate = '2017-06-28'
	
	-- Tinh thuc chay Admarket
	--EXEC dbo.ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket @StartDate, @EndDate
	EXEC [dbo].[ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket_haidh] @StartDate, @EndDate
				
END




```
