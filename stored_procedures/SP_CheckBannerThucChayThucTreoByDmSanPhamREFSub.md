# Stored Procedure: `CheckBannerThucChayThucTreoByDmSanPhamREFSub`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-15 15:29:46.963000
- **Ngày sửa cuối**: 2017-03-24 17:49:47.970000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamREF` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql

--EXEC CheckBannerThucChayThucTreoByDmSanPhamREFSub 342,'2016-01-01'
CREATE PROC [dbo].[CheckBannerThucChayThucTreoByDmSanPhamREFSub]
@DmSanPhamREF INT, @NgayThucHien DATETIME
AS
BEGIN
DECLARE @TypeProduct INT
SET @TypeProduct = (CASE @DmSanPhamREF
WHEN 342 THEN  10
WHEN 339 THEN  5
WHEN 240 THEN  8
WHEN 370 THEN  9
WHEN 598 THEN  14
WHEN 613 THEN  15
WHEN 680 THEN 16
END)

SELECT A.*, B.* FROM (
SELECT  SoHopDong, CONVERT(NVARCHAR(50),DmBannerREF)DmBannerREF, SUM(TongViewThucChay)tv, SUM(TongClickThucChay)tc,
(CASE 
WHEN TypeProduct =5 THEN 339
when TypeProduct =8 THEN 240
when TypeProduct =9 THEN 370
WHEN TypeProduct =10 THEN 342
when TypeProduct =14 THEN 598
WHEN TypeProduct =15 THEN 613
when TypeProduct =16 THEN 680
END)TypeProduct FROM dbo.ThucChay
WHERE DmBannerREF IS not NULL AND TypeProduct =@TypeProduct
AND SoHopDong NOT IN ('Sohagame','','vcm','Soha game','hd_king_test2','hd_stick_test')-- ('','vcm','hd_demo','TEST11111','hd_king_test2','hd_stick_test','sohagame','nb','demo','N')
and ngaythuchien>='2016-01-01'
AND DmBannerREF not in (259052,293059,293059,293059,293059,293059,261115,265194,258893,260343)
AND CONVERT(NVARCHAR(50),DmBannerREF) NOT IN (
SELECT DmBannerREF FROM dbo.ThucChayHopDongChiTiet WHERE DmHinhThucQuangCaoREF = 42 AND DeletedStatus = 0) 
GROUP BY SoHopDong, DmBannerREF, TypeProduct
HAVING  isnull(SUM(TongViewThucChay),0) <> 0 AND ISnull(SUM(TongClickThucChay),0)<> 0
--ORDER BY SUM(TongViewThucChay)
)A
FULL OUTER JOIN 
(
SELECT DISTINCT dbo.ThucChay_FormatSoHopDong(dbo.GetSoHopDongByID(HopDongREF))SoHopDong, tt.DmBannerID, hdct.DmSanPhamREF, hdct.HopDongChiTietID
FROM dbo.ThucChayHopDongChiTietAndBanner_Test tt LEFT JOIN hopdongchitiet hdct ON hdct.HopDongChiTietID = tt.HopDongChiTietREF
WHERE tt.DeletedStatus = 0 AND hdct.DeletedStatus = 0

)B
ON A.SoHopDong = B.SoHopDong
AND A.DmBannerREF =B.DmBannerID
AND A.TypeProduct = B.DmSanPhamREF
WHERE B.DmBannerID IS NULL
AND NOT (A.tv < 1000 OR A.tc < 10)
/*
Mobile
381122: banner Ultra (going 381123)
381122
381123
381147
381148
4 banner này là banner Ultra c nhe
397727: banner này là banner test format Hookeye trên IA a
501319: banner Ultra
503642: banner này là banner iTVC
banner đầu tiên chạy thử nên số HĐ của TVC chưa add đc lên tool Mobile nên để mã HĐ demo a
trong mail Up banner vẫn có cc HTQC đó a
*/
end
```
