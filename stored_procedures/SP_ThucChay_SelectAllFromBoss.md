# Stored Procedure: `ThucChay_SelectAllFromBoss`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-29 08:23:25.170000
- **Ngày sửa cuối**: 2014-10-14 10:39:52.737000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_SelectAllFromBoss] 
	-- Add the parameters for the stored procedure here
AS
BEGIN
DECLARE @SQLCommand nvarchar(4000)

SELECT 

NgayThucHien,
SoHopDong,
DmBannerREF,
TenMaHopDong,
IsKhuyenMai,

TenPhongBan,
TenBoPhan,
TenNhom,
TenDiaDiemLamViec,
TenDangNhap,
TenNhanVien,

TenKhachHang,

NhanHang,
TenNhomNganh,
TenHinhThucQuangCao,
TenSanPham,
TenWebsite,
SoLuong, 

DonViTinh, 
DonGia, 
ChietKhau,

DonGiaTheoDonVi,
SoLuongThucChay,
ThanhTienThucChayTruocTrietKhau,
GiaTriTrietKhauThucChay,
ThanhTienSauTrietKhauThucChay,
GiaTriHoaHongThucChay,
ThanhTienThucThu

FROM dbo.ThucChay_ViewBizAll

END

--EXEC [ThucChay_SelectAllFromBoss]

```
