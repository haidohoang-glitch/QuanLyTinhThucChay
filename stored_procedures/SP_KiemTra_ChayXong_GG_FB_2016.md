# Stored Procedure: `KiemTra_ChayXong_GG_FB_2016`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-29 18:24:50.703000
- **Ngày sửa cuối**: 2016-11-30 15:56:46.460000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROC [dbo].[KiemTra_ChayXong_GG_FB_2016]
AS 

BEGIN

SELECT
Tc.hopdongid,
 TC.SoHopDong,
 TC.DMSanPhamREF,
 TC.[Tên sản phẩm],
 SUM(TC.thanhtienhd)thanhtienhd,
 SUM(TC.ThanhTienThucChay)ThanhTienThucChay,
 SUM(TC.ThanhTienThucChay2016)ThanhTienThucChay2016
FROM dbo.['ThucChay2016_01012611']  TC

WHERE TC.DmSanPhamREF IN(423,306)
--AND TC.HopDongID = 38410
AND NOT (DmHinhThucQuangCao=13 OR DmLoaiBannerREF=18)
GROUP BY hopdongid, TC.SoHopDong,
 TC.DMSanPhamREF,TC.[Tên sản phẩm]
HAVING ROUND(SUM(thanhtienthucchay),0)=ROUND(SUM(thanhtienhd),0)

END



```
