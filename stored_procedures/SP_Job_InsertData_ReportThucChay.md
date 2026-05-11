# Stored Procedure: `Job_InsertData_ReportThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-27 17:44:10.843000
- **Ngày sửa cuối**: 2015-04-02 14:23:46.427000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [Job_InsertData_ReportThucChay]
CREATE  PROCEDURE [dbo].[Job_InsertData_ReportThucChay] 
AS
BEGIN
	DECLARE @FromDate DATETIME, @ToDate DATETIME
	SET @ToDate = 
	(
		SELECT MAX(tcdt.NgayThucHien) FROM ThucChayDaTinh tcdt
	)
	SET @FromDate =
	(
		SELECT MAX(dstchdc.NgayThucHien)
		FROM DoanhSoThucChayHopDongCore dstchdc
		--SELECT MAX(dstchdc.NgayThucHien)
		--FROM DoanhSoThucChayWebsiteCore dstchdc
	)
	IF(@FromDate IS NOT NULL)
	BEGIN
		SET @FromDate = DATEADD(DAY,1,@FromDate)
	END
	SET @FromDate = ISNULL(@FromDate,'2013-01-01')
	SET @FromDate = '2015-03-26'
	SET @ToDate = '2015-03-26'
	IF(@FromDate <=@ToDate)
	BEGIN
		--PRINT 'Insert data into ReportThucChay'
		EXEC Insert_ThucChayDaTinhTheoThoiGian @FromDate, @ToDate
		EXEC Insert_ThucChayDaTinhAdmarketTheoThoiGian @FromDate, @ToDate
		EXEC Insert_DoanhSoThucChayHopDongCore @FromDate, @ToDate
        EXEC Insert_DoanhSoThucChayWebsiteCore @FromDate, @ToDate
        EXEC Insert_DoanhSoThucChayWebsiteTheoThoiGian @FromDate, @ToDate
		EXEC Insert_DoanhSoThucChayhopDongTheoThoiGian @FromDate, @ToDate
		
		--**********Chay du lieu thuc chay theo all time********------
		--EXEC Insert_DoanhSoThucChayHopDongCore_All @FromDate, @ToDate
  --      EXEC Insert_DoanhSoThucChayWebsiteCore @FromDate, @ToDate
		--**********END Chay du lieu thuc chay theo all time********------
		
		EXEC Insert_rptThucChay_ChuyenMuc_All @FromDate, @ToDate
		EXEC Insert_rptThucChay_DoiBan_All @FromDate, @ToDate
		EXEC Insert_rptThucChay_Website_All @FromDate, @ToDate
		
		EXEC Insert_rptThucChay_HinhThucQuangCao_All @FromDate, @ToDate
		EXEC Insert_rptThucChay_HinhThucQuangCao_TheoSanPham_All @FromDate, @ToDate
		EXEC Insert_rptThucChay_HinhThucQuangCao_TheoSanPham_ViTriBanner_All @FromDate, @ToDate
		EXEC Insert_rptThucChay_HinhThucQuangCao_TheoSanPham_Website_All @FromDate, @ToDate
		
		EXEC Insert_rptThucChay_HopDong_All @FromDate, @ToDate
		EXEC Insert_rptThucChay_HopDong_TheoSanPham_All @FromDate, @ToDate
		EXEC Insert_rptThucChay_HopDong_TheoSanPham_ViTriBanner_All @FromDate, @ToDate
		EXEC Insert_rptThucChay_HopDong_TheoSanPham_Website_All @FromDate, @ToDate
		EXEC Insert_rptThucChay_HopDong_TheoHinhThucQuangCao_All @FromDate, @ToDate
		EXEC Insert_rptThucChay_HopDong_TheoViTriBanner_All @FromDate, @ToDate
		EXEC Insert_rptThucChay_HopDong_TheoWebsite_All @FromDate, @ToDate
		
		EXEC Insert_rptThucChay_KhachHang_All @FromDate, @ToDate
		EXEC Insert_rptThucChay_KhachHang_TheoSanPham_All @FromDate, @ToDate
		EXEC Insert_rptThucChay_KhachHang_TheoHinhThucQuangCao_All @FromDate, @ToDate
		EXEC Insert_rptThucChay_KhachHang_TheoWebsite_All @FromDate, @ToDate
		
		EXEC Insert_rptThucChay_NhanVien_All @FromDate, @ToDate
	
	
	    EXEC Insert_rptThucChay_SanPham_All @FromDate, @ToDate
		EXEC Insert_rptThucChay_SanPham_TheoWebsite_All @FromDate, @ToDate
		EXEC Insert_rptThucChay_SanPham_TheoTenViTriBanner_All @FromDate, @ToDate
		EXEC Insert_rptThucChay_SanPham_TheoWebsite_ViTriBanner_All @FromDate, @ToDate
		EXEC Insert_rptThucChay_TenViTriBanner_All @FromDate, @ToDate
		
		EXEC Insert_rptThucChay_BaoCaoTongHopTheoHopDong_All @FromDate, @ToDate
		EXEC Insert_rptThucChay_BaoCaoTongHopTheoWebsite_All @FromDate, @ToDate
	END
	
END



```
