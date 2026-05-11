# Stored Procedure: `Insert_RptNhanHangThucChayFull_ThucThuKhuyenMai_KhongHD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-02-12 11:19:43.983000
- **Ngày sửa cuối**: 2015-02-12 11:22:14.967000

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

--EXEC [Insert_RptNhanHangThucChayFull_ThucThuKhuyenMai_KhongHD] '2013-12-31'

CREATE PROCEDURE [dbo].[Insert_RptNhanHangThucChayFull_ThucThuKhuyenMai_KhongHD]
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
	
	
	INSERT INTO RptNhanHangThucChayFull
	SELECT A.DmNhanHangREF,A.TenNhanHang,A.HopDongID,A.SoHopDong
	,A.HopDongChiTietREF,A.DmSanPhamREF,A.TenSanPham
	,0 DmKenhREF
	,'' TenKenh
	,A.NgayThucHien,A.DonViTinh DonViTinh
	,SUM(A.SoLuontThucChay) SoLuongThucChay
    ,SUM(A.ThucThuPhatSinhTrongKy)ThucThuPhatSinhTrongKy
    ,'ASD' CreatedBy
    ,GETDATE() CreatedAt
    ,0 RecordStatus
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
	                  tcdt.DonViTinh,
	                  tcdt.TenSanPham,
	                  tcdt.DmSanPhamREF,
	                  tcdt.TenWebsite,
	                  tcdt.DmWebsiteREF,
	                  0 AS ThucThuPhatSinhDauKy,
	                  SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS 
	                  ThucThuPhatSinhTrongKy,
	                  SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi) AS SoLuontThucChay,
	                  0 AS ThucThuPhatSinhCuoiKy,
	                  0 AS KhuyenMaiPhatSinhDauKy,
	                  SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) AS
	                  KhuyenMaiPhatSinhTrongKy,
	                  0 AS KhuyenMaiPhatSinhCuoiKy
	           FROM   ThucChayDaTinh tcdt
	           WHERE  tcdt.HopDongID = 0
	                  AND tcdt.DmSanPhamREF NOT IN (299,337,299,144,585) AND NOT(tcdt.DmSanPhamREF = 375 AND YEAR(tcdt.NgayThucHien) = 2013)--KHONG PHAI LA CAC SANPHAM CUA ADMARKET
	                  AND Convert(date,tcdt.NgayThucHien) = @NgayThucHien
	                  AND [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](tcdt.DmMaHopDongREF,@NgayThucHien) =0
	           GROUP BY
	                  tcdt.HopDongID,
	                  tcdt.SoHopDong,
	                  tcdt.TenNhanVien,
	                  tcdt.SysNhanVienREF,
	                  tcdt.HopDongChiTietREF,
	                  tcdt.TenSanPham,
	                  tcdt.DmSanPhamREF,
	                  tcdt.TenWebsite,
	                  tcdt.DmWebsiteREF ,
	                  tcdt.DonViTinh
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
	                  tcdt.DonViTinh,
	                  tcdt.TenSanPham,
	                  tcdt.DmSanPhamREF,
	                  tcdt.TenWebsite,
	                  tcdt.DmWebsiteREF,
	                  0 AS ThucThuPhatSinhDauKy,
	                  SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS 
	                  ThucThuPhatSinhTrongKy,
	                  SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi) AS SoLuontThucChay,
	                  0 AS ThucThuPhatSinhCuoiKy,
	                  0 AS KhuyenMaiPhatSinhDauKy,
	                  SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) AS
	                  KhuyenMaiPhatSinhTrongKy,
	                  0 AS KhuyenMaiPhatSinhCuoiKy
	           FROM   ThucChayDaTinhAdmarket tcdt
	           WHERE  tcdt.HopDongID = 0
	                  AND tcdt.DmSanPhamREF IN (299, 337, 299, 144, 585,375)--LA CAC SANPHAM CUA ADMARKET
	                  AND Convert(date,tcdt.NgayThucHien) = @NgayThucHien
	                  AND [dbo].[fn_CheckIsDmLoaiHopDongNoiBo](tcdt.DmMaHopDongREF,@NgayThucHien) =0
	           GROUP BY
	                  tcdt.HopDongID,
	                  tcdt.SoHopDong,
	                  tcdt.TenNhanVien,
	                  tcdt.SysNhanVienREF,
	                  tcdt.HopDongChiTietREF,
	                  tcdt.TenSanPham,
	                  tcdt.DmSanPhamREF,
	                  tcdt.TenWebsite,
	                  tcdt.DmWebsiteREF ,
	                  tcdt.DonViTinh
	       )A
	WHERE  (ROUND(A.ThucThuPhatSinhTrongKy, 0) <> 0 )
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
	       A.DonViTinh

END

--EXEC [Insert_RptNhanHangThucChayFull_ThucThuKhuyenMai_KhongHD] '2013-12-31'

```
