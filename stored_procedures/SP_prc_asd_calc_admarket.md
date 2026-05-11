# Stored Procedure: `prc_asd_calc_admarket`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-11 15:02:51.053000
- **Ngày sửa cuối**: 2023-07-03 10:27:50.850000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv	
-- Create date: 20170909
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[prc_asd_calc_admarket]
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	declare @ngaythuchien datetime = convert(date,dateadd(dd,-1,getdate()));
	DECLARE @NgayHienTai DATETIME = CONVERT(DATE,DATEADD(dd,1,@ngayThucHien))

	----***************VAT 10% *******************------------------
	---- 1.tinh san pham view plus
	----print '[prc_asd_tinhthucchay_admarket_viewplus]'
	--exec [dbo].[prc_asd_tinhthucchay_admarket_viewplus] @ngaythuchien;

	---- 2.tinh san pham adx cpc
	----print '[prc_asd_tinhthucchay_admarket_adx_cpc]'
	--exec [dbo].[prc_asd_tinhthucchay_admarket_adx_cpc] @ngaythuchien;

	---- 3.insert theo chieu domain
	----print '[prc_insert_thucchaydatinh_bythucchaydatinh_admarket]'
	--exec [dbo].[prc_insert_thucchaydatinh_bythucchaydatinh_admarket] @ngaythuchien;

	---- 4.huy hop dong
	--print 'prc_asd_insert_thucchaydatinh_admarket_hopdonghuy'
	--exec [dbo].[prc_asd_insert_thucchaydatinh_admarket_hopdonghuy] @ngaythuchien; 

	---- 5.làm lại dl bảng online
	--print '[prc_asd_Admarket_TinhGiaTri_Online]'
	--exec [dbo].[prc_asd_Admarket_TinhGiaTri_Online] @ngaythuchien; 

	---- 6.thay doi gia tri hop dong
	--print '[prc_asd_TinhThucChay_Admarket_ThayDoiGiaTri_HopDong]'
	--exec [dbo].[prc_asd_TinhThucChay_Admarket_ThayDoiGiaTri_HopDong] @ngaythuchien;

	---- 7.can chieu domain va hop dong
	--exec [dbo].[ThucChayDaTinhAdmarket_InsertThucChayNoContract] @ngaythuchien;

	----**********END VAT 10% ***********-----------------------------

	--HAIDH COMMENT 20220301 bat dau va ket thuc vao 20221231
	----***********VAT 8% ***************------------------------------
	IF(@ngaythuchien >=  '2022-03-01' AND @ngaythuchien <= '2022-12-31' )
	BEGIN
		
		-- 1.tinh san pham view plus
		---VAT 8%----------
		exec [dbo].[prc_asd_tinhthucchay_admarket_viewplus_VAT8] @ngaythuchien

		-- 2.tinh san pham adx cpc
		---VAT 8%-----
		exec [prc_asd_tinhthucchay_admarket_adx_cpc_VAT8] @ngaythuchien;

		-- 3.insert theo chieu domain
		--VAT 8%
		EXEC [prc_insert_thucchaydatinh_bythucchaydatinh_admarket_VAT8] @ngaythuchien;

		-- 4.huy hop dong
		print 'prc_asd_insert_thucchaydatinh_admarket_hopdonghuy'
		exec [dbo].[prc_asd_insert_thucchaydatinh_admarket_hopdonghuy] @ngaythuchien; 

		-- 5.làm lại dl bảng online
		---VAT 8%
		EXEC [prc_asd_Admarket_TinhGiaTri_Online_VAT8] @ngaythuchien;

		-- 6.thay doi gia tri hop dong
		print '[prc_asd_TinhThucChay_Admarket_ThayDoiGiaTri_HopDong]'
		exec [dbo].[prc_asd_TinhThucChay_Admarket_ThayDoiGiaTri_HopDong] @ngaythuchien;

		-- 7.can chieu domain va hop dong
		exec [dbo].[ThucChayDaTinhAdmarket_InsertThucChayNoContract] @ngaythuchien;

		-----END VAT 8%---------------------------------
	END
	---20230703 HAIDH COMMENT THAY DOI TINH THEO VAT8%
	ELSE
	BEGIN
		----***********VAT 8% ***************------------------------------
		IF(@ngaythuchien >=  '2023-07-01' )
		BEGIN
		
			-- 1.tinh san pham view plus
			---VAT 8%----------
			exec [dbo].[prc_asd_tinhthucchay_admarket_viewplus_VAT8] @ngaythuchien

			-- 2.tinh san pham adx cpc
			---VAT 8%-----
			exec [prc_asd_tinhthucchay_admarket_adx_cpc_VAT8] @ngaythuchien;

			-- 3.insert theo chieu domain
			--VAT 8%
			EXEC [prc_insert_thucchaydatinh_bythucchaydatinh_admarket_VAT8] @ngaythuchien;

			-- 4.huy hop dong
			print 'prc_asd_insert_thucchaydatinh_admarket_hopdonghuy'
			exec [dbo].[prc_asd_insert_thucchaydatinh_admarket_hopdonghuy] @ngaythuchien; 

			-- 5.làm lại dl bảng online
			---VAT 8%
			EXEC [prc_asd_Admarket_TinhGiaTri_Online_VAT8] @ngaythuchien;

			-- 6.thay doi gia tri hop dong
			print '[prc_asd_TinhThucChay_Admarket_ThayDoiGiaTri_HopDong]'
			exec [dbo].[prc_asd_TinhThucChay_Admarket_ThayDoiGiaTri_HopDong] @ngaythuchien;

			-- 7.can chieu domain va hop dong
			exec [dbo].[ThucChayDaTinhAdmarket_InsertThucChayNoContract] @ngaythuchien;

			-----END VAT 8%---------------------------------
		END
		ELSE
		BEGIN
			-------*******************VAT10******************--------------
			-- 1.tinh san pham view plus
			exec [dbo].[prc_asd_tinhthucchay_admarket_viewplus_VAT10] @ngaythuchien

			-- 2.tinh san pham adx cpc

			exec [prc_asd_tinhthucchay_admarket_adx_cpc_VAT10] @ngaythuchien;

			-- 3.insert theo chieu domain

			EXEC [prc_insert_thucchaydatinh_bythucchaydatinh_admarket_VAT10] @ngaythuchien;

			-- 4.huy hop dong
			print 'prc_asd_insert_thucchaydatinh_admarket_hopdonghuy'
			exec [dbo].[prc_asd_insert_thucchaydatinh_admarket_hopdonghuy] @ngaythuchien; 

			-- 5.làm lại dl bảng online

			EXEC [prc_asd_Admarket_TinhGiaTri_Online_VAT10] @ngaythuchien;

			-- 6.thay doi gia tri hop dong
			print '[prc_asd_TinhThucChay_Admarket_ThayDoiGiaTri_HopDong]'
			exec [dbo].[prc_asd_TinhThucChay_Admarket_ThayDoiGiaTri_HopDong] @ngaythuchien;

			-- 7.can chieu domain va hop dong
			exec [dbo].[ThucChayDaTinhAdmarket_InsertThucChayNoContract] @ngaythuchien;
			-------END VAT10
		END
		
	END

	--20221230 HAIDH COMMENT CHUYEN VIEC TINH GIA TRI THUC CHAY DIEU CHINH SANG JOB Job_PerformanceBase_DieuChinhGiaTri VA NO CHAY VAO LUC 12H10
	----haidh comment thuc hien ghi nhan thuc chay theo hopdong
	----exec [dbo].[prc_asd_TinhThucChay_Admarket_With_HopDong]	@NgayThucHien = @ngaythuchien
	--exec [dbo].[prc_asd_TinhThucChay_Admarket_With_HopDong_ThangDuGP]	@NgayThucHien = @ngaythuchien

	----XL DU LIEU NGAY 01 HANG THANG
	--IF(DAY(GETDATE()) = 1)
	--BEGIN
	--    --EXEC [dbo].[prc_asd_TinhThucChay_Admarket_With_HopDong_NgayDauThang]
	--	--@NgayThucHien = @NgayHienTai,
	--	--@NgayGhiNhanThucChay = @ngayThucHien

	--	 EXEC [dbo].prc_asd_TinhThucChay_Admarket_With_HopDong_NgayDauThang_ThangDuGP
	--	@NgayThucHien = @NgayHienTai,
	--	@NgayGhiNhanThucChay = @ngayThucHien

	--END
	----haidh comment thuc hien day trang thai de gui cho ben admarket biet 
	--print '[prc_asd_UpdateTrangThai_ThucChay_PerformanceBase_ThayDoi_With_HopDong]'
	--exec [dbo].[prc_asd_UpdateTrangThai_ThucChay_PerformanceBase_ThayDoi_With_HopDong] @ngaythuchien

	----haidh comment tao ban ghi cho job quet thong bao admarket
	--IF(NOT EXISTS(SELECT TOP (1) ToDate FROM ADX_Job_UpdateStatusThayDoiThucChay WHERE ToDate = @ngaythuchien ORDER BY ToDate))
	--BEGIN
	--	insert 	into  ADX_Job_UpdateStatusThayDoiThucChay (Status, FromDate, ToDate, IsDeleted, RequestKeyError)
	--	select 1, @ngaythuchien,@ngaythuchien,0,''
	--END
END 



```
