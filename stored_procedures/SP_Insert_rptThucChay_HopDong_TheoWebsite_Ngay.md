# Stored Procedure: `Insert_rptThucChay_HopDong_TheoWebsite_Ngay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-27 17:43:56.560000
- **Ngày sửa cuối**: 2015-03-27 17:43:56.560000

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
CREATE PROCEDURE [dbo].[Insert_rptThucChay_HopDong_TheoWebsite_Ngay] 
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
			 INSERT INTO rptThucChay_HopDong_TheoWebsite_Ngay
			 SELECT 
				dstchdc.NgayThucHien,
				dstchdc.HopDongID,
				dstchdc.SoHopDong,
				dstchdc.TenNhanVien,
				dstchdc.DmNhanVienREF,
				dstchdc.TenPhongBan,
				dstchdc.PhongBanREF,
				dstchdc.TenBoPhan,
				dstchdc.BoPhanREF,
				dstchdc.TenNhom,
				dstchdc.NhomREF,
				dstchdc.TenKhachHang,
				dstchdc.DmKhachHangREF,
				'' as LoaiKhachHang,
				dstchdc.DmWebsiteREF,
				dstchdc.TenWebsite,
				'' as DienGiai,
			   [dbo].[fn_GetDauKy_Of_Ngay_HopDongTheoWebsite] 
				(
                  dstchdc.HopDongID,
                  dstchdc.DmNhanVienREF,
                  dstchdc.PhongBanREF,
                  dstchdc.BoPhanREF,
                  dstchdc.NhomREF,
                  dstchdc.DmKhachHangREF,
                  '',
                  dstchdc.DmWebsiteREF,
			      @NgayThucHien,
			      1,0
			      ,
			      dstchdc.TenDonViTinh,
			      dstchdc.Username
				) ThucChayPhatSinhDauKy,
	           SUM(dstchdc.ThucChayPhatSinhTrongKy)ThucChayPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_HopDongTheoWebsite] 
				(
				   dstchdc.HopDongID,
                  dstchdc.DmNhanVienREF,
                  dstchdc.PhongBanREF,
                  dstchdc.BoPhanREF,
                  dstchdc.NhomREF,
                  dstchdc.DmKhachHangREF,
                  '',
                  dstchdc.DmWebsiteREF,
			      @NgayThucHien,
			      1,0
			      ,
			      dstchdc.TenDonViTinh,
			      dstchdc.Username
				)+ SUM(dstchdc.ThucChayPhatSinhTrongKy)
				AS ThucChayPhatSinhCuoiKy,
				
	            [dbo].[fn_GetDauKy_Of_Ngay_HopDongTheoWebsite] 
				(
					 dstchdc.HopDongID,
                  dstchdc.DmNhanVienREF,
                  dstchdc.PhongBanREF,
                  dstchdc.BoPhanREF,
                  dstchdc.NhomREF,
                  dstchdc.DmKhachHangREF,
                  '',
                  dstchdc.DmWebsiteREF,	
			      @NgayThucHien,
			      2,0
			      ,
			      dstchdc.TenDonViTinh,
			      dstchdc.Username
				) KhuyenMaiPhatSinhDauKy,
	           SUM(dstchdc.KhuyenMaiPhatSinhTrongKy)KhuyenMaiPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_HopDongTheoWebsite] 
				(
					dstchdc.HopDongID,
                  dstchdc.DmNhanVienREF,
                  dstchdc.PhongBanREF,
                  dstchdc.BoPhanREF,
                  dstchdc.NhomREF,
                  dstchdc.DmKhachHangREF,
                  '',
                  dstchdc.DmWebsiteREF,		
			      @NgayThucHien,
			      2,0
			      ,
			      dstchdc.TenDonViTinh,
			      dstchdc.Username
				) + SUM(dstchdc.KhuyenMaiPhatSinhTrongKy)
	           AS KhuyenMaiPhatSinhCuoiKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_HopDongTheoWebsite] 
				(
				 dstchdc.HopDongID,
                  dstchdc.DmNhanVienREF,
                  dstchdc.PhongBanREF,
                  dstchdc.BoPhanREF,
                  dstchdc.NhomREF,
                  dstchdc.DmKhachHangREF,
                  '',
                  dstchdc.DmWebsiteREF,
			      @NgayThucHien,
			      3,0
			      ,
			      dstchdc.TenDonViTinh,
			      dstchdc.Username
				) AS NoiBoPhatSinhDauKy,
	           SUM(dstchdc.NoiBoPhatSinhTrongKy)NoiBoPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_HopDongTheoWebsite] 
				(
					 dstchdc.HopDongID,
                  dstchdc.DmNhanVienREF,
                  dstchdc.PhongBanREF,
                  dstchdc.BoPhanREF,
                  dstchdc.NhomREF,
                  dstchdc.DmKhachHangREF,
                  '',	
                  dstchdc.DmWebsiteREF,	
			      @NgayThucHien,
			      3,0
			      ,
			      dstchdc.TenDonViTinh,
			      dstchdc.Username
				) + SUM(dstchdc.NoiBoPhatSinhTrongKy)
				AS NoiBoPhatSinhCuoiKy,
	           'ASD' CreatedBy,
	           GETDATE() CreatedAt,
	           'ASD' LastModifiedBy,
	           GETDATE() LastModifiedAt,
	           0 DeletedStatus,
	           0 RecordStatus,
	           0 PrintStatus,
	            [dbo].[fn_GetDauKy_Of_Ngay_HopDongTheoWebsite] 
				(
					 dstchdc.HopDongID,
                  dstchdc.DmNhanVienREF,
                  dstchdc.PhongBanREF,
                  dstchdc.BoPhanREF,
                  dstchdc.NhomREF,
                  dstchdc.DmKhachHangREF,
                  '',	
                  dstchdc.DmWebsiteREF,
			      @NgayThucHien,
			      1,1
			      ,
			      dstchdc.TenDonViTinh,
			      dstchdc.Username
				) SoLuongPhatSinhDauKy,
	           SUM(dstchdc.SoLuongPhatSinhTrongKy)SoLuongPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_HopDongTheoWebsite] 
				(
					 dstchdc.HopDongID,
                  dstchdc.DmNhanVienREF,
                  dstchdc.PhongBanREF,
                  dstchdc.BoPhanREF,
                  dstchdc.NhomREF,
                  dstchdc.DmKhachHangREF,
                  '',
                  dstchdc.DmWebsiteREF,
			      @NgayThucHien,
			      1,1
			      ,
			      dstchdc.TenDonViTinh,
			      dstchdc.Username
				)+ SUM(dstchdc.SoLuongPhatSinhTrongKy)
				AS SoLuongPhatSinhCuoiKy,
				
	            [dbo].[fn_GetDauKy_Of_Ngay_HopDongTheoWebsite] 
				(
					dstchdc.HopDongID,
                  dstchdc.DmNhanVienREF,
                  dstchdc.PhongBanREF,
                  dstchdc.BoPhanREF,
                  dstchdc.NhomREF,
                  dstchdc.DmKhachHangREF,
                  '',
                  dstchdc.DmWebsiteREF,
			      @NgayThucHien,
			      2,1
			      ,
			      dstchdc.TenDonViTinh,
			      dstchdc.Username
				) SoLuongKhuyenMaiPhatSinhDauKy,
	           SUM(dstchdc.SoLuongKhuyenMaiPhatSinhTrongKy)SoLuongKhuyenMaiPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_HopDongTheoWebsite] 
				(
					dstchdc.HopDongID,
                  dstchdc.DmNhanVienREF,
                  dstchdc.PhongBanREF,
                  dstchdc.BoPhanREF,
                  dstchdc.NhomREF,
                  dstchdc.DmKhachHangREF,
                  '',
                  dstchdc.DmWebsiteREF,
			      @NgayThucHien,
			      2,1
			      ,
			      dstchdc.TenDonViTinh,
			      dstchdc.Username
				) + SUM(dstchdc.SoLuongKhuyenMaiPhatSinhTrongKy)
	           AS SoLuongKhuyenMaiPhatSinhCuoiKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_HopDongTheoWebsite] 
				(
					dstchdc.HopDongID,
                  dstchdc.DmNhanVienREF,
                  dstchdc.PhongBanREF,
                  dstchdc.BoPhanREF,
                  dstchdc.NhomREF,
                  dstchdc.DmKhachHangREF,
                  '',	
                  dstchdc.DmWebsiteREF,
			      @NgayThucHien,
			      3,1
			      ,
			      dstchdc.TenDonViTinh,
			      dstchdc.Username
				) AS SoLuongNoiBoPhatSinhDauKy,
	           SUM(dstchdc.SoLuongNoiBoPhatSinhTrongKy)NoiBoPhatSinhTrongKy,
	           [dbo].[fn_GetDauKy_Of_Ngay_HopDongTheoWebsite] 
				(
				  dstchdc.HopDongID,
                  dstchdc.DmNhanVienREF,
                  dstchdc.PhongBanREF,
                  dstchdc.BoPhanREF,
                  dstchdc.NhomREF,
                  dstchdc.DmKhachHangREF,
                  '',	
                  dstchdc.DmWebsiteREF,
			      @NgayThucHien,
			      3,1
			      ,
			      dstchdc.TenDonViTinh,
			      dstchdc.Username
				) + SUM(dstchdc.SoLuongNoiBoPhatSinhTrongKy)
				AS SoLuongNoiBoPhatSinhCuoiKy,
				dstchdc.TenDonViTinh,
				dstchdc.UserName,
				sum(dstchdc.ThucChayThayDoiTrongKy),
	            sum(dstchdc.NoiBoThayDoiTrongKy),
	            sum(dstchdc.KhuyenMaiThayDoiTrongKy),
	            sum(dstchdc.SoLuongThayDoiTrongKy),
	            sum(dstchdc.SoLuongNoiBoThayDoiTrongKy),
	            sum(dstchdc.SoLuongKhuyenMaiThayDoiTrongKy)
			 FROM   DoanhSoThucChayWebsiteTheoThoiGian dstchdc
			 WHERE dstchdc.NgayThucHien = @NgayThucHien
			 GROUP BY
			    dstchdc.NgayThucHien,
				dstchdc.HopDongID,
				dstchdc.SoHopDong,
				dstchdc.TenNhanVien,
				dstchdc.DmNhanVienREF,
				dstchdc.TenPhongBan,
				dstchdc.PhongBanREF,
				dstchdc.TenBoPhan,
				dstchdc.BoPhanREF,
				dstchdc.TenNhom,
				dstchdc.NhomREF,
				dstchdc.TenKhachHang,
				dstchdc.DmKhachHangREF,
				dstchdc.DmWebsiteREF,
				dstchdc.TenWebsite,
				dstchdc.TenDonViTinh,
				dstchdc.UserName
			SET @NgayThucHien = DATEADD(DAY, 1, @NgayThucHien)
		END
END

```
