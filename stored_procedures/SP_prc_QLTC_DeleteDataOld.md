# Stored Procedure: `prc_QLTC_DeleteDataOld`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2023-07-05 15:56:56.360000
- **Ngày sửa cuối**: 2023-07-05 15:56:56.360000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |
| `@Contract` | `nvarchar(4000)` | No |
| `@Banner` | `nvarchar(4000)` | No |
| `@Product` | `int(4)` | No |
| `@Table` | `nvarchar(4000)` | No |
| `@UserId` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[prc_QLTC_DeleteDataOld]
	@FromDate Datetime = NULL,
	@ToDate Datetime = NULL,
	@Contract Nvarchar(2000) = '',
	@Banner Nvarchar(2000) = '',
	@Product Int = 0,
	@Table Nvarchar(2000) = '',
	@UserId Int = 0
AS
BEGIN
	SET NOCOUNT ON;

	If(@Table = N'DataThucChay_test' Or @Table = N'DataThucChay' Or @Table = N'Branding' Or @Table = N'Branding_Test') --Branding
		Begin
			Insert Into [dbo].[Data_Log_QLTC_Branding]([ThucChayID],[SoHopDong],[DanhsachDmBookingREF],[DmSanPhamREF],[TenSanPham],[DmNhomWebsiteREF],[TenNhomWebsite],
			[DmWebsiteREF],[TenWebsite],[DmChienDichREF],[TenChienDich],[DmBannerREF],[TenBanner],[NgayThucHien],[TongViewThucChay],[TongClickThucChay],[CreatedBy],
			[CreatedAt],[LastModifiedBy],[LastModifiedAt],[DeletedStatus],[PrintStatus],[RecordStatus],[TongSoBaiViet],[SoThuTuTheoNgay],[TypeProduct],[BannerType],
			[UserName],[SaleName],[Email],[LastTimeCalc],[sys_date],[IsReady],[ProductUnitID],[ProductUnitName],[BannerTypeName],[HopDongChiTietREF],[CampainStatus],
			[BannerStatus],[IsNoiBo],[Id_Delete],[CreatedByManipulation],[CreatedAtManipulation])
				Select [ThucChayID],[SoHopDong],[DanhsachDmBookingREF],[DmSanPhamREF],[TenSanPham],[DmNhomWebsiteREF],[TenNhomWebsite],[DmWebsiteREF],[TenWebsite],
				[DmChienDichREF],[TenChienDich],[DmBannerREF],[TenBanner],[NgayThucHien],[TongViewThucChay],[TongClickThucChay],[CreatedBy],[CreatedAt],
				[LastModifiedBy],[LastModifiedAt],[DeletedStatus],[PrintStatus],[RecordStatus],[TongSoBaiViet],[SoThuTuTheoNgay],[TypeProduct],[BannerType],
				[UserName],[SaleName],[Email],[LastTimeCalc],[sys_date],[IsReady],[ProductUnitID],[ProductUnitName],[BannerTypeName],[HopDongChiTietREF],
				[CampainStatus],[BannerStatus],[IsNoiBo],[ID] As Id_Delete, @UserId As CreatedByManipulation, GetDate() As CreatedAtManipulation
				From [dbo].[ThucChay]
				Where CAST(NgayThucHien AS DATE) >= CAST(@FromDate AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(@ToDate AS DATE)
				And (IsNull(@Contract, '') = '' Or SoHopDong In (Select Name From STRING_SPLIT_QLTC(@Contract)))
				And (IsNull(@Banner, '') = '' Or DmBannerREF In (Select Name From STRING_SPLIT_QLTC(@Banner)))
				And (IsNull(@Product, 0) = 0 Or DmSanPhamREF = @Product)

			DELETE FROM [dbo].[ThucChay] Where CAST(NgayThucHien AS DATE) >= CAST(@FromDate AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(@ToDate AS DATE)
				And (IsNull(@Contract, '') = '' Or SoHopDong In (Select Name From STRING_SPLIT_QLTC(@Contract)))
				And (IsNull(@Banner, '') = '' Or DmBannerREF In (Select Name From STRING_SPLIT_QLTC(@Banner)))
				And (IsNull(@Product, 0) = 0 Or DmSanPhamREF = @Product);
		End
	Else If(@Table = N'DataThucchay_Native_Ads_test' Or @Table = N'DataThucchay_Native_Ads') --Native Ads
		Begin
			Insert Into [dbo].[Data_Log_QLTC_Native_Ads]([ThucChay_Native_AdsID],[SoHopDong],[TypeProduct],[DmSanPhamREF],[TenSanPham],[TenNhanHang],[DmNhanHangREF],[DmBannerID],[DmWebsiteID],[TenWebsite],
				[DmViTriBannerSanPhamID],[TenViTriBannerSanPham],[SoLuongThucChay],[SoLuongThucChayKM],[DonViTinh],[ThanhTienThucChaySauCK],[ThanhTienThucChayKM],
				[NgayThucHien],[CreatedAt],[CreatedBy],[LastModifiedAt],[LastModifiedBy],[DeletedStatus], [CreatedByManipulation], [Id_Delete], [CreatedAtManipulation])
				Select [ThucChay_Native_AdsID],[SoHopDong],[TypeProduct],[DmSanPhamREF],[TenSanPham],[TenNhanHang],[DmNhanHangREF],[DmBannerID],[DmWebsiteID],[TenWebsite],
				[DmViTriBannerSanPhamID],[TenViTriBannerSanPham],[SoLuongThucChay],[SoLuongThucChayKM],[DonViTinh],[ThanhTienThucChaySauCK],[ThanhTienThucChayKM],
				[NgayThucHien],[CreatedAt],[CreatedBy],[LastModifiedAt],[LastModifiedBy],[DeletedStatus], @UserId As CreatedByManipulation, 1 As Id_Delete, GetDate() As CreatedAtManipulation
				From [dbo].[ThucChay_Native_Ads]
				Where CAST(NgayThucHien AS DATE) >= CAST(@FromDate AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(@ToDate AS DATE) 
				And (IsNull(@Contract, '') = '' Or SoHopDong In (Select Name From STRING_SPLIT_QLTC(@Contract)))
				And (IsNull(@Banner, '') = '' Or DmBannerID In (Select Name From STRING_SPLIT_QLTC(@Banner)))
				And (IsNull(@Product, 0) = 0 Or DmSanPhamREF = @Product);

			 Delete From [dbo].[ThucChay_Native_Ads]
				Where CAST(NgayThucHien AS DATE) >= CAST(@FromDate AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(@ToDate AS DATE)
				And (IsNull(@Contract, '') = '' Or SoHopDong In (Select Name From STRING_SPLIT_QLTC(@Contract)))
				And (IsNull(@Banner, '') = '' Or DmBannerID In (Select Name From STRING_SPLIT_QLTC(@Banner)))
				And (IsNull(@Product, 0) = 0 Or DmSanPhamREF = @Product);
		End
	Else If(@Table = N'DataThucchay_OnImageAds_test' Or @Table = N'DataThucchay_OnImageAds')--OnImage Ads
		Begin
			Insert Into [dbo].[Data_Log_QLTC_OnImage_Ads]([ThucChay_Native_AdsID],[SoHopDong],[TypeProduct],[DmSanPhamREF],[TenSanPham],[TenNhanHang],[DmNhanHangREF],[DmBannerID],[DmWebsiteID],[TenWebsite],
				[DmViTriBannerSanPhamID],[TenViTriBannerSanPham],[SoLuongThucChay],[SoLuongThucChayKM],[DonViTinh],[ThanhTienThucChaySauCK],[ThanhTienThucChayKM],
				[NgayThucHien],[CreatedAt],[CreatedBy],[LastModifiedAt],[LastModifiedBy],[DeletedStatus], [CreatedByManipulation], [Id_Delete], [CreatedAtManipulation])
				Select [ThucChay_Native_AdsID],[SoHopDong],[TypeProduct],[DmSanPhamREF],[TenSanPham],[TenNhanHang],[DmNhanHangREF],[DmBannerID],[DmWebsiteID],[TenWebsite],
				[DmViTriBannerSanPhamID],[TenViTriBannerSanPham],[SoLuongThucChay],[SoLuongThucChayKM],[DonViTinh],[ThanhTienThucChaySauCK],[ThanhTienThucChayKM],
				[NgayThucHien],[CreatedAt],[CreatedBy],[LastModifiedAt],[LastModifiedBy],[DeletedStatus], @UserId As CreatedByManipulation, 1 As Id_Delete, GetDate() As CreatedAtManipulation
				From [dbo].[ThucChay_Native_Ads]
				Where CAST(NgayThucHien AS DATE) >= CAST(@FromDate AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(@ToDate AS DATE) 
				And (IsNull(@Contract, '') = '' Or SoHopDong In (Select Name From STRING_SPLIT_QLTC(@Contract)))
				And (IsNull(@Banner, '') = '' Or DmBannerID In (Select Name From STRING_SPLIT_QLTC(@Banner)))
				And (IsNull(@Product, 0) = 0 Or DmSanPhamREF = @Product);

			 Delete From [dbo].[ThucChay_Native_Ads]
				Where CAST(NgayThucHien AS DATE) >= CAST(@FromDate AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(@ToDate AS DATE) 
				And (IsNull(@Contract, '') = '' Or SoHopDong In (Select Name From STRING_SPLIT_QLTC(@Contract)))
				And (IsNull(@Banner, '') = '' Or DmBannerID In (Select Name From STRING_SPLIT_QLTC(@Banner)))
				And (IsNull(@Product, 0) = 0 Or DmSanPhamREF = @Product);
		End
	Else If(@Table = N'DataThucChay_Admatic_v2_test' Or @Table = N'DataThucChay_Admatic_v2')--Admatic
		Begin
			 Insert Into [dbo].[Data_Log_QLTC_Admatic]([ThucChay_ThanhTien_AdmaticID],[SoHopDong],[TypeProduct],[DmSanPhamREF],[TenSanPham],[TenNhanHang],[DmNhanHangREF],[DmBannerID],[DmWebsiteID],[TenWebsite]
				,[DmViTriBannerSanPhamID],[TenViTriBannerSanPham],[SoLuongThucChay],[SoLuongThucChayKM],[DonViTinh],[ThanhTienThucChaySauCK_ChuaVAT],[ThanhTienThucChayKM]
				,[NgayThucHien],[CreatedAt],[CreatedBy],[LastModifiedAt],[LastModifiedBy],[DeletedStatus],[CreatedByManipulation],[Id_Delete],[CreatedAtManipulation])
				Select [ThucChay_ThanhTien_AdmaticID],[SoHopDong],[TypeProduct],[DmSanPhamREF],[TenSanPham],[TenNhanHang],[DmNhanHangREF],[DmBannerID],[DmWebsiteID],[TenWebsite]
				,[DmViTriBannerSanPhamID],[TenViTriBannerSanPham],[SoLuongThucChay],[SoLuongThucChayKM],[DonViTinh],[ThanhTienThucChaySauCK_ChuaVAT],[ThanhTienThucChayKM]
				,[NgayThucHien],[CreatedAt],[CreatedBy],[LastModifiedAt],[LastModifiedBy],[DeletedStatus], @UserId As CreatedByManipulation, 1 As Id_Delete, GetDate() As CreatedAtManipulation
				From [dbo].[ThucChay_ThanhTien_Admatic]
				Where CAST(NgayThucHien AS DATE) >= CAST(@FromDate AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(@ToDate AS DATE) 
				And (IsNull(@Contract, '') = '' Or SoHopDong In (Select Name From STRING_SPLIT_QLTC(@Contract)))
				And (IsNull(@Banner, '') = '' Or DmBannerID In (Select Name From STRING_SPLIT_QLTC(@Banner)))
				And (IsNull(@Product, 0) = 0 Or DmSanPhamREF = @Product);

			 Delete From [dbo].[ThucChay_ThanhTien_Admatic]
				Where CAST(NgayThucHien AS DATE) >= CAST(@FromDate AS DATE) AND CAST(NgayThucHien AS DATE) <= CAST(@ToDate AS DATE) 
				And (IsNull(@Contract, '') = '' Or SoHopDong In (Select Name From STRING_SPLIT_QLTC(@Contract)))
				And (IsNull(@Banner, '') = '' Or DmBannerID In (Select Name From STRING_SPLIT_QLTC(@Banner)))
				And (IsNull(@Product, 0) = 0 Or DmSanPhamREF = @Product);
		End
END

```
