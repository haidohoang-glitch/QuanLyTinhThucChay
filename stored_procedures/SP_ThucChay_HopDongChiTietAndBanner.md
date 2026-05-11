# Stored Procedure: `ThucChay_HopDongChiTietAndBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:21:17.697000
- **Ngày sửa cuối**: 2021-08-24 17:04:56.067000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DenNgay` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--[ThucChay_HopDongChiTietAndBanner] '2021-08-23'
CREATE PROCEDURE [dbo].[ThucChay_HopDongChiTietAndBanner]
	@DenNgay DATETIME
AS
BEGIN

DECLARE @ThucChayHopDongChiTietID INT,@DmBannerREF nvarchar(4000), @HopDongChiTietREF int, @HopDongREF int, @BookingREF INT, @DsNhanHangREF NVARCHAR(200), @BannerID nvarchar(50)
DECLARE @CreatedBy NVARCHAR(50), @LastModifiedBy NVARCHAR(50), @DaThucHienUpdateTile TINYINT =0, @DeletedStatus INT
DECLARE @ThoiGianBatDau datetime, @ThoiGianKetThuc DATETIME, @CreatedAt DATETIME, @LastModifiedAt DATETIME
SET @DaThucHienUpdateTile = 1
SET @DsNhanHangREF = ''

--INSERT INTO [dbo].[Log_SP_Call]
--           ([SP_NAME]
--           ,[SP_TIME_CALL]
--           ,[SP_END_TIME_CALL]
--           ,[NOTE]
--		   , VALUE_INPUT)
--     VALUES
--           ('[ThucChay_HopDongChiTietAndBanner]'
--           ,GETDATE()
--           ,NULL
--           ,''
--		   , '@DenNgay = ' + CONVERT(NVARCHAR(50),@DenNgay,103) 
--			)

--DELETE FROM dbo.ThucChayHopDongChiTietAndBanner WHERE CONVERT(DATE,LastModifiedAt) >= @DenNgay

DECLARE Record_Cursor CURSOR FOR 
	SELECT  ThucChayHopDongChiTietID ,DmBannerREF,HopDongREF,HopDongChiTietREF,BookingREF, tc.DmNhanHangREF,ThoiGianBatDau,ThoiGianKetThuc
	, CreatedBy, CreatedAt, LastModifiedBy, LastModifiedAt, tc.DeletedStatus 
	FROM dbo.ThucChayHopDongChiTiet tc
	WHERE HopDongChiTietREF >0 
	AND HopDongREF > 0
	--AND tc.DeletedStatus =0 --HAIDH COMMENT KHI HOPDONGCHITIET BI XOA 20210824
	AND DmBannerREF is not null 
	AND DmBannerREF <> ''
	AND (
		CASE WHEN tc.LastModifiedAt >= tc.CreatedAt THEN Convert(date,tc.LastModifiedAt)
		ELSE Convert(date,tc.CreatedAt)
		END
	 )  >= convert(date,@DenNgay) 
	AND HopDongChiTietREF NOT IN (SELECT HopDongChiTietID FROM dbo.HopDongChiTiet 
								WHERE (TenLoaiNenTang LIKE '%Retargeting%' OR DmLoaiBannerREF = 17 OR DmLoaiNenTangREF = 8 )
								AND DeletedStatus <> 1)
OPEN Record_Cursor

-- Perform the first fetch.
FETCH NEXT FROM Record_Cursor into 
		@ThucChayHopDongChiTietID,@DmBannerREF,@HopDongREF,@HopDongChiTietREF,@BookingREF, @DsNhanHangREF,@ThoiGianBatDau,@ThoiGianKetThuc
		, @CreatedBy, @CreatedAt, @LastModifiedBy, @LastModifiedAt, @DeletedStatus
		
WHILE @@FETCH_STATUS = 0
	BEGIN
		
		--PRINT @HopDongREF
		--PRINT @DmBannerREF
	
		DECLARE Record_Cursor1 CURSOR FOR 
		SELECT dbo.FormatString(item) FROM dbo.ArrayToTable(dbo.Array(@DmBannerREF,','))
		OPEN Record_Cursor1
		FETCH NEXT FROM Record_Cursor1 into @BannerID
		WHILE @@FETCH_STATUS = 0
			BEGIN
				
			IF(EXISTS(SELECT tchdctab.ThucChayHopDongChiTietID
						FROM dbo.ThucChayHopDongChiTietAndBanner tchdctab
					  WHERE tchdctab.HopDongREF = @HopDongREF
					AND tchdctab.HopDongChiTietREF = @HopDongChiTietREF
					AND tchdctab.DmBannerID = @DmBannerREF
					AND ThucChayHopDongChiTietID = @ThucChayHopDongChiTietID
					)
			)
			BEGIN
				UPDATE dbo.ThucChayHopDongChiTietAndBanner
				SET
					ThoiGianBatDau = @ThoiGianBatDau,
					ThoiGianKetThuc = @ThoiGianKetThuc,
					CreatedBy = @CreatedBy,
					CreatedAt = @CreatedAt,
					LastModifiedBy = @LastModifiedBy,
					LastModifiedAt = @LastModifiedAt,
					DeletedStatus = @DeletedStatus,
					DsNhanHangREF = @DsNhanHangREF
				 WHERE HopDongREF = @HopDongREF
					AND HopDongChiTietREF = @HopDongChiTietREF
					AND DmBannerID = @DmBannerREF
					--AND DeletedStatus = 0 --HAIDH COMMENT VOI TH TREO BI HUY 20210824
					AND ThucChayHopDongChiTietID = @ThucChayHopDongChiTietID
				IF(@DeletedStatus = 1)
				BEGIN
					UPDATE tc
					SET
						tc.TiLeThucChayHDCTSoVoiBanner = 0
						,tc.DaThucHienUpdateTiLe = 1
					FROM dbo.ThucChayHopDongChiTietAndBanner tc
					WHERE tc.DeletedStatus = 1
					AND tc.ThucChayHopDongChiTietID = @ThucChayHopDongChiTietID
				END
			END
			ELSE
				BEGIN
					--PRINT @BannerID
					--Insert thuc chay ThucChayHopDongChiTietID	
					Insert into dbo.ThucChayHopDongChiTietAndBanner
							( ThucChayHopDongChiTietID ,
							  DmBannerID ,
							  HopDongChiTietREF ,
							  HopDongREF ,
							  BookingREF ,
							  ThoiGianBatDau ,
							  ThoiGianKetThuc ,
							  TiLeThucChayHDCTSoVoiBanner ,
							  DaThucHienUpdateTiLe ,
							  CreatedBy ,
							  CreatedAt ,
							  LastModifiedBy ,
							  LastModifiedAt ,
							  DeletedStatus ,
							  DsNhanHangREF,
							  LogTime
							)
					select @ThucChayHopDongChiTietID,@BannerID,@HopDongChiTietREF,@HopDongREF,@BookingREF,@ThoiGianBatDau,@ThoiGianKetThuc
					, 0
					, 0
					, @CreatedBy
					, @CreatedAt
					, @LastModifiedBy
					, @LastModifiedAt
					, @DeletedStatus
					, @DsNhanHangREF
					, GETDATE()
				END
			FETCH NEXT FROM Record_Cursor1 into @BannerID
			END
		CLOSE Record_Cursor1
		DEALLOCATE Record_Cursor1
	
	FETCH NEXT FROM Record_Cursor into 
		@ThucChayHopDongChiTietID,@DmBannerREF,@HopDongREF,@HopDongChiTietREF,@BookingREF, @DsNhanHangREF,@ThoiGianBatDau,@ThoiGianKetThuc
		, @CreatedBy, @CreatedAt, @LastModifiedBy, @LastModifiedAt, @DeletedStatus
END

CLOSE Record_Cursor
DEALLOCATE Record_Cursor
--SELECT '1'
END



```
