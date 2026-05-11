# Stored Procedure: `ThucChay_DoiTruVaTinhLai_CPM_DonViGoi_ByThoiGian_V2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-06-28 16:46:58.367000
- **Ngày sửa cuối**: 2022-06-28 17:07:49.887000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@pSoHopDong` | `nvarchar(200)` | No |
| `@pHopDongChiTietREF` | `int(4)` | No |
| `@pNgayGhiNhanThucChay` | `datetime(8)` | No |
| `@GhiChu` | `nvarchar(2000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
EXEC [dbo].[ThucChay_DoiTruVaTinhLai_CPM_DonViGoi_ByThoiGian] 
	'QC2110718',
	821,
	'2018-07-18' ,
	'2018-07-29' ,
	@pNgayGhiNhanThucChay DATET
*/

CREATE PROCEDURE [dbo].[ThucChay_DoiTruVaTinhLai_CPM_DonViGoi_ByThoiGian_V2] 
	@StartDate DATETIME,
	@EndDate DATETIME,
	@pSoHopDong NVARCHAR(100),
	@pHopDongChiTietREF INT,
	--@pDmSanPhamREF INT,
	@pNgayGhiNhanThucChay DATETIME,
	@GhiChu NVARCHAR(1000)
AS
BEGIN

	DECLARE @SoHopDong NVARCHAR(50), @HopDongID INT, @DmSanPhamREF INT, @TenWebsite NVARCHAR(50), @DmWebsiteREF INT, @DmBannerREF INT
	DECLARE @GhiChu_DoiTruThucChay NVARCHAR(1000), @Ghichu_TinhLaiThucChay NVARCHAR(1000), @MinNgayThucHien DATETIME, @MaxNgayThucHien DATETIME

	SET @SoHopDong = @pSoHopDong
	--SET @DmSanPhamREF = @pDmSanPhamREF
	SET @HopDongID = (SELECT TOP (1) HopDongID FROM dbo.HopDong WHERE SoHopDong = @SoHopDong ORDER BY HopDongID)
	
	SET @MinNgayThucHien = ISNULL(@StartDate,'1900-01-01')
	SET @MaxNgayThucHien = ISNULL(@EndDate,'1900-01-01')

	SET @GhiChu_DoiTruThucChay = N'Doi tru thuc chay CPM DonViGoi cho HDCT: ' + Convert(NVARCHAR(50),@pHopDongChiTietREF) + ', SoHopDong: ' + @SoHopDong + ' ,' + @GhiChu
	SET @Ghichu_TinhLaiThucChay = N'Tinh lai thuc chay CPM DonViGoi cho HDCT: ' + Convert(NVARCHAR(50),@pHopDongChiTietREF) + ', SoHopDong: ' + @SoHopDong + ' ,' + @GhiChu

	--THUC HIEN DOI TRU TOAN BO DU LIEU THUC CHAY PHAT SINH
	EXEC [dbo].[ThucChay_Insert_GTTD_DoiTruGiam_ThucChayDaTinh_CPM_DonViGoi_ThoiGian_V2] 
	@NgayThucHien = @pNgayGhiNhanThucChay,
	@HopDongID = @HopDongID,
	@HopDongChiTietREF = @pHopDongChiTietREF,
	--@DmSanPhamREF = @pDmSanPhamREF,
	@GhiChu = @GhiChu_DoiTruThucChay

	----THUC HIEN TINH LAI THUC CHAY 
	EXEC [dbo].[ThucChay_ReExcInsertThucChayDaTinh_DonViGoi_ThoiGian_V2] 
	@StartDate = @MinNgayThucHien,
	@EndDate = @MaxNgayThucHien,
	@NgayThucHien = @pNgayGhiNhanThucChay,
	@HopDongID = @HopDongID,
	@HopDongChiTietID = @pHopDongChiTietREF,
	--@DmSanPhamREF = @DmSanPhamREF,
	@GhiChuTinhLai  = @Ghichu_TinhLaiThucChay

END


```
