# Stored Procedure: `Insert_rptThucChay_NhanHang_Nam`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-31 11:21:04.220000
- **Ngày sửa cuối**: 2015-03-31 11:21:04.220000

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
CREATE PROCEDURE [dbo].[Insert_rptThucChay_NhanHang_Nam]
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
				rtchdn.DmNhanHangREF
	-----------------------------------UPDATE DL-----------------------------
	UPDATE  rptThucChay_NhanHang_Nam
		SET rptThucChay_NhanHang_Nam.NgayThucHien = @NgayThucHien,
		    rptThucChay_NhanHang_Nam.ThucChayPhatSinhTrongKy += td.ThucChayPhatSinhTrongKy,
		    rptThucChay_NhanHang_Nam.ThucChayPhatSinhCuoiKy += td.ThucChayPhatSinhTrongKy,
		    rptThucChay_NhanHang_Nam.KhuyenMaiPhatSinhTrongKy += td.KhuyenMaiPhatSinhTrongKy,
		    rptThucChay_NhanHang_Nam.KhuyenMaiPhatSinhCuoiKy += td.KhuyenMaiPhatSinhTrongKy,
		    rptThucChay_NhanHang_Nam.NoiBoPhatSinhTrongKy += td.NoiBoPhatSinhTrongKy,
		    rptThucChay_NhanHang_Nam.NoiBoPhatSinhCuoiKy += td.NoiBoPhatSinhTrongKy,
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
		FROM rptThucChay_NhanHang_Nam rtchdt
		INNER JOIN @TeampData td
		ON 
		td.DmNhanVienREF = rtchdt.DmNhanVienREF
		AND td.PhongBanREF = rtchdt.PhongBanREF
		AND td.BoPhanREF = rtchdt.BoPhanREF
		AND td.NhomREF = rtchdt.NhomREF
		AND td.TenDonViTinh = rtchdt.TenDonViTinh
		AND td.UserName = rtchdt.UserName
		AND td.DmNhanHangREF = rtchdt.DmNhanHangREF
		AND td.Nam = rtchdt.Nam
		
		UPDATE  @TeampData 
		SET TrangThai = 1
		FROM rptThucChay_NhanHang_Nam rtchdt
		INNER JOIN @TeampData td
		ON 
		td.DmNhanVienREF = rtchdt.DmNhanVienREF
		AND td.PhongBanREF = rtchdt.PhongBanREF
		AND td.BoPhanREF = rtchdt.BoPhanREF
		AND td.NhomREF = rtchdt.NhomREF
		AND td.TenDonViTinh = rtchdt.TenDonViTinh
		AND td.UserName = rtchdt.UserName
		AND td.DmNhanHangREF = rtchdt.DmNhanHangREF
		AND td.Nam = rtchdt.Nam
		-------------------------------------------------INSERT DL
	    INSERT INTO rptThucChay_NhanHang_Nam
				SELECT 
				@NgayThucHien,
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
				[dbo].[fn_GetDauKy_Of_Ngay_NhanHang]
				(
				td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				  td.DmNhanHangREF ,		
			      @NgayThucHien,
			      1,0
				) ThucChayPhatSinhDauKy,
	            td.ThucChayPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_NhanHang]
				(
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				 td.DmNhanHangREF ,		
			      @NgayThucHien,
			      1,0
				)
	            + td.ThucChayPhatSinhTrongKy
	            ) ThucChayPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_NhanHang]
				(
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				   td.DmNhanHangREF ,		
			      @NgayThucHien,
			      2,0
				) KhuyenMaiPhatSinhDauKy,
	            td.KhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_NhanHang]
				(	
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				   td.DmNhanHangREF ,			
			      @NgayThucHien,
			      2,0
				)+ td.KhuyenMaiPhatSinhTrongKy
	            ) KhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_NhanHang]
				(
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,	
				   td.DmNhanHangREF ,			
			      @NgayThucHien,
			      3,0
				) NoiBoPhatSinhDauKy,
	            td.NoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Ngay_NhanHang]
				(	
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				  td.DmNhanHangREF ,		
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
	           [dbo].[fn_GetDauKy_Of_Ngay_NhanHang]
				(
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				  td.DmNhanHangREF ,		
			      @NgayThucHien,
			      1,1
				) ThucChayPhatSinhDauKy,
	            td.ThucChayPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_NhanHang]
				(
				td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				 td.DmNhanHangREF ,		
			      @NgayThucHien,
			      1,1
				)
	            + td.ThucChayPhatSinhTrongKy
	            ) ThucChayPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_NhanHang]
				(
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				   td.DmNhanHangREF ,		
			      @NgayThucHien,
			      2,1
				) KhuyenMaiPhatSinhDauKy,
	            td.KhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_NhanHang]
				(	
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				   td.DmNhanHangREF ,			
			      @NgayThucHien,
			      2,1
				)+ td.KhuyenMaiPhatSinhTrongKy
	            ) KhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_NhanHang]
				(	
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,
				   td.DmNhanHangREF ,			
			      @NgayThucHien,
			      3,1
				) NoiBoPhatSinhDauKy,
	            td.NoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Ngay_NhanHang]
				(
					td.DmNhanVienREF,
				td.PhongBanREF,
				td.BoPhanREF,
				td.NhomREF,
				td.TenDonViTinh,
				td.UserName,	
				  td.DmNhanHangREF ,		
			      @NgayThucHien,
			      3,1
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
