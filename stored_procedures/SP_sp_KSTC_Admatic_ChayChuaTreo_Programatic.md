# Stored Procedure: `sp_KSTC_Admatic_ChayChuaTreo_Programatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-07-27 17:05:40.480000
- **Ngày sửa cuối**: 2021-07-27 17:05:40.480000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
create PROCEDURE [dbo].[sp_KSTC_Admatic_ChayChuaTreo_Programatic]
	-- Add the parameters for the stored procedure here
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

--- Check các banner admatic đã chạy nhưng chưa treo, loại các hợp đồng programatic đã chạy full ký

---List hợp đồng programatic
declare @Table_programmatic table
(Sohopdong nvarchar(50)
);
insert into @Table_programmatic
(Sohopdong
)
select distinct hd.Sohopdong from Hopdong hd join Hopdongchitiet hdct
on hd.Hopdongid = hdct.Hopdongfk
where hdct.DmLoaiNenTangREF = 9
and convert(date,hdct.createdat) >='2021-01-01'
and hd.Trangthaihopdong <> 3
and hdct.Deletedstatus = 0

---select * from @Table_programmatic

---List hợp đồng programatic đã chạy xong
declare @Table_programmatic_done table
(Sohopdong nvarchar(50),
hopdongchitiet int,
thanhtien float,
tc float
);
insert into @Table_programmatic_done
(Sohopdong,
hopdongchitiet,
thanhtien,
tc
)
select tcdt.Sohopdong,tcdt.Hopdongchitietref, hdct.thanhtien, sum(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi) as tc
from Thucchaydatinh tcdt join Hopdongchitiet hdct
on tcdt.HopDongChiTietREF = hdct.HopDongChiTietID 
where hdct.DmLoaiNenTangREF = 9
and tcdt.Ngaythuchien>='2021-01-01'
group by tcdt.Hopdongchitietref, hdct.thanhtien, tcdt.Sohopdong
having sum(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi) >= hdct.thanhtien
---select *from @Table_programmatic

select distinct A.SoHopdong,A.NhanHopDong, A.DmBannerREF, A.DmSanPhamREF, A.TenSanPham,B.* from (
select  tc.SoHopdong,hd.NhanHopDong, convert(nvarchar(50),DmBannerREF)DmBannerREF,dmsanphamref, TenSanpham 
from ThucChay tc left join HopDong hd on tc.SoHopDong = hd.SoHopDong where
1=1  and NgayThuchien >='2021-01-01' 
and  tc.CreatedBy = 'From API_Admatic'   
and 	 tc.SoHopdong  in (select Sohopdong from @Table_programmatic)
union all 
select tc.SoHopdong,hd.NhanHopDong, DmBannerID DmBannerREF, dmsanphamref, TenSanpham 
from ThucChay_ThanhTien_Admatic tc left join HopDong hd on tc.SoHopDong = hd.SoHopDong where
1=1  and NgayThuchien >='2021-01-01' 
and 	 tc.SoHopdong  in (select Sohopdong from @Table_programmatic)
)A 
full outer join 
(select distinct convert(nvarchar(50),DmBannerREF)DmBannerREF
from Thucchayhopdongchitiet where 
1=1 
and  DmHinhThucQuangCaoREF = 42 
and DeletedStatus = 0 and HopDongChiTietREF not in (0,-1)
)B on A.DmBannerREF = B.DmBannerREF
where 
A.Sohopdong not in (select Sohopdong from @Table_programmatic_done)
and B.DmBannerREF is null 
----and A.DmBannerREF not in (79603, 79581,80237,80125,80236,80124,80026,80490,80491 ) -- chạy program matic
order by A.SoHopDong



END




```
