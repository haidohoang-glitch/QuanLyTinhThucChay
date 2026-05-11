# Stored Procedure: `KiemSoat_ThucChayDaTinh_TenWebsite_NhieuHon1ID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-07-24 10:09:13.187000
- **Ngày sửa cuối**: 2023-05-05 14:38:58.897000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
EXEC [KiemSoat_ThucChayDaTinh_TenWebsite_NhieuHon1ID] 
 
*/
CREATE PROCEDURE [dbo].[KiemSoat_ThucChayDaTinh_TenWebsite_NhieuHon1ID] 
AS
BEGIN
	DECLARE @FromDate DATETIME, @ToDate DATETIME
	SET @FromDate = '2018-01-01'
	SET @ToDate = CONVERT(DATE,DATEADD(DAY,-1,GETDATE()))
--Xóa trước khi insert
DELETE FROM KS_ThucChay_TCDT_Website WHERE NgayThucHien =@ToDate
DELETE FROM KiemSoat_ThucChayDaTinh_Website WHERE ToDate =@ToDate
--Insert dữ liệu tcdt website
INSERT INTO dbo.KS_ThucChay_TCDT_Website
	SELECT DmWebsiteREF, TenWebsite, NgayThucHien,SUM(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi) 
	FROM dbo.ThucChayDaTinh WHERE DmSanPhamREF NOT IN (144,628,585) AND NgayThucHien = @ToDate
	GROUP BY DmWebsiteREF, TenWebsite, NgayThucHien
	HAVING ROUND(SUM(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi) ,0)<> 0
	ORDER BY NgayThucHien 

	INSERT INTO dbo.KiemSoat_ThucChayDaTinh_Website
	(
	    TenWebsite,
	    SoLuongSiteLech,
	    TienSiteLech,
	    FromDate,
	    ToDate,
	    createdAt
	)
	SELECT A.TenWebsite,COUNT(distinct DmWebsiteREF),SUM(ThanhTienThucChay) ,@FromDate,@ToDate, GETDATE() FROM (
	SELECT TenWebsite,DmWebsiteREF, SUM(ThanhTienThucChay)ThanhTienThucChay
	FROM KS_ThucChay_TCDT_Website 
	WHERE  1=1 AND TenWebsite <> 'Welax'
	AND NgayThucHien >=@FromDate --- --Duongnt 05-05-2023 
	GROUP BY TenWebsite,DmWebsiteREF
	HAVING ROUND(SUM(ThanhTienThucChay),0) <> 0 )
	A  
	GROUP BY A.TenWebsite
	HAVING COUNT(distinct A.DmWebsiteREF) > 1

	INSERT INTO dbo.KiemSoat_ThucChayDaTinh_Website
	(
	    TenWebsite,
	    SoLuongSiteLech,
	    TienSiteLech,
	    FromDate,
	    ToDate,
	    createdAt
	)
	SELECT A.TenWebsite,COUNT(distinct DmWebsiteREF),SUM(ThanhTienThucChay) ,@FromDate,@ToDate, GETDATE() FROM (
	SELECT TenWebsite,DmWebsiteREF, SUM(ThanhTienThucChay)ThanhTienThucChay
	FROM KS_ThucChay_TCDT_Website 
	WHERE  1=1 AND TenWebsite = 'Welax'
	AND NgayThucHien >=@FromDate --'2018-01-01' --Duongnt 05-05-2023
	GROUP BY TenWebsite,DmWebsiteREF
	HAVING ROUND(SUM(ThanhTienThucChay),0) <> 0 )
	A  
	GROUP BY A.TenWebsite
	HAVING COUNT(distinct A.DmWebsiteREF) > 1
	

