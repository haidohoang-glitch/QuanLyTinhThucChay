# Stored Procedure: `ThucChay_TinhGiaTriThucChay_ThucChay_ThanhTien_Admatic_ByBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-08-04 16:13:18.867000
- **Ngày sửa cuối**: 2023-10-06 16:29:53.993000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(200)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@DmBannerREF` | `int(4)` | No |

## Definition (Source Code)

```sql
/*
EXEC [dbo].[ThucChay_TinhGiaTriThucChay_ThucChay_ThanhTien_Admatic_ByBanner_dev]
	@SoHopDong = N'QC0750621',
	@DmSanPhamREF = 140,
	@DmBannerREF = 576070
*/

CREATE PROCEDURE [dbo].[ThucChay_TinhGiaTriThucChay_ThucChay_ThanhTien_Admatic_ByBanner]
	@SoHopDong NVARCHAR(100),
	@DmSanPhamREF INT,
	@DmBannerREF INT
AS
BEGIN
	DECLARE @HopDongID INT, @DonViTinh NVARCHAR(50) = '', @ToDate DATETIME, @FromDate DATETIME, @NgayThucHienMax DATETIME
	SET @HopDongID = ISNULL((SELECT top (1) HopDongID FROM HopDong where SoHopDong = @SoHopDong order by HopDongID),0)
	SET @ToDate = CONVERT(date,DATEADD(DAY,-1,GETDATE()))
	
	IF(EXISTS(SELECT top (1) HopDongChiTietREF FROM ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic WHERE HopDongREF = @HopDongID
	AND DmSanPhamREF = @DmSanPhamREF
	AND DmHinhThucQuangCaoREF = 42
	and DmBannerREF = Convert(nvarchar(100), @DmBannerREF) order by HopDongChiTietREF))
	BEGIN
		--XAC DINH THOI GIAN MIN
		SET @FromDate = ISNULL((SELECT max(TC.NgayThucHienMax) FROM [dbo].[INFOBANNER_BRANDING_THANHTIEN_ADMATIC] TC WHERE TC.SOHOPDONG = @SoHopDong
					AND TC.DMSANPHAMREF = @DmSanPhamREF
					AND TC.DMBANNERREF = @DmBannerREF),'1900-01-01')

		SET @FromDate = DATEADD(DAY,1,@FromDate)

		IF(@DmSanPhamREF in (821,5133))
		BEGIN
			EXEC [dbo].[ThucChay_Insert_ThucChay_ThanhTien_Admatic_ByBanner_Native_OnImg]
			@SoHopDong = @SoHopDong,
			@DmSanPhamREF = @DmSanPhamREF,
			@DmBannerREF = @DmBannerREF,
			@FromDate = @FromDate,
			@ToDate = @ToDate
		END
		ELSE
		BEGIN
			--XAC DINH LOAI DON VI TINH
			SET @DonViTinh = ISNULL(
				(SELECT TOP (1) (CASE WHEN [LoaiDonGiaTheoDVT] = 1 THEN N'CPC'
				WHEN [LoaiDonGiaTheoDVT] IN (2,3) THEN N'CPM'
				WHEN [LoaiDonGiaTheoDVT] = 4 THEN N'TRUEVIEW'
				WHEN [LoaiDonGiaTheoDVT] = 5 THEN N'BÀI'
				ELSE N'CPM'
				END ) AS DONVITINH --1: CPC, 2,3: CPM, 4: trueview, 5: bài
			FROM [ABM_Data_ThucChay].[dbo].[AdmaticDonGiaBanner]
			WHERE  dmbannerid = @DmBannerREF ORDER BY [LoaiDonGiaTheoDVT]),''
			)
			IF(@DonViTinh = N'CPC' OR @DonViTinh = N'CPM' OR @DonViTinh = N'BÀI')
			BEGIN
				--TINH VA DAY DU LIEU THUC CHAY
				INSERT INTO [dbo].[ThucChay_ThanhTien_Admatic]
					   ([SoHopDong]
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

				SELECT tc.SoHopDong
				, tc.DmSanPhamREF AS TypeProduct
				, tc.DmSanPhamREF
				, tc.TenSanPham
				, tc.TenNhanHang
				, tc.DmNhanHangREF
				, tc.DmBannerREF
				, tc.DmWebsiteID
				, tc.TenWebsite
				, tc.DmViTriBannerSanPhamID
				, tc.TenViTriBannerSanPham
				, (CASE WHEN DGB.LoaiDonGiaTheoDVT = 1 AND DGB.ChietKhau <> 100  THEN tc.TongClickThucChay
					WHEN DGB.LoaiDonGiaTheoDVT IN (2,3) AND DGB.ChietKhau <> 100 THEN tc.TongViewThucChay
					WHEN DGB.LoaiDonGiaTheoDVT IN (5) AND DGB.ChietKhau <> 100 THEN 1
					ELSE 0
				END) AS SoLuongThucChay 
				, (CASE WHEN DGB.LoaiDonGiaTheoDVT = 1 AND DGB.ChietKhau = 100 THEN tc.TongClickThucChay
					WHEN DGB.LoaiDonGiaTheoDVT IN (2,3)  AND DGB.ChietKhau = 100 THEN tc.TongViewThucChay
					WHEN DGB.LoaiDonGiaTheoDVT IN (5)  AND DGB.ChietKhau = 100 THEN 1
					ELSE 0
				END) AS SoLuongThucChayKM
				, (CASE WHEN DGB.LoaiDonGiaTheoDVT = 1 THEN N'CLICK'
					WHEN DGB.LoaiDonGiaTheoDVT IN (2,3) THEN  N'VIEW'
					WHEN DGB.LoaiDonGiaTheoDVT IN (5) THEN  N'BÀI'
					ELSE  N'VIEW'
				END) AS DonViTinh
				,  (CASE WHEN DGB.LoaiDonGiaTheoDVT = 1 AND DGB.ChietKhau <> 100 THEN tc.TongClickThucChay*DGB.DonGiaBanner*(100-DGB.ChietKhau)/100
					WHEN DGB.LoaiDonGiaTheoDVT IN (2,3) AND DGB.ChietKhau <> 100 THEN tc.TongViewThucChay*(DGB.DonGiaBanner/1000)*(100-DGB.ChietKhau)/100
					WHEN DGB.LoaiDonGiaTheoDVT = 5 AND DGB.ChietKhau <> 100 THEN DGB.DonGiaBanner*(100-DGB.ChietKhau)/100
					ELSE 0
				END) AS ThanhTienThucChaySauCK_ChuaVAT 
				,(CASE WHEN DGB.LoaiDonGiaTheoDVT = 1 AND DGB.ChietKhau = 100 THEN tc.TongClickThucChay*DGB.DonGiaBanner
					WHEN DGB.LoaiDonGiaTheoDVT IN (2,3) AND DGB.ChietKhau = 100 THEN tc.TongViewThucChay*(DGB.DonGiaBanner/1000)
					WHEN DGB.LoaiDonGiaTheoDVT = 5 AND DGB.ChietKhau = 100 THEN DGB.DonGiaBanner
					ELSE 0
				END) AS ThanhTienThucChayKM 
				, tc.NgayThucHien
				, GETDATE() AS CreatedAt
				, N'asd_thucchay' AS CreatedBy
				, GETDATE() AS LastModifiedAt
				, N'asd_thucchay' as LastModifiedBy
				, 0 AS DELETEDSTATUS
				FROM 
				(
					SELECT tc.SoHopDong AS SoHopDong, isnull(dbo.GetProductIDByTypeProduct(tc.TypeProduct),0) AS DmSanPhamREF
					,N'' AS TenSanPham
					,N'' AS TenNhanHang
					,0 AS DmNhanHangREF
					, tc.DmBannerREF AS DmBannerREF
					, tc.DmWebsiteREF AS DmWebsiteID
					, tc.TenWebsite AS TenWebsite
					, 0 AS [DmViTriBannerSanPhamID] 
					, N'' AS  [TenViTriBannerSanPham]
					, tc.TongViewThucChay as TongViewThucChay
					, tc.TongClickThucChay as TongClickThucChay
					, tc.NgayThucHien as NgayThucHien FROM ThucChay tc
					WHERE tc.SoHopDong = @SoHopDong
					and tc.DmBannerREF = @DmBannerREF
					AND tc.NgayThucHien BETWEEN @FromDate AND @ToDate
				)TC
				INNER JOIN 
				(
					SELECT TT.HopDongREF, TT.HopDongChiTietREF, TT.DmBannerREF
					, DG.LoaiDonGiaTheoDVT , DG.DonGiaBanner, hdct.ChietKhau FROM

						(SELECT tt.HopDongREF, tt.HopDongChiTietREF, tt.DmBannerREF
						FROM ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic tt WHERE HopDongREF = @HopDongID
							AND tt.DmSanPhamREF = @DmSanPhamREF
							AND tt.DmHinhThucQuangCaoREF = 42
							and tt.DmBannerREF = Convert(nvarchar(100), @DmBannerREF)) tt
						INNER JOIN 
						(
							 SELECT distinct 
							 (CASE WHEN BannerDateCreate < '2023-07-01' THEN [DonGiaBanner_VAT]/1.1 
								ELSE [DonGiaBanner_VAT]/1.08
								end
							 )AS DonGiaBanner , dmbannerid
							 , [LoaiDonGiaTheoDVT] --1: CPC, 2,3: CPM, 4: trueview, 5: Bài
							FROM [ABM_Data_ThucChay].[dbo].[AdmaticDonGiaBanner]
							where dmbannerid = @DmBannerREF
						)DG ON tt.DmBannerREF = DG.dmbannerid
						INNER JOIN (SELECT hdct.HopDongChiTietID, hdct.ChietKhau
						 FROM HopDongChiTiet hdct WHERE hdct.HopDongFK = @HopDongID AND hdct.DmLoaiREF = 42
						 ) hdct ON hdct.HopDongChiTietID = tt.HopDongChiTietREF
				)DGB ON TC.DmBannerREF = DGB.DmBannerREF
			END
			ELSE
			IF(@DonViTinh = N'TRUEVIEW')
			BEGIN
							--TINH VA DAY DU LIEU THUC CHAY
						INSERT INTO [dbo].[ThucChay_ThanhTien_Admatic]
							   ([SoHopDong]
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

						SELECT tc.SoHopDong
						, tc.DmSanPhamREF AS TypeProduct
						, tc.DmSanPhamREF
						, tc.TenSanPham
						, tc.TenNhanHang
						, tc.DmNhanHangREF
						, tc.DmBannerREF
						, tc.DmWebsiteID
						, tc.TenWebsite
						, tc.DmViTriBannerSanPhamID
						, tc.TenViTriBannerSanPham
						, (CASE WHEN DGB.LoaiDonGiaTheoDVT IN (4) AND DGB.ChietKhau <> 100 THEN tc.TongViewThucChay
							WHEN DGB.LoaiDonGiaTheoDVT = 1 AND DGB.ChietKhau <> 100  THEN tc.TongClickThucChay
							WHEN DGB.LoaiDonGiaTheoDVT IN (2,3) AND DGB.ChietKhau <> 100 THEN tc.TongViewThucChay
							ELSE 0
						END) AS SoLuongThucChay 
						, (CASE WHEN DGB.LoaiDonGiaTheoDVT IN (4)  AND DGB.ChietKhau = 100 THEN tc.TongViewThucChay
							WHEN DGB.LoaiDonGiaTheoDVT = 1 AND DGB.ChietKhau = 100 THEN tc.TongClickThucChay
							WHEN DGB.LoaiDonGiaTheoDVT IN (2,3)  AND DGB.ChietKhau = 100 THEN tc.TongViewThucChay
							ELSE 0
						END) AS SoLuongThucChayKM
						, (CASE WHEN DGB.LoaiDonGiaTheoDVT IN (4) THEN  N'TRUEVIEW'
							WHEN DGB.LoaiDonGiaTheoDVT = 1 THEN N'CLICK'
							WHEN DGB.LoaiDonGiaTheoDVT IN (2,3) THEN  N'VIEW'
							ELSE  N''
						END) AS DonViTinh
						,  (CASE WHEN DGB.LoaiDonGiaTheoDVT IN (4) AND DGB.ChietKhau <> 100 THEN tc.TongViewThucChay*(DGB.DonGiaBanner)*(100-DGB.ChietKhau)/100
							WHEN DGB.LoaiDonGiaTheoDVT = 1 AND DGB.ChietKhau <> 100 THEN tc.TongClickThucChay*DGB.DonGiaBanner*(100-DGB.ChietKhau)/100
							WHEN DGB.LoaiDonGiaTheoDVT IN (2,3) AND DGB.ChietKhau <> 100 THEN tc.TongViewThucChay*(DGB.DonGiaBanner/1000)*(100-DGB.ChietKhau)/100
							ELSE tc.TongViewThucChay*(DGB.DonGiaBanner/1000)*(100-DGB.ChietKhau)/100
						END) AS ThanhTienThucChaySauCK_ChuaVAT 
						,(CASE WHEN DGB.LoaiDonGiaTheoDVT IN (4) AND DGB.ChietKhau = 100 THEN tc.TongViewThucChay*(DGB.DonGiaBanner)
							WHEN DGB.LoaiDonGiaTheoDVT = 1 AND DGB.ChietKhau = 100 THEN tc.TongClickThucChay*DGB.DonGiaBanner
							WHEN DGB.LoaiDonGiaTheoDVT IN (2,3) AND DGB.ChietKhau = 100 THEN tc.TongViewThucChay*(DGB.DonGiaBanner/1000)
							ELSE 0
						END) AS ThanhTienThucChayKM 
						, tc.NgayThucHien
						, GETDATE() AS CreatedAt
						, N'asd_thucchay' AS CreatedBy
						, GETDATE() AS LastModifiedAt
						, N'asd_thucchay' as LastModifiedBy
						, 0 AS DELETEDSTATUS
						FROM 
						(
							SELECT tc.SoHopDong AS SoHopDong, isnull(dbo.GetProductIDByTypeProduct(tc.TypeProduct),0) AS DmSanPhamREF
							,N'' AS TenSanPham
							,N'' AS TenNhanHang
							,0 AS DmNhanHangREF
							, tc.bannerid AS DmBannerREF
							, tc.SiteID AS DmWebsiteID
							, tc.SiteName AS TenWebsite
							, 0 AS [DmViTriBannerSanPhamID] 
							, N'' AS  [TenViTriBannerSanPham]
							, tc.True_View as TongViewThucChay
							, 0 as TongClickThucChay
							, tc.NgayThucHien as NgayThucHien FROM ThucChaytrueView tc
							WHERE tc.SoHopDong = @SoHopDong
							and tc.bannerid = @DmBannerREF
							AND tc.NgayThucHien BETWEEN @FromDate AND @ToDate
						)TC
						INNER JOIN 
						(
							SELECT TT.HopDongREF, TT.HopDongChiTietREF, TT.DmBannerREF
							, DG.LoaiDonGiaTheoDVT , DG.DonGiaBanner, hdct.ChietKhau FROM

								(SELECT tt.HopDongREF, tt.HopDongChiTietREF, tt.DmBannerREF
								FROM ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic tt WHERE HopDongREF = @HopDongID
									AND tt.DmSanPhamREF = @DmSanPhamREF
									AND tt.DmHinhThucQuangCaoREF = 42
									and tt.DmBannerREF = Convert(nvarchar(100), @DmBannerREF)) tt
								INNER JOIN 
								(
									 SELECT distinct 
									 (CASE WHEN BannerDateCreate < '2023-07-01' THEN [DonGiaBanner_VAT]/1.1 
								ELSE [DonGiaBanner_VAT]/1.08
								end
							 )AS DonGiaBanner , dmbannerid
									 , [LoaiDonGiaTheoDVT] --1: CPC, 2,3: CPM, 4: trueview
									FROM [ABM_Data_ThucChay].[dbo].[AdmaticDonGiaBanner]
									where dmbannerid = @DmBannerREF
								)DG ON tt.DmBannerREF = DG.dmbannerid
								INNER JOIN (SELECT hdct.HopDongChiTietID, hdct.ChietKhau
								 FROM HopDongChiTiet hdct WHERE hdct.HopDongFK = @HopDongID AND hdct.DmLoaiREF = 42
								 ) hdct ON hdct.HopDongChiTietID = tt.HopDongChiTietREF
						)DGB ON TC.DmBannerREF = DGB.DmBannerREF
			END
		END
		--XAC DINH NGAYTHUCHIEN MAX
		SET @NgayThucHienMax = ISNULL((
			SELECT MAX(NGAYTHUCHIEN) FROM ThucChay_ThanhTien_Admatic 
			WHERE SoHopDong = @SoHopDong
			AND DmSanPhamREF = @DmSanPhamREF
			AND DmBannerID = @DmBannerREF
		),'1900-01-01')

		--UPDATE NGAY THUC HIEN MAX
		UPDATE TC
		SET TC.NgayThucHienMax = @NgayThucHienMax
		FROM  [dbo].[INFOBANNER_BRANDING_THANHTIEN_ADMATIC] TC 
		WHERE TC.SOHOPDONG = @SoHopDong
		AND TC.DMSANPHAMREF = @DmSanPhamREF
		AND TC.DMBANNERREF = @DmBannerREF
	END
END

```
