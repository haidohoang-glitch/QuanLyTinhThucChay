# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinhBySoHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:21:26.450000
- **Ngày sửa cuối**: 2021-05-03 15:15:15.490000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================


CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinhBySoHopDong] 
	@StartDate datetime,
	@EndDate DATETIME,
	@SoHopDong NVARCHAR(50),
	@DmSanPhamREF INT
AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @Count INT
	DECLARE @TypeProduct INT, @HDLechGiaYN NVARCHAR(50), @TenWebsite NVARCHAR(50), @DmWebsiteREF INT, @DmBannerREF INT
	set @NgayThucHien = @StartDate

	delete from dbo.ThucChayTemp

	--Xoa du lieu ThucChayDaTinh truoc khi tinh
	DELETE FROM dbo.ThucChayDaTinh
	WHERE convert(date,NgayThucHien)BETWEEN @StartDate AND @EndDate
	AND DmSanPhamREF IN (231,238,339,240,370,598,613,732,735,680)
	AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, DonViTinh) = 3	 --Đơn vị của hình thức CPM, TRUE REACH
	AND NOT ( DmLoaiBannerREF IN (17,18)OR DmHinhThucQuangCao IN (13,42))
	AND SoHopDong = @SoHopDong AND DmSanPhamREF = @DmSanPhamREF
	AND DotChayHopDong <> N'NGAY'
	AND DonViTinh <> N'TRUE REACH'
	
	while(@NgayThucHien <= @EndDate)
	Begin

		Insert into dbo.ThucChayTemp
		select tc.ThucChayID ,
               tc.SoHopDong ,
               tc.DanhsachDmBookingREF ,
               tc.DmSanPhamREF ,
               tc.TenSanPham ,
               tc.DmNhomWebsiteREF ,
               tc.TenNhomWebsite ,
               tc.DmWebsiteREF ,
               tc.TenWebsite ,
               tc.DmChienDichREF ,
               tc.TenChienDich ,
               tc.DmBannerREF ,
               tc.TenBanner ,
               tc.NgayThucHien ,
               tc.TongViewThucChay ,
               tc.TongClickThucChay ,
               tc.CreatedBy ,
               tc.CreatedAt ,
               tc.LastModifiedBy ,
               tc.LastModifiedAt ,
               tc.DeletedStatus ,
               tc.PrintStatus ,
               tc.RecordStatus ,
               tc.TongSoBaiViet ,
               tc.SoThuTuTheoNgay ,
               tc.TypeProduct ,
               tc.BannerType ,
               tc.UserName ,
               tc.SaleName ,
               tc.Email ,
               tc.LastTimeCalc ,
               tc.sys_date ,
               tc.IsReady ,
               tc.ProductUnitID ,
               tc.ProductUnitName ,
               tc.BannerTypeName ,
               tc.HopDongChiTietREF ,
               tc.CampainStatus ,
               tc.BannerStatus ,
               tc.IsNoiBo from dbo.ThucChay tc
		where Convert(date,NgayThucHien) = Convert(date,@NgayThucHien)
		AND TypeProduct  NOT IN (1,2)
		AND DmWebsiteREF <> 0
		AND SoHopDong = @SoHopDong
		AND (CASE 
		WHEN tc.TypeProduct = 14 THEN 598 
		WHEN TypeProduct = 15 THEN 613
		WHEN TypeProduct = 5 THEN 339
		WHEN TypeProduct = 8 THEN 240
		WHEN TypeProduct = 9 THEN 370
		WHEN TypeProduct = 18 THEN 735
		WHEN TypeProduct = 16 THEN 680
		ELSE TypeProduct
		END)= @DmSanPhamREF

		DECLARE Record_Cursor CURSOR FOR 
		SELECT distinct A.SoHopDong,A.TypeProduct,A.DmWebsiteREF, A.TenWebsite, A.DmBannerREF ,A.HDLechGiaYN
		  FROM
			(
				SELECT tct.SoHopDong,tct.TypeProduct, tct.DmWebsiteREF, tct.TenWebsite, tct.DmBannerREF,
				--dbo.ThucChay_CheckHopDongCoSanPhamLechDonGiaYN(tct.TypeProduct,tct.SoHopDong) HDLechGiaYN 
				'Y' HDLechGiaYN				
				FROM dbo.ThucChayTemp tct
			)A
		ORDER BY A.SoHopDong, A.TypeProduct	
		--WHERE A.HDLechGiaYN = 'Y'
		OPEN Record_Cursor

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor into @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF, @HDLechGiaYN
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
				EXEC dbo.ThucChay_InsertThucChayDaTinh 
													 @NgayThucHien = @NgayThucHien
													,@SoHopDong = @SoHopDong
													,@TypeProduct = @TypeProduct
													,@DmWebsiteREF = @DmWebsiteREF
													,@TenWebsite = @TenWebsite
													,@DmBannerREF = @DmBannerREF
			FETCH NEXT FROM Record_Cursor into @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF, @HDLechGiaYN
			END

		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor
		
		SET @NgayThucHien = dateadd(d,1,@NgayThucHien)

		DELETE FROM dbo.ThucChayTemp
	END
		
	SELECT '1'
END


--EXEC [ThucChay_ExcInsertThucChayDaTinh] '2014-06-03','2014-06-03'

```
