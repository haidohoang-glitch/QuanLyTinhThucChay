# Stored Procedure: `Insert_DoanhSoThucChayNhanHangCore_NoiBo_KhongHD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-09-26 16:00:09.960000
- **Ngày sửa cuối**: 2016-09-26 16:00:09.960000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [Insert_DoanhSoThucChayNhanHangCore_ThucThuKhuyenMai_KhongHD] '2013-12-31'

CREATE PROCEDURE [dbo].[Insert_DoanhSoThucChayNhanHangCore_NoiBo_KhongHD]
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @DmNhanHangREF INT,
	        @TenNhanHang NVARCHAR(200)
	
	DECLARE @DsNganhHangREF  NVARCHAR(100),
	        @DsTenNganhHang  NVARCHAR(200)
	
	SET @DmNhanHangREF = 0
	SET @TenNhanHang = ''
	SET @DsNganhHangREF = '0'
	SET @DsTenNganhHang = ''
	
	
	INSERT INTO DoanhSoThucChayNhanHangCore
	SELECT A.NgayThucHien,
	       A.DmNhanHangREF,
	       A.TenNhanHang,
	       A.DsNganhHangREF,
	       A.DsTenNganhHang,
	       A.HopDongID,
	       A.SoHopDong,
	       A.TenNhanVien,
	       A.SysNhanVienREF,
	       A.HopDongChiTietREF,
	       A.TenSanPham,
	       A.DmSanPhamREF,
	       A.TenWebsite,
	       A.DmWebsiteREF,
	       0 ThucThuPhatSinhDauKy,
	       0 ThucThuPhatSinhTrongKy,
	       0 ThucThuPhatSinhCuoiKy,
	       0 KhuyenMaiPhatSinhDauKy,
	       0 KhuyenMaiPhatSinhTrongKy,
	       0 KhuyenMaiPhatSinhCuoiKy,
	       0 NoiBoPhatSinhDauKy,
	       SUM(A.NoiBoPhatSinhTrongKy) NoiBoPhatSinhTrongKy,
	       0 NoiBoPhatSinhCuoiKy,
	       
	       0 SoLuongPhatSinhDauKy,
		   0 SoLuongPhatSinhTrongKy,
		   0 SoLuongPhatSinhCuoiKy,
			
		   0 SoLuongKhuyenMaiPhatSinhDauKy,
		   0 SoLuongKhuyenMaiPhatSinhTrongKy,
		   0 SoLuongKhuyenMaiPhatSinhCuoiKy,
			
		   0	SoLuongNoiBoPhatSinhDauKy,
			SUM(A.SoLuongNBPhatSinh) SoLuongNoiBoPhatSinhTrongKy,
			0	SoLuongNoiBoPhatSinhCuoiKy,
	       
	       '' DienGiai,
	       'ASD' CreatedBy,
	       GETDATE() CreatedAt,
	       'ASD' LastModifiedBy,
	       GETDATE() LastModifiedAt,
	       0 DeletedStatus,
	       0 PrintStatus,
	       0 RecordStatus,
	       '' TenDangNhap,
		   0 DmPhongBanREF,
		   0 DmBoPhanREF,
		   0 DmNhomLamViecREF,
		   A.Nam,
		   A.Quy,
		   A.Thang,
		   ''
		   ,A.DmDiaDiemLamViecREF
			,A.TenDiaDiemLamViec
			,0 DmKhachHangREF
			,'' TenKhachHang
	FROM   (
	           SELECT @NgayThucHien NgayThucHien,
	                  @DmNhanHangREF DmNhanHangREF,
	                  @TenNhanHang TenNhanHang,
	                  @DsNganhHangREF DsNganhHangREF,
	                  @DsTenNganhHang DsTenNganhHang,
	                  tcdt.HopDongID,
	                  tcdt.SoHopDong,
	                  tcdt.TenNhanVien,
	                  tcdt.SysNhanVienREF,
	                  tcdt.HopDongChiTietREF HopDongChiTietREF,
	                  tcdt.TenSanPham,
	                  tcdt.DmSanPhamREF,
	                  tcdt.TenWebsite,
	                  tcdt.DmWebsiteREF,
	                  YEAR(@NgayThucHien) Nam,
					  MONTH(@NgayThucHien) Thang,
					  DATEPART(QQ,@NgayThucHien) Quy,
	                  0 AS NoiBoPhatSinhDauKy,
	                  SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS 
	                  NoiBoPhatSinhTrongKy,
	                  0 AS NoiBoPhatSinhCuoiKy,
	                  SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi) AS SoLuongNBPhatSinh
	                  ,tcdt.DmDiaDiemLamViecREF
					  ,tcdt.TenDiaDiemLamViec
	           FROM   ThucChayDaTinh tcdt
	           WHERE  tcdt.HopDongID = 0
	                  AND (
	                          tcdt.DmSanPhamREF NOT IN (299, 337, 299, 144, 585,628)
	                          AND NOT(tcdt.DmSanPhamREF = 375 AND YEAR(tcdt.NgayThucHien) = 2013)
	                      )
	                  AND Convert(date,tcdt.NgayThucHien) = @NgayThucHien
	                  AND [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](tcdt.DmMaHopDongREF,@NgayThucHien) >0
	           GROUP BY
	                  tcdt.HopDongID,
	                  tcdt.SoHopDong,
	                  tcdt.TenNhanVien,
	                  tcdt.SysNhanVienREF,
	                  tcdt.HopDongChiTietREF,
	                  tcdt.TenSanPham,
	                  tcdt.DmSanPhamREF,
	                  tcdt.TenWebsite,
	                  tcdt.DmWebsiteREF,
	                  tcdt.DmDiaDiemLamViecREF
					  ,tcdt.TenDiaDiemLamViec
	           UNION
	           SELECT @NgayThucHien NgayThucHien,
	                  @DmNhanHangREF DmNhanHangREF,
	                  @TenNhanHang TenNhanHang,
	                  @DsNganhHangREF DsNganhHangREF,
	                  @DsTenNganhHang DsTenNganhHang,
	                  tcdt.HopDongID,
	                  tcdt.SoHopDong,
	                  tcdt.TenNhanVien,
	                  tcdt.SysNhanVienREF,
	                  tcdt.HopDongChiTietREF HopDongChiTietREF,
	                  tcdt.TenSanPham,
	                  tcdt.DmSanPhamREF,
	                  tcdt.TenWebsite,
	                  tcdt.DmWebsiteREF,
	                  YEAR(@NgayThucHien) Nam,
					  MONTH(@NgayThucHien) Thang,
					  DATEPART(QQ,@NgayThucHien) Quy,
					  0 AS NoiBoPhatSinhDauKy,
	                  SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS 
	                  NoiBoPhatSinhTrongKy,
	                  0 AS NoiBoPhatSinhCuoiKy,
	                  SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi) AS SoLuongNBPhatSinh
	                  ,tcdt.DmDiaDiemLamViecREF
					,tcdt.TenDiaDiemLamViec
	           FROM   ThucChayDaTinhAdmarket tcdt
	           WHERE  tcdt.HopDongID = 0
	                  AND tcdt.DmSanPhamREF IN (299, 337, 299, 144, 585,375,628)--LA CAC SANPHAM CUA ADMARKET
	                  AND Convert(date,tcdt.NgayThucHien) = @NgayThucHien
	                  AND [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](tcdt.DmMaHopDongREF,@NgayThucHien) >0
	           GROUP BY
	                  tcdt.HopDongID,
	                  tcdt.SoHopDong,
	                  tcdt.TenNhanVien,
	                  tcdt.SysNhanVienREF,
	                  tcdt.HopDongChiTietREF,
	                  tcdt.TenSanPham,
	                  tcdt.DmSanPhamREF,
	                  tcdt.TenWebsite,
	                  tcdt.DmWebsiteREF
	                  ,tcdt.DmDiaDiemLamViecREF
					  ,tcdt.TenDiaDiemLamViec
	       )A
	WHERE  ROUND(A.NoiBoPhatSinhTrongKy, 0) <> 0
	GROUP BY
	       A.NgayThucHien,
	       A.DmNhanHangREF,
	       A.TenNhanHang,
	       A.DsNganhHangREF,
	       A.DsTenNganhHang,
	       A.HopDongID,
	       A.SoHopDong,
	       A.TenNhanVien,
	       A.SysNhanVienREF,
	       A.HopDongChiTietREF,
	       A.TenSanPham,
	       A.DmSanPhamREF,
	       A.TenWebsite,
	       A.DmWebsiteREF,
	       A.Nam,
		   A.Quy,
		   A.Thang
		   ,A.DmDiaDiemLamViecREF
			,A.TenDiaDiemLamViec

END

--EXEC [Insert_DoanhSoThucChayNhanHangCore_KhongHD] '2013-12-31'

```
