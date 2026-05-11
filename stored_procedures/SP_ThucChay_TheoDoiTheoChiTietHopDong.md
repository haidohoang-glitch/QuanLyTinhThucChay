# Stored Procedure: `ThucChay_TheoDoiTheoChiTietHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-27 16:58:52.563000
- **Ngày sửa cuối**: 2014-11-19 12:16:58.957000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC ThucChay_TheoDoiTheoChiTietHopDong 'QC1080713'

CREATE PROCEDURE [dbo].[ThucChay_TheoDoiTheoChiTietHopDong] 
	
AS
BEGIN

DECLARE 
	@HopDongChiTietID int,
	@HopDongFK int,
	@NhanHang nvarchar(255) ,
	@DmNhomNganhREF int ,
	@TenNhomNganh nvarchar(50) ,
	@DmLoaiREF int ,
	@TenLoai nvarchar(50) ,
	@DmNhomWebsiteREF int ,
	@TenNhomWebsite nvarchar(100) ,
	@DmWebsiteREF int ,
	@TenWebsite nvarchar(100) ,
	@DmSanPhamREF int ,
	@TenSanPham nvarchar(100) ,
	@DmLoaiBannerREF int ,
	@TenLoaiBanner nvarchar(50) ,
	@DmChuyenMucREF int ,
	@TenChuyenMuc nvarchar(100) ,
	@DmViTriREF int ,
	@TenViTri nvarchar(50) ,
	@ThoiGian nvarchar(50) ,
	@SoLuong int ,
	@DonViTinh nvarchar(50) ,
	@DonGia float ,
	@ChietKhau float ,
	@GiamGia float ,
	@TiLeTuVan float ,
	@KhuyenMai nvarchar(50) ,
	@IsKhuyenMai int ,
	@ChiPhiTuVan float ,
	@ThanhTien float ,
	@GhiChu nvarchar(255) ,
	@DotChayHopDongChiTiet nvarchar(4000) ,
	@NgayDaChay nvarchar(4000) ,
	@SoLuongDaChay float ,
	@SoLuongChuaChay float ,
	@ThanhTienDaChay float ,
	@ThanhTienChuaChay float ,
	@CreatedBy nvarchar(50) ,
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(50) ,
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus INT,
	@ThucChayDenNgay datetime,
	@TrangThaiHopDongChiTietThucChay int 
	
DECLARE Record_Cursor CURSOR FOR 
	SELECT * FROM dbo.HopDongChiTiet A
	WHERE 
	A.LastModifiedAt >= (SELECT MAX(LastModifiedAt) FROM dbo.ThucChayTheoDoiHopDongChiTiet)
	ORDER BY A.LastModifiedAt

OPEN Record_Cursor

FETCH NEXT FROM Record_Cursor into 
      @HopDongChiTietID
      ,@HopDongFK
      ,@NhanHang
      ,@DmNhomNganhREF
      ,@TenNhomNganh
      ,@DmLoaiREF
      ,@TenLoai
      ,@DmNhomWebsiteREF
      ,@TenNhomWebsite
      ,@DmWebsiteREF
      ,@TenWebsite
      ,@DmSanPhamREF
      ,@TenSanPham
      ,@DmLoaiBannerREF
      ,@TenLoaiBanner
      ,@DmChuyenMucREF
      ,@TenChuyenMuc
      ,@DmViTriREF
      ,@TenViTri
      ,@ThoiGian
      ,@SoLuong
      ,@DonViTinh
      ,@DonGia
      ,@ChietKhau
      ,@GiamGia
      ,@TiLeTuVan
      ,@KhuyenMai
      ,@IsKhuyenMai
      ,@ChiPhiTuVan
      ,@ThanhTien
      ,@GhiChu
      ,@CreatedBy
      ,@CreatedAt
      ,@LastModifiedBy
      ,@LastModifiedAt
      ,@DeletedStatus
      ,@PrintStatus
      ,@RecordStatus

WHILE @@FETCH_STATUS = 0
BEGIN

SET @ThucChayDenNgay = (SELECT MAX(NgayThucHien) FROM dbo.ThucChayDaTinh WHERE HopDongChiTietREF=@HopDongChiTietID)

