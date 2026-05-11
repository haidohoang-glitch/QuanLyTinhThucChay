# Stored Procedure: `ThucChay_DoiTruVaTinhLai_CPM_DonViGoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-04-12 15:31:18.277000
- **Ngày sửa cuối**: 2021-04-14 09:39:07.167000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@pSoHopDong` | `nvarchar(200)` | No |
| `@pHopDongChiTietREF` | `int(4)` | No |
| `@pDmSanPhamREF` | `int(4)` | No |
| `@pNgayGhiNhanThucChay` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
EXEC [dbo].[ThucChay_DoiTruVaTinhLai_CPM_DonViGoi] 
	'QC2110718',
	821,
	'2018-07-18' ,
	'2018-07-29' ,
	@pNgayGhiNhanThucChay DATET
*/

CREATE PROCEDURE [dbo].[ThucChay_DoiTruVaTinhLai_CPM_DonViGoi] 
	@StartDate DATETIME,
	@EndDate DATETIME,
	@pSoHopDong NVARCHAR(100),
	@pHopDongChiTietREF INT,
	@pDmSanPhamREF INT,
	@pNgayGhiNhanThucChay DATETIME
AS
BEGIN

	DECLARE @SoHopDong NVARCHAR(50), @HopDongID INT, @DmSanPhamREF INT, @TenWebsite NVARCHAR(50), @DmWebsiteREF INT, @DmBannerREF INT
	DECLARE @GhiChu_DoiTruThucChay NVARCHAR(1000), @Ghichu_TinhLaiThucChay NVARCHAR(1000), @MinNgayThucHien DATETIME, @MaxNgayThucHien DATETIME

	SET @SoHopDong = @pSoHopDong
	SET @DmSanPhamREF = @pDmSanPhamREF
	SET @HopDongID = (SELECT TOP (1) HopDongID FROM dbo.HopDong WHERE SoHopDong = @SoHopDong ORDER BY HopDongID)
	
	SET @MinNgayThucHien = ISNULL(@StartDate,'1900-01-01')
	SET @MaxNgayThucHien = ISNULL(@EndDate,'1900-01-01')

	SET @GhiChu_DoiTruThucChay = N'Doi tru thuc chay CPM DonViGoi cho HDCT: ' + Convert(NVARCHAR(50),@pHopDongChiTietREF) + ', SoHopDong: ' + @SoHopDong
	SET @Ghichu_TinhLaiThucChay = N'Tinh lai thuc chay CPM DonViGoi cho HDCT: ' + Convert(NVARCHAR(50),@pHopDongChiTietREF) + ', SoHopDong: ' + @SoHopDong

	--THUC HIEN DOI TRU TOAN BO DU LIEU THUC CHAY PHAT SINH
	EXEC [dbo].[ThucChay_Insert_GTTD_DoiTruGiam_ThucChayDaTinh_CPM_DonViGoi] 
	@NgayThucHien = @pNgayGhiNhanThucChay,
	@HopDongID = @HopDongID,
	@HopDongChiTietREF = @pHopDongChiTietREF,
	@DmSanPhamREF = @pDmSanPhamREF,
	@GhiChu = @GhiChu_DoiTruThucChay

	----THUC HIEN TINH LAI THUC CHAY 
	EXEC [dbo].[ThucChay_ReExcInsertThucChayDaTinh_DonViGoi] 
	@StartDate = @MinNgayThucHien,
	@EndDate = @MaxNgayThucHien,
	@HopDongID = @HopDongID,
	@HopDongChiTietID = @pHopDongChiTietREF,
	@DmSanPhamREF = @DmSanPhamREF,
	@GhiChuTinhLai  = @Ghichu_TinhLaiThucChay

	--update lai ngay ghi nhan thuc chay
	UPDATE tc
	SET tc.NgayThucHien = @pNgayGhiNhanThucChay
	FROM dbo.ThucChayDaTinh tc
	WHERE tc.HopDongID = @HopDongID
	AND tc.HopDongChiTietREF = @pHopDongChiTietREF
	AND tc.DmSanPhamREF = @DmSanPhamREF
	AND CONVERT(DATE,tc.CreatedAt) = Convert(date,GETDATE())
	AND (tc.GhiChu = @GhiChu_DoiTruThucChay or tc.GhiChu = @Ghichu_TinhLaiThucChay)

	SELECT '1'
END


```
