# Stored Procedure: `ThucChay_UpdateHopDongChiTietAndBanner_ThanhTien_Admatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-06-19 15:02:12.747000
- **Ngày sửa cuối**: 2021-06-04 17:02:13.113000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
--EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner_ThanhTien_Admatic]
CREATE PROCEDURE [dbo].[ThucChay_UpdateHopDongChiTietAndBanner_ThanhTien_Admatic]
AS
BEGIN

--Update HopDongChiTietREF Tu Viec Thuc HIen Ket Noi Bang Tay Giua BannerID & Phan Bo Hop Dong
DECLARE @BannerID nvarchar(50)
DECLARE @TileThucChayHDCTVaBanner FLOAT,@TongViewHD BIGINT, @TongGoi FLOAT =0


DECLARE R_Cursor_ThucTreo CURSOR FOR 
	SELECT DISTINCT tchdctab.DmBannerREF
	FROM dbo.[ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic] tchdctab
	INNER JOIN 
	(SELECT hdct.* FROM dbo.HopDongChiTiet hdct 
		WHERE 1=1 	
		AND hdct.DeletedStatus = 0 
		--AND hdct.DmSanPhamREF IN (821,5133)
		AND NOT ( hdct.DmLoaiBannerREF IN (17,18) OR hdct.DmLoaiREF IN (13))
		AND hdct.DmLoaiREF = 42
		--AND hdct.DonViTinhREF <> 3 --KHONG PHAI DON VI TINH NGAY
	)hdct ON hdct.HopDongChiTietID =  tchdctab.HopDongChiTietREF
	INNER JOIN (SELECT HopDongID FROM dbo.HopDong WHERE DeletedStatus = 0 AND TrangThaiHopDong NOT IN (0,3)) hd
	ON hd.HopDongID = hdct.HopDongFK
	WHERE tchdctab.DaThucHienUpdateTiLe = 0
	AND tchdctab.DeletedStatus = 0

OPEN R_Cursor_ThucTreo

-- Perform the first fetch.
FETCH NEXT FROM R_Cursor_ThucTreo into @BannerID
		
WHILE @@FETCH_STATUS = 0
	BEGIN
		set @TongGoi = (
			SELECT 	sum(convert(float,ISNULL(T.SoLuong,0))*ISNULL(T.DonGia,0))
			FROM
			(
				SELECT  DISTINCT hdct.*
				FROM dbo.[ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic] tchdctab
				INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID =  tchdctab.HopDongChiTietREF and tchdctab.DmSanPhamREF = hdct.DmSanPhamREF
				INNER JOIN (SELECT HopDongID FROM dbo.HopDong WHERE DeletedStatus = 0 AND TrangThaiHopDong NOT IN (0,3)) hd
				ON hd.HopDongID = hdct.HopDongFK
				WHERE tchdctab.DmBannerREF = @BannerID
				AND tchdctab.DeletedStatus = 0
				AND hdct.DmLoaiREF = 42
				)T	
		)
		IF(@TongGoi <> 0)
			BEGIN
				UPDATE tt
				SET
					tt.TiLeThucChayHDCTSoVoiBanner = (ROUND((Convert(FLOAT,hdct.SoLuong*hdct.DonGia))/Convert(FLOAT,@TongGoi),5))*100
					,tt.DaThucHienUpdateTiLe = 1

				FROM dbo.[ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic] tt
				INNER JOIN dbo.HopDongChiTiet hdct  ON hdct.HopDongChiTietID =  tt.HopDongChiTietREF
				INNER JOIN (SELECT HopDongID FROM dbo.HopDong WHERE DeletedStatus = 0 AND TrangThaiHopDong NOT IN (0,3)) hd
				ON hd.HopDongID = hdct.HopDongFK
				WHERE tt.DmBannerREF = @BannerID
				AND tt.DeletedStatus = 0
				AND hdct.DmLoaiREF = 42
			END
		ELSE
		BEGIN
				UPDATE tt
				SET
					tt.TiLeThucChayHDCTSoVoiBanner = 100
					,tt.DaThucHienUpdateTiLe = 1

				FROM dbo.[ThucChayHopDongChiTietAndBanner_ThanhTien_Admatic] tt
				INNER JOIN dbo.HopDongChiTiet hdct  ON hdct.HopDongChiTietID =  tt.HopDongChiTietREF
				INNER JOIN (SELECT HopDongID FROM dbo.HopDong WHERE DeletedStatus = 0 AND TrangThaiHopDong NOT IN (0,3)) hd
				ON hd.HopDongID = hdct.HopDongFK
				WHERE tt.DmBannerREF = @BannerID
				AND tt.DeletedStatus = 0
				AND hdct.DmLoaiREF = 42
		END
		
	PRINT @TongViewHD
	FETCH NEXT FROM R_Cursor_ThucTreo into @BannerID
END

CLOSE R_Cursor_ThucTreo
DEALLOCATE R_Cursor_ThucTreo

END

```
