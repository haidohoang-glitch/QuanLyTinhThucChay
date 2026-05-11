# Stored Procedure: `KiemTra_DauVao_CPM_BannerChayKhacThucTreo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-18 10:07:06.037000
- **Ngày sửa cuối**: 2017-03-03 13:58:35.063000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[KiemTra_DauVao_CPM_BannerChayKhacThucTreo]
	-- Add the parameters for the stored procedure here
	--Check banner chạy của các sp CPM chưa được gán trong thực treo

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT A.*, B.* FROM (
SELECT  SoHopDong shdThucChay, CONVERT(NVARCHAR(50),DmBannerREF)DmBannerREFThucChay, ISNULL(SUM(TongViewThucChay),0)tv, ISNULL(SUM(TongClickThucChay),0)tc,
(CASE 
WHEN TypeProduct =5 THEN 339
when TypeProduct =8 THEN 240
when TypeProduct =9 THEN 370
WHEN TypeProduct =10 THEN 342
when TypeProduct =14 THEN 598
WHEN TypeProduct =15 THEN 613
when TypeProduct =16 THEN 680
END)TypeProduct FROM dbo.ThucChay
WHERE DmBannerREF IS not NULL AND TypeProduct IN (5,8,9,10,14,15,16)
AND SoHopDong NOT IN ('','vcm','hd_demo','TEST11111','hd_king_test2','hd_stick_test','sohagame','nb','demo','hd test','hd_demo_honda')
AND NgayThucHien>='2016-01-01'
AND RIGHT(SoHopDong,2) >='16'
--AND DmBannerREF not in (259052,293059,293059,293059,293059,293059,261115,265194,258893,260343) --cac hd box app cpm nam 2014
AND SoHopDong NOT IN (SELECT SoHopDong FROM dbo.HopDong WHERE TrangThaiHopDong = 3)
GROUP BY SoHopDong, DmBannerREF, TypeProduct
--HAVING  (ISNULL(SUM(TongViewThucChay),0) <> 0 or ISnull(SUM(TongClickThucChay),0)<> 0)
--ORDER BY SUM(TongViewThucChay)
)A
FULL OUTER JOIN 
(
SELECT DISTINCT dbo.GetSoHopDongByID(HopDongREF)SoHopDong, tt.DmBannerID, hdct.DmSanPhamREF
FROM dbo.ThucChayHopDongChiTietAndBanner tt LEFT JOIN hopdongchitiet hdct ON hdct.HopDongChiTietID = tt.HopDongChiTietREF
WHERE tt.DeletedStatus = 0 AND hdct.DeletedStatus = 0
AND RIGHT(dbo.GetSoHopDongByID(HopDongREF),2) >='16'
--AND ROUND(hdct.ThanhTien- hdct.ThanhtienThucChay,0) <> 0
AND hdct.DmSanPhamREF IN (339,370,598,240,613,598,342,680)
AND dbo.GetSoHopDongByID(HopDongREF) IN (SELECT SoHopDong FROM dbo.HopDong)
AND hdct.HopDongFK NOT IN (SELECT HopDongID FROM dbo.HopDong WHERE TrangThaiHopDong = 3)
)B
ON A.shdThucChay = B.SoHopDong
AND A.DmBannerREFThucChay =B.DmBannerID
AND A.TypeProduct = B.DmSanPhamREF
WHERE (B.DmBannerID IS NULL AND (A.tv>1000 or A.tc >10))
ORDER BY A.TypeProduct, A.shdThucChay
END

```
