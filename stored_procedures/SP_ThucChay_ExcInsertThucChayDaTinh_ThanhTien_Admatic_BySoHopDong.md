# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinh_ThanhTien_Admatic_BySoHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-07-29 17:42:07.757000
- **Ngày sửa cuối**: 2021-06-09 16:01:11.277000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

/*
EXEC [dbo].[ThucChay_ExcInsertThucChayDaTinh_ThanhTien_Admatic_BySoHopDong] '2020-07-07','2020-07-07'
*/

CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinh_ThanhTien_Admatic_BySoHopDong] 
	@StartDate datetime,
	@EndDate datetime,
	@SoHopDong nvarchar(50)
AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @Count INT =0
	DECLARE  @HopDongID INT, @DmSanPhamREF INT, @TenWebsite NVARCHAR(50), @DmWebsiteREF INT, @DmBannerREF INT
	, @NgayDanhSoGioiHan DATETIME 
	SET @NgayDanhSoGioiHan = '2020-01-01' --Thoi diem cac hop dong admatic dc ap dung tinh thuc chay theo cach moi (tinh theo do day tien)
	SET @NgayThucHien = @StartDate

	DELETE FROM dbo.[ThucChay_ThanhTien_Admatic_temp]
	--Xoa du lieu ThucChayDaTinh truoc khi tinh

	DELETE FROM dbo.ThucChayDaTinh
	WHERE convert(date,NgayThucHien)BETWEEN @StartDate AND @EndDate
	AND NOT ( DmLoaiBannerREF IN (17,18)OR DmHinhThucQuangCao IN (13))
	AND DmHinhThucQuangCao = 42
	AND NgayDanhSoHopDong >= @NgayDanhSoGioiHan
	AND DotChayHopDong = N'ThanhTien_Admatic'
	and SoHopDong = @SoHopDong

	WHILE(@NgayThucHien <= @EndDate)
	BEGIN
		INSERT INTO [dbo].[ThucChay_ThanhTien_Admatic_temp]
           ([ThucChay_ThanhTien_AdmaticID], [SoHopDong]
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
           ,[ThanhTienThucChaySauCK_ChuaVAT]
           ,[ThanhTienThucChayKM]
           ,[NgayThucHien]
           ,[CreatedAt]
           ,[CreatedBy]
           ,[LastModifiedAt]
           ,[LastModifiedBy]
           ,[DeletedStatus])
 

		SELECT tc.[ThucChay_ThanhTien_AdmaticID], tc.[SoHopDong]
           , tc.[TypeProduct]
           , tc.[DmSanPhamREF]
           , tc.[TenSanPham]
           , tc.[TenNhanHang]
           , tc.[DmNhanHangREF]
           , tc.[DmBannerID]
           , tc.[DmWebsiteID]
           , tc.[TenWebsite]
           , tc.[DmViTriBannerSanPhamID]
           , tc.[TenViTriBannerSanPham]
           , tc.[SoLuongThucChay]
           , tc.[SoLuongThucChayKM]
           , tc.[DonViTinh]
           , tc.[ThanhTienThucChaySauCK_ChuaVAT]
           , tc.[ThanhTienThucChayKM]
           , tc.[NgayThucHien]
           , tc.[CreatedAt]
           , tc.[CreatedBy]
           , tc.[LastModifiedAt]
           , tc.[LastModifiedBy]
           , tc.[DeletedStatus] from dbo.[ThucChay_ThanhTien_Admatic] tc
		INNER JOIN (SELECT hd.* FROM dbo.HopDong hd WHERE hd.TrangThaiHopDong NOT IN (0,3) AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan ) hd
		ON hd.SoHopDong = tc.SoHopDong
		WHERE CONVERT(DATE,tc.NgayThucHien) = CONVERT(DATE,@NgayThucHien)
		AND tc.[DmWebsiteID] <> 0
		and hd.SoHopDong = @SoHopDong

		--CAP NHAT THONG TIN BANNER NATIVE ADS
		EXEC [ThucChay_Insert_And_Update_HopDongChiTietAndBanner_ThanhTien_Admatic] @NgayThucHien = @NgayThucHien
		EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner_ThanhTien_Admatic]
		
		DECLARE Record_Cursor CURSOR FOR 
		SELECT distinct A.SoHopDong, A.DmSanPhamREF, A.DmWebsiteID, A.TenWebsite, A.DmBannerID
		  FROM
			(
				SELECT tct.SoHopDong, tct.DmSanPhamREF, tct.DmWebsiteID, tct.TenWebsite, tct.DmBannerID
				FROM dbo.[ThucChay_ThanhTien_Admatic_temp] tct
			)A
		ORDER BY A.SoHopDong, A.DmSanPhamREF	

		OPEN Record_Cursor

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor into @SoHopDong, @DmSanPhamREF, @DmWebsiteREF, @TenWebsite, @DmBannerREF
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
				--TINH THUC CHAY CHO NHOM SAN PHAM ADMATIC
				SET @HopDongID = (SELECT TOP (1) hd.HopDongID FROM dbo.HopDong hd WHERE hd.SoHopDong = @SoHopDong ORDER BY hd.HopDongID)

				
				EXEC [dbo].[ThucChay_InsertThucChayDaTinh_ByHD_ThanhTien_Admatic] 
					@NgayThucHien = @NgayThucHien,
					@SoHopDong = @SoHopDong,
					@HopDongID = @HopDongID,
					@DmSanPhamREF = @DmSanPhamREF,
					@DmWebsiteREF = @DmWebsiteREF, 
					@DmBannerID = @DmBannerREF,
					@GhiChu = N'Tính thưc chạy thanhtien_admatic'
			FETCH NEXT FROM Record_Cursor into @SoHopDong, @DmSanPhamREF, @DmWebsiteREF, @TenWebsite, @DmBannerREF
			END

		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor

		SET @NgayThucHien = DATEADD(d,1,@NgayThucHien)
		DELETE FROM dbo.[ThucChay_ThanhTien_Admatic_temp]
	END 
	
	SELECT '1'
END


```
