# Function: `fn_IsPhatSinhGiaTriTD_DoanhSoXuatHoaDonNhanHangCore`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-06-12 10:46:58.220000
- **Ngày sửa cuối**: 2015-06-12 10:46:58.220000

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
| `@DmListNhanHangREF` | `nvarchar(400)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@DmListNganhHangREF` | `nvarchar(400)` | No |
| `@DonViTinh` | `nvarchar(100)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@TrangThaiHopDong` | `int(4)` | No |
| `@ThongTinHoaDonREF` | `int(4)` | No |
| `@SoLuong` | `int(4)` | No |
| `@DonGia` | `float(8)` | No |
| `@ChietKhau` | `float(8)` | No |
| `@DmMaHopDongREF` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE FUNCTION [dbo].[fn_IsPhatSinhGiaTriTD_DoanhSoXuatHoaDonNhanHangCore]
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
	@DmListNhanHangREF NVARCHAR(200),
	@DmSanPhamREF INT,
	@DmWebsiteREF INT,
	@DmListNganhHangREF NVARCHAR(200),
	@DonViTinh NVARCHAR(50),
	@NgayThucHien DATETIME, 
	@TrangThaiHopDong INT,
	@ThongTinHoaDonREF INT,
	@SoLuong INT,
	@DonGia FLOAT,
	@ChietKhau FLOAT,
	@DmMaHopDongREF INT 
	
)
RETURNS INT
BEGIN
	DECLARE @IsPhatSinhGiaTriTD INT, @v_count INT
	DECLARE @SoHopDong_Bef NVARCHAR(100), @DmNhanVienREF_Bef INT, @PhongBanREF_Bef INT, @BoPhanREF_Bef INT
	DECLARE @NhomREF_Bef INT, @DmKhachHangREF_Bef INT, @NgayDanhSo_Bef DATETIME, @DmListNhanHangREF_Bef NVARCHAR(200)
	DECLARE @DmSanPhamREF_Bef INT, @DmWebsiteREF_Bef INT, @DmListNganhHangREF_Bef NVARCHAR(200), @DonViTinh_Bef NVARCHAR(50), @TrangThaiHopDong_Bef INT 
	DECLARE @DmMaHopDongREF_Bef INT , @SoLuong_Bef INT, @DonGia_Bef INT , @ChietKhau_Bef INT;
		DECLARE @ishopdongnoibo int
	SET @IsPhatSinhGiaTriTD = 0
	SET @SoHopDong_Bef = ''
	SET @DmNhanVienREF_Bef = 0
	SET @PhongBanREF_Bef = 0
	SET @BoPhanREF_Bef = 0
	SET @NhomREF_Bef = 0
	SET @DmKhachHangREF_Bef = 0
	SET @NgayDanhSo_Bef = '2010-01-01'
	SET @DmListNhanHangREF_Bef = ''
	SET @DmSanPhamREF_Bef = 0
	SET @DmWebsiteREF_Bef = 0
	SET @DmListNganhHangREF_Bef = ''
	SET @DonViTinh_Bef = 0
	SET @TrangThaiHopDong_Bef = 0
	SET @v_count = 0
	IF (SELECT COUNT(dsk.DoanhSoXuatHoaDonNhanHangCoreID)
	     FROM DoanhSoXuatHoaDonNhanHangCore dsk WHERE dsk.HopDongID = @HopDongID AND dsk.HopDongChiTietREF = @HopDongChiTietID) > 0
	     BEGIN
	     	
    	
	SET @ishopdongnoibo = dbo.fn_CheckIsDmLoaiHopDongNoiBo(@DmMaHopDongREF,GETDATE())
	IF @ishopdongnoibo = 0
	SET @SoLuong_Bef = (SELECT SUM(SoLuongPhatSinhTrongKy) FROM DoanhSoXuatHoaDonNhanHangCore dsxhdnhc 
	                WHERE dsxhdnhc.HopDongID = @HopDongID
		            AND dsxhdnhc.HopDongChiTietREF = @HopDongChiTietID
		            AND dsxhdnhc.NgayThucHien = (SELECT MAX(NgayThucHien)FROM DoanhSoXuatHoaDonNhanHangCore WHERE HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietID)
		            AND dsxhdnhc.ThongTinHoaDonREF = (SELECT TOP 1 ThongTinHoaDonREF FROM DoanhSoXuatHoaDonNhanHangCore WHERE HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietID  ORDER BY dsxhdnhc.NgayThucHien DESC)
		 
	)
	ELSE
		SET @SoLuong_Bef = (SELECT SUM(SoLuongNoiBoPhatSinhTrongKy) FROM DoanhSoXuatHoaDonNhanHangCore dsxhdnhc 
	                WHERE dsxhdnhc.HopDongID = @HopDongID
		            AND dsxhdnhc.HopDongChiTietREF = @HopDongChiTietID
		            AND dsxhdnhc.NgayThucHien = (SELECT MAX(NgayThucHien)FROM DoanhSoXuatHoaDonNhanHangCore WHERE HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietID)
		            AND dsxhdnhc.ThongTinHoaDonREF = (SELECT TOP 1 ThongTinHoaDonREF FROM DoanhSoXuatHoaDonNhanHangCore WHERE HopDongID = @HopDongID AND HopDongChiTietREF = @HopDongChiTietID ORDER BY dsxhdnhc.NgayThucHien DESC)
		 
		)
	SELECT TOP 1  @SoHopDong_Bef = dskc.SoHopDong
				, @DmNhanVienREF_bef = dskc.DmNhanVienREF
				, @PhongBanREF_Bef = dskc.PhongBanREF
				, @BoPhanREF_Bef = dskc.BoPhanREF
				, @NhomREF_Bef = dskc.NhomREF
				, @DmKhachHangREF_Bef = dskc.DmKhachHangREF
				, @DmListNhanHangREF_Bef = dskc.DmlistNhanHangREF
				, @DmSanPhamREF_Bef = dskc.DmSanPhamREF
				, @DmWebsiteREF_Bef = dskc.DmWebsiteREF
				, @DmListNganhHangREF_Bef = dskc.DmListNganhHangREF
				, @DonViTinh_Bef = dskc.DonViTinh
				, @TrangThaiHopDong_bef = dskc.TrangThaiHopDong
				, @DmMaHopDongREF_Bef = dskc.DmMaHopDongREF
				, @DonGia_Bef = dskc.DonGia
				, @ChietKhau_Bef = dskc.ChietKhau
	FROM DoanhSoXuatHoaDonNhanHangCore dskc
	WHERE dskc.HopDongID = @HopDongID
	AND dskc.HopDongChiTietREF = @HopDongChiTietID
	AND CONVERT(date,dskc.NgayThucHien) <= @NgayThucHien
	ORDER BY dskc.NgayThucHien DESC
	IF((@SoHopDong <> @SoHopDong_Bef) OR (@DmNhanVienREF_Bef <> @DmNhanVienREF) 
		OR (@PhongBanREF <> @PhongBanREF_Bef) OR (@BoPhanREF <> @BoPhanREF_Bef)
		OR (@NhomREF <> @NhomREF_Bef) OR (@DmKhachHangREF <> @DmKhachHangREF_Bef) OR (@DmMaHopDongREF_Bef <> @DmMaHopDongREF)
		OR (@DmListNhanHangREF_Bef <> @DmListNhanHangREF) OR (@DmSanPhamREF <> @DmSanPhamREF_Bef)
		OR (@DmWebsiteREF <> @DmWebsiteREF_Bef) OR (@DmListNganhHangREF <> @DmListNganhHangREF_Bef)
		OR (@SoLuong_Bef <> @SoLuong) OR (@DonGia_Bef <> @DonGia) OR (@ChietKhau_Bef <> @ChietKhau)
		OR (@DonViTinh <> @DonViTinh_Bef) OR ((@TrangThaiHopDong <> @TrangThaiHopDong_bef) AND (@TrangThaiHopDong = 3))
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
	IF (SELECT COUNT(hdct.HopDongChiTietID) FROM HopDongChiTiet hdct WHERE hdct.HopDongFK = @HopDongID AND hdct.DeletedStatus =0 ) <>
	   (SELECT COUNT(A.HopDongChiTietREF) FROM (SELECT DISTINCT dsxhdc.HopDongChiTietREF AS HopDongChiTietREF
	      FROM DoanhSoXuatHoaDonNhanHangCore dsxhdc WHERE dsxhdc.HopDongID = @HopDongID) A
	   )
	SET @IsPhatSinhGiaTriTD = 1
	IF(SELECT COUNT(DoanhSoXuatHoaDonNhanHangCoreID) FROM DoanhSoXuatHoaDonNhanHangCore dsxhdc WHERE dsxhdc.ThongTinHoaDonREF = @ThongTinHoaDonREF) > 0
	SET @IsPhatSinhGiaTriTD = 1
 END
	SET @IsPhatSinhGiaTriTD = ISNULL(@IsPhatSinhGiaTriTD, 0)
		
	RETURN @IsPhatSinhGiaTriTD;
END


```
