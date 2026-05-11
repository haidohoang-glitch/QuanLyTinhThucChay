# Stored Procedure: `KiemTra_DauVao_DangTin_WebsiteThucTreoKhacHD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-18 10:28:20.790000
- **Ngày sửa cuối**: 2016-11-24 18:10:23.920000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThoiGianBatDau` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC KiemTra_DauVao_DangTin_WebsiteThucTreoKhacHD '2016-01-01'
CREATE PROCEDURE [dbo].[KiemTra_DauVao_DangTin_WebsiteThucTreoKhacHD]
	-- Add the parameters for the stored procedure here
	--Check HTQC thực treo đăng tin có khác với hd không
	@ThoiGianBatDau DATETIME

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT A.*, B.* FROM 
(
SELECT DISTINCT hd.SoHopDong, hd.HopDongID, hdct.DmSanPhamREF,  hdct.DmWebsiteREF,hdct.TenWebsite, hd.TrangThaiHopDong
 FROM dbo.HopDong hd INNER JOIN hopdongchitiet hdct
ON hd.HopDongID = hdct.HopDongFK
WHERE hdct.DmSanPhamREF IN (141,305,637)
AND hdct.DeletedStatus = 0 AND NOT (hdct.DmLoaiREF =13 OR hdct.DmLoaiBannerREF = 18)
AND HopDongID IN (SELECT HopDongREF FROM dbo.ThucChayHopDongChiTietPR WHERE LastModifiedAt >='2016-01-01' AND ThoiGianBatDau>='2016-01-01'
AND DeletedStatus = 0 )
AND hd.Nam>=2014 
--AND hd.TrangThaiHopDong <> 3
)A
RIGHT JOIN 
(
SELECT DISTINCT HopDongREF, dbo.GetSoHopDongByID(HopDongREF)Shd, DmSanPhamREF, DmWebsiteREF, TenWebsite
FROM dbo.ThucChayHopDongChiTietPR WHERE LastModifiedAt >='2016-01-01'AND ThoiGianBatDau>='2016-01-01'
AND DeletedStatus = 0
AND DmHinhThucQuangCaoREF <> 13
AND RIGHT(dbo.GetSoHopDongByID(HopDongREF),2)>='14'
)B
ON A.HopDongID =B.HopDongREF
AND B.DmSanPhamREF =B.DmSanPhamREF
AND A.DmWebsiteREF = B.DmWebsiteREF
WHERE A.DmWebsiteREF <> B.DmWebsiteREF OR a.DmWebsiteREF IS NULL OR B.DmWebsiteREF IS null

END

```
