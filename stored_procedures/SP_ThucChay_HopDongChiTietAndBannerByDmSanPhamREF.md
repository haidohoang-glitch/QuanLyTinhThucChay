# Stored Procedure: `ThucChay_HopDongChiTietAndBannerByDmSanPhamREF`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:21:17.280000
- **Ngày sửa cuối**: 2017-03-22 15:11:42.623000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamREF` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_HopDongChiTietAndBannerByDmSanPhamREF] 342, '2017-02-24'
CREATE PROCEDURE [dbo].[ThucChay_HopDongChiTietAndBannerByDmSanPhamREF]
	-- Add the parameters for the stored procedure here
	@DmSanPhamREF INT,
	@NgayThucHien DATETIME
AS
BEGIN
	                            
	DECLARE @ThucChayHopDongChiTietID INT,@DmBannerREF nvarchar(4000), @HopDongChiTietREF int, @HopDongREF int, @BookingREF int, @DsNhanHangREF NVARCHAR(200),
	@BannerID nvarchar(50)
	DECLARE @CreatedBy NVARCHAR(50), @LastModifiedBy NVARCHAR(50), @DaThucHienUpdateTile TINYINT, @DeletedStatus INT
	DECLARE @ThoiGianBatDau datetime, @ThoiGianKetThuc DATETIME, @CreatedAt DATETIME, @LastModifiedAt DATETIME
	
	SET @DsNhanHangREF = ''
	
	--DELETE FROM 
	/*select * from ThucChayHopDongChiTietAndBanner WHERE HopDongChiTietREF IN (SELECT hdct.HopDongChiTietID
	                            FROM HopDongChiTiet hdct WHERE hdct.DmSanPhamREF = 342)

*/
	DECLARE Record_Cursor CURSOR FOR 

		SELECT  tc.ThucChayHopDongChiTietID,tc.DmBannerREF,tc.HopDongREF,tc.HopDongChiTietREF,tc.BookingREF, tc.DmNhanHangREF ,tc.ThoiGianBatDau,tc.ThoiGianKetThuc
				, tc.CreatedBy, tc.CreatedAt, tc.LastModifiedBy, tc.LastModifiedAt, tc.DeletedStatus 
		  FROM ThucChayHopDongChiTiet tc 
		  LEFT JOIN HopDongChiTiet hdct ON tc.HopDongChiTietREF = hdct.HopDongChiTietID
		  LEFT JOIN HopDong hd ON tc.HopDongREF = hd.HopDongID
		WHERE 1=1 AND hdct.DmSanPhamREF = 342
			AND tc.DeletedStatus <> 1
			AND hdct.DeletedStatus <> 1
			and HopDongChiTietREF >0 
			AND HopDongREF > 0
			AND tc.DmBannerREF is not null 
			AND tc.DmBannerREF NOT IN ('','0')
			AND hd.TrangThaiHopDong <> 3
			--AND hd.Nam >=2014
			AND hdct.HopDongChiTietID  IN 
					(SELECT HopDongChiTietID FROM dbo.HopDongChiTiet WHERE DmSanPhamREF = 342 AND 
					NOT (DmLoaiREF IN (13,42) OR DmLoaiBannerREF = 18 OR DmLoaiNenTangREF = 8 OR DmLoaiBannerREF = 17 )
					AND DeletedStatus =0
					--AND HopDongFK = 48772 
					)
			
			AND CONVERT(DATE,tc.LastModifiedAt) >=@NgayThucHien
				
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
			
			IF(EXISTS(SELECT tchdctab.ThucChayHopDongChiTietID
		            FROM ThucChayHopDongChiTietAndBanner tchdctab
		          WHERE tchdctab.HopDongREF = @HopDongREF
				AND tchdctab.HopDongChiTietREF = @HopDongChiTietREF
				AND tchdctab.DmBannerID = @DmBannerREF
				AND tchdctab.DeletedStatus = 0)
			)
			BEGIN
			PRINT 'ton tai'
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
					PRINT '1' print @BannerID
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
		
	FETCH NEXT FROM Record_Cursor into 
					@ThucChayHopDongChiTietID,@DmBannerREF,@HopDongREF,@HopDongChiTietREF,@BookingREF, @DsNhanHangREF,@ThoiGianBatDau,@ThoiGianKetThuc
					, @CreatedBy, @CreatedAt, @LastModifiedBy, @LastModifiedAt, @DeletedStatus
	END

	CLOSE Record_Cursor
	DEALLOCATE Record_Cursor


	EXEC [dbo].[ThucChay_UpdateHopDongChiTietAndBanner_mobile]

END

```
