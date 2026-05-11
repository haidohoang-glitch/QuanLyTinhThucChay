# Stored Procedure: `Insert_rptThucChay_NganhHang_TheoSanPham_Thang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-31 11:21:04.433000
- **Ngày sửa cuối**: 2015-03-31 11:21:04.433000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author  Thange>
-- Create date: <Create Date  >
-- Description:	<Description  >
-- =============================================
CREATE PROCEDURE [dbo].[Insert_rptThucChay_NganhHang_TheoSanPham_Thang]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	DECLARE @TeampData TABLE 
	   (
	        TenNhanVien nvarchar(200),
	        DmNhanVienREF int,
	        TenPhongBan nvarchar(200),
	        PhongBanREF int,
	        TenBoPhan nvarchar(200),
	        BoPhanREF int,
	        TenNhom nvarchar(200),
	        NhomREF int,
	        TenSanPham NVARCHAR(200),
	        DmSanPhamREF NVARCHAR(200),
	        TenDonViTinh nvarchar(50),
	        UserName nvarchar(50),
			TenNganhHang NVARCHAR(500),
			DmNganhHangREF INT,
			ThucChayPhatSinhTrongKy FLOAT,
			KhuyenMaiPhatSinhTrongKy FLOAT,
			NoiBoPhatSinhTrongKy FLOAT,
			SoLuongPhatSinhTrongKy BIGINT,
			SoLuongKhuyenMaiPhatSinhTrongKy BIGINT,
			SoLuongNoiBoPhatSinhTrongKy BIGINT,
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
	-------- Du Lieu Phat Sinh-----------
	INSERT INTO @TeampData
			SELECT 
			DISTINCT
			    rtchdn.TenNhanVien,
			    rtchdn.DmNhanVienREF,
			    rtchdn.TenPhongBan,
			    rtchdn.PhongbanREF,
			    rtchdn.TenBoPhan,
			    rtchdn.BoPhanREF,
			    rtchdn.TenNhom,
			    rtchdn.NhomREF,
			    rtchdn.TenSanPham,
			    rtchdn.DmSanPhamREF,
			    rtchdn.TenDonViTinh,
			    rtchdn.UserName,
				rtchdn.TenNganhHang,
				rtchdn.DmNganhHangREF,
			    SUM(rtchdn.ThucChayPhatSinhTrongKy),
			    SUM(rtchdn.KhuyenMaiPhatSinhTrongKy),
			    SUM(rtchdn.NoiBoPhatSinhTrongKy),
			    SUM(rtchdn.SoLuongPhatSinhTrongKy),
			    SUM(rtchdn.SoLuongKhuyenMaiPhatSinhTrongKy),
			    SUM(rtchdn.SoLuongNoiBoPhatSinhTrongKy),
			    SUM(rtchdn.ThucChayThayDoiTrongKy),
			    SUM(rtchdn.NoiBoThayDoiTrongKy),
			    SUM(rtchdn.KhuyenMaiThayDoiTrongKy),
			    SUM(rtchdn.SoLuongThayDoiTrongKy),
			    SUM(rtchdn.SoLuongNoiBoThayDoiTrongKy),
			    SUM(rtchdn.SoLuongKhuyenMaiThayDoiTrongKy),
			    month(@NgayThucHien),
			    YEAR(@NgayThucHien),
			    0
			 FROM  DoanhSoThucChayNganhHangCore  rtchdn
			 WHERE 1=1 
			 AND CONVERT(DATE,rtchdn.NgayThucHien) = @NgayThucHien
			GROUP BY 
			   rtchdn.TenNhanVien,
			    rtchdn.DmNhanVienREF,
			    rtchdn.TenPhongBan,
			    rtchdn.PhongbanREF,
			    rtchdn.TenBoPhan,
			    rtchdn.BoPhanREF,
			    rtchdn.TenNhom,
			    rtchdn.NhomREF,
			    rtchdn.TenDonViTinh,
			    rtchdn.UserName,
			    rtchdn.TenNganhHang,
				rtchdn.DmNganhHangREF,
				rtchdn.TenSanPham,
			    rtchdn.DmSanPhamREF
	-----------------------------------UPDATE DL-----------------------------
	UPDATE  rptThucChay_NganhHang_TheoSanPham_Thang
		SET rptThucChay_NganhHang_TheoSanPham_Thang.NgayThucHien = @NgayThucHien,
		    rptThucChay_NganhHang_TheoSanPham_Thang.ThucChayPhatSinhTrongKy += td.ThucChayPhatSinhTrongKy,
		    rptThucChay_NganhHang_TheoSanPham_Thang.ThucChayPhatSinhCuoiKy += td.ThucChayPhatSinhTrongKy,
		    rptThucChay_NganhHang_TheoSanPham_Thang.KhuyenMaiPhatSinhTrongKy += td.KhuyenMaiPhatSinhTrongKy,
		    rptThucChay_NganhHang_TheoSanPham_Thang.KhuyenMaiPhatSinhCuoiKy += td.KhuyenMaiPhatSinhTrongKy,
		    rptThucChay_NganhHang_TheoSanPham_Thang.NoiBoPhatSinhTrongKy += td.NoiBoPhatSinhTrongKy,
		    rptThucChay_NganhHang_TheoSanPham_Thang.NoiBoPhatSinhCuoiKy += td.NoiBoPhatSinhTrongKy,
		     SoLuongPhatSinhTrongKy += td.SoLuongPhatSinhTrongKy,
	        SoLuongPhatSinhCuoiKy += td.SoLuongPhatSinhTrongKy,
			SoLuongKhuyenMaiPhatSinhTrongKy += td.SoLuongKhuyenMaiPhatSinhTrongKy,
			SoLuongKhuyenMaiPhatSinhCuoiKy += td.SoLuongKhuyenMaiPhatSinhTrongKy,
			SoLuongNoiBoPhatSinhTrongKy +=td.SoLuongNoiBoPhatSinhTrongKy,
			SoLuongNoiBoPhatSinhCuoiKy += td.SoLuongNoiBoPhatSinhTrongKy ,
			ThucChayThayDoiTrongKy += td.ThucChayThayDoiTrongKy,
	 			NoiBoThayDoiTrongKy += td.NoiBoThayDoiTrongKy,
	 			KhuyenMaiThayDoiTrongKy += td.KhuyenMaiThayDoiTrongKy,
	 			SoLuongThayDoiTrongKy +=td.SoLuongThayDoiTrongKy,
	 			SoLuongNoiBoThayDoiTrongKy +=td.SoLuongNoiBoThayDoiTrongKy,
	 			SoLuongKhuyenMaiThayDoiTrongKy += td.SoLuongKhuyenMaiThayDoiTrongKy 
		FROM rptThucChay_NganhHang_TheoSanPham_Thang rtchdt
		INNER JOIN @TeampData td
		ON 
		td.DmNhanVienREF = rtchdt.DmNhanVienREF
		AND td.PhongBanREF = rtchdt.PhongBanREF
		AND td.BoPhanREF = rtchdt.BoPhanREF
		AND td.NhomREF = rtchdt.NhomREF
		AND td.TenDonViTinh = rtchdt.TenDonViTinh
		AND td.UserName = rtchdt.UserName
		AND td.DmNganhHangREF = rtchdt.DmNganhHangREF
		AND td.DmSanPhamREF = rtchdt.DmSanPhamREF
		AND td.Thang = rtchdt.Thang
		AND td.Nam = rtchdt.Nam
		
		UPDATE  @TeampData 
		SET TrangThai = 1
		FROM rptThucChay_NganhHang_TheoSanPham_Thang rtchdt
		INNER JOIN @TeampData td
		ON 
		td.DmNhanVienREF = rtchdt.DmNhanVienREF
		AND td.PhongBanREF = rtchdt.PhongBanREF
		AND td.BoPhanREF = rtchdt.BoPhanREF
		AND td.NhomREF = rtchdt.NhomREF
		AND td.TenDonViTinh = rtchdt.TenDonViTinh
		AND td.UserName = rtchdt.UserName
		AND td.DmNganhHangREF = rtchdt.DmNganhHangREF
		AND td.DmSanPhamREF = rtchdt.DmSanPhamREF
		AND td.Thang = rtchdt.Thang
		AND td.Nam = rtchdt.Nam
		-------------------------------------------------INSERT DL
	    INSERT INTO rptThucChay_NganhHang_TheoSanPham_Thang
				SELECT 
				@NgayThucHien,
				td.Thang,
				td.Nam,
				td.TenNganhHang, 
				td.DmNganhHangREF ,
			    
	            td.TenNhanVien,
	            td.DmNhanVienREF,
	            td.TenPhongBan,
	            td.PhongBanREF,
	            td.TenBoPhan,
	            td.BoPhanREF,
	            td.TenNhom,
	            td.NhomREF,
	            td.TenSanPham,
	            td.DmSanPhamREF,
				[dbo].[fn_GetDauKy_Of_Ngay_NganhHangTheoSanPham]
				(
				td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				  td.DmNganhHangREF ,		
			      @NgayThucHien,
			      1,0,td.DmSanPhamREF
				) ThucChayPhatSinhDauKy,
	            td.ThucChayPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_NganhHangTheoSanPham]
				(
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				 td.DmNganhHangREF ,		
			      @NgayThucHien,
			      1,0,td.DmSanPhamREF
				)
	            + td.ThucChayPhatSinhTrongKy
	            ) ThucChayPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_NganhHangTheoSanPham]
				(
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				   td.DmNganhHangREF ,		
			      @NgayThucHien,
			      2,0,td.DmSanPhamREF
				) KhuyenMaiPhatSinhDauKy,
	            td.KhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_NganhHangTheoSanPham]
				(	
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				   td.DmNganhHangREF ,			
			      @NgayThucHien,
			      2,0,td.DmSanPhamREF
				)+ td.KhuyenMaiPhatSinhTrongKy
	            ) KhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_NganhHangTheoSanPham]
				(
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,	
				   td.DmNganhHangREF ,			
			      @NgayThucHien,
			      3,0,td.DmSanPhamREF
				) NoiBoPhatSinhDauKy,
	            td.NoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Ngay_NganhHangTheoSanPham]
				(	
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				  td.DmNganhHangREF ,		
			      @NgayThucHien,
			      3,0,td.DmSanPhamREF
				) + td.NoiBoPhatSinhTrongKy
	            ) NoiBoPhatSinhCuoiKy,
	           'ASD' CreatedBy,
	           GETDATE() CreatedAt,
	           'ASD' LastModifiedBy,
	           GETDATE() LastModifiedAt,
	           0 DeletedStatus,
	           0 RecordStatus,
	           0 PrintStatus,
	           [dbo].[fn_GetDauKy_Of_Ngay_NganhHangTheoSanPham]
				(
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				  td.DmNganhHangREF ,		
			      @NgayThucHien,
			      1,1,td.DmSanPhamREF
				) ThucChayPhatSinhDauKy,
	            td.ThucChayPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_NganhHangTheoSanPham]
				(
				td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				 td.DmNganhHangREF ,		
			      @NgayThucHien,
			      1,1,td.DmSanPhamREF
				)
	            + td.ThucChayPhatSinhTrongKy
	            ) ThucChayPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_NganhHangTheoSanPham]
				(
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				   td.DmNganhHangREF ,		
			      @NgayThucHien,
			      2,1,td.DmSanPhamREF
				) KhuyenMaiPhatSinhDauKy,
	            td.KhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_NganhHangTheoSanPham]
				(	
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				   td.DmNganhHangREF ,			
			      @NgayThucHien,
			      2,1,td.DmSanPhamREF
				)+ td.KhuyenMaiPhatSinhTrongKy
	            ) KhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_NganhHangTheoSanPham]
				(	
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				   td.DmNganhHangREF ,			
			      @NgayThucHien,
			      3,1,td.DmSanPhamREF
				) NoiBoPhatSinhDauKy,
	            td.NoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Ngay_NganhHangTheoSanPham]
				(
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,	
				  td.DmNganhHangREF ,		
			      @NgayThucHien,
			      3,1,td.DmSanPhamREF
				) + td.NoiBoPhatSinhTrongKy
	            ) NoiBoPhatSinhCuoiKy,
				td.TenDonViTinh,
				td.UserName,
				td.ThucChayThayDoiTrongKy,
				td.NoiBoThayDoiTrongKy,
				td.KhuyenMaiThayDoiTrongKy,
				td.SoLuongThayDoiTrongKy,
				td.SoLuongNoiBoThayDoiTrongKy,
				td.SoLuongKhuyenMaiThayDoiTrongKy
			 FROM  @TeampData td
				WHERE 1=1 AND td.TrangThai <> 1
END

```
