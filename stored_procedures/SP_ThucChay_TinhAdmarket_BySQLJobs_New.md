# Stored Procedure: `ThucChay_TinhAdmarket_BySQLJobs_New`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-15 14:12:20.623000
- **Ngày sửa cuối**: 2017-07-01 12:29:20.123000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		DOANNV
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--
CREATE PROCEDURE [dbo].[ThucChay_TinhAdmarket_BySQLJobs_New] 
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
		WHERE tcdt.DmSanPhamREF IN (144,628,337,585)
		AND NOT(tcdt.DmHinhThucQuangCao = 13 OR tcdt.DmLoaiBannerREF = 18)
	)
	
	SET @StartDate = DATEADD(dd, 1, @StartDate);
			
	SET @EndDate = GETDATE();
	SET @EndDate = DATEADD(dd,-1,@EndDate);
	
	--SET @StartDate= '2017-06-30'
	--SET @EndDate = '2017-06-30'
	
	-- Tinh thuc chay Admarket
	--EXEC dbo.ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket @StartDate, @EndDate
	EXEC [dbo].[Admarket_ThucChayDaTinhAdmarket_NhanHang] @StartDate, @EndDate
END




```
