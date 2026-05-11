# Stored Procedure: `ThucChay_TinhGoogleFacebook_BySQLJobs`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-08 10:00:26.430000
- **Ngày sửa cuối**: 2020-10-19 15:19:03.623000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_TinhGoogleFacebook_BySQLJobs] 
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @StartDate	DATETIME,
			@EndDate	DATETIME		
	
	SET @StartDate = CONVERT(DATE, DATEADD(dd, -1, GETDATE()));			
	SET @EndDate = CONVERT(DATE, DATEADD(dd, -1, GETDATE()));
	
	PRINT @StartDate;
	PRINT @EndDate;


	----SET @StartDate = '2017-10-05'


	---- Xoa phan bo
	--EXEC ThucChay_GoogleFacebook_HuyPhanBo @StartDate

	---- TH phan bo giam gia tri
	--EXEC ThucChay_GoogleFacebook_PhanBoGiamGiaTri @StartDate


	---- Tinh thuc chay Google, Facebook
	------HAIDH COMMENT SP NAY LA VA CHAY SP BEN DUOI 2016-10-25
	----EXEC dbo.ThucChayDaTinh_ExcInsertThucChayDaTinhGG_FB @StartDate, @EndDate; 
	--EXEC [dbo].[ThucChay_GoogleFacebook_Doannv] @StartDate;

	EXEC [dbo].[ThucChay_TinhThucChayThanhTien_GGFB_BySQLJobs] @NgayThucHien = @EndDate

END

```
