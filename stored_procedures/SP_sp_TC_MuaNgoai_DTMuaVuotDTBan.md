# Stored Procedure: `sp_TC_MuaNgoai_DTMuaVuotDTBan`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-05-27 10:49:31.650000
- **Ngày sửa cuối**: 2026-02-02 14:09:20.373000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_TC_MuaNgoai_DTMuaVuotDTBan]
	-- Add the parameters for the stored procedure here

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	select B.iddt, B.MaDuToan,B.SoHopDong,B.phanboid, B.TenSanPham
	, dbo.FormatNumber(M.DuToanMua)DuToanMua
	, dbo.FormatNumber(B.DuToanBan)DuToanBan	
  ,dbo.FormatNumber(M.DuToanMua - B.DuToanBan)Mua_Ban  from (
	select 
	dt.ID iddt, dt.MaDuToan, dt.SoHopDong,dtb.ID,dtb.phanboid, (select TenSanPham from DmSanPham sp where sp.DmSanPhamID = dtb.D_SanPhamREF)TenSanPham,
	dtb.ThanhTien DuToanBan
	--,dtb.*
	from [asdag2].PMS.dbo.B_DuToan_ChiTiet dtb inner join [asdag2].PMS.dbo.B_DuToan dt
	on dtb.B_DuToanREF = dt.ID
	where  dtb.IsDeleted = 0
	and dt.TrangThai = 2
	and (RIGHT (dt.SoHopDong,2)  >='18' or dt.SoHopDong = '')
	and (not dtb.phanboid in (538259,577347,571951,563129 --lỗ, đã được duyệt	
			) or dtb.phanboid is null)
	) B

	inner join 
	(
	select B_DuToan_ChiTiet_REF, sum(SoLuongMua*DonGiaMua*(100-ChietKhauMua)/100) DuToanMua 
	from [asdag2].PMS.dbo.B_DuToan_Chitiet_HopDong 
	where IsDeleted = 0
	group by B_DuToan_ChiTiet_REF

	--select top 1 * from [asd14].PMS.dbo.B_DuToan_Chitiet_HopDong
	
	)M
	on B.ID = M.B_DuToan_ChiTiet_REF
	where M.DuToanMua - B.DuToanBan   >1
	AND NOT B.MaDuToan IN ('DT0550725','DT0110624','DT0030224','DT0050224','DT0371223','DT0820323','DT0211122','DT0231022','DT0840522','DT0020918') 
	---loại bỏ theo mail các Nhưng phân bổ này đều đã được confirm giá mua - bán
	order by B.phanboid desc
	--phanboid = @HopDongChiTietID and-- du toan ban
END

```
