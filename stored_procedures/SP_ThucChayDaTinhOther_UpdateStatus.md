# Stored Procedure: `ThucChayDaTinhOther_UpdateStatus`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-12-16 13:39:42.980000
- **Ngày sửa cuối**: 2014-12-16 13:39:42.980000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@id` | `nvarchar(100)` | No |
| `@recordStatus` | `int(4)` | No |
| `@deletedStatus` | `int(4)` | No |
| `@tienThucChay` | `float(8)` | No |
| `@ghiChu` | `nvarchar(2000)` | No |
| `@userActive` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2014-12-15
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChayDaTinhOther_UpdateStatus]
	-- Add the parameters for the stored procedure here
	@id			NVARCHAR(50),
	@recordStatus		INT,
	@deletedStatus	INT,
	@tienThucChay	FLOAT,
	@ghiChu			NVARCHAR(1000),
	@userActive	NVARCHAR(50)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    UPDATE ThucChayDaTinhOther
    SET 
		Recordstatus = @recordStatus,
		DeletedStatus = @deletedStatus,
		ThanhTienThucChay = @tienThucChay,
		GhiChu		 = @ghiChu,
		LastModifiedAt = GETDATE(),
		LastModifiedBy = @userActive
	WHERE 
		ThucChayDaTinhOtherID = @id
		
	-- Day du lieu sang bang ThucChayDaTinh khi duyet du lieu
	IF @recordStatus = 1
	BEGIN
		-- Insert thuc chay
		DECLARE @DmMaHopDongREF INT = 0
			,@TenMaHopDong NVARCHAR(50) = ''
			,@DmHinhThucQuangCao	INT = 27
			,@TenHnhThucQuangCao	NVARCHAR(50) = 'Google Adsense'
			,@DmSanPhamREF INT = 9001
			,@TenSanPham NVARCHAR(50) = 'Google Adsense'
			,@GhiChuThucChay NVARCHAR(50) = 'ThucChay_Google_Adsense'
			,@DonViTinh NVARCHAR(50) = N'Gói'
			,@DmWebsiteREF INT = 0
			,@TenWebsite NVARCHAR(50) = ''
			,@NgayThucHien DATETIME = CONVERT(DATE,GETDATE())
			,@SoLuongThucChay INT = 1
			,@SoLuongThucChayKM INT = 0		
			,@ThanhTienThucChay FLOAT = 0
			,@ThanhTienThucChayKM FLOAT = 0
			,@GiaTriThayDoi			FLOAT = @tienThucChay

		INSERT INTO ThucChayDaTinh
		SELECT  
			NEWID(), 
			0 HopDongID,
			'-' SoHopDong, 
			@DmMaHopDongREF DmMaHopDongREF, 
			@TenMaHopDong TenMaHopDong, 
			'' NgayDanhSoHopDong, 
			'' NgayKyHopDong, 
			'' NhanHopDong, 
			'' NgayNhanBanFax, 
			'' NgayNhanHopDongBanCung, 
			'' NgayChuyenHopDongChoKeToan, 
			0 So, 0 Thang, 0 Nam, 
			0 GiaTriHopDong, 0 CongNo,
			0 HopDongChiTietID,
			0 DangSuDung,
			0 IsGiayPhep, 
			1 TrangThaiHopDong,
			0 IsBanCung, 
			0 DmPhongBanREF, 
			''TenPhongBan, 
			0 DmBoPhanREF, 
			''TenBoPhan, 
			0 DmNhomLamViecREF, 
			''TenNhom, 
			0 DmDiaDiemLamViecREF, 
			'' TenDiaDiemLamViec, 
			0 SysNhanVienREF, 
			'' TenDangNhap,  
			'' TenNhanVien, 
			'' TenKhachHang, 
			'' NhanHang, 
			0 DmNhomNganhREF, 
			'' TenNhomNganh, 
			@DmHinhThucQuangCao DmHinhThucQuangCao, 
			@TenHnhThucQuangCao TenHinhThucQuangCao, 
			@DmSanPhamREF DmSanPhamREF,
			@TenSanPham TenSanPham,  
			0 DmNhomWebsiteREF, 
			'' TenNhomWebsite, 
			0 DmChuyenMucREF, 
			'' TenChuyenMuc,
			0 DmLoaiBannerREF, 
			'' TenLoaiBanner, 
			0 DmViTriREF, 
			'' TenViTri, 
			@GhiChu AS DotChayHopDong,
			0 AS SoLuongDotChayHD,
			'' DotChayBooking,
			0 AS SoLuongDotChayBooking, 
			0 SoLuong,
			@DonViTinh, 
			0 DonGia, 
			0 DonGiaTheoDonViTinh,
			0 ChietKhau, 0 GiamGia, 0 ThanhTien,
			0 TiLeTuVan,  0 ChiPhiTuVan,
			0 IsKhuyenMai,  
			'' KhuyenMai,
			0 DmBannerREF,
			0 DmChienDichREF,
			@DmWebsiteREF DmWebsiteREF,
			@TenWebsite TenWebsite,
			0 TongViewThucChay,
			0 TongClickThucChay,
			0 TongSoBaiViet,
			0 SoLuongThucChay,
			@NgayThucHien AS NgayThucHien,
			@GiaTriThayDoi as GiaTriThayDoi,
			0 as ThanhTienThucChayTruocTrietKhau,
			0 GiaTriTrietKhauThucChay,
			0 AS ThanhTienSauTrietKhauThucChay,
			0 AS GiaTriHoaHongThucChay,
			0 AS ThanhTienThucThu,
			@ThanhTienThucChayKM as ThanhTienKM,
			@SoLuongThucChayKM as SoLuongThucChayKM,
			0 SoLuongLechTreoHa,
			0 ThanhTienLechTreoHa,
			GETDATE(),
			GETDATE(),
			0 IsPheDuyet,
			'' PheDuyetBy,
			'' PheDuyetAt,
			@SoLuongThucChay as SoLuongThayDoi,
			0 as SoLuongKMThayDoi,
			0 as GiaTriKMThayDoi,
			@GhiChu as GhiChu
			
		-- Insert log gia tri thay doi
		EXEC dbo.ThucChay_LogNNTinhGiaTriThayDoi_Insert
			@HopDongREF				= 0
			,@SoHopDong				= ''
			,@HopDongChiTietID		= 0
			,@DmSanPhamREF			= 9001
			,@DmWebsiteREF			= 0
			,@NgayThucHien			= @NgayThucHien
			,@GiaTriThayDoi			= @tienThucChay
			,@DonGiaCurrent			= 0
			,@SoLuongCurrent		= 0
			,@DonGiaOld				= 0
			,@SoLuongOld			= 0
			,@NoiDungLog			= @ghiChu
			,@NguonLog				= 'ThucChay_GoogleAdsense'
			,@GhiChu				= N'ThucChay_GoogleAdsense'
	END
END

```
