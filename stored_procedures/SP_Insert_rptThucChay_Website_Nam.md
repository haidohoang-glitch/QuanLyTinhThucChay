# Stored Procedure: `Insert_rptThucChay_Website_Nam`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-27 17:44:05.090000
- **Ngày sửa cuối**: 2015-03-27 17:44:05.090000

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
--EXEC [dbo].[Insert_rptThucChay_Website_Nam] '2013-01-01'
CREATE PROCEDURE [dbo].[Insert_rptThucChay_Website_Nam]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	DECLARE @TeampData TABLE 
	   (
	        TenNhanVien NVARCHAR(500),
			DmNhanVienREF INT,
			TenPhongBan NVARCHAR(500),
			PhongBanREF INT,
			TenBoPhan NVARCHAR(500),
			BoPhanREF INT,
			TenNhom NVARCHAR(500),
			NhomREF INT,
			TenDonViTinh NVARCHAR(500),
			UserName NVARCHAR(500),
			TenWebsite NVARCHAR(500),
			DmWebsiteREF INT,
			ThucChayPhatSinhTrongKy FLOAT,
			KhuyenMaiPhatSinhTrongKy FLOAT,
			NoiBoPhatSinhTrongKy FLOAT,
			SoluongPhatSinhTrongKy FLOAT,
			SoLuongKhuyenMaiPhatSinhTrongKy FLOAT,
			SoLuongNoiBoPhatSinhTrongKy FLOAT,
			ThucChayThayDoiTrongKy FLOAT,
			NoiBoThayDoiTrongKy FLOAT,
			KhuyenMaiThayDoiTrongKy FLOAT,
			SoLuongThayDoiTrongKy FLOAT,
			SoLuongNoiBoThayDoiTrongKy FLOAT,
			SoLuongKhuyenMaiThayDoiTrongKy FLOAT,
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
			     rtchdn.PhongBanREF,
			     rtchdn.TenBoPhan,
			     rtchdn.BoPhanREF,
			     rtchdn.TenNhom,
			     rtchdn.NhomREF,
			     rtchdn.TenDonViTinh,
			     rtchdn.UserName,
				rtchdn.TenWebsite,
				rtchdn.DmWebsiteREF,
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
			     rtchdn.PhongBanREF,
			     rtchdn.TenBoPhan,
			     rtchdn.BoPhanREF,
			     rtchdn.TenNhom,
			     rtchdn.NhomREF,
			     rtchdn.TenDonViTinh,
			     rtchdn.UserName,
				rtchdn.TenWebsite,
				rtchdn.DmWebsiteREF
	-----------------------------------UPDATE DL-----------------------------
	UPDATE  rptThucChay_Website_Nam 
		SET rptThucChay_Website_Nam.NgayThucHien = @NgayThucHien,
		    rptThucChay_Website_Nam.ThucChayPhatSinhTrongKy += td.ThucChayPhatSinhTrongKy,
		    rptThucChay_Website_Nam.ThucChayPhatSinhCuoiKy += td.ThucChayPhatSinhTrongKy,
		    rptThucChay_Website_Nam.KhuyenMaiPhatSinhTrongKy += td.KhuyenMaiPhatSinhTrongKy,
		    rptThucChay_Website_Nam.KhuyenMaiPhatSinhCuoiKy += td.KhuyenMaiPhatSinhTrongKy,
		    rptThucChay_Website_Nam.NoiBoPhatSinhTrongKy += td.NoiBoPhatSinhTrongKy,
		    rptThucChay_Website_Nam.NoiBoPhatSinhCuoiKy += td.NoiBoPhatSinhTrongKy,
		     rptThucChay_Website_Nam.SoLuongPhatSinhTrongKy += td.SoLuongPhatSinhTrongKy,
		    rptThucChay_Website_Nam.SoLuongPhatSinhCuoiKy += td.SoLuongPhatSinhTrongKy,
		    rptThucChay_Website_Nam.SoLuongKhuyenMaiPhatSinhTrongKy += td.SoLuongKhuyenMaiPhatSinhTrongKy,
		    rptThucChay_Website_Nam.SoLuongKhuyenMaiPhatSinhCuoiKy += td.SoLuongKhuyenMaiPhatSinhTrongKy,
		    rptThucChay_Website_Nam.SoLuongNoiBoPhatSinhTrongKy += td.SoLuongNoiBoPhatSinhTrongKy,
		    rptThucChay_Website_Nam.SoLuongNoiBoPhatSinhCuoiKy += td.SoLuongNoiBoPhatSinhTrongKy,
		     ThucChayThayDoiTrongKy += td.ThucChayThayDoiTrongKy,
	 			NoiBoThayDoiTrongKy += td.NoiBoThayDoiTrongKy,
	 			KhuyenMaiThayDoiTrongKy += td.KhuyenMaiThayDoiTrongKy,
	 			SoLuongThayDoiTrongKy +=td.SoLuongThayDoiTrongKy,
	 			SoLuongNoiBoThayDoiTrongKy +=td.SoLuongNoiBoThayDoiTrongKy,
	 			SoLuongKhuyenMaiThayDoiTrongKy += td.SoLuongKhuyenMaiThayDoiTrongKy 
		FROM rptThucChay_Website_Nam rtchdt
		INNER JOIN @TeampData td
		ON 
		td.DmNhanVienREF = rtchdt.DmNhanVienREF
		AND td.PhongBanREF = rtchdt.PhongBanREF
		AND td.BoPhanREF = rtchdt.BoPhanREF
		AND td.NhomREF = rtchdt.NhomREF
		AND td.TenDonViTinh = rtchdt.TenDonViTinh
		AND td.UserName = rtchdt.UserName
		AND td.DmWebsiteREF = rtchdt.DmWebsiteREF
		AND td.Nam = rtchdt.Nam
		
		UPDATE  @TeampData 
		SET TrangThai = 1
		FROM rptThucChay_Website_Nam rtchdt
		INNER JOIN @TeampData td
		ON 
		td.DmNhanVienREF = rtchdt.DmNhanVienREF
		AND td.PhongBanREF = rtchdt.PhongBanREF
		AND td.BoPhanREF = rtchdt.BoPhanREF
		AND td.NhomREF = rtchdt.NhomREF
		AND td.TenDonViTinh = rtchdt.TenDonViTinh
		AND td.UserName = rtchdt.UserName
		AND td.DmWebsiteREF = rtchdt.DmWebsiteREF
		AND td.Nam = rtchdt.Nam
		-------------------------------------------------INSERT DL
	    INSERT INTO rptThucChay_Website_Nam
				SELECT 
				@NgayThucHien,
				td.Nam,
				td.TenWebsite, 
			    td.DmWebsiteREF ,
			   
				[dbo].[fn_GetDauKy_Of_Ngay_Website]
				(
					td.DmNhanVienREF,
	             td.PhongBanREF,
	             td.BoPhanREF,
	             td.NhomREF,
	             td.TenDonViTinh,
	             td.Username,
				  td.DmWebsiteREF ,		
			      @NgayThucHien,
			      1,0
				) ThucChayPhatSinhDauKy,
	            td.ThucChayPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_Website]
				(
					td.DmNhanVienREF,
	             td.PhongBanREF,
	             td.BoPhanREF,
	             td.NhomREF,
	             td.TenDonViTinh,
	             td.Username,
				 td.DmWebsiteREF ,		
			      @NgayThucHien,
			      1,0
				)
	            + td.ThucChayPhatSinhTrongKy
	            ) ThucChayPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_Website]
				(
					td.DmNhanVienREF,
	             td.PhongBanREF,
	             td.BoPhanREF,
	             td.NhomREF,
	             td.TenDonViTinh,
	             td.Username,
				   td.DmWebsiteREF ,		
			      @NgayThucHien,
			      2,0
				) KhuyenMaiPhatSinhDauKy,
	            td.KhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_Website]
				(
					td.DmNhanVienREF,
	             td.PhongBanREF,
	             td.BoPhanREF,
	             td.NhomREF,
	             td.TenDonViTinh,
	             td.Username,	
				   td.DmWebsiteREF ,			
			      @NgayThucHien,
			      2,0
				)+ td.KhuyenMaiPhatSinhTrongKy
	            ) KhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_Website]
				(
					td.DmNhanVienREF,
	             td.PhongBanREF,
	             td.BoPhanREF,
	             td.NhomREF,
	             td.TenDonViTinh,
	             td.Username,	
				   td.DmWebsiteREF ,			
			      @NgayThucHien,
			      3,0
				) NoiBoPhatSinhDauKy,
	            td.NoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Ngay_Website]
				(
					td.DmNhanVienREF,
	             td.PhongBanREF,
	             td.BoPhanREF,
	             td.NhomREF,
	             td.TenDonViTinh,
	             td.Username,	
				  td.DmWebsiteREF ,		
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
	           [dbo].[fn_GetDauKy_Of_Ngay_Website]
				(
					td.DmNhanVienREF,
	             td.PhongBanREF,
	             td.BoPhanREF,
	             td.NhomREF,
	             td.TenDonViTinh,
	             td.Username,
				  td.DmWebsiteREF ,		
			      @NgayThucHien,
			      1,1
				) SoLuongPhatSinhDauKy,
	            td.SoLuongPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_Website]
				(
					td.DmNhanVienREF,
	             td.PhongBanREF,
	             td.BoPhanREF,
	             td.NhomREF,
	             td.TenDonViTinh,
	             td.Username,
				 td.DmWebsiteREF ,		
			      @NgayThucHien,
			      1,1
				)
	            + td.SoLuongPhatSinhTrongKy
	            ) SoLuongPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_Website]
				(
					td.DmNhanVienREF,
	             td.PhongBanREF,
	             td.BoPhanREF,
	             td.NhomREF,
	             td.TenDonViTinh,
	             td.Username,
				   td.DmWebsiteREF ,		
			      @NgayThucHien,
			      2,1
				) SoLuongKhuyenMaiPhatSinhDauKy,
	            td.SoLuongKhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_Website]
				(	
					td.DmNhanVienREF,
	             td.PhongBanREF,
	             td.BoPhanREF,
	             td.NhomREF,
	             td.TenDonViTinh,
	             td.Username,
				   td.DmWebsiteREF ,			
			      @NgayThucHien,
			      2,1
				)+ td.SoLuongKhuyenMaiPhatSinhTrongKy
	            ) SoLuongKhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_Website]
				(
					td.DmNhanVienREF,
	             td.PhongBanREF,
	             td.BoPhanREF,
	             td.NhomREF,
	             td.TenDonViTinh,
	             td.Username,	
				   td.DmWebsiteREF ,			
			      @NgayThucHien,
			      3,1
				) SoLuongNoiBoPhatSinhDauKy,
	            td.SoLuongNoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Ngay_Website]
				(

	             td.DmNhanVienREF,
	             td.PhongBanREF,
	             td.BoPhanREF,
	             td.NhomREF,
	             td.TenDonViTinh,
	             td.Username,	
				  td.DmWebsiteREF ,		
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
				WHERE 1=1 AND td.TrangThai <> 1
END

```
