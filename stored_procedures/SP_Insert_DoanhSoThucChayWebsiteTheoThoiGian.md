# Stored Procedure: `Insert_DoanhSoThucChayWebsiteTheoThoiGian`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-27 17:43:42.853000
- **Ngày sửa cuối**: 2015-03-27 17:43:42.853000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [dbo].[Insert_DoanhSoThucChayWebsiteTheoThoiGian] '2013-01-01','2013-01-31'
CREATE PROCEDURE [dbo].[Insert_DoanhSoThucChayWebsiteTheoThoiGian]
	-- Add the parameters for the stored procedure here
	@FromDate DATETIME,
	@ToDate DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	DELETE FROM DoanhSoThucChayWebsiteTheoThoiGian
	INSERT INTO DoanhSoThucChayWebsiteTheoThoiGian
	SELECT 
      [NgayThucHien]
      ,[DmSanPhamREF]
      ,[TenSanPham]
      ,[TenWebsite]
      ,[DmWebsiteREF]
      ,[DienGiai]
      ,[ThucChayPhatSinhDauKy]
      ,[ThucChayPhatSinhTrongKy]
      ,[ThucChayPhatSinhCuoiKy]
      ,[KhuyenMaiPhatSinhDauKy]
      ,[KhuyenMaiPhatSinhTrongKy]
      ,[KhuyenMaiPhatSinhCuoiKy]
      ,[NoiBoPhatSinhDauKy]
      ,[NoiBoPhatSinhTrongKy]
      ,[NoiBoPhatSinhCuoiKy]
      ,[SoLuongPhatSinhDauKy]
      ,[SoLuongPhatSinhTrongKy]
      ,[SoLuongPhatSinhCuoiKy]
      ,[SoLuongKhuyenMaiPhatSinhDauKy]
      ,[SoLuongKhuyenMaiPhatSinhTrongKy]
      ,[SoLuongKhuyenMaiPhatSinhCuoiKy]
      ,[SoLuongNoiBoPhatSinhDauKy]
      ,[SoLuongNoiBoPhatSinhTrongKy]
      ,[SoLuongNoiBoPhatSinhCuoiKy]
      ,[CreatedBy]
      ,[CreatedAt]
      ,[LastModifiedBy]
      ,[LastModifiedAt]
      ,[DeletedStatus]
      ,[RecordStatus]
      ,[PrintStatus]
      ,[TenNhanVien]
      ,[DmNhanVienREF]
      ,[TenPhongBan]
      ,[PhongBanREF]
      ,[TenBoPhan]
      ,[BoPhanREF]
      ,[TenNhom]
      ,[NhomREF]
      ,[TenHinhThucQuangCao]
      ,[DmHinhThucQuangCaoREF]
      ,[TenKhachHang]
      ,[DmKhachHangREF]
      ,[SoHopDong]
      ,[HopDongID]
      ,[TenViTriBanner]
      ,[DmViTriBannerREF]
      ,[TenDonViTinh]
      ,[UserName]
      ,[ThucChayThayDoiTrongKy]
      ,[NoiBoThayDoiTrongKy]
      ,[KhuyenMaiThayDoiTrongKy]
      ,[SoLuongThayDoiTrongKy]
      ,[SoLuongNoiBoThayDoiTrongKy]
      ,[SoLuongKhuyenMaiThayDoiTrongKy]
	FROM DoanhSoThucChayWebsiteCore dstchdc WHERE dstchdc.NgayThucHien BETWEEN @FromDate AND @ToDate
	
END

```
