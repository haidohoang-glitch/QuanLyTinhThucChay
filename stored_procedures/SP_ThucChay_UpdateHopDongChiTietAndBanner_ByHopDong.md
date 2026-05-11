# Stored Procedure: `ThucChay_UpdateHopDongChiTietAndBanner_ByHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-05-22 10:09:54.367000
- **Ngày sửa cuối**: 2024-10-14 16:26:44.020000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner]
CREATE PROCEDURE  [dbo].[ThucChay_UpdateHopDongChiTietAndBanner_ByHopDong]
	@HopDongID INT
AS
BEGIN

--Update HopDongChiTietREF Tu Viec Thuc HIen Ket Noi Bang Tay Giua BannerID & Phan Bo Hop Dong
DECLARE @BannerID nvarchar(50)
DECLARE @TileThucChayHDCTVaBanner FLOAT,@TongViewHD BIGINT, @TongGoi INT =0

DECLARE Record_Cursor_v7 CURSOR FOR 
	SELECT DISTINCT tchdctab.DmBannerID
	FROM dbo.ThucChayHopDongChiTietAndBanner tchdctab
	INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID =  tchdctab.HopDongChiTietREF
	INNER JOIN (SELECT hd.HopDongID FROM dbo.HopDong hd WHERE hd.DeletedStatus = 0 AND hd.TrangThaiHopDong NOT IN(0,3)) hd
	ON hd.HopDongID = hdct.HopDongFK
	WHERE tchdctab.DaThucHienUpdateTiLe = 0
	AND tchdctab.HopDongREF = @HopDongID
	AND tchdctab.DeletedStatus = 0
	AND hdct.DeletedStatus = 0 
	--AND hdct.DmSanPhamREF IN (231,238,339,342,337,240,370,598,613,680,735,5056,5299)
	AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 2 --Nhom Tinh Branding
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
							))
	AND (([dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) <> 1) OR hdct.DmSanPhamREF = 680) --Đơn vị của hình thức not CPD and PR
OPEN Record_Cursor_v7

-- Perform the first fetch.
FETCH NEXT FROM Record_Cursor_v7 into @BannerID
		
