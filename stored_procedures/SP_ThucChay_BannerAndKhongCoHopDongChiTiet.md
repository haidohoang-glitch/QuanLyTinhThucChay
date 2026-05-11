# Stored Procedure: `ThucChay_BannerAndKhongCoHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-11 10:13:48.890000
- **Ngày sửa cuối**: 2016-11-11 10:44:03.710000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DenNgay` | `datetime(8)` | No |

## Definition (Source Code)

```sql
--[ThucChay_BannerAndKhongCoHopDongChiTiet] '2015-08-26'
CREATE PROCEDURE [dbo].[ThucChay_BannerAndKhongCoHopDongChiTiet]
	@DenNgay DATETIME
AS
BEGIN

	--Update HopDongChiTietREF Tu Viec Thuc HIen Ket Noi Bang Tay Giua BannerID & Phan Bo Hop Dong
	DECLARE @ThucChayHopDongChiTietID INT,@DmBannerREF nvarchar(4000), @HopDongChiTietREF INT =0, @HopDongREF INT, @SoHopDong NVARCHAR(100) = '', @BookingREF INT =0, @DsNhanHangREF NVARCHAR(200), @BannerID nvarchar(50)
	DECLARE @CreatedBy NVARCHAR(50), @LastModifiedBy NVARCHAR(50), @DaThucHienUpdateTile TINYINT=1, @DeletedStatus INT
	DECLARE @ThoiGianBatDau datetime, @ThoiGianKetThuc DATETIME, @CreatedAt DATETIME, @LastModifiedAt DATETIME
	SET @DsNhanHangREF = ''

	--SELECT * FROM ThucChayHopDongAndBanner

	DELETE FROM ThucChayHopDongAndBanner WHERE CONVERT(DATE,LastModifiedAt) >= @DenNgay

	DECLARE Record_Cursor_HopDongbanner CURSOR FOR 
		SELECT  tc.ThucChayHopDongChiTietID ,tc.DmBannerREF,tc.HopDongREF,ISNULL(tc.HopDongChiTietREF,0)HopDongChiTietREF,ISNULL(tc.BookingREF,0)BookingREF, tc.DmNhanHangREF,tc.ThoiGianBatDau,tc.ThoiGianKetThuc
		, tc.CreatedBy, tc.CreatedAt, tc.LastModifiedBy, tc.LastModifiedAt, tc.DeletedStatus , hd.SoHopDong
		FROM dbo.ThucChayHopDongChiTiet tc
		INNER JOIN dbo.HopDong hd ON tc.HopDongREF = hd.HopDongID
		WHERE 1=1 
		AND (ISNULL(tc.BookingREF,0) =0 AND ISNULL(tc.HopDongChiTietREF,0) = 0 AND tc.DmHinhThucQuangCaoREF = 42) --HAIDH: chi thuc hien voi cac hinh thuc quang cao la Admatic va san pham la nhieu san pham
		AND ISNULL(tc.DmBannerREF,'') <> ''
		AND (
			case when tc.LastModifiedAt >= tc.CreatedAt THEN Convert(date,tc.LastModifiedAt)
			ELSE Convert(date,tc.CreatedAt)
			END
		 )  >= convert(date,@DenNgay) 
	
	OPEN Record_Cursor_HopDongbanner

	-- Perform the first fetch.
	FETCH NEXT FROM Record_Cursor_HopDongbanner into 
			@ThucChayHopDongChiTietID,@DmBannerREF,@HopDongREF,@HopDongChiTietREF,@BookingREF, @DsNhanHangREF,@ThoiGianBatDau,@ThoiGianKetThuc
			, @CreatedBy, @CreatedAt, @LastModifiedBy, @LastModifiedAt, @DeletedStatus, @SoHopDong
		
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
		
			IF(EXISTS(SELECT tchdctab.ThucChayHopDongChiTietID
						FROM ThucChayHopDongAndBanner tchdctab
					  WHERE tchdctab.HopDongREF = @HopDongREF
					AND tchdctab.DmBannerID = @DmBannerREF
					AND tchdctab.DeletedStatus = 0)
			)
			BEGIN
				UPDATE ThucChayHopDongAndBanner
				SET
					ThoiGianBatDau = @ThoiGianBatDau,
					ThoiGianKetThuc = @ThoiGianKetThuc,
					CreatedBy = @CreatedBy,
					CreatedAt = @CreatedAt,
					LastModifiedBy = @LastModifiedBy,
					LastModifiedAt = @LastModifiedAt,
					DeletedStatus = @DeletedStatus,
					DsNhanHangREF = @DsNhanHangREF,
					SoHopDong	  = @SoHopDong
				 WHERE HopDongREF = @HopDongREF
					AND DmBannerID = @DmBannerREF
					AND DeletedStatus = 0
			END
			ELSE
				BEGIN
					PRINT @BannerID
					--Insert thuc chay ThucChayHopDongChiTietID	
					Insert into dbo.ThucChayHopDongAndBanner
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
							  SoHopDong
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
					, @SoHopDong
				END
			FETCH NEXT FROM Record_Cursor1 into @BannerID
			end
		CLOSE Record_Cursor1
		DEALLOCATE Record_Cursor1
	
	FETCH NEXT FROM Record_Cursor_HopDongbanner into 
			@ThucChayHopDongChiTietID,@DmBannerREF,@HopDongREF,@HopDongChiTietREF,@BookingREF, @DsNhanHangREF,@ThoiGianBatDau,@ThoiGianKetThuc
			, @CreatedBy, @CreatedAt, @LastModifiedBy, @LastModifiedAt, @DeletedStatus, @SoHopDong
	END

	CLOSE Record_Cursor_HopDongbanner
	DEALLOCATE Record_Cursor_HopDongbanner

	SELECT '1'

END


```
