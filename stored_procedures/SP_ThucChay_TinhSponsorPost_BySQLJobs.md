# Stored Procedure: `ThucChay_TinhSponsorPost_BySQLJobs`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-12 18:01:09.850000
- **Ngày sửa cuối**: 2015-04-08 15:35:44.320000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--exec [ThucChay_TinhSponsorPost_BySQLJobs]
CREATE PROCEDURE [dbo].[ThucChay_TinhSponsorPost_BySQLJobs]
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
		WHERE tcdt.DmSanPhamREF = 381
		AND tcdt.DmSanPhamREF <> 13
	)
	
	SET @StartDate = DATEADD(dd, 1, @StartDate);
			
	SET @EndDate = GETDATE();
	SET @EndDate = DATEADD(dd,-1,@EndDate);
	
	-- Tinh thuc chay Sponsor	
	EXEC ThucChay_ExcInsertThucChayDaTinh_SponsorPost_v2 @StartDate, @EndDate
	-- Update gia tri thay doi
	EXEC [ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_SponsorPost] @StartDate,@EndDate
	
	INSERT INTO ThucChayDaTinh
		SELECT * FROM ThucChayDaTinhSponsorPost tcdtsp WHERE tcdtsp.NgayThucHien BETWEEN @StartDate AND @EndDate
		
	UPDATE ThucChayDaTinh SET TenSanPham = 'Sponsored Post' WHERE DmSanPhamREF = 381 AND NgayThucHien BETWEEN @StartDate AND @EndDate
	UPDATE HopDongChiTiet SET TenSanPham = 'Sponsored Post' WHERE DmSanPhamREF = 381
END


```
