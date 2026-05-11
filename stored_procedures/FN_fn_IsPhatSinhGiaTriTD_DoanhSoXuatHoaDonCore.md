# Function: `fn_IsPhatSinhGiaTriTD_DoanhSoXuatHoaDonCore`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-06-12 10:46:58.870000
- **Ngày sửa cuối**: 2015-06-12 10:46:58.870000

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
| `@DmHinhThucQuangCaoREF` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@DmBannerREF` | `int(4)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@TrangThaiHopDong` | `int(4)` | No |
| `@SoHoaDon` | `nvarchar(100)` | No |
| `@ThongTinHoaDonREF` | `int(4)` | No |
| `@SoLuong` | `int(4)` | No |
| `@DonGia` | `float(8)` | No |
| `@ChietKhau` | `float(8)` | No |
| `@DmMaHopDongREF` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE FUNCTION [dbo].[fn_IsPhatSinhGiaTriTD_DoanhSoXuatHoaDonCore]
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
	@DmHinhThucQuangCaoREF INT,
	@DmSanPhamREF INT,
	@DmWebsiteREF INT,
	@DmBannerREF INT,
	@DonViTinh NVARCHAR(50),
	@NgayThucHien DATETIME, 
	@TrangThaiHopDong INT,
	@SoHoaDon NVARCHAR(50),
	@ThongTinHoaDonREF INT,
	@SoLuong INT,
	@DonGia FLOAT,
	@ChietKhau FLOAT,
	@DmMaHopDongREF int
	
)
RETURNS INT
BEGIN
	DECLARE @IsPhatSinhGiaTriTD INT, @v_count INT
	DECLARE @SoHopDong_Bef NVARCHAR(100), @DmNhanVienREF_Bef INT, @PhongBanREF_Bef INT, @BoPhanREF_Bef INT
	DECLARE @NhomREF_Bef INT, @DmKhachHangREF_Bef INT, @NgayDanhSo_Bef DATETIME, @DmHinhThucQuangCaoREF_Bef INT
	DECLARE @DmSanPhamREF_Bef INT, @DmWebsiteREF_Bef INT, @DmBannerREF_Bef INT, @DonViTinh_Bef NVARCHAR(50), @TrangThaiHopDong_Bef INT 
	DECLARE @DmMaHopDongREF_Bef INT
	DECLARE @SoHoaDon_bef NVARCHAR(50), @SoLuong_Bef INT, @DonGia_Bef FLOAT, @ChietKhau_Bef FLOAT;
		DECLARE @ishopdongnoibo int
	SET @IsPhatSinhGiaTriTD = 0
	SET @SoHopDong_Bef = ''
	SET @DmNhanVienREF_Bef = 0
	SET @PhongBanREF_Bef = 0
	SET @BoPhanREF_Bef = 0
	SET @NhomREF_Bef = 0
	SET @DmKhachHangREF_Bef = 0
	SET @NgayDanhSo_Bef = '2010-01-01'
	SET @DmHinhThucQuangCaoREF_Bef = 0
	SET @DmSanPhamREF_Bef = 0
	SET @DmWebsiteREF_Bef = 0
	SET @DmBannerREF_Bef = 0
	SET @DonViTinh_Bef = 0
	SET @TrangThaiHopDong_Bef = 0
	SET @v_count = 0
	SET @SoHoaDon_bef =''
	SET @DmMaHopDongREF_Bef = 0
	
	IF (SELECT COUNT(dsk.DoanhSoXuatHoaDonNganhHangCoreID)
	     FROM DoanhSoXuatHoaDonNganhHangCore dsk WHERE dsk.HopDongID = @HopDongID AND dsk.HopDongChiTietREF = @HopDongChiTietID) > 0
	     BEGIN
	SET @ishopdongnoibo = dbo.fn_CheckIsDmLoaiHopDongNoiBo(@DmMaHopDongREF,GETDATE())
	IF @ishopdongnoibo = 0
	SET @SoLuong_Bef = (SELECT SUM(SoLuongPhatSinhTrongKy) FROM DoanhSoXuatHoaDonNganhHangCore dsxhdnhc 
	                WHERE dsxhdnhc.HopDongID = @HopDongID
		            AND dsxhdnhc.HopDongChiTietREF = @HopDongChiTietID
		            AND dsxhdnhc.NgayThucHien = (SELECT MAX(NgayThucHien)FROM DoanhSoXuatHoaDonNganhHangCore WHERE HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietID)
		            AND dsxhdnhc.ThongTinHoaDonREF = (SELECT TOP 1 ThongTinHoaDonREF FROM DoanhSoXuatHoaDonNganhHangCore WHERE HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietID  ORDER BY dsxhdnhc.NgayThucHien DESC)
		 
	)
	ELSE
		SET @SoLuong_Bef = (SELECT SUM(SoLuongNoiBoPhatSinhTrongKy) FROM DoanhSoXuatHoaDonNganhHangCore dsxhdnhc 
	                WHERE dsxhdnhc.HopDongID = @HopDongID
		            AND dsxhdnhc.HopDongChiTietREF = @HopDongChiTietID
		            AND dsxhdnhc.NgayThucHien = (SELECT MAX(NgayThucHien)FROM DoanhSoXuatHoaDonNganhHangCore WHERE HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietID)
		            AND dsxhdnhc.ThongTinHoaDonREF = (SELECT TOP 1 ThongTinHoaDonREF FROM DoanhSoXuatHoaDonNganhHangCore WHERE HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietID ORDER BY dsxhdnhc.NgayThucHien DESC)
		 
		)
	SELECT TOP 1  @SoHopDong_Bef = dskc.SoHopDong
				, @DmNhanVienREF_bef = dskc.DmNhanVienREF
				, @PhongBanREF_Bef = dskc.PhongBanREF
				, @BoPhanREF_Bef = dskc.BoPhanREF
				, @NhomREF_Bef = dskc.NhomREF
				, @DmKhachHangREF_Bef = dskc.DmKhachHangREF
				, @DmHinhThucQuangCaoREF_Bef = dskc.DmHinhThucQuangCaoREF
				, @DmSanPhamREF_Bef = dskc.DmSanPhamREF
				, @DmWebsiteREF_Bef = dskc.DmWebsiteREF
				, @DmBannerREF_Bef = dskc.ViTriBannerREF
				, @DonViTinh_Bef = dskc.DonViTinh
				, @TrangThaiHopDong_bef = dskc.TrangThaiHopDong
				, @SoHoaDon_bef = dskc.SoHoaDon
			
				, @DonGia_Bef = dskc.DonGia
				, @ChietKhau_Bef = dskc.ChietKhau
				, @DmMaHopDongREF_Bef = dskc.DmMaHopDongREF
	FROM DoanhSoXuatHoaDonCore dskc
	WHERE dskc.HopDongID = @HopDongID
	AND dskc.HopDongChiTietREF = @HopDongChiTietID
	AND CONVERT(date,dskc.NgayThucHien) <= @NgayThucHien
	AND dskc.DeletedStatus <> 1
	ORDER BY dskc.NgayThucHien DESC
	IF((@SoHopDong <> @SoHopDong_Bef) OR (@DmNhanVienREF_Bef <> @DmNhanVienREF) 
		OR (@PhongBanREF <> @PhongBanREF_Bef) OR (@BoPhanREF <> @BoPhanREF_Bef)
		OR (@NhomREF <> @NhomREF_Bef) OR (@DmKhachHangREF <> @DmKhachHangREF_Bef)
		OR (@DmHinhThucQuangCaoREF <> @DmHinhThucQuangCaoREF_Bef) OR (@DmSanPhamREF <> @DmSanPhamREF_Bef)
		OR (@DmWebsiteREF <> @DmWebsiteREF_Bef) OR (@DmBannerREF <> @DmBannerREF_Bef)
		OR (@DmMaHopDongREF <> @DmMaHopDongREF_Bef)
		OR (@DonViTinh <> @DonViTinh_Bef) OR ((@TrangThaiHopDong <> @TrangThaiHopDong_bef) AND (@TrangThaiHopDong = 3))
		OR (@SoHoaDon <> @SoHoaDon_bef) OR (@SoLuong_Bef <> @SoLuong) OR (@ChietKhau_Bef <> @ChietKhau) OR (@DonGia <> @DonGia_Bef)
	)
	BEGIN
		SET @IsPhatSinhGiaTriTD = 1
	END		 

	SET @v_count =
	   ( 
		SELECT COUNT(HopDongREF) FROM ThongTinHoaDon 
	    WHERE HopDongREF = @HopDongID 
	    AND DeletedStatus = 1
	    AND LastModifiedAt = @NgayThucHien
	   )
	IF(@v_count >0)
	BEGIN
		SET @IsPhatSinhGiaTriTD = 1
	END
	SET @v_count =
	   ( 
		SELECT COUNT(HopDongREF) FROM ThongTinHoaDon 
	    WHERE HopDongREF = @HopDongID 
	    AND CONVERT(DATE,CreatedAt) <> CONVERT(DATE,LastModifiedAt)
	    AND LastModifiedAt = @NgayThucHien
	   )
	IF(@v_count >0)
	BEGIN
		SET @IsPhatSinhGiaTriTD = 1
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
		SELECT COUNT(hd.HopDongID) FROM HopDong hd 
	    WHERE hd.HopDongID = @HopDongID 
	    AND hd.TrangThaiHopDong = 3
	    AND CONVERT(DATE,CreatedAt) <> CONVERT(DATE,LastModifiedAt)
	    AND LastModifiedAt = @NgayThucHien
	   )
	IF(@v_count >0)
	BEGIN
		SET @IsPhatSinhGiaTriTD = 1
	END
	IF (SELECT COUNT(hdct.HopDongChiTietID) FROM HopDongChiTiet hdct WHERE hdct.HopDongFK = @HopDongID AND hdct.DeletedStatus =0 ) <>
	   (SELECT COUNT(A.HopDongChiTietREF) FROM (SELECT DISTINCT dsxhdc.HopDongChiTietREF AS HopDongChiTietREF
	      FROM DoanhSoXuatHoaDonCore dsxhdc WHERE dsxhdc.HopDongID = @HopDongID) A
	   )
	SET @IsPhatSinhGiaTriTD = 1
	IF(SELECT COUNT(DoanhSoXuatHoaDonCoreID) FROM DoanhSoXuatHoaDonCore dsxhdc WHERE dsxhdc.ThongTinHoaDonREF = @ThongTinHoaDonREF) > 0
	SET @IsPhatSinhGiaTriTD = 1
	END
	SET @IsPhatSinhGiaTriTD = ISNULL(@IsPhatSinhGiaTriTD, 0)
	RETURN @IsPhatSinhGiaTriTD;
END


```
