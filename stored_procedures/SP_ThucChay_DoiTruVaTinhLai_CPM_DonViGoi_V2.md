# Stored Procedure: `ThucChay_DoiTruVaTinhLai_CPM_DonViGoi_V2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-12-23 10:14:14.243000
- **Ngày sửa cuối**: 2021-12-28 09:38:02.080000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@pSoHopDong` | `nvarchar(200)` | No |
| `@pHopDongChiTietREF` | `int(4)` | No |
| `@pNgayGhiNhanThucChay` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
EXEC exec [dbo].[ThucChay_DoiTruVaTinhLai_CPM_DonViGoi_V2] 
  @StartDate = '2021-09-25',
  @EndDate = '2021-12-20' ,
  @pSoHopDong ='QC4840921' ,
  @pHopDongChiTietREF = 634950,
   @pNgayGhiNhanThucChay ='2021-12-26'
*/

CREATE PROCEDURE [dbo].[ThucChay_DoiTruVaTinhLai_CPM_DonViGoi_V2] 
	@StartDate DATETIME,
	@EndDate DATETIME,
	@pSoHopDong NVARCHAR(100),
	@pHopDongChiTietREF INT,
	@pNgayGhiNhanThucChay DATETIME
AS
BEGIN

	DECLARE @SoHopDong NVARCHAR(50), @HopDongID INT, @DmSanPhamREF INT, @TenWebsite NVARCHAR(50), @DmWebsiteREF INT, @DmBannerREF INT
	DECLARE @GhiChu_DoiTruThucChay NVARCHAR(1000), @Ghichu_TinhLaiThucChay NVARCHAR(1000), @MinNgayThucHien DATETIME, @MaxNgayThucHien DATETIME

	SET @SoHopDong = @pSoHopDong

	SET @HopDongID = (SELECT TOP (1) HopDongID FROM dbo.HopDong WHERE SoHopDong = @SoHopDong ORDER BY HopDongID)
	
	SET @MinNgayThucHien = ISNULL(@StartDate,'1900-01-01')
	SET @MaxNgayThucHien = ISNULL(@EndDate,'1900-01-01')

	SET @GhiChu_DoiTruThucChay = N'Doi tru thuc chay CPM DonViGoi cho HDCT: ' + Convert(NVARCHAR(50),@pHopDongChiTietREF) + ', SoHopDong: ' + @SoHopDong
	SET @Ghichu_TinhLaiThucChay = N'Tinh lai thuc chay CPM DonViGoi cho HDCT: ' + Convert(NVARCHAR(50),@pHopDongChiTietREF) + ', SoHopDong: ' + @SoHopDong

	--THUC HIEN DOI TRU TOAN BO DU LIEU THUC CHAY PHAT SINH
	EXEC [dbo].[ThucChay_Insert_GTTD_DoiTruGiam_ThucChayDaTinh_CPM_DonViGoi_V2] 
	@NgayThucHien = @pNgayGhiNhanThucChay,
	@HopDongID = @HopDongID,
	@HopDongChiTietREF = @pHopDongChiTietREF,
	@GhiChu = @GhiChu_DoiTruThucChay

	----THUC HIEN TINH LAI THUC CHAY 
	EXEC [dbo].[ThucChay_ReExcInsertThucChayDaTinh_DonViGoi_V2] 
	@StartDate = @MinNgayThucHien,
	@EndDate = @MaxNgayThucHien,
	@HopDongID = @HopDongID,
	@HopDongChiTietID = @pHopDongChiTietREF,
	@GhiChuTinhLai  = @Ghichu_TinhLaiThucChay

	--update lai ngay ghi nhan thuc chay
	UPDATE tc
	SET tc.NgayThucHien = @pNgayGhiNhanThucChay
	FROM dbo.ThucChayDaTinh tc
	WHERE tc.HopDongID = @HopDongID
	AND tc.HopDongChiTietREF = @pHopDongChiTietREF
	AND CONVERT(DATE,tc.CreatedAt) = Convert(date,GETDATE())
	AND (tc.GhiChu = @GhiChu_DoiTruThucChay or tc.GhiChu = @Ghichu_TinhLaiThucChay)

	SELECT '1'
END


```
