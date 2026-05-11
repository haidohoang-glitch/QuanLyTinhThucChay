# Stored Procedure: `prc_asd_calc_admarket_UpdateValue_With_HopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-12-30 09:50:59.747000
- **Ngày sửa cuối**: 2025-07-10 14:49:48.333000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv	
-- Create date: 20170909
-- Description:	<Description,,>
-- =============================================
/*
EXEC [dbo].[prc_asd_calc_admarket_UpdateValue_With_HopDong]
*/
CREATE PROCEDURE [dbo].[prc_asd_calc_admarket_UpdateValue_With_HopDong]
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	declare @ngaythuchien datetime = convert(date,dateadd(dd,-1,getdate()));
	DECLARE @NgayHienTai DATETIME = CONVERT(DATE,DATEADD(dd,1,@ngayThucHien))

	--haidh comment thuc hien ghi nhan thuc chay theo hopdong
	--exec [dbo].[prc_asd_TinhThucChay_Admarket_With_HopDong]	@NgayThucHien = @ngaythuchien
	--1. thuc hien xl xoa du lieu MKT-FEE truoc khi tinh thuc chay trong ngay
	exec [dbo].[prc_asd_DeletedThucChay_Admarket_With_HopDong_MKT_FEE]	@NgayThucHien = @ngaythuchien

	--2. thuc hien tinh theo request
	exec [dbo].[prc_asd_TinhThucChay_Admarket_With_HopDong_ThangDuGP]	@NgayThucHien = @ngaythuchien

	--XL DU LIEU NGAY 01 HANG THANG
	IF(DAY(GETDATE()) = 1)
	BEGIN
	    --EXEC [dbo].[prc_asd_TinhThucChay_Admarket_With_HopDong_NgayDauThang]
		--@NgayThucHien = @NgayHienTai,
		--@NgayGhiNhanThucChay = @ngayThucHien

		 EXEC [dbo].prc_asd_TinhThucChay_Admarket_With_HopDong_NgayDauThang_ThangDuGP
		@NgayThucHien = @NgayHienTai,
		@NgayGhiNhanThucChay = @ngayThucHien

	END
	--haidh comment thuc hien day trang thai de gui cho ben admarket biet 
	--print '[prc_asd_UpdateTrangThai_ThucChay_PerformanceBase_ThayDoi_With_HopDong]'
	exec [dbo].[prc_asd_UpdateTrangThai_ThucChay_PerformanceBase_ThayDoi_With_HopDong] @ngaythuchien

	--haidh comment tao ban ghi cho job quet thong bao admarket
	IF(NOT EXISTS(SELECT TOP (1) ToDate FROM ADX_Job_UpdateStatusThayDoiThucChay WHERE ToDate = @ngaythuchien ORDER BY ToDate))
	BEGIN
		insert 	into  ADX_Job_UpdateStatusThayDoiThucChay (Status, FromDate, ToDate, IsDeleted, RequestKeyError)
		select 1, @ngaythuchien,@ngaythuchien,0,''
	END
END 



```
