# Stored Procedure: `sp_ThucChay_CheckXoaHDCTVaUpdateGTTD_Admatic_NhieuSanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-09-27 15:08:09.010000
- **Ngày sửa cuối**: 2022-10-25 11:41:58.657000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[sp_ThucChay_CheckXoaHDCTVaUpdateGTTD_Admatic_NhieuSanPham] '2018-06-12'
CREATE  PROCEDURE [dbo].[sp_ThucChay_CheckXoaHDCTVaUpdateGTTD_Admatic_NhieuSanPham] 
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE @HopDongID INT , @NgayThayDoi DATETIME, @SoHopDong NVARCHAR(1000)
	, @GhiChu_doitru NVARCHAR(1000), @ThanhTienThucChayHDCT_Xoa BIGINT = 0
	, @ExistAdmaticNhieuSanPham SMALLINT = 0, @ExistNhieuHDCTCungSanPham SMALLINT = 0
	, @FromDate DATETIME, @todate DATETIME

	DECLARE Cursor_HDCT_xoa_admatic CURSOR FOR
		--CHECK HOPDONGCHITIET BI XOA TRONG NGAY
		SELECT DISTINCT hd.HopDongID, CONVERT(DATE,hdct.LastModifiedAt) AS NgayThayDoi FROM
		(
			SELECT hdct.HopDongChiTietID, hdct.HopDongFK, hdct.DmLoaiREF, hdct.DmSanPhamREF, hdct.DmLoaiBannerREF, hdct.DeletedStatus, hdct.LastModifiedAt 
			FROM dbo.HopDongChiTiet hdct
			WHERE 1=1 
			AND(hdct.DmLoaiREF = 42)
			AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF =18)
			AND hdct.DmSanPhamREF IN (231,238,339,240,598,613,370,680,735,821,342,585,5056)
			AND hdct.DeletedStatus = 1
			AND CONVERT(DATE,hdct.LastModifiedAt) = @NgayThucHien
		) hdct INNER JOIN 
		(SELECT hd.HopDongID, hd.SoHopDong, hd.TrangThaiHopDong FROM dbo.HopDong hd WHERE hd.TrangThaiHopDong NOT IN (0,3))hd
		ON hdct.HopDongFK = hd.HopDongID
		ORDER BY hd.HopDongID

	OPEN Cursor_HDCT_xoa_admatic
	FETCH NEXT FROM Cursor_HDCT_xoa_admatic INTO @HopDongID , @NgayThayDoi
	WHILE @@FETCH_STATUS =0
	BEGIN
		SET @ThanhTienThucChayHDCT_Xoa = ISNULL(
												(SELECT SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) 
													FROM dbo.ThucChayDaTinh tcdt
													WHERE 1=1 
													AND HopDongID = @HopDongID
													AND DmHinhThucQuangCao = 42
													AND DmSanPhamREF NOT IN (736,817)
													AND NOT (DmHinhThucQuangCao = 13 OR DmLoaiBannerREF = 18)
													AND NgayThucHien <= @NgayThucHien
												),0)
		--NEU CHUA PHAT SINH THUC CHAY => KHONG PHAI LAM GI CA
		IF(@ThanhTienThucChayHDCT_Xoa = 0)
		BEGIN
		    PRINT 'NEU CHUA PHAT SINH THUC CHAY => KHONG PHAI LAM GI CA'
		END
		--NEU CO PHAT SINH THUC CHAY
		ELSE
		BEGIN
			SELECT @todate = MAX(NgayThucHien), @FromDate = MIN(NgayThucHien),@SoHopDong = SoHopDong  FROM dbo.ThucChayDaTinh
				WHERE HopDongID = @HopDongID
				AND DmHinhThucQuangCao = 42
				AND DmSanPhamREF NOT IN (736,817)
				AND NOT (DmHinhThucQuangCao = 13 OR DmLoaiBannerREF = 18)
				AND NgayThucHien <= @NgayThucHien
				GROUP BY SoHopDong

			SET @GhiChu_doitru = N'HDCT XOA, doi tru thuc chay hopdong admatic thay doi: '+ @SoHopDong

		    --TH1: NEU CHI CO 01 HDCT ADMATIC TON TAI => CHI THUC HIEN DOI TRU TOAN BO
			IF(EXISTS(SELECT COUNT(hdct.HopDongChiTietID) FROM dbo.HopDongChiTiet hdct 
				WHERE hdct.HopDongFK = @HopDongID 
				AND(hdct.DmLoaiREF = 42)
				AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF =18)
				AND hdct.DmSanPhamREF IN (231,238,339,240,598,613,370,680,735,821,342,585,5056)
				--AND hdct.DeletedStatus = 1
				GROUP BY hdct.HopDongFK HAVING COUNT(hdct.HopDongChiTietID) <= 1))
			BEGIN
				PRINT 'TH1: NEU CHI CO 01 HDCT ADMATIC TON TAI => CHI THUC HIEN DOI TRU TOAN BO'
				--2. THUC HIEN DOI TRU TOAN BO THUCCHAYDATINH CUA HOPDONG VOI ADMATIC
				EXEC [dbo].[ThucChay_Insert_GTTD_All_ThucChayDaTinh_Admatic_WithHopDong] 
				@FromDate = @FromDate,
				@ToDate = @todate,
				@NgayGhiNhanThucChay = @todate,
				@HopDongID = @HopDongID, 
				@GhiChu = @GhiChu_doitru

				--THUC HIEN UPDATE NGAY THUC HIEN DOI TRU
				--UPDATE LAI NGAY GHI NHAN THUC CHAY
				UPDATE dbo.ThucChayDaTinh
				SET NgayThucHien = @NgayThucHien
				WHERE HopDongID = @HopDongID
				AND DmHinhThucQuangCao = 42
				AND (GhiChu = @GhiChu_doitru)
				AND CONVERT(DATE,CreatedAt) = CONVERT(DATE, GETDATE())

				--UPDATE LAI NGAY GHI NHAN THUC CHAY
				UPDATE dbo.ThucChayDaTinhAdmarket
				SET NgayThucHien = @NgayThucHien
				WHERE HopDongID = @HopDongID
				AND DmHinhThucQuangCao = 42
				AND DmSanPhamREF = 585
				AND (GhiChu = @GhiChu_doitru)
				AND CONVERT(DATE,CreatedAt) = CONVERT(DATE, GETDATE())
			END
			--TH2: NEU CO > 01 HDCT ADMATIC TON TAI
			ELSE
			BEGIN
				PRINT 'TH2: NEU CO > 01 HDCT ADMATIC TON TAI'
				SET @ExistAdmaticNhieuSanPham = ISNULL((SELECT COUNT(DISTINCT hdct.HopDongChiTietID) 
													FROM dbo.HopDongChiTiet  hdct
													WHERE hdct.HopDongFK = @HopDongID 
													AND (hdct.DmLoaiREF = 42)
													AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF =18)
													AND hdct.DmSanPhamREF = 733 --nhieu san pham
													GROUP BY HopDongFK),0)
				
				SET @ExistNhieuHDCTCungSanPham = ISNULL((SELECT COUNT(DISTINCT hdct.HopDongChiTietID) 
													FROM dbo.HopDongChiTiet  hdct
													WHERE hdct.HopDongFK = @HopDongID 
													AND (hdct.DmLoaiREF = 42)
													AND hdct.DeletedStatus = 0
													AND EXISTS(SELECT ct.HopDongChiTietID FROM dbo.HopDongChiTiet ct
																WHERE ct.HopDongFK = @HopDongID 
																AND(ct.DmLoaiREF = 42)
																AND NOT (ct.DmLoaiREF = 13 OR ct.DmLoaiBannerREF =18)
																AND ct.DmSanPhamREF IN (231,238,339,240,598,613,370,680,735,821,342,585,5056)
																AND ct.DeletedStatus = 1
																AND ct.DmSanPhamREF = hdct.DmSanPhamREF)
													AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF =18)
													GROUP BY HopDongFK),0)

				--TH2.1 NẾU KHÔNG TỒN TẠI HDCT CÓ NHIEU SẢN PHẨM VÀ HDCT(MOT HOAC NHIEU HDCT) BỊ XÓA CÓ SẢN PHẨM LÀ DUY NHẤT TRONG HD
				IF(@ExistAdmaticNhieuSanPham = 0 AND @ExistNhieuHDCTCungSanPham = 0)
				BEGIN
				    PRINT 'TH2.1 NẾU KHÔNG TỒN TẠI HDCT CÓ NHIEU SẢN PHẨM VÀ HDCT(MOT HOAC NHIEU HDCT) BỊ XÓA CÓ SẢN PHẨM LÀ DUY NHẤT TRONG HD => THUC HIEN DOI TRU'
					--2. THUC HIEN DOI TRU TOAN BO THUCCHAYDATINH CUA HOPDONG VOI ADMATIC
					EXEC [dbo].[ThucChay_Insert_GTTD_All_ThucChayDaTinh_Admatic_WithHopDong] 
					@FromDate = @FromDate,
					@ToDate = @todate,
					@NgayGhiNhanThucChay = @todate,
					@HopDongID = @HopDongID, 
					@GhiChu = @GhiChu_doitru

					--THUC HIEN UPDATE NGAY THUC HIEN DOI TRU
					--UPDATE LAI NGAY GHI NHAN THUC CHAY
					UPDATE dbo.ThucChayDaTinh
					SET NgayThucHien = @NgayThucHien
					WHERE HopDongID = @HopDongID
					AND DmHinhThucQuangCao = 42
					AND (GhiChu = @GhiChu_doitru)
					AND CONVERT(DATE,CreatedAt) = CONVERT(DATE, GETDATE())

					--UPDATE LAI NGAY GHI NHAN THUC CHAY
					UPDATE dbo.ThucChayDaTinhAdmarket
					SET NgayThucHien = @NgayThucHien
					WHERE HopDongID = @HopDongID
					AND DmHinhThucQuangCao = 42
					AND DmSanPhamREF = 585
					AND (GhiChu = @GhiChu_doitru)
					AND CONVERT(DATE,CreatedAt) = CONVERT(DATE, GETDATE())
				END
				--TH2.2 CÒN LẠI LÀ THỰC HIỆN ĐỐI TRỪ VÀ TÍNH LẠI TOÀN BỘ
				ELSE
				BEGIN
				    PRINT 'TH2.2 CÒN LẠI LÀ THỰC HIỆN ĐỐI TRỪ VÀ TÍNH LẠI TOÀN BỘ'
					EXEC [dbo].[ThucChay_DoiTruVaTinhLaiThucChay_Admatic_SoHopDong] 
						@FromDate = @FromDate,
						@ToDate = @todate,
						@HopDongID = @HopDongID,
						@NgayGhiNhanThucChay = @NgayThucHien
				END
			END
		END

	FETCH NEXT FROM Cursor_HDCT_xoa_admatic INTO @HopDongID , @NgayThayDoi
	END
	CLOSE Cursor_HDCT_xoa_admatic;
	DEALLOCATE Cursor_HDCT_xoa_admatic;

END


```
