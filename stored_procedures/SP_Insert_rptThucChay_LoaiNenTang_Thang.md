# Stored Procedure: `Insert_rptThucChay_LoaiNenTang_Thang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-07 12:18:42.313000
- **Ngày sửa cuối**: 2015-03-07 12:18:42.313000

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
CREATE PROCEDURE [dbo].[Insert_rptThucChay_LoaiNenTang_Thang]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	DECLARE @TeampData TABLE 
	   (
			TenLoaiNenTang NVARCHAR(500),
			DmLoaiNenTangREF INT,
			ThucChayPhatSinhTrongKy FLOAT,
			KhuyenMaiPhatSinhTrongKy FLOAT,
			NoiBoPhatSinhTrongKy FLOAT,
			SoLuongPhatSinhTrongKy BIGINT,
			SoLuongKhuyenMaiPhatSinhTrongKy BIGINT,
			SoLuongNoiBoPhatSinhTrongKy BIGINT,
			Thang INT,
			Nam INT,
			TrangThai INT 
		)

	 -------Du lieu phat sinh---
	INSERT INTO @TeampData
	SELECT 
	rtchdn.TenLoaiNenTang,
	rtchdn.DmLoaiNenTangREF,
	SUM(rtchdn.ThucChayPhatSinhTrongKy),
	SUM(rtchdn.ThucChayPhatSinhTrongKy),
	SUM(rtchdn.ThucChayPhatSinhTrongKy),
	SUM(rtchdn.SoLuongPhatSinhTrongKy),
	SUM(rtchdn.SoLuongKhuyenMaiPhatSinhTrongKy),
	SUM(rtchdn.SoLuongNoiBoPhatSinhTrongKy),
	MONTH(@NgayThucHien),
	YEAR(@NgayThucHien),
	0
	FROM  DoanhSoThucChayHopDongTheoThoiGian rtchdn
	WHERE 1=1
	AND rtchdn.NgayThucHien = @NgayThucHien
	GROUP BY
	rtchdn.TenLoaiNenTang,
	rtchdn.DmLoaiNenTangREF
	-----------------------------------UPDATE DL----------------------------
	UPDATE rptThucChay_LoaiNenTang_Thang
	SET
	NgayThucHien = @NgayThucHien,
	ThucChayPhatSinhTrongKy += td.ThucChayPhatSinhTrongKy,
	ThucChayPhatSinhCuoiKy += td.ThucChayPhatSinhTrongKy,
	KhuyenMaiPhatSinhTrongKy +=td.KhuyenMaiPhatSinhTrongKy,
	KhuyenMaiPhatSinhCuoiKy +=td.KhuyenMaiPhatSinhTrongKy,
	NoiBoPhatSinhTrongKy += td.NoiBoPhatSinhTrongKy,
	NoiBoPhatSinhCuoiKy += td.NoiBoPhatSinhTrongKy,
	SoLuongPhatSinhTrongKy += td.SoLuongPhatSinhTrongKy,
	        SoLuongPhatSinhCuoiKy += td.SoLuongPhatSinhTrongKy,
			SoLuongKhuyenMaiPhatSinhTrongKy += td.SoLuongKhuyenMaiPhatSinhTrongKy,
			SoLuongKhuyenMaiPhatSinhCuoiKy += td.SoLuongKhuyenMaiPhatSinhTrongKy,
			SoLuongNoiBoPhatSinhTrongKy +=td.SoLuongNoiBoPhatSinhTrongKy,
			SoLuongNoiBoPhatSinhCuoiKy += td.SoLuongNoiBoPhatSinhTrongKy   
	FROM rptThucChay_LoaiNenTang_Thang rpttclntt
	INNER JOIN @TeampData td ON
	td.DmLoaiNenTangREF = rpttclntt.DmLoaiNenTang
	AND td.Thang = rpttclntt.Thang
	AND td.Nam = rpttclntt.Nam
	
	
	UPDATE @TeampData
	SET
	TrangThai = 1
	FROM rptThucChay_LoaiNenTang_Thang rpttclntt
	INNER JOIN @TeampData td ON
	td.DmLoaiNenTangREF = rpttclntt.DmLoaiNenTang
	AND td.Thang = rpttclntt.Thang
	AND td.Nam = rpttclntt.Nam
	-------------------------------INSERT DL-------------------------------------
	INSERT INTO rptThucChay_LoaiNenTang_Thang
				SELECT 
				@NgayThucHien,
				td.Thang,
				td.Nam,
			    td.TenLoaiNenTang,
			    td.DmLoaiNenTangREF,
				[dbo].[fn_GetDauKy_Of_Thang_LoaiNenTang]
				(
				  td.DmLoaiNenTangREF,	
			      @NgayThucHien,
			      1,0
				) ThucChayPhatSinhDauKy,
	            td.ThucChayPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Thang_LoaiNenTang]
				(
				 td.DmLoaiNenTangREF,			
			      @NgayThucHien,
			      1,0
				)
	            + td.ThucChayPhatSinhTrongKy
	            ) ThucChayPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Thang_LoaiNenTang]
				(
				  td.DmLoaiNenTangREF,			
			      @NgayThucHien,
			      2,0
				) KhuyenMaiPhatSinhDauKy,
	            td.KhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Thang_LoaiNenTang]
				(	
				 td.DmLoaiNenTangREF,	
			      @NgayThucHien,
			      2,0
				)+ td.KhuyenMaiPhatSinhTrongKy
	            ) KhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Thang_LoaiNenTang]
				(	
				  td.DmLoaiNenTangREF,			
			      @NgayThucHien,
			      3,0
				) NoiBoPhatSinhDauKy,
	            td.NoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Thang_LoaiNenTang]
				(	
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
	           [dbo].[fn_GetDauKy_Of_Thang_LoaiNenTang]
				(
				  td.DmLoaiNenTangREF,	
			      @NgayThucHien,
			      1,1
				) ThucChayPhatSinhDauKy,
	            td.ThucChayPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Thang_LoaiNenTang]
				(
				 td.DmLoaiNenTangREF,			
			      @NgayThucHien,
			      1,1
				)
	            + td.ThucChayPhatSinhTrongKy
	            ) ThucChayPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Thang_LoaiNenTang]
				(
				  td.DmLoaiNenTangREF,			
			      @NgayThucHien,
			      2,1
				) KhuyenMaiPhatSinhDauKy,
	            td.KhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Thang_LoaiNenTang]
				(	
				 td.DmLoaiNenTangREF,	
			      @NgayThucHien,
			      2,1
				)+ td.KhuyenMaiPhatSinhTrongKy
	            ) KhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Thang_LoaiNenTang]
				(	
				  td.DmLoaiNenTangREF,			
			      @NgayThucHien,
			      3,1
				) NoiBoPhatSinhDauKy,
	            td.NoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Thang_LoaiNenTang]
				(	
				  td.DmLoaiNenTangREF,			
			      @NgayThucHien,
			      3,1
				) + td.NoiBoPhatSinhTrongKy
	            ) NoiBoPhatSinhCuoiKy
			 FROM  @TeampData td
				WHERE 1=1 
				AND td.TrangThai <> 1
END

```
