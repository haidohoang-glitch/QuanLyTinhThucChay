# Stored Procedure: `ThucChay_CheckVaUpdateGiaTriThayDoi_Admatic_NhieuSanPham_GiaBanner_dev`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-08-07 11:12:55.300000
- **Ngày sửa cuối**: 2017-08-07 11:43:07.050000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
----*********AP DUNG CHO TRUONG HOP THAY DOI DON GIA BANNER************----------
--EXEC [dbo].[ThucChay_CheckVaUpdateGiaTriThayDoi_Admatic_NhieuSanPham_GiaBanner_dev] '2017-08-04'

CREATE  PROCEDURE [dbo].[ThucChay_CheckVaUpdateGiaTriThayDoi_Admatic_NhieuSanPham_GiaBanner_dev] 
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @DsBannerID NVARCHAR(500), @HopDongID INT, @HopDongChiTietID INT, @DmBannerID INT, @DmWebsiteREF INT
	--SET @NgayThucHien ='2016-10-09'

	---****AP DUNG CHO TRUONG HOP CO BANNER THAY DOI DON GIA****---

	--1. XAC DINH DANH SACH BANNER CO THAY DOI GIA
	SELECT @DsBannerID = COALESCE(@DsBannerID,'') + A.DmBannerID + ',' FROM
	(
		SELECT  tt.DmBannerID
		FROM dbo.ThucChayHopDongChiTietAndBanner_Admatic tt
		INNER JOIN ThucChayHopDongChiTietAndBanner_Admatic_DonGiaTD td ON tt.DmBannerID = td.DmBannerID
		AND tt.ThucChayHopDongChiTietID = td.ThucChayHopDongChiTietID
		WHERE CONVERT(DATE,td.LogTime) = @NgayThucHien
		--AND TT.DonGia_Banner <> td.DonGia_Banner
		AND abs(CONVERT(INT,TT.DonGia_Banner) - CONVERT(INT,td.DonGia_Banner)) >2
		AND tt.DonGia_Banner <> 0
		AND td.DonGia_Banner <> 0
		AND tt.HopDongREF = 504166
	)A

	--2. XAC DINH CAC HOP DONG CHI TIET CHAY UNG VOI DANH SACH BANNER THAY DOI GIA
	DECLARE Cursor_giabanner_admatic CURSOR FOR
		SELECT DISTINCT HopDongID, HopDongChiTietREF, DmBannerREF, DmWebsiteREF
		FROM dbo.ThucChayDaTinh 
		WHERE DmHinhThucQuangCao = 42
		AND DmBannerREF IN (SELECT DISTINCT VALUE FROM dbo.ASD_SPLIT(',',@DsBannerID)) 
		AND NgayThucHien <= @NgayThucHien --CHO NAY XEM LAI
		AND HopDongID =504166
		
	OPEN Cursor_giabanner_admatic
	FETCH NEXT FROM Cursor_giabanner_admatic INTO @HopDongID, @HopDongChiTietID ,@DmBannerID, @DmWebsiteREF
	WHILE @@FETCH_STATUS =0
	BEGIN
		PRINT 'Update gia tri thay doi'
		--3. UPDATE GIA TRI THAY DOI CUA CAC HOP DONG CHI TIET CO BANNER THAY DOI GIA
		EXEC [dbo].[ThucChay_Insert_GTTD_DoiTruGiam_ThucChayDaTinh_Admatic_dev] 
			@NgayThucHien, --@NgayThucHien DATETIME,
			@HopDongID, --@HopDongID INT, 
			@HopDongChiTietID, --@HopDongChiTietID INT
			@DmBannerID,
			@DmWebsiteREF

		--4. TINH GIA TRI THUC CHAY CHO CAC HOP DONG CHI TIET
		EXEC [dbo].[ThucChay_Insert_GTTD_VoiDonGiaMoi_ThucChayDaTinh_Admatic_dev] 
			@NgayThucHien, --@NgayThucHien DATETIME,
			@HopDongID, --@HopDongID INT, 
			@HopDongChiTietID, --@HopDongChiTietID INT
			@DmBannerID,
			@DmWebsiteREF

		--4.1 UPDATE TRANG THAI THUC CHAY TREN THU TU CHAY
		EXEC [dbo].[ThucChay_Innit_ThucChay_AdmaticHopDongChiTietThucChay_ByHopDongID] @HopDongID, @NgayThucHien

	FETCH NEXT FROM Cursor_giabanner_admatic INTO @HopDongID, @HopDongChiTietID ,@DmBannerID, @DmWebsiteREF
	END
	CLOSE Cursor_giabanner_admatic;
	DEALLOCATE Cursor_giabanner_admatic;

END


```
