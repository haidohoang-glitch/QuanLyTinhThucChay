# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinh_CPR_ByDVT_CPR_dev`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-09 10:36:02.147000
- **Ngày sửa cuối**: 2017-06-09 10:55:10.203000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_ExcInsertThucChayDaTinh_CPR_ByDVT_CPR_dev] '2017-06-07','2017-06-07'

CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinh_CPR_ByDVT_CPR_dev] 
	@StartDate datetime,
	@EndDate datetime
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	DECLARE @SoHopDong NVARCHAR(50), @HopDongID INT
			, @TypeProduct INT
			, @TenWebsite NVARCHAR(50)
			, @DmWebsiteREF INT
			
	set @NgayThucHien = @StartDate
	SET @TenWebsite = '(Blanks)'
	SET @DmWebsiteREF = 826
	
	--Xoa du lieu ThucChayDaTinh truoc khi tinh
	--DELETE FROM ThucChayDaTinh
	--WHERE convert(date,NgayThucHien) BETWEEN @StartDate AND @EndDate
	--AND DmSanPhamREF IN (680)
	--AND DonViTinh = 'CPR'
	
	DELETE FROM ThucChayCPRTemp
	
	DELETE FROM dbo.ThucChayTemp
	
	WHILE(@NgayThucHien <= @EndDate)
	BEGIN
		
		Insert into dbo.ThucChayTemp
		select * from ThucChay 
		where Convert(nvarchar(50),NgayThucHien,103) = Convert(nvarchar(50),@NgayThucHien,103)
		AND TypeProduct IN (16,14)
		AND DmWebsiteREF != 0
		
		INSERT INTO ThucChayCPRTemp
		--SELECT * FROM ThucChayCPR tcc
		--where Convert(nvarchar(50),NgayThucHien,103) = Convert(nvarchar(50),@NgayThucHien,103)
		
		SELECT * FROM ThucChayCPR tcc
		where Convert(date,NgayThucHien) = Convert(date,@NgayThucHien)
		
		-----------
			SELECT distinct A.SoHopDong,A.TypeProduct
		  FROM
			(
				SELECT tct.SoHopDong,tct.TypeProduct,tct.DmBannerREF FROM
				(
					SELECT distinct tct.SoHopDong,tct.TypeProduct,tct.DmBannerREF
					FROM dbo.ThucChayTemp tct
					INNER JOIN 
					(SELECT hd.SoHopDong FROM HopDong hd
						INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
					    WHERE hdct.DmSanPhamREF IN (680,598) 
					    AND hdct.DonViTinhREF = 30
					    AND hd.TrangThaiHopDong <> 3
					    AND hdct.DeletedStatus = 0
					    AND SoHopDong = 'QC1080317'
					)hd ON hd.SoHopDong = tct.SoHopDong
					WHERE tct.NgayThucHien = '2017-06-07'
				)tct
				INNER JOIN dbo.ThucChayCPRTemp tcc ON tcc.typeproduct = tct.TypeProduct AND tcc.bannerid = tct.DmBannerREF
			)A
		ORDER BY A.SoHopDong, A.TypeProduct	
		-----------

		--DECLARE Record_Cursor CURSOR FOR 
		--SELECT distinct A.SoHopDong,A.TypeProduct
		--  FROM
		--	(
		--		SELECT tct.SoHopDong,tct.TypeProduct,tct.DmBannerREF FROM
		--		(
		--			SELECT distinct tct.SoHopDong,tct.TypeProduct,tct.DmBannerREF
		--			FROM ThucChayTemp tct
		--			INNER JOIN 
		--			(SELECT hd.SoHopDong FROM HopDong hd
		--				INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
		--			    WHERE hdct.DmSanPhamREF IN (680,598) 
		--			    AND hdct.DonViTinhREF = 30
		--			    AND hd.TrangThaiHopDong <> 3
		--			    AND hdct.DeletedStatus = 0
		--			)hd ON hd.SoHopDong = tct.SoHopDong
		--		)tct
		--		INNER JOIN ThucChayCPRTemp tcc ON tcc.typeproduct = tct.TypeProduct AND tcc.bannerid = tct.DmBannerREF
		--	)A
		--ORDER BY A.SoHopDong, A.TypeProduct	
		----WHERE A.HDLechGiaYN = 'Y'
		--OPEN Record_Cursor

		---- Perform the first fetch.
		--FETCH NEXT FROM Record_Cursor into @SoHopDong, @TypeProduct
			
		--WHILE @@FETCH_STATUS = 0
		--	BEGIN
		--		PRINT @SoHopDong
		--		PRINT @TypeProduct
		--		SET @HopDongID =
		--		ISNULL((
		--			SELECT TOP 1 hd.HopDongID FROM HopDong hd
		--			WHERE hd.SoHopDong = @SoHopDong
		--		),0)
		--		--EXEC [dbo].[ThucChay_InsertThucChayDaTinh_CPR_ByDVT_CPR] @NgayThucHien ,@HopDongID,	@TypeProduct ,@DmWebsiteREF ,@TenWebsite 
		--	FETCH NEXT FROM Record_Cursor into @SoHopDong, @TypeProduct
		--	END

		--CLOSE Record_Cursor
		--DEALLOCATE Record_Cursor
		
		--XU LY HD HUY
		set @NgayThucHien = dateadd(d,1,@NgayThucHien)
		DELETE FROM dbo.ThucChayTemp
		DELETE FROM ThucChayCPRTemp
	end 
	
	SELECT '1'
END


--EXEC [ThucChay_ExcInsertThucChayDaTinh_CPR] '2014-06-03','2014-06-03'

```
