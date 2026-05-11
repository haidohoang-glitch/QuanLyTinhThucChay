# Stored Procedure: `sp_KSTC_Admatic_ChayChuaTreo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-08 14:53:37.633000
- **Ngày sửa cuối**: 2021-12-28 15:38:55.437000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_KSTC_Admatic_ChayChuaTreo] 
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	select distinct A.SoHopdong,A.NhanHopDong, A.DmBannerREF, A.DmSanPhamREF, A.TenSanPham from (
select  tc.SoHopdong,hd.NhanHopDong, convert(nvarchar(50),DmBannerREF)DmBannerREF,dmsanphamref, TenSanpham 
from ThucChay tc left join HopDong hd on tc.SoHopDong = hd.SoHopDong where
1=1  and NgayThuchien >='2021-01-01' 
and  tc.CreatedBy = 'From API_Admatic'  
and DmBannerREF not in (79603,79581,80026,80124, 80125, 80236, 80237, 80490, 80491)--pbo Admatic programmatic
and 	 tc.SoHopdong not in ('hd_demo', '', 'HD DEMO', 'hd_king_test2','HD SELFSERVE','TEST','HD TEST','DEMO')
and 	 tc.SoHopdong not like '%demo%'
and 	 tc.SoHopdong not like '%test%'
union all 
select tc.SoHopdong,hd.NhanHopDong, DmBannerID DmBannerREF, dmsanphamref, TenSanpham 
from ThucChay_ThanhTien_Admatic tc left join HopDong hd on tc.SoHopDong = hd.SoHopDong where
1=1  and NgayThuchien >='2021-01-01' 
and 	 tc.SoHopdong not in ('hd_demo', '', 'HD DEMO', 'hd_king_test2','HD SELFSERVE','TEST','HD TEST','DEMO')
and 	 tc.SoHopdong not like '%demo%'
and 	 tc.SoHopdong not like '%test%'
and DmBannerID not in (79603,79581,80026,80124, 80125, 80236, 80237, 80490, 80491)  -- pbo Admatic programmatic
)A 
full outer join 
(select distinct convert(nvarchar(50),Banner_id)  DmBannerREF
 from [asdag2].thuctreo.dbo.thuctreo where 1=1 
and  product_formality_id = 42 
and Deleted_Status = 0 and contract_detail_id not in (0,-1)

--select top 1 * from [asd14].thuctreo.dbo.thuctreo
)B on A.DmBannerREF = B.DmBannerREF
where B.DmBannerREF is null 
order by A.SoHopDong
END

```
