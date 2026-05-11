# Stored Procedure: `Insert_rptThucChay_KhachHang_TheoHinhThucQuangCao_Nam`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-27 17:43:58.290000
- **Ngày sửa cuối**: 2015-03-27 17:43:58.290000

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
CREATE PROCEDURE [dbo].[Insert_rptThucChay_KhachHang_TheoHinhThucQuangCao_Nam]
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
			TenHinhThucKhachHang NVARCHAR(200),
			DmHinhThucKhachHangREF INT,
			TenHinhThucQuangCao NVARCHAR(200),
			DmHinhThucQuangCaoREF INT,
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
			Nam INT,
			TrangThai INT 
	   )
	  -------------du lieu phat sinh -----------------
	  INSERT INTO @TeampData
	  SELECT
	  rtchdn.TenKhachHang,
	  rtchdn.DmKhachHangREF,
	  '' TenHinhThucKhachHang,
	  '' DmHinhThucKhachHangREF,
	  rtchdn.TenHinhThucQuangCao,
	  rtchdn.DmHinhThucQuangCaoREF,
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
	  YEAR(@NgayThucHien),
	  0
	  FROM DoanhSoThucChayWebsiteTheoThoiGian rtchdn
	  WHERE 1=1 
	  AND rtchdn.NgayThucHien = @NgayThucHien
	  GROUP BY 
	  rtchdn.TenKhachHang,
	  rtchdn.DmKhachHangREF,
	  rtchdn.TenHinhThucQuangCao,
	  rtchdn.DmHinhThucQuangCaoREF,
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
	  UPDATE  rptThucChay_KhachHang_TheoHinhThucQuangCao_Nam 
		SET rptThucChay_KhachHang_TheoHinhThucQuangCao_Nam.NgayThucHien = @NgayThucHien,
		    rptThucChay_KhachHang_TheoHinhThucQuangCao_Nam.ThucChayPhatSinhTrongKy += td.ThucChayPhatSinhTrongKy,
		    rptThucChay_KhachHang_TheoHinhThucQuangCao_Nam.ThucChayPhatSinhCuoiKy += td.ThucChayPhatSinhTrongKy,
		    rptThucChay_KhachHang_TheoHinhThucQuangCao_Nam.KhuyenMaiPhatSinhTrongKy += td.KhuyenMaiPhatSinhTrongKy,
		    rptThucChay_KhachHang_TheoHinhThucQuangCao_Nam.KhuyenMaiPhatSinhCuoiKy += td.KhuyenMaiPhatSinhTrongKy,
		    rptThucChay_KhachHang_TheoHinhThucQuangCao_Nam.NoiBoPhatSinhTrongKy += td.NoiBoPhatSinhTrongKy,
		    rptThucChay_KhachHang_TheoHinhThucQuangCao_Nam.NoiBoPhatSinhCuoiKy += td.NoiBoPhatSinhTrongKy,
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
		FROM rptThucChay_KhachHang_TheoHinhThucQuangCao_Nam rtchdt
		INNER JOIN @TeampData td
		ON 
		td.DmNhanVienREF = rtchdt.DmNhanVienREF
		AND td.PhongBanREF = rtchdt.PhongBanREF
		AND td.BoPhanREF = rtchdt.BoPhanREF
		AND td.NhomREF = rtchdt.NhomREF
		AND td.TenDonViTinh = rtchdt.TenDonViTinh
		AND td.UserName = rtchdt.UserName
		AND td.DmKhachHangREF = rtchdt.DmKhachHangREF
		AND td.DmHinhThucKhachHangREF = rtchdt.DmHinhThucKhachHangREF
		AND td.DmHinhThucQuangCaoREF = rtchdt.DmHinhThucQuangCaoREF
		AND td.Nam = rtchdt.Nam
		
		 UPDATE  @TeampData 
		SET TrangThai = 1
		FROM rptThucChay_KhachHang_TheoHinhThucQuangCao_Nam rtchdt
		INNER JOIN @TeampData td
		ON 
		td.DmNhanVienREF = rtchdt.DmNhanVienREF
		AND td.PhongBanREF = rtchdt.PhongBanREF
		AND td.BoPhanREF = rtchdt.BoPhanREF
		AND td.NhomREF = rtchdt.NhomREF
		AND td.TenDonViTinh = rtchdt.TenDonViTinh
		AND td.UserName = rtchdt.UserName
		AND td.DmKhachHangREF = rtchdt.DmKhachHangREF
		AND td.DmHinhThucKhachHangREF = rtchdt.DmHinhThucKhachHangREF
		AND td.DmHinhThucQuangCaoREF = rtchdt.DmHinhThucQuangCaoREF
		AND td.Nam = rtchdt.Nam
		----------------------------------INSERT dl------------------------------------
		INSERT INTO rptThucChay_KhachHang_TheoHinhThucQuangCao_Nam
				SELECT 
				@NgayThucHien,

				td.Nam,
				td.TenKhachHang,
	            td.DmKhachHangREF,
	            td.TenHinhThucKhachHang,
	            td.DmHinhThucKhachHangREF,
	            td.TenHinhThucQuangCao,
	            td.DmHinhThucQuangCaoREF,
	            '',
				[dbo].[fn_GetDauKy_Of_Ngay_KhachHangTheoHinhThucQuangCao]
				(
					td.DmNhanVienREF,
					td.PhongBanREF,
					td.BoPhanREF,
					td.NhomREF,
					td.TenDonViTinh,
					td.Username,
				  td.DmKhachHangREF,	
				  td.DmHinhThucKhachHangREF	,
				  td.DmHinhThucQuangCaoREF,
			      @NgayThucHien,
			      1,0
				) ThucChayPhatSinhDauKy,
	            td.ThucChayPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_KhachHangTheoHinhThucQuangCao]
				(
					td.DmNhanVienREF,
					td.PhongBanREF,
					td.BoPhanREF,
					td.NhomREF,
					td.TenDonViTinh,
					td.Username,
				   td.DmKhachHangREF,	
				  td.DmHinhThucKhachHangREF	,
				  td.DmHinhThucQuangCaoREF,
			      @NgayThucHien,
			      1,0
				)
	            +  td.ThucChayPhatSinhTrongKy
	            ) ThucChayPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_KhachHangTheoHinhThucQuangCao]
				(
					td.DmNhanVienREF,
					td.PhongBanREF,
					td.BoPhanREF,
					td.NhomREF,
					td.TenDonViTinh,
					td.Username,
				   td.DmKhachHangREF,	
				  td.DmHinhThucKhachHangREF	,
				  td.DmHinhThucQuangCaoREF,
			      @NgayThucHien,
			      2,0
				) KhuyenMaiPhatSinhDauKy,
	            td.KhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_KhachHangTheoHinhThucQuangCao]
				(	
					td.DmNhanVienREF,
					td.PhongBanREF,
					td.BoPhanREF,
					td.NhomREF,
					td.TenDonViTinh,
					td.Username,
				   td.DmKhachHangREF,	
				  td.DmHinhThucKhachHangREF	,
				  td.DmHinhThucQuangCaoREF,
			      @NgayThucHien,
			      2,0
				)+  td.KhuyenMaiPhatSinhTrongKy
	            ) KhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_KhachHangTheoHinhThucQuangCao]
				(
					td.DmNhanVienREF,
					td.PhongBanREF,
					td.BoPhanREF,
					td.NhomREF,
					td.TenDonViTinh,
					td.Username,	
				  td.DmKhachHangREF,	
				  td.DmHinhThucKhachHangREF	,
				  td.DmHinhThucQuangCaoREF,
			      @NgayThucHien,
			      3,0
				) NoiBoPhatSinhDauKy,
	            td.NoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Ngay_KhachHangTheoHinhThucQuangCao]
				(	
					td.DmNhanVienREF,
					td.PhongBanREF,
					td.BoPhanREF,
					td.NhomREF,
					td.TenDonViTinh,
					td.Username,
				    td.DmKhachHangREF,	
				  td.DmHinhThucKhachHangREF	,
				  td.DmHinhThucQuangCaoREF,
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
	             [dbo].[fn_GetDauKy_Of_Ngay_KhachHangTheoHinhThucQuangCao]
				(
					td.DmNhanVienREF,
					td.PhongBanREF,
					td.BoPhanREF,
					td.NhomREF,
					td.TenDonViTinh,
					td.Username,
				 td.DmKhachHangREF,	
				  td.DmHinhThucKhachHangREF	,
				  td.DmHinhThucQuangCaoREF,
			      @NgayThucHien,
			      1,1
				) ThucChayPhatSinhDauKy,
	            td.ThucChayPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_KhachHangTheoHinhThucQuangCao]
				(
					td.DmNhanVienREF,
					td.PhongBanREF,
					td.BoPhanREF,
					td.NhomREF,
					td.TenDonViTinh,
					td.Username,
					td.DmKhachHangREF,	
				  td.DmHinhThucKhachHangREF	,
				  td.DmHinhThucQuangCaoREF,
			      @NgayThucHien,
			      1,1
				)
	            +  td.ThucChayPhatSinhTrongKy
	            ) ThucChayPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_KhachHangTheoHinhThucQuangCao]
				(
					td.DmNhanVienREF,
					td.PhongBanREF,
					td.BoPhanREF,
					td.NhomREF,
					td.TenDonViTinh,
					td.Username,
				   td.DmKhachHangREF,	
				  td.DmHinhThucKhachHangREF	,
				  td.DmHinhThucQuangCaoREF,
			      @NgayThucHien,
			      2,1
				) KhuyenMaiPhatSinhDauKy,
	            td.KhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_KhachHangTheoHinhThucQuangCao]
				(	
					td.DmNhanVienREF,
					td.PhongBanREF,
					td.BoPhanREF,
					td.NhomREF,
					td.TenDonViTinh,
					td.Username,
				   td.DmKhachHangREF,	
				  td.DmHinhThucKhachHangREF	,
				  td.DmHinhThucQuangCaoREF,
			      @NgayThucHien,
			      2,1
				)+  td.KhuyenMaiPhatSinhTrongKy
	            ) KhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_KhachHangTheoHinhThucQuangCao]
				(
					td.DmNhanVienREF,
					td.PhongBanREF,
					td.BoPhanREF,
					td.NhomREF,
					td.TenDonViTinh,
					td.Username,	
				   td.DmKhachHangREF,	
				  td.DmHinhThucKhachHangREF	,
				  td.DmHinhThucQuangCaoREF,
			      @NgayThucHien,
			      3,1
				) NoiBoPhatSinhDauKy,
	            td.NoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Ngay_KhachHangTheoHinhThucQuangCao]
				(
					td.DmNhanVienREF,
					td.PhongBanREF,
					td.BoPhanREF,
					td.NhomREF,
					td.TenDonViTinh,
					td.Username,	
				   td.DmKhachHangREF,	
				  td.DmHinhThucKhachHangREF	,
				  td.DmHinhThucQuangCaoREF,
			      @NgayThucHien,
			      3,1
				) + td.NoiBoPhatSinhTrongKy
	            ) NoiBoPhatSinhCuoiKy,
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

```
