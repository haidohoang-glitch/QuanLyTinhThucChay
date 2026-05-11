# Stored Procedure: `sp_TC_MuaNgoai_TCMuaVuotDTMua`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-05-27 13:55:31.980000
- **Ngày sửa cuối**: 2026-01-29 09:50:25.770000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_TC_MuaNgoai_TCMuaVuotDTMua]
	-- Add the parameters for the stored procedure here

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	select TC.SoHopDong,TC.PhanBoId, TC.TenSanPham,
	dbo.FormatNumber(TC.TCMua)ThucChayMua,dbo.FormatNumber(Mua.DuToanMua)DuToanMua, dbo.FormatNumber(TC.TCMua - Mua.DuToanMua)Vuot from 

	 (
	select contract_number SoHopDong, contract_id, PhanBoId,(select TenSanPham from DmSanPham sp where sp.DmSanPhamID = ct.product_id) TenSanPham , 
	sum(SoluongChay*DonGia*(100-ChietKhauMua)/100) TCMua
	from [asdag2].pms.dbo.B_QuanLyThucChay tc 
	inner join [asdag2].Contract.dbo.contract_details ct on tc.PhanBoId = ct.Id
	inner join [asdag2].Contract.dbo.contracts c on ct.contract_id = c.Id
	where tc. IsDeleted= 0 and TrangThai in (4,1,2)
	and c.[contract_Year] >='2019'
	and ct.id not in (598114 --pbo km
	)--hd 
	group by contract_number,contract_id, PhanBoId,product_id
	--select top 1 * from [asd14].Contract.dbo.contracts
	)TC
	inner join
	(
	select dtb.phanboid, sum(SoLuongMua*DonGiaMua*(100-ChietKhauMua)/100) DuToanMua 
	from [asdag2].PMS.dbo.B_DuToan_Chitiet_HopDong dtm inner join 
	[asdag2].PMS.dbo.B_DuToan_ChiTiet dtb on dtm.B_DuToan_ChiTiet_REF = dtb.ID
	where dtm.IsDeleted = 0
	and dtb.phanboid not in (598114--pbo km
	)
	group by dtb.phanboid
	)Mua
	on TC.PhanBoId = Mua.phanboid
	where (TC.TCMua - Mua.DuToanMua) > 10
	order by TC.phanboid desc
END

```
