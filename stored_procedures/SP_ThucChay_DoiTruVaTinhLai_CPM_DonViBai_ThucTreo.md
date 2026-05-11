# Stored Procedure: `ThucChay_DoiTruVaTinhLai_CPM_DonViBai_ThucTreo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-07 11:44:39.173000
- **Ngày sửa cuối**: 2023-07-20 16:50:10.457000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@pSoHopDong` | `nvarchar(200)` | No |
| `@pHopDongChiTietREF` | `int(4)` | No |
| `@pDmSanPhamREF` | `int(4)` | No |
| `@pNgayThucHien` | `datetime(8)` | No |
| `@pNgayGhiNhanThucChay` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
EXEC [dbo].[ThucChay_DoiTruVaTinhLai_CPM_DonViBai] 
	'QC2110718',
	821,
	'2018-07-18' ,
	'2018-07-29' ,
	@pNgayGhiNhanThucChay DATET
*/

CREATE PROCEDURE [dbo].[ThucChay_DoiTruVaTinhLai_CPM_DonViBai_ThucTreo] 
	@pSoHopDong NVARCHAR(100),
	@pHopDongChiTietREF INT,
	@pDmSanPhamREF INT,
	@pNgayThucHien DATETIME,
	@pNgayGhiNhanThucChay DATETIME
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	DECLARE @SoHopDong NVARCHAR(50), @HopDongID INT, @DmSanPhamREF INT, @TenWebsite NVARCHAR(50), @DmWebsiteREF INT, @DmBannerREF INT
	DECLARE @GhiChu_DoiTruThucChay NVARCHAR(1000), @Ghichu_TinhLaiThucChay NVARCHAR(1000),
	@NgayDanhSoGioiHan DATETIME = '2021-06-10'
	--@NgayDanhSoGioiHan DATETIME = '2021-04-01'

	SET @SoHopDong = @pSoHopDong
	SET @DmSanPhamREF = @pDmSanPhamREF
	SET @NgayThucHien = @pNgayThucHien

	--HAIDH COMMENT THEM VAO VI THEO CACH TINH MOI THEO TUNG THUC TREO VA CHAY 2021-06-07
	SET @HopDongID = ISNULL((SELECT TOP (1) HopDongID FROM dbo.HopDong WHERE SoHopDong = @SoHopDong
	AND NgayDanhSoHopDong >= @NgayDanhSoGioiHan ORDER BY HopDongID),0)

	SET @GhiChu_DoiTruThucChay = N'Doi tru thuc chay CPM DonViBai cho HDCT: ' + Convert(NVARCHAR(50),@pHopDongChiTietREF) + ', SoHopDong: ' + @SoHopDong
	SET @Ghichu_TinhLaiThucChay = N'Tinh lai thuc chay CPM DonViBai cho HDCT: ' + Convert(NVARCHAR(50),@pHopDongChiTietREF) + ', SoHopDong: ' + @SoHopDong

	--THUC HIEN DOI TRU TOAN BO DU LIEU THUC CHAY PHAT SINH
	EXEC [dbo].[ThucChay_Insert_GTTD_DoiTruGiam_ThucChayDaTinh_CPM_DonViBai] 
	@NgayThucHien = @NgayThucHien,
	@NgayGhiNhanThucChay = @pNgayGhiNhanThucChay,
	@HopDongID = @HopDongID,
	@HopDongChiTietREF = @pHopDongChiTietREF,
	@DmSanPhamREF = @DmSanPhamREF,
	@GhiChu = @GhiChu_DoiTruThucChay

	--XAC DINH NEU THUC CHAY VE KO MOI THUC HIEN TINH LAI
	IF((EXISTS(SELECT TOP (1) tcdt.HopDongChiTietREF, tcdt.DmSanPhamREF FROM dbo.ThucChayDaTinh tcdt
	WHERE tcdt.HopDongID = @HopDongID
	AND tcdt.HopDongChiTietREF = @pHopDongChiTietREF
	AND tcdt.NgayThucHien <= @pNgayGhiNhanThucChay
	GROUP BY tcdt.HopDongChiTietREF, tcdt.DmSanPhamREF HAVING ROUND(SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi),0) = 0 
	AND ROUND(SUM(tcdt.ThanhTienKM + GiaTriKMThayDoi),0) = 0)))
	BEGIN
		--UPDATE THONG TIN THUC TREO
		UPDATE tt
		SET tt.RecordStatus = 0
		FROM dbo.ThucChayHopDongChiTiet tt
		WHERE 1=1
		AND tt.HopDongREF = @HopDongID
		AND tt.HopDongChiTietREF = @pHopDongChiTietREF
		AND tt.DmSanPhamREF = @DmSanPhamREF 
	END

	--THUC HIEN TINH LAI THUC CHAY 
	EXEC [dbo].[ThucChay_TinhLai_InsertThucChayDaTinh_CPM_DonViBai_ThucTreo] 
	@NgayThucHien = @pNgayGhiNhanThucChay,
	@HopDongID = @HopDongID,
	@HopDongChiTietREF = @pHopDongChiTietREF,
	@DmSanPhamREF = @DmSanPhamREF,
	@GhiChuTinhLai = @Ghichu_TinhLaiThucChay

	SELECT '1'
END


```
