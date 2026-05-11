# Function: `fn_TC_CheckLoaithaydoi_ThucChayHopDongChiTietPR`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2017-06-12 15:57:21.343000
- **Ngày sửa cuối**: 2017-06-12 15:57:21.343000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@ThucChayHopDongChiTietPRID` | `int(4)` | No |
| `@HopDongID` | `int(4)` | No |
| `@DmHinhThucQuangCaoREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@DmNhanHangREF` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@DmViTriREF` | `int(4)` | No |
| `@SoLuong` | `int(4)` | No |
| `@GiaTien` | `float(8)` | No |
| `@ChietKhau` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@NgayDanhSoHopDong` | `datetime(8)` | No |
| `@SysNhanVienREF` | `int(4)` | No |
| `@DmMaHopDongREF` | `int(4)` | No |
| `@TenDangNhap` | `nvarchar(50)` | No |
| `@TenKhachHang` | `nvarchar(510)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[fn_TC_CheckLoaithaydoi_ThucChayHopDongChiTietPR]
    (
      @ThucChayHopDongChiTietPRID INT ,
      @HopDongID INT ,
      @DmHinhThucQuangCaoREF INT ,
      @DmSanPhamREF INT ,
      @DmNhanHangREF INT ,
      @DmWebsiteREF INT ,
      @DmViTriREF INT ,
      @SoLuong INT ,
      @GiaTien FLOAT ,
      @ChietKhau INT ,
      @NgayThucHien DATETIME ,
      @SoHopDong NVARCHAR(50) ,
      @NgayDanhSoHopDong DATETIME ,
      @SysNhanVienREF INT ,
      @DmMaHopDongREF INT ,
      @TenDangNhap NVARCHAR(25) ,
      @TenKhachHang NVARCHAR(255)
    )
RETURNS INT --LOAI THAY DOI : 1 CHI THAY DOI GIA TRI, 2 THAY DOI THONG TIN, 0 KHONG THAY DOI GIA TRI HOAC THONG TIN 
    BEGIN
        DECLARE @out_type INT ,
            @v_count_row INT ,
            @ThoiGianBatDauCheck DATETIME ,
            @DmSanPhamREF_Bf INT ,
            @DmHinhThucQuangCaoREF_Bf INT;
        DECLARE @DmNhanHangREF_Bf INT ,
            @DmWebsiteREF_Bf INT;
        DECLARE @DmViTriREF_Bf INT ,
            @GiaTien_Bf FLOAT ,
            @ChietKhau_Bf INT ,
            @NgayThucHien_Bf DATETIME;
        DECLARE @SoHopDong_Bf NVARCHAR(50) ,
            @NgayDanhSoHopDong_Bf DATETIME ,
            @SysNhanVienREF_Bf INT ,
            @DmMaHopDongREF_Bf INT ,
            @TenDangNhap_Bf NVARCHAR(25);
        DECLARE @TenKhachHang_Bf NVARCHAR(255);
	
        SET @ThoiGianBatDauCheck = '2016-01-01';
	
	--Neu chua tinh thuc chay hoac ngay tinh thuc chay = ngaythuchien thi khong phai check
        SET @v_count_row = 0;
	
        SELECT TOP 1
                @DmHinhThucQuangCaoREF_Bf = tcdt.DmHinhThucQuangCao ,
                @DmSanPhamREF_Bf = tcdt.DmSanPhamREF ,
                @DmNhanHangREF_Bf = CONVERT(INT, tcdt.NhanHang) ,
                @DmWebsiteREF_Bf = tcdt.DmWebsiteREF ,
                @DmViTriREF_Bf = tcdt.DmViTriREF ,
                @GiaTien_Bf = tcdt.DonGiaTheoDonVi ,
                @ChietKhau_Bf = tcdt.ChietKhau ,
                @NgayThucHien_Bf = tcdt.NgayThucHien ,
                @SoHopDong_Bf = tcdt.SoHopDong ,
                @NgayDanhSoHopDong_Bf = tcdt.NgayDanhSoHopDong ,
                @SysNhanVienREF_Bf = tcdt.SysNhanVienREF ,
                @DmMaHopDongREF_Bf = tcdt.DmMaHopDongREF ,
                @TenDangNhap_Bf = tcdt.TenDangNhap ,
                @TenKhachHang_Bf = tcdt.TenKhachHang
        FROM    ThucChayDaTinh tcdt
        WHERE   tcdt.HopDongID = @HopDongID
                AND tcdt.NgayThucHien <= @NgayThucHien
                AND tcdt.DotChayBooking = CONVERT(NVARCHAR(50), @ThucChayHopDongChiTietPRID)
                AND tcdt.NgayThucHien >= @ThoiGianBatDauCheck
        ORDER BY tcdt.NgayThucHien DESC;


        IF ( @NgayThucHien > @NgayThucHien_Bf )
            BEGIN
                IF ( ( @DmHinhThucQuangCaoREF_Bf <> @DmHinhThucQuangCaoREF )
                     OR ( @DmSanPhamREF_Bf <> @DmSanPhamREF )
                     OR ( @DmNhanHangREF_Bf <> @DmNhanHangREF )
                     OR ( @DmWebsiteREF_Bf <> @DmWebsiteREF )
                     OR ( @DmViTriREF_Bf <> @DmViTriREF )
                     OR ( @SoHopDong_Bf <> @SoHopDong )
                     OR ( @NgayDanhSoHopDong_Bf <> @NgayDanhSoHopDong )
                     OR ( @SysNhanVienREF_Bf <> @SysNhanVienREF )
                     OR ( @DmMaHopDongREF_Bf <> @DmMaHopDongREF )
                     OR ( @TenDangNhap_Bf <> @TenDangNhap )
                     OR ( @TenKhachHang_Bf <> @TenKhachHang )
                   )
                    SET @out_type = 2; --THAY DOI THONG TIN THUC CHAY
                ELSE
                    IF ( ( @GiaTien_Bf <> @GiaTien )
                         OR ( @ChietKhau_Bf <> @ChietKhau )
                       )
                        SET @out_type = 1;
            END;
        SET @out_type = ISNULL(@out_type, 0);
        RETURN @out_type;
    END;

```
