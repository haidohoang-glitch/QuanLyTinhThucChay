# Stored Procedure: `Insert_DoanhSoXuatHoaDonNganhHangCore_PhatSinhThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-12 10:46:56.997000
- **Ngày sửa cuối**: 2015-06-12 10:46:56.997000

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
CREATE PROCEDURE [dbo].[Insert_DoanhSoXuatHoaDonNganhHangCore_PhatSinhThayDoi]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME,
	@HopDongID INT
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
    DECLARE @NgayGhiAmGanNhat DATETIME
      IF (SELECT COUNT(*) FROM DoanhSoXuatHoaDonNganhHangCore WHERE HopDongID = @HopDongID AND (ThucThuPhatSinhTrongKy<0 OR NoiBoPhatSinhTrongKy < 0)) > 0
		BEGIN
			set @NgayGhiAmGanNhat = (SELECT MAX(NgayThucHien) FROM DoanhSoXuatHoaDonNganhHangCore WHERE HopDongID = @HopDongID AND (ThucThuPhatSinhTrongKy<0 OR NoiBoPhatSinhTrongKy < 0))
		END
	ELSE set @NgayGhiAmGanNhat = '2000-01-01'
	IF(Convert(date,@NgayGhiAmGanNhat) = '2000-01-01')
	begin
    INSERT INTO DoanhSoXuatHoaDonNganhHangCore
  
	SELECT 
      @NgayThucHien
      ,[TenNganhHang]
      ,[DmNganhHangREF]
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
      ,[DmListNganhHangREF]
      ,[DmMaHopDongREF]
  FROM [dbo].[DoanhSoXuatHoaDonNganhHangCore] WHERE HopDongID = @HopDongID
  AND TypeRecordStatus IN (0,1)
  END 
  ELSE
  	BEGIN
  		 INSERT INTO DoanhSoXuatHoaDonNganhHangCore
  
	SELECT 
      @NgayThucHien
      ,[TenNganhHang]
      ,[DmNganhHangREF]
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
      ,[DmListNganhHangREF]
      ,[DmMaHopDongREF]
  FROM [dbo].[DoanhSoXuatHoaDonNganhHangCore] WHERE HopDongID = @HopDongID
  AND TypeRecordStatus IN (3,1) AND NgayThucHien >= @NgayGhiAmGanNhat
 END
END

```
