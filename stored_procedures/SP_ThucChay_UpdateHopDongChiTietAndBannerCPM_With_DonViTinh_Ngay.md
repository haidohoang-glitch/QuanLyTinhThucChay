# Stored Procedure: `ThucChay_UpdateHopDongChiTietAndBannerCPM_With_DonViTinh_Ngay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-02-22 11:22:46.037000
- **Ngày sửa cuối**: 2019-08-02 14:40:09.980000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBannerCPM_With_DonViTinh_Ngay]
CREATE PROCEDURE [dbo].[ThucChay_UpdateHopDongChiTietAndBannerCPM_With_DonViTinh_Ngay]
AS
BEGIN

--Update HopDongChiTietREF Tu Viec Thuc HIen Ket Noi Bang Tay Giua BannerID & Phan Bo Hop Dong
DECLARE @BannerID nvarchar(50)
DECLARE @TileThucChayHDCTVaBanner FLOAT,@TongViewHD BIGINT, @TongGoi INT =0


DECLARE Record_Cursor CURSOR FOR 
	SELECT DISTINCT tchdctab.DmBannerID
	FROM dbo.ThucChayHopDongChiTietAndBanner tchdctab
	INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID =  tchdctab.HopDongChiTietREF
	WHERE tchdctab.DaThucHienUpdateTiLe = 0
	AND tchdctab.DeletedStatus = 0
	AND hdct.DeletedStatus = 0 
	AND hdct.DmSanPhamREF IN (231,238,339,240,598,613,370,680,735,342,821)
	AND NOT ( hdct.DmLoaiBannerREF IN (17,18) OR hdct.DmLoaiREF IN (13,42))
	AND hdct.DonViTinhREF IN (3,4) --DON VI TINH LA NGAY, TUAN
OPEN Record_Cursor

-- Perform the first fetch.
FETCH NEXT FROM Record_Cursor into @BannerID
		
WHILE @@FETCH_STATUS = 0
	BEGIN
		--1. Tinh tong view
		SET @TongViewHD =
		(
			SELECT 	sum(convert(bigint,ISNULL(T.SoLuong,0)))
			FROM
			(
				SELECT  DISTINCT hdct.* --sum(convert(bigint,ISNULL(hdct.SoLuong,0))*1000)
				FROM dbo.ThucChayHopDongChiTietAndBanner tchdctab
				INNER JOIN 
				(SELECT hdct.HopDongChiTietID,
				(CASE WHEN hdct.DonViTinhREF = 4 THEN hdct.SoLuong *7 --quy tuan ra ngay
					ELSE hdct.SoLuong
				END) AS SoLuong
				FROM dbo.HopDongChiTiet hdct
				WHERE hdct.DeletedStatus = 0
				AND hdct.DmSanPhamREF IN (231,238,339,240,598,613,370,680,735,342,821)
				AND NOT ( hdct.DmLoaiBannerREF IN (17,18) OR hdct.DmLoaiREF IN (13,42))
				AND hdct.DonViTinhREF IN (3,4) --DON VI TINH LA NGAY,TUAN
				)hdct ON hdct.HopDongChiTietID =  tchdctab.HopDongChiTietREF
				WHERE tchdctab.DmBannerID = convert(nvarchar(100),@BannerID)
				AND tchdctab.DeletedStatus = 0
				
			)T
		)
		SET @TongViewHD = ISNULL(@TongViewHD,0)
		--PRINT @TongViewHD;
		IF(@TongViewHD <> 0)
			BEGIN
				UPDATE tchdct
				SET
					tchdct.TiLeThucChayHDCTSoVoiBanner = ((Convert(FLOAT,hdct.SoLuong))/Convert(FLOAT,@TongViewHD)*100)
					,tchdct.DaThucHienUpdateTiLe = 1
				FROM dbo.ThucChayHopDongChiTietAndBanner tchdct
				INNER JOIN 
				(
					SELECT hdct.HopDongChiTietID,
					(CASE WHEN hdct.DonViTinhREF = 4 THEN hdct.SoLuong *7 --quy tuan ra ngay
					ELSE hdct.SoLuong
					END) AS SoLuong
					FROM dbo.HopDongChiTiet hdct WHERE hdct.DeletedStatus = 0
					AND  hdct.DmSanPhamREF IN (231,238,339,240,598,613,370,680,735,342,821)
					AND NOT ( hdct.DmLoaiBannerREF IN (17,18) OR hdct.DmLoaiREF IN (13,42))
					AND hdct.DonViTinhREF IN (3,4) --DON VI TINH LA NGAY
				)hdct  ON hdct.HopDongChiTietID =  tchdct.HopDongChiTietREF
				WHERE tchdct.DmBannerID = convert(nvarchar(100),@BannerID)
				AND tchdct.DeletedStatus = 0
				
			END
		ELSE
		BEGIN
				UPDATE tchdct
				SET
					tchdct.TiLeThucChayHDCTSoVoiBanner = 100
					,tchdct.DaThucHienUpdateTiLe = 1
				FROM dbo.ThucChayHopDongChiTietAndBanner tchdct
				INNER JOIN 
				(
					SELECT hdct.HopDongChiTietID,
					(CASE WHEN hdct.DonViTinhREF = 4 THEN hdct.SoLuong *7 --quy tuan ra ngay
					ELSE hdct.SoLuong
					END) AS SoLuong
					FROM dbo.HopDongChiTiet hdct
					WHERE hdct.DeletedStatus = 0
					AND hdct.DmSanPhamREF IN (231,238,339,240,598,613,370,680,735,342, 821)
					AND NOT ( hdct.DmLoaiBannerREF IN (17,18) OR hdct.DmLoaiREF IN (13,42))
					AND hdct.DonViTinhREF IN (3,4) --DON VI TINH LA NGAY
				)hdct  ON hdct.HopDongChiTietID =  tchdct.HopDongChiTietREF
				WHERE tchdct.DmBannerID = @BannerID
				AND tchdct.DeletedStatus = 0
				
		END
	--PRINT @TongViewHD
	FETCH NEXT FROM Record_Cursor into @BannerID
END

CLOSE Record_Cursor
DEALLOCATE Record_Cursor

SELECT '1'

END

```
