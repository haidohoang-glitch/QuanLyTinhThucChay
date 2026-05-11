# Stored Procedure: `ThucChay_DoiTruVaTinhLai_CPM_Native_Ads_GhiChu`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-08 16:11:38.457000
- **Ngày sửa cuối**: 2021-06-10 17:31:40.150000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@pSoHopDong` | `nvarchar(200)` | No |
| `@pDmSanPhamREF` | `int(4)` | No |
| `@pStartDate` | `datetime(8)` | No |
| `@pEndDate` | `datetime(8)` | No |
| `@pNgayGhiNhanThucChay` | `datetime(8)` | No |
| `@GhiChu` | `nvarchar(2000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
EXEC [dbo].[ThucChay_ExcInsertThucChayDaTinh_CPM_Native_Ads_BySoHopDongAndNgayThucHien] 
	'QC2110718',
	821,
	'2018-07-18' ,
	'2018-07-29' ,
	@pNgayGhiNhanThucChay DATET
*/

CREATE PROCEDURE [dbo].[ThucChay_DoiTruVaTinhLai_CPM_Native_Ads_GhiChu] 
	@pSoHopDong NVARCHAR(100),
	@pDmSanPhamREF INT,
	@pStartDate datetime,
	@pEndDate DATETIME,
	@pNgayGhiNhanThucChay DATETIME,
	@GhiChu	NVARCHAR(1000)
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	DECLARE @SoHopDong NVARCHAR(50), @HopDongID INT, @DmSanPhamREF INT, @TenWebsite NVARCHAR(50), @DmWebsiteREF INT, @DmBannerREF INT
	DECLARE @GhiChu_DoiTruThucChay NVARCHAR(1000), @Ghichu_TinhLaiThucChay NVARCHAR(1000)

	SET @SoHopDong = @pSoHopDong
	SET @DmSanPhamREF = @pDmSanPhamREF
	SET @HopDongID = (SELECT TOP (1) HopDongID FROM dbo.HopDong WHERE SoHopDong = @SoHopDong ORDER BY HopDongID)

	SET @GhiChu_DoiTruThucChay = @GhiChu +  N', Doi tru thuc chay Native ads cho SoHopDong: ' + @SoHopDong
	SET @Ghichu_TinhLaiThucChay = @GhiChu + N', Tinh lai thuc chay Native ads cho SoHopDong: ' + @SoHopDong

	SET @NgayThucHien = @pStartDate

	DELETE FROM dbo.ThucChay_Native_Ads_Temp
	WHERE 1=1

	--CAP NHAT THONG TIN BANNER NATIVE ADS
	EXEC [ThucChay_Insert_And_Update_HopDongChiTietAndBanner_Native_Ads] @NgayThucHien = @pStartDate
	EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner_Native_Ads_NgayThucHien] @NgayThucHien = @NgayThucHien

	
	WHILE(@NgayThucHien <= @pEndDate)
	BEGIN
		
		--THUC HIEN DOI TRU THUC CHAY THEO NGAYTHUCHIEN
		EXEC [dbo].[ThucChay_Insert_GTTD_DoiTruGiam_ThucChayDaTinh_ByHD_Native_Ads] 
		@FromDate = @NgayThucHien,
		@ToDate = @NgayThucHien,
		@NgayGhiNhanThucChay = @NgayThucHien,
		@HopDongID = @HopDongID,
		@DmSanPhamREF = @DmSanPhamREF,
		@GhiChu = @GhiChu_DoiTruThucChay

		INSERT INTO [dbo].[ThucChay_Native_Ads_Temp]
           ([ThucChay_Native_AdsID]
           ,[SoHopDong]
           ,[TypeProduct]
           ,[DmSanPhamREF]
           ,[TenSanPham]
           ,[TenNhanHang]
           ,[DmNhanHangREF]
           ,[DmBannerID]
           ,[DmWebsiteID]
           ,[TenWebsite]
           ,[DmViTriBannerSanPhamID]
           ,[TenViTriBannerSanPham]
           ,[SoLuongThucChay]
           ,[SoLuongThucChayKM]
           ,[DonViTinh]
           ,[ThanhTienThucChaySauCK]
           ,[ThanhTienThucChayKM]
           ,[NgayThucHien]
           ,[CreatedAt]
           ,[CreatedBy]
           ,[LastModifiedAt]
           ,[LastModifiedBy]
           ,[DeletedStatus])

		SELECT  [ThucChay_Native_AdsID]
           ,[SoHopDong]
           ,[TypeProduct]
           ,[DmSanPhamREF]
           ,[TenSanPham]
           ,[TenNhanHang]
           ,[DmNhanHangREF]
           ,[DmBannerID]
           ,[DmWebsiteID]
           ,[TenWebsite]
           ,[DmViTriBannerSanPhamID]
           ,[TenViTriBannerSanPham]
           ,[SoLuongThucChay]
           ,[SoLuongThucChayKM]
           ,[DonViTinh]
           ,[ThanhTienThucChaySauCK]
           ,[ThanhTienThucChayKM]
           ,[NgayThucHien]
           ,[CreatedAt]
           ,[CreatedBy]
           ,[LastModifiedAt]
           ,[LastModifiedBy]
           ,[DeletedStatus] from dbo.ThucChay_Native_Ads
		WHERE CONVERT(DATE,NgayThucHien) = CONVERT(DATE,@NgayThucHien)
		AND [DmWebsiteID] <> 0
		AND SoHopDong = @SoHopDong
		AND DmSanPhamREF = @DmSanPhamREF

		--select * from [ThucChay_Native_Ads_Temp]
	

		DECLARE Record_Cursor CURSOR FOR 
		SELECT distinct A.SoHopDong, A.DmSanPhamREF, A.DmWebsiteID, A.TenWebsite, A.DmBannerID
		  FROM
			(
				SELECT tct.SoHopDong, tct.DmSanPhamREF, tct.DmWebsiteID, tct.TenWebsite, tct.DmBannerID
				FROM dbo.[ThucChay_Native_Ads_Temp] tct
				WHERE tct.SoHopDong = @SoHopDong
				AND tct.DmSanPhamREF = @DmSanPhamREF
			)A
		ORDER BY A.SoHopDong, A.DmSanPhamREF	

		OPEN Record_Cursor

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor into @SoHopDong, @DmSanPhamREF, @DmWebsiteREF, @TenWebsite, @DmBannerREF
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
				--TINH THUC CHAY CHO SAN PHAM NATIVE ADS
				SET @HopDongID = (SELECT TOP (1) hd.HopDongID FROM dbo.HopDong hd WHERE hd.SoHopDong = @SoHopDong ORDER BY hd.HopDongID)

				EXEC [dbo].[ThucChay_Insert_TinhLai_ThucChayDaTinh_ByHD_Native_Ads] 
					@NgayThucHien = @NgayThucHien,
					@SoHopDong = @SoHopDong,
					@HopDongID = @HopDongID,
					@DmSanPhamREF = @DmSanPhamREF,
					@DmWebsiteREF = @DmWebsiteREF, 
					@DmBannerID = @DmBannerREF,
					@GhiChu = @Ghichu_TinhLaiThucChay
			FETCH NEXT FROM Record_Cursor into @SoHopDong, @DmSanPhamREF, @DmWebsiteREF, @TenWebsite, @DmBannerREF
			END

		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor

		SET @NgayThucHien = DATEADD(d,1,@NgayThucHien)
		DELETE FROM dbo.ThucChay_Native_Ads_temp
	END 
	--CAP NHAT LAI THONG TIN NGAY THUC HIEN CHO GIA TRI DOI TRU, TINH LAI THUC CHAY
	UPDATE dbo.ThucChayDaTinh
	SET NgayThucHien = @pNgayGhiNhanThucChay
	WHERE HopDongID = @HopDongID
	AND DmSanPhamREF = @DmSanPhamREF
	AND CONVERT(DATE,CreatedAt) = CONVERT(DATE,GETDATE())
	AND (GhiChu = @GhiChu_DoiTruThucChay OR GhiChu = @Ghichu_TinhLaiThucChay)

	SELECT '1'
END


```
