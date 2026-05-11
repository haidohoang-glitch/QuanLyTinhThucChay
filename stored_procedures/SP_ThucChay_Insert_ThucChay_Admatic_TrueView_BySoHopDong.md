# Stored Procedure: `ThucChay_Insert_ThucChay_Admatic_TrueView_BySoHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-05-19 17:14:18.587000
- **Ngày sửa cuối**: 2017-05-20 08:11:28.440000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[Job_ThucChay_Admatic_NhieuSanPham]
CREATE  PROCEDURE [dbo].[ThucChay_Insert_ThucChay_Admatic_TrueView_BySoHopDong] 
@NgayThucHien DATETIME,
@SoHopDong NVARCHAR(200)
AS
BEGIN
	--HAIDH COMMENT : True View Them thong tin thuc chay True View vao table ThucChay_Admatic
	INSERT INTO dbo.ThucChay_Admatic
			( ThucChayID ,
			  SoHopDong ,
			  DanhsachDmBookingREF ,
			  DmSanPhamREF ,
			  TenSanPham ,
			  DmNhomWebsiteREF ,
			  TenNhomWebsite ,
			  DmWebsiteREF ,
			  TenWebsite ,
			  DmChienDichREF ,
			  TenChienDich ,
			  DmBannerREF ,
			  TenBanner ,
			  NgayThucHien ,
			  TongViewThucChay ,
			  TongClickThucChay ,
			  CreatedBy ,
			  CreatedAt ,
			  LastModifiedBy ,
			  LastModifiedAt ,
			  DeletedStatus ,
			  PrintStatus ,
			  RecordStatus ,
			  TongSoBaiViet ,
			  SoThuTuTheoNgay ,
			  TypeProduct ,
			  BannerType ,
			  UserName ,
			  SaleName ,
			  Email ,
			  LastTimeCalc ,
			  sys_date ,
			  IsReady ,
			  ProductUnitID ,
			  ProductUnitName ,
			  BannerTypeName ,
			  HopDongChiTietREF ,
			  CampainStatus ,
			  BannerStatus ,
			  IsNoiBo,
			  HopDongID,
			  TongTrueViewThucChay
			)
	SELECT  'ThucChaytrueviewID' ThucChayID ,
			  tc.SoHopDong ,
			  '' DanhsachDmBookingREF ,
			  tc.DmSanPhamREF ,
			  tc.TenSanPham,
			  0 DmNhomWebsiteREF ,
			  '' TenNhomWebsite ,
			  tc.[SiteID] DmWebsiteREF ,
			  tc.[SiteName] TenWebsite ,
			  tc.[campaignid] ,
			  '' TenChienDich ,
			  tc.[bannerid] DmBannerREF,
			  '' TenBanner ,
			  tc.NgayThucHien ,
			  tc.[Views] ,
			  tc.[Clicks] ,
			  tc.CreatedBy ,
			  tc.CreatedAt ,
			  tc.LastModifiedBy ,
			  tc.LastModifiedAt ,
			  tc.[DeletedStatus] ,
			  0 PrintStatus ,
			  0 RecordStatus ,
			  0 TongSoBaiViet ,
			  0 SoThuTuTheoNgay ,
			  tc.[TypeProduct] ,
			  0 BannerType ,
			  '' UserName ,
			  '' SaleName ,
			  '' Email ,
			  '' LastTimeCalc ,
			  GETDATE() sys_date ,
			  0 IsReady ,
			  0 ProductUnitID ,
			  '' ProductUnitName ,
			  '' BannerTypeName ,
			  0 HopDongChiTietREF ,
			  0 CampainStatus ,
			  0 BannerStatus ,
			  0 IsNoiBo, 
			  bn.HopDongID,
			  tc.[True_View]
			  FROM dbo.ThucChayTrueView tc
	INNER JOIN (
		SELECT DISTINCT hd.SoHopDong, hd.HopDongID, bn.DmBannerID 
		FROM dbo.ThucChayHopDongChiTietAndBanner_admatic bn
		INNER JOIN dbo.HopDong hd ON bn.HopDongREF = hd.HopDongID
		WHERE hd.SoHopDong = @SoHopDong
		AND bn.DonViTinh = N'TRUE VIEW'
	)bn 
	ON tc.SoHopDong = bn.SoHopDong 
	AND tc.[bannerid] = bn.DmBannerID
	WHERE tc.NgayThucHien = @NgayThucHien
	AND tc.SoHopDong = @SoHopDong
	
END

```
