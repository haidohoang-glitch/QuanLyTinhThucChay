# Stored Procedure: `KiemTra_DaTinh_Mobile_TinhDungDu`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-21 10:58:52.240000
- **Ngày sửa cuối**: 2016-11-21 10:58:52.240000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[KiemTra_DaTinh_Mobile_TinhDungDu]
	-- Add the parameters for the stored procedure here
    
AS
BEGIN
	DECLARE @HopDongID NVARCHAR(MAX)
select Z.*, TCDT.*,dbo.FormatNumber(Z.thanhtientc - TCDT.tcdt)lech  from (
select Y.HopDOngID,Y.DonViTinh, sum(Y.thanhtientc) thanhtientc
from (select X.HopDOngID, X.hopdongchitietref, X.tv, X.tc, X.DonViTinh, X.SoLuong,
(case when X.sltc >=X.SoLuong then X.SoLuong*DonGia* (100-X.ChietKhau)/100
 else  X.sltc*DonGia* (100-X.ChietKhau)/100 end) thanhtientc

  from ( 

select K.HopDongID, K.hopdongchitietref, sum(K.tv)tv,sum(K.tc)tc, K.ChietKhau,
(case when K.DonViTinh = 'CPC' then 'CLICK' when K.DonViTinh = 'CPM' then 'VIEW' end) DonViTinh,
(case when K.DonViTinh = 'CPC' then K.DonGia when K.DonViTinh = 'CPM' then K.DonGia/1000 end) DonGia,
(case when K.DonViTinh = 'CPC' then sum(K.tc) when K.DonViTinh = 'CPM' then sum(K.tv)end) sltc,
(case when K.DonViTinh = 'CPC' then K.SoLuong when K.DonViTinh = 'CPM' then K.SOLuong*1000 end)
SoLuong 

  from (
select A.*, B.hopdongchitietref,B.DonViTinh, B.SoLuong, B.DonGia, B.ChietKhau, B.ThanhTIen, B.HopDongID from (
select convert(nvarchar(50),dmbannerref)dmbannerref, isnull(sum(Tongviewthucchay),0)tv, isnull(sum(TongClickThucChay),0)tc from thucchay where typeproduct = 10
group by dmbannerref
)A
left join (
select distinct convert(nvarchar(50),tt.dmbannerref)dmbannerref, hopdongchitietref, ct.DonViTinh, ct.SoLuong,ct.HopDongID,
 ct.DonGia, ct.ChietKhau, ct.ThanhTIen
 from thucchayhopdongchitiet tt
inner join (select hopDongID, HopDongChiTietID,DonViTinh, SoLuong, DonGia, ChietKhau, ThanhTIen from HopDong hd inner join HopDongChiTiet hdct on HopDongID = HopDongFK where trangthaihopdong <> 3 and hdct.deletedstatus = 0 
and dmsanphamref = 342
and DonViTinh not in (N'đ/v',N'Gói', 'CPA', 'CPV')
)

 ct on  ct.HopDongChiTietID= tt.HopDongChiTietREF
where tt.deletedstatus = 0

)B
on A.DmBannerREF = B.DmBannerREF
where not (A.tv < 1000 and B.DonViTinh = 'CPM')
and not (A.tc <10 and B.DonViTinh = 'CPC')
)K
group by K.HopDongChiTietREF, K.DonViTinh, K.SOLuong, K.DonGia, K.ChietKhau, K.ThanhTien, K.HopDOngID
)X
)Y
group by Y.HopDongID, Y.DonViTinh
)Z
full outer join

(select HopDOngID, SoHopDong, DonViTinh, sum(ThanhTienSauTrietKhauThucChay+GiaTriThayDOi)tcdt
 from thucchaydatinh where dmsanphamref =342 and trangthaihopdong <> 3
 group by  HopDOngID, SoHopDong, DOnviTinh
 having round(sum(ThanhTienSauTrietKhauThucChay+GiaTriThayDOi),0) <> 0
 )TCDT
 on Z.HopDongID= TCDT.HopDongID
 and Z.DonViTinh = TCDT.DonViTinh
where round(Z.thanhtientc,0) <> round(TCDT.tcdt,0)
order BY TCDT.HopDongID desc

END

```
