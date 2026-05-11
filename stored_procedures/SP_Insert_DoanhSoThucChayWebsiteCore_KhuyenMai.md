# Stored Procedure: `Insert_DoanhSoThucChayWebsiteCore_KhuyenMai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-23 11:21:35.570000
- **Ngày sửa cuối**: 2014-12-23 11:21:35.570000

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
CREATE PROCEDURE [dbo].[Insert_DoanhSoThucChayWebsiteCore_KhuyenMai]
	@NgayThucHien DATETIME
AS
BEGIN
	DELETE 	FROM   DoanhSoThucChayWebsiteCore
	WHERE  1 = 1
	       AND (
	               KhuyenMaiPhatSinhDauKy <> 0
	               OR KhuyenMaiPhatSinhTrongKy <> 0
	               OR KhuyenMaiPhatSinhCuoiKy <> 0
	           )
	       AND NgayThucHien = @NgayThucHien
	
	INSERT INTO DoanhSoThucChayWebsiteCore
	SELECT tcdt.NgayThucHien,
	       tcdt.DmSanPhamREF,
	       tcdt.TenSanPham,
	       tcdt.TenWebsite,
	       tcdt.DmWebsiteREF,
	       '' DienGiai,
	       0 ThucThuDauKy,
	       0 ThucThuTrongKy,
	       0 ThucThuCuoiKy,
	       [dbo].[fn_GetDoanhSoDauKy_Of_DoanhSoThucChayWebsiteCore](
	       	2, @NgayThucHien, tcdt.DmSanPhamREF, tcdt.DmWebsiteREF
	       ) AS 
	       KhuyenMaiDauKy,
	       SUM(
	           tcdt.ThanhTienThucChayTruocTrietKhau + tcdt.GiaTriKMThayDoi
	       ) AS KhuyenMaiTrongKy,
	       (
	           [dbo].[fn_GetDoanhSoDauKy_Of_DoanhSoThucChayWebsiteCore](
	           	1, @NgayThucHien, tcdt.DmSanPhamREF, tcdt.DmWebsiteREF
	           ) 
	           + SUM(tcdt.ThanhTienThucChayTruocTrietKhau + tcdt.GiaTriKMThayDoi)
	       ) KhuyenMaiCuoiKy,
	       0 NoiBoDauKy,
	       0 NoiBoTrongKy,
	       0 NoiBoCuoiKy,
	       'Admin' CreatedBy,
	       GETDATE() CreatedAt,
	       'Admin' LastModifiedBy,
	       GETDATE() LastModifiedAt,
	       0 DeletedStatus,
	       0 RecordStatus,
	       0 PrintStatus
	FROM   ThucChayDaTinh tcdt
	       INNER JOIN HopDong hd
	            ON  tcdt.HopDongID = hd.HopDongID
	       INNER JOIN KhachHangThongTinChung khttc
	            ON  khttc.KhachHangThongTinChungID = hd.DmKhachHangREF
	       LEFT JOIN HopDongChiTiet hdct
	            ON  hdct.HopDongChiTietID = tcdt.HopDongChiTietREF
	WHERE  1 = 1
	       --AND tcdt.DmSanPhamREF NOT IN (299,337,299,144,585)--//Danh sach cac san pham cua Admarket
	       AND tcdt.NgayThucHien = @NgayThucHien
	       AND (tcdt.ChietKhau = 100 OR tcdt.IsKhuyenMai = 1)
	GROUP BY
	       tcdt.NgayThucHien,
	       tcdt.DmSanPhamREF,
	       tcdt.TenSanPham,
	       tcdt.TenWebsite,
	       tcdt.DmWebsiteREF
END

```
