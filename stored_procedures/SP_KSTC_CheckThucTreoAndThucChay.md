# Stored Procedure: `KSTC_CheckThucTreoAndThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-08 16:41:23.487000
- **Ngày sửa cuối**: 2014-12-08 16:47:59.597000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@TypeProduct` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE dbo.KSTC_CheckThucTreoAndThucChay 
	-- Add the parameters for the stored procedure here
	@StartDate DATETIME, 
	@EndDate DATETIME,
	@TypeProduct INT
AS
BEGIN
IF @TypeProduct = 10
BEGIN	
	SELECT a.SoHopDong SHDTC, a.HopDongChiTietREF HDCTThucChay, a.tc, a.tv, b.SoHopDong SHDThucTreo, 	
	b.HopDongChiTietREF HDCTThucTreo	
	  FROM (	
			SELECT dbo.ThucChay_FormatSoHopDong(tc.SoHopDong)SoHopDong, tc.HopDongChiTietREF,SUM(TongClickThucChay)tc, SUM(TongViewThucChay)tv	
			FROM ThucChay tc 
			WHERE tc.TypeProduct = 10 AND tc.NgayThucHien >= '2014-01-01' AND tc.NgayThucHien BETWEEN @StartDate AND @EndDate	
			GROUP BY dbo.ThucChay_FormatSoHopDong(tc.SoHopDong),tc.HopDongChiTietREF	
			)a	
			FULL OUTER JOIN	
			(	
			SELECT DISTINCT dbo.GetSoHopDongByID(tchdct.HopDongREF) SoHopDong, HopDongChiTietREF	
			FROM ThucChayHopDongChiTiet tchdct 
				INNER JOIN HopDongChiTiet hdct 	ON tchdct.HopDongChiTietREF = hdct.HopDongChiTietID			
			WHERE hdct.DmSanPhamREF = 342 	
			AND tchdct.DeletedStatus <> 1
			AND hdct.DeletedStatus <> 1
			AND tchdct.HopDongREF IN (SELECT HopDongID FROM HopDong hd WHERE hd.TrangThaiHopDong <> 3) 
			)b	
	ON (a.SoHopDong = b.SoHopDong	
	AND a.HopDongChiTietREF = b.HopDongChiTietREF)	
	WHERE (a.SoHopDong IS NULL OR b.SoHopDong IS NULL OR a.HopDongChiTietREF IS NULL OR b.HopDongChiTietREF IS NULL)	
	AND a.SoHopDong NOT IN ('','02','CPC',N'KHÃ¡CHONLINE','N','NB',	
	'CPC760713',--Trên tool hợp đồng là cpm, tool mobilead là cpc	
	'CPC370613',--Trên tool hợp đồng là cpm, tool mobilead là cpc	
	'CPC520913',--Trên tool hợp đồng là cpc, tool mobilead là cpm	
	'CPC821212',--không có ở sản phẩm mobile, tuy nhiên khách vẫn sử dụng(trước đó MobileAd chưa nối với ASD bây giờ)	
	'CPC980713',--không có ở sản phẩm mobile, tuy nhiên khách vẫn sử dụng(trước đó MobileAd chưa nối với ASD bây giờ)	
	'CPC670613',--không có ở sản phẩm mobile, tuy nhiên khách vẫn sử dụng(trước đó MobileAd chưa nối với ASD bây giờ)	
	'cpc1341111',--không có ở sản phẩm mobile, tuy nhiên khách vẫn sử dụng(trước đó MobileAd chưa nối với ASD bây giờ)	
	'QC2020713',---> không chạy ở mobilead	
	'CPC180913',--trên hđ chạy CPM: thực tế chạy 1 chiến dịch CPC và 1 chiến dịch CPM(hiện tại mới chỉ bổ sung phân bổ cho q/c CPM)	
	'QC2701013',--trên hđ chạy CPM: thực tế chạy thêm 1 quảng cáo CPC(hiện tại mới chỉ bổ sung phân bổ cho q/c CPM)	
	'QC320213',--trên hđ chạy CPM: thực tế chạy quảng cáo CPC vs CPM(hiện tại mới chỉ bổ sung phân bổ cho q/c CPM)	
	'NB211113'--trên hđ chạy CPM Catfish: thực tế chạy 1 quảng cáo Catfish và 1 quảng cáo Medium(hiện tại mới chỉ bổ sung phân bổ cho q/c CPM)	
	)	
	ORDER BY a.SoHopDong, a.HopDongChiTietREF, b.SoHopDong, b.HopDongChiTietREF	

	--QC1941014	22000: sai hop dong
	--QC1941014	62085: sai hop dong

END
ELSE IF @TypeProduct = 381
BEGIN
	SELECT a.SoHopDong SHDTC, a.HopDongChiTietREF HDCTThucChay, b.SoHopDong SHDThucTreo, b.HopDongChiTietREF HDCTThucTreo
	FROM 
	(
	SELECT DISTINCT dbo.ThucChay_FormatSoHopDong(tc.SoHopDong)SoHopDong, tc.HopDongChiTietREF
	FROM ThucChay tc 
	WHERE tc.DmSanPhamREF = 381 
	AND tc.NgayThucHien >= '2014-01-01'
	)a
	FULL OUTER JOIN
	(
	SELECT DISTINCT dbo.GetSoHopDongByID(tchdct.HopDongREF) SoHopDong, HopDongChiTietREF
	FROM ThucChayHopDongChiTiet tchdct INNER JOIN HopDongChiTiet hdct 
	ON tchdct.HopDongChiTietREF = hdct.HopDongChiTietID
	WHERE hdct.DmSanPhamREF = 381
	)b
	ON (a.SoHopDong = b.SoHopDong
	AND a.HopDongChiTietREF = b.HopDongChiTietREF
	)
	WHERE ( a.SoHopDong IS NOT NULL AND b.SoHopDong IS NULL
	                           )
	ORDER BY a.SoHopDong, a.HopDongChiTietREF, b.SoHopDong, b.HopDongChiTietREF

END

	
END

```
