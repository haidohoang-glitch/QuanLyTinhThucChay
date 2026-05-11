# Stored Procedure: `Insert_DoanhSoTienVeCore_ByNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-12 10:47:07.577000
- **Ngày sửa cuối**: 2015-06-12 10:47:07.577000

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

--EXEC [dbo].[Insert_DoanhSoTienVeCore_ByNgayThucHien] '2015-01-05'
CREATE PROCEDURE [dbo].[Insert_DoanhSoTienVeCore_ByNgayThucHien]
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @IsPhatSinhGiaTriTD INT, @HopDongID INT, @TrangThaiHopDong_New INT, @HopDongChiTietID INT, @DeletedStatus_HDCT_New INT
	DECLARE @SoHopDong_New NVARCHAR(100), @DmNhanVienREF_New INT, @PhongBanREF_New INT, @BoPhanREF_New INT,@DmMaHopDongREF_New INT
	DECLARE @NhomREF_New INT, @DmKhachHangREF_New INT, @NgayDanhSo_New DATETIME, @DmHinhThucQuangCaoREF_New INT
	DECLARE @DmSanPhamREF_New INT, @DmWebsiteREF_New INT, @DmBannerREF_New INT, @DonViTinh_New NVARCHAR(50)
	DECLARE @ThongTinTienVeID INT, @SoHoaDon NVARCHAR(50),@SoLuong INT,@DonGia FLOAT,@ChietKhau FLOAT 
	
	DECLARE @NgayThucHien_update DATETIME, @HopDongID_Update INT, @HopDongChiTietID_Update INT, @ThongTinTienVeID_Update INT;
	DECLARE @TableHopDongTD TABLE (HopDongIDTD INT)
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
	SET @DmWebsiteREF_New = 0
	SET @DmBannerREF_New = 0
	SET @DonViTinh_New = 0
	SET @TrangThaiHopDong_New = 0
	SET @HopDongChiTietID = 0
	SET @DeletedStatus_HDCT_New = 0
	SET @ThongTinTienVeID = 0
	
			
	DECLARE Record_Cursor CURSOR FOR
	
	SELECT hd.DmMaHopDongREF, hd.HopDongID, hd.SoHopDong, hd.SysNhanVienREF, hd.DmPhongBanREF
	, hd.DmBoPhanREF, hd.DmNhomLamViecREF, hd.DmKhachHangREF, hd.NgayDanhSoHopDong, hd.TrangThaiHopDong
	, hdct.HopDongChiTietID, hdct.DmLoaiREF, hdct.DmSanPhamREF, hdct.DmWebsiteREF
	, hdct.DmBannerREF, hdct.DonViTinh, hdct.DeletedStatus,tthd.ThongTinTienVeID
	, hdct.SoLuong, hdct.DonGia, hdct.ChietKhau
	FROM HopDong hd
		INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
		INNER JOIN ThongTinTienVe tthd ON tthd.HopDongREF = hd.HopDongID
		WHERE 1=1
		AND 
		(
		   CONVERT(date,@NgayThucHien) = CONVERT(date,tthd.LastModifiedAt)
		OR CONVERT(date,@NgayThucHien) = CONVERT(date,hd.LastModifiedAt)
		OR CONVERT(date,@NgayThucHien) = CONVERT(date,hdct.LastModifiedAt)
		)
		
	
		
	OPEN Record_Cursor

	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor INTO @DmMaHopDongREF_New, @HopDongID, @SoHopDong_New, @DmNhanVienREF_New, @PhongBanREF_New
	, @BoPhanREF_New, @NhomREF_New, @DmKhachHangREF_New, @NgayDanhSo_New, @TrangThaiHopDong_New
	, @HopDongChiTietID, @DmHinhThucQuangCaoREF_New, @DmSanPhamREF_New, @DmWebsiteREF_New
	, @DmBannerREF_New, @DonViTinh_New, @DeletedStatus_HDCT_New,@ThongTinTienVeID
	, @SoLuong,@DonGia,@ChietKhau
			
	WHILE @@FETCH_STATUS = 0
		BEGIN
			PRINT @HopDongChiTietID
			SET @IsPhatSinhGiaTriTD = [dbo].[fn_IsPhatSinhGiaTriTD_DoanhSoTienVeCore_New]
			(
				@NgayThucHien,
				@HopDongID,
				@HopDongChiTietID ,
				--@SoHopDong_New ,
				--@DmNhanVienREF_New,
				--@PhongBanREF_New,
				--@BoPhanREF_New,
				--@NhomREF_New,
				--@DmKhachHangREF_New,
				--@NgayDanhSo_New, --Cho nay can xem lai
				--@DmHinhThucQuangCaoREF_New,
				--@DmSanPhamREF_New,
				--@DmWebsiteREF_New,
				--@DmBannerREF_New,
				--@DonViTinh_New,
				--@NgayThucHien, 
				--@TrangThaiHopDong_New,
				--@SoHoaDon,
				@ThongTinTienVeID
				--@SoLuong,@DonGia,@ChietKhau,@DmMaHopDongREF_New
			)
			--@IsPhatSinhGiaTriTD = 0 PHAT SINH GIA TRI 
			--TINH DOANH SO PHAT SINH TRONG KY
			IF(@IsPhatSinhGiaTriTD = 0)
			BEGIN
				PRINT(@IsPhatSinhGiaTriTD)
				EXEC [Insert_DoanhSoTienVeCore_PhatSinhTrongKy] @NgayThucHien, @HopDongID,@HopDongChiTietID ,@DmMaHopDongREF_New ,@ThongTinTienVeID
			END
			--@IsPhatSinhGiaTriTD <> 0 PHAT SINH GIA TRI THAY DOI
			ELSE
			BEGIN
				      INSERT INTO @TableHopDongTD SELECT @HopDongID
			END
		FETCH NEXT FROM Record_Cursor INTO @DmMaHopDongREF_New, @HopDongID, @SoHopDong_New, @DmNhanVienREF_New, @PhongBanREF_New
	, @BoPhanREF_New, @NhomREF_New, @DmKhachHangREF_New, @NgayDanhSo_New, @TrangThaiHopDong_New
	, @HopDongChiTietID, @DmHinhThucQuangCaoREF_New, @DmSanPhamREF_New, @DmWebsiteREF_New
	, @DmBannerREF_New, @DonViTinh_New, @DeletedStatus_HDCT_New,@ThongTinTienVeID
	, @SoLuong,@DonGia,@ChietKhau
	END

	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor 		
	----- Thuc hien ghi nhan lai cac hopdong bi thay doi 
	IF(SELECT COUNT(*) FROM @TableHopDongTD) > 0
	DECLARE @NgayTienVeThayDoi DATETIME, @HopDongIDThayDoi INT, @HopDongChiTietIDThayDoi INT, @ThongTinTienVeThayDoiID INT;
	DECLARE @HopDongID_TD INT 
	BEGIN
		DECLARE BU_cursor1 CURSOR FOR
		SELECT DISTINCT
		thdt.HopDongIDTD
		FROM @TableHopDongTD thdt 
		OPEN BU_cursor1
		FETCH NEXT FROM BU_cursor1 INTO @HopDongID_TD
		                             
		WHILE @@FETCH_STATUS = 0
		BEGIN
			EXEC dbo.Insert_DoanhSoTienVeCore_PhatSinhThayDoi @NgayThucHien,@HopDongID_TD
			
		FETCH NEXT FROM BU_cursor1 INTO @HopDongID_TD
		END

		CLOSE BU_cursor1
		DEALLOCATE BU_cursor1
		
		DECLARE BU_cursor CURSOR FOR
		SELECT DISTINCT
		hd.HopDongIDTD,
		hdct.HopDongChiTietID,
		tthd.ThongTinTienVeID
		FROM (SELECT DISTINCT
		thdt.HopDongIDTD
		FROM @TableHopDongTD thdt)  hd 
		INNER JOIN HopDongChiTiet hdct ON hd.HopDongIDTD = hdct.HopDongFK
		INNER JOIN ThongTinTienVe tthd ON hd.HopDongIDTD = tthd.HopDongREF
		WHERE tthd.NgayThanhToan <=@NgayThucHien
		OPEN BU_cursor
		FETCH NEXT FROM BU_cursor INTO @HopDongIDThayDoi,@HopDongChiTietIDThayDoi,@ThongTinTienVeThayDoiID
		                             
		WHILE @@FETCH_STATUS = 0
		BEGIN
			--DELETE FROM DoanhSoTienVeCore WHERE HopDongID = @HopDongIDThayDoi AND HopDongChiTietREF = @HopDongChiTietIDThayDoi AND ThongTinTienVeREF = @ThongTinTienVeThayDoiID
            EXEC dbo.Insert_DoanhSoTienVeCore_NoiBo_History_Update @NgayThucHien,@HopDongIDThayDoi,@HopDongChiTietIDThayDoi,@ThongTinTienVeThayDoiID
            EXEC dbo.Insert_DoanhSoTienVeCore_ThucThuKhuyenMai_History_Update @NgayThucHien,@HopDongIDThayDoi,@HopDongChiTietIDThayDoi,@ThongTinTienVeThayDoiID
			
			FETCH NEXT FROM BU_cursor INTO @HopDongIDThayDoi,@HopDongChiTietIDThayDoi,@ThongTinTienVeThayDoiID
		END

		CLOSE BU_cursor
		DEALLOCATE BU_cursor
	END

END

```
