# Stored Procedure: `ThucChay_HopDongChiTietAndBannerCPDByHopDongChiTietREF`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-03-23 10:59:47.350000
- **Ngày sửa cuối**: 2017-04-10 17:35:39.087000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DenNgay` | `datetime(8)` | No |
| `@HopDongChiTietREF1` | `int(4)` | No |

## Definition (Source Code)

```sql
--exec [ThucChay_HopDongChiTietAndBannerCPDByHopDongChiTietREF]  '2017-03-29',502685


CREATE PROCEDURE [dbo].[ThucChay_HopDongChiTietAndBannerCPDByHopDongChiTietREF]
	@DenNgay DATETIME,
	@HopDongChiTietREF1 INT
AS
BEGIN

--Update HopDongChiTietREF Tu Viec Thuc HIen Ket Noi Bang Tay Giua BannerID & Phan Bo Hop Dong
DECLARE @ThucChayHopDongChiTietID INT,@DmBannerREF nvarchar(4000), @HopDongChiTietREF int, @HopDongREF int, @BookingREF int, @BannerID nvarchar(50)
DECLARE @CreatedBy NVARCHAR(50), @LastModifiedBy NVARCHAR(50), @DaThucHienUpdateTile TINYINT, @DeletedStatus INT
DECLARE @ThoiGianBatDau datetime, @ThoiGianKetThuc DATETIME, @CreatedAt DATETIME, @LastModifiedAt DATETIME
SET @DaThucHienUpdateTile = 1

DELETE FROM ThucChayHopDongChiTietAndBannerCPD
WHERE CONVERT(DATE,LastModifiedAt) >= @DenNgay AND HopDongChiTietREF = @HopDongChiTietREF1

DECLARE Record_Cursor CURSOR FOR 
	SELECT  ThucChayHopDongChiTietID ,DmBannerREF,HopDongREF,HopDongChiTietREF,BookingREF,ThoiGianBatDau,ThoiGianKetThuc
		, CreatedBy, CreatedAt, LastModifiedBy, LastModifiedAt, tc.DeletedStatus 
	FROM dbo.ThucChayHopDongChiTiet tc
	WHERE 
	HopDongChiTietREF >0 
	AND HopDongREF > 0
	AND DmBannerREF is not null 
	AND DmBannerREF <> ''
	AND (
		case when tc.LastModifiedAt >= tc.CreatedAt THEN Convert(date,tc.LastModifiedAt)
		ELSE Convert(date,tc.CreatedAt)
		END
	 )  >= convert(date,@DenNgay) 
	AND tc.HopDongChiTietREF IN (SELECT hdct.HopDongChiTietID
	                               FROM HopDongChiTiet hdct WHERE hdct.DmSanPhamREF IN (140, 228, 564, 549) AND hdct.DeletedStatus = 0	                               
	)
	AND tc.HopDongChiTietREF = @HopDongChiTietREF1
OPEN Record_Cursor

-- Perform the first fetch.
FETCH NEXT FROM Record_Cursor into 
		@ThucChayHopDongChiTietID,@DmBannerREF,@HopDongREF,@HopDongChiTietREF,@BookingREF,@ThoiGianBatDau,@ThoiGianKetThuc
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
		DELETE FROM ThucChayHopDongChiTietAndBannerCPD
		WHERE ThucChayHopDongChiTietID  = @ThucChayHopDongChiTietID 
			AND DmBannerID = @BannerID
			AND BookingREF = @BookingREF
			AND HopDongChiTietREF = @HopDongChiTietREF
		PRINT @BannerID
		--Insert thuc chay ThucChayHopDongChiTietID	
		Insert INTO dbo.ThucChayHopDongChiTietAndBannerCPD
		        ( ThucChayHopDongChiTietID ,
		          DmBannerID ,
		          HopDongChiTietREF ,
		          HopDongREF ,
		          BookingREF ,
		          ThoiGianBatDau ,
		          ThoiGianKetThuc ,
		          CreatedBy ,
		          CreatedAt ,
		          LastModifiedBy ,
		          LastModifiedAt ,
		          DeletedStatus
		        )
		select @ThucChayHopDongChiTietID,@BannerID,@HopDongChiTietREF,@HopDongREF,@BookingREF,@ThoiGianBatDau,@ThoiGianKetThuc		
		, @CreatedBy
		, @CreatedAt
		, @LastModifiedBy
		, @LastModifiedAt
		, @DeletedStatus
		FETCH NEXT FROM Record_Cursor1 into @BannerID
		end
	CLOSE Record_Cursor1
	DEALLOCATE Record_Cursor1
	
	FETCH NEXT FROM Record_Cursor into 
		@ThucChayHopDongChiTietID,@DmBannerREF,@HopDongREF,@HopDongChiTietREF,@BookingREF,@ThoiGianBatDau,@ThoiGianKetThuc
		, @CreatedBy, @CreatedAt, @LastModifiedBy, @LastModifiedAt, @DeletedStatus
END

CLOSE Record_Cursor
DEALLOCATE Record_Cursor

SELECT '1'



END

--EXEC [dbo].[ThucChay_HopDongChiTietAndBannerCPD] '2014-01-01'

--SELECT COUNT(*) FROM ThucChayHopDongChiTietAndBannerCPD

```
