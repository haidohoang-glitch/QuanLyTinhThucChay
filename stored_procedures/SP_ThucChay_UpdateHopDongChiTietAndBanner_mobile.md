# Stored Procedure: `ThucChay_UpdateHopDongChiTietAndBanner_mobile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-05-10 11:22:48.453000
- **Ngày sửa cuối**: 2018-08-20 11:12:06.937000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

--EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner_mobile]
CREATE PROCEDURE [dbo].[ThucChay_UpdateHopDongChiTietAndBanner_mobile]
AS
BEGIN

--Update HopDongChiTietREF Tu Viec Thuc HIen Ket Noi Bang Tay Giua BannerID & Phan Bo Hop Dong
DECLARE @BannerID nvarchar(50)
DECLARE @TileThucChayHDCTVaBanner FLOAT,@TongViewHD BIGINT, @TongGoi INT =0


DECLARE Record_Cursor CURSOR FOR 
	SELECT DISTINCT tchdctab.DmBannerID
	FROM dbo.ThucChayHopDongChiTietAndBanner tchdctab
	INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID =  tchdctab.HopDongChiTietREF
	INNER JOIN (SELECT hd.HopDongID FROM dbo.HopDong hd WHERE hd.DeletedStatus = 0 AND hd.TrangThaiHopDong NOT IN(0,3)) hd
	ON hd.HopDongID = hdct.HopDongFK
	WHERE tchdctab.DaThucHienUpdateTiLe = 0
	AND tchdctab.DeletedStatus = 0
	AND hdct.DeletedStatus = 0 
	AND hdct.DmSanPhamREF IN (342)
	
	
	--AND (([dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) <> 1)) --Đơn vị của hình thức not CPD and PR
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
			FROM dbo.ThucChayHopDongChiTietAndBanner tchdctab
			INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID =  tchdctab.HopDongChiTietREF
			INNER JOIN (SELECT hd.HopDongID FROM dbo.HopDong hd WHERE hd.DeletedStatus = 0 AND hd.TrangThaiHopDong NOT IN(0,3)) hd
			ON hd.HopDongID = hdct.HopDongFK
			WHERE tchdctab.DmBannerID = convert(nvarchar(100),@BannerID)
			AND tchdctab.DeletedStatus = 0
			AND hdct.DmSanPhamREF IN (342)
			--AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](hdct.DonViTinhREF, hdct.DonViTinh) <> 1
			)T
		)
		SET @TongViewHD = ISNULL(@TongViewHD,0)
		PRINT @TongViewHD;
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
				AND HopDongChiTiet.DmSanPhamREF IN (342)
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
				AND HopDongChiTiet.DmSanPhamREF IN (342)
				--AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](HopDongChiTiet.DonViTinhREF, HopDongChiTiet.DonViTinh)<>1-- = 3	
		END
		
		
	PRINT @TongViewHD
	FETCH NEXT FROM Record_Cursor into @BannerID
END

CLOSE Record_Cursor
DEALLOCATE Record_Cursor

SELECT '1'

END

--EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner]

```
