# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinh_CPM_Native_Ads_BySoHopDongSanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2019-11-25 15:16:52.230000
- **Ngày sửa cuối**: 2022-07-06 15:52:29.450000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@pSoHopDong` | `nvarchar(100)` | No |
| `@pDmSanPhamREF` | `int(4)` | No |
| `@NgayGhiNhanThucChay` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================


CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinh_CPM_Native_Ads_BySoHopDongSanPham] 
	@StartDate datetime,
	@EndDate DATETIME,
	@pSoHopDong NVARCHAR(50),
	@pDmSanPhamREF INT,
	@NgayGhiNhanThucChay DATETIME
AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @Count INT =0
	DECLARE @SoHopDong NVARCHAR(50), @HopDongID INT, @DmSanPhamREF INT, @TenWebsite NVARCHAR(50), @DmWebsiteREF INT, @DmBannerREF INT
	SET @NgayThucHien = @StartDate
	SET @SoHopDong = @pSoHopDong

	DELETE FROM dbo.ThucChay_Native_Ads_Temp
	--Xoa du lieu ThucChayDaTinh truoc khi tinh

	DELETE FROM dbo.ThucChayDaTinh
	WHERE convert(date,NgayThucHien)BETWEEN @StartDate AND @EndDate
	AND DmSanPhamREF IN (821, 5133)
	AND NOT ( DmLoaiBannerREF IN (17,18)OR DmHinhThucQuangCao IN (13,42))
	AND DotChayHopDong <> N'NGAY'
	AND SoHopDong = @pSoHopDong
	AND DmSanPhamREF = @pDmSanPhamREF
	AND NOT EXISTS(SELECT top (1) iv.HopDongChiTietREF FROM DmThongTinHopDongBanInventory iv 
		WHERE iv.HopDongChiTietREF = HopDongChiTietREF
		ORDER BY iv.HopDongChiTietREF
	)

	WHILE(@NgayThucHien <= @EndDate)
	BEGIN
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
		WHERE 1=1
		and CONVERT(DATE,NgayThucHien) = CONVERT(DATE,@NgayThucHien)
		AND [DmWebsiteID] <> 0
		AND SoHopDong = @SoHopDong
		AND DmSanPhamREF = @pDmSanPhamREF


		--SELECT tct.SoHopDong, tct.DmSanPhamREF, tct.DmWebsiteID, tct.TenWebsite, tct.DmBannerID
		--		FROM dbo.[ThucChay_Native_Ads_Temp] tct

		--CAP NHAT THONG TIN BANNER NATIVE ADS
		EXEC [ThucChay_Insert_And_Update_HopDongChiTietAndBanner_Native_Ads] @NgayThucHien = @NgayThucHien
		--EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner_Native_Ads]
		EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner_Native_Ads_NgayThucHien]	@NgayThucHien = @NgayThucHien

		DECLARE Record_Cursor CURSOR FOR 
		SELECT distinct A.SoHopDong, A.DmSanPhamREF, A.DmWebsiteID, A.TenWebsite, A.DmBannerID
		  FROM
			(
				SELECT tct.SoHopDong, tct.DmSanPhamREF, tct.DmWebsiteID, tct.TenWebsite, tct.DmBannerID
				FROM dbo.[ThucChay_Native_Ads_Temp] tct
			)A
		ORDER BY A.SoHopDong, A.DmSanPhamREF	

		OPEN Record_Cursor

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor into @SoHopDong, @DmSanPhamREF, @DmWebsiteREF, @TenWebsite, @DmBannerREF
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
				--TINH THUC CHAY CHO SAN PHAM NATIVE ADS
				SET @HopDongID = (SELECT TOP (1) hd.HopDongID FROM dbo.HopDong hd WHERE hd.SoHopDong = @SoHopDong ORDER BY hd.HopDongID)
					--print 	 @NgayThucHien
					--print @SoHopDong
					--print @HopDongID
					--print @DmSanPhamREF
					--print @DmWebsiteREF
					--print @DmBannerREF
				EXEC [dbo].[ThucChay_InsertThucChayDaTinh_ByHD_Native_Ads] 
					@NgayThucHien = @NgayThucHien,
					@SoHopDong = @SoHopDong,
					@HopDongID = @HopDongID,
					@DmSanPhamREF = @DmSanPhamREF,
					@DmWebsiteREF = @DmWebsiteREF, 
					@DmBannerID = @DmBannerREF,
					@GhiChu = N'Tinh lai theo hopdong: ThucChay_ExcInsertThucChayDaTinh_CPM_Native_Ads_BySoHopDongSanPham'
			FETCH NEXT FROM Record_Cursor into @SoHopDong, @DmSanPhamREF, @DmWebsiteREF, @TenWebsite, @DmBannerREF
			END

		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor

		SET @NgayThucHien = DATEADD(d,1,@NgayThucHien)
		DELETE FROM dbo.ThucChay_Native_Ads_temp
	END 
	
	--CAP NHAP NGAY GHI NHAN THUC CHAY
	UPDATE dbo.ThucChayDaTinh
	SET NgayThucHien = @NgayGhiNhanThucChay
	WHERE SoHopDong = @pSoHopDong
	AND DmSanPhamREF = @pDmSanPhamREF
	AND CONVERT(DATE,CreatedAt) = CONVERT(DATE,GETDATE())
	AND NgayThucHien between @StartDate and @EndDate 
END


--EXEC [ThucChay_ExcInsertThucChayDaTinh] '2014-06-03','2014-06-03'

```
