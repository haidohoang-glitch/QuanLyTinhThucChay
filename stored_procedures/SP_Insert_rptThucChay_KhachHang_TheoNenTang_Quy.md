# Stored Procedure: `Insert_rptThucChay_KhachHang_TheoNenTang_Quy`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-07 12:18:40.830000
- **Ngày sửa cuối**: 2015-03-07 12:18:40.830000

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
CREATE PROCEDURE [dbo].[Insert_rptThucChay_KhachHang_TheoNenTang_Quy]
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
			TenLoaiNenTang NVARCHAR(200),
			DmLoaiNenTangREF INT,
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
	  -------------du lieu phat sinh -----------------
	  INSERT INTO @TeampData
	  SELECT
	  rtchdn.TenKhachHang,
	  rtchdn.DmKhachHangREF,
	  rtchdn.TenHinhThucKhachHang,
	  rtchdn.DmHinhThucKhachHangREF,
	  rtchdn.TenLoaiNenTang,
	  rtchdn.DmLoaiNenTangREF,
	  SUM(rtchdn.ThucChayPhatSinhTrongKy),
	  SUM(rtchdn.KhuyenMaiPhatSinhTrongKy),
	  SUM(rtchdn.NoiBoPhatSinhTrongKy),
	  SUM(rtchdn.SoLuongPhatSinhTrongKy),
	  SUM(rtchdn.SoLuongKhuyenMaiPhatSinhTrongKy),
	  SUM(rtchdn.SoLuongNoiBoPhatSinhTrongKy),
	  DATEPART(QQ,@NgayThucHien),
	  YEAR(@NgayThucHien),
	  0
	  FROM DoanhSoThucChayHopDongTheoThoiGian rtchdn
	  WHERE 1=1 
	  AND rtchdn.NgayThucHien = @NgayThucHien
	  GROUP BY 
	  rtchdn.TenKhachHang,
	  rtchdn.DmKhachHangREF,
	  rtchdn.TenHinhThucKhachHang,
	  rtchdn.DmHinhThucKhachHangREF,
	  rtchdn.TenLoaiNenTang,
	  rtchdn.DmLoaiNenTangREF
	  ------------------------------------UPDATE dl------------------------
	  UPDATE  rptThucChay_KhachHang_TheoNenTang_Quy 
		SET rptThucChay_KhachHang_TheoNenTang_Quy.NgayThucHien = @NgayThucHien,
		    rptThucChay_KhachHang_TheoNenTang_Quy.ThucChayPhatSinhTrongKy += td.ThucChayPhatSinhTrongKy,
		    rptThucChay_KhachHang_TheoNenTang_Quy.ThucChayPhatSinhCuoiKy += td.ThucChayPhatSinhTrongKy,
		    rptThucChay_KhachHang_TheoNenTang_Quy.KhuyenMaiPhatSinhTrongKy += td.KhuyenMaiPhatSinhTrongKy,
		    rptThucChay_KhachHang_TheoNenTang_Quy.KhuyenMaiPhatSinhCuoiKy += td.KhuyenMaiPhatSinhTrongKy,
		    rptThucChay_KhachHang_TheoNenTang_Quy.NoiBoPhatSinhTrongKy += td.NoiBoPhatSinhTrongKy,
		    rptThucChay_KhachHang_TheoNenTang_Quy.NoiBoPhatSinhCuoiKy += td.NoiBoPhatSinhTrongKy,
		    SoLuongPhatSinhTrongKy += td.SoLuongPhatSinhTrongKy,
	        SoLuongPhatSinhCuoiKy += td.SoLuongPhatSinhTrongKy,
			SoLuongKhuyenMaiPhatSinhTrongKy += td.SoLuongKhuyenMaiPhatSinhTrongKy,
			SoLuongKhuyenMaiPhatSinhCuoiKy += td.SoLuongKhuyenMaiPhatSinhTrongKy,
			SoLuongNoiBoPhatSinhTrongKy +=td.SoLuongNoiBoPhatSinhTrongKy,
			SoLuongNoiBoPhatSinhCuoiKy += td.SoLuongNoiBoPhatSinhTrongKy   
		FROM rptThucChay_KhachHang_TheoNenTang_Quy rtchdt
		INNER JOIN @TeampData td
		ON td.DmKhachHangREF = rtchdt.DmKhachHangREF
		AND td.DmHinhThucKhachHangREF = rtchdt.DmHinhThucKhachHangREF
		AND td.DmLoaiNenTangREF = rtchdt.DmLoaiNenTangREF
		AND td.Quy = rtchdt.Quy
		AND td.Nam = rtchdt.Nam
		
		 UPDATE  @TeampData 
		SET TrangThai = 1
		FROM rptThucChay_KhachHang_TheoNenTang_Quy rtchdt
		INNER JOIN @TeampData td
		ON td.DmKhachHangREF = rtchdt.DmKhachHangREF
		AND td.DmHinhThucKhachHangREF = rtchdt.DmHinhThucKhachHangREF
		AND td.DmLoaiNenTangREF = rtchdt.DmLoaiNenTangREF
		AND td.Quy = rtchdt.Quy
		AND td.Nam = rtchdt.Nam
		----------------------------------INSERT dl------------------------------------
		INSERT INTO rptThucChay_KhachHang_TheoNenTang_Quy
				SELECT 
				@NgayThucHien,
				td.Quy,
				td.Nam,
				td.TenKhachHang,
	            td.DmKhachHangREF,
	            td.TenHinhThucKhachHang,
	            td.DmHinhThucKhachHangREF,
	            td.TenLoaiNenTang,
	            td.DmLoaiNenTangREF,
	            '',
				[dbo].[fn_GetDauKy_Of_Quy_KhachHangTheoLoaiNenTang]
				(
				  td.DmKhachHangREF,	
				  td.DmHinhThucKhachHangREF	,
				  td.DmLoaiNenTangREF,
			      @NgayThucHien,
			      1,0
				) ThucChayPhatSinhDauKy,
	            td.ThucChayPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Quy_KhachHangTheoLoaiNenTang]
				(
				   td.DmKhachHangREF,	
				  td.DmHinhThucKhachHangREF	,
				  td.DmLoaiNenTangREF,
			      @NgayThucHien,
			      1,0
				)
	            +  td.ThucChayPhatSinhTrongKy
	            ) ThucChayPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Quy_KhachHangTheoLoaiNenTang]
				(
				   td.DmKhachHangREF,	
				  td.DmHinhThucKhachHangREF	,
				  td.DmLoaiNenTangREF,
			      @NgayThucHien,
			      2,0
				) KhuyenMaiPhatSinhDauKy,
	            td.KhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Quy_KhachHangTheoLoaiNenTang]
				(	
				   td.DmKhachHangREF,	
				  td.DmHinhThucKhachHangREF	,
				  td.DmLoaiNenTangREF,
			      @NgayThucHien,
			      2,0
				)+  td.KhuyenMaiPhatSinhTrongKy
	            ) KhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Quy_KhachHangTheoLoaiNenTang]
				(	
				  td.DmKhachHangREF,	
				  td.DmHinhThucKhachHangREF	,
				  td.DmLoaiNenTangREF,
			      @NgayThucHien,
			      3,0
				) NoiBoPhatSinhDauKy,
	            td.NoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Quy_KhachHangTheoLoaiNenTang]
				(	
				    td.DmKhachHangREF,	
				  td.DmHinhThucKhachHangREF	,
				  td.DmLoaiNenTangREF,
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
	             [dbo].[fn_GetDauKy_Of_Quy_KhachHangTheoLoaiNenTang]
				(
				 td.DmKhachHangREF,	
				  td.DmHinhThucKhachHangREF	,
				  td.DmLoaiNenTangREF,
			      @NgayThucHien,
			      1,1
				) ThucChayPhatSinhDauKy,
	            td.ThucChayPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Quy_KhachHangTheoLoaiNenTang]
				(
					td.DmKhachHangREF,	
				  td.DmHinhThucKhachHangREF	,
				  td.DmLoaiNenTangREF,
			      @NgayThucHien,
			      1,1
				)
	            +  td.ThucChayPhatSinhTrongKy
	            ) ThucChayPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Quy_KhachHangTheoLoaiNenTang]
				(
				   td.DmKhachHangREF,	
				  td.DmHinhThucKhachHangREF	,
				  td.DmLoaiNenTangREF,
			      @NgayThucHien,
			      2,1
				) KhuyenMaiPhatSinhDauKy,
	            td.KhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Quy_KhachHangTheoLoaiNenTang]
				(	
				   td.DmKhachHangREF,	
				  td.DmHinhThucKhachHangREF	,
				  td.DmLoaiNenTangREF,
			      @NgayThucHien,
			      2,1
				)+  td.KhuyenMaiPhatSinhTrongKy
	            ) KhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Quy_KhachHangTheoLoaiNenTang]
				(	
				   td.DmKhachHangREF,	
				  td.DmHinhThucKhachHangREF	,
				  td.DmLoaiNenTangREF,
			      @NgayThucHien,
			      3,1
				) NoiBoPhatSinhDauKy,
	            td.NoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Quy_KhachHangTheoLoaiNenTang]
				(	
				   td.DmKhachHangREF,	
				  td.DmHinhThucKhachHangREF	,
				  td.DmLoaiNenTangREF,
			      @NgayThucHien,
			      3,1
				) + td.NoiBoPhatSinhTrongKy
	            ) NoiBoPhatSinhCuoiKy
			 FROM  @TeampData td
				WHERE 1=1 AND td.TrangThai <>1
		
END

```
