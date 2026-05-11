# Stored Procedure: `ThucChay_DoiTruVaTinhLai_CPM_Native_Ads_ByHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-07-07 11:15:12.017000
- **Ngày sửa cuối**: 2023-04-26 09:53:06.840000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@pSoHopDong` | `nvarchar(200)` | No |
| `@pHopDongChiTietID` | `int(4)` | No |
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

CREATE PROCEDURE [dbo].[ThucChay_DoiTruVaTinhLai_CPM_Native_Ads_ByHopDongChiTiet] 
	@pSoHopDong NVARCHAR(100),
	@pHopDongChiTietID INT,
	@pStartDate datetime,
	@pEndDate DATETIME,
	@pNgayGhiNhanThucChay DATETIME,
	@GhiChu	NVARCHAR(1000)
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	DECLARE @SoHopDong NVARCHAR(50), @HopDongID INT, @HopDongChiTietID INT, @DmSanPhamREF INT, @TenWebsite NVARCHAR(50), @DmWebsiteREF INT, @DmBannerREF INT
	DECLARE @GhiChu_DoiTruThucChay NVARCHAR(1000), @Ghichu_TinhLaiThucChay NVARCHAR(1000)

	SET @SoHopDong = @pSoHopDong
	SET @HopDongChiTietID = @pHopDongChiTietID
	SET @HopDongID = (SELECT TOP (1) HopDongID FROM dbo.HopDong WHERE SoHopDong = @SoHopDong ORDER BY HopDongID)

	SET @GhiChu_DoiTruThucChay = @GhiChu +  N', Doi tru thuc chay Native ads cho SoHopDong: ' + @SoHopDong
	SET @Ghichu_TinhLaiThucChay = @GhiChu + N', Tinh lai thuc chay Native ads cho SoHopDong: ' + @SoHopDong
	
	SET @pStartDate = CONVERT(DATE,@pStartDate)
	SET @pEndDate  = CONVERT(DATE,@pEndDate)
	SET @pNgayGhiNhanThucChay  = CONVERT(DATE,@pNgayGhiNhanThucChay)
	SET @NgayThucHien = @pNgayGhiNhanThucChay

	DELETE FROM dbo.ThucChay_Native_Ads_Temp
	WHERE 1=1

	--CAP NHAT THONG TIN BANNER NATIVE ADS
	EXEC [ThucChay_Insert_And_Update_HopDongChiTietAndBanner_Native_Ads] @NgayThucHien = @pStartDate
	EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner_Native_Ads_NgayThucHien] @NgayThucHien = @NgayThucHien

	--THUC HIEN DOI TRU THUC CHAY THEO NGAYTHUCHIEN
	EXEC [dbo].[ThucChay_Insert_GTTD_DoiTruGiam_ThucChayDaTinh_ByHopDongChiTiet_Native_Ads] 
	@FromDate = @pStartDate,
	@ToDate = @pEndDate,
	@NgayGhiNhanThucChay = @NgayThucHien,
	@HopDongID  = @HopDongID,
	@HopDongChiTietID = @HopDongChiTietID,
	@GhiChu = @GhiChu_DoiTruThucChay

	INSERT INTO [dbo].[ThucChay_Native_Ads_Temp]
        ([ThucChay_Native_AdsID]
        ,[SoHopDong]
        ,[TypeProduct]
        ,[DmSanPhamREF]
        ,[TenSanPham]
        ,[DmBannerID]
        ,[DmWebsiteID]
        ,[TenWebsite]
        ,[SoLuongThucChay]
        ,[SoLuongThucChayKM]
        ,[DonViTinh]
        ,[ThanhTienThucChaySauCK]
        ,[ThanhTienThucChayKM]
        ,[NgayThucHien]
       )

	SELECT  0 [ThucChay_Native_AdsID]
        ,[SoHopDong]
        ,[TypeProduct]
        ,[DmSanPhamREF]
        ,[TenSanPham]
        ,[DmBannerID]
        ,[DmWebsiteID]
        ,[TenWebsite]
        ,SUM([SoLuongThucChay]) AS [SoLuongThucChay]
        ,SUM([SoLuongThucChayKM]) AS [SoLuongThucChayKM]
        ,[DonViTinh]
        ,SUM([ThanhTienThucChaySauCK]) AS [ThanhTienThucChaySauCK]
        ,SUM([ThanhTienThucChayKM]) AS [ThanhTienThucChayKM]
        ,@NgayThucHien AS [NgayThucHien]
        FROM dbo.ThucChay_Native_Ads
	WHERE CONVERT(DATE,NgayThucHien) BETWEEN @pStartDate AND @pEndDate
	AND [DmWebsiteID] <> 0
	AND SoHopDong = @SoHopDong
	--AND DmSanPhamREF = @DmSanPhamREF
	GROUP BY [SoHopDong]
        ,[TypeProduct]
        ,[DmSanPhamREF]
        ,[TenSanPham]
        ,[DmBannerID]
        ,[DmWebsiteID]
        ,[TenWebsite]
		,[DonViTinh]

	

	DECLARE Record_Cursor CURSOR FOR 
	SELECT distinct A.SoHopDong, A.DmSanPhamREF, A.DmWebsiteID, A.TenWebsite, A.DmBannerID
		FROM
		(
			SELECT tct.SoHopDong, tct.DmSanPhamREF, tct.DmWebsiteID, tct.TenWebsite, tct.DmBannerID
			FROM dbo.[ThucChay_Native_Ads_Temp] tct
			WHERE tct.SoHopDong = @SoHopDong
			
		)A
		INNER JOIN 
		(	SELECT distinct HopDongREF, HopDongChiTietREF, DmSanPhamID, DmBannerID, TiLeThucChayHDCTSoVoiBanner 
			FROM dbo.ThucChayHopDongChiTietAndBanner_Native_Ads 
			WHERE HopDongREF = @HopDongID
			AND HopDongChiTietREF = @HopDongChiTietID
			AND DeletedStatus = 0
		)tt ON CONVERT(NVARCHAR(100),A.DmBannerID) = tt.DmBannerID AND A.DmSanPhamREF = tt.DmSanPhamID
	ORDER BY A.SoHopDong, A.DmSanPhamREF	

	OPEN Record_Cursor

	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor into @SoHopDong, @DmSanPhamREF, @DmWebsiteREF, @TenWebsite, @DmBannerREF
			
	WHILE @@FETCH_STATUS = 0
		BEGIN
			--TINH THUC CHAY CHO SAN PHAM NATIVE ADS
			SET @HopDongID = (SELECT TOP (1) hd.HopDongID FROM dbo.HopDong hd WHERE hd.SoHopDong = @SoHopDong ORDER BY hd.HopDongID)

			--EXEC [dbo].[ThucChay_Insert_TinhLai_ThucChayDaTinh_ByHD_Native_Ads] 
			--	@NgayThucHien = @NgayThucHien,
			--	@SoHopDong = @SoHopDong,
			--	@HopDongID = @HopDongID,
			--	@DmSanPhamREF = @DmSanPhamREF,
			--	@DmWebsiteREF = @DmWebsiteREF, 
			--	@DmBannerID = @DmBannerREF,
			--	@GhiChu = @Ghichu_TinhLaiThucChay

			EXEC [dbo].[ThucChay_Insert_TinhLai_ThucChayDaTinh_ByHopDongChiTiet_Native_Ads] 
			@NgayThucHien = @NgayThucHien,
			@SoHopDong = @SoHopDong,
			@HopDongID = @HopDongID,
			@HopDongChiTietID = @HopDongChiTietID,
			@DmSanPhamREF = @DmSanPhamREF,
			@DmWebsiteREF = @DmWebsiteREF, 
			@DmBannerID = @DmBannerREF,
			@GhiChu = @Ghichu_TinhLaiThucChay

		FETCH NEXT FROM Record_Cursor into @SoHopDong, @DmSanPhamREF, @DmWebsiteREF, @TenWebsite, @DmBannerREF
		END

	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor

	DELETE FROM dbo.ThucChay_Native_Ads_temp

END


```
