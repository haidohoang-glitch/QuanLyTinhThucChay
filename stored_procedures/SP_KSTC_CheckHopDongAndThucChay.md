# Stored Procedure: `KSTC_CheckHopDongAndThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-08 16:57:21.443000
- **Ngày sửa cuối**: 2014-12-08 16:57:21.443000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE dbo.KSTC_CheckHopDongAndThucChay
	-- Add the parameters for the stored procedure here
	@DmSanPhamREF INT --10: Mobile, 381: Sponsor
AS
BEGIN
	IF @DmSanPhamREF = 10
	BEGIN	
		SELECT a.SoHopDong SHDTC, a.HopDongChiTietREF as HopDongChiTietTC,a.tv, a.tc,
		a.ProductUnitName, b.SoHopDong SHDHD, 
		b.HopDongChiTietID as HopDongChiTietHD, b.DonViTinh

		FROM (
		SELECT dbo.ThucChay_FormatSoHopDong(tc.SoHopDong)SoHopDong, 
		tc.HopDongChiTietREF, tc.ProductUnitID, tc.ProductUnitName
		,SUM(tc.TongViewThucChay)tv, SUM(tc.TongClickThucChay)tc
		  FROM ThucChay tc WHERE tc.TypeProduct = 10
		 -- AND tc.SoHopDong like '%CPC080413%'
		GROUP BY dbo.ThucChay_FormatSoHopDong(tc.SoHopDong), 
		tc.HopDongChiTietREF, tc.ProductUnitID, tc.ProductUnitName
		)a
		FULL OUTER JOIN
		(
		SELECT DISTINCT SoHopDong, HopDongChiTietID, hdct.DonViTinh
		FROM HopDong hd INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
		WHERE hdct.DmSanPhamREF = 342 AND hdct.DeletedStatus <> 1
		)b
		ON (a.SoHopDong = b.SoHopDong
		AND a.HopDongChiTietREF = b.HopDongChiTietID
		)
		WHERE (b.SoHopDong IS NULL 
		OR b.HopDongChiTietID IS NULL 
		OR b.DonViTinh IS NULL 
		)
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
		ORDER BY a.SoHopDong, a.HopDongChiTietREF, b.SoHopDong, b.HopDongChiTietID
	END
	ELSE IF @DmSanPhamREF = 381
		BEGIN
		SELECT a.SoHopDong SHDTC, a.HopDongChiTietREF as HopDongChiTietTC, a.ProductUnitName, b.SoHopDong SHDHD, 
		b.HopDongChiTietID as HopDongChiTietHD, b.DonViTinh
		FROM (
		SELECT DISTINCT dbo.ThucChay_FormatSoHopDong(tc.SoHopDong)SoHopDong, tc.HopDongChiTietREF, tc.ProductUnitID, tc.ProductUnitName
		  FROM ThucChay tc WHERE tc.TypeProduct = 381
		 -- AND tc.SoHopDong like '%CPC080413%'
		)a
		FULL OUTER JOIN
		(
		SELECT DISTINCT SoHopDong, HopDongChiTietID, hdct.DonViTinh
		FROM HopDong hd INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
		WHERE hdct.DmSanPhamREF = 381 --AND hdct.DeletedStatus <> 1
		--AND hd.SoHopDong = 'CPC080413'
		)b
		ON (a.SoHopDong = b.SoHopDong
		AND a.HopDongChiTietREF = b.HopDongChiTietID
		)
		WHERE (b.SoHopDong IS NULL 
		OR b.HopDongChiTietID IS NULL 
		OR b.DonViTinh IS NULL 
		)
		ORDER BY a.SoHopDong, a.HopDongChiTietREF, b.SoHopDong, b.HopDongChiTietID

		END
END

```
