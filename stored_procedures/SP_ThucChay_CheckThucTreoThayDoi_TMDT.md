# Stored Procedure: `ThucChay_CheckThucTreoThayDoi_TMDT`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-06-24 16:59:13.273000
- **Ngày sửa cuối**: 2014-11-19 12:17:00.213000

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
--EXEC [ThucChay_CheckThucTreoThayDoi_TMDT] '2013-01-29'

CREATE PROCEDURE [dbo].[ThucChay_CheckThucTreoThayDoi_TMDT] 
-- Add the parameters for the stored procedure here
	@NgayThucHien DATETIME
AS
BEGIN
	-- Declare the return variable here
	DECLARE @HopDongREF INT, @SoHopDong NVARCHAR(50), @HopDongChiTietID INT
	-- Tin vip	241
	-- Box nổi bật	264
	-- Box sản phẩm Hot	300
	-- Siêu chăm sóc	268
	-- Tin vip xuyên trang	248
	-- sàn BĐS	270
	-- Tin nổi bật	243
	-- Top giao dịch hot 244
	-- Tin đính 249
	
	DECLARE Record_Cursor CURSOR  
	FOR
	    --LAY THONG TIN HOPDONGCHITIET CUA TAT CAC CAC THUC TREO DC NHAP HOAC SUA NGAYTHUCHIEN> THOIGIANBATDAU
		SELECT DISTINCT A.HopDongREF, A.SoHopDong ,A.HopDongChiTietREF
		FROM(
			   SELECT tchdctp.HopDongREF,
					  hd.SoHopDong,
					  tchdctp.HopDongChiTietREF,
					  tchdctp.ThoiGianBatDau,
					  tchdctp.ThoiGianKetThuc,
					  (   CASE 
							   WHEN tchdctp.CreatedAt >= tchdctp.LastModifiedAt THEN tchdctp.CreatedAt
							   ELSE tchdctp.LastModifiedAt
						  END
					  ) NgayThucHien
			   FROM HopDong hd INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
			   INNER JOIN ThucChayHopDongChiTiet tchdctp ON hdct.HopDongChiTietID = tchdctp.HopDongChiTietREF
				WHERE  tchdctp.ThoiGianBatDau IS NOT NULL
					  AND (   CASE 
								   WHEN tchdctp.CreatedAt >= tchdctp.LastModifiedAt THEN CONVERT(DATE,tchdctp.CreatedAt)
								   ELSE CONVERT(DATE,tchdctp.LastModifiedAt)
							  END
						  ) = @NgayThucHien
	                  AND hdct.DmSanPhamREF IN (241,264,300,268,248,270,243,244,249)
	                  AND hdct.DeletedStatus = 0
	                  AND hd.DeletedStatus = 0
	                  AND tchdctp.DeletedStatus = 0
			)A
		ORDER BY
			   A.HopDongREF, A.HopDongChiTietREF
			   
	
	OPEN Record_Cursor
	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong, @HopDongChiTietID 
	WHILE @@FETCH_STATUS = 0
	BEGIN
		PRINT @HopDongChiTietID
		EXEC [ThucChay_CheckHopDongCoThayDoi_TMDT] @HopDongREF ,@SoHopDong ,@HopDongChiTietID ,@NgayThucHien 
	    FETCH NEXT FROM Record_Cursor INTO @HopDongREF, @SoHopDong, @HopDongChiTietID 
	END
	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor
END

--EXEC [ThucChay_CheckThucTreoThayDoi_TMDT] '2013-01-29'

```
