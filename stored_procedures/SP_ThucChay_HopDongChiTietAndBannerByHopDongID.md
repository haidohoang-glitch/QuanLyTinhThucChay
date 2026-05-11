# Stored Procedure: `ThucChay_HopDongChiTietAndBannerByHopDongID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:21:17.070000
- **Ngày sửa cuối**: 2024-10-14 15:59:25.500000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |

## Definition (Source Code)

```sql
--[ThucChay_HopDongChiTietAndBanner] '2015-08-26'
CREATE PROCEDURE [dbo].[ThucChay_HopDongChiTietAndBannerByHopDongID]
	@HopDongID INT
AS
BEGIN

--Update HopDongChiTietREF Tu Viec Thuc HIen Ket Noi Bang Tay Giua BannerID & Phan Bo Hop Dong
DECLARE @ThucChayHopDongChiTietID INT,@DmBannerREF nvarchar(4000), @HopDongChiTietREF int, @HopDongREF int, @BookingREF INT, @DsNhanHangREF NVARCHAR(200), @BannerID nvarchar(50)
DECLARE @CreatedBy NVARCHAR(50), @LastModifiedBy NVARCHAR(50), @DaThucHienUpdateTile TINYINT, @DeletedStatus INT
DECLARE @ThoiGianBatDau datetime, @ThoiGianKetThuc DATETIME, @CreatedAt DATETIME, @LastModifiedAt DATETIME

SET @DaThucHienUpdateTile = 1
SET @DsNhanHangREF = ''

DELETE FROM ThucChayHopDongChiTietAndBanner WHERE HopDongREF = @HopDongID
DECLARE Record_Cursor_GTTD_CPM CURSOR FOR 
	SELECT  ThucChayHopDongChiTietID ,DmBannerREF,HopDongREF,HopDongChiTietREF,BookingREF, tc.DmNhanHangREF,ThoiGianBatDau,ThoiGianKetThuc
	, CreatedBy, CreatedAt, LastModifiedBy, LastModifiedAt, tc.DeletedStatus 
	FROM dbo.ThucChayHopDongChiTiet tc
	WHERE 
	HopDongChiTietREF >0 
	AND HopDongREF > 0
	AND tc.HopDongREF = @HopDongID
	AND DmBannerREF is not null 
	AND DmBannerREF <> ''
	
OPEN Record_Cursor_GTTD_CPM

-- Perform the first fetch.
FETCH NEXT FROM Record_Cursor_GTTD_CPM into 
		@ThucChayHopDongChiTietID,@DmBannerREF,@HopDongREF,@HopDongChiTietREF,@BookingREF, @DsNhanHangREF,@ThoiGianBatDau,@ThoiGianKetThuc
		, @CreatedBy, @CreatedAt, @LastModifiedBy, @LastModifiedAt, @DeletedStatus
		
WHILE @@FETCH_STATUS = 0
	BEGIN
		
	PRINT @HopDongREF
	PRINT @DmBannerREF
	
	DECLARE Record_Cursor1 CURSOR FOR 
	SELECT dbo.FormatString(item) FROM dbo.ArrayToTable(dbo.Array(@DmBannerREF,','))
	OPEN Record_Cursor1
	FETCH NEXT FROM Record_Cursor1 into @BannerID
	WHILE @@FETCH_STATUS = 0
		BEGIN
		--Delete khi ton tai ThucChayHopDongChiTietID
		--DELETE FROM ThucChayHopDongChiTietAndBanner
		--WHERE ThucChayHopDongChiTietID = @ThucChayHopDongChiTietID
		
		IF(EXISTS(SELECT tchdctab.ThucChayHopDongChiTietID
		            FROM ThucChayHopDongChiTietAndBanner tchdctab
		          WHERE tchdctab.HopDongREF = @HopDongREF
				AND tchdctab.HopDongChiTietREF = @HopDongChiTietREF
				AND tchdctab.DmBannerID = @DmBannerREF
				AND tchdctab.DeletedStatus = 0)
		)
		BEGIN
			UPDATE ThucChayHopDongChiTietAndBanner
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
				AND DeletedStatus = 0
		END
		ELSE
			BEGIN
				PRINT @BannerID
				--Insert thuc chay ThucChayHopDongChiTietID	
				Insert INTO dbo.ThucChayHopDongChiTietAndBanner
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
				          DsNhanHangREF
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
			END
		FETCH NEXT FROM Record_Cursor1 into @BannerID
		end
	CLOSE Record_Cursor1
	DEALLOCATE Record_Cursor1
	
FETCH NEXT FROM Record_Cursor_GTTD_CPM into 
		@ThucChayHopDongChiTietID,@DmBannerREF,@HopDongREF,@HopDongChiTietREF,@BookingREF, @DsNhanHangREF,@ThoiGianBatDau,@ThoiGianKetThuc
		, @CreatedBy, @CreatedAt, @LastModifiedBy, @LastModifiedAt, @DeletedStatus
END

CLOSE Record_Cursor_GTTD_CPM
DEALLOCATE Record_Cursor_GTTD_CPM

SELECT '1'



END

--EXEC [dbo].[ThucChay_HopDongChiTietAndBanner] '2014-09-22'

--SELECT COUNT(*) FROM ThucChayHopDongChiTietAndBanner

```
