# Stored Procedure: `Insert_rptThucChay_SanPham_TheoTenViTriBanner_Nam`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-27 17:44:02.220000
- **Ngày sửa cuối**: 2015-03-27 17:44:02.220000

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
--EXEC [dbo].[Insert_rptThucChay_SanPham_TheoViTriBanner_Nam] '2013-01-01'
CREATE PROCEDURE [dbo].[Insert_rptThucChay_SanPham_TheoTenViTriBanner_Nam]
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
	        TenDonViTinh nvarchar(50),
	        UserName nvarchar(50),
			TenSanPham NVARCHAR(500),
			DmSanPhamREF INT,
			TenViTriBanner NVARCHAR(200),
			DmViTriBannerREF INT,
			ThucChayPhatSinhTrongKy FLOAT,
			KhuyenMaiPhatSinhTrongKy FLOAT,
			NoiBoPhatSinhTrongKy FLOAT,
			SoluongPhatSinhTrongKy FLOAT,
			SoLuongKhuyenMaiPhatSinhTrongKy FLOAT,
			SoLuongNoiBoPhatSinhTrongKy FLOAT,
			ThucChayThayDoiTrongKy FLOAT,
			NoiBoThayDoiTrongKy FLOAT,
			KhuyenMaiThayDoiTrongKy FLOAT,
			SoLuongThayDoiTrongKy BIGINT,
			SoLuongNoiBoThayDoiTrongKy BIGINT,
			SoLuongKhuyenMaiThayDoiTrongKy BIGINT,
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
			    rtchdn.TenDonViTinh,
			    rtchdn.UserName,
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
			    YEAR(@NgayThucHien),
			    0
			 FROM  DoanhSoThucChayWebsiteTheoThoiGian rtchdn
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
				rtchdn.TenSanPham,
				rtchdn.DmSanPhamREF,
				rtchdn.TenViTriBanner,
				rtchdn.DmViTriBannerREF
	-----------------------------------UPDATE DL-----------------------------
	UPDATE  rptThucChay_SanPham_TheoViTriBanner_Nam 
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
		    SoLuongNoiBoPhatSinhTrongKy += td.SoLuongNoiBoPhatSinhTrongKy,
		    SoLuongNoiBoPhatSinhCuoiKy += td.SoLuongNoiBoPhatSinhTrongKy,
		    ThucChayThayDoiTrongKy += td.ThucChayThayDoiTrongKy,
	 			NoiBoThayDoiTrongKy += td.NoiBoThayDoiTrongKy,
	 			KhuyenMaiThayDoiTrongKy += td.KhuyenMaiThayDoiTrongKy,
	 			SoLuongThayDoiTrongKy +=td.SoLuongThayDoiTrongKy,
	 			SoLuongNoiBoThayDoiTrongKy +=td.SoLuongNoiBoThayDoiTrongKy,
	 			SoLuongKhuyenMaiThayDoiTrongKy += td.SoLuongKhuyenMaiThayDoiTrongKy 
		FROM rptThucChay_SanPham_TheoViTriBanner_Nam rtchdt
		INNER JOIN @TeampData td
		ON 
		td.DmNhanVienREF = rtchdt.DmNhanVienREF
		AND td.PhongBanREF = rtchdt.PhongBanREF
		AND td.BoPhanREF = rtchdt.BoPhanREF
		AND td.NhomREF = rtchdt.NhomREF
		AND td.TenDonViTinh = rtchdt.TenDonViTinh
		AND td.UserName = rtchdt.UserName
		AND td.DmSanPhamREF = rtchdt.DmSanPhamREF
		AND td.DmViTriBannerREF = rtchdt.DmViTriBannerREF

		AND td.Nam = rtchdt.Nam
		
		UPDATE  @TeampData 
		SET TrangThai = 1
		FROM rptThucChay_SanPham_TheoViTriBanner_Nam rtchdt
		INNER JOIN @TeampData td
		ON 
		td.DmNhanVienREF = rtchdt.DmNhanVienREF
		AND td.PhongBanREF = rtchdt.PhongBanREF
		AND td.BoPhanREF = rtchdt.BoPhanREF
		AND td.NhomREF = rtchdt.NhomREF
		AND td.TenDonViTinh = rtchdt.TenDonViTinh
		AND td.UserName = rtchdt.UserName
		AND td.DmSanPhamREF = rtchdt.DmSanPhamREF
		AND td.DmViTriBannerREF = rtchdt.DmViTriBannerREF
		
		AND td.Nam = rtchdt.Nam
		-------------------------------------------------INSERT DL
	    INSERT INTO rptThucChay_SanPham_TheoViTriBanner_Nam
				SELECT 
				@NgayThucHien,
				td.Nam,
			    td.DmSanPhamREF ,
			    td.TenSanPham, 
	            td.TenViTriBanner,
	            td.DmViTriBannerREF,
				[dbo].[fn_GetDauKy_Of_Ngay_SanPhamTheoTenViTriBanner]
				(
				td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				  td.DmSanPhamREF ,	
				  td.DmViTriBannerREF,	
			      @NgayThucHien,
			      1,0
				) ThucChayPhatSinhDauKy,
	            td.ThucChayPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_SanPhamTheoTenViTriBanner]
				(
				td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				  td.DmSanPhamREF ,	
				  td.DmViTriBannerREF,
			      @NgayThucHien,
			      1,0
				)
	            + td.ThucChayPhatSinhTrongKy
	            ) ThucChayPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_SanPhamTheoTenViTriBanner]
				(
				td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				   td.DmSanPhamREF ,	
				  td.DmViTriBannerREF,	
			      @NgayThucHien,
			      2,0
				) KhuyenMaiPhatSinhDauKy,
	            td.KhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_SanPhamTheoTenViTriBanner]
				(	
				td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				    td.DmSanPhamREF ,	
				  td.DmViTriBannerREF,			
			      @NgayThucHien,
			      2,0
				)+ td.KhuyenMaiPhatSinhTrongKy
	            ) KhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_SanPhamTheoTenViTriBanner]
				(	
				td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				    td.DmSanPhamREF ,	
				  td.DmViTriBannerREF,		
			      @NgayThucHien,
			      3,0
				) NoiBoPhatSinhDauKy,
	            td.NoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Ngay_SanPhamTheoTenViTriBanner]
				(	
				td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				  td.DmSanPhamREF ,	
				  td.DmViTriBannerREF,	
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
	           [dbo].[fn_GetDauKy_Of_Ngay_SanPhamTheoTenViTriBanner]
				(
				td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				   td.DmSanPhamREF ,	
				  td.DmViTriBannerREF,
			      @NgayThucHien,
			      1,1
				) SoLuongPhatSinhDauKy,
	            td.SoLuongPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_SanPhamTheoTenViTriBanner]
				(
				td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				  td.DmSanPhamREF ,	
				  td.DmViTriBannerREF,	
			      @NgayThucHien,
			      1,1
				)
	            + td.SoLuongPhatSinhTrongKy
	            ) SoLuongPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_SanPhamTheoTenViTriBanner]
				(
				td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				   td.DmSanPhamREF ,	
				  td.DmViTriBannerREF,		
			      @NgayThucHien,
			      2,1
				) SoLuongKhuyenMaiPhatSinhDauKy,
	            td.SoLuongKhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_SanPhamTheoTenViTriBanner]
				(	
				td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				   td.DmSanPhamREF ,	
				  td.DmViTriBannerREF,			
			      @NgayThucHien,
			      2,1
				)+ td.SoLuongKhuyenMaiPhatSinhTrongKy
	            ) SoLuongKhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_SanPhamTheoTenViTriBanner]
				(	
				td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				   td.DmSanPhamREF ,	
				  td.DmViTriBannerREF,			
			      @NgayThucHien,
			      3,1
				) SoLuongNoiBoPhatSinhDauKy,
	            td.SoLuongNoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Ngay_SanPhamTheoTenViTriBanner]
				(
				td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,	
				  td.DmSanPhamREF ,	
				  td.DmViTriBannerREF,		
			      @NgayThucHien,
			      3,1
				) + td.SoLuongNoiBoPhatSinhTrongKy
	            ) SoLuongNoiBoPhatSinhCuoiKy,
	            td.tenNhanVien,
	            td.DmNhanVienREF,
	            td.TenPhongban,
				td.PhongBanREF,
				td.tenBoPhan,
				td.BoPhanREF,
				td.tenNhom,
				td.NhomREF,
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
