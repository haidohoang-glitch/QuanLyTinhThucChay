# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinh_CPR_ByDVT_CPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:21:23.820000
- **Ngày sửa cuối**: 2021-06-11 14:39:17.050000

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
--EXEC [ThucChay_ExcInsertThucChayDaTinh_CPR_ByDVT_CPR] '2017-06-12','2017-06-12'

CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinh_CPR_ByDVT_CPR] 
	@StartDate datetime,
	@EndDate DATETIME

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
	DELETE FROM dbo.ThucChayDaTinh
	WHERE convert(date,NgayThucHien) BETWEEN @StartDate AND @EndDate
	AND DmSanPhamREF IN (680,598)
	AND DonViTinh = 'CPR'
	
	
	DELETE FROM dbo.ThucChayCPRTemp
	
	DELETE FROM dbo.ThucChayTemp
	
	WHILE(@NgayThucHien <= @EndDate)
	BEGIN
		
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
		
		select ThucChayID ,
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
		          IsNoiBo from ThucChay 
		where Convert(nvarchar(50),NgayThucHien,103) = Convert(nvarchar(50),@NgayThucHien,103)
		--where NgayThucHien = @NgayThucHien
		AND TypeProduct IN (16,14)
		AND DmWebsiteREF != 0

		
		INSERT INTO dbo.ThucChayCPRTemp
		        ( bannerid ,
		          uvngay ,
		          uv ,
		          typeproduct ,
		          ProductName ,
		          NgayThucHien ,
		          ThoiGianTao ,
		          uvhour ,
		          TVDenNgay ,
		          TCDenNgay
		        )
		SELECT bannerid ,
		          uvngay ,
		          uv ,
		          typeproduct ,
		          ProductName ,
		          NgayThucHien ,
		          ThoiGianTao ,
		          uvhour ,
		          TVDenNgay ,
		          TCDenNgay FROM ThucChayCPR tcc
		where Convert(nvarchar(50),NgayThucHien,103) = Convert(nvarchar(50),@NgayThucHien,103)
		--where NgayThucHien = @NgayThucHien
		--SELECT * FROM ThucChayCPR tcc
		--where Convert(date,NgayThucHien) = Convert(date,@NgayThucHien)
		

		
		DECLARE Record_Cursor CURSOR FOR 
		SELECT distinct A.SoHopDong,A.TypeProduct
		  FROM
			(
				SELECT tct.SoHopDong,tct.TypeProduct,tct.DmBannerREF FROM
				(
					SELECT distinct tct.SoHopDong,tct.TypeProduct,tct.DmBannerREF
					FROM ThucChayTemp tct
					INNER JOIN 
					(SELECT hd.SoHopDong FROM HopDong hd
						INNER JOIN HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
					    WHERE hdct.DmSanPhamREF IN (680,598) 
					    AND hdct.DonViTinhREF = 30
					    AND hd.TrangThaiHopDong <> 3
					    AND hdct.DeletedStatus = 0
					    --AND SoHopDong = @shd
					)hd ON hd.SoHopDong = tct.SoHopDong
				)tct
				INNER JOIN ThucChayCPRTemp tcc ON tcc.typeproduct = tct.TypeProduct AND tcc.bannerid = tct.DmBannerREF
			)A
		ORDER BY A.SoHopDong, A.TypeProduct	
		--WHERE A.HDLechGiaYN = 'Y'
		OPEN Record_Cursor

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor into @SoHopDong, @TypeProduct
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
				SET @HopDongID =
				ISNULL((
					SELECT TOP 1 hd.HopDongID FROM HopDong hd
					WHERE hd.SoHopDong = @SoHopDong
				),0)

				--PRINT @SoHopDong
				EXEC [dbo].[ThucChay_InsertThucChayDaTinh_CPR_ByDVT_CPR] @NgayThucHien ,@HopDongID,	@TypeProduct ,@DmWebsiteREF ,@TenWebsite 
			FETCH NEXT FROM Record_Cursor into @SoHopDong, @TypeProduct
			END

		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor
		
		--XU LY HD HUY
		set @NgayThucHien = dateadd(d,1,@NgayThucHien)
		DELETE FROM dbo.ThucChayTemp
		DELETE FROM ThucChayCPRTemp
	end 
	
	--SELECT '1'
END


--EXEC [ThucChay_ExcInsertThucChayDaTinh_CPR] '2014-06-03','2014-06-03'

```
