# Stored Procedure: `prc_asd_calc_admarket_UpdateValue_With_HopDong_NgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-07-29 16:12:13.030000
- **Ngày sửa cuối**: 2024-07-29 16:12:13.030000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ngaythuchien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv	
-- Create date: 20170909
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[prc_asd_calc_admarket_UpdateValue_With_HopDong_NgayThucHien] @ngaythuchien datetime
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	----declare @ngaythuchien datetime = convert(date,dateadd(dd,-1,getdate()));
	DECLARE @NgayHienTai DATETIME = CONVERT(DATE,DATEADD(dd,1,@ngayThucHien))

	--haidh comment thuc hien ghi nhan thuc chay theo hopdong
	--exec [dbo].[prc_asd_TinhThucChay_Admarket_With_HopDong]	@NgayThucHien = @ngaythuchien
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
	print '[prc_asd_UpdateTrangThai_ThucChay_PerformanceBase_ThayDoi_With_HopDong]'
	exec [dbo].[prc_asd_UpdateTrangThai_ThucChay_PerformanceBase_ThayDoi_With_HopDong] @ngaythuchien

	--haidh comment tao ban ghi cho job quet thong bao admarket
	IF(NOT EXISTS(SELECT TOP (1) ToDate FROM ADX_Job_UpdateStatusThayDoiThucChay WHERE ToDate = @ngaythuchien ORDER BY ToDate))
	BEGIN
		insert 	into  ADX_Job_UpdateStatusThayDoiThucChay (Status, FromDate, ToDate, IsDeleted, RequestKeyError)
		select 1, @ngaythuchien,@ngaythuchien,0,''
	END
END 



```
