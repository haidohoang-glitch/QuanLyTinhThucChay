# Stored Procedure: `ThucChay_UpdateHopDongChiTietAndBanner_Native_Ads_NgayThucHien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-05-20 11:12:43.517000
- **Ngày sửa cuối**: 2022-07-06 09:51:03.070000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner_Native_Ads_NgayThucHien]	@NgayThucHien = '2022-07-04'
CREATE PROCEDURE [dbo].[ThucChay_UpdateHopDongChiTietAndBanner_Native_Ads_NgayThucHien]
	@NgayThucHien DATETIME
AS
BEGIN

--Update HopDongChiTietREF Tu Viec Thuc HIen Ket Noi Bang Tay Giua BannerID & Phan Bo Hop Dong
DECLARE @BannerID nvarchar(50)
DECLARE @TileThucChayHDCTVaBanner FLOAT,@TongViewHD BIGINT, @TongGoi FLOAT =0


DECLARE R_Cursor_ThucTreo CURSOR FOR 
	SELECT DISTINCT tchdctab.DmBannerID
	FROM dbo.[ThucChayHopDongChiTietAndBanner_Native_Ads] tchdctab
	INNER JOIN 
	(SELECT hdct.* FROM dbo.HopDongChiTiet hdct 
		WHERE 1=1 	
		AND hdct.DeletedStatus = 0 
		AND hdct.DmSanPhamREF IN (821,5133,733)
		AND NOT ( hdct.DmLoaiBannerREF IN (17,18) OR hdct.DmLoaiREF IN (13,42))
		AND hdct.DonViTinhREF <> 3 --KHONG PHAI DON VI TINH NGAY
		--and HopDongChiTietID = 607989
	)hdct ON hdct.HopDongChiTietID =  tchdctab.HopDongChiTietREF
	INNER JOIN (SELECT HopDongID FROM dbo.HopDong WHERE DeletedStatus = 0 AND TrangThaiHopDong NOT IN (0,3)) hd
	ON hd.HopDongID = hdct.HopDongFK
	WHERE tchdctab.DaThucHienUpdateTiLe = 0
	AND tchdctab.DeletedStatus = 0
	UNION ALL
	SELECT DISTINCT tchdctab.DmBannerID
	FROM dbo.[ThucChayHopDongChiTietAndBanner_Native_Ads] tchdctab
	INNER JOIN 
	(SELECT hdct.* FROM dbo.HopDongChiTiet hdct 
		WHERE 1=1 	
		AND hdct.DeletedStatus = 0 
		AND hdct.DmSanPhamREF IN (821,5133,733)
		AND NOT ( hdct.DmLoaiBannerREF IN (17,18) OR hdct.DmLoaiREF IN (13,42))
		AND hdct.DonViTinhREF <> 3 --KHONG PHAI DON VI TINH NGAY
		--and HopDongChiTietID = 607989
	)hdct ON hdct.HopDongChiTietID =  tchdctab.HopDongChiTietREF
	INNER JOIN (SELECT HopDongID FROM dbo.HopDong WHERE DeletedStatus = 0 AND TrangThaiHopDong NOT IN (0,3)) hd
	ON hd.HopDongID = hdct.HopDongFK
	WHERE (tchdctab.DaThucHienUpdateTiLe = 1 AND Convert(date,tchdctab.LastmodifiedAt) = @NgayThucHien)


OPEN R_Cursor_ThucTreo

-- Perform the first fetch.
FETCH NEXT FROM R_Cursor_ThucTreo into @BannerID
		
WHILE @@FETCH_STATUS = 0
	BEGIN
		--TAO LOG DE CHECK XEM CO UPDATE BANNER TRONG NGAY KO
		insert into dbo.Log_ThucChayHopDongChitietAndBanner
		SELECT @BannerID as DmBanner, @NgayThucHien AS NgayThucHien, '[ThucChayHopDongChiTietAndBanner_Native_Ads] NGAY' AS Table_Name, 'Update' as Actions, getdate() createat 

		set @TongGoi = (
			SELECT 	sum(convert(bigint,ISNULL(T.SoLuong,0))*ISNULL(T.DonGia,0))
			FROM
			(
				SELECT  DISTINCT hdct.*
				FROM dbo.[ThucChayHopDongChiTietAndBanner_Native_Ads] tchdctab
				INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID =  tchdctab.HopDongChiTietREF
				INNER JOIN (SELECT HopDongID FROM dbo.HopDong WHERE DeletedStatus = 0 AND TrangThaiHopDong NOT IN (0,3) 
				--tuyetnta bổ sung tạm ngày 09/02/2021
				and Nam >=2020
				) hd
				ON hd.HopDongID = hdct.HopDongFK 
				WHERE tchdctab.DmBannerID = convert(nvarchar(100),@BannerID)
				AND tchdctab.DeletedStatus = 0
				AND hdct.DmSanPhamREF IN (821,5133,733)
				AND tchdctab.DmHinhThucQuangCaoID <> 42
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
				AND hdct.DmSanPhamREF IN (821,5133,733)
				AND tchdctab.DmHinhThucQuangCaoID <> 42
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
				AND hdct.DmSanPhamREF IN (821,5133,733)
				AND tchdctab.DmHinhThucQuangCaoID <> 42

				UPDATE TC
				SET TC.TiLeThucChayHDCTSoVoiBanner = 0
				FROM dbo.[ThucChayHopDongChiTietAndBanner_Native_Ads] TC
				WHERE TC.DeletedStatus = 1
		END
		
	PRINT @TongViewHD
	FETCH NEXT FROM R_Cursor_ThucTreo into @BannerID
END

CLOSE R_Cursor_ThucTreo
DEALLOCATE R_Cursor_ThucTreo

END

```
