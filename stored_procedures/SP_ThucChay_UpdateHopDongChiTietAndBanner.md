# Stored Procedure: `ThucChay_UpdateHopDongChiTietAndBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-07-16 14:45:29.077000
- **Ngày sửa cuối**: 2022-12-21 15:15:42.213000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner]
CREATE PROCEDURE [dbo].[ThucChay_UpdateHopDongChiTietAndBanner]
AS
BEGIN

--Update HopDongChiTietREF Tu Viec Thuc HIen Ket Noi Bang Tay Giua BannerID & Phan Bo Hop Dong
DECLARE @BannerID nvarchar(50)
DECLARE @TileThucChayHDCTVaBanner FLOAT,@TongViewHD BIGINT, @TongGoi INT =0

--INSERT INTO [dbo].[Log_SP_Call]
--           ([SP_NAME]
--           ,[SP_TIME_CALL]
--           ,[SP_END_TIME_CALL]
--           ,[NOTE]
--		   , VALUE_INPUT)
--     VALUES
--           ('[ThucChay_UpdateHopDongChiTietAndBanner]'
--           , GETDATE()
--           , NULL
--           , ''
--		   , ''
--			)

DECLARE Record_Cursor CURSOR FOR 
	SELECT DISTINCT tchdctab.DmBannerID
	FROM dbo.ThucChayHopDongChiTietAndBanner tchdctab
	INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID =  tchdctab.HopDongChiTietREF
	INNER JOIN (SELECT hd.HopDongID FROM dbo.HopDong hd WHERE hd.DeletedStatus = 0 AND hd.TrangThaiHopDong NOT IN(0,3)) hd
	ON hd.HopDongID = hdct.HopDongFK
	WHERE tchdctab.DaThucHienUpdateTiLe = 0
	AND tchdctab.DeletedStatus = 0
	AND hdct.DeletedStatus = 0 
	--AND hdct.DmSanPhamREF IN (231,238,339,342,337,240,370,598,613,680,735,5056,5299)
	AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = hdct.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 2 --Nhom Tinh Branding
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
							))
	AND (([dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) <> 1) OR hdct.DmSanPhamREF = 680) --Đơn vị của hình thức not CPD and PR
OPEN Record_Cursor

-- Perform the first fetch.
FETCH NEXT FROM Record_Cursor into @BannerID
		
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
	FETCH NEXT FROM Record_Cursor into @BannerID
END

CLOSE Record_Cursor
DEALLOCATE Record_Cursor

--SELECT '1'

END

--EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner]

```
