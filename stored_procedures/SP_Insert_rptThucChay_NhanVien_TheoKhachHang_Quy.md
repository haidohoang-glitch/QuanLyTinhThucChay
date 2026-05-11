# Stored Procedure: `Insert_rptThucChay_NhanVien_TheoKhachHang_Quy`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-07 12:18:44.180000
- **Ngày sửa cuối**: 2015-03-07 12:18:44.180000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author  Name>
-- Create date: <Create Date  >
-- Description:	<Description  >
-- =============================================
CREATE PROCEDURE [dbo].[Insert_rptThucChay_NhanVien_TheoKhachHang_Quy]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	DECLARE @TeampData TABLE 
	   (
			TenNhanVien NVARCHAR(200),
			DmNhanVienREF INT,
			SoDienThoai NVARCHAR(20),
		    TenPhongBan NVARCHAR(200),
			PhongBanREF INT,
			TenBoPhan NVARCHAR(200),
			BoPhanREF INT,
			TenNhom NVARCHAR(200),
		    NhomREF INT,
		    TenKhachHang NVARCHAR(200),
		    DmKhachHangREF INT,
		    DmHinhThucKhachHang INT,
		    SoDienThoaiKhachHang NVARCHAR(20),
			ThucChayPhatSinhTrongKy FLOAT,
			KhuyenMaiPhatSinhTrongKy FLOAT,
			NoiBoPhatSinhTrongKy FLOAT,
			SoLuongPhatSinhTrongKy BIGINT,
			SoLuongKhuyenMaiPhatSinhTrongKy BIGINT,
			SoLuongNoiBoPhatSinhTrongKy BIGINT,
			Quy INT,
			Nam INT,
			TrangThai INT 
		)
    -----------------------------Du lieu phat sinh-----
     INSERT INTO @TeampData
	 SELECT DISTINCT
		       rtchdn.TenNhanVien,
		       rtchdn.DmNhanVienREF,
		       '' as Mobile,
		       rtchdn.TenPhongBan,
		       rtchdn.PhongBanREF,
		       rtchdn.TenBoPhan,
		       rtchdn.BoPhanREF,
		       rtchdn.TenNhom,
		       rtchdn.NhomREF,
		       rtchdn.TenKhachHang,
		       rtchdn.DmKhachHangREF,
		       rtchdn.DmHinhThucKhachHangREF,
		       '' as Mobile,
		       SUM(rtchdn.ThucChayPhatSinhTrongKy),
		       SUM(rtchdn.KhuyenMaiPhatSinhTrongKy),
		       SUM(rtchdn.NoiBoPhatSinhTrongKy),
		       SUM(rtchdn.SoLuongPhatSinhTrongKy),
			   SUM(rtchdn.SoLuongKhuyenMaiPhatSinhTrongKy),
			   SUM(rtchdn.SoLuongNoiBoPhatSinhTrongKy),
		       DATEPART(QQ,@NgayThucHien),
		       YEAR(@NgayThucHien),
		       0
			 FROM  DoanhSoThucChayHopDongTheoThoiGian rtchdn
			
			 WHERE 1=1 AND rtchdn.NgayThucHien = @NgayThucHien
	     GROUP BY
	           rtchdn.TenNhanVien,
		       rtchdn.DmNhanVienREF,
		       rtchdn.TenPhongBan,
		       rtchdn.PhongBanREF,
		       rtchdn.TenBoPhan,
		       rtchdn.BoPhanREF,
		       rtchdn.TenNhom,
		       rtchdn.NhomREF,
		       rtchdn.TenKhachHang,
		       rtchdn.DmKhachHangREF,
		       rtchdn.DmHinhThucKhachHangREF
	---------------------------------UPDATE DL----------------------------------------
	UPDATE rptThucChay_NhanVien_TheoKhachHang_Quy
	SET NgayThucHien = @NgayThucHien,
	 ThucChayPhatSinhTrongKy += td.ThucChayPhatSinhTrongKy,
	 ThucChayPhatSinhCuoiKy += td.ThucChayPhatSinhTrongKy,
	 KhuyenMaiPhatSinhTrongKy += td.KhuyenMaiPhatSinhTrongKy,
	 KhuyenMaiPhatSinhCuoiKy += td.KhuyenMaiPhatSinhTrongKy,
     NoiBoPhatSinhTrongKy += td.NoiBoPhatSinhTrongKy,
	 NoiBoPhatSinhCuoiKy += td.NoiBoPhatSinhTrongKy,
	 SoLuongPhatSinhTrongKy += td.SoLuongPhatSinhTrongKy,
	        SoLuongPhatSinhCuoiKy += td.SoLuongPhatSinhTrongKy,
			SoLuongKhuyenMaiPhatSinhTrongKy += td.SoLuongKhuyenMaiPhatSinhTrongKy,
			SoLuongKhuyenMaiPhatSinhCuoiKy += td.SoLuongKhuyenMaiPhatSinhTrongKy,
			SoLuongNoiBoPhatSinhTrongKy +=td.SoLuongNoiBoPhatSinhTrongKy,
			SoLuongNoiBoPhatSinhCuoiKy += td.SoLuongNoiBoPhatSinhTrongKy  
	FROM rptThucChay_NhanVien_TheoKhachHang_Quy r
	INNER JOIN @TeampData td ON
	td.DmNhanVienREF = r.DmNhanVienREF
	AND td.PhongBanREF = r.PhongBanREF
	AND td.BoPhanREF = r.BoPhanREF
	AND td.NhomREF = r.NhomREF
		AND td.DmKhachHangREF = r.DmKhachHangREF
	AND td.Nam = r.Nam
	AND td.Quy = r.Quy
	
	UPDATE @TeampData
	SET TrangThai =1
	FROM rptThucChay_NhanVien_TheoKhachHang_Quy r
	INNER JOIN @TeampData td ON
	td.DmNhanVienREF = r.DmNhanVienREF
	AND td.PhongBanREF = r.PhongBanREF
	AND td.BoPhanREF = r.BoPhanREF
	AND td.NhomREF = r.NhomREF
		AND td.DmKhachHangREF = r.DmKhachHangREF
	AND td.Nam = r.Nam
	AND td.Quy = r.Quy
	-----------------------------------------INSERT---------------------------------------
	INSERT INTO rptThucChay_NhanVien_TheoKhachHang_Quy
				SELECT 
				@NgayThucHien,
				td.Quy,
				td.Nam,
			    td.TenNhanVien, 
	           td.DmNhanVienREF ,
	           td.SoDienThoai ,
	           td.TenPhongBan,
	           td.PhongBanREF ,
	           td.TenBoPhan ,
	           td.BoPhanREF ,
	           td.TenNhom ,
	           td.NhomREF ,
	           td.TenKhachHang,
	           td.DmKhachHangREF,
	           td.DmHinhThucKhachHang,
	           td.SoDienThoaiKhachHang,
	           '',
				[dbo].[fn_GetDauKy_Of_Quy_NhanVienTheoKhachHang]
				(
				  td.DmNhanVienREF ,
				  td.PhongBanREF ,
				  td.BoPhanREF ,
				  td.NhomREF ,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHang,
			      @NgayThucHien,
			      1,0
				) ThucChayPhatSinhDauKy,
	            td.ThucChayPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Quy_NhanVienTheoKhachHang]
				(
				   td.DmNhanVienREF ,
				  td.PhongBanREF ,
				  td.BoPhanREF ,
				  td.NhomREF ,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHang,
			      @NgayThucHien,
			      1,0
				)
	            + td.ThucChayPhatSinhTrongKy
	            ) ThucChayPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Quy_NhanVienTheoKhachHang]
				(
				  td.DmNhanVienREF ,
				  td.PhongBanREF ,
				  td.BoPhanREF ,
				  td.NhomREF ,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHang,
			      @NgayThucHien,
			      2,0
				) KhuyenMaiPhatSinhDauKy,
	            td.KhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Quy_NhanVienTheoKhachHang]
				(	
				  td.DmNhanVienREF ,
				  td.PhongBanREF ,
				  td.BoPhanREF ,
				  td.NhomREF ,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHang,
			      @NgayThucHien,
			      2,0
				)+ td.KhuyenMaiPhatSinhTrongKy
	            ) KhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Quy_NhanVienTheoKhachHang]
				(	
				  td.DmNhanVienREF ,
				  td.PhongBanREF ,
				  td.BoPhanREF ,
				  td.NhomREF ,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHang,
			      @NgayThucHien,
			      3,0
				) NoiBoPhatSinhDauKy,
	            td.NoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Quy_NhanVienTheoKhachHang]
				(	
				  td.DmNhanVienREF ,
				  td.PhongBanREF ,
				  td.BoPhanREF ,
				  td.NhomREF ,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHang,
			      @NgayThucHien,
			      3,0
				) + td.NoiBoPhatSinhTrongKy
	            ) NoiBoPhatSinhCuoiKy,
	           'ASD' CreatedBy,
	           GETDATE() CreatedAt,
	           'ASD' LastModifiedBy,
	           GETDATE() LastModifiedAt,
	           0 DeletedStatus,
	           0 RecordStatus,
	           0 PrintStatus,
	           [dbo].[fn_GetDauKy_Of_Quy_NhanVienTheoKhachHang]
				(
				  td.DmNhanVienREF ,
				  td.PhongBanREF ,
				  td.BoPhanREF ,
				  td.NhomREF ,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHang,
			      @NgayThucHien,
			      1,1
				) SoLuongPhatSinhDauKy,
	            td.SoLuongPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Quy_NhanVienTheoKhachHang]
				(
				   td.DmNhanVienREF ,
				  td.PhongBanREF ,
				  td.BoPhanREF ,
				  td.NhomREF ,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHang,
			      @NgayThucHien,
			      1,1
				)
	            + td.SoLuongPhatSinhTrongKy
	            ) SoLuongPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Quy_NhanVienTheoKhachHang]
				(
				  td.DmNhanVienREF ,
				  td.PhongBanREF ,
				  td.BoPhanREF ,
				  td.NhomREF ,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHang,
			      @NgayThucHien,
			      2,1
				) SoLuongKhuyenMaiPhatSinhDauKy,
	            td.SoLuongKhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Quy_NhanVienTheoKhachHang]
				(	
				   td.DmNhanVienREF ,
				  td.PhongBanREF ,
				  td.BoPhanREF ,
				  td.NhomREF ,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHang,
			      @NgayThucHien,
			      2,1
				)+ td.SoLuongKhuyenMaiPhatSinhTrongKy
	            ) SoLuongKhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Quy_NhanVienTheoKhachHang]
				(	
				  td.DmNhanVienREF ,
				  td.PhongBanREF ,
				  td.BoPhanREF ,
				  td.NhomREF ,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHang,
			      @NgayThucHien,
			      3,1
				) SoluongNoiBoPhatSinhDauKy,
	            td.SoluongNoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Quy_NhanVienTheoKhachHang]
				(	
				  td.DmNhanVienREF ,
				  td.PhongBanREF ,
				  td.BoPhanREF ,
				  td.NhomREF ,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHang,
			      @NgayThucHien,
			      3,1
				) + td.SoLuongNoiBoPhatSinhTrongKy
	            ) SoLuongNoiBoPhatSinhCuoiKy
			 FROM  @TeampData td
				WHERE 1=1 
				AND TrangThai <> 1
END

```