WHILE @@FETCH_STATUS = 0
	BEGIN
		--1. Tinh tong view
		SET @TongViewHD =
		(
			SELECT 	sum(convert(bigint,ISNULL(T.SoLuong,0))*1000)
			FROM
			(
			SELECT  DISTINCT hdct.* --sum(convert(bigint,ISNULL(hdct.SoLuong,0))*1000)
			FROM ThucChayHopDongChiTietAndBanner tchdctab
			INNER JOIN HopDongChiTiet hdct ON hdct.HopDongChiTietID =  tchdctab.HopDongChiTietREF
			INNER JOIN (SELECT hd.HopDongID FROM dbo.HopDong hd WHERE hd.DeletedStatus = 0 AND hd.TrangThaiHopDong NOT IN(0,3)) hd
			ON hd.HopDongID = hdct.HopDongFK
			WHERE tchdctab.DmBannerID = convert(nvarchar(100),@BannerID)
			AND tchdctab.DeletedStatus = 0
			--AND hdct.DmSanPhamREF IN (231,238,339,342,337,240,370,598,613,680,735,5056,5299)
			AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 2 --Nhom Tinh Branding
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
							))
			AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) <> 1
			)T
		)
		SET @TongViewHD = ISNULL(@TongViewHD,0)
		--PRINT @TongViewHD;
		IF(@TongViewHD <> 0)
			BEGIN
				UPDATE dbo.ThucChayHopDongChiTietAndBanner
				SET
					ThucChayHopDongChiTietAndBanner.TiLeThucChayHDCTSoVoiBanner = ((Convert(FLOAT,SoLuong)*1000)/Convert(FLOAT,@TongViewHD)*100)
					,DaThucHienUpdateTiLe = 1

				FROM dbo.ThucChayHopDongChiTietAndBanner
				INNER JOIN dbo.HopDongChiTiet  ON HopDongChiTiet.HopDongChiTietID =  ThucChayHopDongChiTietAndBanner.HopDongChiTietREF
				INNER JOIN (SELECT hd.HopDongID FROM dbo.HopDong hd WHERE hd.DeletedStatus = 0 AND hd.TrangThaiHopDong NOT IN(0,3)) hd
				ON hd.HopDongID = HopDongChiTiet.HopDongFK
				WHERE ThucChayHopDongChiTietAndBanner.DmBannerID = convert(nvarchar(100),@BannerID)
				AND ThucChayHopDongChiTietAndBanner.DeletedStatus = 0
				--AND HopDongChiTiet.DmSanPhamREF IN (231,238,339,342,337,240,370,598,613,680,735,5056,5299)
				AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = HopDongChiTiet.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 2 --Nhom Tinh Branding
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
							))
				AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](HopDongChiTiet.DonViTinhREF, HopDongChiTiet.DonViTinh) <>1--= 3	
			END
		ELSE
		BEGIN
				UPDATE dbo.ThucChayHopDongChiTietAndBanner
				SET
					ThucChayHopDongChiTietAndBanner.TiLeThucChayHDCTSoVoiBanner = 100
					,DaThucHienUpdateTiLe = 1

				FROM dbo.ThucChayHopDongChiTietAndBanner
				INNER JOIN dbo.HopDongChiTiet  ON HopDongChiTiet.HopDongChiTietID =  ThucChayHopDongChiTietAndBanner.HopDongChiTietREF
				INNER JOIN (SELECT hd.HopDongID FROM dbo.HopDong hd WHERE hd.DeletedStatus = 0 AND hd.TrangThaiHopDong NOT IN(0,3)) hd
				ON hd.HopDongID = HopDongChiTiet.HopDongFK
				WHERE ThucChayHopDongChiTietAndBanner.DmBannerID = @BannerID
				AND ThucChayHopDongChiTietAndBanner.DeletedStatus = 0
				--AND HopDongChiTiet.DmSanPhamREF IN (231,238,339,342,337,240,370,598,613,680,735,5056,5299)
				AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = HopDongChiTiet.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 2 --Nhom Tinh Branding
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
							))
				AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](HopDongChiTiet.DonViTinhREF, HopDongChiTiet.DonViTinh)<>1-- = 3	
		END
		
		--Ap dung cho cac san pham CPR chay voi don vi tinh la goi
		set @TongGoi = (
			SELECT 	sum(convert(bigint,ISNULL(T.SoLuong,0))*1000)
			FROM
			(
				SELECT  DISTINCT hdct.* --sum(convert(bigint,ISNULL(hdct.SoLuong,0))*1000)
				FROM ThucChayHopDongChiTietAndBanner tchdctab
				INNER JOIN HopDongChiTiet hdct ON hdct.HopDongChiTietID =  tchdctab.HopDongChiTietREF
				INNER JOIN (SELECT hd.HopDongID FROM dbo.HopDong hd WHERE hd.DeletedStatus = 0 AND hd.TrangThaiHopDong NOT IN(0,3)) hd
				ON hd.HopDongID = hdct.HopDongFK
				WHERE tchdctab.DmBannerID = convert(nvarchar(100),@BannerID)
				AND tchdctab.DeletedStatus = 0
				AND hdct.DmSanPhamREF IN (680)
				)T	
		)
		IF(@TongGoi <> 0)
			BEGIN
				UPDATE dbo.ThucChayHopDongChiTietAndBanner
				SET
					ThucChayHopDongChiTietAndBanner.TiLeThucChayHDCTSoVoiBanner = (ROUND((Convert(FLOAT,SoLuong)*1000)/Convert(FLOAT,@TongGoi),5)*100)
					,DaThucHienUpdateTiLe = 1

				FROM dbo.ThucChayHopDongChiTietAndBanner
				INNER JOIN dbo.HopDongChiTiet  ON HopDongChiTiet.HopDongChiTietID =  ThucChayHopDongChiTietAndBanner.HopDongChiTietREF
				INNER JOIN (SELECT hd.HopDongID FROM dbo.HopDong hd WHERE hd.DeletedStatus = 0 AND hd.TrangThaiHopDong NOT IN(0,3)) hd
				ON hd.HopDongID = HopDongChiTiet.HopDongFK
				WHERE ThucChayHopDongChiTietAndBanner.DmBannerID = convert(nvarchar(100),@BannerID)
				AND ThucChayHopDongChiTietAndBanner.DeletedStatus = 0
				AND HopDongChiTiet.DmSanPhamREF IN (680)
			END
		ELSE
		BEGIN
				UPDATE dbo.ThucChayHopDongChiTietAndBanner
				SET
					ThucChayHopDongChiTietAndBanner.TiLeThucChayHDCTSoVoiBanner = 100
					,DaThucHienUpdateTiLe = 1

				FROM dbo.ThucChayHopDongChiTietAndBanner
				INNER JOIN dbo.HopDongChiTiet  ON HopDongChiTiet.HopDongChiTietID =  ThucChayHopDongChiTietAndBanner.HopDongChiTietREF
				INNER JOIN (SELECT hd.HopDongID FROM dbo.HopDong hd WHERE hd.DeletedStatus = 0 AND hd.TrangThaiHopDong NOT IN(0,3)) hd
				ON hd.HopDongID = HopDongChiTiet.HopDongFK
				WHERE ThucChayHopDongChiTietAndBanner.DmBannerID = @BannerID
				AND ThucChayHopDongChiTietAndBanner.DeletedStatus = 0
				AND HopDongChiTiet.DmSanPhamREF IN (680)
		END
		
		--UPDATE TH THUCTREO BI XOA, haidh comment 20210824
		UPDATE tc
		SET
			tc.TiLeThucChayHDCTSoVoiBanner = 0
			,tc.DaThucHienUpdateTiLe = 1
		FROM dbo.ThucChayHopDongChiTietAndBanner tc
		WHERE tc.DmBannerID = @BannerID
		AND tc.DeletedStatus = 1

	--PRINT @TongViewHD
	FETCH NEXT FROM Record_Cursor_v7 into @BannerID
END

CLOSE Record_Cursor_v7
DEALLOCATE Record_Cursor_v7

--SELECT '1'

END

--EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner]

```
