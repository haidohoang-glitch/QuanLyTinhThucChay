# Stored Procedure: `prc_QLTC_InsertDataNew`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2023-07-05 15:56:56.393000
- **Ngày sửa cuối**: 2025-03-06 13:58:02.853000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |
| `@Contract` | `nvarchar(4000)` | No |
| `@Banner` | `nvarchar(4000)` | No |
| `@Product` | `int(4)` | No |
| `@Table` | `nvarchar(4000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[prc_QLTC_InsertDataNew]
	@FromDate Datetime = NULL,
	@ToDate Datetime = NULL,
	@Contract Nvarchar(2000) = '',
	@Banner Nvarchar(2000) = '',
	@Product Int = 0,
	@Table Nvarchar(2000) = ''
AS
BEGIN
	SET NOCOUNT ON;

	If(@Table = N'DataThucChay_test' Or @Table = N'DataThucChay' Or @Table = N'Branding' Or @Table = N'Branding_Test') --Branding
		BEGIN
			INSERT INTO [dbo].[ThucChay](ThucChayID , SoHopDong, DanhsachDmBookingREF, DmSanPhamREF, TenSanPham, DmNhomWebsiteREF,
						TenNhomWebsite, DmWebsiteREF, TenWebsite, DmChienDichREF, TenChienDich, DmBannerREF, TenBanner, NgayThucHien,
						TongViewThucChay, TongClickThucChay, CreatedBy, CreatedAt, LastModifiedBy,LastModifiedAt,  DeletedStatus,
						PrintStatus,  RecordStatus, TongSoBaiViet, SoThuTuTheoNgay, TypeProduct, BannerType, UserName, SaleName,
						Email, LastTimeCalc, sys_date, IsReady, ProductUnitID, ProductUnitName, BannerTypeName, HopDongChiTietREF,
						CampainStatus, BannerStatus, IsNoiBo)
				SELECT ThucChayID, SoHopDong, DanhsachDmBookingREF, DmSanPhamREF, TenSanPham, DmNhomWebsiteREF, TenNhomWebsite,
						ISNULL([dbo].[GetWebsiteIDByDomainName](TenWebsite), 0), TenWebsite, DmChienDichREF, TenChienDich, DmBannerREF
						, TenBanner, NgayThucHien, TongViewThucChay, TongClickThucChay, N'From API', createdAt, N'From API', createdAt
						, 0, 0, 0, TongSoBaiViet, SoThuTuTheoNgay, TypeProduct, BannerType, UserName, SaleName, Email, LastTimeCalc, 
						sys_date, IsReady, ProductUnitID, ProductUnitName, BannerTypeName, HopDongChiTietREF, CampainStatus, BannerStatus
						, (CASE WHEN IsNoiBo = N'True' THEN 1
								WHEN IsNoiBo = N'False' THEN 0
								ELSE NULL
						END) AS'IsNoiBo'
				FROM [dbo].[DataThucChay_test]
				WHERE CAST(NgayThucHien AS DATE) >= CAST(@FromDate AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(@ToDate AS DATE)
				AND (ISNULL(@Contract, '') = '' OR SoHopDong IN (SELECT Name FROM STRING_SPLIT_QLTC(@Contract)))
				AND (ISNULL(@Banner, '') = '' OR DmBannerREF IN (SELECT Name FROM STRING_SPLIT_QLTC(@Banner)))
				AND (ISNULL(@Product, 0) = 0 OR DmSanPhamREF = @Product)
		END
	ELSE IF(@Table = N'DataThucchay_Native_Ads_test' OR @Table = N'DataThucchay_Native_Ads') --Native Ads
		BEGIN
			 INSERT INTO [dbo].[ThucChay_Native_Ads](ThucChay_Native_AdsID, SoHopDong, TypeProduct, DmSanPhamREF, TenSanPham, TenNhanHang, DmNhanHangREF, DmBannerID, DmWebsiteID,
				TenWebsite, DmViTriBannerSanPhamID, TenViTriBannerSanPham, SoLuongThucChay, SoLuongThucChayKM, DonViTinh, ThanhTienThucChaySauCK,
				ThanhTienThucChayKM, NgayThucHien, CreatedAt, CreatedBy, LastModifiedAt, LastModifiedBy, DeletedStatus)
				SELECT 0 ThuChay_Native_ads_ID,[SoHopDong],CONVERT(INT,[TypeProduct]) AS [TypeProduct],[dbo].[GetProductIDByTypeProduct](TypeProduct) AS DmSanPhamREF,
				[TenSanPham],[TenNhanHang],CONVERT(INT,ISNULL([NhanHangID],0)) AS [NhanHangID],CONVERT(INT,ISNULL([DmBannerID],0)) AS [DmBannerID],
				ISNULL(dbo.GetWebsiteIDByDomainName(TenWebsite),0) AS [DmWebsiteID],[TenWebsite],CONVERT(INT,ISNULL([DmViTriREF],0)) AS [DmViTriREF],
				[TenViTri],CONVERT(BIGINT,ISNULL([SoLuongThucChay],0)) AS [SoLuongThucChay],
				CONVERT(BIGINT,ISNULL([SoLuongThucChayKhuyenMai],0)) AS  [SoLuongThucChayKhuyenMai],[DonViTinh],
				--CONVERT(FLOAT,ISNULL([ThanhTienThucChay],0))/1.1 AS [ThanhTienThucChay_TruocVAT], --thay bang dong duoi
				(CASE WHEN (NgayThucHien >= '2022-04-01') AND (NgayThucHien < '2023-01-01') THEN CONVERT(FLOAT,ISNULL([ThanhTienThucChay],0))/1.08
						WHEN (NgayThucHien >= '2023-07-01') THEN CONVERT(FLOAT,ISNULL([ThanhTienThucChay],0))/(1+CONVERT(FLOAT,ISNULL(vat,0))/100 ) -- tu ngay 01-07-2023 Tinh theo VAT san pham tra --Duongnt add	01-07-2023															
						ELSE CONVERT(FLOAT,ISNULL([ThanhTienThucChay],0))/1.1
					END) AS [ThanhTienThucChay_TruocVAT],
				--CONVERT(FLOAT,ISNULL([ThanhTienThucChaykhuyenMai],0))/1.1 AS [ThanhTienThucChaykhuyenMai_TruocVAT], --thay bang dong duoi
				(CASE WHEN (NgayThucHien >= '2022-04-01') AND (NgayThucHien < '2023-01-01') THEN CONVERT(FLOAT,ISNULL(ThanhTienThucChaykhuyenMai,0))/1.08
						WHEN (NgayThucHien >= '2023-07-01') THEN CONVERT(FLOAT,ISNULL(ThanhTienThucChaykhuyenMai,0))/(1+CONVERT(FLOAT,ISNULL(vat,0))/100 ) -- tu ngay 01-07-2023 Tinh theo VAT san pham tra --Duongnt add	01-07-2023															
						ELSE CONVERT(FLOAT,ISNULL(ThanhTienThucChaykhuyenMai,0))/1.1
					END) AS [ThanhTienThucChaykhuyenMai_TruocVAT],
				[NgayThucHien],
				GETDATE() AS [createdAt], [createdBy] , GETDATE() AS LastModifiedAt, [createdBy] AS LastModifiedBy, 0 AS DeletedStatus
				FROM [dbo].[DataThucchay_Native_Ads_test]
				WHERE CAST(NgayThucHien AS DATE) >= CAST(@FromDate AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(@ToDate AS DATE)
				AND (ISNULL(@Contract, '') = '' OR SoHopDong IN (SELECT Name FROM STRING_SPLIT_QLTC(@Contract)))
				AND (ISNULL(@Banner, '') = '' OR DmBannerID IN (SELECT Name FROM STRING_SPLIT_QLTC(@Banner)))
				AND CONVERT(INT,[TypeProduct]) = 19
		END
	ELSE IF(@Table = N'DataThucchay_OnImageAds_test' OR @Table = N'DataThucchay_OnImageAds')--OnImage Ads
		BEGIN
			 Insert Into [dbo].[ThucChay_Native_Ads](ThucChay_Native_AdsID, SoHopDong, TypeProduct, DmSanPhamREF, TenSanPham, TenNhanHang, DmNhanHangREF, DmBannerID,
				DmWebsiteID, TenWebsite, DmViTriBannerSanPhamID, TenViTriBannerSanPham, SoLuongThucChay, SoLuongThucChayKM, DonViTinh,
				ThanhTienThucChaySauCK, ThanhTienThucChayKM, NgayThucHien, CreatedAt, CreatedBy, LastModifiedAt, LastModifiedBy, DeletedStatus)
				Select 0 ThuChay_Native_ads_ID,[SoHopDong], CONVERT(INT,[TypeProduct]) AS [TypeProduct], CONVERT(INT,[TypeProduct]) AS [TypeProduct],[TenSanPham],
				[TenNhanHang], CONVERT(INT,ISNULL([NhanHangID],0)) AS [NhanHangID], CONVERT(INT,ISNULL([DmBannerID],0)) AS [DmBannerID],
				ISNULL(dbo.GetWebsiteIDByDomainName(TenWebsite),0) AS [DmWebsiteID], [TenWebsite], CONVERT(INT,ISNULL([DmViTriREF],0)) AS [DmViTriREF],
				[TenViTri],CONVERT(BIGINT,ISNULL([SoLuongThucChay],0)) AS [SoLuongThucChay],
				CONVERT(BIGINT,ISNULL([SoLuongThucChayKhuyenMai],0)) AS  [SoLuongThucChayKhuyenMai], [DonViTinh],
				--CONVERT(FLOAT,ISNULL([ThanhTienThucChay],0))/1.1 AS [ThanhTienThucChay_TruocVAT],
				(CASE WHEN (NgayThucHien >= '2022-04-01') AND (NgayThucHien < '2023-01-01') THEN CONVERT(FLOAT,ISNULL([ThanhTienThucChay],0))/1.08
						WHEN (NgayThucHien >= '2023-07-01') THEN CONVERT(FLOAT,ISNULL([ThanhTienThucChay],0))/(1+CONVERT(FLOAT,ISNULL(vat,0))/100 ) -- tu ngay 01-07-2023 Tinh theo VAT san pham tra --Duongnt add	01-07-2023															
						ELSE CONVERT(FLOAT,ISNULL([ThanhTienThucChay],0))/1.1
					END) AS [ThanhTienThucChay_TruocVAT],

				--CONVERT(FLOAT,ISNULL([ThanhTienThucChaykhuyenMai],0))/1.1 AS [ThanhTienThucChaykhuyenMai_TruocVAT],
				(CASE WHEN (NgayThucHien >= '2022-04-01') AND (NgayThucHien < '2023-01-01') THEN CONVERT(FLOAT,ISNULL(ThanhTienThucChaykhuyenMai,0))/1.08
						WHEN (NgayThucHien >= '2023-07-01') THEN CONVERT(FLOAT,ISNULL(ThanhTienThucChaykhuyenMai,0))/(1+CONVERT(FLOAT,ISNULL(vat,0))/100 ) -- tu ngay 01-07-2023 Tinh theo VAT san pham tra --Duongnt add	01-07-2023															
						ELSE CONVERT(FLOAT,ISNULL(ThanhTienThucChaykhuyenMai,0))/1.1
					END) AS [ThanhTienThucChaykhuyenMai_TruocVAT],

				[NgayThucHien], GETDATE() AS [createdAt], [createdBy] , GETDATE() AS LastModifiedAt, [createdBy] AS LastModifiedBy, 0 AS DeletedStatus
				From [dbo].[DataThucchay_OnImageAds_test]
				Where CAST(NgayThucHien AS DATE) >= CAST(@FromDate AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(@ToDate AS DATE)
				And (IsNull(@Contract, '') = '' Or SoHopDong In (Select Name From STRING_SPLIT_QLTC(@Contract)))
				And (IsNull(@Banner, '') = '' Or DmBannerID In (Select Name From STRING_SPLIT_QLTC(@Banner)))
				And CONVERT(INT,[TypeProduct]) = 5133
		End
	Else If(@Table = N'DataThucChay_Admatic_v2_test' Or @Table = N'DataThucChay_Admatic_v2')--Admatic
		Begin
			 Insert Into [dbo].[ThucChay_ThanhTien_Admatic](SoHopDong, TypeProduct, DmSanPhamREF, TenSanPham, TenNhanHang, DmNhanHangREF, DmBannerID, DmWebsiteID, TenWebsite, 
				DmViTriBannerSanPhamID, TenViTriBannerSanPham, SoLuongThucChay, SoLuongThucChayKM, DonViTinh, [ThanhTienThucChaySauCK_ChuaVAT], 
				ThanhTienThucChayKM, NgayThucHien, CreatedAt, CreatedBy, LastModifiedAt, LastModifiedBy, DeletedStatus)
				Select contract_number AS [SoHopDong]
					  ,CONVERT(INT,DmSanPhamREF) AS [TypeProduct]
					  ,CONVERT(INT,DmSanPhamREF) AS DmSanPhamREF
					  ,[TenSanPham]
					  ,NhanHang
					  ,CONVERT(INT,ISNULL(NhanHangID,0)) AS [NhanHangID]
					  ,CONVERT(INT,ISNULL(banner_id,0)) AS [DmBannerID]
					  ,ISNULL(dbo.GetWebsiteIDByDomainName(domain_name),0) AS [DmWebsiteID]
					 ,domain_name AS [TenWebsite]
					  ,CONVERT(INT,ISNULL(DmViTriREF,0)) AS [DmViTriREF]
					  ,TenViTri
					  ,(CASE WHEN ProductUnitName = N'CPM' AND ((CONVERT(FLOAT,domain_tt_money)  <> 0 AND CONVERT(FLOAT,domain_tt_promotion) = 0) 
																OR (CONVERT(FLOAT,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) <> 0))   
							THEN  CONVERT(BIGINT,ISNULL(domain_tt_view,0)) 
						WHEN ProductUnitName = N'CPC' and ((convert(float,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) = 0)  
														or (convert(float,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) <> 0))
							THEN CONVERT(BIGINT,ISNULL(domain_tt_click,0)) 
						WHEN ProductUnitName = N'TRUEVIEW' and ((convert(float,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) = 0)   
														or (convert(float,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) <> 0))
							THEN  CONVERT(BIGINT,ISNULL(domain_tt_view,0)) 
						WHEN ProductUnitName = N'TRUE VIEW' and ((convert(float,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) = 0)
														or   (convert(float,domain_tt_money)  <> 0 and convert(float,domain_tt_promotion) <> 0) )
							THEN  CONVERT(BIGINT,ISNULL(domain_tt_view,0)) 
						ELSE 0--CONVERT(BIGINT,ISNULL(domain_tt_view,0)) --tuyetnta cf
					  END ) AS [SoLuongThucChay]
					  ,(CASE WHEN ProductUnitName = N'CPM' and (convert(float,domain_tt_money)  = 0 and convert(float,domain_tt_promotion) <> 0) THEN  CONVERT(BIGINT,ISNULL(domain_tt_view,0)) 
						WHEN ProductUnitName = N'CPC' and (convert(float,domain_tt_money)  = 0 and convert(float,domain_tt_promotion) <> 0) THEN CONVERT(BIGINT,ISNULL(domain_tt_click,0)) 
						WHEN ProductUnitName = N'TRUEVIEW' and (convert(float,domain_tt_money)  = 0 and convert(float,domain_tt_promotion) <> 0) THEN  CONVERT(BIGINT,ISNULL(domain_tt_view,0)) 
						WHEN ProductUnitName = N'TRUE VIEW' and (convert(float,domain_tt_money)  = 0 and convert(float,domain_tt_promotion) <> 0) THEN  CONVERT(BIGINT,ISNULL(domain_tt_view,0)) 
						ELSE 0
					  END ) AS  [SoLuongThucChayKhuyenMai]
					  ,(CASE WHEN ProductUnitName =  N'CPM' THEN N'VIEW'
						WHEN ProductUnitName = N'CPC' THEN N'CLICK'
						WHEN ProductUnitName =  N'TRUEVIEW' THEN N'TRUE VIEW'
						WHEN ProductUnitName =  N'TRUE VIEW' THEN N'TRUE VIEW'
						ELSE N''
					  END) AS [DonViTinh]
					  --domain_tt_money da bao gom chietkhau va sau VAT
					  ,CONVERT(FLOAT,ISNULL(domain_tt_money,0))/(1+CONVERT(FLOAT,vat)/100) AS [ThanhTienThucChaySauCK_ChuaVAT]					   
					  ,CONVERT(FLOAT,ISNULL(domain_tt_promotion,0))/(1+CONVERT(FLOAT,vat)/100) AS [ThanhTienThucChayKM]
					  ,[NgayThucHien]
					  , GETDATE() AS [createdAt]
					  , [createdBy] 
					  , GETDATE() AS LastModifiedAt
					  , [createdBy] AS LastModifiedBy
					  , 0 AS DeletedStatus
				From [dbo].[DataThucChay_Admatic_v2_test]
				Where CAST(NgayThucHien AS DATE) >= CAST(@FromDate AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(@ToDate AS DATE)
				And (IsNull(@Contract, '') = '' Or contract_number In (Select Name From STRING_SPLIT_QLTC(@Contract)))
				And (IsNull(@Banner, '') = '' Or banner_id In (Select Name From STRING_SPLIT_QLTC(@Banner)))
				And (IsNull(@Product, 0) = 0 Or DmSanPhamREF = @Product)
		End
END

```
