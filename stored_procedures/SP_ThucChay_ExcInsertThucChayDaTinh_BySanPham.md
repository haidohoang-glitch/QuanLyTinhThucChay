# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinh_BySanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:21:26.703000
- **Ngày sửa cuối**: 2018-11-02 16:20:43.263000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

/*
EXEC [dbo].[ThucChay_ExcInsertThucChayDaTinh_BySanPham] '2018-09-21','2018-09-21', 370
*/
CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinh_BySanPham] 
	@StartDate datetime,
	@EndDate DATETIME,
	@DmSanPhamREF INT
AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @Count INT
	DECLARE @SoHopDong NVARCHAR(50), @TypeProduct INT, @HDLechGiaYN NVARCHAR(50), @TenWebsite NVARCHAR(50), @DmWebsiteREF INT, @DmBannerREF INT
	set @NgayThucHien = @StartDate

	delete from dbo.ThucChayTemp

	--Xoa du lieu ThucChayDaTinh truoc khi tinh
	--DELETE FROM dbo.ThucChayDaTinh
	--WHERE convert(date,NgayThucHien)BETWEEN @StartDate AND @EndDate
	--AND DmSanPhamREF IN (231,238,339,240,598,613,370,680,735)
	--AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, DonViTinh) = 3	 --Đơn vị của hình thức CPM, TRUE REACH
	--AND NOT ( DmLoaiBannerREF IN (17,18)OR DmHinhThucQuangCao IN (13,42))
	--AND DonViTinh <> N'TRUE REACH'
	--AND DmSanPhamREF = @DmSanPhamREF
	--AND DotChayHopDong <> N'NGAY'

	while(@NgayThucHien <= @EndDate)
	Begin

		Insert into dbo.ThucChayTemp
		        ( ThucChayID ,
		          SoHopDong ,
		          DanhsachDmBookingREF ,
		          DmSanPhamREF ,
		          TenSanPham ,
		          DmNhomWebsiteREF ,
		          TenNhomWebsite ,
		          DmWebsiteREF ,
		          TenWebsite ,
		          DmChienDichREF ,
		          TenChienDich ,
		          DmBannerREF ,
		          TenBanner ,
		          NgayThucHien ,
		          TongViewThucChay ,
		          TongClickThucChay ,
		          CreatedBy ,
		          CreatedAt ,
		          LastModifiedBy ,
		          LastModifiedAt ,
		          DeletedStatus ,
		          PrintStatus ,
		          RecordStatus ,
		          TongSoBaiViet ,
		          SoThuTuTheoNgay ,
		          TypeProduct ,
		          BannerType ,
		          UserName ,
		          SaleName ,
		          Email ,
		          LastTimeCalc ,
		          sys_date ,
		          IsReady ,
		          ProductUnitID ,
		          ProductUnitName ,
		          BannerTypeName ,
		          HopDongChiTietREF ,
		          CampainStatus ,
		          BannerStatus ,
		          IsNoiBo
		        )
	
		select  ThucChayID ,
		          SoHopDong ,
		          DanhsachDmBookingREF ,
		          DmSanPhamREF ,
		          TenSanPham ,
		          DmNhomWebsiteREF ,
		          TenNhomWebsite ,
		          DmWebsiteREF ,
		          TenWebsite ,
		          DmChienDichREF ,
		          TenChienDich ,
		          DmBannerREF ,
		          TenBanner ,
		          NgayThucHien ,
		          TongViewThucChay ,
		          TongClickThucChay ,
		          CreatedBy ,
		          CreatedAt ,
		          LastModifiedBy ,
		          LastModifiedAt ,
		          DeletedStatus ,
		          PrintStatus ,
		          RecordStatus ,
		          TongSoBaiViet ,
		          SoThuTuTheoNgay ,
		          TypeProduct ,
		          BannerType ,
		          UserName ,
		          SaleName ,
		          Email ,
		          LastTimeCalc ,
		          sys_date ,
		          IsReady ,
		          ProductUnitID ,
		          ProductUnitName ,
		          BannerTypeName ,
		          HopDongChiTietREF ,
		          CampainStatus ,
		          BannerStatus ,
		          IsNoiBo from dbo.ThucChay 
		where Convert(DATE,NgayThucHien) = Convert(DATE,@NgayThucHien)
		AND TypeProduct NOT IN (1,2,17, -3)
		AND DmWebsiteREF <> 0
		AND [dbo].[GetProductIDByTypeProduct](TypeProduct) = @DmSanPhamREF
		--AND SoHopDong = 'qc5031217'

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
				--PRINT @SoHopDong
				--PRINT  @TypeProduct
				--PRINT  @DmWebsiteREF
				--PRINT @TenWebsite
				--PRINT @DmBannerREF
				--PRINT dbo.FormatDate(@NgayThucHien)

				EXEC dbo.ThucChay_InsertThucChayDaTinh @NgayThucHien, @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF
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
