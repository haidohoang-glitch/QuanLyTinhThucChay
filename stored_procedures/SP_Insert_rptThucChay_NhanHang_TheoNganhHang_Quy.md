# Stored Procedure: `Insert_rptThucChay_NhanHang_TheoNganhHang_Quy`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-31 11:21:06.127000
- **Ngày sửa cuối**: 2015-03-31 11:21:06.127000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author  Quye>
-- Create date: <Create Date  >
-- Description:	<Description  >
-- =============================================
CREATE PROCEDURE [dbo].[Insert_rptThucChay_NhanHang_TheoNganhHang_Quy]
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
	        DsTenNganhHang NVARCHAR(200),
	        DmListNganhHangREF NVARCHAR(200),
	        TenDonViTinh nvarchar(50),
	        UserName nvarchar(50),
			TenNhanHang NVARCHAR(500),
			DmNhanHangREF INT,
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
			    rtchdn.DsTenNganhHang,
			    rtchdn.DmListNganhHangREF,
			    rtchdn.TenDonViTinh,
			    rtchdn.UserName,
				rtchdn.TenNhanHang,
				rtchdn.DmNhanHangREF,
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
			 FROM  DoanhSoThucChayNhanHangCore  rtchdn
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
			    rtchdn.TenNhanHang,
				rtchdn.DmNhanHangREF,
				rtchdn.DsTenNganhHang,
			    rtchdn.DmListNganhHangREF
	-----------------------------------UPDATE DL-----------------------------
	UPDATE  rptThucChay_NhanHang_TheoNganhHang_Quy
		SET rptThucChay_NhanHang_TheoNganhHang_Quy.NgayThucHien = @NgayThucHien,
		    rptThucChay_NhanHang_TheoNganhHang_Quy.ThucChayPhatSinhTrongKy += td.ThucChayPhatSinhTrongKy,
		    rptThucChay_NhanHang_TheoNganhHang_Quy.ThucChayPhatSinhCuoiKy += td.ThucChayPhatSinhTrongKy,
		    rptThucChay_NhanHang_TheoNganhHang_Quy.KhuyenMaiPhatSinhTrongKy += td.KhuyenMaiPhatSinhTrongKy,
		    rptThucChay_NhanHang_TheoNganhHang_Quy.KhuyenMaiPhatSinhCuoiKy += td.KhuyenMaiPhatSinhTrongKy,
		    rptThucChay_NhanHang_TheoNganhHang_Quy.NoiBoPhatSinhTrongKy += td.NoiBoPhatSinhTrongKy,
		    rptThucChay_NhanHang_TheoNganhHang_Quy.NoiBoPhatSinhCuoiKy += td.NoiBoPhatSinhTrongKy,
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
		FROM rptThucChay_NhanHang_TheoNganhHang_Quy rtchdt
		INNER JOIN @TeampData td
		ON 
		td.DmNhanVienREF = rtchdt.DmNhanVienREF
		AND td.PhongBanREF = rtchdt.PhongBanREF
		AND td.BoPhanREF = rtchdt.BoPhanREF
		AND td.NhomREF = rtchdt.NhomREF
		AND td.TenDonViTinh = rtchdt.TenDonViTinh
		AND td.UserName = rtchdt.UserName
		AND td.DmNhanHangREF = rtchdt.DmNhanHangREF
		AND td.DmListNganhHangREF = rtchdt.DmListNganhHangREF
		AND td.Quy = rtchdt.Quy
		AND td.Nam = rtchdt.Nam
		
		UPDATE  @TeampData 
		SET TrangThai = 1
		FROM rptThucChay_NhanHang_TheoNganhHang_Quy rtchdt
		INNER JOIN @TeampData td
		ON 
		td.DmNhanVienREF = rtchdt.DmNhanVienREF
		AND td.PhongBanREF = rtchdt.PhongBanREF
		AND td.BoPhanREF = rtchdt.BoPhanREF
		AND td.NhomREF = rtchdt.NhomREF
		AND td.TenDonViTinh = rtchdt.TenDonViTinh
		AND td.UserName = rtchdt.UserName
		AND td.DmNhanHangREF = rtchdt.DmNhanHangREF
		AND td.DmListNganhHangREF = rtchdt.DmListNganhHangREF
		AND td.Quy = rtchdt.Quy
		AND td.Nam = rtchdt.Nam
		-------------------------------------------------INSERT DL
	    INSERT INTO rptThucChay_NhanHang_TheoNganhHang_Quy
				SELECT 
				@NgayThucHien,
				td.Quy,
				td.Nam,
				td.TenNhanHang, 
				td.DmNhanHangREF ,
			    
	            td.TenNhanVien,
	            td.DmNhanVienREF,
	            td.TenPhongBan,
	            td.PhongBanREF,
	            td.TenBoPhan,
	            td.BoPhanREF,
	            td.TenNhom,
	            td.NhomREF,
	            td.DsTenNganhHang,
	            td.DmListNganhHangREF,
				[dbo].[fn_GetDauKy_Of_Ngay_NhanHangTheoNganhHang]
				(
				td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				  td.DmNhanHangREF ,		
			      @NgayThucHien,
			      1,0,td.DmListNganhHangREF
				) ThucChayPhatSinhDauKy,
	            td.ThucChayPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_NhanHangTheoNganhHang]
				(
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				 td.DmNhanHangREF ,		
			      @NgayThucHien,
			      1,0,td.DmListNganhHangREF
				)
	            + td.ThucChayPhatSinhTrongKy
	            ) ThucChayPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_NhanHangTheoNganhHang]
				(
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				   td.DmNhanHangREF ,		
			      @NgayThucHien,
			      2,0,td.DmListNganhHangREF
				) KhuyenMaiPhatSinhDauKy,
	            td.KhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_NhanHangTheoNganhHang]
				(	
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				   td.DmNhanHangREF ,			
			      @NgayThucHien,
			      2,0,td.DmListNganhHangREF
				)+ td.KhuyenMaiPhatSinhTrongKy
	            ) KhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_NhanHangTheoNganhHang]
				(
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,	
				   td.DmNhanHangREF ,			
			      @NgayThucHien,
			      3,0,td.DmListNganhHangREF
				) NoiBoPhatSinhDauKy,
	            td.NoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Ngay_NhanHangTheoNganhHang]
				(	
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				  td.DmNhanHangREF ,		
			      @NgayThucHien,
			      3,0,td.DmListNganhHangREF
				) + td.NoiBoPhatSinhTrongKy
	            ) NoiBoPhatSinhCuoiKy,
	           'ASD' CreatedBy,
	           GETDATE() CreatedAt,
	           'ASD' LastModifiedBy,
	           GETDATE() LastModifiedAt,
	           0 DeletedStatus,
	           0 RecordStatus,
	           0 PrintStatus,
	           [dbo].[fn_GetDauKy_Of_Ngay_NhanHangTheoNganhHang]
				(
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				  td.DmNhanHangREF ,		
			      @NgayThucHien,
			      1,1,td.DmListNganhHangREF
				) ThucChayPhatSinhDauKy,
	            td.ThucChayPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_NhanHangTheoNganhHang]
				(
				td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				 td.DmNhanHangREF ,		
			      @NgayThucHien,
			      1,1,td.DmListNganhHangREF
				)
	            + td.ThucChayPhatSinhTrongKy
	            ) ThucChayPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_NhanHangTheoNganhHang]
				(
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				   td.DmNhanHangREF ,		
			      @NgayThucHien,
			      2,1,td.DmListNganhHangREF
				) KhuyenMaiPhatSinhDauKy,
	            td.KhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_NhanHangTheoNganhHang]
				(	
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				   td.DmNhanHangREF ,			
			      @NgayThucHien,
			      2,1,td.DmListNganhHangREF
				)+ td.KhuyenMaiPhatSinhTrongKy
	            ) KhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_NhanHangTheoNganhHang]
				(	
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				   td.DmNhanHangREF ,			
			      @NgayThucHien,
			      3,1,td.DmListNganhHangREF
				) NoiBoPhatSinhDauKy,
	            td.NoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Ngay_NhanHangTheoNganhHang]
				(
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,	
				  td.DmNhanHangREF ,		
			      @NgayThucHien,
			      3,1,td.DmListNganhHangREF
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
