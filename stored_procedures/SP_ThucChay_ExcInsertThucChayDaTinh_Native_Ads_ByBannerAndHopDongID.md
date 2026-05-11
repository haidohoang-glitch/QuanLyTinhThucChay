# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinh_Native_Ads_ByBannerAndHopDongID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-09 15:33:34.333000
- **Ngày sửa cuối**: 2021-06-09 15:34:41.773000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@NgayGhiNhanThucChay` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |
| `@DmBannerID` | `int(4)` | No |
| `@GhiChu` | `nvarchar(2000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================


CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinh_Native_Ads_ByBannerAndHopDongID] 
	@StartDate datetime,
	@EndDate datetime,
	@NgayGhiNhanThucChay DATETIME,
	@HopDongID int,
	@DmBannerID int,
	@GhiChu NVARCHAR(1000)
AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @Count INT =0
	DECLARE @SoHopDong NVARCHAR(50),  @DmSanPhamREF INT, @TenWebsite NVARCHAR(50), @DmWebsiteREF INT
	SET @NgayThucHien = convert(date,@NgayGhiNhanThucChay)
	SET @SoHopDong = (Select SoHopDong from HopDong where HopDongID = @HopDongID)
	DELETE FROM dbo.ThucChay_Native_Ads_Temp
	WHERE 1=1
	--Xoa du lieu ThucChayDaTinh truoc khi tinh

	--CHO NAY CAN CAN NHAC - HAIDH COMMENT
	DELETE FROM dbo.ThucChayDaTinh
	WHERE convert(date,NgayThucHien) = @NgayThucHien
	AND DmSanPhamREF IN (821, 5133)
	AND DmHinhThucQuangCao <> 42
	AND NOT ( DmLoaiBannerREF IN (17,18)OR DmHinhThucQuangCao IN (13))
	AND DotChayHopDong <> N'NGAY'
	and HopDongID = @HopDongID
	AND DmBannerREF = @DmBannerID

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
	SELECT 1 as [ThucChay_Native_AdsID]
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
		,@NgayThucHien AS NgayThucHien
        from dbo.ThucChay_Native_Ads
	WHERE CONVERT(DATE,NgayThucHien) BETWEEN Convert(date,@StartDate) AND Convert(date,@EndDate)
	AND DmBannerID = @DmBannerID
	AND [DmWebsiteID] <> 0
	and SoHopDong=@SoHopDong
	GROUP BY [SoHopDong]
        ,[TypeProduct]
        ,[DmSanPhamREF]
        ,[TenSanPham]
        ,[DmBannerID]
        ,[DmWebsiteID]
        ,[TenWebsite]
		 ,[DonViTinh]
	--CAP NHAT THONG TIN BANNER NATIVE ADS
	EXEC [ThucChay_Insert_And_Update_HopDongChiTietAndBanner_admatic_Native_Ads] @NgayThucHien = @NgayThucHien
	EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner_admatic_Native_Ads]

	DECLARE Record_Cursor_Banner CURSOR FOR 
	SELECT distinct A.SoHopDong, A.DmSanPhamREF, A.DmWebsiteID, A.TenWebsite, A.DmBannerID
		FROM
		(
			SELECT tct.SoHopDong, tct.DmSanPhamREF, tct.DmWebsiteID, tct.TenWebsite, tct.DmBannerID
			FROM dbo.[ThucChay_Native_Ads_Temp] tct
		)A
	ORDER BY A.SoHopDong, A.DmSanPhamREF	

	OPEN Record_Cursor_Banner

	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor_Banner into @SoHopDong, @DmSanPhamREF, @DmWebsiteREF, @TenWebsite, @DmBannerID
			
	WHILE @@FETCH_STATUS = 0
		BEGIN
			--TINH THUC CHAY CHO SAN PHAM NATIVE ADS
			SET @HopDongID = (SELECT TOP (1) hd.HopDongID FROM dbo.HopDong hd WHERE hd.SoHopDong = @SoHopDong ORDER BY hd.HopDongID)

			EXEC [dbo].[ThucChay_InsertThucChayDaTinh_ByHD_Native_Ads] 
				@NgayThucHien = @NgayThucHien,
				@SoHopDong = @SoHopDong,
				@HopDongID = @HopDongID,
				@DmSanPhamREF = @DmSanPhamREF,
				@DmWebsiteREF = @DmWebsiteREF, 
				@DmBannerID = @DmBannerID,
				@GhiChu = @GhiChu
		FETCH NEXT FROM Record_Cursor_Banner into @SoHopDong, @DmSanPhamREF, @DmWebsiteREF, @TenWebsite, @DmBannerID
		END

	CLOSE Record_Cursor_Banner
	DEALLOCATE Record_Cursor_Banner


	DELETE FROM dbo.ThucChay_Native_Ads_temp
	WHERE 1=1
	SELECT '1'
END


--EXEC [ThucChay_ExcInsertThucChayDaTinh] '2014-06-03','2014-06-03'

```
