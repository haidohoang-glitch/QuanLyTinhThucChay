# Stored Procedure: `sp_KSTC_CheckGetData_Admatic_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-08-08 11:00:10.737000
- **Ngày sửa cuối**: 2021-06-08 14:33:19.673000

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

--EXEC [sp_KSTC_CheckGetData_Admatic_v2] '2021-06-07'
CREATE PROCEDURE [dbo].[sp_KSTC_CheckGetData_Admatic_v2]
	-- Add the parameters for the stored procedure here
	@NgayThucHien datetime
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	
    -- Insert statements for procedure here
	---------------Nhom Not AdX----------------------
	select 'Not AdX' Nhom,tc.contract_number, DmSanPhamREF, TenSanPham, domain_name, banner_id, ProductUnitName,
	(case when ProductUnitName = 'CPM' then domain_tt_view else domain_tt_click end )SoLuongThucChay_v2, 
	(case when ProductUnitName = 'CPM' then TongViewThucChay else TongClickThucChay end )SoLuongThucChay_v1, 
	SoHopDong,TenWebsite, DmBannerREF
	from (
	select A.*,B.*
	from (
		select contract_number, DmSanPhamREF, TenSanPham, domain_name, banner_id, ProductUnitName, domain_tt_click, domain_tt_view
		from DataThucChay_Admatic_v2 where NgayThucHien = @NgayThucHien
		--and contract_number <> 'HD DEMO'
		and DmSanPhamREF not in (585,821,5133)
		and ProductUnitName not in ('TRUE VIEW')--khong tinh truong hop true view
)A
left join
(
		select  SoHopDong,DmSanPhamREF typeproduct, TenWebsite, DmBannerREF, TongViewThucChay, TongClickThucChay
		from DataThucChay_Admatic where NgayThucHien = @NgayThucHien-- and DmBannerREF =76097 
		--and SoHopDong not in ('HD DEMO')
)B
on A.banner_id = B.DmBannerREF and A.domain_name = B.TenWebsite
where A.contract_number <> B.SoHopDong or A.contract_number is null or B.SoHopDong is null
or A.DmSanPhamREF <> B.typeproduct or A.DmSanPhamREF is null or B.typeproduct is null
or A.domain_name is null or B.TenWebsite is null
or isnull(A.domain_tt_click,0) <> isnull(B.TongClickThucChay ,0)
or isnull(A.domain_tt_view,0) <> isnull(B.TongViewThucChay ,0)
)tc
where (case when ProductUnitName = 'CPM' then isnull(domain_tt_view,0) else isnull(domain_tt_click,0) end ) <> (case when ProductUnitName = 'CPM' then isnull(TongViewThucChay,0) else isnull(TongClickThucChay,0) end )
order by tc.banner_id

---------------Nhom AdX----------------------
	select ' AdX' Nhom,A.*,B.* from (
select contract_number, DmSanPhamREF, TenSanPham, domain_name, banner_id, domain_tt_money, domain_tt_promotion
from DataThucChay_Admatic_v2 where NgayThucHien = @NgayThucHien
--and contract_number <> 'HD DEMO'
and DmSanPhamREF =585
)A
full outer join
(
select  contract_number,DmSanPhamREF, TenSanPham, domain_name, banner_id, domain_tt_money, domain_tt_promotion
from DataThucchay_ADX where NgayThucHien  =@NgayThucHien
--and SoHopDong not in ('HD DEMO')
)B
on A.banner_id = B.banner_id and A.domain_name = B.domain_name
where A.contract_number <> B.contract_number or A.contract_number is null or B.contract_number is null
or A.domain_name is null or B.domain_name is null
or isnull(round(A.domain_tt_money,0),0) <> isnull(round(B.domain_tt_money,0),0)
or isnull(round(A.domain_tt_promotion,0),0) <> isnull(round(B.domain_tt_promotion,0),0)
order by A.banner_id
END

```
