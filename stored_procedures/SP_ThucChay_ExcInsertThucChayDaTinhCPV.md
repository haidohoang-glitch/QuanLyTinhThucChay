# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinhCPV`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:21:25.483000
- **Ngày sửa cuối**: 2021-06-11 09:04:44.837000

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

--EXEC [ThucChay_ExcInsertThucChayDaTinhCPV] '2014-10-01','2014-10-01'

CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinhCPV] 
	@StartDate datetime,
	@EndDate datetime
AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @Count INT
	DECLARE @SoHopDong NVARCHAR(50), @TypeProduct INT, @HDLechGiaYN NVARCHAR(50)
	, @TenWebsite NVARCHAR(50), @DmWebsiteREF INT, @DmBannerREF INT
	set @NgayThucHien = @StartDate
	
	--INSERT INTO [dbo].[Log_SP_Call]
 --          ([SP_NAME]
 --          ,[SP_TIME_CALL]
 --          ,[SP_END_TIME_CALL]
 --          ,[NOTE]
	--	   , VALUE_INPUT)
 --    VALUES
 --          ('[ThucChay_ExcInsertThucChayDaTinhCPV]'
 --          ,GETDATE()
 --          ,NULL
 --          ,''
	--	   , '@StartDate = ' + CONVERT(NVARCHAR(50),@StartDate,103) +
	--	     '@EndDate = ' + CONVERT(NVARCHAR(50),@EndDate,103)
	--		)

	DELETE FROM dbo.ThucChayTemp
	DELETE FROM dbo.ThucChayCPVTemp
	
	--Xoa du lieu ThucChayDaTinh truoc khi tinh
	DELETE FROM ThucChayDaTinh
	WHERE convert(date,NgayThucHien) BETWEEN @StartDate AND @EndDate
	AND DmSanPhamREF IN (240)
	AND DmHinhThucQuangCao <> 42
	AND DonViTinh = 'CPV' --Đơn vị của hình thức CPV	
	
	while(@NgayThucHien <= @EndDate)
	Begin
		DELETE FROM dbo.ThucChayTemp
		DELETE FROM dbo.ThucChayCPVTemp
		
		INSERT INTO dbo.ThucChayCPVTemp
		        ( typeproduct ,
		          ProductName ,
		          bannerid ,
		          totalview ,
		          percent_rate ,
		          CPV ,
		          NgayThucHien
		        )
		
		SELECT typeproduct ,
		          ProductName ,
		          bannerid ,
		          totalview ,
		          percent_rate ,
		          CPV ,
		          NgayThucHien FROM ThucChayCPV tcc
		WHERE convert(date,tcc.NgayThucHien) = @NgayThucHien
		
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
		AND TypeProduct NOT IN (1,2,17)
		AND DmWebsiteREF != 0

		DECLARE Record_Cursor CURSOR FOR 
		SELECT distinct A.SoHopDong,A.TypeProduct,A.DmWebsiteREF, A.TenWebsite, A.DmBannerREF
		  FROM
			(
				SELECT tct.SoHopDong,tct.TypeProduct, tct.DmWebsiteREF, tct.TenWebsite, tct.DmBannerREF
				FROM ThucChayTemp tct
				INNER JOIN ThucChayCPVTemp tcc ON tct.DmBannerREF = tcc.bannerid
				AND tct.NgayThucHien = tcc.NgayThucHien AND tcc.typeproduct = tct.TypeProduct
			)A
		ORDER BY A.SoHopDong, A.TypeProduct	
		--WHERE A.HDLechGiaYN = 'Y'
		OPEN Record_Cursor

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor into @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
				--PRINT 'vao 1'
				EXEC ThucChay_InsertThucChayDaTinhCPV @NgayThucHien, @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF
			FETCH NEXT FROM Record_Cursor into @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF
			END

		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor
		
		set @NgayThucHien = dateadd(d,1,@NgayThucHien)
		--delete from dbo.ThucChayTemp
	end 
	
	--SELECT '1'
END


--EXEC [ThucChay_ExcInsertThucChayDaTinhCPV] '2014-08-12','2014-08-13'

```
