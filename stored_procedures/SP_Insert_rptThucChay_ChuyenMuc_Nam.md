# Stored Procedure: `Insert_rptThucChay_ChuyenMuc_Nam`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-27 17:43:51.390000
- **Ngày sửa cuối**: 2015-03-27 17:43:51.390000

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
CREATE PROCEDURE [dbo].[Insert_rptThucChay_ChuyenMuc_Nam]
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
			TenChuyenMuc NVARCHAR(200),
			DmChuyenMucREF INT,
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

    -- Insert statements for procedure here
	 INSERT INTO @TeampData
	 SELECT 
	 dstchdc.TenNhanVien,
	 dstchdc.DmNhanVienREF,
	 dstchdc.TenPhongBan,
	 dstchdc.PhongBanREF,
	 dstchdc.TenBoPhan,
	 dstchdc.BoPhanREF,
	 dstchdc.TenNhom,
	 dstchdc.NhomREF,
	 dstchdc.TenDonViTinh,
	 dstchdc.UserName,
	 dstchdc.TenChuyenMuc,
	 dstchdc.DmChuyenMucREF,
	 SUM(isnull(dstchdc.ThucChayPhatSinhTrongKy,0)),
	 SUM(isnull(dstchdc.KhuyenMaiPhatSinhTrongKy,0)),
	 SUM(isnull(dstchdc.NoiBoPhatSinhTrongKy,0)),
	 SUM(isnull(dstchdc.SoLuongPhatSinhTrongKy,0)),
	 SUM(isnull(dstchdc.SoLuongKhuyenMaiPhatSinhTrongKy,0)),
	 SUM(isnull(dstchdc.SoLuongNoiBoPhatSinhTrongKy,0)),
	 SUM(isnull(dstchdc.ThucChayThayDoiTrongKy,0)),
	 SUM(isnull(dstchdc.NoiBoThayDoiTrongKy,0)),
	 SUM(isnull(dstchdc.KhuyenMaiThayDoiTrongKy,0)),
	 SUM(isnull(dstchdc.SoLuongThayDoiTrongKy,0)),
	 SUM(isnull(dstchdc.SoLuongNoiBoThayDoiTrongKy,0)),
	 SUM(isnull(dstchdc.SoLuongKhuyenMaiThayDoiTrongKy,0)),
	 YEAR(@NgayThucHien),
	 0
	 FROM DoanhSoThucChayHopDongTheoThoiGian dstchdc 
	 WHERE 1=1
	 AND dstchdc.NgayThucHien = @NgayThucHien
	 GROUP BY 
	 dstchdc.TenNhanVien,
	 dstchdc.DmNhanVienREF,
	 dstchdc.TenPhongBan,
	 dstchdc.PhongBanREF,
	 dstchdc.TenBoPhan,
	 dstchdc.BoPhanREF,
	 dstchdc.TenNhom,
	 dstchdc.NhomREF,
	 dstchdc.TenDonViTinh,
	 dstchdc.UserName,
	 dstchdc.TenChuyenMuc,
	 dstchdc.DmChuyenMucREF
	 ------------------UPDATE DL-----------------------------
	 UPDATE rptThucChay_ChuyenMuc_Nam
	 SET
	 	-- rptThucChay_ChuyenMuc_ThangID = ? -- this column value is auto-generated
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
	 FROM rptThucChay_ChuyenMuc_Nam rtccmt
	 INNER JOIN @TeampData td ON
	 td.DmNhanVienREF = rtccmt.DmNhanVienREF
	 AND td.PhongBanREF = rtccmt.PhongBanREF
	 AND td.BoPhanREF = rtccmt.BoPhanREF
	 AND td.NhomREF = rtccmt.NhomREF
	 AND td.TenDonViTinh = rtccmt.TenDonViTinh
	 AND td.UserName = rtccmt.UserName
	 AND td.DmChuyenMucREF = rtccmt.DmChuyenMucREF
	 AND td.TenChuyenMuc = rtccmt.TenChuyenMuc
	 AND td.Nam = rtccmt.Nam
	 
	  UPDATE @TeampData
	 SET
	 	-- rptThucChay_ChuyenMuc_ThangID = ? -- this column value is auto-generated
	 TrangThai = 1
	 FROM rptThucChay_ChuyenMuc_Nam rtccmt
	 INNER JOIN @TeampData td ON
	  td.DmNhanVienREF = rtccmt.DmNhanVienREF
	 AND td.PhongBanREF = rtccmt.PhongBanREF
	 AND td.BoPhanREF = rtccmt.BoPhanREF
	 AND td.NhomREF = rtccmt.NhomREF
	 AND td.TenDonViTinh = rtccmt.TenDonViTinh
	 AND td.UserName = rtccmt.UserName
	 AND td.DmChuyenMucREF = rtccmt.DmChuyenMucREF
	 AND td.TenChuyenMuc = rtccmt.TenChuyenMuc
	 AND td.Nam = rtccmt.Nam 
	 ------------------------InsertDL----------------------------------------
	 INSERT INTO rptThucChay_ChuyenMuc_Nam
	 SELECT 
	            @NgayThucHien,
				td.Nam,
				td.TenChuyenMuc,
				td.DmChuyenMucREF,
				[dbo].[fn_GetDauKy_Of_Ngay_ChuyenMuc] 
				(
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,
				  td.DmChuyenMucREF,		
			      @NgayThucHien,
			      1,0
				) ThucChayPhatSinhDauKy,
	            td.ThucChayPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_ChuyenMuc] 
				(
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,
				  td.DmChuyenMucREF,	
			      @NgayThucHien,
			      1,0
				)
	            +td.ThucChayPhatSinhTrongKy
	            ) ThucChayPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_ChuyenMuc] 
				(
					td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,
				  td.DmChuyenMucREF,	
			      @NgayThucHien,
			      2,0
				) KhuyenMaiPhatSinhDauKy,
	            td.KhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_ChuyenMuc] 
				(
					td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,	
				  td.DmChuyenMucREF,
			      @NgayThucHien,
			      2,0
				)+ td.KhuyenMaiPhatSinhTrongKy
	            ) KhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_ChuyenMuc] 
				(
					td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,	
				  td.DmChuyenMucREF,
			      @NgayThucHien,
			      3,0
				) NoiBoPhatSinhDauKy,
	            td.NoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Ngay_ChuyenMuc] 
				(
					td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,	
				  td.DmChuyenMucREF,
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
	           [dbo].[fn_GetDauKy_Of_Ngay_ChuyenMuc] 
				(
					td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,
				  td.DmChuyenMucREF,		
			      @NgayThucHien,
			      1,1
				) SoLuongPhatSinhDauKy,
	            td.SoLuongPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_ChuyenMuc] 
				(
					td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,
				  td.DmChuyenMucREF,	
			      @NgayThucHien,
			      1,1
				)
	            +td.SoLuongPhatSinhTrongKy
	            ) SoLuongPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_ChuyenMuc] 
				(
					td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,
				  td.DmChuyenMucREF,	
			      @NgayThucHien,
			      2,1
				) SoLuongKhuyenMaiPhatSinhDauKy,
	            td.SoLuongKhuyenMaiPhatSinhTrongKy,
	            ([dbo].[fn_GetDauKy_Of_Ngay_ChuyenMuc] 
				(
					td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,	
				  td.DmChuyenMucREF,
			      @NgayThucHien,
			      2,1
				)+ td.SoLuongKhuyenMaiPhatSinhTrongKy
	            ) SoLuongKhuyenMaiPhatSinhCuoiKy,
	            [dbo].[fn_GetDauKy_Of_Ngay_ChuyenMuc] 
				(	
					td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,
				  td.DmChuyenMucREF,
			      @NgayThucHien,
			      3,1
				) SoLuongNoiBoPhatSinhDauKy,
	            td.SoLuongNoiBoPhatSinhTrongKy,
	            (
	            	[dbo].[fn_GetDauKy_Of_Ngay_ChuyenMuc] 
				(
				  td.DmNhanVienREF,
				  td.PhongBanREF,
				  td.BoPhanREF,
				  td.NhomREF,
				  td.TenDonViTinh,
				  td.UserName,	
				  td.DmChuyenMucREF,
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
	 FROM @TeampData td 
	 WHERE td.TrangThai <>1

END

```
