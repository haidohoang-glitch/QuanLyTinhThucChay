# Stored Procedure: `sp_KSTC_CheckTCDT_Admatic_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-08-10 17:41:01.367000
- **Ngày sửa cuối**: 2021-06-08 14:46:12.773000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_KSTC_CheckTCDT_Admatic_v2]
	-- Add the parameters for the stored procedure here
	@FromDate Datetime,
	@ToDate Datetime
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	select 'KiTruoc 20/11/2020' Loai,TC.*, TCDT.* from (
SELECT tc.SoHopDong, hd.NgayDanhSoHopDong, DmBannerID,DmSanPhamREF, sum(ThanhTienThucChaySauCK_ChuaVAT)ThanhTienThucChaySauCK_ChuaVAT,
sum(ThanhTienThucChayKM)ThanhTienThucChayKM 
FROM ThucChay_ThanhTien_Admatic tc left join HopDong hd on tc.SoHopDong = hd.SoHopDong
WHERE 1=1
and typeproduct not in (-3)
--AND tc.NgayThucHien = ''
and tc.SoHopDong not in ('HD DEMO','TEST BILLBOARD','HD_TEST')
and NgayDanhSoHopDong between '2020-07-20'  and '2020-11-19'
and ((DmSanPhamREF not in (821,5133) and len(DmBannerID) in (5,6)) or (DmSanPhamREF  in (821,5133) and len(DmBannerID)= 5))
--and DmSanPhamREF = 342
and NgayThucHien between @FromDate and @ToDate
and tc.SoHopDong not in (select SoHopDong from DmThongTinHopDongBanInventory)
GROUP BY tc.SoHopDong,DmBannerID,hd.NgayDanhSoHopDong--,NgayThucHien
,DmSanPhamREF
)TC
 full outer join

(select SoHopDong,DmBannerREF, DmSanPhamREF, sum(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi) tcdt, sum(ThanhTienKM+GiaTriKMThayDoi) tcdtkm
from ThucChayDaTinh tcdt where 1=1
--and DmBannerREF = 76515
and DmHinhThucQuangCao = 42 and DmSanPhamREF not in (817,560)
and ((DmSanPhamREF not in (821,5133) and len(DmBannerREF) in (5,6)) or (DmSanPhamREF  in (821,5133) and len(DmBannerREF)= 5))
and NgayDanhSoHopDong  between '2020-07-20'  and '2020-11-19'
and DotChayBooking <> 'HDBAN_INVENTORY'
and tcdt.SoHopDong not in (select SoHopDong from DmThongTinHopDongBanInventory)
 and NgayThucHien between @FromDate and @ToDate
group by SoHopDong,DmBannerREF,NgayDanhSoHopDong, DmSanPhamREF--,NgayThucHien--,ghichu
)TCDT
on TC.SoHopDong = TCDT.SoHopDong
and TC.DmBannerID = TCDT.DmBannerREF
and TC.DmSanPhamREF = TCDT.DmSanPhamREF
where isnull(round(TC.ThanhTienThucChaySauCK_ChuaVAT,0),0) <> isnull(round(TCDT.tcdt,0),0)
or isnull(TC.ThanhTienThucChayKM ,0) <> isnull(TCDT.tcdtkm,0)
or TC.SoHopDong is null or TCDT.SoHopDong is null
or TC.DmBannerID is null or TCDT.DmBannerREF is null
or TC.DmSanPhamREF is null or TCDT.DmSanPhamREF is null
order by TC.SoHopDong, TC.DmBannerID, TCDT.SoHopDong, TCDT.DmBannerREF
----------------------------------------------ki từ 20/11/2020-----------------------

	select 'KiTu 20/11/2020' Loai,TC.*, TCDT.* from (
SELECT tc.SoHopDong, hd.NgayDanhSoHopDong, DmBannerID,DmSanPhamREF, sum(ThanhTienThucChaySauCK_ChuaVAT)ThanhTienThucChaySauCK_ChuaVAT,
sum(ThanhTienThucChayKM)ThanhTienThucChayKM 
FROM ThucChay_ThanhTien_Admatic tc left join HopDong hd on tc.SoHopDong = hd.SoHopDong
WHERE 1=1
and typeproduct not in (-3)
--AND tc.NgayThucHien = ''
and tc.SoHopDong not in ('HD DEMO','TEST BILLBOARD','HD_TEST')
and NgayDanhSoHopDong >= '2020-11-20'
--and DmSanPhamREF = 342
and NgayThucHien between @FromDate and @ToDate
and tc.SoHopDong not in (select SoHopDong from DmThongTinHopDongBanInventory)
GROUP BY tc.SoHopDong,DmBannerID,hd.NgayDanhSoHopDong--,NgayThucHien
,DmSanPhamREF
--having sum(ThanhTienThucChaySauCK_ChuaVAT) <> 0 
)TC
 full outer join

(select SoHopDong,DmBannerREF, sum(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi) tcdt, sum(ThanhTienKM+GiaTriKMThayDoi) tcdtkm
from ThucChayDaTinh tcdt where 1=1
--and DmBannerREF = 567334
and DmHinhThucQuangCao = 42 and DmSanPhamREF not in (817,560,140)
and NgayDanhSoHopDong >= '2020-11-20'
and DotChayBooking <> 'HDBAN_INVENTORY'
 --and SoHopDong ='QC5180720' and DmSanPhamREF = 342
 and tcdt.SoHopDong not in (select SoHopDong from DmThongTinHopDongBanInventory)
 and NgayThucHien between @FromDate and @ToDate
group by SoHopDong,DmBannerREF,NgayDanhSoHopDong--,NgayThucHien--,ghichu
)TCDT
on TC.SoHopDong = TCDT.SoHopDong
and TC.DmBannerID = TCDT.DmBannerREF
--and TC.NgayThucHien = TCDT.NgayThucHien
where isnull(round(TC.ThanhTienThucChaySauCK_ChuaVAT,0),0) <> isnull(round(TCDT.tcdt,0),0)
or isnull(TC.ThanhTienThucChayKM ,0) <> isnull(TCDT.tcdtkm,0)
or TC.SoHopDong is null or TCDT.SoHopDong is null
or TC.DmBannerID is null or TCDT.DmBannerREF is null
--or TC.NgayThucHien is null or TCDT.NgayThucHien is null
order by TC.SoHopDong, TC.DmBannerID, TCDT.SoHopDong, TCDT.DmBannerREF
END




```
