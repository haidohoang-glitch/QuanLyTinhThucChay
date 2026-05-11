# Stored Procedure: `Insert_rptThucChay_KhachHang_Thang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-27 17:43:56.987000
- **Ngày sửa cuối**: 2015-03-27 17:43:56.987000

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
--EXEC [dbo].[Insert_rptThucChay_KhachHang_Thang] '2013-01-01'
CREATE PROCEDURE [dbo].[Insert_rptThucChay_KhachHang_Thang]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	 DECLARE @TeampData TABLE 
	   (
			TenKhachHang NVARCHAR(500),
			DmKhachHangREF INT,
			SoDienThoai NVARCHAR(200),
			TenHinhThucKhachHang NVARCHAR(200),
			ThucChayPhatSinhTrongKy FLOAT,
			KhuyenMaiPhatSinhTrongKy FLOAT,
			NoiBoPhatSinhTrongKy FLOAT,
			SoLuongPhatSinhTrongKy BIGINT,
			SoLuongKhuyenMaiPhatSinhTrongKy BIGINT,
			SoLuongNoiBoPhatSinhTrongKy BIGINT,
			TenNhanVien NVARCHAR(200),
			DmNhanVienREF INT,
			TenPhongBan NVARCHAR(200),
			PhongBanREF INT,
			TenBoPhan NVARCHAR(200),
			BoPhanREF INT,
			TenNhom NVARCHAR(200),
			NhomREF INT,
			TenDonViTinh NVARCHAR(50),
			Username NVARCHAR(50),
			ThucChayThayDoiTrongKy FLOAT,
			NoiBoThayDoiTrongKy FLOAT,
			KhuyenMaiThayDoiTrongKy FLOAT,
			SoLuongThayDoiTrongKy BIGINT,
			SoLuongNoiBoThayDoiTrongKy BIGINT,
			SoLuongKhuyenMaiThayDoiTrongKy BIGINT,
			Thang INT,
			Nam INT,
			TrangThai INT 
	   )
	  -------------du lieu phat sinh -----------------
	  INSERT INTO @TeampData
	  SELECT
	  rtchdn.TenKhachHang,
	  rtchdn.DmKhachHangREF,
	  '' as Mobile,
	  '' TenHinhThucKhachHang,
	  SUM(rtchdn.ThucChayPhatSinhTrongKy),
	  SUM(rtchdn.KhuyenMaiPhatSinhTrongKy),
	  SUM(rtchdn.NoiBoPhatSinhTrongKy),
	  SUM(rtchdn.SoLuongPhatSinhTrongKy),
	  SUM(rtchdn.SoLuongKhuyenMaiPhatSinhTrongKy),
	  SUM(rtchdn.SoLuongNoiBoPhatSinhTrongKy),
	  rtchdn.TenNhanVien,
	  rtchdn.DmNhanVienREF,
					rtchdn.TenPhongBan,
					rtchdn.PhongBanREF,
					rtchdn.TenBoPhan,
					rtchdn.BoPhanREF,
					rtchdn.TenNhom,
					rtchdn.NhomREF,
					rtchdn.TenDonViTinh,
					rtchdn.UserName,
					SUM(rtchdn.ThucChayThayDoiTrongKy),
					SUM(rtchdn.NoiBoThayDoiTrongKy),
					SUM(rtchdn.KhuyenMaiThayDoiTrongKy),
					SUM(rtchdn.SoLuongThayDoiTrongKy),
					SUM(rtchdn.SoLuongNoiBoThayDoiTrongKy),
					SUM(rtchdn.SoLuongKhuyenMaiThayDoiTrongKy),
	  Month(@NgayThucHien),
	  YEAR(@NgayThucHien),
	  0
	  FROM DoanhSoThucChayWebsiteTheoThoiGian rtchdn
		  
	  WHERE 1=1 
	  AND rtchdn.NgayThucHien = @NgayThucHien
	  GROUP BY 
	   rtchdn.TenKhachHang,
	  rtchdn.DmKhachHangREF,
	  rtchdn.TenNhanVien,
	  rtchdn.DmNhanVienREF,
					rtchdn.TenPhongBan,
					rtchdn.PhongBanREF,
					rtchdn.TenBoPhan,
					rtchdn.BoPhanREF,
					rtchdn.TenNhom,
					rtchdn.NhomREF,
					rtchdn.TenDonViTinh,
					rtchdn.UserName
	  ------------------------------------UPDATE dl------------------------
	  UPDATE  rptThucChay_KhachHang_Thang
		SET rptThucChay_KhachHang_Thang.NgayThucHien = @NgayThucHien,
		    rptThucChay_KhachHang_Thang.ThucChayPhatSinhTrongKy += td.ThucChayPhatSinhTrongKy,
		    rptThucChay_KhachHang_Thang.ThucChayPhatSinhCuoiKy += td.ThucChayPhatSinhTrongKy,
		    rptThucChay_KhachHang_Thang.KhuyenMaiPhatSinhTrongKy += td.KhuyenMaiPhatSinhTrongKy,
		    rptThucChay_KhachHang_Thang.KhuyenMaiPhatSinhCuoiKy += td.KhuyenMaiPhatSinhTrongKy,
		    rptThucChay_KhachHang_Thang.NoiBoPhatSinhTrongKy += td.NoiBoPhatSinhTrongKy,
		    rptThucChay_KhachHang_Thang.NoiBoPhatSinhCuoiKy += td.NoiBoPhatSinhTrongKy,
		    SoLuongPhatSinhTrongKy += td.SoLuongPhatSinhTrongKy,
	        SoLuongPhatSinhCuoiKy += td.SoLuongPhatSinhTrongKy,
			SoLuongKhuyenMaiPhatSinhTrongKy += td.SoLuongKhuyenMaiPhatSinhTrongKy,
			SoLuongKhuyenMaiPhatSinhCuoiKy += td.SoLuongKhuyenMaiPhatSinhTrongKy,
			SoLuongNoiBoPhatSinhTrongKy +=td.SoLuongNoiBoPhatSinhTrongKy,
			SoLuongNoiBoPhatSinhCuoiKy += td.SoLuongNoiBoPhatSinhTrongKy  ,
			ThucChayThayDoiTrongKy += td.ThucChayThayDoiTrongKy,
	 			NoiBoThayDoiTrongKy += td.NoiBoThayDoiTrongKy,
	 			KhuyenMaiThayDoiTrongKy += td.KhuyenMaiThayDoiTrongKy,
	 			SoLuongThayDoiTrongKy +=td.SoLuongThayDoiTrongKy,
	 			SoLuongNoiBoThayDoiTrongKy +=td.SoLuongNoiBoThayDoiTrongKy,
	 			SoLuongKhuyenMaiThayDoiTrongKy += td.SoLuongKhuyenMaiThayDoiTrongKy    
		FROM rptThucChay_KhachHang_Thang rtchdt
		INNER JOIN @TeampData td
		ON 
		td.DmNhanVienREF = rtchdt.DmNhanVienREF
		AND td.PhongBanREF = rtchdt.PhongBanREF
		AND td.BoPhanREF = rtchdt.BoPhanREF
		AND td.NhomREF = rtchdt.NhomREF
		AND td.TenDonViTinh = rtchdt.TenDonViTinh
		AND td.UserName = rtchdt.UserName
		AND td.DmKhachHangREF = rtchdt.DmKhachHangREF
		AND td.Nam = rtchdt.Nam
		AND td.Thang = rtchdt.Thang

		
		 UPDATE  @TeampData 
		SET TrangThai = 1
		FROM rptThucChay_KhachHang_Thang rtchdt
		INNER JOIN @TeampData td
		ON 
		td.DmNhanVienREF = rtchdt.DmNhanVienREF
		AND td.PhongBanREF = rtchdt.PhongBanREF
		AND td.BoPhanREF = rtchdt.BoPhanREF
		AND td.NhomREF = rtchdt.NhomREF
		AND td.TenDonViTinh = rtchdt.TenDonViTinh
		AND td.UserName = rtchdt.UserName
		AND td.DmKhachHangREF = rtchdt.DmKhachHangREF
		AND td.Thang = rtchdt.Thang
		AND td.Nam = rtchdt.Nam
		----------------------------------INSERT dl------------------------------------
		INSERT INTO rptThucChay_KhachHang_Thang
				SELECT 
				@NgayThucHien,
				td.Thang,
				td.Nam,
				td.TenKhachHang,
	            td.DmKhachHangREF,
	            td.SoDienThoai,
	            td.TenHinhThucKhachHang,
				[dbo].[fn_GetDauKy_Of_Ngay_KhachHang]
				(
					td.DmNhanVienREF,
					td.PhongBanREF,
					td.BoPhanREF,
					td.NhomREF,
					td.TenDonViTinh,
					td.Username,
				  td.DmKhachHangREF,		
			      @NgayThucHien,
			      1,0
				) ThucChayPhatSinhDauKy,
	            td.ThucChayPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_KhachHang]
				(
					td.DmNhanVienREF,
					td.PhongBanREF,
					td.BoPhanREF,
					td.NhomREF,
					td.TenDonViTinh,
					td.Username,
				   td.DmKhachHangREF,	
			      @NgayThucHien,
			      1,0
				)
	            +  td.ThucChayPhatSinhTrongKy
	            ) ThucChayPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_KhachHang]
				(
					td.DmNhanVienREF,
					td.PhongBanREF,
					td.BoPhanREF,
					td.NhomREF,
					td.TenDonViTinh,
					td.Username,
				   td.DmKhachHangREF,	
			      @NgayThucHien,
			      2,0
				) KhuyenMaiPhatSinhDauKy,
	            td.KhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_KhachHang]
				(	
					td.DmNhanVienREF,
					td.PhongBanREF,
					td.BoPhanREF,
					td.NhomREF,
					td.TenDonViTinh,
					td.Username,
				    td.DmKhachHangREF,	
			      @NgayThucHien,
			      2,0
				)+  td.KhuyenMaiPhatSinhTrongKy
	            ) KhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_KhachHang]
				(	
					td.DmNhanVienREF,
					td.PhongBanREF,
					td.BoPhanREF,
					td.NhomREF,
					td.TenDonViTinh,
					td.Username,
				   td.DmKhachHangREF,	
			      @NgayThucHien,
			      3,0
				) NoiBoPhatSinhDauKy,
	            td.NoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Ngay_KhachHang]
				(
					td.DmNhanVienREF,
					td.PhongBanREF,
					td.BoPhanREF,
					td.NhomREF,
					td.TenDonViTinh,
					td.Username,	
				    td.DmKhachHangREF,	
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
	              [dbo].[fn_GetDauKy_Of_Quy_KhachHang]
				(
					td.DmNhanVienREF,
					td.PhongBanREF,
					td.BoPhanREF,
					td.NhomREF,
					td.TenDonViTinh,
					td.Username,
				  td.DmKhachHangREF,		
			      @NgayThucHien,
			      1,1
				) SoLuongPhatSinhDauKy,
	            td.SoLuongPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Quy_KhachHang]
				(
					td.DmNhanVienREF,
					td.PhongBanREF,
					td.BoPhanREF,
					td.NhomREF,
					td.TenDonViTinh,
					td.Username,
				   td.DmKhachHangREF,	
			      @NgayThucHien,
			      1,1
				)
	            +  td.SoLuongPhatSinhTrongKy
	            ) SoLuongPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Quy_KhachHang]
				(
					td.DmNhanVienREF,
					td.PhongBanREF,
					td.BoPhanREF,
					td.NhomREF,
					td.TenDonViTinh,
					td.Username,
				   td.DmKhachHangREF,	
			      @NgayThucHien,
			      2,1
				) SoLuongKhuyenMaiPhatSinhDauKy,
	            td.SoLuongKhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Quy_KhachHang]
				(	
					td.DmNhanVienREF,
					td.PhongBanREF,
					td.BoPhanREF,
					td.NhomREF,
					td.TenDonViTinh,
					td.Username,
				    td.DmKhachHangREF,	
			      @NgayThucHien,
			      2,1
				)+  td.SoLuongKhuyenMaiPhatSinhTrongKy
	            ) SoLuongKhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Quy_KhachHang]
				(
					td.DmNhanVienREF,
					td.PhongBanREF,
					td.BoPhanREF,
					td.NhomREF,
					td.TenDonViTinh,
					td.Username,	
				   td.DmKhachHangREF,	
			      @NgayThucHien,
			      3,1
				) SoLuongNoiBoPhatSinhDauKy,
	            td.SoLuongNoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Quy_KhachHang]
				(	
					td.DmNhanVienREF,
					td.PhongBanREF,
					td.BoPhanREF,
					td.NhomREF,
					td.TenDonViTinh,
					td.Username,
				    td.DmKhachHangREF,	
			      @NgayThucHien,
			      3,1
				) + td.SoLuongNoiBoPhatSinhTrongKy
	            ) SoLuongNoiBoPhatSinhCuoiKy,
	            td.TenNhanVien,
	            td.DmNhanVienREF,
	            td.TenPhongBan,
	            td.PhongBanREF,
	            td.TenBoPhan,
	            td.BoPhanREF,
	            td.TenNhom,
	            td.NhomREF,
	            td.TenDonViTinh,
	            td.Username,
	            td.ThucChayThayDoiTrongKy,
	            td.NoiBoThayDoiTrongKy,
	            td.KhuyenMaiThayDoiTrongKy,
	            td.SoLuongThayDoiTrongKy,
	            td.SoLuongNoiBoThayDoiTrongKy,
	            td.SoLuongKhuyenMaiThayDoiTrongKy
			 FROM  @TeampData td
				WHERE 1=1 AND td.TrangThai <>1
		
END


--SELECT * FROM NhanSuSoYeuLyLich nssyll WHERE nssyll.HoVaTen = N'Trần Nhân Thuần'
```
