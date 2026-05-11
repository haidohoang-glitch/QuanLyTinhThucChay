# Stored Procedure: `Insert_DoanhSoXuatHoaDonNhanHangCore_PhatSinhThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-12 10:46:54.877000
- **Ngày sửa cuối**: 2015-06-12 10:46:54.877000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[Insert_DoanhSoXuatHoaDonNhanHangCore_PhatSinhThayDoi]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@HopDongID INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;
     DECLARE @NgayGhiAmGanNhat DATETIME
      IF (SELECT COUNT(*) FROM DoanhSoXuatHoaDonNhanHangCore WHERE HopDongID = @HopDongID AND (ThucThuPhatSinhTrongKy<0 OR NoiBoPhatSinhTrongKy < 0)) > 0
		BEGIN
			set @NgayGhiAmGanNhat = (SELECT MAX(NgayThucHien) FROM DoanhSoXuatHoaDonNhanHangCore WHERE HopDongID = @HopDongID AND (ThucThuPhatSinhTrongKy<0 OR NoiBoPhatSinhTrongKy < 0))
		END
	ELSE set @NgayGhiAmGanNhat = '2000-01-01'
	IF(Convert(date,@NgayGhiAmGanNhat) = '2000-01-01')
	begin
    -- Insert statements for procedure here
    INSERT INTO DoanhSoXuatHoaDonNhanHangCore
  
	SELECT 
      @NgayThucHien
      ,[TenNhanHang]
      ,[DmNhanHangREF]
      ,[DsTenNganhHang]
      ,[DmListNganhHangREF]
      ,[HopDongID]
      ,[SoHopDong]
      ,[NgayDanhSo]
      ,[NgayKyHopDong]
      ,[TenNhanVien]
      ,[DmNhanVienREF]
      ,[TenPhongBan]
      ,[PhongBanREF]
      ,[TenBoPhan]
      ,[BoPhanREF]
      ,[TenNhom]
      ,[NhomREF]
      ,[TenKhachHang]
      ,[DmKhachHangREF]
      ,[HopDongChiTietREF]
      ,[DmSanPhamREF]
      ,[TenSanPham]
      ,[TenWebsite]
      ,[DmWebsiteREF]
      ,-[SoLuongPhatSinhDauKy]
      ,-[SoLuongPhatSinhTrongKy]
      ,-[SoLuongPhatSinhCuoiKy]
      ,-[SoLuongKMPhatSinhDauKy]
      ,-[SoLuongKMPhatSinhTrongKy]
      ,-[SoLuongKMPhatSinhCuoiKy]
      ,-[SoLuongNoiBoPhatSinhDauKy]
      ,-[SoLuongNoiBoPhatSinhTrongKy]
      ,-[SoLuongNoiBoPhatSInhCuoiKy]
      ,[DonViTinhREF]
      ,[DonViTinh]
      ,[TenDangNhap]
      ,[DonGia]
      ,[ChietKhau]
      ,-[ThucThuPhatSinhDauKy]
      ,-[ThucThuPhatSinhTrongKy]
      ,-[ThucThuPhatSinhCuoiKy]
      ,-[KhuyenMaiPhatSinhDauKy]
      ,-[KhuyenMaiPhatSinhTrongKy]
      ,-[KhuyenMaiPhatSinhCuoiKy]
      ,-[NoiBoPhatSinhDauKy]
      ,-[NoiBoPhatSinhTrongKy]
      ,-[NoiBoPhatSinhCuoiKy]
      ,[TrangThaiHopDong]
      ,[DienGiai]
      ,[CreatedBy]
      ,[CreatedAt]
      ,[LastModifiedBy]
      ,[lastModifiedAt]
      ,[RecordStatus]
      ,[DeletedStatus]
      ,[PrintStatus]
      ,2
      ,[SoHoaDon]
      ,[NgayXuatHoaDon]
      ,[ThongTinHoaDonREF]
      ,[DmListNhanHangREF]
      ,[DmMaHopDongREF]
  FROM [dbo].[DoanhSoXuatHoaDonNhanHangCore] WHERE HopDongID = @HopDongID
   AND TypeRecordStatus IN (0,1)
	END
	ELSE
		BEGIN
			   INSERT INTO DoanhSoXuatHoaDonNhanHangCore
  
	SELECT 
      @NgayThucHien
      ,[TenNhanHang]
      ,[DmNhanHangREF]
      ,[DsTenNganhHang]
      ,[DmListNganhHangREF]
      ,[HopDongID]
      ,[SoHopDong]
      ,[NgayDanhSo]
      ,[NgayKyHopDong]
      ,[TenNhanVien]
      ,[DmNhanVienREF]
      ,[TenPhongBan]
      ,[PhongBanREF]
      ,[TenBoPhan]
      ,[BoPhanREF]
      ,[TenNhom]
      ,[NhomREF]
      ,[TenKhachHang]
      ,[DmKhachHangREF]
      ,[HopDongChiTietREF]
      ,[DmSanPhamREF]
      ,[TenSanPham]
      ,[TenWebsite]
      ,[DmWebsiteREF]
      ,-[SoLuongPhatSinhDauKy]
      ,-[SoLuongPhatSinhTrongKy]
      ,-[SoLuongPhatSinhCuoiKy]
      ,-[SoLuongKMPhatSinhDauKy]
      ,-[SoLuongKMPhatSinhTrongKy]
      ,-[SoLuongKMPhatSinhCuoiKy]
      ,-[SoLuongNoiBoPhatSinhDauKy]
      ,-[SoLuongNoiBoPhatSinhTrongKy]
      ,-[SoLuongNoiBoPhatSInhCuoiKy]
      ,[DonViTinhREF]
      ,[DonViTinh]
      ,[TenDangNhap]
      ,[DonGia]
      ,[ChietKhau]
      ,-[ThucThuPhatSinhDauKy]
      ,-[ThucThuPhatSinhTrongKy]
      ,-[ThucThuPhatSinhCuoiKy]
      ,-[KhuyenMaiPhatSinhDauKy]
      ,-[KhuyenMaiPhatSinhTrongKy]
      ,-[KhuyenMaiPhatSinhCuoiKy]
      ,-[NoiBoPhatSinhDauKy]
      ,-[NoiBoPhatSinhTrongKy]
      ,-[NoiBoPhatSinhCuoiKy]
      ,-[TrangThaiHopDong]
      ,[DienGiai]
      ,[CreatedBy]
      ,[CreatedAt]
      ,[LastModifiedBy]
      ,[lastModifiedAt]
      ,[RecordStatus]
      ,[DeletedStatus]
      ,[PrintStatus]
      ,2
      ,[SoHoaDon]
      ,[NgayXuatHoaDon]
      ,[ThongTinHoaDonREF]
      ,[DmListNhanHangREF]
      ,[DmMaHopDongREF]
  FROM [dbo].[DoanhSoXuatHoaDonNhanHangCore] WHERE HopDongID = @HopDongID
   AND TypeRecordStatus IN (3,1) AND NgayThucHien >= @NgayGhiAmGanNhat
		END
END

```
