# Stored Procedure: `ThucChay_CheckVaUpdateGiaTriThayDoi_Admatic_NhieuSanPham_v1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-07-31 14:56:04.973000
- **Ngày sửa cuối**: 2018-09-14 15:50:40.400000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[ThucChay_CheckVaUpdateGiaTriThayDoi_Admatic_NhieuSanPham_v1] '2018-06-12'
CREATE  PROCEDURE [dbo].[ThucChay_CheckVaUpdateGiaTriThayDoi_Admatic_NhieuSanPham_v1] 
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @HopDongID INT , @NgayThayDoi DATETIME, @SoHopDong NVARCHAR(1000)
	, @GhiChu_tinhlaigiatri NVARCHAR(1000) = '', @GhiChu_doitru NVARCHAR(1000)
	, @FromDate DATETIME, @todate DATETIME
	
	DECLARE Cursor_HD_admatic CURSOR FOR
		--XAC DINH DANH SACH CÁC PHAN BO CO THAY DOI THONG TIN THANHTIEN HOAC CHIETKHAU	
		SELECT DISTINCT hdtd.HopDongFK, CONVERT(DATE,hdtd.NgayThayDoi)NgayThayDoi
		FROM dbo.HopDongThayDoi hdtd
		INNER JOIN dbo.HopDongChiTietThayDoi hdcttd ON hdtd.HopDongThayDoiID = hdcttd.HopDongThayDoiREF
		INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = hdcttd.HopDongChiTietREF
		WHERE hdtd.LoaiThayDoi = 1
		AND CONVERT(DATE,hdtd.NgayThayDoi) = @NgayThucHien
		AND((hdct.DmLoaiREF = 42) AND (hdct.ChietKhau <> hdcttd.ChietKhau OR hdct.ThanhTien <> hdcttd.ThanhTien))
		AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF =18)
		AND hdct.DmSanPhamREF NOT IN (736,817) -- chi phí công nghệ, chi phi marketing fee

	OPEN Cursor_HD_admatic
	FETCH NEXT FROM Cursor_HD_admatic INTO @HopDongID , @NgayThayDoi
	WHILE @@FETCH_STATUS =0
	BEGIN
		SELECT @todate = MAX(NgayThucHien), @FromDate = MIN(NgayThucHien),@SoHopDong = SoHopDong  FROM dbo.ThucChayDaTinh
		WHERE HopDongID = @HopDongID
		AND DmHinhThucQuangCao = 42
		AND NgayThucHien <= @NgayThucHien
		GROUP BY SoHopDong
		-- VOI TRUONG HOP CHI THAY DOI TANG SOLUONG CUA PHAN BO CHUA DAY TIEN THI KHONG PHAI LAM GI
		--THUC HIEN DOI TRU TINH LAI
		EXEC [dbo].[ThucChay_DoiTruVaTinhLaiThucChay_Admatic_SoHopDong] 
			@FromDate = @FromDate,
			@ToDate = @todate,
			@HopDongID = @HopDongID,
			@NgayGhiNhanThucChay = @NgayThucHien

		--SET @FromDate = ISNULL(@FromDate,'1900-01-01')
		--SET @todate = ISNULL(@todate, '1900-01-01')
		--SET @GhiChu_doitru = N'Doi tru thuc chay hopdong admatic thay doi: '+ @SoHopDong
		--SET @GhiChu_tinhlaigiatri = N'Tinh lai gia tri thuc chay hopdong admatic:' + @SoHopDong
		----1. XAC DINH NGUYEN NHAN THAY DOI: THANHTIEN, CHIETKHAU

		----2. THUC HIEN DOI TRU TOAN BO THUCCHAYDATINH CUA HOPDONG VOI ADMATIC
		--EXEC [dbo].[ThucChay_Insert_GTTD_All_ThucChayDaTinh_Admatic_WithHopDong] 
		--@FromDate = @FromDate,
		--@ToDate = @todate,
		--@NgayGhiNhanThucChay = @todate,
		--@HopDongID = @HopDongID, 
		--@GhiChu = @GhiChu_doitru

		----3. THUC HIEN TINH LẠI GIA TRI
		--EXEC [dbo].[ThucChay_TinhLaiThucChay_ByHopDongID_Admatic_NhieuSanPham] 
		--@FromDate = @FromDate, 
		--@ToDate = @todate, 
		--@HopDongFK = @HopDongID,
		--@GhiChu = @GhiChu_tinhlaigiatri

		----UPDATE LAI NGAY GHI NHAN THUC CHAY
		--UPDATE dbo.ThucChayDaTinh
		--SET NgayThucHien = @NgayThucHien
		--WHERE HopDongID = @HopDongID
		--AND DmHinhThucQuangCao = 42
		--AND (GhiChu = @GhiChu_doitru OR GhiChu = @GhiChu_tinhlaigiatri)
		--AND CONVERT(DATE,CreatedAt) = CONVERT(DATE, GETDATE())

		----UPDATE LAI NGAY GHI NHAN THUC CHAY
		--UPDATE dbo.ThucChayDaTinhAdmarket
		--SET NgayThucHien = @NgayThucHien
		--WHERE HopDongID = @HopDongID
		--AND DmHinhThucQuangCao = 42
		--AND DmSanPhamREF = 585
		--AND (GhiChu = @GhiChu_doitru OR GhiChu = @GhiChu_tinhlaigiatri)
		--AND CONVERT(DATE,CreatedAt) = CONVERT(DATE, GETDATE())

	FETCH NEXT FROM Cursor_HD_admatic INTO @HopDongID , @NgayThayDoi
	END
	CLOSE Cursor_HD_admatic;
	DEALLOCATE Cursor_HD_admatic;

END


```