/*	
--ktra max ngay thuc hien

declare @newzingvn float, @saostarvn float,@ngoisaonet FLOAT, @vtvvn FLOAT, @ngoisao FLOAT,@nhandan FLOAT, @Ellecom FLOAT,@giadinhnetvn FLOAT, @emdepvn FLOAT
,@baoxaydung FLOAT

set @newzingvn = (select SUM(ThanhTienThucChay) from KS_ThucChay_TCDT_Website 
					WHERE NgayThucHien BETWEEN @FromDate and @ToDate and 
					TenWebsite ='news.zing.vn' and DmWebsiteREF <>79455 and NgayThucHien <= '2018-09-27')

set @saostarvn = (select SUM(ThanhTienThucChay) from KS_ThucChay_TCDT_Website 
					WHERE NgayThucHien BETWEEN @FromDate and @ToDate and 
					TenWebsite ='saostar.vn' and DmWebsiteREF <>73815 and NgayThucHien <= '2018-09-18')

set @ngoisaonet = (select SUM(ThanhTienThucChay) from KS_ThucChay_TCDT_Website 
					WHERE NgayThucHien BETWEEN @FromDate and @ToDate and 
					TenWebsite ='ngoisao.net' and DmWebsiteREF <>1153 and NgayThucHien <= '2018-09-18')
set @vtvvn = (select SUM(ThanhTienThucChay) from KS_ThucChay_TCDT_Website 
					WHERE NgayThucHien BETWEEN @FromDate and @ToDate and 
					TenWebsite ='vtv.vn' and DmWebsiteREF <>265 and NgayThucHien <= '2019-12-31')
					
set @vtvvn = (select SUM(ThanhTienThucChay) from KS_ThucChay_TCDT_Website 
					WHERE NgayThucHien BETWEEN @FromDate and @ToDate and 
					TenWebsite ='vtv.vn' and DmWebsiteREF <>265 and NgayThucHien <= '2019-12-31')
set @ngoisao = (select SUM(ThanhTienThucChay) from KS_ThucChay_TCDT_Website 
					WHERE NgayThucHien BETWEEN @FromDate and @ToDate and 
					TenWebsite ='Ngoisao' and DmWebsiteREF <>1153 and NgayThucHien <= '2019-12-31')
set @nhandan = (select SUM(ThanhTienThucChay) from KS_ThucChay_TCDT_Website 
					WHERE NgayThucHien BETWEEN @FromDate and @ToDate and 
					TenWebsite ='nhandan.com.vn' and DmWebsiteREF <>310092 and NgayThucHien <= '2019-12-31')
set @Ellecom = (select SUM(ThanhTienThucChay) from KS_ThucChay_TCDT_Website 
					WHERE NgayThucHien BETWEEN @FromDate and @ToDate and 
					TenWebsite ='Elle.com' and DmWebsiteREF <>293021 and NgayThucHien <= '2019-12-31')
set @giadinhnetvn = (select SUM(ThanhTienThucChay) from KS_ThucChay_TCDT_Website 
					WHERE NgayThucHien BETWEEN @FromDate and @ToDate and 
					TenWebsite ='giadinh.net.vn' and DmWebsiteREF <>85 and NgayThucHien <= '2019-12-31')
set @emdepvn = (select SUM(ThanhTienThucChay) from KS_ThucChay_TCDT_Website 
					WHERE NgayThucHien BETWEEN @FromDate and @ToDate and 
					TenWebsite ='emdep.vn' and DmWebsiteREF <>15348 and NgayThucHien <= '2019-12-31')
set @baoxaydung = (select SUM(ThanhTienThucChay) from KS_ThucChay_TCDT_Website 
					WHERE NgayThucHien BETWEEN @FromDate and @ToDate and 
					TenWebsite ='baoxaydung.com.vn' and DmWebsiteREF <>310084 and NgayThucHien <= '2019-12-31')
--- Loại bỏ website 					
if @newzingvn = 0 
	begin 
		delete from KiemSoat_ThucChayDaTinh_Website where TenWebsite = 'news.zing.vn' and ToDate = @ToDate
	end
if @saostarvn = 0 
	begin
		delete from KiemSoat_ThucChayDaTinh_Website where TenWebsite = 'saostar.vn' and ToDate = @ToDate
	end
if @ngoisaonet = 0 
	begin
		delete from KiemSoat_ThucChayDaTinh_Website where TenWebsite = 'ngoisao.net' and ToDate = @ToDate
	END
if @vtvvn = 0 
	begin
		delete from KiemSoat_ThucChayDaTinh_Website where TenWebsite = 'vtv.vn' and ToDate = @ToDate
	end    

if @vtvvn = 0 
	begin
		delete from KiemSoat_ThucChayDaTinh_Website where TenWebsite = 'vtv.vn' and ToDate = @ToDate
	end  

if @ngoisao = 0 
	begin
		delete from KiemSoat_ThucChayDaTinh_Website where TenWebsite = 'Ngoisao' and ToDate = @ToDate
	end  
if @nhandan = 0 
	begin
		delete from KiemSoat_ThucChayDaTinh_Website where TenWebsite = 'nhandan.com.vn' and ToDate = @ToDate
	end  

if @Ellecom = 0 
	begin
		delete from KiemSoat_ThucChayDaTinh_Website where TenWebsite = 'Elle.com' and ToDate = @ToDate
	end  
if @giadinhnetvn = 0 
	begin
		delete from KiemSoat_ThucChayDaTinh_Website where TenWebsite = 'giadinh.net.vn' and ToDate = @ToDate
	end  
if @emdepvn = 0 
	begin
		delete from KiemSoat_ThucChayDaTinh_Website where TenWebsite = 'emdep.vn' and ToDate = @ToDate
	end  
if @baoxaydung = 0 
	begin
		delete from KiemSoat_ThucChayDaTinh_Website where TenWebsite = 'baoxaydung.com.vn' and ToDate = @ToDate
	end  
	*/
SELECT * FROM dbo.KiemSoat_ThucChayDaTinh_Website WHERE ToDate =@ToDate
--delete from KiemSoat_ThucChayDaTinh_Website
END
--SELECT * FROM dbo.KiemSoat_ThucChayDaTinh_Website WHERE ToDate ='2021-05-31'

```
