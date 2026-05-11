# Stored Procedure: `ThucChay_CheckVaUpdateGiaTriThayDoi_Admatic_NhieuSanPham_GiaBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-09 17:13:01.227000
- **Ngày sửa cuối**: 2020-07-14 11:26:45.967000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
----*********AP DUNG CHO TRUONG HOP THAY DOI DON GIA BANNER************----------
--EXEC [dbo].[ThucChay_CheckVaUpdateGiaTriThayDoi_Admatic_NhieuSanPham_GiaBanner_dev] '2017-08-04'

CREATE  PROCEDURE [dbo].[ThucChay_CheckVaUpdateGiaTriThayDoi_Admatic_NhieuSanPham_GiaBanner] 
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @DsBannerID NVARCHAR(500), @HopDongID INT, @HopDongChiTietID INT, @DmBannerID INT, @DmWebsiteREF INT
	, @NgayCheckLog DATETIME, @ChiGhu NVARCHAR(1000)
	, @NgayDanhSoGioiHan DATETIME = '2020-07-20'
	--SET @NgayThucHien ='2016-10-09'

	---****AP DUNG CHO TRUONG HOP CO BANNER THAY DOI DON GIA****---
	set @NgayCheckLog = DATEADD(day,1,@NgayThucHien)

	--1. XAC DINH DANH SACH BANNER CO THAY DOI GIA
	SELECT @DsBannerID = COALESCE(@DsBannerID,'') + A.DmBannerID + ',' FROM
	(
		SELECT  tt.DmBannerID
		FROM (SELECT tc.* FROM dbo.ThucChayHopDongChiTietAndBanner_Admatic tc
		INNER JOIN dbo.HopDong hd ON tc.HopDongREF = hd.HopDongID WHERE hd.NgayDanhSoHopDong < @NgayDanhSoGioiHan) tt
		INNER JOIN dbo.ThucChayHopDongChiTietAndBanner_Admatic_DonGiaTD td ON tt.DmBannerID = td.DmBannerID
		AND tt.ThucChayHopDongChiTietID = td.ThucChayHopDongChiTietID
		WHERE CONVERT(DATE,td.LogTime) = @NgayCheckLog
		--AND TT.DonGia_Banner <> td.DonGia_Banner
		AND abs(CONVERT(INT,TT.DonGia_Banner) - CONVERT(INT,td.DonGia_Banner)) >2
		AND tt.DonGia_Banner <> 0
		AND td.DonGia_Banner <> 0
		--AND tt.HopDongREF = 504166
	)A

	--2. XAC DINH CAC HOP DONG CHI TIET CHAY UNG VOI DANH SACH BANNER THAY DOI GIA
	DECLARE Cursor_giabanner_admatic CURSOR FOR
		SELECT DISTINCT HopDongID, HopDongChiTietREF, DmBannerREF, DmWebsiteREF
		FROM dbo.ThucChayDaTinh 
		WHERE DmHinhThucQuangCao = 42
		AND DmBannerREF IN (SELECT DISTINCT VALUE FROM dbo.ASD_SPLIT(',',@DsBannerID)) 
		AND NgayThucHien < @NgayThucHien --CHO NAY XEM LAI
		AND NgayDanhSoHopDong < @NgayDanhSoGioiHan
		--AND HopDongID =504166
		
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
