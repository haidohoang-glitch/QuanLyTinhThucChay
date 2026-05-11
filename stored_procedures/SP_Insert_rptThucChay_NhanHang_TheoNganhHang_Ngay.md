# Stored Procedure: `Insert_rptThucChay_NhanHang_TheoNganhHang_Ngay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-31 11:21:06.323000
- **Ngày sửa cuối**: 2015-03-31 11:21:06.323000

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

--EXEC Insert_rptThucChay_NhanHang_Ngay '2013-01-01', '2013-01-15'
CREATE PROCEDURE [dbo].[Insert_rptThucChay_NhanHang_TheoNganhHang_Ngay]
	@FromDate DATETIME,
	@ToDate DATETIME
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = @FromDate
	DELETE 
	FROM   rptThucChay_NhanHang_TheoNganhHang_Ngay
	WHERE  1 = 1
	       AND NgayThucHien BETWEEN @FromDate AND @ToDate
	
	WHILE @NgayThucHien <= @ToDate
	BEGIN
	    INSERT INTO rptThucChay_NhanHang_TheoNganhHang_Ngay
	    SELECT dstchdc.NgayThucHien,
	           dstchdc.TenNhanHang,
	           dstchdc.DmNhanHangREF,
	           dstchdc.TenNhanVien,
	           dstchdc.DmNhanVienREF,
	           dstchdc.TenPhongBan,
	           dstchdc.PhongBanREF,
	           dstchdc.TenBoPhan,
	           dstchdc.BoPhanREF,
	           dstchdc.TenNhom,
	           dstchdc.NhomREF,
	           dstchdc.DsTenNganhHang,
	           dstchdc.DmListNganhHangREF,
	           [dbo].[fn_GetDauKy_Of_Ngay_NhanHangTheoNganhHang] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmNhanHangREF,
			     @NgayThucHien,
			      1,0,
			     DmListNganhHangREF
				) ThucChayPhatSinhDauKy,
	           SUM(dstchdc.ThucChayPhatSinhTrongKy)ThucChayPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_NhanHangTheoNganhHang] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmNhanHangREF,
			      @NgayThucHien,
			      1,0,
			      DmListNganhHangREF
				)+ SUM(dstchdc.ThucChayPhatSinhTrongKy)
				AS ThucChayPhatSinhCuoiKy,
				
	            [dbo].[fn_GetDauKy_Of_Ngay_NhanHangTheoNganhHang] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmNhanHangREF,
			      @NgayThucHien,
			      2,0,DmListNganhHangREF
				) KhuyenMaiPhatSinhDauKy,
	           SUM(dstchdc.KhuyenMaiPhatSinhTrongKy)KhuyenMaiPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_NhanHangTheoNganhHang] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmNhanHangREF,
			      @NgayThucHien,
			      2,0,DmListNganhHangREF
				) + SUM(dstchdc.KhuyenMaiPhatSinhTrongKy)
	           AS KhuyenMaiPhatSinhCuoiKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_NhanHangTheoNganhHang] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmNhanHangREF,
			      @NgayThucHien,
			      3,0,DmListNganhHangREF
				) AS NoiBoPhatSinhDauKy,
	           SUM(dstchdc.NoiBoPhatSinhTrongKy)NoiBoPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_NhanHangTheoNganhHang] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmNhanHangREF,
			      @NgayThucHien,
			      3,0,DmListNganhHangREF
				) + SUM(dstchdc.NoiBoPhatSinhTrongKy)
				AS NoiBoPhatSinhCuoiKy,
	           'ASD' CreatedBy,
	           GETDATE() CreatedAt,
	           'ASD' LastModifiedBy,
	           GETDATE() LastModifiedAt,
	           0 DeletedStatus,
	           0 RecordStatus,
	           0 PrintStatus,
	          [dbo].[fn_GetDauKy_Of_Ngay_NhanHangTheoNganhHang] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,

                 dstchdc.DmNhanHangREF,
			      @NgayThucHien,
			      1,1,DmListNganhHangREF
				) SoLuongPhatSinhDauKy,
	           SUM(dstchdc.SoLuongPhatSinhTrongKy)SoLuongPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_NhanHangTheoNganhHang] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmNhanHangREF,
			      @NgayThucHien,
			      1,1,DmListNganhHangREF
				)+ SUM(dstchdc.SoLuongPhatSinhTrongKy)
				AS SoLuongPhatSinhCuoiKy,
				
	            [dbo].[fn_GetDauKy_Of_Ngay_NhanHangTheoNganhHang] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmNhanHangREF,
			      @NgayThucHien,
			      2,1,DmListNganhHangREF
				) SoLuongKhuyenMaiPhatSinhDauKy,
	           SUM(dstchdc.SoLuongKhuyenMaiPhatSinhTrongKy)SoLuongKhuyenMaiPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_NhanHangTheoNganhHang] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmNhanHangREF,
			      @NgayThucHien,
			      2,1,DmListNganhHangREF
				) + SUM(dstchdc.SoLuongKhuyenMaiPhatSinhTrongKy)
	           AS SoLuongKhuyenMaiPhatSinhCuoiKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_NhanHangTheoNganhHang] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmNhanHangREF,
			      @NgayThucHien,
			      3,1,DmListNganhHangREF
				) AS SoLuongNoiBoPhatSinhDauKy,
	           SUM(dstchdc.SoLuongNoiBoPhatSinhTrongKy)NoiBoPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_NhanHangTheoNganhHang] 
				(
				dstchdc.DmNhanVienREF,
				dstchdc.PhongBanREF,
				dstchdc.BoPhanREF,
				dstchdc.NhomREF,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
                 dstchdc.DmNhanHangREF,
			      @NgayThucHien,
			      3,1,DmListNganhHangREF
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
	    FROM   DoanhSoThucChayNhanHangCore dstchdc
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
	           dstchdc.TenNhanHang,
	           dstchdc.DmNhanHangREF,
	           dstchdc.DsTenNganhHang,
	           dstchdc.DmListNganhHangREF
	    PRINT @NgayThucHien
	    
	    SET @NgayThucHien = DATEADD(DAY, 1, @NgayThucHien)
	END
END

```
