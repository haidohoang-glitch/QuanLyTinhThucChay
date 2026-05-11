# Stored Procedure: `API_Publisher_GetThucChayTamTinhTheoSanPhamWebsite`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-03-25 10:18:40.580000
- **Ngày sửa cuối**: 2017-04-05 10:57:11.013000

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

CREATE PROCEDURE [dbo].[API_Publisher_GetThucChayTamTinhTheoSanPhamWebsite]
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @v_SiteID INT, @v_DmSanPhamREF INT

	SET @v_SiteID = 964
	SET @v_DmSanPhamREF = 598

	--SET @v_SiteID = @SiteID
	--SET @v_DmSanPhamREF = @DmSanPhamREF

	SELECT d.TenWebsite	
	, d.TenSanPham
	, N'(980x250; 300x600)' DinhDang
	, d.NgayThucHien
	, d.DonViTinh
	, SUM(d.SoLuongThucChay) SoLuongThucChay
	, ROUND(SUM(d.ThanhTienSauTrietKhauThucChay + d.GiaTriThayDoi)*1.1,0) ThanhTienThucChay_VAT
	, N'TamTinh' TrangThai
	FROM dbo.ThucChayDaTinh d
	WHERE 1=1
	AND d.DmSanPhamREF = @v_DmSanPhamREF
	AND d.DmWebsiteREF = @v_SiteID
	AND d.NgayThucHien = @NgayThucHien
	--AND DmSanPhamREF IN (231,238,339,240,598,613,370,680) 
	--AND not (DmHinhThucQuangCao IN(13,42) OR DmLoaiBannerREF IN (17,18))
	GROUP BY d.TenWebsite, d.TenSanPham, d.NgayThucHien, d.DonViTinh

END



```
