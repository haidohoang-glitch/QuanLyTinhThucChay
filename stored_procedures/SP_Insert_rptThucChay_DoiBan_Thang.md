# Stored Procedure: `Insert_rptThucChay_DoiBan_Thang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-27 17:43:46.587000
- **Ngày sửa cuối**: 2015-03-27 17:43:46.587000

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
CREATE PROCEDURE [dbo].[Insert_rptThucChay_DoiBan_Thang]
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
     ---- Du Lieu Phat Sinh
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
     SUM(isnull(rtchdn.ThucChayPhatSinhTrongKy,0)),
     SUM(isnull(rtchdn.KhuyenMaiPhatSinhTrongKy,0)),
     SUM(isnull(rtchdn.NoiBoPhatSinhTrongKy,0)),
     SUM(isnull(rtchdn.SoLuongPhatSinhTrongKy,0)),
     SUM(isnull(rtchdn.SoLuongKhuyenMaiPhatSinhTrongKy,0)),
     SUM(isnull(rtchdn.SoLuongNoiBoPhatSinhTrongKy,0)),
     SUM(isnull(rtchdn.ThucChayThayDoiTrongKy,0)),
     SUM(isnull(rtchdn.NoiBoThayDoiTrongKy,0)),
     SUM(isnull(rtchdn.KhuyenmaiThayDoiTrongKy,0)),
     SUM(isnull(rtchdn.SoLuongThayDoiTrongKy,0)),
     SUM(isnull(rtchdn.SoLuongNoiBoThayDoiTrongKy,0)),
     SUM(isnull(rtchdn.SoLuongKhuyenMaiThayDoiTrongKy,0)),
     MONTH(@NgayThucHien),
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
     rtchdn.UserName
     ----------------------------------UPDATE DL-----------------------------
     UPDATE rptThucChay_DoiBan_Thang
     SET
     NgayThucHien = @NgayThucHien,
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
     
     FROM rptThucChay_DoiBan_Thang rtcdbt
     INNER JOIN @TeampData td ON
     td.DmNhanVienREF = rtcdbt.DmNhanVienREF
	 AND td.PhongBanREF = rtcdbt.PhongBanREF
	 AND td.BoPhanREF = rtcdbt.BoPhanREF
	 AND td.NhomREF = rtcdbt.NhomREF
	 AND td.TenDonViTinh = rtcdbt.TenDonViTinh
	 AND td.UserName = rtcdbt.UserName
     AND td.Thang = rtcdbt.Thang
     AND td.Nam = rtcdbt.Nam
     ---------
      UPDATE @TeampData
     SET
     TrangThai = 1
     FROM rptThucChay_DoiBan_Thang rtcdbt
     INNER JOIN @TeampData td ON
    td.DmNhanVienREF = rtcdbt.DmNhanVienREF
	 AND td.PhongBanREF = rtcdbt.PhongBanREF
	 AND td.BoPhanREF = rtcdbt.BoPhanREF
	 AND td.NhomREF = rtcdbt.NhomREF
	 AND td.TenDonViTinh = rtcdbt.TenDonViTinh
	 AND td.UserName = rtcdbt.UserName
     AND td.Thang = rtcdbt.Thang
     AND td.Nam = rtcdbt.Nam
     --------------------------------insert dl-------------------------------------
     INSERT INTO rptThucChay_DoiBan_Thang
				SELECT 
				@NgayThucHien,
				td.Thang,
				td.Nam,
				td.TenPhongBan,
				td.PhongBanREF,
				td.TenBoPhan,
				td.BoPhanREF,
				td.TenNhom,
				td.NhomREF,
				[dbo].[fn_GetDauKy_Of_Ngay_DoiBan]
				(
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,		
			      @NgayThucHien,
			      1,0
				) ThucChayPhatSinhDauKy,
	            td.ThucChayPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_DoiBan]
				(
				 td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,
			      @NgayThucHien,
			      1,0
				)
	            + td.ThucChayPhatSinhTrongKy
	            ) ThucChayPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_DoiBan]
				(
				td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,
			      @NgayThucHien,
			      2,0
				) KhuyenMaiPhatSinhDauKy,
	            td.KhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_DoiBan]
				(	
				td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,	
			      @NgayThucHien,
			      2,0
				)+ td.KhuyenMaiPhatSinhTrongKy
	            ) KhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_DoiBan]
				(	
				 td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,
			      @NgayThucHien,
			      3,0
				) NoiBoPhatSinhDauKy,
	            td.NoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Ngay_DoiBan]
				(	
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,
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
	           [dbo].[fn_GetDauKy_Of_Ngay_DoiBan]
				(
				 td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,	
			      @NgayThucHien,
			      1,1
				) SoLuongPhatSinhDauKy,
	            td.SoLuongPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_DoiBan]
				(
				 td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,
			      @NgayThucHien,
			      1,1
				)
	            + td.SoLuongPhatSinhTrongKy
	            ) SoLuongPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_DoiBan]
				(
				td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,
			      @NgayThucHien,
			      2,1
				) SoLuongKhuyenMaiPhatSinhDauKy,
	            td.SoLuongKhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_DoiBan]
				(	
				 td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,	
			      @NgayThucHien,
			      2,1
				)+ td.SoLuongKhuyenMaiPhatSinhTrongKy
	            ) SoLuongKhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_DoiBan]
				(	
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,
			      @NgayThucHien,
			      3,1
				) SoLuongNoiBoPhatSinhDauKy,
	            td.SoLuongNoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Ngay_DoiBan]
				(	
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,
			      @NgayThucHien,
			      3,1
				) + td.SoLuongNoiBoPhatSinhTrongKy
	            ) SoLuongNoiBoPhatSinhCuoiKy,
	            td.TenNhanVien,
	            td.DmNhanVienREF,
	            td.TenDonViTinh,
	            td.Username,
	            td.ThucChayThayDoiTrongKy,
	            td.NoiBoThayDoiTrongKy,
	            td.KhuyenMaiThayDoiTrongKy,
	            td.SoLuongThayDoiTrongKy,
	            td.SoLuongNoiBoThayDoiTrongKy,
	            td.SoLuongKhuyenMaiThayDoiTrongKy
				FROM @TeampData td WHERE td.TrangThai <>1
END

```
