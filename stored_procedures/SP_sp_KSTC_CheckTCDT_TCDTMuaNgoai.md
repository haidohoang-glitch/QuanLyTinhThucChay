# Stored Procedure: `sp_KSTC_CheckTCDT_TCDTMuaNgoai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-08-06 15:23:17.290000
- **Ngày sửa cuối**: 2021-01-06 15:15:27.833000

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
--sp_KSTC_CheckTCDT_TCDTMuaNgoai '2021-01-05'
CREATE PROCEDURE [dbo].[sp_KSTC_CheckTCDT_TCDTMuaNgoai] 
	-- Add the parameters for the stored procedure here
	@NgayThucHien DateTime
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

--1. Kiem tra du lieu 2 bang
	select 'Check2Table'[NoiDung], A.*,B.*, A.tc- B.BanCK from (
select SoHopDong, HopDongID, HopDongChiTietREF, DmSanPhamREF, DotChayBooking, round(sum(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi),0)tc
from ThucChayDaTinh where  1=1
and NgayThucHien <= @NgayThucHien 
and (DmHinhThucQuangCao = 13 or DmLoaiBannerREF =18)
and DmChienDichREF = 0 
and Nam >=2019
--and HopDongChiTietREF = 577458
group by SoHopDong,HopDongID, HopDongChiTietREF, DmSanPhamREF, DotChayBooking
--having  round(sum(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi),0) <> 0
)A
full outer join
(
select SoHopDong, HopdongREF, HopDongChiTietREF, dmsanphamref, 
convert(nvarchar(50),ThucChayMuaNgoaiChiTietREF)ThucChayMuaNgoaiChiTietREF,
ROUND(SUM(TongThanhTienThucChayBanSauCK),0)BanCK,
ROUND(SUM (ThanhTienLaiThucChaySauCK+GiaTriThayDoiLaiSauCK),0)LaiThucChay
from ThucChayDaTinh_MuaNgoai where 1=1
and NgayThucHien <=@NgayThucHien
and DmChienDichREF = 0 
and RIGHT(SoHopDong,2)>='19'
--and HopDongChiTietREF = 577458
group by SoHopDong,HopDongChiTietREF, ThucChayMuaNgoaiChiTietREF,HopdongREF,dmsanphamref
)B
on A.HopDongChiTietREF = B.HopDongChiTietREF
and A.DotChayBooking = B.ThucChayMuaNgoaiChiTietREF
where (A.HopDongChiTietREF is null or B.HopDongChiTietREF is null or A.DotChayBooking is null or B.ThucChayMuaNgoaiChiTietREF is null)
and not ((A.tc = 0 and isnull(B.LaiThucChay,0) =0 ) or (A.tc = 1 and isnull(B.LaiThucChay,0) =0))
--or abs(A.tc - B.BanCK) > 1
---------------------------------------------------check lãi âm------------------------------------------------------
select  'CheckLaiAm'[NoiDung],SoHopDong, HopdongREF, HopDongChiTietREF, 
dmsanphamref,ROUND(SUM (ThanhTienLaiThucChaySauCK+GiaTriThayDoiLaiSauCK),0)LaiThucChay, max(NgayThucHien) max_NgayThucHien
from ThucChayDaTinh_MuaNgoai
where 1=1 and DmChienDichREF = 0
group by SoHopDong,HopdongREF, HopDongChiTietREF, dmsanphamref
having ROUND(SUM (ThanhTienLaiThucChaySauCK+GiaTriThayDoiLaiSauCK),0) < 0 and max(NgayThucHien) >='2020-01-01'
order by  max(NgayThucHien) desc
END

```
