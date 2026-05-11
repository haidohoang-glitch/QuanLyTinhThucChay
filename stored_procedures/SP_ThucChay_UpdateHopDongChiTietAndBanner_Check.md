# Stored Procedure: `ThucChay_UpdateHopDongChiTietAndBanner_Check`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-01-15 16:23:03.110000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.300000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[ThucChay_UpdateHopDongChiTietAndBanner_Check]
AS
BEGIN

--Update HopDongChiTietREF Tu Viec Thuc HIen Ket Noi Bang Tay Giua BannerID & Phan Bo Hop Dong
DECLARE @BannerID nvarchar(50)
DECLARE @TileThucChayHDCTVaBanner FLOAT,@TongViewHD BIGINT


DECLARE Record_Cursor CURSOR FOR 
	SELECT DISTINCT tchdctab.DmBannerID
	FROM ThucChayHopDongChiTietAndBanner tchdctab
	INNER JOIN HopDongChiTiet hdct ON hdct.HopDongChiTietID =  tchdctab.HopDongChiTietREF
	WHERE tchdctab.DaThucHienUpdateTiLe = 1
	AND tchdctab.DeletedStatus = 0
	AND hdct.DeletedStatus = 0 
	AND hdct.DmSanPhamREF IN (231,238,339,342,337,240,370)
	AND hdct.HopDongChiTietID = 51435
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
			WHERE tchdctab.DmBannerID = convert(nvarchar(100),@BannerID)
			AND tchdctab.DeletedStatus = 0
			AND hdct.DmSanPhamREF IN (231,238,339,342,337,240,370)
			)T
		)
		SET @TongViewHD = ISNULL(@TongViewHD,0)
		PRINT @TongViewHD;
		IF(@TongViewHD != 0)
			BEGIN
				UPDATE ThucChayHopDongChiTietAndBanner
				SET
					ThucChayHopDongChiTietAndBanner.TiLeThucChayHDCTSoVoiBanner = (ROUND((Convert(FLOAT,SoLuong)*1000)/Convert(FLOAT,@TongViewHD),3)*100)
					,DaThucHienUpdateTiLe = 1

				FROM ThucChayHopDongChiTietAndBanner
				INNER JOIN HopDongChiTiet  ON HopDongChiTiet.HopDongChiTietID =  ThucChayHopDongChiTietAndBanner.HopDongChiTietREF
				WHERE ThucChayHopDongChiTietAndBanner.DmBannerID = convert(nvarchar(100),@BannerID)
				AND ThucChayHopDongChiTietAndBanner.DeletedStatus = 0
				AND HopDongChiTiet.DmSanPhamREF IN (231,238,339,342,337,240,370)	
			END
		ELSE
		BEGIN
				UPDATE ThucChayHopDongChiTietAndBanner
				SET
					ThucChayHopDongChiTietAndBanner.TiLeThucChayHDCTSoVoiBanner = 100
					,DaThucHienUpdateTiLe = 1

				FROM ThucChayHopDongChiTietAndBanner
				INNER JOIN HopDongChiTiet  ON HopDongChiTiet.HopDongChiTietID =  ThucChayHopDongChiTietAndBanner.HopDongChiTietREF
				WHERE ThucChayHopDongChiTietAndBanner.DmBannerID = @BannerID
				AND ThucChayHopDongChiTietAndBanner.DeletedStatus = 0
				AND HopDongChiTiet.DmSanPhamREF IN (231,238,339,342,337,240,370)	
			END
	PRINT @TongViewHD
	FETCH NEXT FROM Record_Cursor into @BannerID
END

CLOSE Record_Cursor
DEALLOCATE Record_Cursor

SELECT '1'

END

--EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner_Check]

```
