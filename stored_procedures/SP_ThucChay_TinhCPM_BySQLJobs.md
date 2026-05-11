# Stored Procedure: `ThucChay_TinhCPM_BySQLJobs`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-02 13:20:38.843000
- **Ngày sửa cuối**: 2024-11-28 09:31:14.090000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--


CREATE PROCEDURE [dbo].[ThucChay_TinhCPM_BySQLJobs]
	-- Add the parameters for the stored procedure here

AS
BEGIN
	DECLARE @dtStart DATETIME, @dtEnd DATETIME

	--INSERT INTO dbo.Log_SP_Call
	--(
	--    SP_NAME,
	--    SP_TIME_CALL,
	--    SP_END_TIME_CALL,
	--    NOTE,
	--    VALUE_INPUT
	--)
	--VALUES
	--(   N'[ThucChay_TinhCPM_BySQLJobs]',       -- SP_NAME - nvarchar(500)
	--    GETDATE(), -- SP_TIME_CALL - datetime
	--    NULL, -- SP_END_TIME_CALL - datetime
	--    N'',       -- NOTE - nvarchar(500)
	--    N''        -- VALUE_INPUT - nvarchar(2000)
	--)

	SET @dtStart = (
					SELECT TOP (1) tcdt.NgayThucHien
					--MAX(tcdt.NgayThucHien) 
					FROM dbo.ThucChayDaTinh tcdt
					LEFT JOIN (SELECT * FROM dbo.HopDongChiTiet hdct
						WHERE hdct.DeletedStatus = 0
						AND ISNULL(hdct.DmLoaiNenTangREF,0) <> 8
						AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 2 --Nhom Tinh Branding
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
							))
						AND not (hdct.DmLoaiREF IN(13,42) OR hdct.DmLoaiBannerREF IN (17,18))
                        
					) hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
						WHERE 1=1
						AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = tcdt.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 2 --Nhom Tinh Branding
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
							))
						AND not (tcdt.DmHinhThucQuangCao IN(13,42) OR tcdt.DmLoaiBannerREF IN (17,18))
						AND NOT (tcdt.DmHinhThucQuangCao IN (26,5010,5000) AND (tcdt.DmChienDichREF = 3)) --Haidh comment 23/09/2022 Loai ThangduGP cua ben Performance Base
						AND tcdt.DotChayHopDong <> N'NGAY'
						ORDER BY tcdt.NgayThucHien desc
	)	

	
	SET @dtStart = DATEADD(dd,1, @dtStart)
	SET @dtStart = CONVERT(DATE, @dtStart)
	SET @dtEnd = CONVERT(DATE,GETDATE())
	SET @dtEnd = DATEADD(dd,-1, @dtEnd)
	
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
	
	-------------------DONG TAM THOI *****************----------------

	--Tinh Thuc Chay CPM
	--PRINT '[dbo].[ThucChay_HopDongChiTietAndBanner]'
	EXEC [dbo].[ThucChay_HopDongChiTietAndBanner] @dtEnd

	--PRINT '[ThucChay_UpdateHopDongChiTietAndBanner]'
	EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner] 

	-------------------DONG TAM THOI *****************----------------

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
