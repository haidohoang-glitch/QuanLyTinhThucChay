# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinh_Admatic_Native_Ads`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-12-10 15:41:00.830000
- **Ngày sửa cuối**: 2020-11-19 17:24:42.590000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================


CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinh_Admatic_Native_Ads] 
	@StartDate datetime,
	@EndDate datetime
AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @Count INT =0
	DECLARE @SoHopDong NVARCHAR(50), @HopDongID INT, @DmSanPhamREF INT, @TenWebsite NVARCHAR(50), @DmWebsiteREF INT, @DmBannerREF INT
	DECLARE @NgayDanhSoGioiHan DATETIME = '2020-11-16'
	SET @NgayThucHien = @StartDate

	DELETE FROM dbo.ThucChay_Native_Ads_Temp
	WHERE 1=1
	--Xoa du lieu ThucChayDaTinh truoc khi tinh

	DELETE FROM dbo.ThucChayDaTinh
	WHERE convert(date,NgayThucHien)BETWEEN @StartDate AND @EndDate
	AND DmSanPhamREF IN (821, 5133)
	AND DmHinhThucQuangCao = 42
	AND NOT ( DmLoaiBannerREF IN (17,18)OR DmHinhThucQuangCao IN (13))
	AND DotChayHopDong <> N'NGAY'
	AND NgayDanhSoHopDong < @NgayDanhSoGioiHan
	AND HopdongID not in (1026983,1027978,1027386,1027184,1025262,1027928)

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

		SELECT  TC.[ThucChay_Native_AdsID]
           ,TC.[SoHopDong]
           ,TC.[TypeProduct]
           ,TC.[DmSanPhamREF]
           ,TC.[TenSanPham]
           ,TC.[TenNhanHang]
           ,TC.[DmNhanHangREF]
           ,TC.[DmBannerID]
           ,TC.[DmWebsiteID]
           ,TC.[TenWebsite]
           ,TC.[DmViTriBannerSanPhamID]
           ,TC.[TenViTriBannerSanPham]
           ,TC.[SoLuongThucChay]
           ,TC.[SoLuongThucChayKM]
           ,TC.[DonViTinh]
           ,TC.[ThanhTienThucChaySauCK]
           ,TC.[ThanhTienThucChayKM]
           ,TC.[NgayThucHien]
           ,TC.[CreatedAt]
           ,TC.[CreatedBy]
           ,TC.[LastModifiedAt]
           ,TC.[LastModifiedBy]
           ,TC.[DeletedStatus] from dbo.ThucChay_Native_Ads TC
		   INNER JOIN
		   (
			SELECT HD.SoHopDong FROM HopDong hd WHERE HD.NgayDanhSoHopDong < @NgayDanhSoGioiHan
		   ) HD ON HD.SoHopDong = TC.SoHopDong
		WHERE CONVERT(DATE,TC.NgayThucHien) = CONVERT(DATE,@NgayThucHien)
		AND TC.[DmWebsiteID] <> 0

		--CAP NHAT THONG TIN BANNER NATIVE ADS
		EXEC [ThucChay_Insert_And_Update_HopDongChiTietAndBanner_admatic_Native_Ads] @NgayThucHien = @NgayThucHien
		EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner_admatic_Native_Ads]

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

				EXEC [dbo].[ThucChay_InsertThucChayDaTinh_ByHD_Admatic_Native_Ads] 
					@NgayThucHien = @NgayThucHien,
					@SoHopDong = @SoHopDong,
					@HopDongID = @HopDongID,
					@DmSanPhamREF = @DmSanPhamREF,
					@DmWebsiteREF = @DmWebsiteREF, 
					@DmBannerID = @DmBannerREF,
					@GhiChu = ''
			FETCH NEXT FROM Record_Cursor into @SoHopDong, @DmSanPhamREF, @DmWebsiteREF, @TenWebsite, @DmBannerREF
			END

		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor

		SET @NgayThucHien = DATEADD(d,1,@NgayThucHien)

		DELETE FROM dbo.ThucChay_Native_Ads_temp
		WHERE 1=1
	END 
	
	SELECT '1'
END


--EXEC [ThucChay_ExcInsertThucChayDaTinh] '2014-06-03','2014-06-03'

```
