# Function: `BaoCaoThongTinTongHop_SelectChiTiet`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-12-04 09:15:10.977000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.923000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[BaoCaoThongTinTongHop_SelectChiTiet] 
(
	
)
RETURNS nvarchar(4000)
AS
BEGIN
	Declare @SelectChiTiet nvarchar(4000)
	
	set @SelectChiTiet = '	
	---------------------------------Thông tin chi tiết----------------------------------
	--Thông tin chung chi tiết
	 hdct.NhanHang
	,hdct.TenNhomNganh
	,dmlsp.TenLoaiSanPham AS HinhThucQuangCao
	,hdct.TenSanPham
	,hdct.TenNhomWebsite AS Tag
	,hdct.TenWebsite
	,hdct.TenChuyenMuc
	,hdct.TenLoaiBanner
	,hdct.TenViTri	
	--Thông tin Số lượng & Đơn giá
	,hdct.ThoiGian
	,hdct.SoLuong as SoLuong
	,hdct.DonViTinh
	,hdct.DonGia
	--Thông tin chiết khấu
	,hdct.ChietKhau
	,hdct.GiamGia as ThanhTienChietKhau
	,hdct.TiLeTuVan
	,hdct.ChiPhiTuVan
	,hdct.IsKhuyenMai
	--Thông tin thành tiền
	,hdct.ThanhTien
	--Thông tin thực chạy
	,hdct.DotChayHopDongChiTiet
	,hdct.NgayDaChay
	,hdct.ThucChayDenNgay
	,hdct.SoLuongDaChay
	,hdct.ThanhTienDaChay
	,hdct.SoLuongChuaChay	
	,hdct.ThanhTienChuaChay
	--Trạng Thái Thực chạy: -1: Không xác định,0: Chưa chạy, 1: Đang chạy, 2: Chạy xong
	,hdct.TrangThaiHopDongChiTietThucChay	
	'
	
	
	-- Return the result of the function
	RETURN @SelectChiTiet

END

```
