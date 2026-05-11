# Stored Procedure: `Insert_rptThucChay_HinhThucQuanCao_Thang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-07 12:18:32.720000
- **Ngày sửa cuối**: 2015-03-07 12:18:32.720000

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
CREATE PROCEDURE [dbo].[Insert_rptThucChay_HinhThucQuanCao_Thang]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	DECLARE @TeampData TABLE 
	   (
			TenHinhThucQuangCao NVARCHAR(200),
			DmHinhThucQuangCaoREF INT,
			ThucChayPhatSinhTrongKy FLOAT,
			KhuyenMaiPhatSinhTrongKy FLOAT,
			NoiBoPhatSinhTrongKy FLOAT,
			SoLuongPhatSinhTrongKy FLOAT,
			SoLuongKhuyenMaiPhatSinhTrongKy FLOAT,
			SoLuongNoiBoPhatSinhTrongKy FLOAT,
			Thang INT,
			Nam INT,
			TrangThai INT 
		)
    -- Insert statements for procedure here
	INSERT INTO @TeampData
	SELECT
	rtchdn.TenHinhThucKhachHang,
	rtchdn.DmHinhThucKhachHangREF,
	SUM(rtchdn.ThucChayPhatSinhTrongKy),
	SUM(rtchdn.KhuyenMaiPhatSinhTrongKy),
	SUM(rtchdn.NoiBoPhatSinhTrongKy),
	SUM(rtchdn.SoLuongPhatSinhTrongKy),
	SUM(rtchdn.SoLuongKhuyenMaiPhatSinhTrongKy),
	SUM(rtchdn.SoLuongNoiBoPhatSinhTrongKy),
	MONTH(@NgayThucHien),
	YEAR(@NgayThucHien),
	0
	FROM DoanhSoThucChayHopDongTheoThoiGian rtchdn
	WHERE 1=1
	AND rtchdn.NgayThucHien = @NgayThucHien
	GROUP BY
	rtchdn.TenHinhThucKhachHang,
	rtchdn.DmHinhThucKhachHangREF
	-------------------------------------UPDATE DL--------------------------------
	UPDATE rptThucChay_HinhThucQuangCao_Thang
	SET NgayThucHien = @NgayThucHien,
	ThucChayPhatSinhTrongKy += td.ThucChayPhatSinhTrongKy,
	ThucChayPhatSinhCuoiKy += td.ThucChayPhatSinhTrongKy,
	KhuyenMaiPhatSinhTrongKy += td.KhuyenMaiPhatSinhTrongKy,
	KhuyenMaiPhatSinhCuoiKy += td.KhuyenMaiPhatSinhTrongKy,
	NoiBoPhatSinhTrongKy +=td.NoiBoPhatSinhTrongKy,
	NoiBoPhatSinhCuoiKy += td.NoiBoPhatSinhTrongKy,
	SoLuongPhatSinhTrongKy += td.SoLuongPhatSinhTrongKy,
	SoLuongPhatSinhCuoiKy += td.SoLuongPhatSinhTrongKy,
	SoLuongKhuyenMaiPhatSinhTrongKy += td.SoLuongKhuyenMaiPhatSinhTrongKy,
	SoLuongKhuyenMaiPhatSinhCuoiKy += td.SoLuongKhuyenMaiPhatSinhTrongKy,
	SoLuongNoiBoPhatSinhTrongKy +=td.SoLuongNoiBoPhatSinhTrongKy,
	SoLuongNoiBoPhatSinhCuoiKy += td.SoLuongNoiBoPhatSinhTrongKy     
	FROM rptThucChay_HinhThucQuangCao_Thang rtchtqct
	INNER JOIN @TeampData td on
	td.DmHinhThucQuangCaoREF = rtchtqct.DmHinhThucQuangCao
	AND td.Thang = rtchtqct.Thang
	AND td.Nam = rtchtqct.Nam
	--------------
	UPDATE @TeampData
	SET TrangThai = 1 
	FROM rptThucChay_HinhThucQuangCao_Thang rtchtqct
	INNER JOIN @TeampData td on
	td.DmHinhThucQuangCaoREF = rtchtqct.DmHinhThucQuangCao
	AND td.Thang = rtchtqct.Thang
	AND td.Nam = rtchtqct.Nam
	-------------------------------------INSERT DL--------------------------------------
	INSERT INTO rptThucChay_HinhThucQuangCao_Thang
				SELECT 
				@NgayThucHien,
				td.Thang,
				td.Nam,
				td.TenHinhThucQuangCao,
				td.DmHinhThucQuangCaoREF,
				[dbo].[fn_GetDauKy_Of_Thang_HinhThucQuangCao]
				(
				  td.DmHinhThucQuangCaoREF,		
			      @NgayThucHien,
			      1,0
				) ThucChayPhatSinhDauKy,
	            td.ThucChayPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Thang_HinhThucQuangCao]
				(
				  td.DmHinhThucQuangCaoREF,		
			      @NgayThucHien,
			      1,0
				)
	            + td.ThucChayPhatSinhTrongKy
	            ) ThucChayPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Thang_HinhThucQuangCao]
				(
				   td.DmHinhThucQuangCaoREF,		
			      @NgayThucHien,
			      2,0
				) KhuyenMaiPhatSinhDauKy,
	            td.KhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Thang_HinhThucQuangCao]
				(	
				  td.DmHinhThucQuangCaoREF,		
			      @NgayThucHien,
			      2,0
				)+ td.KhuyenMaiPhatSinhTrongKy
	            ) KhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Thang_HinhThucQuangCao]
				(	
				  td.DmHinhThucQuangCaoREF,		
			      @NgayThucHien,
			      3,0
				) NoiBoPhatSinhDauKy,
	            td.NoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Thang_HinhThucQuangCao]
				(	
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
	            [dbo].[fn_GetDauKy_Of_Thang_HinhThucQuangCao]
				(
				  td.DmHinhThucQuangCaoREF,		
			      @NgayThucHien,
			      1,1
				) SoLuongPhatSinhDauKy,
	            td.SoLuongPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Thang_HinhThucQuangCao]
				(
				  td.DmHinhThucQuangCaoREF,		
			      @NgayThucHien,
			      1,1
				)
	            + td.SoLuongPhatSinhTrongKy
	            ) SoLuongPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Thang_HinhThucQuangCao]
				(
				   td.DmHinhThucQuangCaoREF,		
			      @NgayThucHien,
			      2,1
				) SoLuongKhuyenMaiPhatSinhDauKy,
	            td.SoLuongKhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Thang_HinhThucQuangCao]
				(	
				  td.DmHinhThucQuangCaoREF,		
			      @NgayThucHien,
			      2,1
				)+ td.SoLuongKhuyenMaiPhatSinhTrongKy
	            ) SoLuongKhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Thang_HinhThucQuangCao]
				(	
				  td.DmHinhThucQuangCaoREF,		
			      @NgayThucHien,
			      3,1
				) SoLuongNoiBoPhatSinhDauKy,
	            td.SoLuongNoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Thang_HinhThucQuangCao]
				(	
				   td.DmHinhThucQuangCaoREF,		
			      @NgayThucHien,
			      3,1
				) + td.SoLuongNoiBoPhatSinhTrongKy
	            ) SoLuongNoiBoPhatSinhCuoiKy
			 FROM  @TeampData td
				WHERE 1=1 
				AND td.TrangThai <>1
END

```
