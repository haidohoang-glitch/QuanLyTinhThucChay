# Stored Procedure: `ThucChay_UpdateGiaTriThayDoi_CPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-09-14 14:36:23.720000
- **Ngày sửa cuối**: 2016-10-31 14:40:39.783000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_UpdateGiaTriThayDoi_CPR] '2015-08-14'

CREATE PROCEDURE [dbo].[ThucChay_UpdateGiaTriThayDoi_CPR] 
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @IsPhatSinhGiaTriTD INT, @HopDongID INT, @TrangThaiHopDong_New INT
			, @HopDongChiTietID INT, @DeletedStatus_HDCT_New INT
	DECLARE @SoHopDong_New NVARCHAR(100), @DmNhanVienREF_New INT
			, @PhongBanREF_New INT, @BoPhanREF_New INT,@DmMaHopDongREF_New INT
	DECLARE @NhomREF_New INT, @DmKhachHangREF_New INT
			, @NgayDanhSo_New DATETIME, @DmHinhThucQuangCaoREF_New INT
	DECLARE @DmSanPhamREF_New INT, @DmLoaiBannerREF_New INT
			, @DmBannerREF_New INT, @DonViTinh_New NVARCHAR(50), @ThanhTien_New BIGINT
			, @DmNhomWebsiteTag_New NVARCHAR(300)
	DECLARE @DmChuyenMuc_new INT ,@ChietKhau_New FLOAT, @DonGia_New INT, @ls_DmNhanHangREF NVARCHAR(200)
	SET @IsPhatSinhGiaTriTD = 0 --Khong phai la phat sinh gia tri thay doi
	SET @IsPhatSinhGiaTriTD = 0
	SET @HopDongID  = 0
	SET @SoHopDong_New = ''
	SET @DmNhanVienREF_New = 0
	SET @PhongBanREF_New = 0
	SET @BoPhanREF_New = 0
	SET @NhomREF_New = 0
	SET @DmKhachHangREF_New = 0
	SET @NgayDanhSo_New = '2010-01-01'
	SET @DmHinhThucQuangCaoREF_New = 0
	SET @DmSanPhamREF_New = 0
	SET @DmNhomWebsiteTag_New = '' 
	SET @DmBannerREF_New = 0
	SET @DmLoaiBannerREF_New = 0
	SET @DonViTinh_New = 0
	SET @TrangThaiHopDong_New = 0
	SET @HopDongChiTietID = 0
	SET @DeletedStatus_HDCT_New = 0
	SET @DonGia_New = 0
	SET @ChietKhau_New = 0
	SET @ls_DmNhanHangREF = ''
	SET @ThanhTien_New = 0
	
	
	--*******CHECK DE PHAN BIET PHAT SINH DOANH SO THONG THUONG VA PHAT SINH GIA TRI THAY DOI DO THAY DOI CAC DOI TUONG TREN HD)
	--===========CAC DOI TUONG CAN PHAI CHECK
			--@HopDongID,
			--@HopDongChiTietID,
			--@SoHopDong_New,
			--@DmNhanVienREF_New,
			--@PhongBanREF_New,
			--@BoPhanREF_New,
			--@NhomREF_New,
			--@DmKhachHangREF_New,
			--@NgayDanhSo_New, --Cho nay can xem lai
			--@DmHinhThucQuangCaoREF_New,
			--@DmSanPhamREF_New,
			--@DmNhomWebsiteTag_New,
			--@DmLoaiBannerREF_New,
			--@DmBannerREF_New,
			--@DonViTinh_New,
			--@TrangThaiHopDong_New,
			--@NgayThucHien 
			--**(Phan bo bi xoa)
			
	DECLARE Record_Cursor CURSOR FOR
	--XAC DINH DANH SACH CAC HOP DONG CO THUC CHAY VA CO PHAT SINH THONG TIN THAY DOI CUA SAN PHAM BRAND PAGE
	SELECT hd.DmMaHopDongREF, hd.HopDongID, hd.SoHopDong, hd.SysNhanVienREF, hd.DmPhongBanREF
	, hd.DmBoPhanREF, hd.DmNhomLamViecREF, hd.DmKhachHangREF, hd.NgayDanhSoHopDong, hd.TrangThaiHopDong
	, hdct.HopDongChiTietID, hdct.DanhSachNhanHangREF, hdct.DmLoaiREF, hdct.DmSanPhamREF, hdct.DmLoaiBannerREF
	, hdct.DmBannerREF, hdct.DonViTinh, hdct.DonGia, hdct.DeletedStatus,hdct.DmChuyenMucREF,hdct.ChietKhau
	, hdct.DmNhomWebsiteREF, hdct.ThanhTien
	FROM HopDong hd
		INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
		INNER JOIN KhachHangThongTinChung khttc ON hd.DmKhachHangREF = khttc.KhachHangThongTinChungID
		INNER JOIN (
			SELECT TOP 1 TCDT.HopDongID, TCDT.HopDongChiTietREF, TCDT.DmSanPhamREF
			  FROM ThucChayDaTinh tcdt
			WHERE TCDT.NgayThucHien <= @NgayThucHien
		)TCDT ON hdct.HopDongChiTietID = tcdt.HopDongChiTietREF 
		WHERE 1=1
		AND hdct.DmSanPhamREF IN (680)
		AND CONVERT(date,@NgayThucHien) =(
		CASE 
		WHEN CONVERT(DATE,hd.NgayDanhSoHopDong) > CONVERT(DATE,hd.LastModifiedAt) THEN CONVERT(date,hd.NgayDanhSoHopDong) 
		WHEN CONVERT(DATE,hd.NgayDanhSoHopDong) <= CONVERT(DATE,hd.LastModifiedAt) THEN CONVERT(date,hd.LastModifiedAt)
		END 
		)
		
		
	OPEN Record_Cursor

	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor INTO @DmMaHopDongREF_New, @HopDongID, @SoHopDong_New, @DmNhanVienREF_New, @PhongBanREF_New
	, @BoPhanREF_New, @NhomREF_New, @DmKhachHangREF_New, @NgayDanhSo_New, @TrangThaiHopDong_New
	, @HopDongChiTietID, @ls_DmNhanHangREF, @DmHinhThucQuangCaoREF_New, @DmSanPhamREF_New, @DmLoaiBannerREF_New
	, @DmBannerREF_New, @DonViTinh_New, @DonGia_New, @DeletedStatus_HDCT_New, @DmChuyenMuc_new,@ChietKhau_New
	, @DmNhomWebsiteTag_New	, @ThanhTien_New	
	WHILE @@FETCH_STATUS = 0
		BEGIN
			PRINT @HopDongChiTietID
			SET @IsPhatSinhGiaTriTD = [dbo].[fn_IsPhatSinhGiaTriTD_ThucChayCPR]
			(
				@HopDongID,
				@HopDongChiTietID,
				@SoHopDong_New,
				@DmNhanVienREF_New,
				@PhongBanREF_New,
				@BoPhanREF_New,
				@NhomREF_New,
				@DmKhachHangREF_New,
				@NgayDanhSo_New, --Cho nay can xem lai
				@DmHinhThucQuangCaoREF_New,
				@DmSanPhamREF_New,
				@DmNhomWebsiteTag_New,
				@DmLoaiBannerREF_New,
				@DmBannerREF_New,
				@DonViTinh_New,
				@TrangThaiHopDong_New,
				@NgayThucHien 
			)
			--@IsPhatSinhGiaTriTD = 0 PHAT SINH GIA TRI 
			IF(@DeletedStatus_HDCT_New = 1)
			BEGIN
				SET @IsPhatSinhGiaTriTD = 1
			END
			
			--TINH DOANH SO PHAT SINH TRONG KY
			IF(@IsPhatSinhGiaTriTD = 0)
			BEGIN
				--PRINT @IsPhatSinhGiaTriTD
				EXEC [ThucChay_CheckHopDongCoPhatSinhGiaTri_CPR] @HopDongID,@DmSanPhamREF_New,@HopDongChiTietID,@NgayThucHien,@DonGia_New,@ChietKhau_New, @ThanhTien_New
			END
			--@IsPhatSinhGiaTriTD <> 0 
			--PHAT SINH GIA TRI THAY DOI
			ELSE 
				BEGIN
					EXEC [ThucChay_CheckHopDongCoPhatSinhGiaTriThayDoi_CPR] @HopDongID,@DmSanPhamREF_New,@HopDongChiTietID,@NgayThucHien,@DonGia_New,@ChietKhau_New, @ThanhTien_New
				END
		FETCH NEXT FROM Record_Cursor INTO @DmMaHopDongREF_New, @HopDongID, @SoHopDong_New, @DmNhanVienREF_New, @PhongBanREF_New
	, @BoPhanREF_New, @NhomREF_New, @DmKhachHangREF_New, @NgayDanhSo_New, @TrangThaiHopDong_New
	, @HopDongChiTietID, @ls_DmNhanHangREF, @DmHinhThucQuangCaoREF_New, @DmSanPhamREF_New, @DmLoaiBannerREF_New
	, @DmBannerREF_New, @DonViTinh_New, @DonGia_New, @DeletedStatus_HDCT_New, @DmChuyenMuc_new,@ChietKhau_New
	, @DmNhomWebsiteTag_New	, @ThanhTien_New
	END

	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor 	
	
	SELECT '1'
END

--EXEC [ThucChay_UpdateGiaTriThayDoi_CPR] '2014-06-03','2014-06-03'

```
