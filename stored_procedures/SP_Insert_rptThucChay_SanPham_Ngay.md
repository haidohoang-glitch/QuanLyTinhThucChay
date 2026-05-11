# Stored Procedure: `Insert_rptThucChay_SanPham_Ngay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-27 17:44:01.467000
- **Ngày sửa cuối**: 2015-03-27 17:44:01.467000

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

--EXEC Insert_rptThucChay_SanPham_Ngay '2013-01-01', '2013-01-15'
CREATE PROCEDURE [dbo].[Insert_rptThucChay_SanPham_Ngay]
	@FromDate DATETIME,
	@ToDate DATETIME
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = @FromDate
	DELETE 
	FROM   rptThucChay_SanPham_Ngay
	WHERE  1 = 1
	       AND NgayThucHien BETWEEN @FromDate AND @ToDate
	
	WHILE @NgayThucHien <= @ToDate
	BEGIN
	    INSERT INTO rptThucChay_SanPham_Ngay
	    SELECT dstchdc.NgayThucHien,
	           dstchdc.DmSanPhamREF,
	           dstchdc.TenSanPham,
	          
	           [dbo].[fn_GetDauKy_Of_Ngay_SanPham] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmSanPhamREF,
			     @NgayThucHien,
			      1,0
				) ThucChayPhatSinhDauKy,
	           SUM(dstchdc.ThucChayPhatSinhTrongKy)ThucChayPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_SanPham] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmSanPhamREF,
			      @NgayThucHien,
			      1,0
				)+ SUM(dstchdc.ThucChayPhatSinhTrongKy)
				AS ThucChayPhatSinhCuoiKy,
				
	            [dbo].[fn_GetDauKy_Of_Ngay_SanPham] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmSanPhamREF,
			      @NgayThucHien,
			      2,0
				) KhuyenMaiPhatSinhDauKy,
	           SUM(dstchdc.KhuyenMaiPhatSinhTrongKy)KhuyenMaiPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_SanPham] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmSanPhamREF,
			      @NgayThucHien,
			      2,0
				) + SUM(dstchdc.KhuyenMaiPhatSinhTrongKy)
	           AS KhuyenMaiPhatSinhCuoiKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_SanPham] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmSanPhamREF,
			      @NgayThucHien,
			      3,0
				) AS NoiBoPhatSinhDauKy,
	           SUM(dstchdc.NoiBoPhatSinhTrongKy)NoiBoPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_SanPham] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmSanPhamREF,
			      @NgayThucHien,
			      3,0
				) + SUM(dstchdc.NoiBoPhatSinhTrongKy)
				AS NoiBoPhatSinhCuoiKy,
	           'ASD' CreatedBy,
	           GETDATE() CreatedAt,
	           'ASD' LastModifiedBy,
	           GETDATE() LastModifiedAt,
	           0 DeletedStatus,
	           0 RecordStatus,
	           0 PrintStatus,
	          [dbo].[fn_GetDauKy_Of_Ngay_SanPham] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,

                 dstchdc.DmSanPhamREF,
			      @NgayThucHien,
			      1,1
				) SoLuongPhatSinhDauKy,
	           SUM(dstchdc.SoLuongPhatSinhTrongKy)SoLuongPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_SanPham] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmSanPhamREF,
			      @NgayThucHien,
			      1,1
				)+ SUM(dstchdc.SoLuongPhatSinhTrongKy)
				AS SoLuongPhatSinhCuoiKy,
				
	            [dbo].[fn_GetDauKy_Of_Ngay_SanPham] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmSanPhamREF,
			      @NgayThucHien,
			      2,1
				) SoLuongKhuyenMaiPhatSinhDauKy,
	           SUM(dstchdc.SoLuongKhuyenMaiPhatSinhTrongKy)SoLuongKhuyenMaiPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_SanPham] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmSanPhamREF,
			      @NgayThucHien,
			      2,1
				) + SUM(dstchdc.SoLuongKhuyenMaiPhatSinhTrongKy)
	           AS SoLuongKhuyenMaiPhatSinhCuoiKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_SanPham] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmSanPhamREF,
			      @NgayThucHien,
			      3,1
				) AS SoLuongNoiBoPhatSinhDauKy,
	           SUM(dstchdc.SoLuongNoiBoPhatSinhTrongKy)NoiBoPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_SanPham] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmSanPhamREF,
			      @NgayThucHien,
			      3,1
				) + SUM(dstchdc.SoLuongNoiBoPhatSinhTrongKy)
				AS SoLuongNoiBoPhatSinhCuoiKy,
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
				SUM(dstchdc.ThucChayThayDoiTrongKy),
				SUM(dstchdc.NoiBoThayDoiTrongKy),
				SUM(dstchdc.KhuyenMaiThayDoiTrongKy),
				SUM(dstchdc.SoLuongThayDoiTrongKy),
				SUM(dstchdc.SoLuongNoiBoThayDoiTrongKy),
				SUM(dstchdc.SoLuongKhuyenMaiThayDoiTrongKy)
	    FROM   DoanhSoThucChayWebsiteTheoThoiGian dstchdc
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
	           dstchdc.TenSanPham,
	           dstchdc.DmSanPhamREF
	    
	    PRINT @NgayThucHien
	    
	    SET @NgayThucHien = DATEADD(DAY, 1, @NgayThucHien)
	END
END

```
