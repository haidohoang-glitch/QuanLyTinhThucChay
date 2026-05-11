# Stored Procedure: `sp_KSTC_CheckThanhTienThucChay_BannerAdmatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-09-23 11:40:32.533000
- **Ngày sửa cuối**: 2020-12-23 17:42:29.753000

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
--sp_KSTC_CheckThanhTienThucChay_BannerAdmatic '2020-12-08'
CREATE PROCEDURE [dbo].[sp_KSTC_CheckThanhTienThucChay_BannerAdmatic]
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here

	--Check soluong--
	select TC.*, TC.SL_ThucChay - (TC.SoLuongThucChay_tt+SoLuongThucChayKM_tt) from (
select 'CheckSL'Loai,A.SoHopDong, A.DmBannerREF,A.DmSanPhamREF,
(case when B.DonViTinh = 'CLICK' then A.tc 
      when B.DonViTinh = 'VIEW' then A.tv
	  else - 1 end) SL_ThucChay,B.* from (
Select tc.SoHopDong, tc.DmBannerREF,DmSanPhamREF, sum(TongViewThucChay)tv, sum(TongClickThucChay)tc
from ThucChay tc
inner join HopDong hd on hd.SoHopDong = tc.SoHopDong
where hd.NgayDanhSoHopDong >= '2020-07-20'
--and DmBannerREF ='76028'
and len(DmBannerREF) = 5
and NgayThucHien <=@NgayThucHien
and tc.SoHopDong not in ('HD DEMO','TEST_CD','HD_TEST_NB','TEST FORMAT BALLOON','TEST ALL')
and tc.SoHopDong not like '%TEST%'
and tc.SoHopDong not like '%DEMO%'
and tc.SoHopDong not like '%HD%'
group by tc.SoHopDong,tc.DmBannerREF,DmSanPhamREF
)A
 full outer join 

(select tc.SoHopDong SoHopDong_tt,DmBannerID,DmSanPhamREF DmSanPhamREF_tt,
tc.DonViTinh, sum(tc.SoLuongThucChay)SoLuongThucChay_tt,sum(tc.SoLuongThucChayKM)SoLuongThucChayKM_tt
from thucchay_thanhtien_admatic tc
inner join HopDong hd on hd.SoHopDong = tc.SoHopDong
where len(DmBannerID) =5 
and hd.NgayDanhSoHopDong >= '2020-07-20'
and NgayThucHien <= @NgayThucHien
--and DmBannerID = '76028'
and DmSanPhamREF not in (585,821)
and tc.SoHopDong not in ('HD DEMO','TEST_CD','HD_TEST_NB','TEST FORMAT BALLOON','TEST ALL')
and tc.SoHopDong not like '%TEST%'
and tc.SoHopDong not like '%DEMO%'
and tc.SoHopDong not like '%HD%'
and tc.DonViTinh <> 'TRUE VIEW'
group by tc.SoHopDong,DmBannerID,tc.DonViTinh,DmSanPhamREF
)B
on A.DmBannerREF = B.DmBannerID
and A.DmSanPhamREF =B.DmSanPhamREF_tt
)TC
where (TC.DmBannerREF is null or TC.DmBannerID is null  
or TC.DmSanPhamREF is null or TC.DmSanPhamREF_tt is null
or TC.SL_ThucChay <> TC.SoLuongThucChay_tt + SoLuongThucChayKM_tt)
and TC.SL_ThucChay <> -1
order by TC.SoHopDong

	--Check tien--
