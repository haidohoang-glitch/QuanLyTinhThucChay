# Stored Procedure: `ThucChay_TinhMobile_BySQLJobs_ByNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2023-01-09 09:47:04.127000
- **Ngày sửa cuối**: 2023-01-09 10:03:53.280000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
 --=============================================	
/* EXEC [dbo].[ThucChay_TinhMobile_BySQLJobs_ByNgayThucHien]
	@NgayThucHien = '2023-01-07'
*/
--
CREATE PROCEDURE [dbo].[ThucChay_TinhMobile_BySQLJobs_ByNgayThucHien]
	@NgayThucHien Datetime
	-- Add the parameters for the stored procedure here

AS
BEGIN
	DECLARE @StartDate DATETIME, @EndDate DATETIME


	
	SET @StartDate = CONVERT(DATE,@NgayThucHien)
	SET @EndDate = CONVERT(DATE,@NgayThucHien)

	-----dat chay de fix loi ngay 06/06/2022
	--SET @StartDate = '2022-06-01'
	--SET @EndDate =   '2022-06-05'

	---- Tinh thuc chay Mobile  --
	--SET @StartDate = '2018-12-06'
	--SET @EndDate =   '2018-12-06'
	--EXEC dbo.ThucChay_ExcInsertThucChayDaTinhMobile_v4 @StartDate, @EndDate
	
	------ Update Gia tri thay doi thuc chay Mobile
	--EXEC dbo.ThucChayDaTinh_Mobile_UpdateGiaTriThayDoi_v2 @StartDate, @EndDate
	
	------Cap Nhat Thong tin nhan hang loi
	----EXEC ThucChay_UpdateThongTinNhanHangThucChayDaTinh @EndDate

	EXEC sp_TC_ExcInsertThucChayDaTinh_Mobile @StartDate, @EndDate, NULL
	
		
END


```
