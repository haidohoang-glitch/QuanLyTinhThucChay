# Stored Procedure: `CheckBannerCoChayChuaTreo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-09-11 11:21:54.030000
- **Ngày sửa cuối**: 2018-09-26 10:38:59.570000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--CheckBannerCoChayChuaTreo '2018-09-25'
CREATE PROCEDURE [dbo].[CheckBannerCoChayChuaTreo]
	@NgayThucHien DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	
    -- Insert statements for procedure here
	--create ThucChayTemp
	
DROP TABLE #CheckBannerThucChayTemp
SELECT *
INTO #CheckBannerThucChayTemp
FROM (

	SELECT LTRIM(RTRIM(ISNULL(tc.SoHopDong,'')))SoHopDong,
 CONVERT(NVARCHAR(50),tc.DmBannerREF)DmBannerREF, 
SUM(tc.TongViewThucChay)tv, SUM(tc.TongClickThucChay)tc,
TypeProduct
 FROM thucchay tc WHERE tc.CreatedBy NOT LIKE N'%From API_Admatic%'
AND tc.NgayThucHien =@NgayThucHien
AND tc.TypeProduct NOT IN (-3,17)
AND tc.SoHopDong NOT IN( '' ,'TONGSANPHAM','Sohagame')
AND tc.SoHopDong NOT LIKE'%demo%' 
AND tc.SoHopDong NOT like '%test%'
GROUP BY tc.SoHopDong, tc.DmBannerREF,tc.TypeProduct
)A

SELECT A.*, B.* FROM (
SELECT SoHopDong,
DmBannerREF, tv,tc,TypeProduct
FROM #CheckBannerThucChayTemp tc 
WHERE DmBannerREF NOT IN (SELECT tt.DmBannerREF FROM dbo.ThucChayHopDongChiTiet tt WHERE (tt.DmHinhThucQuangCaoREF = 42 OR tt.HopDongChiTietREF = -1) AND tt.DeletedStatus = 0)
AND DmBannerREF NOT IN (540557,540558,540565,540566,541419,542144,542197,542218,542263,543722,543758,543762,543826,543895,543896,543910,543972,544068,544247,544251,544272,544271,544325,544396,544395,544394,544393544521,544544,544561,544622,544740,545047)
)A

LEFT JOIN 
(
SELECT DISTINCT
dbo.GetSoHopDongByID(HopDongREF)shd, CONVERT(NVARCHAR(50),DmBannerREF)DmBannerREF 
FROM dbo.ThucChayHopDongChiTiet WHERE DeletedStatus = 0
AND HopDongChiTietREF <> -1
AND DmSanPhamREF IN (240,339,342,598,613,680,370,735)
)B
ON A.SoHopDong = B.shd
AND A.DmBannerREF = B.DmBannerREF
WHERE 1=1
AND ( B.shd IS NULL OR B.DmBannerREF IS NULL
)
ORDER BY RIGHT(A.SoHopDong,2) DESC

END

```