select 'CheckTien'Loai,G.HopDongREF, G.SoHopDong,G.HopDongChiTietREF,G.ChietKhau,G.DmBannerREF, G.DonViTinh, isnull(G.TienThucChay,0)TienThucChay
 ,isnull(G.TienThucChayKM,0)TienThucChayKM, TC.*, (isnull(G.TienThucChay,0) - Tc.thanhtien_admatic)Lech from (
select A.*,B.tv,B.tc,
(case when  A.DonViTinh ='CPM' and A.ChietKhau <> 100 then B.tv*A.DonGia/1000*(100 - A.ChietKhau)/100 
when A.DonViTinh ='CPC' and A.ChietKhau <> 100 then B.tc*A.DonGia*(100 - A.ChietKhau)/100
--when  A.DonViTinh not in ('CPC','CPM') and A.ChietKhau <> 100 then -1
end )TienThucChay,
(case when  A.DonViTinh ='CPM'  and A.ChietKhau = 100 then B.tv*A.DonGia/1000
when  A.DonViTinh ='CPC'  and A.ChietKhau= 100 then B.tc*A.DonGia
--when   A.DonViTinh not in ('CPC','CPM') and A.ChietKhau = 100 then -1
end )TienThucChayKM
from (
select  HopDongREF,SoHopDong,tt.HopDongChiTietREF, ct.ChietKhau, ct.DonGia,ct.DonViTinh,
tt.DmBannerREF--, sum(TongViewThucChay)tv, sum(TongClickThucChay)tc 
from ThucChayHopDongChiTiet tt 
inner join HopDong hd on hd.HopDongID = tt.HopDongREF
inner join HopDongChiTiet ct on ct.HopDongChiTietID = tt.HopDongChiTietREF
where DmHinhThucQuangCaoREF = 42 and len(tt.DmBannerREF) = 5 and tt.DeletedStatus = 0
and NgayDanhSoHopDong >='2020-07-20'
and HopDongChiTietREF not in (0,-1)
and ct.DonViTinh in ('CPM','CPC','TRUEVIEW','TRUE VIEW')
--and SoHopDong ='QC5180720'
--and tt.DmBannerREF ='76028'
)A
inner join
(
Select tc.SoHopDong, tc.DmBannerREF, sum(TongViewThucChay)tv, sum(TongClickThucChay)tc
from ThucChay tc
inner join HopDong hd on hd.SoHopDong = tc.SoHopDong
where hd.NgayDanhSoHopDong >= '2020-07-20'
--and DmBannerREF ='76028'
and NgayThucHien <=@NgayThucHien
and tc.SoHopDong not in ('HD DEMO','TEST_CD','HD_TEST_NB','TEST FORMAT BALLOON','TEST ALL')
and tc.SoHopDong not like '%TEST%'
and tc.SoHopDong not like '%DEMO%'
and tc.SoHopDong not like '%HD%'
group by tc.SoHopDong,tc.DmBannerREF
)B
on A.DmBannerREF = B.DmBannerREF
) G full outer join 

(select tc.SoHopDong,DmBannerID,tc.DonViTinh, sum(ThanhTienThucChaySauCK_ChuaVAT)thanhtien_admatic, sum(ThanhTienThucChayKM/1.1)km 
from thucchay_thanhtien_admatic tc
inner join HopDong hd on hd.SoHopDong = tc.SoHopDong
where len(DmBannerID) =5 
and NgayThucHien <= @NgayThucHien
--and DmBannerID = '76028'
and convert(nvarchar(50),DmBannerID) in (select tt.DmBannerREF from ThucChayHopDongChiTiet tt inner join HopDongChiTiet hdct
											  on  tt.HopDongChiTietREF = hdct.HopDongChiTietID
												where tt.DeletedStatus = 0 and hdct.DeletedStatus = 0 and hdct.DonViTinh <> N'Gói' and tt.DmBannerREF <> '0' and hdct.DmLoaiREF = 42)

and DmSanPhamREF not in (585,821,5133)
and hd.NgayDanhSoHopDong >= '2020-07-20'
and tc.SoHopDong not in ('HD DEMO','TEST_CD','HD_TEST_NB','TEST FORMAT BALLOON','TEST ALL')
and tc.SoHopDong not like '%TEST%'
and tc.SoHopDong not like '%DEMO%'
and tc.SoHopDong not like '%HD%'
and tc.DonViTinh not in ('TRUE VIEW','TRUEVIEW')
group by tc.SoHopDong,DmBannerID,tc.DonViTinh
)TC
on G.DmBannerREF = TC.DmBannerID
where abs(isnull(G.TienThucChay,0)- isnull(TC.thanhtien_admatic,0)) >100
or abs(isnull(G.TienThucChayKM,0) - isnull(TC.km,0))> 100
or G.DmBannerREF is null or TC.DmBannerID is null 
order by G.HopDongREF desc, G.DmBannerREF asc

END





```