IF(EXISTS(SELECT * FROM ThucChayTheoDoiHopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID))
BEGIN
UPDATE [dbo].[ThucChayTheoDoiHopDongChiTiet]
   SET     
      [NhanHang] = @NhanHang
      ,[DmNhomNganhREF] = @DmNhomNganhREF
      ,[TenNhomNganh] = @TenNhomNganh
      ,[DmLoaiREF] = @DmLoaiREF
      ,[TenLoai] = @TenLoai
      ,[DmNhomWebsiteREF] = @DmNhomWebsiteREF
      ,[TenNhomWebsite] = @TenNhomWebsite
      ,[DmWebsiteREF] = @DmWebsiteREF
      ,[TenWebsite] = @TenWebsite
      ,[DmSanPhamREF] = @DmSanPhamREF
      ,[TenSanPham] = @TenSanPham
      ,[DmLoaiBannerREF] = @DmLoaiBannerREF
      ,[TenLoaiBanner] = @TenLoaiBanner
      ,[DmChuyenMucREF] = @DmChuyenMucREF
      ,[TenChuyenMuc] = @TenChuyenMuc
      ,[DmViTriREF] = @DmViTriREF
      ,[TenViTri] = @TenViTri
      ,[ThoiGian] = @ThoiGian
      ,[SoLuong] = @SoLuong
      ,[DonViTinh] = @DonViTinh
      ,[DonGia] = @DonGia
      ,[ChietKhau] = @ChietKhau
      ,[GiamGia] = @GiamGia
      ,[TiLeTuVan] = @TiLeTuVan
      ,[KhuyenMai] = @KhuyenMai
      ,[IsKhuyenMai] = @IsKhuyenMai
      ,[ChiPhiTuVan] = @ChiPhiTuVan
      ,[ThanhTien] = @ThanhTien
      ,[GhiChu] = @GhiChu
      ,[DotChayHopDongChiTiet] = dbo.GetDotChayHopDongChiTiet(@HopDongChiTietID)
      ,[NgayDaChay] = dbo.GetDotDaChayHopDongChiTiet(@HopDongChiTietID)
      ,[ThucChayDenNgay] = @ThucChayDenNgay
      ,[SoLuongDaChay] = dbo.ThucChay_GetSoLuongThucChayByHopDongChiTietID(@HopDongChiTietID)
      ,[SoLuongChuaChay] = dbo.ThucChay_GetSoLuongChuaChayTheoDonViTinh(@SoLuong,@DonViTinh,@HopDongChiTietID)
      ,[ThanhTienDaChay] = dbo.ThucChay_GetThanhTienThucChayByHopDongChiTietID(@HopDongChiTietID)
      ,[ThanhTienChuaChay] = dbo.ThucChay_GetThanhTienChuaChayByHopDongChiTietID(@HopDongChiTietID)
      ,[CreatedBy] = @CreatedBy
      ,[CreatedAt] = @CreatedAt
      ,[LastModifiedBy] = @LastModifiedBy
      ,[LastModifiedAt] = @LastModifiedAt
      ,[DeletedStatus] = @DeletedStatus
      ,[PrintStatus] = @PrintStatus
      ,[RecordStatus] = @RecordStatus
 WHERE [HopDongChiTietID] = @HopDongChiTietID 


End
ELSE
BEGIN
INSERT INTO ThucChayTheoDoiHopDongChiTiet
	SELECT 
       @HopDongChiTietID
      ,@HopDongFK
      ,@NhanHang
      ,@DmNhomNganhREF
      ,@TenNhomNganh
      ,@DmLoaiREF
      ,@TenLoai
      ,@DmNhomWebsiteREF
      ,@TenNhomWebsite
      ,@DmWebsiteREF
      ,@TenWebsite
      ,@DmSanPhamREF
      ,@TenSanPham
      ,@DmLoaiBannerREF
      ,@TenLoaiBanner
      ,@DmChuyenMucREF
      ,@TenChuyenMuc
      ,@DmViTriREF
      ,@TenViTri
      ,@ThoiGian
      ,@SoLuong
      ,@DonViTinh
      ,@DonGia
      ,@ChietKhau
      ,@GiamGia
      ,@TiLeTuVan
      ,@KhuyenMai
      ,@IsKhuyenMai
      ,@ChiPhiTuVan
      ,@ThanhTien
      ,@GhiChu
	  ,dbo.GetDotChayHopDongChiTiet(@HopDongChiTietID) AS DotChayHopDongChiTiet	
	  ,dbo.GetDotDaChayHopDongChiTiet(@HopDongChiTietID) AS NgayDaChay
	  ,@ThucChayDenNgay
	  ,0
	  ,dbo.ThucChay_GetSoLuongThucChayByHopDongChiTietID(@HopDongChiTietID) AS SoLuongDaChay
	  ,dbo.ThucChay_GetSoLuongChuaChayTheoDonViTinh(@SoLuong,@DonViTinh,@HopDongChiTietID) AS SoLuongChuaChay
	  ,dbo.ThucChay_GetThanhTienThucChayByHopDongChiTietID(@HopDongChiTietID) AS ThanhTienDaChay
	  ,dbo.ThucChay_GetThanhTienChuaChayByHopDongChiTietID(@HopDongChiTietID) AS ThanhTienChuaChay      
      ,@CreatedBy
      ,@CreatedAt
      ,@LastModifiedBy
      ,@LastModifiedAt
      ,@DeletedStatus
      ,@PrintStatus
      ,@RecordStatus
      	


END
 
UPDATE dbo.ThucChayTheoDoiHopDongChiTiet
SET TrangThaiHopDongChiTietThucChay = [dbo].[GetTrangThaiThucChayHopDongChiTiet](@HopDongChiTietID)
WHERE [HopDongChiTietID] = @HopDongChiTietID 
 
FETCH NEXT FROM Record_Cursor into 
	  @HopDongChiTietID
	  ,@HopDongFK
	  ,@NhanHang
	  ,@DmNhomNganhREF
	  ,@TenNhomNganh
	  ,@DmLoaiREF
	  ,@TenLoai
	  ,@DmNhomWebsiteREF
	  ,@TenNhomWebsite
	  ,@DmWebsiteREF
	  ,@TenWebsite
	  ,@DmSanPhamREF
	  ,@TenSanPham
	  ,@DmLoaiBannerREF
	  ,@TenLoaiBanner
	  ,@DmChuyenMucREF
	  ,@TenChuyenMuc
	  ,@DmViTriREF
	  ,@TenViTri
	  ,@ThoiGian
	  ,@SoLuong
	  ,@DonViTinh
	  ,@DonGia
	  ,@ChietKhau
	  ,@GiamGia
	  ,@TiLeTuVan
	  ,@KhuyenMai
	  ,@IsKhuyenMai
	  ,@ChiPhiTuVan
	  ,@ThanhTien
	  ,@GhiChu
	  ,@CreatedBy
	  ,@CreatedAt
	  ,@LastModifiedBy
	  ,@LastModifiedAt
	  ,@DeletedStatus
	  ,@PrintStatus
	  ,@RecordStatus
      	
END

CLOSE Record_Cursor
DEALLOCATE Record_Cursor

	

	
END

```
