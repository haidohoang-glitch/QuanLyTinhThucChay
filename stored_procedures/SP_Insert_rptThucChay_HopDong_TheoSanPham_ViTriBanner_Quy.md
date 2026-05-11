# Stored Procedure: `Insert_rptThucChay_HopDong_TheoSanPham_ViTriBanner_Quy`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-27 17:43:54.290000
- **Ngày sửa cuối**: 2015-03-27 17:43:54.290000

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
--EXEC [dbo].[Insert_rptThucChay_HopDong_TheoSanPham_ViTriBanner_Quy_NEW] '2013-01-02'
CREATE PROCEDURE [dbo].[Insert_rptThucChay_HopDong_TheoSanPham_ViTriBanner_Quy]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	DECLARE @TeampData TABLE 
	   (
	        HopDongID INT,
			SoHopDong NVARCHAR(50),
			TenNhanVien NVARCHAR(200),
			DmNhanVienREF INT,
		    TenPhongBan NVARCHAR(200),
			PhongBanREF INT,
			TenBoPhan NVARCHAR(200),
			BoPhanREF INT,
			TenNhom NVARCHAR(200),
		    NhomREF INT,
			TenKhachHang NVARCHAR(500),
			DmKhachHangREF INT,
			DmHinhThucKhachHangREF NVARCHAR(200),
			TenSanPham NVARCHAR(200),
			DmSanPhamREF INT,
			TenViTriBanner NVARCHAR(200),
			ViTriBannerREF INT,
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
			Quy INT,
			Nam INT,
			TrangThai INT,
			TenDonViTinh nvarchar(50),
			UserName nvarchar(50)
		)

    -- Tổng hợp dữ liệu theo ngày
	   INSERT INTO @TeampData
			SELECT 
			DISTINCT
		        rtchdn.HopDongID,
				rtchdn.SoHopDong,
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
			    '',
			    rtchdn.TenSanPham,
			    rtchdn.DmSanPhamREF,
			    rtchdn.TenViTriBanner,
			    rtchdn.DmViTriBannerREF,
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
			    DATEPART(QQ,@NgayThucHien),
			    YEAR(@NgayThucHien),
			    0,
			    rtchdn.TenDonViTinh,
			    rtchdn.UserName
			 FROM  DoanhSoThucChayWebsiteTheoThoiGian rtchdn
			 WHERE 1=1 
			 AND CONVERT(DATE,rtchdn.NgayThucHien) = @NgayThucHien
			GROUP BY 
			    rtchdn.HopDongID,
				rtchdn.SoHopDong,
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
			    rtchdn.TenSanPham,
			    rtchdn.DmSanPhamREF,
			    rtchdn.TenViTriBanner,
			    rtchdn.DmViTriBannerREF,
			    rtchdn.TenDonViTinh,
			    rtchdn.UserName
			    
	    --------------------------------------UPDATE dl đã tồn tại------------------------------------
		UPDATE  rptThucChay_HopDong_TheoSanPham_ViTriBanner_Quy 
		SET rptThucChay_HopDong_TheoSanPham_ViTriBanner_Quy.NgayThucHien = @NgayThucHien,
		    rptThucChay_HopDong_TheoSanPham_ViTriBanner_Quy.ThucChayPhatSinhTrongKy += td.ThucChayPhatSinhTrongKy,
		    rptThucChay_HopDong_TheoSanPham_ViTriBanner_Quy.ThucChayPhatSinhCuoiKy += td.ThucChayPhatSinhTrongKy,
		    rptThucChay_HopDong_TheoSanPham_ViTriBanner_Quy.KhuyenMaiPhatSinhTrongKy += td.KhuyenMaiPhatSinhTrongKy,
		    rptThucChay_HopDong_TheoSanPham_ViTriBanner_Quy.KhuyenMaiPhatSinhCuoiKy += td.KhuyenMaiPhatSinhTrongKy,
		    rptThucChay_HopDong_TheoSanPham_ViTriBanner_Quy.NoiBoPhatSinhTrongKy += td.NoiBoPhatSinhTrongKy,
		    rptThucChay_HopDong_TheoSanPham_ViTriBanner_Quy.NoiBoPhatSinhCuoiKy += td.NoiBoPhatSinhTrongKy,
		    SoLuongPhatSinhTrongKy += td.SoLuongPhatSinhTrongKy,
	        SoLuongPhatSinhCuoiKy += td.SoLuongPhatSinhTrongKy,
			SoLuongKhuyenMaiPhatSinhTrongKy += td.SoLuongKhuyenMaiPhatSinhTrongKy,
			SoLuongKhuyenMaiPhatSinhCuoiKy += td.SoLuongKhuyenMaiPhatSinhTrongKy,
			SoLuongNoiBoPhatSinhTrongKy +=td.SoLuongNoiBoPhatSinhTrongKy,
			SoLuongNoiBoPhatSinhCuoiKy += td.SoLuongNoiBoPhatSinhTrongKy,
			ThucChayThayDoiTrongKy += td.ThucChayThayDoiTrongKy,
	 			NoiBoThayDoiTrongKy += td.NoiBoThayDoiTrongKy,
	 			KhuyenMaiThayDoiTrongKy += td.KhuyenMaiThayDoiTrongKy,
	 			SoLuongThayDoiTrongKy +=td.SoLuongThayDoiTrongKy,
	 			SoLuongNoiBoThayDoiTrongKy +=td.SoLuongNoiBoThayDoiTrongKy,
	 			SoLuongKhuyenMaiThayDoiTrongKy += td.SoLuongKhuyenMaiThayDoiTrongKy     
		FROM rptThucChay_HopDong_TheoSanPham_ViTriBanner_Quy rtchdt
		INNER JOIN @TeampData td
		ON td.HopDongID = rtchdt.HopDongID
		AND td.DmNhanVienREF = rtchdt.DmNhanVienREF
		AND td.PhongBanREF = rtchdt.PhongBanREF
		AND td.BoPhanREF = rtchdt.BoPhanREF
		AND td.NhomREF = rtchdt.NhomREF
		AND td.DmKhachHangREF = rtchdt.DmKhachHangREF
		AND td.DmHinhThucKhachHangREF = rtchdt.LoaiKhachHang
		AND td.DmSanPhamREF = rtchdt.DmSanPhamREF
		AND td.Quy = rtchdt.Quy
		AND td.Nam = rtchdt.Nam
		AND td.TenDonViTinh = rtchdt.TenDonViTinh
		AND td.UserName = rtchdt.UserName
		AND td.ViTriBannerREF = rtchdt.DmViTriBannerREF
		UPDATE  @TeampData 
		SET TrangThai = 1
		FROM @TeampData td
		INNER JOIN rptThucChay_HopDong_TheoSanPham_ViTriBanner_Quy rtchdt
		ON td.HopDongID = rtchdt.HopDongID
		AND td.DmNhanVienREF = rtchdt.DmNhanVienREF
		AND td.PhongBanREF = rtchdt.PhongBanREF
		AND td.BoPhanREF = rtchdt.BoPhanREF
		AND td.NhomREF = rtchdt.NhomREF
		AND td.DmKhachHangREF = rtchdt.DmKhachHangREF
		AND td.DmHinhThucKhachHangREF = rtchdt.LoaiKhachHang
		AND td.DmSanPhamREF = rtchdt.DmSanPhamREF
		AND td.Quy = rtchdt.Quy
		AND td.Nam = rtchdt.Nam
		AND td.TenDonViTinh = rtchdt.TenDonViTinh
		AND td.UserName = rtchdt.UserName
		AND td.ViTriBannerREF = rtchdt.DmViTriBannerREF
     ------------------------------------Insert--------------------------------------------
     INSERT INTO rptThucChay_HopDong_TheoSanPham_ViTriBanner_Quy
     SELECT 
				@NgayThucHien,
				td.Quy,
				td.Nam,
				td.HopDongID,
				td.SoHopDong,
				td.TenNhanVien,
				td.DmNhanVienREF,
				td.TenPhongBan,
				Td.PhongBanREF,
				td.TenBoPhan,
				td.BoPhanREF,
				td.TenNhom,
				td.NhomREF,
				td.TenKhachHang,
				td.DmKhachHangREF,
			    td.DmHinhThucKhachHangREF,
			    td.DmSanPhamREF,
			    td.TenSanPham,
			    td.ViTriBannerREF,
			    td.TenViTriBanner,
				'',
				[dbo].[fn_GetDauKy_Of_Ngay_HopDongTheoSanPhamBanner] 
				(
				  td.HopDongID,	
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHangREF,
				  td.DmSanPhamREF,
				  td.ViTriBannerREF,
			      @NgayThucHien,
			      1,0
			      ,
			      td.TenDonViTinh,
			      td.Username
				) ThucChayPhatSinhDauKy,
	             td.ThucChayPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_HopDongTheoSanPhamBanner] 
				(
				  td.HopDongID,	
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHangREF,
				  td.DmSanPhamREF,
				  td.ViTriBannerREF,
			      @NgayThucHien,
			      1,0
			      ,
			      td.TenDonViTinh,
			      td.Username
				)
	            + td.ThucChayPhatSinhTrongKy
	            ) ThucChayPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_HopDongTheoSanPhamBanner] 
				(
				  td.HopDongID,	
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHangREF,
				  td.DmSanPhamREF,
				  td.ViTriBannerREF,
			      @NgayThucHien,
			      2,0
			      ,
			      td.TenDonViTinh,
			      td.Username
				) KhuyenMaiPhatSinhDauKy,
	            td.KhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_HopDongTheoSanPhamBanner] 
				(	
				  td.HopDongID,	
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHangREF,
				  td.DmSanPhamREF,
				  td.ViTriBannerREF,
			      @NgayThucHien,
			      2,0
			      ,
			      td.TenDonViTinh,
			      td.Username
				)+ td.KhuyenMaiPhatSinhTrongKy
	            ) KhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_HopDongTheoSanPhamBanner] 
				(	
				  td.HopDongID,	
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHangREF,
				  td.DmSanPhamREF,
				  td.ViTriBannerREF,
			      @NgayThucHien,
			      3,0
			      ,
			      td.TenDonViTinh,
			      td.Username
				) NoiBoPhatSinhDauKy,
	            td.NoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Ngay_HopDongTheoSanPhamBanner] 
				(	
				  td.HopDongID,	
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHangREF,
				  td.DmSanPhamREF,
				  td.ViTriBannerREF,
			      @NgayThucHien,
			      3,0
			      ,
			      td.TenDonViTinh,
			      td.Username
				) + td.NoiBoPhatSinhTrongKy
	            ) NoiBoPhatSinhCuoiKy,
	           'ASD' CreatedBy,
	           GETDATE() CreatedAt,
	           'ASD' LastModifiedBy,
	           GETDATE() LastModifiedAt,
	           0 DeletedStatus,
	           0 RecordStatus,
	           0 PrintStatus,
	            [dbo].[fn_GetDauKy_Of_Ngay_HopDongTheoSanPhamBanner] 
				(
				  td.HopDongID,	
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHangREF,
				  td.DmSanPhamREF,
				  td.ViTriBannerREF,
			      @NgayThucHien,
			      1,1
			      ,
			      td.TenDonViTinh,
			      td.Username
				) SoLuongPhatSinhDauKy,
				
	             td.SoLuongPhatSinhTrongKy,
	             
	            ([dbo].[fn_GetDauKy_Of_Ngay_HopDongTheoSanPhamBanner] 
				(
				 td.HopDongID,	
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHangREF,
				  td.DmSanPhamREF,
				  td.ViTriBannerREF,
			      @NgayThucHien,
			      1,1
			      ,
			      td.TenDonViTinh,
			      td.Username
				)
	            + td.SoLuongPhatSinhTrongKy
	            ) SoLuongPhatSinhCuoiKy,
	            
	            [dbo].[fn_GetDauKy_Of_Ngay_HopDongTheoSanPhamBanner] 
				(
				  td.HopDongID,	
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHangREF,
				  td.DmSanPhamREF,
				  td.ViTriBannerREF,
			      @NgayThucHien,
			      2,1
			      ,
			      td.TenDonViTinh,
			      td.Username
				) SoLuongKhuyenMaiPhatSinhDauKy,
				
	            td.SoLuongKhuyenMaiPhatSinhTrongKy,
	            
	            ([dbo].[fn_GetDauKy_Of_Ngay_HopDongTheoSanPhamBanner] 
				(	
				  td.HopDongID,	
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHangREF,
				  td.DmSanPhamREF,
				  td.ViTriBannerREF,
			      @NgayThucHien,
			      2,1
			      ,
			      td.TenDonViTinh,
			      td.Username
				)+ td.SoLuongKhuyenMaiPhatSinhTrongKy
	            ) SoLuongKhuyenMaiPhatSinhCuoiKy,
	            
	            [dbo].[fn_GetDauKy_Of_Ngay_HopDongTheoSanPhamBanner] 
				(	
				  td.HopDongID,	
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHangREF,
				  td.DmSanPhamREF,
				  td.ViTriBannerREF,
			      @NgayThucHien,
			      3,1
			      ,
			      td.TenDonViTinh,
			      td.Username
				) SoLuongNoiBoPhatSinhDauKy,
				
	            td.SoLuongNoiBoPhatSinhTrongKy,
	            (
	            [dbo].[fn_GetDauKy_Of_Ngay_HopDongTheoSanPhamBanner] 
				(	
				  td.HopDongID,	
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHangREF,
				  td.DmSanPhamREF,
				  td.ViTriBannerREF,
			      @NgayThucHien,
			      3,1
			      ,
			      td.TenDonViTinh,
			      td.Username
				) + td.SoLuongNoiBoPhatSinhTrongKy
	            ) SoLuongNoiBoPhatSinhCuoiKy,
	            td.TenDonViTinh,
	            td.UserName,
	             td.ThucChayThayDoiTrongKy,
	            td.NoiBoThayDoiTrongKy,
	            td.KhuyenMaiThayDoiTrongKy,
	            td.SoLuongThayDoiTrongKy,
	            td.SoLuongNoiBoThayDoiTrongKy,
	            td.SoLuongKhuyenMaiThayDoiTrongKy
     FROM @TeampData td WHERE td.TrangThai <> 1
			 
END

```
