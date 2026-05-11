# Stored Procedure: `sp_ListHopDongNativeOnImageChayVuotChuaDuThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-03-17 11:07:39.150000
- **Ngày sửa cuối**: 2021-03-25 09:52:26.607000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_ListHopDongNativeOnImageChayVuotChuaDuThucChay]
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
	declare @NgayThucHien datetime
	set @NgayThucHien = convert(date,DATEADD(day,-1,getdate()))
	--select @NgayThucHien
	EXEC CheckThucChayVuotHopDong_TableTCDT    @NgayThucHien,  @NgayThucHien
    -- Insert statements for procedure here
	
select (A.SoHopDong + ' - ' + A.TenSanPham) SoHopDong , A.NhanHang,A.HopDongID, A.HopDongChiTietID,
A.SoLuong,A.DonViTinh,
--A.DonGia, A.ChietKhau,  
dbo.FormatNumber(A.ThanhTien) ThanhTien,
dbo.FormatNumber(B.sltc)sltc, 
dbo.FormatNumber(B.tcdt)tcdt, 
dbo.FormatNumber(A.ThanhTien - B.tcdt)ThucChayConThieu from (
select SoHopDong,hdct.NhanHang,HopDongID, HopDongChiTietID, TenSanPham, SoLuong,DonViTinh,
DonGia,ChietKhau, ThanhTien,
(case when DonViTinh = 'CPM' then SoLuong *1000 else SoLuong end) SoLuongQuyDoi, 
(case when DonViTinh = 'CPM' then 'VIEW'
 when DonViTinh = 'CPC' then 'CLICK'
else 'True View' end) DonViQuyDoi
from hopdongchitiet hdct inner join HopDong hd on hd.HopDongID = hdct.HopDongFK
where DmLoaiREF <> 42 and DonViTinhREF <> 10 and DmSanPhamREF in (821,5133)
and DonViTinh in ('CPM','CPC','True View')
and hdct.DeletedStatus = 0
and ChietKhau <> 100
)A

left join 
(
/*
select SoHopDong, HopDongChiTietREF,sum(SoLuongThucChay+SoLuongThayDoi)sltc,
round(sum(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi),0)tcdt
from ThucChayDaTinh where  DmHinhThucQuangCao <> 42  and DmSanPhamREF in (821,5133) 
--and SoHopDong = 'QC0630920'
group by SoHopDong, HopDongChiTietREF
*/
select tc.SoHopDong, tc.HopDongChiTietID, sum(tc.sltc)sltc,sum(tc.tcdt)tcdt from (
select SoHopDong, HopDongChiTietID,( case when DonViTinh = 'VIEW' then sum(SoLuongThucChay)/1000 else sum(SoLuongThucChay) end)sltc,
round(sum(ThanhTienThucChay),0)tcdt
from KS_ThucChay_TCDT where  DmHinhThucQuangCao <> 42  and DmSanPhamREF in (821,5133) 
--and SoHopDong = 'QC0630920'
group by SoHopDong, HopDongChiTietID,DonViTinh
)tc
group by tc.SoHopDong, tc.HopDongChiTietID
)B
on A.HopDongChiTietID =B.HopDongChiTietID
where round(A.ThanhTien - B.tcdt,0) > 1
and A.SoLuongQuyDoi <= B.sltc
order by A.TenSanPham, A.HopDongID desc,A.HopDongChiTietID

END

```
