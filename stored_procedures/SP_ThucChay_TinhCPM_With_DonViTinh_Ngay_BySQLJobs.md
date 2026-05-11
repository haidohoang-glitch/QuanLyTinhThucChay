# Stored Procedure: `ThucChay_TinhCPM_With_DonViTinh_Ngay_BySQLJobs`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-02-12 11:51:25.480000
- **Ngày sửa cuối**: 2022-06-06 14:07:33.903000

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


CREATE PROCEDURE [dbo].[ThucChay_TinhCPM_With_DonViTinh_Ngay_BySQLJobs]
	-- Add the parameters for the stored procedure here

AS
BEGIN
	DECLARE @dtStart DATETIME, @dtEnd DATETIME
	
	--HAIDH COMMENT CHI TINH CHO NGAY @dtEnd 20210310 DE TUYET KO BI MISS THONG TIN 
	--SET @dtStart = ISNULL(
	--				(
	--				SELECT MAX(tcdt.NgayThucHien) FROM dbo.ThucChayDaTinh tcdt
	--				LEFT JOIN 
	--				(
	--					SELECT * FROM dbo.HopDongChiTiet hdct WHERE hdct.DeletedStatus = 0
	--					AND ISNULL(hdct.DmLoaiNenTangREF,0) <> 8
	--					AND hdct.DmSanPhamREF IN (231,238,339,240,598,613,370,680,735,342,821) 
	--				) hdct ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
	--				WHERE tcdt.DmSanPhamREF IN (231,238,339,240,598,613,370,680,735,342,821) 
	--				AND not (tcdt.DmHinhThucQuangCao IN(13,42) OR tcdt.DmLoaiBannerREF IN (17,18))
	--				AND tcdt.NgayThucHien >= '2017-12-31'
	--				AND tcdt.DotChayHopDong = N'NGAY' --HAIDH COMMENT Day la thong tin the hien tinh thuc chay san pham CPM theo ngay
	--			),GETDATE())

	SET @dtStart = DATEADD(dd,1, @dtStart)

	SET @dtEnd = Convert(date,GETDATE())
	SET @dtEnd = DATEADD(dd,-1, @dtEnd)

	-----dat chay de fix loi ngay 06/06/2022
	--SET @dtStart = '2022-06-01'
	--SET @dtEnd =   '2022-06-05'
		
	--THUC HIEN TACH THONG TIN THUC TREO
	PRINT 'Start create banner'
	EXEC [dbo].[ThucChay_HopDongChiTietAndBanner] @DenNgay = @dtEnd
	EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBannerCPM_With_DonViTinh_Ngay]

	--HAIDH COMMENT CHI TINH CHO NGAY @dtEnd 20210310 DE TUYET KO BI MISS THONG TIN 

	PRINT 'Start tinh thuc chay'
	--TINH THUC CHAY CHO CAC SAN PHAM CPM CHAY THEO SITE, TAG
	EXEC  [dbo].[ThucChay_ExcInsertThucChayDaTinhCPM_With_DonViTinh_Ngay_Site] @StartDate = @dtEnd,
																				@EndDate = @dtEnd

	
	----Tinh gia tri thay doi CPM
	----EXEC [ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_CPM] @dtStart,@dtEnd
	----TAM THOI COMMENT DE CHECK VIEC LOI GIA TRI THAY DOI
	PRINT 'Start tinh gia tri thay doi'
	EXEC [dbo].[sp_TC_UpdateGiaTriThayDoiThucChayDaTinh_CPM_With_DonViTinh_Ngay] @StartDate = @dtEnd ,
																				 @EndDate = @dtEnd
	
END

```
