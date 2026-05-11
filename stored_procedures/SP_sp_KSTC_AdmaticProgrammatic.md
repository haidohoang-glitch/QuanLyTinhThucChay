# Stored Procedure: `sp_KSTC_AdmaticProgrammatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-11 17:01:35.073000
- **Ngày sửa cuối**: 2021-11-30 13:54:22.813000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[sp_KSTC_AdmaticProgrammatic]
	-- Add the parameters for the stored procedure here
	
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
Declare @month int, @year int
set @month =(SELECT  month(ACTUAL_RUN_DATE) FROM [ASDag2].contract.dbo.CONTRACT_INFO_DATE_RUNNING_REAL)
set @year = (SELECT  year(ACTUAL_RUN_DATE) FROM [ASDag2].contract.dbo.CONTRACT_INFO_DATE_RUNNING_REAL)
select @month 'ThucChayThang', a.SoHopDong, a.HopDongChiTietID, a.TenSanPham, dbo.FormatNumber(a.ThanhTien)ThanhTien, a.ThoiGianSuaPhanBo,
isnull(dbo.FormatNumber(b.ThucChay),0)ThucChay--, round (a.ThanhTien - b.ThucChay,0)Lech 
from( 
select hd.SoHopDong,hd.HopDongID,hdct.HopDongChiTietID, hdct.DmSanPhamREF,hdct.TenSanPham,hdct.ThanhTien 
, Max(hdct.LastModifiedAt)ThoiGianSuaPhanBo
from HopDongChiTiet hdct inner join HopDong hd on hd.HopDongID= hdct.HopDongFK
where hdct.DmLoaiNenTangREF= 9 and hdct.DeletedStatus=0
and hdct.CreatedAt>='2021-04-08'
group by hd.SoHopDong,hdct.HopDongChiTietID, hdct.ThanhTien,hd.HopDongID, hdct.DmSanPhamREF,hdct.TenSanPham
)a 
left join (
select hd.SoHopDong,hdct.HopDongChiTietID, SUM(tcdt.SoLuongThucChay+tcdt.SoLuongThayDoi) SoLuong
,SUM(tcdt.ThanhTienSauTrietKhauThucChay+tcdt.GiaTriThayDoi) ThucChay --, tcdt.NgayThucHien 
from HopDongChiTiet hdct inner join HopDong hd on hd.HopDongID= hdct.HopDongFK
inner join ThucChayDaTinh tcdt on hdct.HopDongChiTietID= tcdt.HopDongChiTietREF
where hdct.DmLoaiNenTangREF= 9 
group by hd.SoHopDong,hdct.HopDongChiTietID--,tcdt.NgayThucHien 
)b
on a.HopDongChiTietID=b.HopDongChiTietID
where 1=1 and (
(a.HopDongChiTietID is null or b.HopDongChiTietID is null)
or round(a.ThanhTien-b.ThucChay,0) <> 0 
or (month(a.ThoiGianSuaPhanBo) = @month and year(a.ThoiGianSuaPhanBo) =@year )
)
---- thuongbuithihoai bổ sung dòng Tổng
union all
select @month 'ThucChayThang', 'Tong' SoHopDong, '' HopDongChiTietID, 'AdmaticProgrammatic' TenSanPham, dbo.FormatNumber(sum(a.ThanhTien))ThanhTien, ''ThoiGianSuaPhanBo,
dbo.FormatNumber(sum(b.ThucChay))ThucChay--, round (a.ThanhTien - b.ThucChay,0)Lech 
from( 
select hd.SoHopDong,hd.HopDongID,hdct.HopDongChiTietID, hdct.DmSanPhamREF,hdct.TenSanPham,hdct.ThanhTien 
, Max(hdct.LastModifiedAt)ThoiGianSuaPhanBo
from HopDongChiTiet hdct inner join HopDong hd on hd.HopDongID= hdct.HopDongFK
where hdct.DmLoaiNenTangREF= 9 and hdct.DeletedStatus=0
and hdct.CreatedAt>='2021-04-08'
group by hd.SoHopDong,hdct.HopDongChiTietID, hdct.ThanhTien,hd.HopDongID, hdct.DmSanPhamREF,hdct.TenSanPham
)a 
left join (
select hd.SoHopDong,hdct.HopDongChiTietID, SUM(tcdt.SoLuongThucChay+tcdt.SoLuongThayDoi) SoLuong
,SUM(tcdt.ThanhTienSauTrietKhauThucChay+tcdt.GiaTriThayDoi) ThucChay --, tcdt.NgayThucHien 
from HopDongChiTiet hdct inner join HopDong hd on hd.HopDongID= hdct.HopDongFK
inner join ThucChayDaTinh tcdt on hdct.HopDongChiTietID= tcdt.HopDongChiTietREF
where hdct.DmLoaiNenTangREF= 9 
group by hd.SoHopDong,hdct.HopDongChiTietID--,tcdt.NgayThucHien 
)b
on a.HopDongChiTietID=b.HopDongChiTietID
where 1=1 and (
(a.HopDongChiTietID is null or b.HopDongChiTietID is null)
or round(a.ThanhTien-b.ThucChay,0) <> 0 
or (month(a.ThoiGianSuaPhanBo) = @month and year(a.ThoiGianSuaPhanBo) =@year )
)

END

```
