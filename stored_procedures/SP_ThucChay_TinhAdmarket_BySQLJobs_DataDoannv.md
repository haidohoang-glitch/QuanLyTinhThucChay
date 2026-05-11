# Stored Procedure: `ThucChay_TinhAdmarket_BySQLJobs_DataDoannv`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-07-10 17:35:46.370000
- **Ngày sửa cuối**: 2015-07-14 17:09:18.230000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_TinhAdmarket_BySQLJobs_DataDoannv] 
	-- Add the parameters for the stored procedure here	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    DECLARE @StartDate	DATETIME,
			@EndDate	DATETIME
			
	--SET @StartDate = (
	--	SELECT MAX(NgayThucHien) 
	--	FROM ThucChayDaTinhAdmarket AS tcdt
	--	WHERE tcdt.DmSanPhamREF IN (144,299,337,585)
	--)
	
	--SET @StartDate = DATEADD(dd, 1, @StartDate);
			
	--SET @EndDate = GETDATE();
	--SET @EndDate = DATEADD(dd,-1,@EndDate);
	SET @StartDate = '2015-07-13'
	SET @EndDate = '2015-07-13'
	-- Tinh thuc chay Admarket
	--EXEC dbo.ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket @StartDate, @EndDate
	EXEC [dbo].[ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket_haidh] @StartDate, @EndDate
END





----1. xoa bang online
--DELETE FROM ThucChayAdmarketOnline
--INSERT INTO ThucChayAdmarketOnline 
--INSERT INTO ThucChayAdmarketOnline 

--SELECT 
--      [ThucChayAdmarketOnlineID]
--      ,[DmSanPhamREF]
--      ,[TenSanPham]
--      ,[TaiKhoan]
--      ,[TotalView]
--      ,[TotalClick]
--      ,[SoLuong]
--      ,[DonViTinh]
--      ,[TienThucChay]
--      ,[TienKhuyenMai]
--      ,[NgayThucHien]
--      ,[IsNoiBo]
--      ,[GhiChu]
--      ,[RecordStatus]
--      ,[CreatedAt]
--      ,[CreatedBy]
--      ,[LastModifiedAt]
--      ,[LastModifiedBy]
--      ,[DmViTriREF]
--      ,[TenViTri]
--  FROM [ABM_Data_Release].[dbo].[ThucChayAdmarketOnlineHistory]
--WHERE DayHistory = '2015-05-15'
--GO
----2. xoa tcdt admarket
--DELETE FROM ThucChayDaTinhAdmarket WHERE NgayThucHien >= '2015-05-14'
----3.tinh
--EXEC dbo.ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket '2015-05-14',  '2015-05-14'
--EXEC dbo.ThucChayDaTinh_ExcInsertThucChayDaTinhAdmarket '2015-05-15',  '2015-05-15'




```
