# Stored Procedure: `Insert_rptThucChay_HinhThucQuangCao_TheoSanPham_ViTriBanner_Quy`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-27 17:43:48.890000
- **Ngày sửa cuối**: 2015-03-27 17:43:48.890000

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
CREATE PROCEDURE [dbo].[Insert_rptThucChay_HinhThucQuangCao_TheoSanPham_ViTriBanner_Quy]
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
	   		TenPhongBan NVARCHAR(200),
	   		PhongBanREF INT,
	   		TenBoPhan NVARCHAR(200),
	   		BoPhanREF INT,
	   		TenNhom NVARCHAR(200),
	   		NhomREF INT,
	   		TenDonViTinh NVARCHAR(50),
	   		UserName NVARCHAR(50),
			TenHinhThucQuangCao NVARCHAR(200),
			DmHinhThucQuangCaoREF INT,
			TenSanPham NVARCHAR(200),
			DmSanPhamREF INT,
			TenViTriBanner NVARCHAR(200),
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
			Quy INT,
			Nam INT,
			TrangThai INT 
		)
    -- Insert statements for procedure here
	INSERT INTO @TeampData
	SELECT
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
		rtchdn.TenHinhThucQuangCao,
	rtchdn.DmHinhThucQuangCaoREF,
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
	0
	FROM DoanhSoThucChayWebsiteTheoThoiGian rtchdn
	WHERE 1=1
	AND rtchdn.NgayThucHien = @NgayThucHien
	GROUP BY
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
		rtchdn.TenHinhThucQuangCao,
	rtchdn.DmHinhThucQuangCaoREF,
	rtchdn.TenSanPham,
	rtchdn.DmSanPhamREF,
	rtchdn.TenViTriBanner,
	rtchdn.DmViTriBannerREF
	-------------------------------------UPDATE DL--------------------------------
	UPDATE rptThucChay_HinhThucQuangCao_TheoSanPham_ViTriBanner_Quy
	SET NgayThucHien = @NgayThucHien,
	ThucChayPhatSinhTrongKy += td.ThucChayPhatSinhTrongKy,
	ThucChayPhatSinhCuoiKy += td.ThucChayPhatSinhTrongKy,
	KhuyenMaiPhatSinhTrongKy += td.KhuyenMaiPhatSinhTrongKy,
	KhuyenMaiPhatSinhCuoiKy += td.KhuyenMaiPhatSinhTrongKy,
	NoiBoPhatSinhTrongKy +=td.NoiBoPhatSinhTrongKy,
	NoiBoPhatSinhCuoiKy += td.NoiBoPhatSinhTrongKy ,
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
	FROM rptThucChay_HinhThucQuangCao_TheoSanPham_ViTriBanner_Quy rtchtqct
	INNER JOIN @TeampData td ON
	 td.DmNhanVienREF = rtchtqct.DmNhanVienREF
	 AND td.PhongBanREF = rtchtqct.PhongBanREF
	 AND td.BoPhanREF = rtchtqct.BoPhanREF
	 AND td.NhomREF = rtchtqct.NhomREF
	 AND td.TenDonViTinh = rtchtqct.TenDonViTinh
	 AND td.UserName = rtchtqct.UserName
	AND td.DmHinhThucQuangCaoREF = rtchtqct.DmHinhThucQuangCaoREF
	AND td.DmSanPhamREF = rtchtqct.DmSanPhamREF
	AND td.DmViTriBannerREF = rtchtqct.DmViTriBannerREF
	AND td.Quy = rtchtqct.Quy
	AND td.Nam = rtchtqct.Nam
	--------------
	UPDATE @TeampData
	SET TrangThai = 1 
	FROM rptThucChay_HinhThucQuangCao_TheoSanPham_ViTriBanner_Quy rtchtqct
	INNER JOIN @TeampData td on
	 td.DmNhanVienREF = rtchtqct.DmNhanVienREF
	 AND td.PhongBanREF = rtchtqct.PhongBanREF
	 AND td.BoPhanREF = rtchtqct.BoPhanREF
	 AND td.NhomREF = rtchtqct.NhomREF
	 AND td.TenDonViTinh = rtchtqct.TenDonViTinh
	 AND td.UserName = rtchtqct.UserName
	AND td.DmHinhThucQuangCaoREF = rtchtqct.DmHinhThucQuangCaoREF
	AND td.DmSanPhamREF = rtchtqct.DmSanPhamREF
	AND td.DmViTriBannerREF = rtchtqct.DmViTriBannerREF
	AND td.Quy = rtchtqct.Quy
	AND td.Nam = rtchtqct.Nam
	-------------------------------------INSERT DL--------------------------------------
	INSERT INTO rptThucChay_HinhThucQuangCao_TheoSanPham_ViTriBanner_Quy
				SELECT 
				@NgayThucHien,
				td.Quy,
				td.Nam,
				td.TenHinhThucQuangCao,
				td.DmHinhThucQuangCaoREF,
				td.TenSanPham,
				td.DmSanPhamREF,
				td.TenViTriBanner,
				td.DmViTriBannerREF,
				[dbo].[fn_GetDauKy_Of_Ngay_HinhThucQuangCaoTheoSanPhamViTriBanner]
				(
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,
				  td.DmHinhThucQuangCaoREF,	
				  td.DmSanPhamREF,	
				  td.DmViTriBannerREF,
			      @NgayThucHien,
			      1,0
				) ThucChayPhatSinhDauKy,
	            td.ThucChayPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_HinhThucQuangCaoTheoSanPhamViTriBanner]
				(
					td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,
				  td.DmHinhThucQuangCaoREF,	
				  td.DmSanPhamREF,	
				  td.DmViTriBannerREF,
			      @NgayThucHien,
			      1,0
				)
	            + td.ThucChayPhatSinhTrongKy
	            ) ThucChayPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_HinhThucQuangCaoTheoSanPhamViTriBanner]
				(
					td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,
				  td.DmHinhThucQuangCaoREF,	
				  td.DmSanPhamREF,	
				  td.DmViTriBannerREF,
			      @NgayThucHien,
			      2,0
				) KhuyenMaiPhatSinhDauKy,
	            td.KhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_HinhThucQuangCaoTheoSanPhamViTriBanner]
				(	
					td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,
				  td.DmHinhThucQuangCaoREF,	
				  td.DmSanPhamREF,	
				  td.DmViTriBannerREF,	
			      @NgayThucHien,
			      2,0
				)+ td.KhuyenMaiPhatSinhTrongKy
	            ) KhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_HinhThucQuangCaoTheoSanPhamViTriBanner]
				(	
					td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,
				  td.DmHinhThucQuangCaoREF,	
				  td.DmSanPhamREF,	
				  td.DmViTriBannerREF,
			      @NgayThucHien,
			      3,0
				) NoiBoPhatSinhDauKy,
	            td.NoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Ngay_HinhThucQuangCaoTheoSanPhamViTriBanner]
				(	
					td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,
				  td.DmHinhThucQuangCaoREF,	
				  td.DmSanPhamREF,	
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
	           [dbo].[fn_GetDauKy_Of_Ngay_HinhThucQuangCaoTheoSanPhamViTriBanner]
				(
					td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,
				  td.DmHinhThucQuangCaoREF,	
				  td.DmSanPhamREF,	
				  td.DmViTriBannerREF,	
			      @NgayThucHien,
			      1,1
				) SoLuongPhatSinhDauKy,
	            td.SoLuongPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_HinhThucQuangCaoTheoSanPhamViTriBanner]
				(
					td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,
				  td.DmHinhThucQuangCaoREF,	
				  td.DmSanPhamREF,	
				  td.DmViTriBannerREF,
			      @NgayThucHien,
			      1,1
				)
	            + td.SoLuongPhatSinhTrongKy
	            ) SoLuongPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_HinhThucQuangCaoTheoSanPhamViTriBanner]
				(
					td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,
				  td.DmHinhThucQuangCaoREF,	
				  td.DmSanPhamREF,	
				  td.DmViTriBannerREF,	
			      @NgayThucHien,
			      2,1
				) SoLuongKhuyenMaiPhatSinhDauKy,
	            td.SoLuongKhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_HinhThucQuangCaoTheoSanPhamViTriBanner]
				(
					td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,
				  td.DmHinhThucQuangCaoREF,	
				  td.DmSanPhamREF,	
				  td.DmViTriBannerREF,	
			      @NgayThucHien,
			      2,1
				)+ td.SoLuongKhuyenMaiPhatSinhTrongKy
	            ) SoLuongKhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_HinhThucQuangCaoTheoSanPhamViTriBanner]
				(
					td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,
				  td.DmHinhThucQuangCaoREF,	
				  td.DmSanPhamREF,	
				  td.DmViTriBannerREF,
			      @NgayThucHien,
			      3,1
				) SoLuongNoiBoPhatSinhDauKy,
	            td.SoLuongNoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Ngay_HinhThucQuangCaoTheoSanPhamViTriBanner]
				(
					td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,
				  td.DmHinhThucQuangCaoREF,	
				  td.DmSanPhamREF,	
				  td.DmViTriBannerREF,	
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
				WHERE 1=1 
				AND td.TrangThai <>1
END

```
