# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinh_bySP)`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-16 18:20:48.633000
- **Ngày sửa cuối**: 2017-06-16 18:23:54.227000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmsanphamREF` | `int(4)` | No |
| `@Typeproduct` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
/*
Exec [dbo].[ThucChay_ExcInsertThucChayDaTinh_bySP)] 
	'2017-06-15',
	'2017-06-15',
	680,
	16

*/

CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinh_bySP)] 
	@StartDate datetime,
	@EndDate DATETIME,
	@DmsanphamREF INT,
	@Typeproduct INT
AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @Count INT
	DECLARE @SoHopDong NVARCHAR(50), @HDLechGiaYN NVARCHAR(50), @TenWebsite NVARCHAR(50), @DmWebsiteREF INT, @DmBannerREF INT
	set @NgayThucHien = @StartDate
	delete from dbo.ThucChayTemp
	--Xoa du lieu ThucChayDaTinh truoc khi tinh
	DELETE FROM ThucChayDaTinh
	WHERE convert(date,NgayThucHien)BETWEEN @StartDate AND @EndDate
	AND DmSanPhamREF =@DmsanphamREF
	AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, DonViTinh) = 3	 --Đơn vị của hình thức CPM, TRUE REACH
	AND NOT ( DmLoaiBannerREF IN (17,18)OR DmHinhThucQuangCao IN (13,42))

	while(@NgayThucHien <= @EndDate)
	Begin

		Insert into dbo.ThucChayTemp
		select * from ThucChay 
		where Convert(nvarchar(50),NgayThucHien,103) = Convert(nvarchar(50),@NgayThucHien,103)
		AND TypeProduct = @Typeproduct
		AND DmWebsiteREF != 0
		DECLARE Record_Cursor CURSOR FOR 
		SELECT distinct A.SoHopDong,A.TypeProduct,A.DmWebsiteREF, A.TenWebsite, A.DmBannerREF ,A.HDLechGiaYN
		  FROM
			(
				SELECT tct.SoHopDong,tct.TypeProduct, tct.DmWebsiteREF, tct.TenWebsite, tct.DmBannerREF,
				--dbo.ThucChay_CheckHopDongCoSanPhamLechDonGiaYN(tct.TypeProduct,tct.SoHopDong) HDLechGiaYN 
				'Y' HDLechGiaYN				
				FROM ThucChayTemp tct
			)A
		ORDER BY A.SoHopDong, A.TypeProduct	
		--WHERE A.HDLechGiaYN = 'Y'
		OPEN Record_Cursor

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor into @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF, @HDLechGiaYN
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
			IF(@HDLechGiaYN = 'Y')
				BEGIN
					--PRINT @SoHopDong
					EXEC ThucChay_InsertThucChayDaTinh @NgayThucHien, @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF
					--PRINT 'Y'
				END
			ELSE
				BEGIN
					--EXEC ThucChay_InsertThucChayDaTinh_ByHDLoaiSP @NgayThucHien, @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite
					PRINT ''
					--PRINT 'N'
				END
			
			FETCH NEXT FROM Record_Cursor into @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF, @HDLechGiaYN
			END

		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor
		
		--XU LY HD HUY
		--HAIDH COMMENT PHAN CHUC NANG KIEM SOAT HOPDONG HUY
		--EXEC [ThucChay_UpdateGiaTriThayDoi_HDHuy] @NgayThucHien, @NgayThucHien
		set @NgayThucHien = dateadd(d,1,@NgayThucHien)
		delete from dbo.ThucChayTemp
	end 
	
	SELECT '1'
END


--EXEC [ThucChay_ExcInsertThucChayDaTinh] '2014-06-03','2014-06-03'

```
