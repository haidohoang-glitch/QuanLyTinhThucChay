# Stored Procedure: `ThucChay_DoiTruVaTinhLaiThucChay_Admatic_SoHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-07-31 15:11:50.340000
- **Ngày sửa cuối**: 2018-11-01 16:05:17.860000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |
| `@HopDongID` | `nvarchar(1000)` | No |
| `@NgayGhiNhanThucChay` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[ThucChay_DoiTruVaTinhLaiThucChay_Admatic_SoHopDong]   '2018-06-07','2018-08-21', 1003632,'2018-10-31'
CREATE  PROCEDURE [dbo].[ThucChay_DoiTruVaTinhLaiThucChay_Admatic_SoHopDong] 
	@FromDate DATETIME,
	@ToDate DATETIME,
	@HopDongID NVARCHAR(500),
	@NgayGhiNhanThucChay DATETIME
AS
BEGIN
	DECLARE @SoHopDong NVARCHAR(50)
	, @GhiChu_doitru NVARCHAR(1000), @GhiChu_tinhlaigiatri NVARCHAR(1000)



	SET @SoHopDong = (SELECT TOP (1) SoHopDong FROM dbo.HopDong WHERE HopDongID = @HopDongID ORDER BY HopDongID)

	SET @FromDate = ISNULL(@FromDate,'1900-01-01')
	SET @todate = ISNULL(@todate, '1900-01-01')
	SET @GhiChu_doitru = N'Doi tru thuc chay hopdong admatic thay doi: '+ @SoHopDong
	SET @GhiChu_tinhlaigiatri = N'Tinh lai gia tri thuc chay hopdong admatic:' + @SoHopDong
	--1. XAC DINH NGUYEN NHAN THAY DOI: THANHTIEN, CHIETKHAU

	--2. THUC HIEN DOI TRU TOAN BO THUCCHAYDATINH CUA HOPDONG VOI ADMATIC
	EXEC [dbo].[ThucChay_Insert_GTTD_All_ThucChayDaTinh_Admatic_WithHopDong] 
	@FromDate = @FromDate,
	@ToDate = @todate,
	@NgayGhiNhanThucChay = @todate,
	@HopDongID = @HopDongID, 
	@GhiChu = @GhiChu_doitru
	
	--3. THUC HIEN TINH LẠI GIA TRI
	EXEC [dbo].[ThucChay_TinhLaiThucChay_ByHopDongID_Admatic_NhieuSanPham] 
	@FromDate = @FromDate, 
	@ToDate = @todate, 
	@HopDongFK = @HopDongID,
	@GhiChu = @GhiChu_tinhlaigiatri

	--UPDATE LAI NGAY GHI NHAN THUC CHAY
	UPDATE dbo.ThucChayDaTinh
	SET NgayThucHien = @NgayGhiNhanThucChay
	WHERE HopDongID = @HopDongID
	AND DmHinhThucQuangCao = 42
	AND (GhiChu = @GhiChu_doitru OR GhiChu = @GhiChu_tinhlaigiatri)
	AND CONVERT(DATE,CreatedAt) = CONVERT(DATE, GETDATE())

	--UPDATE LAI NGAY GHI NHAN THUC CHAY
	UPDATE dbo.ThucChayDaTinhAdmarket
	SET NgayThucHien = @NgayGhiNhanThucChay
	WHERE HopDongID = @HopDongID
	AND DmHinhThucQuangCao = 42
	AND DmSanPhamREF = 585
	AND (GhiChu = @GhiChu_doitru OR GhiChu = @GhiChu_tinhlaigiatri)
	AND CONVERT(DATE,CreatedAt) = CONVERT(DATE, GETDATE())

END


```
