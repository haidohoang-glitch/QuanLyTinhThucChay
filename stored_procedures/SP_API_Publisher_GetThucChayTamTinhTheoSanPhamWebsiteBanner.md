# Stored Procedure: `API_Publisher_GetThucChayTamTinhTheoSanPhamWebsiteBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-04-05 10:58:38.523000
- **Ngày sửa cuối**: 2017-07-04 11:37:07.497000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
[dbo].[API_Publisher_GetThucChayTamTinhTheoSanPhamWebsite] '2017-03-24'
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME

*/

CREATE PROCEDURE [dbo].[API_Publisher_GetThucChayTamTinhTheoSanPhamWebsiteBanner]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @v_SiteID INT, @v_DmSanPhamREF INT

	SET @v_SiteID = 964
	SET @v_DmSanPhamREF = 598

	--SET @v_SiteID = @SiteID
	--SET @v_DmSanPhamREF = @DmSanPhamREF

	SELECT TenWebsite, DmWebsiteREF, DmBannerREF, '' TenBanner
	, DonViTinh, SUM(SoLuongThucChay)SoLuongThucChay
	, NgayThucHien, SUM(ThanhTienSauTrietKhauThucChay +GiaTriThayDoi)*1.1 ThanhTienThucChay_VAT
	, SUM(TongViewThucChay)TongSoLuongThucChay_View
	, SUM(TongClickThucChay)TongSoLuongThucChay_Click
	, N'TamTinh' AS TrangThai
	FROM dbo.ThucChayDaTinh
	WHERE HopDongID <> 0
	AND DmSanPhamREF = @v_DmSanPhamREF
	AND NgayThucHien = @NgayThucHien
	AND DmWebsiteREF = @v_SiteID
	AND DmSanPhamREF IN (231,238,339,240,598,613,370,680) 
	AND not (DmHinhThucQuangCao IN(13,42) OR DmLoaiBannerREF IN (17,18))
	GROUP BY TenWebsite, DmWebsiteREF, DmBannerREF
	, DonViTinh, NgayThucHien

END



```
