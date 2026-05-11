# Stored Procedure: `GetBaoCaoThongTinTongHop`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-12-02 15:31:41.487000
- **Ngày sửa cuối**: 2014-11-19 12:16:58.113000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
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
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@MaxRecords` | `int(4)` | Yes |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[GetBaoCaoThongTinTongHop]
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
	--#Thông tin chi tiết Hợp đồng#---
	--Nhãn hàng, nghành hàng
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
	--Thông tin phân trang
	,@PageIndex Int
	,@RecordCount Int
	,@MaxRecords int output
AS
BEGIN

	
	Declare 
	@SQLCommand nvarchar(4000)
	,@SelectChiTiet nvarchar(4000)
	,@SelectTongHop nvarchar(4000)
	,@FilterChiTiet nvarchar(4000)
	,@ThoiGianColumn VARCHAR(50)
	,@TenDangNhapColumn VARCHAR(50)
	,@DmSanPhamREFColumn VARCHAR(50)
	,@DmWebsiteREFColumn VARCHAR(50)
	
	set @ThoiGianColumn = 'NgayKyHopDong'
	set @TenDangNhapColumn = 'TenDangNhap'	
	set @DmSanPhamREFColumn = 'DmSanPhamREF'
	set @DmWebsiteREFColumn = 'DmWebsiteREF'
	
	set @FilterChiTiet = dbo.BaoCaoThongTinTongHop_FilterChiTiet(
																--Nhãn hàng, nghành hàng
																 @DmNghanhHangREFList 
																,@DmNhanHangREFList 
																--Thông tin sản phẩm
																,@DmLoaiSanPhamREFList 
																,@DmSanPhamREFList 
																--Thông tin Website
																,@DmNhomWebsiteREFList 
																,@DmWebsiteREFList 
																)	
																														
	set @FilterChiTiet = @FilterChiTiet + ' and ' + dbo.GetSecurityWebsiteProduct(
																		--Thời gian thực hiện
																		 @ThoiGianBatDau 
																		,@ThoiGianKetThuc	
																		,@TenDangNhap
																		,@ThoiGianColumn
																		,@TenDangNhapColumn
																		,@DmSanPhamREFColumn
																		,@DmWebsiteREFColumn
																		)														
	
	set @SelectChiTiet = dbo.BaoCaoThongTinTongHop_SelectChiTiet()
	

	set @SelectTongHop = dbo.BaoCaoThongTinTongHop_SelectTongHop(
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
																--Thông tin bảo mật hệ thống
																,@TenDangNhap 	
																,@ThoiGianColumn
																,@TenDangNhapColumn
																)
	
	
	
	--Xử lý phân trang
	declare @StartIndex Int, @i Int, @PageCount Int, @ApproximatedNumber float, @PageNumberCommand nvarchar(4000), @MaxRecordsByPage int	
	set @ApproximatedNumber=0.49999
	set @i=1
	set @PageNumberCommand = 'select @MaxRecords=count(*) from ('+ @SelectTongHop+ ') T'	
	
	EXEC sp_executesql @PageNumberCommand, N'@MaxRecords int output', @MaxRecords output
	PRINT @MaxRecords
	PRINT @PageNumberCommand
	
	set @PageCount = round(convert(float,@MaxRecords)/@RecordCount+@ApproximatedNumber,0)
	SET @StartIndex = (@PageIndex - 1)*@RecordCount + 1
	Set @MaxRecordsByPage = @PageIndex*@RecordCount	
	
	--Phân trang cho bảng HopDongTongHop	
	if(@PageCount>=@PageIndex)
		set @SelectTongHop = 	'SELECT * FROM 
		(SELECT *, ROW_NUMBER() OVER(ORDER BY '+@ThoiGianColumn+' DeSC) AS rownum from ('+@SelectTongHop +') T  ) as VitualTable '+
		'WHERE rownum between '+ Convert(nvarchar(50),@StartIndex) + ' and ' + Convert(nvarchar(50),@MaxRecordsByPage)
	else
		set @SelectTongHop = 'select * from ('+@SelectTongHop + ') T'
	
	--Kết quả SQL Command
	set @SQLCommand = 'select X.*,' + @SelectChiTiet + ' from (' + @SelectTongHop + ')X ' 
	+ 	
	'	
	INNER JOIN dbo.ThucChayTheoDoiHopDongChiTiet hdct ON X.HopDongID = hdct.HopDongFK
	INNER JOIN DmLoaiSanPham dmlsp ON hdct.DmLoaiREF = dmlsp.DmLoaiSanPhamID
	' 
	+ ' where ' + @FilterChiTiet + ' order by SoHopDong'

	
	exec(@SQLCommand)	
END

```
