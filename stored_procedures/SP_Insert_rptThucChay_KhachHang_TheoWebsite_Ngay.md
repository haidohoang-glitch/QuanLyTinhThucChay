# Stored Procedure: `Insert_rptThucChay_KhachHang_TheoWebsite_Ngay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-27 17:44:00.333000
- **Ngày sửa cuối**: 2015-03-27 17:44:00.333000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		Doannv
-- Create date: 03022014
-- Description:	<Description,,>
-- =============================================
--EXEC [dbo].[Insert_rptThucChay_HopDong_Ngay]  '2013-01-01','2013-01-31'
CREATE PROCEDURE [dbo].[Insert_rptThucChay_KhachHang_TheoWebsite_Ngay] 
	-- Add the parameters for the stored procedure here
    @FromDate DATETIME,
	@ToDate DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	DECLARE @NgayThucHien DATETIME
	SET @NgayThucHien = @FromDate
	DELETE 
	FROM   rptThucChay_HopDong_Ngay
	WHERE  1 = 1
	       AND NgayThucHien BETWEEN @FromDate AND @ToDate
	
	WHILE @NgayThucHien <= @ToDate
		BEGIN
			 INSERT INTO rptThucChay_KhachHang_TheoWebsite_Ngay
			 SELECT 
				dstchdc.NgayThucHien,
				dstchdc.TenKhachHang,
				dstchdc.DmKhachHangREF,
				'' as TenHinhThucKhachHang,
				0,
				dstchdc.TenWebsite,
				dstchdc.DmWebsiteREF,
				'' DienGiai,
			   [dbo].[fn_GetDauKy_Of_Ngay_KhachHangTheoWebsite] 
				(
					dstchdc.DmNhanVienREF,
					dstchdc.PhongBanREF,
					dstchdc.BoPhanREF,
					dstchdc.NhomREF,
					dstchdc.TenDonViTinh,
					dstchdc.Username,
                  dstchdc.DmKhachHangREF,
                  0,
                  dstchdc.DmWebsiteREF,
			      @NgayThucHien,
			      1,0
				) ThucChayPhatSinhDauKy,
	           SUM(dstchdc.ThucChayPhatSinhTrongKy)ThucChayPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_KhachHangTheoWebsite] 
				(
					dstchdc.DmNhanVienREF,
					dstchdc.PhongBanREF,
					dstchdc.BoPhanREF,
					dstchdc.NhomREF,
					dstchdc.TenDonViTinh,
					dstchdc.Username,
				  dstchdc.DmKhachHangREF,
                  0,
                  dstchdc.DmWebsiteREF,
			      @NgayThucHien,
			      1,0
				)+ SUM(dstchdc.ThucChayPhatSinhTrongKy)
				AS ThucChayPhatSinhCuoiKy,
				
	            [dbo].[fn_GetDauKy_Of_Ngay_KhachHangTheoWebsite] 
				(
					dstchdc.DmNhanVienREF,
					dstchdc.PhongBanREF,
					dstchdc.BoPhanREF,
					dstchdc.NhomREF,
					dstchdc.TenDonViTinh,
					dstchdc.Username,
				  dstchdc.DmKhachHangREF,
                  0,
                  dstchdc.DmWebsiteREF,
			      @NgayThucHien,
			      2,0
				) KhuyenMaiPhatSinhDauKy,
	           SUM(dstchdc.KhuyenMaiPhatSinhTrongKy)KhuyenMaiPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_KhachHangTheoWebsite] 
				(
					dstchdc.DmNhanVienREF,
					dstchdc.PhongBanREF,
					dstchdc.BoPhanREF,
					dstchdc.NhomREF,
					dstchdc.TenDonViTinh,
					dstchdc.Username,
					dstchdc.DmKhachHangREF,
                  0,
                  dstchdc.DmWebsiteREF,	
			      @NgayThucHien,
			      2,0
				) + SUM(dstchdc.KhuyenMaiPhatSinhTrongKy)
	           AS KhuyenMaiPhatSinhCuoiKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_KhachHangTheoWebsite] 
				(
					dstchdc.DmNhanVienREF,
					dstchdc.PhongBanREF,
					dstchdc.BoPhanREF,
					dstchdc.NhomREF,
					dstchdc.TenDonViTinh,
					dstchdc.Username,
				  dstchdc.DmKhachHangREF,
                  0,
                  dstchdc.DmWebsiteREF,
			      @NgayThucHien,
			      3,0
				) AS NoiBoPhatSinhDauKy,
	           SUM(dstchdc.NoiBoPhatSinhTrongKy)NoiBoPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_KhachHangTheoWebsite] 
				(
					dstchdc.DmNhanVienREF,
					dstchdc.PhongBanREF,
					dstchdc.BoPhanREF,
					dstchdc.NhomREF,
					dstchdc.TenDonViTinh,
					dstchdc.Username,
					dstchdc.DmKhachHangREF,
                  0,
                  dstchdc.DmWebsiteREF,
			      @NgayThucHien,
			      3,0
				) + SUM(dstchdc.NoiBoPhatSinhTrongKy)
				AS NoiBoPhatSinhCuoiKy,
	           'ASD' CreatedBy,
	           GETDATE() CreatedAt,
	           'ASD' LastModifiedBy,
	           GETDATE() LastModifiedAt,
	           0 DeletedStatus,
	           0 RecordStatus,
	           0 PrintStatus,
	          [dbo].[fn_GetDauKy_Of_Ngay_KhachHangTheoWebsite] 
				(
					dstchdc.DmNhanVienREF,
					dstchdc.PhongBanREF,
					dstchdc.BoPhanREF,
					dstchdc.NhomREF,
					dstchdc.TenDonViTinh,
					dstchdc.Username,

                  dstchdc.DmKhachHangREF,
                  0,
                  dstchdc.DmWebsiteREF,
			      @NgayThucHien,
			      1,1
				) SoLuongPhatSinhDauKy,
	           SUM(dstchdc.SoLuongPhatSinhTrongKy)SoLuongPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_KhachHangTheoWebsite] 
				(
					dstchdc.DmNhanVienREF,
					dstchdc.PhongBanREF,
					dstchdc.BoPhanREF,
					dstchdc.NhomREF,
					dstchdc.TenDonViTinh,
					dstchdc.Username,
					dstchdc.DmKhachHangREF,
                  0,
                  dstchdc.DmWebsiteREF,
			      @NgayThucHien,
			      1,1
				)+ SUM(dstchdc.SoLuongPhatSinhTrongKy)
				AS SoLuongPhatSinhCuoiKy,
				
	            [dbo].[fn_GetDauKy_Of_Ngay_KhachHangTheoWebsite] 
				(
					dstchdc.DmNhanVienREF,
					dstchdc.PhongBanREF,
					dstchdc.BoPhanREF,
					dstchdc.NhomREF,
					dstchdc.TenDonViTinh,
					dstchdc.Username,
					dstchdc.DmKhachHangREF,
                  0,
                  dstchdc.DmWebsiteREF,
			      @NgayThucHien,
			      2,1
				) SoLuongKhuyenMaiPhatSinhDauKy,
	           SUM(dstchdc.SoLuongKhuyenMaiPhatSinhTrongKy)SoLuongKhuyenMaiPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_KhachHangTheoWebsite] 
				(
					dstchdc.DmNhanVienREF,
					dstchdc.PhongBanREF,
					dstchdc.BoPhanREF,
					dstchdc.NhomREF,
					dstchdc.TenDonViTinh,
					dstchdc.Username,
					dstchdc.DmKhachHangREF,
                  0,
                  dstchdc.DmWebsiteREF,
			      @NgayThucHien,
			      2,1
				) + SUM(dstchdc.SoLuongKhuyenMaiPhatSinhTrongKy)
	           AS SoLuongKhuyenMaiPhatSinhCuoiKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_KhachHangTheoWebsite] 
				(
					dstchdc.DmNhanVienREF,
					dstchdc.PhongBanREF,
					dstchdc.BoPhanREF,
					dstchdc.NhomREF,
					dstchdc.TenDonViTinh,
					dstchdc.Username,
					dstchdc.DmKhachHangREF,
                  0,
                  dstchdc.DmWebsiteREF,
			      @NgayThucHien,
			      3,1
				) AS SoLuongNoiBoPhatSinhDauKy,
	           SUM(dstchdc.SoLuongNoiBoPhatSinhTrongKy)NoiBoPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_KhachHangTheoWebsite] 
				(
					dstchdc.DmNhanVienREF,
					dstchdc.PhongBanREF,
					dstchdc.BoPhanREF,
					dstchdc.NhomREF,
					dstchdc.TenDonViTinh,
					dstchdc.Username,
				  dstchdc.DmKhachHangREF,
                  0,
                  dstchdc.DmWebsiteREF,
			      @NgayThucHien,
			      3,1
				) + SUM(dstchdc.SoLuongNoiBoPhatSinhTrongKy)
				AS SoLuongNoiBoPhatSinhCuoiKy,
				 dstchdc.TenNhanVien,
	            dstchdc.DmNhanVienREF,
	            dstchdc.TenPhongBan,
	            dstchdc.PhongBanREF,
	            dstchdc.TenBoPhan,
	            dstchdc.BoPhanREF,
	            dstchdc.TenNhom,
	            dstchdc.NhomREF,
	            dstchdc.TenDonViTinh,
	            dstchdc.Username,
	            sum(dstchdc.ThucChayThayDoiTrongKy),
	            sum(dstchdc.NoiBoThayDoiTrongKy),
	            sum(dstchdc.KhuyenMaiThayDoiTrongKy),
	            sum(dstchdc.SoLuongThayDoiTrongKy),
	            sum(dstchdc.SoLuongNoiBoThayDoiTrongKy),
	            sum(dstchdc.SoLuongKhuyenMaiThayDoiTrongKy)
			 FROM   DoanhSoThucChayWebsiteTheoThoiGian dstchdc 
			
			
			 WHERE dstchdc.NgayThucHien = @NgayThucHien
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
	            dstchdc.Username,
			    dstchdc.NgayThucHien,
				dstchdc.TenKhachHang,
				dstchdc.DmKhachHangREF,
				dstchdc.TenWebsite,
				dstchdc.DmWebsiteREF
			SET @NgayThucHien = DATEADD(DAY, 1, @NgayThucHien)
		END
END

```
