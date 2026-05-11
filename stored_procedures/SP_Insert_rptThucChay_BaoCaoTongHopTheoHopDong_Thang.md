# Stored Procedure: `Insert_rptThucChay_BaoCaoTongHopTheoHopDong_Thang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-27 17:43:49.360000
- **Ngày sửa cuối**: 2015-03-27 17:43:49.360000

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
--EXEC [dbo].[Insert_rptThucChay_BaoCaoTongHopTheoHopDong_Thang_NEW] '2013-01-02'
CREATE PROCEDURE [dbo].[Insert_rptThucChay_BaoCaoTongHopTheoHopDong_Thang]
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
			TenHinhThucQuangCao NVARCHAR(200),
			DmHinhThucQuangCaoREF INT,
			TenWebsite NVARCHAR(250),
			DmWebsiteREF INT,
			TenViTriBanner NVARCHAR(250),
			DmViTriBannerREF INT,
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
			    rtchdn.DmHinhThucKhachHangREF,
			    rtchdn.TenSanPham,
			    rtchdn.DmSanPhamREF,
			    rtchdn.TenHinhThucQuangCao,
			    rtchdn.DmHinhThucQuangCaoREF,
			    rtchdn.TenWebsite,
			    rtchdn.DmWebsiteREF,
			    rtchdn.TenViTriBanner,
			    rtchdn.VitriBannerREF,
			    SUM(rtchdn.ThucChayPhatSinhTrongKy),
			    SUM(rtchdn.KhuyenMaiPhatSinhTrongKy),
			    SUM(rtchdn.NoiBoPhatSinhTrongKy),
			    SUM(rtchdn.SoLuongPhatSinhTrongKy),
				SUM(rtchdn.SoLuongKhuyenMaiPhatSinhTrongKy),
				SUM(rtchdn.SoLuongNoiBoPhatSinhTrongKy),
				SUM(ThucChayThayDoiTrongKy),
				SUM(NoiBoThayDoiTrongKy),
				SUM(KhuyenMaiThayDoiTrongKy),
				SUM(SoLuongThayDoiTrongKy),
				SUM(SoLuongNoiBoThayDoiTrongKy),
				SUM(SoLuongKhuyenMaiThayDoiTrongKy),
			    MONTH(@NgayThucHien),
			    YEAR(@NgayThucHien),
			    0,
			    rtchdn.TenDonViTinh,
			    rtchdn.UserName
			 FROM  DoanhSoThucChayHopDongTheoThoiGian rtchdn
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
			    rtchdn.DmHinhThucKhachHangREF,
			    rtchdn.TenSanPham,
			    rtchdn.DmSanPhamREF,
			    rtchdn.TenHinhThucQuangCao,
			    rtchdn.DmHinhThucQuangCaoREF,
			    rtchdn.TenWebsite,
			    rtchdn.DmWebsiteREF,
			    rtchdn.TenViTriBanner,
			    rtchdn.VitriBannerREF,
			    rtchdn.TenDonViTinh,
			    rtchdn.UserName
			    
	    --------------------------------------UPDATE dl đã tồn tại------------------------------------
		UPDATE  rptThucChay_BaoCaoTongHopTheoHopDong_Thang 
		SET rptThucChay_BaoCaoTongHopTheoHopDong_Thang.NgayThucHien = @NgayThucHien,
		    rptThucChay_BaoCaoTongHopTheoHopDong_Thang.ThucChayPhatSinhTrongKy += td.ThucChayPhatSinhTrongKy,
		    rptThucChay_BaoCaoTongHopTheoHopDong_Thang.ThucChayPhatSinhCuoiKy += td.ThucChayPhatSinhTrongKy,
		    rptThucChay_BaoCaoTongHopTheoHopDong_Thang.KhuyenMaiPhatSinhTrongKy += td.KhuyenMaiPhatSinhTrongKy,
		    rptThucChay_BaoCaoTongHopTheoHopDong_Thang.KhuyenMaiPhatSinhCuoiKy += td.KhuyenMaiPhatSinhTrongKy,
		    rptThucChay_BaoCaoTongHopTheoHopDong_Thang.NoiBoPhatSinhTrongKy += td.NoiBoPhatSinhTrongKy,
		    rptThucChay_BaoCaoTongHopTheoHopDong_Thang.NoiBoPhatSinhCuoiKy += td.NoiBoPhatSinhTrongKy,
		    SoLuongPhatSinhTrongKy += td.SoLuongPhatSinhTrongKy,
	        SoLuongPhatSinhCuoiKy += td.SoLuongPhatSinhTrongKy,
			SoLuongKhuyenMaiPhatSinhTrongKy += td.SoLuongKhuyenMaiPhatSinhTrongKy,
			SoLuongKhuyenMaiPhatSinhCuoiKy += td.SoLuongKhuyenMaiPhatSinhTrongKy,
			SoLuongNoiBoPhatSinhTrongKy +=td.SoLuongNoiBoPhatSinhTrongKy,
			SoLuongNoiBoPhatSinhCuoiKy += td.SoLuongNoiBoPhatSinhTrongKy ,
			ThucChayThayDoiTrongKy += td.ThucChayThayDoiTrongKy,
			NoiBoThayDoiTrongKy += td.NoiBoThayDoiTrongKy,
			KhuyenMaiThayDoiTrongKy += td.KhuyenMaiThayDoiTrongKy,
			SoLuongThayDoiTrongKy += td.SoLuongThayDoiTrongKy,
			SoLuongNoiBoThayDoiTrongKy += td.SoLuongNoiBoThayDoiTrongKy,
			SoLuongKhuyenMaiThayDoiTrongKy += td.SoLuongKhuyenMaiThayDoiTrongKy    
		FROM rptThucChay_BaoCaoTongHopTheoHopDong_Thang rtchdt
		INNER JOIN @TeampData td
		ON td.HopDongID = rtchdt.HopDongID
		AND td.DmNhanVienREF = rtchdt.DmNhanVienREF
		AND td.PhongBanREF = rtchdt.PhongBanREF
		AND td.BoPhanREF = rtchdt.BoPhanREF
		AND td.NhomREF = rtchdt.NhomREF
		AND td.DmKhachHangREF = rtchdt.DmKhachHangREF
		AND td.DmHinhThucKhachHangREF = rtchdt.LoaiKhachHang
		AND td.DmSanPhamREF = rtchdt.DmSanPhamREF
		AND td.Thang = rtchdt.Thang
		AND td.Nam = rtchdt.Nam
		AND td.TenDonViTinh = rtchdt.TenDonViTinh
		AND td.UserName = rtchdt.UserName
		AND td.DmHinhThucQuangCaoREF = rtchdt.DmHinhThucQuangCaoREF
		AND td.DmWebsiteREF = rtchdt.DmWebsiteREF
		AND td.DmViTriBannerREF = rtchdt.DmViTriBannerREF
		UPDATE  @TeampData 
		SET TrangThai = 1
		FROM @TeampData td
		INNER JOIN rptThucChay_BaoCaoTongHopTheoHopDong_Thang rtchdt
		ON td.HopDongID = rtchdt.HopDongID
		AND td.DmNhanVienREF = rtchdt.DmNhanVienREF
		AND td.PhongBanREF = rtchdt.PhongBanREF
		AND td.BoPhanREF = rtchdt.BoPhanREF
		AND td.NhomREF = rtchdt.NhomREF
		AND td.DmKhachHangREF = rtchdt.DmKhachHangREF
		AND td.DmHinhThucKhachHangREF = rtchdt.LoaiKhachHang
		AND td.DmSanPhamREF = rtchdt.DmSanPhamREF
		AND td.Thang = rtchdt.Thang
		AND td.Nam = rtchdt.Nam
		AND td.TenDonViTinh = rtchdt.TenDonViTinh
		AND td.UserName = rtchdt.UserName
		AND td.DmHinhThucQuangCaoREF = rtchdt.DmHinhThucQuangCaoREF
		AND td.DmWebsiteREF = rtchdt.DmWebsiteREF
		AND td.DmViTriBannerREF = rtchdt.DmViTriBannerREF
     ------------------------------------Insert--------------------------------------------
     INSERT INTO rptThucChay_BaoCaoTongHopTheoHopDong_Thang
     SELECT 
				@NgayThucHien,
				td.Thang,
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
			    td.DmHinhThucQuangCaoREF,
			    td.TenHinhThucQuangCao,
			     td.TenWebsite,
			    td.DmWebsiteREF,
			    td.TenViTriBanner,
			    td.DmViTriBannerREF,
				'',
				[dbo].[fn_GetDauKy_Of_Ngay_BaoCaoTongHopTheoHopDong] 
				(
				  td.HopDongID,	
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHangREF,
				  td.DmSanPhamREF,
				  td.DmHinhThucQuangCaoREF,
			    td.DmWebsiteREF,
			    td.DmViTriBannerREF,
			      @NgayThucHien,
			      1,0
			      ,
			      td.TenDonViTinh,
			      td.Username
				) ThucChayPhatSinhDauKy,
	             td.ThucChayPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_BaoCaoTongHopTheoHopDong] 
				(
				  td.HopDongID,	
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHangREF,
				  td.DmSanPhamREF,
				  td.DmHinhThucQuangCaoREF,
				   td.DmWebsiteREF,
			    td.DmViTriBannerREF,
			      @NgayThucHien,
			      1,0
			      ,
			      td.TenDonViTinh,
			      td.Username
				)
	            + td.ThucChayPhatSinhTrongKy
	            ) ThucChayPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_BaoCaoTongHopTheoHopDong] 
				(
				  td.HopDongID,	
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHangREF,
				  td.DmSanPhamREF,
				  td.DmHinhThucQuangCaoREF,
				   td.DmWebsiteREF,
			    td.DmViTriBannerREF,
			      @NgayThucHien,
			      2,0
			      ,
			      td.TenDonViTinh,
			      td.Username
				) KhuyenMaiPhatSinhDauKy,
	            td.KhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_BaoCaoTongHopTheoHopDong] 
				(	
				  td.HopDongID,	
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHangREF,
				  td.DmSanPhamREF,
				  td.DmHinhThucQuangCaoREF,
				   td.DmWebsiteREF,
			    td.DmViTriBannerREF,
			      @NgayThucHien,
			      2,0
			      ,
			      td.TenDonViTinh,
			      td.Username
				)+ td.KhuyenMaiPhatSinhTrongKy
	            ) KhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_BaoCaoTongHopTheoHopDong] 
				(	
				  td.HopDongID,	
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHangREF,
				  td.DmSanPhamREF,
				  td.DmHinhThucQuangCaoREF,
				   td.DmWebsiteREF,
			    td.DmViTriBannerREF,
			      @NgayThucHien,
			      3,0
			      ,
			      td.TenDonViTinh,
			      td.Username
				) NoiBoPhatSinhDauKy,
	            td.NoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Ngay_BaoCaoTongHopTheoHopDong] 
				(	
				  td.HopDongID,	
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHangREF,
				  td.DmSanPhamREF,
				  td.DmHinhThucQuangCaoREF,
				   td.DmWebsiteREF,
			    td.DmViTriBannerREF,
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
	            [dbo].[fn_GetDauKy_Of_Ngay_BaoCaoTongHopTheoHopDong] 
				(
				  td.HopDongID,	
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHangREF,
				  td.DmSanPhamREF,
				  td.DmHinhThucQuangCaoREF,
				   td.DmWebsiteREF,
			    td.DmViTriBannerREF,
			      @NgayThucHien,
			      1,1
			      ,
			      td.TenDonViTinh,
			      td.Username
				) SoLuongPhatSinhDauKy,
				
	             td.SoLuongPhatSinhTrongKy,
	             
	            ([dbo].[fn_GetDauKy_Of_Ngay_BaoCaoTongHopTheoHopDong] 
				(
				 td.HopDongID,	
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHangREF,
				  td.DmSanPhamREF,
				  td.DmHinhThucQuangCaoREF,
				   td.DmWebsiteREF,
			    td.DmViTriBannerREF,
			      @NgayThucHien,
			      1,1
			      ,
			      td.TenDonViTinh,
			      td.Username
				)
	            + td.SoLuongPhatSinhTrongKy
	            ) SoLuongPhatSinhCuoiKy,
	            
	            [dbo].[fn_GetDauKy_Of_Ngay_BaoCaoTongHopTheoHopDong] 
				(
				  td.HopDongID,	
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHangREF,
				  td.DmSanPhamREF,
				  td.DmHinhThucQuangCaoREF,
				   td.DmWebsiteREF,
			    td.DmViTriBannerREF,
			      @NgayThucHien,
			      2,1
			      ,
			      td.TenDonViTinh,
			      td.Username
				) SoLuongKhuyenMaiPhatSinhDauKy,
				
	            td.SoLuongKhuyenMaiPhatSinhTrongKy,
	            
	            ([dbo].[fn_GetDauKy_Of_Ngay_BaoCaoTongHopTheoHopDong] 
				(	
				  td.HopDongID,	
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHangREF,
				  td.DmSanPhamREF,
				  td.DmHinhThucQuangCaoREF,
				   td.DmWebsiteREF,
			    td.DmViTriBannerREF,
			      @NgayThucHien,
			      2,1
			      ,
			      td.TenDonViTinh,
			      td.Username
				)+ td.SoLuongKhuyenMaiPhatSinhTrongKy
	            ) SoLuongKhuyenMaiPhatSinhCuoiKy,
	            
	            [dbo].[fn_GetDauKy_Of_Ngay_BaoCaoTongHopTheoHopDong] 
				(	
				  td.HopDongID,	
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHangREF,
				  td.DmSanPhamREF,
				  td.DmHinhThucQuangCaoREF,
				   td.DmWebsiteREF,
			    td.DmViTriBannerREF,
			      @NgayThucHien,
			      3,1
			      ,
			      td.TenDonViTinh,
			      td.Username
				) SoLuongNoiBoPhatSinhDauKy,
				
	            td.SoLuongNoiBoPhatSinhTrongKy,
	            (
	            [dbo].[fn_GetDauKy_Of_Ngay_BaoCaoTongHopTheoHopDong] 
				(	
				  td.HopDongID,	
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.DmKhachHangREF,
				  td.DmHinhThucKhachHangREF,
				  td.DmSanPhamREF,
				  td.DmHinhThucQuangCaoREF,
				   td.DmWebsiteREF,
			    td.DmViTriBannerREF,
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
