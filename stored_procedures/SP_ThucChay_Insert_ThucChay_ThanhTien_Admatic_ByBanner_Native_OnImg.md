# Stored Procedure: `ThucChay_Insert_ThucChay_ThanhTien_Admatic_ByBanner_Native_OnImg`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-12-02 16:51:59.550000
- **Ngày sửa cuối**: 2024-12-16 15:30:50.197000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(200)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@DmBannerREF` | `int(4)` | No |
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
/*
	EXEC [dbo].[ThucChay_Insert_ThucChay_ThanhTien_Admatic_ByBanner_Native_OnImg]
	@SoHopDong = 'QC6741120',
	@DmSanPhamREF = 821,
	@DmBannerREF = 1,
	@FromDate = '2020-12-01',
	@ToDate = '2020-12-01'
*/
CREATE PROCEDURE [dbo].[ThucChay_Insert_ThucChay_ThanhTien_Admatic_ByBanner_Native_OnImg]
	@SoHopDong NVARCHAR(100),
	@DmSanPhamREF INT,
	@DmBannerREF INT,
	@FromDate DATETIME,
	@ToDate DATETIME
AS
BEGIN
		DELETE FROM [dbo].[ThucChay_ThanhTien_Admatic]
		WHERE SoHopDong = @SoHopDong
		AND DmSanPhamREF = @DmSanPhamREF
		AND DmBannerID = @DmBannerREF
		AND NgayThucHien BETWEEN @FromDate AND @ToDate
		--and len(DmBannerID) = 6

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

		select a.SoHopDong, a.DmSanPhamREF as TypeProduct, a.DmSanPhamREF
		,a.TenSanPham, a.TenNhanHang, a.DmNhanHangREF, a.DmBannerID, a.DmWebsiteID, a.TenWebsite
		,a.[DmViTriBannerSanPhamID] ,a.[TenViTriBannerSanPham], a.[SoLuongThucChay] ,a.[SoLuongThucChayKM], a.[DonViTinh]
		,a.[ThanhTienThucChaySauCK]
		,a.[ThanhTienThucChayKM]
		,a.[NgayThucHien]
		,getdate() [CreatedAt]
		,N'thucchay_Branding' [CreatedBy]
		,getdate() [LastModifiedAt]
		,N'thucchay_Branding' [LastModifiedBy]
		,a.[DeletedStatus] 
		from dbo.thucchay_Native_ads a
		where a.SoHopDong = @SoHopDong
		and a.DmSanPhamREF = @DmSanPhamREF
		and a.DmBannerID = @DmBannerREF
		AND CONVERT(DATE,A.NgayThucHien) BETWEEN @FromDate AND @ToDate
		--and len(DmBannerID) = 6

END

```
