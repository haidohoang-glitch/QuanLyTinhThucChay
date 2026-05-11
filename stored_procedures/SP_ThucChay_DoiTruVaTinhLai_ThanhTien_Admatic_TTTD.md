# Stored Procedure: `ThucChay_DoiTruVaTinhLai_ThanhTien_Admatic_TTTD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-04 17:44:29.777000
- **Ngày sửa cuối**: 2021-06-04 17:44:40.290000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@pSoHopDong` | `nvarchar(200)` | No |
| `@pHopDongChiTietID` | `int(4)` | No |
| `@pDmSanPhamREF` | `int(4)` | No |
| `@pStartDate` | `datetime(8)` | No |
| `@pEndDate` | `datetime(8)` | No |
| `@pNgayGhiNhanThucChay` | `datetime(8)` | No |
| `@GhiChu` | `nvarchar(1000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
EXEC [dbo].[ThucChay_DoiTruVaTinhLai_ThanhTien_Admatic] 
	'QC2110718',
	23455,
	821,
	'2018-07-18' ,
	'2018-07-29' ,
	@pNgayGhiNhanThucChay DATET
*/

CREATE PROCEDURE [dbo].[ThucChay_DoiTruVaTinhLai_ThanhTien_Admatic_TTTD] 
	@pSoHopDong NVARCHAR(100),
	@pHopDongChiTietID INT,
	@pDmSanPhamREF INT,
	@pStartDate datetime,
	@pEndDate DATETIME,
	@pNgayGhiNhanThucChay DATETIME,
	@GhiChu NVARCHAR(500)
AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @NgayDanhSoGioiHan DATETIME
	DECLARE @SoHopDong NVARCHAR(50), @HopDongID INT, @DmSanPhamREF INT, @HopDongChiTietID INT, @TenWebsite NVARCHAR(50), @DmWebsiteREF INT, @DmBannerREF INT
	DECLARE @GhiChu_DoiTruThucChay NVARCHAR(1000), @Ghichu_TinhLaiThucChay NVARCHAR(1000)

	SET @NgayDanhSoGioiHan = '2020-07-20'
	SET @SoHopDong = @pSoHopDong
	SET @DmSanPhamREF = @pDmSanPhamREF
	SET @HopDongChiTietID = @pHopDongChiTietID
	SET @HopDongID = (SELECT TOP (1) HopDongID FROM dbo.HopDong WHERE SoHopDong = @SoHopDong ORDER BY HopDongID)

	SET @GhiChu_DoiTruThucChay = N'Doi tru thuc chay thanhtien_admatic cho SoHopDong: ' + @SoHopDong + @GhiChu
	SET @Ghichu_TinhLaiThucChay = N'Tinh lai thuc chay thanhtien_admatic cho SoHopDong: ' + @SoHopDong + @GhiChu


	SET @NgayThucHien = convert(date,@pStartDate)

	DELETE FROM dbo.ThucChay_ThanhTien_Admatic_temp WHERE 1=1

	--CAP NHAT THONG TIN BANNER NATIVE ADS
	EXEC [ThucChay_Insert_And_Update_HopDongChiTietAndBanner_ThanhTien_Admatic] @NgayThucHien = @NgayThucHien
	EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner_ThanhTien_Admatic_NgayThucHien]	@NgayThucHien = @NgayThucHien

	
	WHILE(@NgayThucHien <= @pEndDate)
	BEGIN
		
		--THUC HIEN DOI TRU THUC CHAY THEO NGAYTHUCHIEN
		EXEC [dbo].[ThucChay_Insert_GTTD_DoiTruGiam_ThucChayDaTinh_ByHD_ThanhTien_Admatic] 
		@FromDate = @NgayThucHien,
		@ToDate = @NgayThucHien,
		@NgayGhiNhanThucChay = @NgayThucHien,
		@HopDongID = @HopDongID,
		@HopDongChiTietID = @HopDongChiTietID,
		@DmSanPhamREF = @DmSanPhamREF,
		@GhiChu = @GhiChu_DoiTruThucChay

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
		INNER JOIN (SELECT hd.* FROM dbo.HopDong hd 
						WHERE hd.TrangThaiHopDong NOT IN (0,3) 
						AND hd.NgayDanhSoHopDong >= @NgayDanhSoGioiHan 
						AND hd.SoHopDong = @SoHopDong
					) hd
		ON hd.SoHopDong = tc.SoHopDong
		WHERE CONVERT(DATE,tc.NgayThucHien) = CONVERT(DATE,@NgayThucHien)
		AND tc.[DmWebsiteID] <> 0

		
		DECLARE R_Cursor_TinhLai_Admatic CURSOR FOR 
		SELECT distinct A.SoHopDong, A.DmSanPhamREF, A.DmWebsiteID, A.TenWebsite, A.DmBannerID
		  FROM
			(
				SELECT TC.SoHopDong, TC.DmSanPhamREF, TC.DmWebsiteID, TC.TenWebsite, TC.DmBannerID 
				FROM 
				(SELECT tct.SoHopDong, tct.DmSanPhamREF, tct.DmWebsiteID, tct.TenWebsite, tct.DmBannerID
								FROM dbo.[ThucChay_ThanhTien_Admatic_temp] tct
								WHERE tct.SoHopDong = @SoHopDong
				)TC
				INNER JOIN 
				(	SELECT HopDongREF, HopDongChiTietREF, DmSanPhamREF , DmBannerREF as DmBannerID, TiLeThucChayHDCTSoVoiBanner 
					FROM dbo.ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic
					WHERE HopDongREF = @HopDongID
					AND HopDongChiTietREF = @HopDongChiTietID
					AND DeletedStatus = 0
				)tt ON CONVERT(NVARCHAR(100),tc.DmBannerID) = tt.DmBannerID
				WHERE 1=1 --THEM DK chi tinh khi san pham chay va treo trung nhau hoac sp hopdong = 733 haidh comment 24/11/2020
				AND EXISTS(SELECT TOP (1) hdct.HopDongChiTietID FROM dbo.HopDongChiTiet hdct 
					WHERE hdct.HopDongChiTietID = @HopDongChiTietID
					AND hdct.DmLoaiREF = 42
					AND hdct.DeletedStatus = 0
					AND NOT (hdct.DmLoaiREF = 42 AND hdct.DmLoaiNenTangREF = 9) --INVENTORY ADMAITC
					AND (hdct.DmSanPhamREF = 733 Or hdct.DmSanPhamREF = tc.DmSanPhamREF)
					Order BY hdct.HopDongChiTietID
				)
			)A
		ORDER BY A.SoHopDong, A.DmSanPhamREF	

		OPEN R_Cursor_TinhLai_Admatic

		-- Perform the first fetch.
		FETCH NEXT FROM R_Cursor_TinhLai_Admatic into @SoHopDong, @DmSanPhamREF, @DmWebsiteREF, @TenWebsite, @DmBannerREF
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
				--TINH THUC CHAY CHO SAN PHAM NATIVE ADS
				--print 'nhay vao day'
				SET @HopDongID = (SELECT TOP (1) hd.HopDongID FROM dbo.HopDong hd WHERE hd.SoHopDong = @SoHopDong ORDER BY hd.HopDongID)

				EXEC [dbo].[ThucChay_Insert_TinhLai_ThucChayDaTinh_ByHD_ThanhTien_Admatic] 
					@NgayThucHien = @NgayThucHien,
					@SoHopDong = @SoHopDong,
					@HopDongID = @HopDongID,
					@HopDongChiTietID = @HopDongChiTietID,
					@DmSanPhamREF = @DmSanPhamREF,
					@DmWebsiteREF = @DmWebsiteREF, 
					@DmBannerID = @DmBannerREF,
					@GhiChu = @Ghichu_TinhLaiThucChay
			FETCH NEXT FROM R_Cursor_TinhLai_Admatic into @SoHopDong, @DmSanPhamREF, @DmWebsiteREF, @TenWebsite, @DmBannerREF
			END

		CLOSE R_Cursor_TinhLai_Admatic
		DEALLOCATE R_Cursor_TinhLai_Admatic

		SET @NgayThucHien = DATEADD(d,1,@NgayThucHien)
		--DELETE FROM dbo.ThucChay_ThanhTien_Admatic_temp
	END 
	--CAP NHAT LAI THONG TIN NGAY THUC HIEN CHO GIA TRI DOI TRU, TINH LAI THUC CHAY
	UPDATE dbo.ThucChayDaTinh
	SET NgayThucHien = @pNgayGhiNhanThucChay
	WHERE HopDongID = @HopDongID
	AND HopDongChiTietREF = @pHopDongChiTietID
	AND CONVERT(DATE,CreatedAt) = CONVERT(DATE,GETDATE())
	AND (GhiChu = @GhiChu_DoiTruThucChay OR GhiChu = @Ghichu_TinhLaiThucChay)

	SELECT '1'
END


```
