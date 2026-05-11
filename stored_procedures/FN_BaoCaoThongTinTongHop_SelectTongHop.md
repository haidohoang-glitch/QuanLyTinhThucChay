# Function: `BaoCaoThongTinTongHop_SelectTongHop`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-12-04 18:26:55.510000
- **Ngày sửa cuối**: 2014-10-14 10:39:37.897000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@ThoiGianBatDau` | `datetime(8)` | No |
| `@ThoiGianKetThuc` | `datetime(8)` | No |
| `@TypeDate` | `int(4)` | No |
| `@TenMaHopDongList` | `nvarchar(8000)` | No |
| `@SoHopDongList` | `nvarchar(8000)` | No |
| `@TrangThaiHopDong` | `int(4)` | No |
| `@TrangThaiThucChay` | `int(4)` | No |
| `@DmPhongBanREF` | `int(4)` | No |
| `@DmBoPhanREF` | `int(4)` | No |
| `@DmNhomLamViecREF` | `int(4)` | No |
| `@SysNhanVienREFList` | `nvarchar(8000)` | No |
| `@DmKhachHangREFList` | `nvarchar(8000)` | No |
| `@DmDatNuocREF` | `int(4)` | No |
| `@DmTinhThanhPhoREF` | `int(4)` | No |
| `@DmQuanHuyenREF` | `int(4)` | No |
| `@DmNghanhHangREFList` | `nvarchar(8000)` | No |
| `@DmNhanHangREFList` | `nvarchar(8000)` | No |
| `@DmLoaiSanPhamREFList` | `nvarchar(8000)` | No |
| `@DmSanPhamREFList` | `nvarchar(8000)` | No |
| `@DmNhomWebsiteREFList` | `nvarchar(8000)` | No |
| `@DmWebsiteREFList` | `nvarchar(8000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@ThoiGianColumn` | `varchar(50)` | No |
| `@TenDangNhapColumn` | `varchar(50)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[BaoCaoThongTinTongHop_SelectTongHop]
(
	--Thời gian thực hiện
	 @ThoiGianBatDau DATETIME
	,@ThoiGianKetThuc DATETIME
	,@TypeDate int
	--Thông tin Hợp đồng
	,@TenMaHopDongList nvarchar(4000)
	,@SoHopDongList nvarchar(4000)	
	,@TrangThaiHopDong int --Bản cứng, bản fax, giấy phép
	,@TrangThaiThucChay int --Đã chạy, chưa chạy, chạy xong 
	--Thông tin về đội bán
	,@DmPhongBanREF int
	,@DmBoPhanREF int
	,@DmNhomLamViecREF int
	,@SysNhanVienREFList nvarchar(4000) 
	--Thông tin về khách hàng
	,@DmKhachHangREFList nvarchar(4000)
	,@DmDatNuocREF int
	,@DmTinhThanhPhoREF int
	,@DmQuanHuyenREF int
	--#Thông tin chi tiết Hợp đồng#
	,@DmNghanhHangREFList nvarchar(4000)
	,@DmNhanHangREFList nvarchar(4000)
	--Thông tin sản phẩm
	,@DmLoaiSanPhamREFList nvarchar(4000)
	,@DmSanPhamREFList nvarchar(4000)
	--Thông tin Website
	,@DmNhomWebsiteREFList nvarchar(4000)
	,@DmWebsiteREFList nvarchar(4000)	
	--Thông tin bảo mật hệ thống
	,@TenDangNhap nvarchar(50)	
	,@ThoiGianColumn VARCHAR(50)
	,@TenDangNhapColumn VARCHAR(50)	
)
RETURNS nvarchar(4000)
AS
BEGIN

	Declare @SelectTongHop nvarchar(4000)
	,@FilterTongHop nvarchar(4000)
	,@FilterSecurity nvarchar(4000)
	,@SQLCommand nvarchar(4000)

	
	set @FilterSecurity = dbo.GetSecurityDataByTenDangNhap(@ThoiGianBatDau,@ThoiGianKetThuc,@TenDangNhap,@ThoiGianColumn,@TenDangNhapColumn)
	
	--print @FilterSecurity
		
	set @FilterTongHop = dbo.BaoCaoThongTinTongHop_FilterTongHop(
																--Thời gian thực hiện
																 @ThoiGianBatDau 
																,@ThoiGianKetThuc 
																,@TypeDate 
																--Thông tin Hợp đồng
																,@TenMaHopDongList 
																,@SoHopDongList 	
																,@TrangThaiHopDong  --Bản cứng, bản fax, giấy phép
																,@TrangThaiThucChay  --Đã chạy, chưa chạy, chạy xong 
																--Thông tin về đội bán
																,@DmPhongBanREF 
																,@DmBoPhanREF 
																,@DmNhomLamViecREF 
																,@SysNhanVienREFList  
																--Thông tin về khách hàng
																,@DmKhachHangREFList 
																,@DmDatNuocREF 
																,@DmTinhThanhPhoREF 
																,@DmQuanHuyenREF 
																--#Thông tin chi tiết Hợp đồng#
																,@DmNghanhHangREFList 
																,@DmNhanHangREFList 
																--Thông tin sản phẩm
																,@DmLoaiSanPhamREFList 
																,@DmSanPhamREFList
																--Thông tin Website
																,@DmNhomWebsiteREFList 
																,@DmWebsiteREFList 																															
																)
	
	set @SelectTongHop = '
	
	SELECT 	
	---------------------------------Thông tin tổng hợp----------------------------------	
	--Thông tin chung hợp đồng	
	hdth.HopDongID --Cột này ko hiển thị
	--,hdth.TenMaHopDong,
	,hdth.SoHopDong	
	--Thông tin về sale	 
	,hdth.TenNhanVien
	,hdth.TenPhongBan  
	,hdth.TenBoPhan
	,hdth.TenNhom
	,hdth.TenKhachHang	
	--Thông tin về thời gian -- Tất cả cột này ẩn
	,hdth.NgayKyHopDong 
	,hdth.ThucChayDenNgay
	,hdth.HoaDonDenNgay
	,hdth.TienDaThanhToanDenNgay	
	/*	
	,hdth.NgayDanhSoHopDong	
	,hdth.NgayNhanHopDongBanCung
	,hdth.NgayNhanBanFax		
	*/	
	--Thông tin các doanh số theo hợp đồng
	,hdth.TongTienKyHopDong
	--,hdth.TongTienHaiDauHopDong			
	,hdth.TongTienThucChay
	--,hdth.TongTienChuaChay		
	,hdth.TongTienXuatHoaDon	
	,hdth.TongTienDaThanhToan	
	,hdth.CongNo
	--Trạng thái hợp đồng
	,hdth.IsGiayPhep	
	,hdth.IsBanCung
	--Trạng Thái Thực chạy: -1: Không xác định,0: Chưa chạy, 1: Đang chạy, 2: Chạy xong
	,hdth.TrangThaiHopDong 		
	FROM HopDongTongHop hdth
	'
		 
	set @SQLCommand = @SelectTongHop + ' where ' + @FilterSecurity + ' and ' + @FilterTongHop 

	-- Return the result of the function
	RETURN @SQLCommand

END

```
