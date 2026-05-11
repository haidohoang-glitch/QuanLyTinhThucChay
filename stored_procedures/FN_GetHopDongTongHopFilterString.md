# Function: `GetHopDongTongHopFilterString`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-10-02 15:10:01.680000
- **Ngày sửa cuối**: 2014-10-14 10:39:36.257000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@HopDongIDList` | `nvarchar(8000)` | No |
| `@NhanHopDongList` | `nvarchar(8000)` | No |
| `@TypeSearchDate` | `nvarchar(100)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmKhachHangREFList` | `int(4)` | No |
| `@NganhHangList` | `nvarchar(8000)` | No |
| `@TrangThaiHopDong` | `int(4)` | No |
| `@IsBanCung` | `int(4)` | No |
| `@TrangThaiThucChayHopDong` | `int(4)` | No |
| `@DmPhongBanREFList` | `nvarchar(8000)` | No |
| `@DmBoPhanREFList` | `nvarchar(8000)` | No |
| `@DmNhomLamViecREFList` | `nvarchar(8000)` | No |
| `@TenNhanVienList` | `nvarchar(8000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |
| `@DmPhongBanREF` | `int(4)` | No |
| `@DmBoPhanREF` | `int(4)` | No |
| `@DmNhomlamViecREF` | `int(4)` | No |
| `@DmChucDanhREF` | `int(4)` | No |
| `@DmDiaDiemLamViecREFList` | `int(4)` | No |
| `@ToanTuGiaTriHopDong` | `nvarchar(100)` | No |
| `@GiaTriHopDong` | `float(8)` | No |
| `@ToanTuTongTienKyHopDong` | `nvarchar(100)` | No |
| `@TongTienKyHopDong` | `float(8)` | No |
| `@ToanTuTongTienHaiDauHopDong` | `nvarchar(100)` | No |
| `@TongTienHaiDauHopDong` | `float(8)` | No |
| `@ToanTuTongTienThucChay` | `nvarchar(100)` | No |
| `@TongTienThucChay` | `float(8)` | No |
| `@ToanTuTongTienChuaChay` | `nvarchar(100)` | No |
| `@TongTienChuaChay` | `float(8)` | No |
| `@ToanTuTongTienXuatHoaDon` | `nvarchar(100)` | No |
| `@TongTienXuatHoaDon` | `float(8)` | No |
| `@ToanTuTongTienDaThanhToan` | `nvarchar(100)` | No |
| `@TongTienDaThanhToan` | `float(8)` | No |
| `@ToanTuCongNo` | `nvarchar(100)` | No |
| `@CongNo` | `float(8)` | No |
| `@DmSanPhamREFList` | `nvarchar(8000)` | No |
| `@DmWebsiteREFList` | `nvarchar(8000)` | No |

## Definition (Source Code)

```sql

-- =============================================
--PRINT [dbo].[GetThucChayFilterString]
--(
-- --@StartDate = 
-- '2013-08-01',
-- --@EndDate = 
-- '2013-09-15',
-- --@DmSanPhamREFList = 
-- N'',
-- --@DmWebsiteREFList =
--  N'',
-- --@SoHopDongList = 
-- N'',
-- --@DmPhongBanREFList = 
-- N'',
-- --@DmBoPhanREFList = 
-- N'',
-- --@DmNhomLamViecREFList = 
-- N'',
-- --@TenNhanVienList = 
-- N'',
-- --@TenDangNhap = 
-- 'doanluan',
-- '3',
-- '',
-- '',
-- '6'
-- )


CREATE FUNCTION [dbo].[GetHopDongTongHopFilterString]
(
	-- Add the parameters for the function here		
	
	--Thong Tin Chung Hop Dong
	@HopDongIDList nvarchar(4000)
	,@NhanHopDongList nvarchar(4000)

	--Type Search By ThoiGian: 
	/*
	--Thoi gian Hop Dong
	,@NgayKyHopDong DATETIME
	,@NgayDanhSoHopDong datetime
	,@NgayChuyenHopDongChoKeToan datetime
	,@NgayNhanHopDongBanCung DATETIME
	,@NgayNhanBanFax DATETIME
	--Thoi gian Thuc Chay
	,@ThucChayDenNgay DATETIME
	--Thoi Gian Xuat Hoa Don
	,@HoaDonDenNgay DATETIME
	--Thoi Gian Tien Ve
	,@TienDaThanhToanDenNgay DATETIME	
	*/
	,@TypeSearchDate nvarchar(50) 
	,@StartDate datetime
	,@EndDate datetime

	--Thong Tin Khach Hang           
	,@DmKhachHangREFList int
	,@NganhHangList nvarchar(4000)

	--Trang Thai Hop Dong
	,@TrangThaiHopDong int                         
	,@IsBanCung INT
	--Trang Thai Thuc Chay Hop Dong
	,@TrangThaiThucChayHopDong INT

	--Thong Tin Ve Nhan Su - Sale 	   
	,@DmPhongBanREFList nvarchar(4000)
	,@DmBoPhanREFList nvarchar(4000)
	,@DmNhomLamViecREFList nvarchar(4000)
	,@TenNhanVienList nvarchar(4000)
	,@TenDangNhap NVARCHAR(50)
	,@DmPhongBanREF int
	,@DmBoPhanREF int
	,@DmNhomlamViecREF int
	,@DmChucDanhREF INT

	--Dia diem lam viec
	,@DmDiaDiemLamViecREFList int

	--Tien Hop Dong
	,@ToanTuGiaTriHopDong NVARCHAR(50)
	,@GiaTriHopDong float      
	,@ToanTuTongTienKyHopDong NVARCHAR(50)                         
	,@TongTienKyHopDong FLOAT
	,@ToanTuTongTienHaiDauHopDong NVARCHAR(50)                         
	,@TongTienHaiDauHopDong float         
	--TienThucChay
	,@ToanTuTongTienThucChay NVARCHAR(50)    
	,@TongTienThucChay FLOAT
	,@ToanTuTongTienChuaChay NVARCHAR(50)    
	,@TongTienChuaChay float  
	--Tien Xuat Hoa Don
	,@ToanTuTongTienXuatHoaDon NVARCHAR(50)
	,@TongTienXuatHoaDon float           
	--Tien Thanh Toan
	,@ToanTuTongTienDaThanhToan NVARCHAR(50)
	,@TongTienDaThanhToan FLOAT
	--Tien Cong No
	,@ToanTuCongNo NVARCHAR(50)
	,@CongNo FLOAT	

	--Thong Tin Hop Dong Chi Tiet
	,@DmSanPhamREFList nvarchar(4000)	
	,@DmWebsiteREFList nvarchar(4000)   
		
)
RETURNS nvarchar(4000)
AS
BEGIN	

	Declare @DauNhay nvarchar(50)
	Declare @FilterSQLCommand nvarchar(4000)
	
	DECLARE @GroupPermission INT;
	DECLARE @PhongID INT, @BoPhanID INT, @NhomLamViecID INT
	DECLARE @ListWebsiteID nvarchar(200), @ListSanPhamID nvarchar(200), @ListTenNhanVien nvarchar(2000)
	DECLARE @ToUserName NVARCHAR(50), @ToanTu nvarchar(50)
	
	
	set @DauNhay = ''''
	SET @ToUserName = (SELECT ToUserName FROM MappingUser A WHERE A.FromUserName = @TenDangNhap)
	
	IF @ToUserName IS NOT NULL
		SET @TenDangNhap = @ToUserName
			
	set @FilterSQLCommand = 'CONVERT(DATE,'+ @TypeSearchDate +') Between ' + @DauNhay + Convert(nvarchar(50),@StartDate) + @DauNhay + ' and '+ @DauNhay + Convert(nvarchar(50),@EndDate)+@DauNhay
				
	--Set quyen theo dieu kien tim kiem	
	if(@DmSanPhamREFList <> 'ALL')
		set @FilterSQLCommand = @FilterSQLCommand + ' and DmSanPhamREF in (' + @DmSanPhamREFList + ')'
	if(@DmWebsiteREFList <> 'ALL')
		set @FilterSQLCommand = @FilterSQLCommand + ' and DmWebsiteREF in (' + @DmWebsiteREFList + ')'				
	if(@HopDongIDList <> 'ALL')
		set @FilterSQLCommand = @FilterSQLCommand + ' and HopDongID in (' + @HopDongIDList + ')'
	if(@DmPhongBanREFList <> 'ALL')
		set @FilterSQLCommand = @FilterSQLCommand + ' and DmPhongBanREF in (' + @DmPhongBanREFList + ')' 
	if(@DmBoPhanREFList <> 'ALL')
		set @FilterSQLCommand = @FilterSQLCommand + ' and DmBoPhanREF in (' + @DmBoPhanREFList + ')' 
	if(@DmNhomLamViecREFList <> 'ALL')
		set @FilterSQLCommand = @FilterSQLCommand + ' and DmNhomLamViecREF in (' + @DmNhomLamViecREFList + ')'
		
	--Tien Hop Dong
	IF @ToanTuGiaTriHopDong <> 'ALL'
		SET @FilterSQLCommand += ' AND GiaTriHopDong ' + @ToanTuGiaTriHopDong + CONVERT(NVARCHAR(50),@GiaTriHopDong) 			

	IF @ToanTuTongTienKyHopDong <> 'ALL'
		SET @FilterSQLCommand += ' AND TongTienKyHopDong ' + @ToanTuTongTienKyHopDong + CONVERT(NVARCHAR(50),@TongTienKyHopDong) 

	IF @ToanTuTongTienHaiDauHopDong <> 'ALL'
		SET @FilterSQLCommand += ' AND TongTienHaiDauHopDong ' + @ToanTuTongTienHaiDauHopDong + CONVERT(NVARCHAR(50),@TongTienHaiDauHopDong) 
	
	--TienThucChay
	IF @ToanTuTongTienThucChay <> 'ALL'
		SET @FilterSQLCommand += ' AND TongTienThucChay ' + @ToanTuTongTienThucChay + CONVERT(NVARCHAR(50),@TongTienThucChay) 

	IF @ToanTuTongTienChuaChay <> 'ALL'
		SET @FilterSQLCommand += ' AND TongTienChuaChay ' + @ToanTuTongTienChuaChay + CONVERT(NVARCHAR(50),@TongTienChuaChay) 

	--Tien Xuat Hoa Don
	IF @ToanTuTongTienXuatHoaDon <> 'ALL'
		SET @FilterSQLCommand += ' AND TongTienXuatHoaDon ' + @ToanTuTongTienXuatHoaDon + CONVERT(NVARCHAR(50),@TongTienXuatHoaDon) 	
	
	--Tien Thanh Toan
	IF @ToanTuTongTienDaThanhToan <> 'ALL'
		SET @FilterSQLCommand += ' AND TongTienDaThanhToan ' + @ToanTuTongTienDaThanhToan + CONVERT(NVARCHAR(50),@TongTienDaThanhToan) 

	--Tien Cong No
	IF @ToanTuCongNo <> 'ALL'
		SET @FilterSQLCommand += ' AND CongNo ' + @ToanTuCongNo + CONVERT(NVARCHAR(50),@CongNo) 	
	
	IF @DmDiaDiemLamViecREFList <> 'ALL'
		SET @FilterSQLCommand += ' AND DmDiaDiemLamViecREFList IN (' + @DmDiaDiemLamViecREFList + ')'			
		
	IF @TrangThaiThucChayHopDong <> 'ALL'
		SET @FilterSQLCommand += ' AND TrangThaiThucChayHopDong IN (' + @TrangThaiThucChayHopDong + ')'	

	IF @IsBanCung <> 'ALL'
		SET @FilterSQLCommand += ' AND IsBanCung IN (' + @IsBanCung + ')'	
	
	IF @TrangThaiHopDong <> 'ALL'
		SET @FilterSQLCommand += ' AND TrangThaiHopDong IN (' + @TrangThaiHopDong + ')'	
		
	IF @DmKhachHangREFList <> 'ALL'
		SET @FilterSQLCommand += ' AND DmKhachHangREF IN (' + @DmKhachHangREFList + ')'				
		
	IF @TenNhanVienList <> 'ALL'
		SET @FilterSQLCommand += ' AND TenDangNhap IN (' + @TenNhanVienList + ')'	

	IF @NhanHopDongList <> 'ALL'
		SET @FilterSQLCommand += ' AND NhanHang IN (' + @NhanHopDongList + ')'	

	IF @NganhHangList <> 'ALL'
		SET @FilterSQLCommand += ' AND @NganhHang IN (' + @NganhHangList + ')'	

	
	set @FilterSQLCommand = ' and ' + @FilterSQLCommand
	
	SET @GroupPermission = dbo.NhanSuCheckGroupPermisstion(@TenDangNhap)
	SET @ListWebsiteID = dbo.GetListWebsiteByNhanVien(@TenDangNhap)
	SET @ListSanPhamID = dbo.GetListSanPhamByNhanVien(@TenDangNhap)	
	--Kiem tra neu co quyen quan ly full quyen
	if(@GroupPermission <> -1) 	
	Begin		
		
		--Kiem tra neu co chuc vu 
		set @FilterSQLCommand = @FilterSQLCommand + ' and (' 
		
		set @FilterSQLCommand = @FilterSQLCommand + dbo.GetDieuKienQuanLyByTenDangNhap(@TenDangNhap,@DmPhongBanREF ,@DmBoPhanREF ,@DmNhomlamViecREF ,@DmChucDanhREF)	
		
		--Kiem tra neu co quyen quan ly Website
		if(@ListWebsiteID <> '') set @FilterSQLCommand = @FilterSQLCommand + ' OR (DmWebsiteREF in (' + @ListWebsiteID + '))'
		
		--Kiem tra neu co quyen quan ly SanPham
		if(@ListSanPhamID <> '') set @FilterSQLCommand = @FilterSQLCommand + ' OR (DmSanPhamREF in (' + @ListSanPhamID + '))'						
		

		set @FilterSQLCommand = @FilterSQLCommand + ')'
	End	
	
	RETURN @FilterSQLCommand

END
```
