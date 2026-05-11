# Function: `fn_Check_Loaithaydoi_ThucChayHopDongChiTietPR`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2016-01-19 10:32:31.990000
- **Ngày sửa cuối**: 2016-01-20 09:47:06.603000

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

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[fn_Check_Loaithaydoi_ThucChayHopDongChiTietPR]
(
	@ThucChayHopDongChiTietPRID INT,
	@HopDongID INT,
	@DmHinhThucQuangCaoREF INT,
	@DmSanPhamREF INT,
	@DmNhanHangREF INT,
	@DmWebsiteREF INT,
	@DmViTriREF INT,
	@SoLuong INT,
	@GiaTien FLOAT,
	@ChietKhau INT,
	@NgayThucHien DATETIME
)
RETURNS INT --LOAI THAY DOI : 1 CHI THAY DOI GIA TRI, 2 THAY DOI THONG TIN, 0 KHONG THAY DOI GIA TRI HOAC THONG TIN 

BEGIN
	DECLARE @out_type INT, @v_count_row INT, @ThoiGianBatDauCheck DATETIME, @DmSanPhamREF_Bf INT, @DmHinhThucQuangCaoREF_Bf INT
	DECLARE @DmNhanHangREF_Bf INT,	@DmWebsiteREF_Bf INT
	DECLARE @DmViTriREF_Bf INT,	@GiaTien_Bf FLOAT,	@ChietKhau_Bf INT, @NgayThucHien_Bf datetime
	
	SET @ThoiGianBatDauCheck = '2016-01-01'
	
	--Neu chua tinh thuc chay hoac ngay tinh thuc chay = ngaythuchien thi khong phai check
	SET @v_count_row = 0
	
	SELECT TOP 1 @DmHinhThucQuangCaoREF_Bf = tcdt.DmHinhThucQuangCao
		, @DmSanPhamREF_Bf = tcdt.DmSanPhamREF
		, @DmNhanHangREF_Bf = Convert(int,tcdt.NhanHang)
		, @DmWebsiteREF_Bf =  tcdt.DmWebsiteREF
		, @DmViTriREF_Bf =  tcdt.DmViTriREF
		, @GiaTien_bf  = tcdt.DonGiaTheoDonVi
		, @ChietKhau_bf = tcdt.ChietKhau
		, @NgayThucHien_Bf = tcdt.NgayThucHien
		FROM ThucChayDaTinh tcdt
		WHERE 1=1
		AND tcdt.HopDongID = @HopDongID
		AND tcdt.NgayThucHien <= @NgayThucHien
		AND tcdt.DotChayBooking = CONVERT(NVARCHAR(50),@ThucChayHopDongChiTietPRID)
		AND tcdt.NgayThucHien >= @ThoiGianBatDauCheck
	order by tcdt.NgayThucHien	desc
	IF(@NgayThucHien > @NgayThucHien_Bf)
	BEGIN
		IF(
			(@DmHinhThucQuangCaoREF_bf <> @DmHinhThucQuangCaoREF)
			OR (@DmSanPhamREF_bf <> @DmSanPhamREF)
			OR (@DmNhanHangREF_Bf <> @DmNhanHangREF)
			OR (@DmWebsiteREF_Bf <> @DmWebsiteREF)
			OR (@DmViTriREF_Bf <> @DmViTriREF)
		) 
			SET @out_type = 2 --THAY DOI THONG TIN THUC CHAY
		ELSE IF((@GiaTien_Bf <> @GiaTien)
		OR (@ChietKhau_Bf <> @ChietKhau)
		)
			SET @out_type = 1
	END
	SET @out_type = ISNULL(@out_type,0)
	RETURN @out_type
END

```
