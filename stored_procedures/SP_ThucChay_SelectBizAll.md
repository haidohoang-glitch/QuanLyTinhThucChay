# Stored Procedure: `ThucChay_SelectBizAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-29 09:45:26.397000
- **Ngày sửa cuối**: 2014-10-14 10:39:52.703000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_SelectBizAll] 
	-- Add the parameters for the stored procedure here
AS
BEGIN

SELECT 

NgayThucHien,
SoHopDong,
DmBannerREF,
TenMaHopDong,
IsKhuyenMai,

DmPhongBanREF,
TenPhongBan,
DmBoPhanREF,
TenBoPhan,
DmNhomLamViecREF,
TenNhom,
TenDiaDiemLamViec,
TenDangNhap,
TenNhanVien,

TenKhachHang,

NhanHang,
TenNhomNganh,
TenHinhThucQuangCao,
DmSanPhamREF, 
TenSanPham,
DmWebsiteREF
TenWebsite,
SoLuong, 

DonViTinh, 
DonGia, 
ChietKhau,
GiaTriThayDoi,
DonGiaTheoDonVi,
SoLuongThucChay,
ThanhTienThucChayTruocTrietKhau,
GiaTriTrietKhauThucChay,
ThanhTienSauTrietKhauThucChay,
GiaTriHoaHongThucChay,
ThanhTienThucThu


FROM dbo.ThucChay_ViewAll


END

--EXEC [ThucChay_SelectAllFromBoss]

```
