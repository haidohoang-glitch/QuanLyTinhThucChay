# Stored Procedure: `BaoCaoThongTinTongHop_SelectTongHop_sp`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-12-04 12:45:54.593000
- **Ngày sửa cuối**: 2014-10-14 10:40:04.120000

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
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE procedure [dbo].[BaoCaoThongTinTongHop_SelectTongHop_sp]
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
	--Thông tin bảo mật hệ thống
	,@TenDangNhap nvarchar(50)	
	--Thông tin phân trang
	,@PageIndex Int
	,@RecordCount Int	
)
AS
Begin
	Declare @SelectTongHop nvarchar(4000)
	,@FilterTongHop nvarchar(4000)
	,@FilterSecurity nvarchar(4000)
	,@SQLCommand nvarchar(4000)
	,@ThoiGianColumn VARCHAR(50)
	,@TenDangNhapColumn VARCHAR(50)
	
	set @ThoiGianColumn = 'NgayKyHopDong'
	set @TenDangNhapColumn = 'TenDangNhap'
	
	Declare @TableTemp TABLE (
						SelectTongHop [nvarchar](4000)  NULL,
						MaxRecords int NULL
	)	
	
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
																)
	
	set @SelectTongHop = '
	
	SELECT 	
	---------------------------------Thông tin tổng hợp----------------------------------	
	--Thông tin chung hợp đồng	 
	hdth.TenMaHopDong
	,hdth.SoHopDong
	,hdth.TenNhanVien
	,hdth.TenPhongBan
	,hdth.TenBoPhan
	,hdth.TenNhom
	,hdth.TenKhachHang	
	--Thông tin về thời gian
	,hdth.NgayKyHopDong
	,hdth.NgayDanhSoHopDong	
	,hdth.NgayNhanHopDongBanCung
	,hdth.NgayNhanBanFax
	,hdth.ThucChayDenNgay	
	,hdth.HoaDonDenNgay
	,hdth.TienDaThanhToanDenNgay
	
	--Trạng thái hợp đồng
	,hdth.IsGiayPhep	
	,hdth.IsBanCung
	--Trạng Thái Thực chạy: -1: Không xác định,0: Chưa chạy, 1: Đang chạy, 2: Chạy xong
	,hdth.TrangThaiHopDong 	
	--Thông tin các doanh số theo hợp đồng
	,hdth.TongTienKyHopDong
	,hdth.TongTienHaiDauHopDong			
	,hdth.TongTienThucChay
	,hdth.TongTienChuaChay		
	,hdth.TongTienXuatHoaDon	
	,hdth.TongTienDaThanhToan	
	,hdth.CongNo
		
	FROM HopDongTongHop hdth
	'
		 
	set @SQLCommand = @SelectTongHop + ' where ' + @FilterSecurity + ' and ' + @FilterTongHop 
	
	
	--Xử lý phân trang
	declare @StartIndex Int, @MaxRecords Int, @i Int, @PageCount Int, @ApproximatedNumber float, @PageNumberCommand nvarchar(4000)	
	set @ApproximatedNumber=0.49999
	set @i=1
	set @PageNumberCommand = 'select @MaxRecords=count(*) from ('+ @SQLCommand+ ') T'	
	
	EXEC sp_executesql @PageNumberCommand, N'@MaxRecords int output', @MaxRecords output
	
	set @PageCount = round(convert(float,@MaxRecords)/@RecordCount+@ApproximatedNumber,0)
	SET @StartIndex = (@PageIndex - 1)*@RecordCount + 1
	Set @MaxRecords = @PageIndex*@RecordCount	
	
	if(@PageCount>=@PageIndex)
		set @SQLCommand = 	'SELECT * FROM 
		(SELECT *, ROW_NUMBER() OVER(ORDER BY '+@ThoiGianColumn+' DeSC) AS rownum from ('+@SQLCommand +') T  ) as VitualTable '+
		'WHERE rownum between '+ Convert(nvarchar(50),@StartIndex) + ' and ' + Convert(nvarchar(50),@MaxRecords)
	else
		set @SQLCommand = 'select * from ('+@SQLCommand + ') T'
		
	--print @SQLCommand
	
	--exec(@SQLCommand)
		
	Insert into @TableTemp select @SQLCommand, @MaxRecords
	
	select * from @TableTemp
End

```
