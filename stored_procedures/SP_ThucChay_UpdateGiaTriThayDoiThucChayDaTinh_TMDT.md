# Stored Procedure: `ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_TMDT`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-24 16:59:27.667000
- **Ngày sửa cuối**: 2015-11-04 12:55:41.620000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_TMDT] '2014-03-13'

CREATE PROCEDURE [dbo].[ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_TMDT] 
	-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	DECLARE	@HopDongREF INT, @HopDongChiTietID INT , @SoHopDong NVARCHAR(50), @NgayThucHienBF DATETIME
	DECLARE @IsExistHDCT INT
	-- Tin vip	241
	-- Box nổi bật	264
	-- Box sản phẩm Hot	300
	-- Siêu chăm sóc	268
	-- Tin vip xuyên trang	248
	-- sàn BĐS	270
	-- Tin nổi bật	243
	-- Top giao dịch hot 244
	-- Tin đính 249
	-- Box giá vàng 385

	PRINT CONVERT(NVARCHAR(20),@NgayThucHien)
	SET @NgayThucHienBF = DATEADD(DAY,-1,@NgayThucHIen)
	SET @IsExistHDCT = 0
	
	DECLARE Record_Cursor CURSOR FOR 
		
		SELECT distinct hdtd.HopDongFK, hdtd.SoHopDong, dchdcttd.HopDongChiTietREF
		FROM 
		  (	SELECT distinct hdtd.*, hd.SoHopDong from HopDongThayDoi hdtd
			INNER JOIN HopDong hd ON hd.HopDongID = hdtd.HopDongFK
		  ) hdtd
		INNER JOIN DotChayHopDongChiTietThayDoi dchdcttd ON hdtd.HopDongThayDoiID = dchdcttd.HopDongREF
		INNER JOIN HopDongChiTiet hdct ON hdct.HopDongChiTietID = dchdcttd.HopDongChiTietREF
		WHERE 1=1
		AND hdct.DmLoaiREF <> 13 --Khong Update gia tri thay doi cho HTQC Mua Ngoai 
		AND convert(date,hdtd.NgayThayDoi) = @NgayThucHIen
		AND hdct.DmSanPhamREF IN (241,264,300,268,248,270,243,244,249)

	OPEN Record_Cursor

	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong, @HopDongChiTietID
		
	WHILE @@FETCH_STATUS = 0
		BEGIN
			--CHECK VA UPDATE NEU HD CT CO THAY DOI THONG TIN VE GIA, SL, CK
			PRINT @SoHopDong +';hdct:'+ CONVERT(NVARCHAR(50), @HopDongChiTietID)
			SET @IsExistHDCT =
			(
				SELECT count(hdct.HopDongChiTietID) FROM HopDongChiTiet hdct
				WHERE hdct.HopDongChiTietID = @HopDongChiTietID
				AND hdct.DeletedStatus = 0
			)
			IF(@IsExistHDCT >0)
			BEGIN
				EXEC [ThucChay_CheckHopDongCoThayDoi_TMDT] @HopDongREF ,@SoHopDong ,@HopDongChiTietID ,@NgayThucHien	
			END
			ELSE
				BEGIN
					PRINT 'HDCT BI Xoa'
				END
		FETCH NEXT FROM Record_Cursor into @HopDongREF, @SoHopDong, @HopDongChiTietID
		END
	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor
	SELECT 2
END

--EXEC [ThucChay_UpdateGiaTriThayDoiThucChayDaTinh_TMDT] '2014-04-20'

```
