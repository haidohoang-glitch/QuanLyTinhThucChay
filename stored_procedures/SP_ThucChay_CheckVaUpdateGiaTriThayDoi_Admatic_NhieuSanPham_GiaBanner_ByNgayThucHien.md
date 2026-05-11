# Stored Procedure: `ThucChay_CheckVaUpdateGiaTriThayDoi_Admatic_NhieuSanPham_GiaBanner_ByNgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-08-09 11:48:49.707000
- **Ngày sửa cuối**: 2018-07-20 10:51:31.087000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@DsBannerID` | `nvarchar(1000)` | No |
| `@HopDongID` | `int(4)` | No |

## Definition (Source Code)

```sql
----*********AP DUNG CHO TRUONG HOP THAY DOI DON GIA BANNER************----------
--EXEC [dbo].[ThucChay_CheckVaUpdateGiaTriThayDoi_Admatic_NhieuSanPham_GiaBanner_ByNgayThucHien] '2017-08-07' ,'522650'

CREATE  PROCEDURE [dbo].[ThucChay_CheckVaUpdateGiaTriThayDoi_Admatic_NhieuSanPham_GiaBanner_ByNgayThucHien] 
	@NgayThucHien DATETIME,
	@DsBannerID NVARCHAR(500),
	@HopDongID int
AS
BEGIN
	DECLARE @HopDongChiTietID INT, @DmBannerID INT, @DmWebsiteREF INT
	, @ChiGhu NVARCHAR(1000)
	--SET @NgayThucHien ='2016-10-09'

	---****AP DUNG CHO TRUONG HOP CO BANNER THAY DOI DON GIA****---

	
	--2. XAC DINH CAC HOP DONG CHI TIET CHAY UNG VOI DANH SACH BANNER THAY DOI GIA
	DECLARE Cursor_giabanner_admatic CURSOR FOR
		SELECT DISTINCT HopDongID, HopDongChiTietREF, DmBannerREF, DmWebsiteREF
		FROM dbo.ThucChayDaTinh 
		WHERE DmHinhThucQuangCao = 42
		AND DmBannerREF IN (SELECT DISTINCT VALUE FROM dbo.ASD_SPLIT(',',@DsBannerID)) 
		AND NgayThucHien <= @NgayThucHien --CHO NAY XEM LAI
		AND HopDongID = @HopDongID
		
	OPEN Cursor_giabanner_admatic
	FETCH NEXT FROM Cursor_giabanner_admatic INTO @HopDongID, @HopDongChiTietID ,@DmBannerID, @DmWebsiteREF
	WHILE @@FETCH_STATUS =0
	BEGIN
		PRINT 'Update gia tri thay doi'
		SET @ChiGhu =  N'ADMATIC_DonGia_TD_GTTD đối trừ giảm từ '
		--3. UPDATE GIA TRI THAY DOI CUA CAC HOP DONG CHI TIET CO BANNER THAY DOI GIA
		EXEC [dbo].[ThucChay_Insert_GTTD_DoiTruGiam_ThucChayDaTinh_Admatic] 
			@NgayThucHien = @NgayThucHien, --@NgayThucHien DATETIME,
			@HopDongID = @HopDongID, --@HopDongID INT, 
			@HopDongChiTietID = @HopDongChiTietID, --@HopDongChiTietID INT
			@DmBannerREF = @DmBannerID,
			@DmWebsiteREF = @DmWebsiteREF,
			@GhiChu = @ChiGhu

		SET @ChiGhu = N'ADMATIC_DonGia_TD_GTTD Tăng với đơn giá mới '
		--4. TINH GIA TRI THUC CHAY CHO CAC HOP DONG CHI TIET
		EXEC [dbo].[ThucChay_Insert_GTTD_VoiDonGiaMoi_ThucChayDaTinh_Admatic] 
			@NgayThucHien, --@NgayThucHien DATETIME,
			@HopDongID, --@HopDongID INT, 
			@HopDongChiTietID, --@HopDongChiTietID INT
			@DmBannerID,
			@DmWebsiteREF,
			@ChiGhu

		--4.1 UPDATE TRANG THAI THUC CHAY TREN THU TU CHAY
		EXEC [dbo].[ThucChay_Innit_ThucChay_AdmaticHopDongChiTietThucChay_ByHopDongID] @HopDongID, @NgayThucHien

	FETCH NEXT FROM Cursor_giabanner_admatic INTO @HopDongID, @HopDongChiTietID ,@DmBannerID, @DmWebsiteREF
	END
	CLOSE Cursor_giabanner_admatic;
	DEALLOCATE Cursor_giabanner_admatic;

END


```
