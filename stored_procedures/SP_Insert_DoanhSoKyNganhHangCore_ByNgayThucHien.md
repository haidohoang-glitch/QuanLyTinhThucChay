# Stored Procedure: `Insert_DoanhSoKyNganhHangCore_ByNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-04-22 16:43:01.563000
- **Ngày sửa cuối**: 2015-04-22 16:43:01.563000

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
--EXEC [dbo].[Insert_DoanhSoKyNganhHangCore_ByNgayThucHien] '2014-01-13'
CREATE PROCEDURE [dbo].[Insert_DoanhSoKyNganhHangCore_ByNgayThucHien]
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @IsPhatSinhGiaTriTD INT, @HopDongID INT, @TrangThaiHopDong_New INT, @HopDongChiTietID INT, @DeletedStatus_HDCT_New INT
	DECLARE @SoHopDong_New NVARCHAR(100), @DmNhanVienREF_New INT, @PhongBanREF_New INT, @BoPhanREF_New INT,@DmMaHopDongREF_New INT
	DECLARE @NhomREF_New INT, @DmKhachHangREF_New INT, @NgayDanhSo_New DATETIME, @DmListNhanHangREF_New NVARCHAR(200)
	DECLARE @DmSanPhamREF_New INT, @DmWebsiteREF_New INT, @DmListNganhHangREF_New NVARCHAR(200), @DonViTinh_New NVARCHAR(50)
	DECLARE @SoLuongNhan INT,@DmNganhHangREF INT , @TenNganhHang NVARCHAR(200), @DmListNganhHangREF NVARCHAR(200);
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
	SET @DmListNhanHangREF_New = ''
	SET @DmSanPhamREF_New = 0
	SET @DmWebsiteREF_New = 0
	SET @DmListNganhHangREF_New = ''
	SET @DonViTinh_New = 0
	SET @TrangThaiHopDong_New = 0
	SET @HopDongChiTietID = 0
	SET @DeletedStatus_HDCT_New = 0
	DECLARE  @IsPhatSinhGiaTriTDcheck INT  SET @IsPhatSinhGiaTriTDcheck = 0
	
	DECLARE Record_Cursor CURSOR FOR
	SELECT hd.DmMaHopDongREF, hd.HopDongID, hd.SoHopDong, hd.SysNhanVienREF, hd.DmPhongBanREF
	, hd.DmBoPhanREF, hd.DmNhomLamViecREF, hd.DmKhachHangREF, hd.NgayDanhSoHopDong, hd.TrangThaiHopDong
	, hdct.HopDongChiTietID, hdct.DanhSachNhanHangREF, hdct.DmSanPhamREF, hdct.DmWebsiteREF
	, hdct.DmNhomNganhREF, hdct.DonViTinh, hdct.DeletedStatus
	 
	FROM HopDong hd
		INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
		INNER JOIN KhachHangThongTinChung khttc ON hd.DmKhachHangREF = khttc.KhachHangThongTinChungID
		WHERE 1=1
		AND 
		CONVERT(date,@NgayThucHien) =
		CASE 
		WHEN CONVERT(DATE,hd.NgayDanhSoHopDong) > CONVERT(DATE,hd.LastModifiedAt) THEN CONVERT(date,hd.NgayDanhSoHopDong) 
		WHEN CONVERT(DATE,hd.NgayDanhSoHopDong) <= CONVERT(DATE,hd.LastModifiedAt) THEN CONVERT(date,hd.LastModifiedAt)
		END 
		--WHERE ((convert(date,hdct.LastModifiedAt) = @NgayThucHien)
		--		OR (CONVERT(date,hd.LastModifiedAt) = @NgayThucHien)
		--)
		
		
	OPEN Record_Cursor

	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor INTO @DmMaHopDongREF_New, @HopDongID, @SoHopDong_New, @DmNhanVienREF_New, @PhongBanREF_New
	, @BoPhanREF_New, @NhomREF_New, @DmKhachHangREF_New, @NgayDanhSo_New, @TrangThaiHopDong_New
	, @HopDongChiTietID, @DmListNhanHangREF_New, @DmSanPhamREF_New, @DmWebsiteREF_New
	, @DmListNganhHangREF_New, @DonViTinh_New, @DeletedStatus_HDCT_New
			
	WHILE @@FETCH_STATUS = 0
		BEGIN
		
					SET @IsPhatSinhGiaTriTD = [dbo].[fn_IsPhatSinhGiaTriTD_DoanhSoKyNganhHangCore]
					(
						@HopDongID,
						@HopDongChiTietID ,
						@SoHopDong_New ,
						@DmNhanVienREF_New,
						@PhongBanREF_New,
						@BoPhanREF_New,
						@NhomREF_New,
						@DmKhachHangREF_New,
						@NgayDanhSo_New, --Cho nay can xem lai
						@DmListNganhHangREF_New,
						@DmSanPhamREF_New,
						@DmWebsiteREF_New,
					
						@DonViTinh_New,
						@NgayThucHien, 
						@TrangThaiHopDong_New,
						@DmMaHopDongREF_New
					)
					--@IsPhatSinhGiaTriTD = 0 PHAT SINH GIA TRI 
					IF(@DeletedStatus_HDCT_New = 1)
					BEGIN
						SET @IsPhatSinhGiaTriTD = 1
					END
			
				--TINH DOANH SO PHAT SINH TRONG KY
			IF(@IsPhatSinhGiaTriTD = 0)
				BEGIN	
					EXEC [Insert_DoanhSoKyNganhHangCore_PhatSinhTrongKy] @NgayThucHien, @HopDongID,@HopDongChiTietID ,@DmMaHopDongREF_New 
					PRINT('Phat Sinh Trong Ky')
				END
			ELSE
				BEGIN
					EXEC [dbo].[Insert_DoanhSoKyNganhHangCore_PhatSinhGiaTriThayDoi] @NgayThucHien, @HopDongID, @HopDongChiTietID, @DmMaHopDongREF_New
					PRINT('Phat sinh Thay Doi')
				END
		FETCH NEXT FROM Record_Cursor INTO @DmMaHopDongREF_New, @HopDongID, @SoHopDong_New, @DmNhanVienREF_New, @PhongBanREF_New
	, @BoPhanREF_New, @NhomREF_New, @DmKhachHangREF_New, @NgayDanhSo_New, @TrangThaiHopDong_New
	, @HopDongChiTietID, @DmListNhanHangREF_New, @DmSanPhamREF_New, @DmWebsiteREF_New
	, @DmListNganhHangREF_New, @DonViTinh_New, @DeletedStatus_HDCT_New
	END

	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor 		
	
END

```
