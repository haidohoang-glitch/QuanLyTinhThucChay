# Stored Procedure: `ThucChay_CheckVaUpdateGiaTriThayDoi_Admatic_NhieuSanPham_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-10-05 17:38:26.323000
- **Ngày sửa cuối**: 2022-12-21 14:23:13.473000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[dbo].[ThucChay_CheckVaUpdateGiaTriThayDoi_Admatic_NhieuSanPham_v2] '2018-06-12'
CREATE  PROCEDURE [dbo].[ThucChay_CheckVaUpdateGiaTriThayDoi_Admatic_NhieuSanPham_v2] 
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @HopDongID INT , @NgayThayDoi DATETIME, @SoHopDong NVARCHAR(1000)
	, @GhiChu_tinhlaigiatri NVARCHAR(1000) = '', @GhiChu_doitru NVARCHAR(1000)
	, @FromDate DATETIME, @todate DATETIME
	, @NgayDanhSoGioiHan DATETIME = '2020-07-20'

	DECLARE Cursor_HD_admatic CURSOR FOR
		SELECT DISTINCT A.HopDongID, A.NgayThayDoi FROM
		(
			--XAC DINH DANH SACH CÁC PHAN BO CO THAY DOI THONG TIN THANHTIEN HOAC CHIETKHAU	
			SELECT DISTINCT hdtd.HopDongFK AS HopDongID, CONVERT(DATE,hdtd.NgayThayDoi) NgayThayDoi
			FROM  
			(	SELECT hdtd.* FROM dbo.HopDongThayDoi hdtd 
				INNER JOIN dbo.HopDong hd on hd.HopDongID = hdtd.HopDongFK
				WHERE 1=1 
				AND hd.NgayDanhSoHopDong < @NgayDanhSoGioiHan --2020-07-20
				AND CONVERT(DATE, hdtd.NgayThayDoi) = @NgayThucHien
								
			)hdtd
			INNER JOIN dbo.HopDongChiTietThayDoi hdcttd ON hdtd.HopDongThayDoiID = hdcttd.HopDongThayDoiREF
			INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = hdcttd.HopDongChiTietREF
			WHERE hdtd.LoaiThayDoi = 1
			AND CONVERT(DATE,hdtd.NgayThayDoi) = @NgayThucHien
			AND((hdct.DmLoaiREF = 42) AND (hdct.ChietKhau <> hdcttd.ChietKhau OR hdct.ThanhTien <> hdcttd.ThanhTien))
			AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF =18)
			AND hdct.DmSanPhamREF IN (231,238,339,240,598,613,370,680, 733,735,821,342,585,5056,5268)
			AND NOT (EXISTS(SELECT HopDongChiTietREF 
					FROM dbo.DmThongTinHopDongBanInventory 
					WHERE hdct.HopDongChiTietID = HopDongChiTietREF)
			) --HD Ban Inventory
			UNION ALL

			--CHECK HOPDONGCHITIET BI XOA TRONG NGAY
			SELECT DISTINCT hd.HopDongID, CONVERT(DATE,hdct.LastModifiedAt) AS NgayThayDoi FROM
			(
				SELECT hdct.HopDongChiTietID, hdct.HopDongFK, hdct.DmLoaiREF, hdct.DmSanPhamREF, hdct.DmLoaiBannerREF, hdct.DeletedStatus, hdct.LastModifiedAt 
				FROM dbo.HopDongChiTiet hdct
				WHERE 1=1 
				AND(hdct.DmLoaiREF = 42)
				AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF =18)
				AND hdct.DmSanPhamREF IN (231,238,339,240,598,613,370,680, 733,735,821,342,585,5056,5268)
				AND hdct.DeletedStatus = 1
				AND NOT (EXISTS(SELECT HopDongChiTietREF 
						FROM dbo.DmThongTinHopDongBanInventory 
						WHERE hdct.HopDongChiTietID = HopDongChiTietREF)
				)--HD Ban Inventory
				AND CONVERT(DATE,hdct.LastModifiedAt) = @NgayThucHien
			) hdct INNER JOIN 
			(SELECT hd.HopDongID, hd.SoHopDong, hd.TrangThaiHopDong FROM dbo.HopDong hd WHERE hd.TrangThaiHopDong NOT IN (0,3) AND hd.NgayDanhSoHopDong < @NgayDanhSoGioiHan)hd
			ON hdct.HopDongFK = hd.HopDongID
		)A

	OPEN Cursor_HD_admatic
	FETCH NEXT FROM Cursor_HD_admatic INTO @HopDongID , @NgayThayDoi
	WHILE @@FETCH_STATUS =0
	BEGIN
		
		--1. TH THAY DOI
		IF(NOT EXISTS(SELECT hdct.HopDongChiTietID
				FROM dbo.HopDongChiTiet hdct
				WHERE 1=1 
				AND hdct.HopDongFK = @HopDongID
				AND(hdct.DmLoaiREF = 42)
				AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF =18)
				AND hdct.DmSanPhamREF IN (231,238,339,240,598,613,370,680, 733,735,821,342,585,5056,5268)
				AND hdct.DeletedStatus = 1
				AND CONVERT(DATE,hdct.LastModifiedAt) = @NgayThucHien))
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
		END
		--2. TH HDCT BI XOA
		ELSE
		BEGIN
			--THUC HIEN XU LY VOI TH CO HDCT XOA
		    EXEC [dbo].[sp_ThucChay_CheckXoaHDCTVaUpdateGTTD_Admatic_NhieuSanPham_V1] 
					@NgayThucHien = @NgayThayDoi,
					@HopDongID = @HopDongID

		END
		

	FETCH NEXT FROM Cursor_HD_admatic INTO @HopDongID , @NgayThayDoi
	END
	CLOSE Cursor_HD_admatic;
	DEALLOCATE Cursor_HD_admatic;

END


```
