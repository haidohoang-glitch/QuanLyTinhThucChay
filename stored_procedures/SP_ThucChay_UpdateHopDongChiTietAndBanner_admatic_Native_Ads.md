# Stored Procedure: `ThucChay_UpdateHopDongChiTietAndBanner_admatic_Native_Ads`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2018-12-10 16:01:00.730000
- **Ngày sửa cuối**: 2021-05-26 09:35:22.290000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner_Native_Ads]
CREATE PROCEDURE [dbo].[ThucChay_UpdateHopDongChiTietAndBanner_admatic_Native_Ads]
AS
BEGIN

--Update HopDongChiTietREF Tu Viec Thuc HIen Ket Noi Bang Tay Giua BannerID & Phan Bo Hop Dong
DECLARE @BannerID nvarchar(50)
DECLARE @TileThucChayHDCTVaBanner FLOAT,@TongViewHD BIGINT, @TongGoi INT =0


DECLARE Record_Cursor CURSOR FOR 
	SELECT DISTINCT tchdctab.DmBannerID
	FROM dbo.[ThucChayHopDongChiTietAndBanner_Native_Ads] tchdctab
	INNER JOIN 
	(SELECT hdct.* FROM dbo.HopDongChiTiet hdct 
		WHERE 1=1 	
		AND hdct.DeletedStatus = 0 
		AND hdct.DmSanPhamREF IN (821, 5133)
		AND hdct.DmLoaiREF = 42
		AND NOT ( hdct.DmLoaiBannerREF IN (17,18) OR hdct.DmLoaiREF IN (13))
		AND hdct.DonViTinhREF <> 3 --KHONG PHAI DON VI TINH NGAY
	)hdct ON hdct.HopDongChiTietID =  tchdctab.HopDongChiTietREF
	INNER JOIN (SELECT HopDongID FROM dbo.HopDong WHERE DeletedStatus = 0 AND TrangThaiHopDong NOT IN (0,3)) hd
	ON hd.HopDongID = hdct.HopDongFK
	WHERE tchdctab.DaThucHienUpdateTiLe = 0
	AND tchdctab.DeletedStatus = 0

OPEN Record_Cursor

-- Perform the first fetch.
FETCH NEXT FROM Record_Cursor into @BannerID
		
WHILE @@FETCH_STATUS = 0
	BEGIN
		set @TongGoi = (
			SELECT 	sum(convert(bigint,ISNULL(T.SoLuong,0))*ISNULL(T.DonGia,0))
			FROM
			(
				SELECT  DISTINCT hdct.*
				FROM dbo.[ThucChayHopDongChiTietAndBanner_Native_Ads] tchdctab
				INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID =  tchdctab.HopDongChiTietREF
				INNER JOIN (SELECT HopDongID FROM dbo.HopDong WHERE DeletedStatus = 0 AND TrangThaiHopDong NOT IN (0,3)) hd
				ON hd.HopDongID = hdct.HopDongFK
				WHERE tchdctab.DmBannerID = convert(nvarchar(100),@BannerID)
				AND tchdctab.DeletedStatus = 0
				AND hdct.DmSanPhamREF IN (821, 5133)
				AND tchdctab.DmHinhThucQuangCaoID = 42
				)T	
		)
		IF(@TongGoi <> 0)
			BEGIN
				UPDATE tchdctab
				SET
					tchdctab.TiLeThucChayHDCTSoVoiBanner = (ROUND((Convert(FLOAT,hdct.SoLuong*hdct.DonGia))/Convert(FLOAT,@TongGoi),5))*100
					,tchdctab.DaThucHienUpdateTiLe = 1

				FROM dbo.[ThucChayHopDongChiTietAndBanner_Native_Ads] tchdctab
				INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID =  tchdctab.HopDongChiTietREF
				INNER JOIN (SELECT HopDongID FROM dbo.HopDong WHERE DeletedStatus = 0 AND TrangThaiHopDong NOT IN (0,3)) hd
				ON hd.HopDongID = hdct.HopDongFK
				WHERE tchdctab.DmBannerID = convert(nvarchar(100),@BannerID)
				AND tchdctab.DeletedStatus = 0
				AND hdct.DmSanPhamREF IN (821, 5133)
				AND tchdctab.DmHinhThucQuangCaoID = 42
			END
		ELSE

		BEGIN
				UPDATE tchdctab
				SET
					tchdctab.TiLeThucChayHDCTSoVoiBanner = 100
					,tchdctab.DaThucHienUpdateTiLe = 1

				FROM dbo.[ThucChayHopDongChiTietAndBanner_Native_Ads] tchdctab
				INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID =  tchdctab.HopDongChiTietREF
				INNER JOIN (SELECT HopDongID FROM dbo.HopDong WHERE DeletedStatus = 0 AND TrangThaiHopDong NOT IN (0,3)) hd
				ON hd.HopDongID = hdct.HopDongFK
				WHERE tchdctab.DmBannerID = @BannerID
				AND tchdctab.DeletedStatus = 0
				AND hdct.DmSanPhamREF IN (821, 5133)
				AND tchdctab.DmHinhThucQuangCaoID = 42
		END
		
	PRINT @TongViewHD
	FETCH NEXT FROM Record_Cursor into @BannerID
END

CLOSE Record_Cursor
DEALLOCATE Record_Cursor

END

```
