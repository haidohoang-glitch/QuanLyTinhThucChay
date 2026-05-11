# Stored Procedure: `ThucChay_TinhMuaNgoai_BySQLJobs`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-01-14 11:33:07.427000
- **Ngày sửa cuối**: 2020-09-04 15:04:48.530000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2015-01-14
-- Description:	<Description,,>
-- =============================================
--EXEC [dbo].[ThucChay_TinhMuaNgoai_BySQLJobs]

CREATE PROCEDURE [dbo].[ThucChay_TinhMuaNgoai_BySQLJobs]
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
		FROM dbo.ThucChayDaTinh AS tcdt
		WHERE (tcdt.DmHinhThucQuangCao = 13 OR tcdt.DmLoaiBannerREF = 18)
	)
	
	SET @StartDate = DATEADD(dd, 1, @StartDate);
			
	SET @EndDate = GETDATE();
	SET @EndDate = Convert(date,DATEADD(dd,-1,@EndDate));

	--SET @StartDate = '2018-11-01'
	--SET @EndDate = '2018-11-01'
	-- Tinh thuc chay MuaNgoai
	--EXEC dbo.ThucChayDaTinh_MuaNgoai_ExcThucChayByDay @EndDate, @EndDate

	--TINH THUC CHAY MUA NGOAI HANG NGAY
	EXEC  [dbo].[ThucChayDaTinh_ExecThucChayMuaNgoaiChiTiet] @NgayThucHien = @EndDate
	--TINH GIA TRI THAY DOI MUA NGOAI
	EXEC  [dbo].[ThucChayDaTinh_UpdateGiaTriThayDoiMuaNgoaiChiTiet] @NgayThucHien = @EndDate
	--DAY THONG TIN THUC CHAY MUA NGOAI CUA ADMARKET SANG THUC CHAY ADMARKET
	EXEC [dbo].[ThucChayDaTinh_MuaNgoai_SendThucChayDaTinhAdmarket] @NgayThucHien = @EndDate

END



```
