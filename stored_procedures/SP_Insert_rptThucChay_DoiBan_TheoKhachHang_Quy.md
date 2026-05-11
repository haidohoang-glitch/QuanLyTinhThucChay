# Stored Procedure: `Insert_rptThucChay_DoiBan_TheoKhachHang_Quy`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-07 12:18:29.920000
- **Ngày sửa cuối**: 2015-03-07 12:18:29.920000

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
CREATE PROCEDURE [dbo].[Insert_rptThucChay_DoiBan_TheoKhachHang_Quy]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	  DECLARE @TeampData TABLE 
	   (
	   	    TenPhongBan NVARCHAR(200),
			PhongBanREF INT,
			TenBoPhan NVARCHAR(200),
			BoPhanREF INT,
			TenNhom NVARCHAR(200),
		    NhomREF INT,
		    TenKhachHang NVARCHAR(200),
		    DmKhachHangREF INT,
			ThucChayPhatSinhTrongKy FLOAT,
			KhuyenMaiPhatSinhTrongKy FLOAT,
			NoiBoPhatSinhTrongKy FLOAT,
			SoLuongPhatSinhTrongKy BIGINT,
			SoLuongKhuyenMaiPhatSinhTrongKy BIGINT,
			SoLuongNoiBoPhatSinhTrongKy BIGINT,
			Quy INT,
			Nam INT,
			TrangThai INT 
		)
     ---- Du Lieu Phat Sinh
     INSERT INTO @TeampData
     SELECT 
     rtchdn.TenPhongBan,
     rtchdn.PhongBanREF,
     rtchdn.TenBoPhan,
     rtchdn.BoPhanREF,
     rtchdn.TenNhom,
     rtchdn.NhomREF,
     rtchdn.TenKhachHang,
     rtchdn.DmKhachHangREF,
     SUM(isnull(rtchdn.ThucChayPhatSinhTrongKy,0)),
     SUM(isnull(rtchdn.KhuyenMaiPhatSinhTrongKy,0)),
     SUM(isnull(rtchdn.NoiBoPhatSinhTrongKy,0)),
     SUM(isnull(rtchdn.SoLuongPhatSinhTrongKy,0)),
     SUM(isnull(rtchdn.SoLuongKhuyenMaiPhatSinhTrongKy,0)),
     SUM(isnull(rtchdn.SoLuongNoiBoPhatSinhTrongKy,0)),
     DATEPART(QQ,@NgayThucHien),
     YEAR(@NgayThucHien),
     0
     FROM DoanhSoThucChayHopDongTheoThoiGian rtchdn
     WHERE 1=1
     AND rtchdn.NgayThucHien = @NgayThucHien
     GROUP BY
     rtchdn.TenPhongBan,
     rtchdn.PhongBanREF,
     rtchdn.TenBoPhan,
     rtchdn.BoPhanREF,
     rtchdn.TenNhom,
     rtchdn.NhomREF,
     rtchdn.TenKhachHang,
     rtchdn.DmKhachHangREF
     ----------------------------------UPDATE DL-----------------------------
     UPDATE rptThucChay_DoiBan_TheoKhachHang_Quy
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
     SoLuongNoiBoPhatSinhCuoiKy += td.SoLuongNoiBoPhatSinhTrongKy
     
     FROM rptThucChay_DoiBan_TheoKhachHang_Quy rtcdbt
     INNER JOIN @TeampData td ON
     td.PhongBanREF = rtcdbt.PhongBanREF
     AND td.BoPhanREF = rtcdbt.BoPhanREF
     AND td.NhomREF = rtcdbt.NhomREF 
     AND td.DmKhachHangREF = rtcdbt.DmKhachHangREF
     AND td.Quy = rtcdbt.Quy
     AND td.Nam = rtcdbt.Nam
     ---------
      UPDATE @TeampData
     SET
     TrangThai = 1
     FROM rptThucChay_DoiBan_TheoKhachHang_Quy rtcdbt
     INNER JOIN @TeampData td ON
     td.PhongBanREF = rtcdbt.PhongBanREF
     AND td.BoPhanREF = rtcdbt.BoPhanREF
     AND td.NhomREF = rtcdbt.NhomREF 
     AND td.DmKhachHangREF = rtcdbt.DmKhachHangREF
     AND td.Quy = rtcdbt.Quy
     AND td.Nam = rtcdbt.Nam
     --------------------------------insert dl-------------------------------------
     INSERT INTO rptThucChay_DoiBan_TheoKhachHang_Quy
				SELECT 
				
				@NgayThucHien,
				
				td.Quy,
				td.Nam,
				td.TenKhachHang,
				td.DmKhachHangREF,
				td.TenPhongBan,
				td.PhongBanREF,
				td.TenBoPhan,
				td.BoPhanREF,
				td.TenNhom,
				td.NhomREF,
				'',
				[dbo].[fn_GetDauKy_Of_Quy_DoiBanTheoKhachHang]
				(
				  td.DmKhachHangREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,		
			      @NgayThucHien,
			      1,0
				) ThucChayPhatSinhDauKy,
	            td.ThucChayPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Quy_DoiBanTheoKhachHang]
				(
				 td.DmKhachHangREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,		
			      @NgayThucHien,
			      1,0
				)
	            + td.ThucChayPhatSinhTrongKy
	            ) ThucChayPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Quy_DoiBanTheoKhachHang]
				(
				td.DmKhachHangREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,		
			      @NgayThucHien,
			      2,0
				) KhuyenMaiPhatSinhDauKy,
	            td.KhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Quy_DoiBanTheoKhachHang]
				(	
				 td.DmKhachHangREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,		
			      @NgayThucHien,
			      2,0
				)+ td.KhuyenMaiPhatSinhTrongKy
	            ) KhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Quy_DoiBanTheoKhachHang]
				(	
				 td.DmKhachHangREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,		
			      @NgayThucHien,
			      3,0
				) NoiBoPhatSinhDauKy,
	            td.NoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Quy_DoiBanTheoKhachHang]
				(	
				  td.DmKhachHangREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,		
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
	           [dbo].[fn_GetDauKy_Of_Quy_DoiBanTheoKhachHang]
				(
				  td.DmKhachHangREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,		
			      @NgayThucHien,
			      1,1
				) SoLuongPhatSinhDauKy,
	            td.SoLuongPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Quy_DoiBanTheoKhachHang]
				(
				  td.DmKhachHangREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,		
			      @NgayThucHien,
			      1,1
				)
	            + td.SoLuongPhatSinhTrongKy
	            ) SoLuongPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Quy_DoiBanTheoKhachHang]
				(
				 td.DmKhachHangREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,		
			      @NgayThucHien,
			      2,1
				) SoLuongKhuyenMaiPhatSinhDauKy,
	            td.SoLuongKhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Quy_DoiBanTheoKhachHang]
				(	
				 td.DmKhachHangREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,		
			      @NgayThucHien,
			      2,1
				)+ td.SoLuongKhuyenMaiPhatSinhTrongKy
	            ) SoLuongKhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Quy_DoiBanTheoKhachHang]
				(	
				  td.DmKhachHangREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,		
			      @NgayThucHien,
			      3,1
				) SoLuongNoiBoPhatSinhDauKy,
	            td.SoLuongNoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Quy_DoiBanTheoKhachHang]
				(	
				 td.DmKhachHangREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,		
			      @NgayThucHien,
			      3,1
				) + td.SoLuongNoiBoPhatSinhTrongKy
	            ) SoLuongNoiBoPhatSinhCuoiKy
				FROM @TeampData td WHERE td.TrangThai <>1
END

```
