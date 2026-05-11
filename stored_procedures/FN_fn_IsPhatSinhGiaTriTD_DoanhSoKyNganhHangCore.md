# Function: `fn_IsPhatSinhGiaTriTD_DoanhSoKyNganhHangCore`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-04-22 16:42:50.287000
- **Ngày sửa cuối**: 2015-04-22 16:42:50.287000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@HopDongID` | `int(4)` | No |
| `@HopDongChiTietID` | `int(4)` | No |
| `@SoHopDong` | `nvarchar(200)` | No |
| `@DmNhanVienREF` | `int(4)` | No |
| `@PhongBanREF` | `int(4)` | No |
| `@BoPhanREF` | `int(4)` | No |
| `@NhomREF` | `int(4)` | No |
| `@DmKhachHangREF` | `int(4)` | No |
| `@NgayDanhSo` | `datetime(8)` | No |
| `@DmListNganhHangREF` | `nvarchar(400)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@TrangThaiHopDong` | `int(4)` | No |
| `@DmMaHopDongREF` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE FUNCTION [dbo].[fn_IsPhatSinhGiaTriTD_DoanhSoKyNganhHangCore]
(
	@HopDongID INT,
	@HopDongChiTietID INT,
	@SoHopDong NVARCHAR(100),
	@DmNhanVienREF INT,
	@PhongBanREF INT,
	@BoPhanREF INT,
	@NhomREF INT,
	@DmKhachHangREF INT,
	@NgayDanhSo DATETIME, --Cho nay can xem lai
	@DmListNganhHangREF NVARCHAR(200),
	@DmSanPhamREF INT,
	@DmWebsiteREF INT,
	@DonViTinh NVARCHAR(50),
	@NgayThucHien DATETIME, 
	@TrangThaiHopDong INT,
	@DmMaHopDongREF INT
	
)
RETURNS INT
BEGIN
	DECLARE @IsPhatSinhGiaTriTD INT, @v_count INT
	DECLARE @SoHopDong_Bef NVARCHAR(100), @DmNhanVienREF_Bef INT, @PhongBanREF_Bef INT, @BoPhanREF_Bef INT
	DECLARE @NhomREF_Bef INT, @DmKhachHangREF_Bef INT, @NgayDanhSo_Bef DATETIME, @DmNganhHangREF_Bef INT
	DECLARE @DmSanPhamREF_Bef INT, @DmWebsiteREF_Bef INT, @DmListNganhHangREF_Bef NVARCHAR(200), @DonViTinh_Bef NVARCHAR(50), @TrangThaiHopDong_Bef INT 
	DECLARE @DmMaHopDongREF_Bef INT 
	SET @IsPhatSinhGiaTriTD = 0
	SET @SoHopDong_Bef = ''
	SET @DmNhanVienREF_Bef = 0
	SET @PhongBanREF_Bef = 0
	SET @BoPhanREF_Bef = 0
	SET @NhomREF_Bef = 0
	SET @DmKhachHangREF_Bef = 0
	SET @NgayDanhSo_Bef = '2010-01-01'
	SET @DmNganhHangREF_Bef = 0
	SET @DmSanPhamREF_Bef = 0
	SET @DmWebsiteREF_Bef = 0
	SET @DonViTinh_Bef = 0
	SET @TrangThaiHopDong_Bef = 0
	SET @DmListNganhHangREF_Bef = ''
	SET @v_count = 0
	IF (SELECT COUNT(dskc.DoanhSoKyNganhHangCoreID)
	      FROM DoanhSoKyNganhHangCore dskc
	WHERE dskc.HopDongID = @HopDongID
	AND dskc.HopDongChiTietREF = @HopDongChiTietID
	AND CONVERT(date,dskc.NgayThucHien) <= @NgayThucHien) > 0 
	BEGIN
	
		SELECT TOP 1  @SoHopDong_Bef = dskc.SoHopDong
					, @DmNhanVienREF_bef = dskc.DmNhanVienREF
					, @PhongBanREF_Bef = dskc.PhongBanREF
					, @BoPhanREF_Bef = dskc.BoPhanREF
					, @NhomREF_Bef = dskc.NhomREF
					, @DmKhachHangREF_Bef = dskc.DmKhachHangREF
					, @DmSanPhamREF_Bef = dskc.DmSanPhamREF
					, @DmWebsiteREF_Bef = dskc.DmWebsiteREF
					, @DonViTinh_Bef = dskc.DonViTinh
					, @TrangThaiHopDong_bef = dskc.TrangThaiHopDong
					, @DmListNganhHangREF_Bef = dskc.DmListNganhHangREF
					, @DmMaHopDongREF_Bef = dskc.DmMaSoHopDongREF
		FROM DoanhSoKyNganhHangCore dskc
		WHERE dskc.HopDongID = @HopDongID
		AND dskc.HopDongChiTietREF = @HopDongChiTietID
		
		AND CONVERT(date,dskc.NgayThucHien) <= @NgayThucHien
		ORDER BY dskc.NgayThucHien DESC
		IF((@SoHopDong <> @SoHopDong_Bef) OR (@DmNhanVienREF_Bef <> @DmNhanVienREF) 
			OR (@PhongBanREF <> @PhongBanREF_Bef) OR (@BoPhanREF <> @BoPhanREF_Bef)
			OR (@NhomREF <> @NhomREF_Bef) OR (@DmKhachHangREF <> @DmKhachHangREF_Bef)
			OR (@DmListNganhHangREF_Bef <> @DmListNganhHangREF) OR (@DmSanPhamREF <> @DmSanPhamREF_Bef)
			OR (@DmWebsiteREF <> @DmWebsiteREF_Bef) OR (@DmMaHopDongREF_Bef <> @DmMaHopDongREF) 
			OR (@DonViTinh <> @DonViTinh_Bef) OR ((@TrangThaiHopDong <> @TrangThaiHopDong_bef) AND (@TrangThaiHopDong = 3))
		)
		BEGIN
			SET @IsPhatSinhGiaTriTD = 1
		END		 
	END
	SET @v_count =
	(
		SELECT COUNT(hdct.HopDongChiTietID) 
		FROM HopDongChiTiet hdct
		WHERE HDCT.DeletedStatus = 1
		AND hdct.HopDongChiTietID = @HopDongChiTietID
		AND Convert(date,hdct.LastModifiedAt) = @NgayThucHien
	) 
	IF(@v_count >0)
	BEGIN
		SET @IsPhatSinhGiaTriTD = 1
	END
	SET @v_count =
	(
		SELECT COUNT(hd.HopDongID) 
		FROM HopDong hd
		WHERE hd.TrangThaiHopDong = 3
		AND hd.HopDongID = @HopDongID
		AND Convert(date,hd.LastModifiedAt) = @NgayThucHien
	) 
	IF(@v_count >0)
	BEGIN
		SET @IsPhatSinhGiaTriTD = 1
	END
	SET @IsPhatSinhGiaTriTD = ISNULL(@IsPhatSinhGiaTriTD, 0)
		
	RETURN @IsPhatSinhGiaTriTD;
END


```
