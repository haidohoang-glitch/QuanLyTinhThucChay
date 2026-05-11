# Stored Procedure: `CheckBannerThucChayThucTreoByDmSanPhamREF`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-15 15:19:34.240000
- **Ngày sửa cuối**: 2017-03-24 17:03:44.970000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamREF` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql

--EXEC CheckBannerThucChayThucTreoByDmSanPhamREF 342, '2016-01-01'
CREATE PROCEDURE [dbo].[CheckBannerThucChayThucTreoByDmSanPhamREF] 
@DmSanPhamREF INT,
@NgayThucHien DATETIME
AS
BEGIN
DELETE FROM ThucChayHopDongChiTietAndBanner_Test 
DECLARE @ThucChayHopDongChiTietID INT,@DmBannerREF nvarchar(4000), @HopDongChiTietREF int, @HopDongREF int, @BookingREF INT, @DsNhanHangREF NVARCHAR(200), @BannerID nvarchar(50)
DECLARE @CreatedBy NVARCHAR(50), @LastModifiedBy NVARCHAR(50), @DaThucHienUpdateTile TINYINT, @DeletedStatus INT
DECLARE @ThoiGianBatDau datetime, @ThoiGianKetThuc DATETIME, @CreatedAt DATETIME, @LastModifiedAt DATETIME
SET @DaThucHienUpdateTile = 1
SET @DsNhanHangREF = ''


DECLARE Record_Cursor CURSOR FOR 
	SELECT  ThucChayHopDongChiTietID ,DmBannerREF,HopDongREF,HopDongChiTietREF,BookingREF , tc.DmNhanHangREF,ThoiGianBatDau,ThoiGianKetThuc
	, CreatedBy, CreatedAt, LastModifiedBy, LastModifiedAt, tc.DeletedStatus 
	FROM dbo.ThucChayHopDongChiTiet tc
	WHERE 
	HopDongChiTietREF >0 
	AND HopDongREF > 0
	AND DmBannerREF is not null 
	AND DmBannerREF <> ''
	AND tc.ThoiGianBatDau >=@NgayThucHien
	AND tc.HopDongChiTietREF IN (SELECT HopDongChiTietID FROM dbo.HopDongChiTiet WHERE DmSanPhamREF =@DmSanPhamREF AND DeletedStatus = 0)

OPEN Record_Cursor

-- Perform the first fetch.
FETCH NEXT FROM Record_Cursor into 
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
		            FROM ThucChayHopDongChiTietAndBanner_Test tchdctab
		          WHERE tchdctab.HopDongREF = @HopDongREF
				AND tchdctab.HopDongChiTietREF = @HopDongChiTietREF
				AND tchdctab.DmBannerID = @DmBannerREF
				AND tchdctab.DeletedStatus = 0)
		)
		BEGIN
			UPDATE ThucChayHopDongChiTietAndBanner_Test
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
				Insert into dbo.ThucChayHopDongChiTietAndBanner_Test
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
	
	FETCH NEXT FROM Record_Cursor into 
		@ThucChayHopDongChiTietID,@DmBannerREF,@HopDongREF,@HopDongChiTietREF,@BookingREF, @DsNhanHangREF,@ThoiGianBatDau,@ThoiGianKetThuc
		, @CreatedBy, @CreatedAt, @LastModifiedBy, @LastModifiedAt, @DeletedStatus
END

CLOSE Record_Cursor
DEALLOCATE Record_Cursor
-------------------------

END

```
