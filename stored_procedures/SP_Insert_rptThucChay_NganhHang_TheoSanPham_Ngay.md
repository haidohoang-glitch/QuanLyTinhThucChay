# Stored Procedure: `Insert_rptThucChay_NganhHang_TheoSanPham_Ngay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-31 11:21:05.047000
- **Ngày sửa cuối**: 2015-03-31 11:21:05.047000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [Insert_rptThucChay_NganhHang_TheoSanPham_Ngay] '2013-01-01', '2013-01-15'
CREATE PROCEDURE [dbo].[Insert_rptThucChay_NganhHang_TheoSanPham_Ngay]
	@FromDate DATETIME,
	@ToDate DATETIME
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = @FromDate
	DELETE 
	FROM   rptThucChay_NganhHang_TheoSanPham_Ngay
	WHERE  1 = 1
	       AND NgayThucHien BETWEEN @FromDate AND @ToDate
	
	WHILE @NgayThucHien <= @ToDate
	BEGIN
	    INSERT INTO rptThucChay_NganhHang_TheoSanPham_Ngay
	    SELECT dstchdc.NgayThucHien,
	           dstchdc.TenNganhHang,
	           dstchdc.DmNganhHangREF,
	           dstchdc.TenNhanVien,
	           dstchdc.DmNhanVienREF,
	           dstchdc.TenPhongBan,
	           dstchdc.PhongBanREF,
	           dstchdc.TenBoPhan,
	           dstchdc.BoPhanREF,
	           dstchdc.TenNhom,
	           dstchdc.NhomREF,
	           dstchdc.TenSanPham,
	           dstchdc.DmSanPhamREF,
	           [dbo].[fn_GetDauKy_Of_Ngay_NganhHangTheoSanPham] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmNganhHangREF,
			     @NgayThucHien,
			      1,0,
			     DmSanPhamREF
				) ThucChayPhatSinhDauKy,
	           SUM(dstchdc.ThucChayPhatSinhTrongKy)ThucChayPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_NganhHangTheoSanPham] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmNganhHangREF,
			      @NgayThucHien,
			      1,0,
			      DmSanPhamREF
				)+ SUM(dstchdc.ThucChayPhatSinhTrongKy)
				AS ThucChayPhatSinhCuoiKy,
				
	            [dbo].[fn_GetDauKy_Of_Ngay_NganhHangTheoSanPham] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmNganhHangREF,
			      @NgayThucHien,
			      2,0,DmSanPhamREF
				) KhuyenMaiPhatSinhDauKy,
	           SUM(dstchdc.KhuyenMaiPhatSinhTrongKy)KhuyenMaiPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_NganhHangTheoSanPham] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmNganhHangREF,
			      @NgayThucHien,
			      2,0,DmSanPhamREF
				) + SUM(dstchdc.KhuyenMaiPhatSinhTrongKy)
	           AS KhuyenMaiPhatSinhCuoiKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_NganhHangTheoSanPham] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmNganhHangREF,
			      @NgayThucHien,
			      3,0,DmSanPhamREF
				) AS NoiBoPhatSinhDauKy,
	           SUM(dstchdc.NoiBoPhatSinhTrongKy)NoiBoPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_NganhHangTheoSanPham] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmNganhHangREF,
			      @NgayThucHien,
			      3,0,DmSanPhamREF
				) + SUM(dstchdc.NoiBoPhatSinhTrongKy)
				AS NoiBoPhatSinhCuoiKy,
	           'ASD' CreatedBy,
	           GETDATE() CreatedAt,
	           'ASD' LastModifiedBy,
	           GETDATE() LastModifiedAt,
	           0 DeletedStatus,
	           0 RecordStatus,
	           0 PrintStatus,
	          [dbo].[fn_GetDauKy_Of_Ngay_NganhHangTheoSanPham] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,

                 dstchdc.DmNganhHangREF,
			      @NgayThucHien,
			      1,1,DmSanPhamREF
				) SoLuongPhatSinhDauKy,
	           SUM(dstchdc.SoLuongPhatSinhTrongKy)SoLuongPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_NganhHangTheoSanPham] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmNganhHangREF,
			      @NgayThucHien,
			      1,1,DmSanPhamREF
				)+ SUM(dstchdc.SoLuongPhatSinhTrongKy)
				AS SoLuongPhatSinhCuoiKy,
				
	            [dbo].[fn_GetDauKy_Of_Ngay_NganhHangTheoSanPham] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmNganhHangREF,
			      @NgayThucHien,
			      2,1,DmSanPhamREF
				) SoLuongKhuyenMaiPhatSinhDauKy,
	           SUM(dstchdc.SoLuongKhuyenMaiPhatSinhTrongKy)SoLuongKhuyenMaiPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_NganhHangTheoSanPham] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmNganhHangREF,
			      @NgayThucHien,
			      2,1,DmSanPhamREF
				) + SUM(dstchdc.SoLuongKhuyenMaiPhatSinhTrongKy)
	           AS SoLuongKhuyenMaiPhatSinhCuoiKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_NganhHangTheoSanPham] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmNganhHangREF,
			      @NgayThucHien,
			      3,1,DmSanPhamREF
				) AS SoLuongNoiBoPhatSinhDauKy,
	           SUM(dstchdc.SoLuongNoiBoPhatSinhTrongKy)NoiBoPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_NganhHangTheoSanPham] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmNganhHangREF,
			      @NgayThucHien,
			      3,1,DmSanPhamREF
				) + SUM(dstchdc.SoLuongNoiBoPhatSinhTrongKy)
				AS SoLuongNoiBoPhatSinhCuoiKy,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
				SUM(dstchdc.ThucChayThayDoiTrongKy),
				SUM(dstchdc.NoiBoThayDoiTrongKy),
				SUM(dstchdc.KhuyenMaiThayDoiTrongKy),
				SUM(dstchdc.SoLuongThayDoiTrongKy),
				SUM(dstchdc.SoLuongNoiBoThayDoiTrongKy),
				SUM(dstchdc.SoLuongKhuyenMaiThayDoiTrongKy)
	    FROM   DoanhSoThucChayNganhHangCore dstchdc
	    WHERE  dstchdc.NgayThucHien = @NgayThucHien
	    GROUP BY
	            dstchdc.TenNhanVien,
	            dstchdc.DmNhanVienREF,
	            dstchdc.TenPhongban,
				dstchdc.PhongBanREF,
				dstchdc.tenBoPhan,
				dstchdc.BoPhanREF,
				dstchdc.tenNhom,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
	           dstchdc.NgayThucHien,
	           dstchdc.TenNganhHang,
	           dstchdc.DmNganhHangREF,
	           dstchdc.TenSanPham,
	           dstchdc.DmSanPhamREF
	    PRINT @NgayThucHien
	    
	    SET @NgayThucHien = DATEADD(DAY, 1, @NgayThucHien)
	END
END

```
