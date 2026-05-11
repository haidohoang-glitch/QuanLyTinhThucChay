# Stored Procedure: `prc_asd_calc_admarket_bk20220301`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-03-01 15:04:39.800000
- **Ngày sửa cuối**: 2022-03-01 15:04:39.800000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv	
-- Create date: 20170909
-- Description:	<Description,,>
-- =============================================
create PROCEDURE [dbo].[prc_asd_calc_admarket_bk20220301]
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	declare @ngaythuchien datetime = convert(date,dateadd(dd,-1,getdate()));
	DECLARE @NgayHienTai DATETIME = CONVERT(DATE,DATEADD(dd,1,@ngayThucHien))
	-- tinh san pham view plus
	--print '[prc_asd_tinhthucchay_admarket_viewplus]'
	exec [dbo].[prc_asd_tinhthucchay_admarket_viewplus] @ngaythuchien;

	--VAT 8%----------
	--exec [dbo].[prc_asd_tinhthucchay_admarket_viewplus_VAT8] @ngaythuchien

	-- tinh san pham adx cpc
	--print '[prc_asd_tinhthucchay_admarket_adx_cpc]'
	exec [dbo].[prc_asd_tinhthucchay_admarket_adx_cpc] @ngaythuchien;

	--VAT 8%-----
	--exec [prc_asd_tinhthucchay_admarket_adx_cpc_VAT8] @ngaythuchien;

	-- insert theo chieu domain
	--print '[prc_insert_thucchaydatinh_bythucchaydatinh_admarket]'
	exec [dbo].[prc_insert_thucchaydatinh_bythucchaydatinh_admarket] @ngaythuchien;

	--VAT 8%
	--EXEC [prc_insert_thucchaydatinh_bythucchaydatinh_admarket_VAT8] @ngaythuchien;

	-- huy hop dong
	print 'prc_asd_insert_thucchaydatinh_admarket_hopdonghuy'
	exec [dbo].[prc_asd_insert_thucchaydatinh_admarket_hopdonghuy] @ngaythuchien; 

	-- làm lại dl bảng online
	print '[prc_asd_Admarket_TinhGiaTri_Online]'
	exec [dbo].[prc_asd_Admarket_TinhGiaTri_Online] @ngaythuchien; 

	--VAT 8%
	--EXEC [prc_asd_Admarket_TinhGiaTri_Online_VAT8] @ngaythuchien;

	-- thay doi gia tri hop dong
	print '[prc_asd_TinhThucChay_Admarket_ThayDoiGiaTri_HopDong]'
	exec [dbo].[prc_asd_TinhThucChay_Admarket_ThayDoiGiaTri_HopDong] @ngaythuchien;


	-- can chieu domain va hop dong
	exec [dbo].[ThucChayDaTinhAdmarket_InsertThucChayNoContract] @ngaythuchien;

	--haidh comment thuc hien ghi nhan thuc chay theo hopdong
	exec [dbo].[prc_asd_TinhThucChay_Admarket_With_HopDong]	@NgayThucHien = @ngaythuchien

	--XL DU LIEU NGAY 01 HANG THANG
	IF(DAY(GETDATE()) = 1)
	BEGIN
	    EXEC [dbo].[prc_asd_TinhThucChay_Admarket_With_HopDong_NgayDauThang]
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
