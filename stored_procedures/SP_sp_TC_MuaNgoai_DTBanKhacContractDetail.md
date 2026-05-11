# Stored Procedure: `sp_TC_MuaNgoai_DTBanKhacContractDetail`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-05-28 10:22:40.430000
- **Ngày sửa cuối**: 2026-01-29 09:19:34.647000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_TC_MuaNgoai_DTBanKhacContractDetail]
	-- Add the parameters for the stored procedure here

AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	select DTB.MaDuToan,DTB.SoHopDong,DTB.phanboid,DTB.TenSanPham
	,CT.TenWebsite
	,dbo.FormatNumber(DTB.SoLuongBan) SoLuong_DT
	,dbo.FormatNumber(DTB.SoLuongChay) SoLuong_Chay
	,dbo.FormatNumber(DTB.DonGiaBan) DonGia_DT
	,DTB.ChietKhauBan CK_DT
	,dbo.FormatNumber(DTB.DuToanBan)DuToanBan
	,CT.soluong soluong_hd
	,dbo.FormatNumber(CT.dongia)dongia_hd, CT.chietkhau CK_hd
	,dbo.FormatNumber(CT.thanhtienpbo)thanhtien_hd
	, (case when DTB.SoLuongBan <> CT.soluong then 'x' else '' end )LechSL
	, (case when DTB.DonGiaBan <> CT.dongia then 'x' else '' end )LechDG
	, (case when DTB.ChietKhauBan <> CT.chietkhau then 'x' else '' end )LechCK
	from 

	 (
				select 
				dt.ID iddt, dt.MaDuToan, dt.SoHopDong,dtb.ID,dtb.phanboid, (select TenSanPham from DmSanPham sp where sp.DmSanPhamID = dtb.D_SanPhamREF)TenSanPham,
				dtb.SoLuong SoLuongBan, dtb.DonGia DonGiaBan, dtb.ChietKhau ChietKhauBan,dtb.ThanhTien DuToanBan,
				TCMua.SoluongChay--, TCMua.DonGiaMua
				--,dtb.*
				from ASDAG2.PMS.dbo.B_DuToan_ChiTiet dtb inner join ASDAG2.PMS.dbo.B_DuToan dt
				on dtb.B_DuToanREF = dt.ID
	
						inner join (
						select contract_number SoHopDong, contract_id, PhanBoId,
				sum(SoluongChay)SoluongChay-- , DonGia DonGiaMua
				from ASDAG2.pms.dbo.B_QuanLyThucChay tc 
				inner join ASDAG2.Contract.dbo.contract_details ct on tc.PhanBoId = ct.Id
				inner join [asdag2].Contract.dbo.contracts c on ct.contract_id = c.Id
				where tc. IsDeleted= 0 and TrangThai in (4,1,2)
				and c.[contract_Year] >='2019'
				group by contract_number, contract_id, PhanBoId
				)TCMua on TCMua.PhanBoId = dtb.phanboid

				where  dtb.IsDeleted = 0
				and dt.TrangThai = 2
				and (RIGHT (dt.SoHopDong,2)  >='18' or dt.SoHopDong = '')
				and (not dtb.phanboid in (538259,577347,571951 --lỗ, đã được duyệt	
						) or dtb.phanboid is null)
	--select top 1 * from [asdag2].PMS.dbo.B_DuToan_ChiTiet
	)DTB
	inner join
	(
	select HopDongFK,HopDongChiTietID,TenWebsite,DmSanPhamREF,soluong,dongia, chietkhau, ThanhTien thanhtienpbo, GhiChu
	from HopDongChiTiet ct
	where ct.DeletedStatus = 0
	
	)CT
	on DTB.PhanBoId = CT.HopDongChiTietID
	where abs(DTB.DuToanBan - ct.thanhtienpbo) > 1
	order by DTB.phanboid desc
END

```
