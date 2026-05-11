# Function: `BaoCaoThongTinTongHop_FilterAll`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-12-04 09:39:50.917000
- **Ngày sửa cuối**: 2014-10-14 10:39:38.020000

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

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION BaoCaoThongTinTongHop_FilterAll 
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
	,@DmNghanhHangREFList nvarchar(4000)
	,@DmNhanHangREFList nvarchar(4000)		
	--Thông tin sản phẩm
	,@DmLoaiSanPhamREFList nvarchar(4000)
	,@DmSanPhamREFList nvarchar(4000)
	--Thông tin Website
	,@DmNhomWebsiteREFList nvarchar(4000)
	,@DmWebsiteREFList nvarchar(4000)		
)
RETURNS nvarchar(4000)
AS
BEGIN

	Declare @FilterTongHop nvarchar(4000)
	
	--Thời gian thực hiện
	DECLARE @TimeFilter nvarchar(100), @DauNhay nvarchar(5)
	
	set @TimeFilter = ' 1=1 '
	
	if(@ThoiGianBatDau is not null and @ThoiGianKetThuc is not null)
	Begin		
		set @DauNhay = ''''
		
		set @ThoiGianBatDau = convert(date,@ThoiGianBatDau)
		
		set @ThoiGianKetThuc = convert(date,@ThoiGianKetThuc)
			
		Set @TimeFilter = 
		CASE 
		--NgayKyHopDong
		WHEN @TypeDate = 1 THEN 'convert(date,NgayKyHopDong)' 
		--ThucChayDenNgay	
		WHEN @TypeDate = 2 THEN 'convert(date,ThucChayDenNgay)' 
		--HoaDonDenNgay
		WHEN @TypeDate = 3 THEN 'convert(date,HoaDonDenNgay)'
		--TienDaThanhToanDenNgay
		WHEN @TypeDate = 4 THEN 'convert(date,TienDaThanhToanDenNgay)'
		END 
		
		Set @TimeFilter = @TimeFilter + ' between ' + @DauNhay + Convert(nvarchar(50),@ThoiGianBatDau) + @DauNhay + ' and ' + @DauNhay + Convert(nvarchar(50),@ThoiGianKetThuc) + @DauNhay		
	end 
		
	
	--Thông tin Hợp đồng
	DECLARE @ThongTinHopDongFilter nvarchar(4000)
	
	set @ThongTinHopDongFilter = ' 1=1 '

	if(@TrangThaiHopDong is not null and @TrangThaiHopDong >=1)
		set @ThongTinHopDongFilter = @ThongTinHopDongFilter + ' and ' + 		
								CASE 
									WHEN @TrangThaiHopDong = 1 THEN ' IsBanCung = 1'
									WHEN @TrangThaiHopDong = 2 THEN ' IsBanCung <> 1'
									WHEN @TrangThaiHopDong = 3 THEN ' NgayNhanBanFax is not null'
									WHEN @TrangThaiHopDong = 4 THEN ' NgayNhanBanFax is null'
									WHEN @TrangThaiHopDong = 5 THEN ' IsGiayPhep = 1'
									WHEN @TrangThaiHopDong = 6 THEN ' IsGiayPhep <> 1'									
								END;	
	
	if(@TrangThaiThucChay is not null and @TrangThaiThucChay >=0)
		set @ThongTinHopDongFilter = @ThongTinHopDongFilter + ' and ' + 'TrangThaiHopDong = ' + Convert(nvarchar(50),@TrangThaiThucChay)	
	
	if(@TenMaHopDongList is not null and @TenMaHopDongList <> '')
		set @ThongTinHopDongFilter = @ThongTinHopDongFilter + ' and ' + 'TenMaHopDong in (' + @TenMaHopDongList + ')'
	
	if(@SoHopDongList is not null and @SoHopDongList <> '')
		set @ThongTinHopDongFilter = @ThongTinHopDongFilter + ' and ' + 'SoHopDong in (' + @SoHopDongList + ')'	


	--Thông tin về đội bán
	DECLARE @DoiBanFilter nvarchar(4000)
	
	set @DoiBanFilter = ' 1=1 '

	if(@DmPhongBanREF >0)
		set @DoiBanFilter = @DoiBanFilter + ' and DmPhongBanREF = ' + Convert(nvarchar(50),@DmPhongBanREF)	
	else
		if(@DmBoPhanREF >0)
			set @DoiBanFilter = @DoiBanFilter + ' and DmBoPhanREF = ' + Convert(nvarchar(50),@DmBoPhanREF)
		else
			if(@DmNhomLamViecREF >0)
				set @DoiBanFilter = @DoiBanFilter + ' and DmNhomLamViecREF = ' + Convert(nvarchar(50),@DmNhomLamViecREF)	
										
	if(@SysNhanVienREFList is not null and @SysNhanVienREFList <> '')
		set @DoiBanFilter = @DoiBanFilter + ' and ' + 'SysNhanVienREF in (' + @SysNhanVienREFList + ')'


	--Thông tin về khách hàng
	Declare @KhachHangFilter nvarchar(4000)
	set @KhachHangFilter = ' 1=1 '
	
	if(@DmDatNuocREF >0)
		set @KhachHangFilter = @KhachHangFilter + ' and DmDatNuocREF = ' + Convert(nvarchar(50),@DmDatNuocREF)	
	else
		if(@DmBoPhanREF >0)
			set @KhachHangFilter = @KhachHangFilter + ' and DmTinhThanhPhoREF = ' + Convert(nvarchar(50),@DmTinhThanhPhoREF)
		else
			if(@DmNhomLamViecREF >0)
				set @KhachHangFilter = @KhachHangFilter + ' and DmQuanHuyenREF = ' + Convert(nvarchar(50),@DmQuanHuyenREF)	
										
	if(@DmNghanhHangREFList is not null and @DmNghanhHangREFList <> '')
		set @KhachHangFilter = @KhachHangFilter + ' and ' + 'DmNghanhHangREF in (' + @DmNghanhHangREFList + ')'	

	if(@DmNhanHangREFList is not null and @DmNhanHangREFList <> '')
		set @KhachHangFilter = @KhachHangFilter + ' and ' + 'DmNhanHangREF in (' + @DmNhanHangREFList + ')'	
	
	if(@DmKhachHangREFList is not null and @DmKhachHangREFList <> '')
		set @KhachHangFilter = @KhachHangFilter + ' and ' + 'DmKhachHangREF in (' + @DmKhachHangREFList + ')'		
		
	
	set @FilterTongHop = @TimeFilter + ' and ' + @DoiBanFilter + ' and ' + @ThongTinHopDongFilter + ' and ' + @KhachHangFilter 
	

	Declare @FilterChiTiet nvarchar(4000)
	set @FilterChiTiet = '1=1'
	
	--Thông tin sản phẩm
	Declare @SanPhamFilter nvarchar(4000)
	set @SanPhamFilter = '1=1'
	
	if(@DmLoaiSanPhamREFList is not null and @DmLoaiSanPhamREFList <> '')
		set @SanPhamFilter = @SanPhamFilter + ' and ' + 'DmLoaiSanPhamREF in (' + @DmLoaiSanPhamREFList + ')'	
	
	if(@DmSanPhamREFList is not null and @DmSanPhamREFList <> '')
		set @SanPhamFilter = @SanPhamFilter + ' and ' + 'DmSanPhamREF in (' + @DmSanPhamREFList + ')'		
		
	--Thông tin Website
	Declare @WebsiteFilter nvarchar(4000)
	set @WebsiteFilter = '1=1'
	
	if(@DmNhomWebsiteREFList is not null and @DmNhomWebsiteREFList <> '')
		set @WebsiteFilter = @WebsiteFilter + ' and ' + 'DmNhomWebsiteREF in (' + @DmNhomWebsiteREFList + ')'	
	
	if(@DmWebsiteREFList is not null and @DmWebsiteREFList <> '')
		set @WebsiteFilter = @WebsiteFilter + ' and ' + 'DmWebsiteREF in (' + @DmWebsiteREFList + ')'	

	
	set @FilterChiTiet = @SanPhamFilter + ' and ' + @WebsiteFilter	

	Declare @FilterAll nvarchar(4000)
	
	set @FilterAll = @FilterTongHop + ' and ' + @FilterChiTiet
	-- Return the result of the function
	RETURN @FilterAll

END

```
