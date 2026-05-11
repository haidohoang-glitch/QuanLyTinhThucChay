# Stored Procedure: `KSTC_CheckGiaTriThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-09 15:40:46.873000
- **Ngày sửa cuối**: 2014-12-17 17:20:39.800000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@Type` | `int(4)` | No |

## Definition (Source Code)

```sql
--EXEC KSTC_CheckGiaTriThayDoi '2014-12-06',342,2
CREATE PROCEDURE [dbo].[KSTC_CheckGiaTriThayDoi] 
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@DmSanPhamREF INT, --342: Mobile, 381: Sponsor
	@Type INT --1:So sánh dữ liệu TCDT tại ngày thực hiện với dữ liệu tcdt quá khứ theo các thông tin có thể thay đổi
	         --2: so sánh dữ liệu TCDT tại ngày thực hiện với dữ liệu trên hợp đồng hiện tại
AS
BEGIN
IF @Type = 1
BEGIN
	SELECT a.*, b.* FROM (
		SELECT distinct tcdt.HopDongChiTietREF, tcdt.HopDongID,
		tcdt.DmSanPhamREF, 
		tcdt.DmHinhThucQuangCao, 
		tcdt.DonViTinh,tcdt.DonGia, 
		tcdt.DonGiaTheoDonVi,
		SoLuongDotChayHD, 
		SoLuong,
		tcdt.ChietKhau, 
		tcdt.IsKhuyenMai
		FROM ThucChayDaTinh tcdt 
		WHERE tcdt.NgayThucHien = @NgayThucHien
		AND tcdt.DmSanPhamREF = @DmSanPhamREF
	)a
	LEFT JOIN
	(
		SELECT distinct tcdt.HopDongChiTietREF, tcdt.HopDongID,
		tcdt.DmSanPhamREF, 
		tcdt.DmHinhThucQuangCao, 
		tcdt.DonViTinh,tcdt.DonGia, 
		tcdt.DonGiaTheoDonVi,
		SoLuongDotChayHD, 
		SoLuong,
		tcdt.ChietKhau, 
		tcdt.IsKhuyenMai
		FROM ThucChayDaTinh tcdt 
		WHERE tcdt.NgayThucHien < @NgayThucHien
		AND tcdt.DmSanPhamREF = @DmSanPhamREF
	)b
	ON a.HopDongChiTietREF = b.HopDongChiTietREF
	AND a.HopDongID = b.HopDongID
	AND a.DmSanPhamREF = b.DmSanPhamREF 
	AND	a.DmHinhThucQuangCao = b.DmHinhThucQuangCao 
	AND	a.DonViTinh = b.DonViTinh
	and a.DonGia = b.DonGia 
	AND	a.DonGiaTheoDonVi = b.DonGiaTheoDonVi
	AND	a.SoLuongDotChayHD = b.SoLuongDotChayHD 
	AND	a.SoLuong = b.SoLuongDotChayHD
	AND	a.ChietKhau = b.ChietKhau 
	AND	a.IsKhuyenMai = b.IsKhuyenMai
	WHERE
	(a.DmSanPhamREF <> b.DmSanPhamREF 
	OR	a.DmHinhThucQuangCao <> b.DmHinhThucQuangCao 
	OR	a.DonViTinh <> b.DonViTinh
	OR  a.DonGia <> b.DonGia 
	OR	a.DonGiaTheoDonVi <> b.DonGiaTheoDonVi
	OR	a.SoLuongDotChayHD <> b.SoLuongDotChayHD 
	OR	a.SoLuong <> b.SoLuongDotChayHD
	OR	a.ChietKhau <> b.ChietKhau 
	OR	a.IsKhuyenMai <> b.IsKhuyenMai 
	)	
END
ELSE IF @Type = 2
BEGIN
	SELECT * FROM (
	SELECT tcdt.HopDongChiTietREF, tcdt.HopDongID,
		tcdt.DmSanPhamREF, 
		(SELECT DmSanPhamREF FROM HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = tcdt.HopDongChiTietREF) sphd, 
		tcdt.DmHinhThucQuangCao, 
		(SELECT DmLoaiREF FROM HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = tcdt.HopDongChiTietREF) HTQCHD,
		tcdt.DonViTinh,
		(SELECT CASE WHEN DonViTinh ='CPM' THEN 'VIEW'
					 WHEN donvitinh = 'CPC' THEN 'CLICK'
					 ELSE DonViTinh 
		 END
		 FROM HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = tcdt.HopDongChiTietREF) DonViTinhHD,
		tcdt.DonGia, 
		(SELECT DonGia FROM HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = tcdt.HopDongChiTietREF) DonGiaHD,
		SoLuongDotChayHD, 
		(SELECT SoLuong FROM HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = tcdt.HopDongChiTietREF) SoLuongHD,
		tcdt.ChietKhau, 
		(SELECT ChietKhau FROM HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = tcdt.HopDongChiTietREF) ChietKhauHD,
		tcdt.IsKhuyenMai,
		(SELECT IsKhuyenMai FROM HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = tcdt.HopDongChiTietREF) IsKhuyenMaiHD
		FROM ThucChayDaTinh tcdt 
		WHERE tcdt.NgayThucHien = @NgayThucHien	
		AND tcdt.DmSanPhamREF = @DmSanPhamREF
	) a
	WHERE a.DmSanPhamREF <> a.sphd
	OR a.DmHinhThucQuangCao <> a.HTQCHD
	OR a.DonViTinh <> a.DonViTinhHD
	OR a.DonGia <> a.DonGiaHD
	OR a.SoLuongDotChayHD <> a.SoLuongHD
	OR a.ChietKhau <> a.ChietKhauHD
	OR a.IsKhuyenMai <> a.IsKhuyenMaiHD
END

END
```
