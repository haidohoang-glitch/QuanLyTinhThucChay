# Stored Procedure: `ThucChay_TinhCPM_BySQLJobs_NgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-29 15:02:34.450000
- **Ngày sửa cuối**: 2023-01-09 09:56:06.520000

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
-- =============================================
--
/*
Exec [dbo].[ThucChay_TinhCPM_BySQLJobs_NgayThucHien]
	@NgayThucHien = '2023-01-07'
*/

CREATE PROCEDURE [dbo].[ThucChay_TinhCPM_BySQLJobs_NgayThucHien]
	@NgayThucHien Datetime
	-- Add the parameters for the stored procedure here

AS
BEGIN
	DECLARE @dtStart DATETIME, @dtEnd DATETIME


	
	SET @dtStart = CONVERT(DATE,@NgayThucHien)
	SET @dtEnd = CONVERT(DATE,@NgayThucHien)
	

	
	
	-----dat chay de fix loi ngay 06/06/2022
	--SET @dtStart = '2022-06-01'
	--SET @dtEnd =   '2022-06-05'

	--INSERT INTO [dbo].[Log_MaxNgayThucHien]
	--				([MaxNgayThucHien]
	--				,[NhomSanPham]
	--				,[LogTime]
	--				,Next_MaxNgayThucHien )
	--			VALUES
	--				(@dtStart
	--				,1
	--				,GETDATE()
	--				,@dtEnd
	--				)
	
	--Tinh Thuc Chay CPM
	--PRINT '[dbo].[ThucChay_HopDongChiTietAndBanner]'
	EXEC [dbo].[ThucChay_HopDongChiTietAndBanner] @dtEnd

	--PRINT '[ThucChay_UpdateHopDongChiTietAndBanner]'
	EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner] 

	PRINT '[ThucChay_ExcInsertThucChayDaTinh]'
	EXEC [ThucChay_ExcInsertThucChayDaTinh] @dtStart,@dtEnd

	PRINT '[ThucChay_ExcInsertThucChayDaTinhCPV]'
	EXEC [dbo].[ThucChay_ExcInsertThucChayDaTinhCPV] @dtStart,@dtEnd 
	
	--Tinh gia tri thay doi CPM
	--EXEC [ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPM] @dtStart,@dtEnd
	EXEC [sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_CPM] @dtStart,@dtEnd, NULL
	
	--Tinh gia tri thuc chay CPR voi don vi la Goi
	EXEC [ThucChay_ExcInsertThucChayDaTinh_CPR] @dtStart,@dtEnd
	
	--Tinh gia tri thu chay voi don vi la CPR
	EXEC [ThucChay_ExcInsertThucChayDaTinh_CPR_ByDVT_CPR] @dtStart,@dtEnd
	
	-- Tinh cho don vi la True View
	EXEC ThucChay_ExcInsertThucChayDaTinhTrueView @dtStart,@dtEnd

	-- Check va tinh gia tri thay doi cua TRUE VIEW va TRUE REACH
	EXEC [dbo].[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_TRUEVIEW] 
		@StartDate = @dtStart ,
		@EndDate = @dtEnd
	--Tinh thuc chay cho san pham Native Ads, On Image , Nhieu san pham (DonViGoi)
	EXEC [dbo].[ThucChay_ExcInsertThucChayDaTinh_CPM_Native_Ads] 
	@StartDate = @dtStart,
	@EndDate = @dtEnd

	--Check va tinh gia tri thay doi cua Native Ads
	EXEC [dbo].[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_Native_Ads] 
    @StartDate = @dtStart ,
    @EndDate = @dtEnd

	--print 'DONVIBAI'
	----**BEGIN DONVIBAI**---
	--THUC CHAY CHO CHO CPM DonViBai 2021-03-05 haidh, NGAYDANHSOGIOIHAN < '2021-06-10'
	EXEC [dbo].[ThucChay_ExcInsertThucChayDaTinh_DonViBai] 
	@StartDate = @dtStart,
	@EndDate = @dtEnd

	--print 'UPDATE GIA TRI THAY DOI DONVIBAI'
	--UPDATE GIA TRI THAY DOI
	EXEC [dbo].[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_DonViBai] 
    @StartDate = @dtStart ,
    @EndDate = @dtEnd

	----THUC CHAY CHO CHO CPM DonViBai 2021-06-07 haidh, NGAYDANHSOGIOIHAN >= '2021-06-10'
	--print 'Tinh GIA TRI THAY DOI DONVIBAI treo'
	EXEC [dbo].[ThucChay_ExcInsertThucChayDaTinh_DonViBai_ThucTreo] 
	@StartDate = @dtStart,
	@EndDate = @dtEnd

	--print 'Update GIA TRI THAY DOI DONVIBAI treo'
	--UPDATE GIA TRI THAY DOI
	EXEC [dbo].[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_DonViBai_ThucTreo] 
    @StartDate = @dtStart ,
    @EndDate = @dtEnd

	----**END DONVIBAI**---

	--print 'DONVIGOI'
	----**BEGIN DONVIGOI**----
	--TINH THUC CHAY DONVIGOI HAIDH 20220628 THEM VIEC TINH NHIEU SAN PHAM (KHONG BAO GOM NATIVE ADS, ONIMAGE)
	EXEC [dbo].[ThucChay_ExcInsertThucChayDaTinh_DonViGoi_V2] 
	@StartDate = @dtStart,
	@EndDate = @dtEnd
	--TINH THUC CHAY DONVIGOI HAIDH 20210601
	--EXEC [dbo].[ThucChay_ExcInsertThucChayDaTinh_DonViGoi] 
	--@StartDate = @dtStart,
	--@EndDate = @dtEnd


	--UPDATE GIA TRI THAY DOI DONVIGOI HAIDH 20220628 THEM VIEC TINH NHIEU SAN PHAM (BAO GOM CA NATIVE ADS, ONIMAGE)
	EXEC [dbo].[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_DonViGoi_v2] 
	-- Add the parameters for the stored procedure here
    @StartDate = @dtStart ,
    @EndDate = @dtEnd
	--UPDATE GIA TRI THAY DOI DONVIGOI HAIDH 20210601
	--EXEC [dbo].[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_DonViGoi] 
	---- Add the parameters for the stored procedure here
 --   @StartDate = @dtStart ,
 --   @EndDate = @dtEnd
	----**END DONVIGOI**----

END

--EXEC [dbo].[ThucChay_TinhCPM_BySQLJobs]

```
