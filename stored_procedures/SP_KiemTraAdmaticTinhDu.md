# Stored Procedure: `KiemTraAdmaticTinhDu`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-05-18 14:27:42.217000
- **Ngày sửa cuối**: 2017-05-18 14:27:42.217000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE KiemTraAdmaticTinhDu
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	DROP TABLE  #AdmaticChayXong
SELECT hd.SoHopDong, SUM(hdct.ThanhTien)ttpb, SUM(hdct.ThanhtienThucChay)tttcpb,(SUM(hdct.ThanhTien)- SUM(hdct.ThanhtienThucChay))Lechhdtc
INTO #AdmaticChayXong
FROM hopdong hd INNER JOIN dbo.HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK 
WHERE hdct.DeletedStatus = 0 --AND hdct.DmLoaiREF = 42
AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18) AND hdct.DmSanPhamREF IN (339,240,342,598,613)
GROUP BY  hd.SoHopDong, hd.ThanhTienThucChay 
HAVING ABS((SUM(hdct.ThanhTien)- SUM(hdct.ThanhtienThucChay))) BETWEEN 0 AND 1012

--SELECT * FROM #AdmaticChayXong
----Ra soat tcdt da tinh dung va du cac sp chay admatic chua?
SELECT C.*, D.*, (ISNULL(C.TTTuTinh,0) - ISNULL(D.tc,0)) Lech FROM (
SELECT A.*, B.*, (CASE 
WHEN B.LoaiDonGiaTheoDVT IN (2,3) THEN A.tv*B.DonGiaBanner/1000 
WHEN B.LoaiDonGiaTheoDVT IN (1) THEN A.tc*B.DonGiaBanner END )TTTuTinh FROM (
SELECT SoHopDong, DmBannerREF, TypeProduct,SUM(ISNULL(TongViewThucChay,0))tv, SUM(ISNULL(TongClickThucChay,0))tc
FROM thucchay WHERE TypeProduct IN (5,9,10,8,14,15,16) AND NgayThucHien >='2016-07-01' AND
DmBannerREF NOT IN (SELECT DISTINCT DmBannerREF FROM dbo.ThucChayHopDongChiTiet WHERE DeletedStatus =0 AND ThoiGianBatDau >='2016-07-01' AND 
DmHinhThucQuangCaoREF <> 42)
AND (SoHopDong NOT IN ('HD_DEMO','hd_king_test2','hd_stick_test','demo','hd test','hd_demo_honda') OR (SoHopDong = '' AND TypeProduct =10 AND IsNoiBo = 1))
--AND DmBannerREF = 511458
AND SoHopDong NOT IN (SELECT SoHopDong FROM #AdmaticChayXong)
GROUP BY SoHopDong, TypeProduct, DmBannerREF
--HAVING (SUM(ISNULL(TongViewThucChay,0)) >1000 OR SUM(ISNULL(TongClickThucChay,0)) > 10)
)A
LEFT join
(SELECT AdmaticDonGiaBannerID, AdmaticBannerID, AdmaticProductID, DmBannerID, DonGiaBanner_VAT/1.1 DonGiaBanner, LoaiDonGiaTheoDVT
FROM dbo.AdmaticDonGiaBanner WHERE DmBannerID <> 0 AND DeletedStatus = 0)
B
ON A.DmBannerREF = B.DmBannerID
WHERE ((RIGHT(A.SoHopDong,2) ='16' AND SUBSTRING(A.SoHopDong,7,1)>='7') OR (RIGHT(A.SoHopDong,2) >='17' AND SUBSTRING(A.SoHopDong,7,1)>='1'))
AND  SoHopDong NOT IN (SELECT SoHopDong FROM #AdmaticChayXong) and 
A.SoHopDong NOT IN 
			('QC2850716',--kingsize, banner 386338 khong phải admatic, hd da chạy xong
			'QC0290816', --kingsize, banner 384298 khong phải admatic, hd da chạy xong
			'QC1350417','QC0570417'-- hd cpv
			)
)C
FULL OUTER JOIN 
(SELECT SoHopDong, DmBannerREF, SUM(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi)*100/(100-ChietKhau) tc
FROM dbo.ThucChayDaTinh WHERE DmHinhThucQuangCao = 42
AND  DmSanPhamREF <> 585 
AND SoHopDong NOT IN (SELECT SoHopDong FROM #AdmaticChayXong)
--AND DmBannerREF = 511458
GROUP BY SoHopDong,DmBannerREF, ChietKhau
HAVING SUM(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi) <> 0
)D
ON C.DmBannerREF = D.DmBannerREF
WHERE ABS(ISNULL(ROUND(C.TTTuTinh,0),0)- ISNULL(ROUND(D.tc,0),0))>1000
ORDER BY C.SoHopDong, C.TypeProduct,  C.DmBannerREF
END

```
