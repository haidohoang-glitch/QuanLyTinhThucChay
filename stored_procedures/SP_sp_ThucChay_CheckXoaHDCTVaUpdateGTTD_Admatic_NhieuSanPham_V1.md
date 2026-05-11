# Stored Procedure: `sp_ThucChay_CheckXoaHDCTVaUpdateGTTD_Admatic_NhieuSanPham_V1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-10-05 17:43:31.547000
- **Ngày sửa cuối**: 2019-02-20 09:42:53.913000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongID` | `int(4)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[sp_ThucChay_CheckXoaHDCTVaUpdateGTTD_Admatic_NhieuSanPham] '2018-06-12'
CREATE  PROCEDURE [dbo].[sp_ThucChay_CheckXoaHDCTVaUpdateGTTD_Admatic_NhieuSanPham_V1] 
	@NgayThucHien DATETIME,
	@HopDongID INT
AS
BEGIN
	DECLARE @NgayThayDoi DATETIME, @SoHopDong NVARCHAR(1000)
	, @GhiChu_doitru NVARCHAR(1000), @ThanhTienThucChayHDCT_Xoa BIGINT = 0
	, @ExistAdmaticNhieuSanPham SMALLINT = 0, @ExistNhieuHDCTCungSanPham SMALLINT = 0
	, @FromDate DATETIME, @todate DATETIME, @HopDongChiTietID INT = 0

	SET @NgayThayDoi = @NgayThucHien

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
				AND hdct.DmSanPhamREF NOT IN (736,817) -- chi phí công nghệ, chi phi marketing fee
				GROUP BY hdct.HopDongFK HAVING COUNT(hdct.HopDongChiTietID) <= 1))
			BEGIN
				PRINT 'TH1: NEU CHI CO 01 HDCT ADMATIC TON TAI => CHI THUC HIEN DOI TRU TOAN BO'
				--2. THUC HIEN DOI TRU TOAN BO THUCCHAYDATINH CUA HOPDONG VOI ADMATIC
				--EXEC [dbo].[ThucChay_Insert_GTTD_All_ThucChayDaTinh_Admatic_WithHopDong] 
				--@FromDate = @FromDate,
				--@ToDate = @todate,
				--@NgayGhiNhanThucChay = @todate,
				--@HopDongID = @HopDongID, 
				--@GhiChu = @GhiChu_doitru
				SET @HopDongChiTietID = ISNULL((SELECT TOP (1) hdct.HopDongChiTietID FROM dbo.HopDongChiTiet hdct 
					WHERE hdct.HopDongFK = @HopDongID 
					AND(hdct.DmLoaiREF = 42)
					AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF =18)
					AND hdct.DmSanPhamREF NOT IN (736,817) -- chi phí công nghệ, chi phi marketing fee
					AND hdct.DeletedStatus = 1
					ORDER BY hdct.HopDongChiTietID
				),0)

				EXEC [dbo].[ThucChay_Insert_GTTD_All_ThucChayDaTinh_HDCT_Admatic_WithHopDong] 
				@FromDate = @FromDate,
				@ToDate  = @todate,
				@NgayGhiNhanThucChay = @todate,
				@HopDongID = @HopDongID, 
				@HopDongChiTietID = @HopDongChiTietID,
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
																AND ct.DmSanPhamREF NOT IN (736,817) -- chi phí công nghệ, chi phi marketing fee
																AND ct.DeletedStatus = 1
																AND ct.DmSanPhamREF = hdct.DmSanPhamREF)
													AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF =18)
													GROUP BY HopDongFK),0)

				--TH2.1 NẾU KHÔNG TỒN TẠI HDCT CÓ NHIEU SẢN PHẨM VÀ HDCT(MOT HOAC NHIEU HDCT) BỊ XÓA CÓ SẢN PHẨM LÀ DUY NHẤT TRONG HD
				IF(@ExistAdmaticNhieuSanPham = 0 AND @ExistNhieuHDCTCungSanPham = 0)
				BEGIN
				    PRINT 'TH2.1 NẾU KHÔNG TỒN TẠI HDCT CÓ NHIEU SẢN PHẨM VÀ HDCT(MOT HOAC NHIEU HDCT) BỊ XÓA CÓ SẢN PHẨM LÀ DUY NHẤT TRONG HD => THUC HIEN DOI TRU'
					--2. THUC HIEN DOI TRU TOAN BO THUCCHAYDATINH CUA HOPDONG VOI ADMATIC
					--EXEC [dbo].[ThucChay_Insert_GTTD_All_ThucChayDaTinh_Admatic_WithHopDong] 
					--@FromDate = @FromDate,
					--@ToDate = @todate,
					--@NgayGhiNhanThucChay = @todate,
					--@HopDongID = @HopDongID, 
					--@GhiChu = @GhiChu_doitru

					SET @HopDongChiTietID = ISNULL((SELECT TOP (1) hdct.HopDongChiTietID FROM dbo.HopDongChiTiet hdct 
					WHERE hdct.HopDongFK = @HopDongID 
					AND(hdct.DmLoaiREF = 42)
					AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF =18)
					AND hdct.DmSanPhamREF NOT IN (736,817) -- chi phí công nghệ, chi phi marketing fee
					AND hdct.DeletedStatus = 1
					ORDER BY hdct.HopDongChiTietID
					),0)

					EXEC [dbo].[ThucChay_Insert_GTTD_All_ThucChayDaTinh_HDCT_Admatic_WithHopDong] 
					@FromDate = @FromDate,
					@ToDate  = @todate,
					@NgayGhiNhanThucChay = @todate,
					@HopDongID = @HopDongID, 
					@HopDongChiTietID = @HopDongChiTietID,
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
END


```
