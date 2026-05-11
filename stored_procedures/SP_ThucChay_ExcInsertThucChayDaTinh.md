# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:21:26.923000
- **Ngày sửa cuối**: 2024-12-05 10:20:11.360000

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


CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinh] 
	@StartDate datetime,
	@EndDate datetime
AS
BEGIN
	DECLARE @NgayThucHien DATETIME, @Count INT
	DECLARE @SoHopDong NVARCHAR(50), @TypeProduct INT, @HDLechGiaYN NVARCHAR(50), @TenWebsite NVARCHAR(50), @DmWebsiteREF INT, @DmBannerREF INT

	set @NgayThucHien = @StartDate
	--log SP call

	--INSERT INTO [dbo].[Log_SP_Call]
 --          ([SP_NAME]
 --          ,[SP_TIME_CALL]
 --          ,[SP_END_TIME_CALL]
 --          ,[NOTE]
	--	   , VALUE_INPUT)
 --    VALUES
 --          ('[ThucChay_ExcInsertThucChayDaTinh]'
 --          ,GETDATE()
 --          ,NULL
 --          ,''
	--	   , '@StartDate = ' + CONVERT(NVARCHAR(50),@StartDate,103) +
	--	     ', @EndDate = ' + CONVERT(NVARCHAR(50),@EndDate,103)
	--		)

	DELETE FROM dbo.ThucChayTemp
	WHERE 1=1

	--Xoa du lieu ThucChayDaTinh truoc khi tinh
	DELETE FROM dbo.ThucChayDaTinh
	WHERE convert(date,NgayThucHien)BETWEEN @StartDate AND @EndDate
	--AND DmSanPhamREF IN (231,238,339,240,598,613,370,680,735,5056,5299)
	AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = dbo.ThucChayDaTinh.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 2 --Nhom Tinh Branding
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
	))
	AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, DonViTinh) = 3	 --Đơn vị của hình thức CPM, TRUE REACH
	AND NOT ( DmLoaiBannerREF IN (17,18)OR DmHinhThucQuangCao IN (13,42))
	AND DonViTinh <> N'TRUE REACH'
	AND DotChayHopDong <> N'NGAY'

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
		where CONVERT(DATE,NgayThucHien) = Convert(DATE,@NgayThucHien)
		AND TypeProduct NOT IN (1,2,17, -3, 10)
		AND DmWebsiteREF <> 0
		AND SoHopDong NOT IN (N'HD DEMO',N'TONGSANPHAM')
		DECLARE Record_Cursor CURSOR FOR 
		SELECT distinct A.SoHopDong,A.TypeProduct,A.DmWebsiteREF, A.TenWebsite, A.DmBannerREF ,A.HDLechGiaYN
		  FROM
			(
				SELECT tct.SoHopDong,tct.TypeProduct, tct.DmWebsiteREF, tct.TenWebsite, tct.DmBannerREF,
				'Y' HDLechGiaYN				
				FROM dbo.ThucChayTemp tct
			)A
		ORDER BY A.SoHopDong, A.TypeProduct	
		OPEN Record_Cursor

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor into @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF, @HDLechGiaYN
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
		
				EXEC dbo.ThucChay_InsertThucChayDaTinh @NgayThucHien, @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF

			FETCH NEXT FROM Record_Cursor into @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @DmBannerREF, @HDLechGiaYN
			END

		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor
		
		--XU LY HD HUY
		--HAIDH COMMENT PHAN CHUC NANG KIEM SOAT HOPDONG HUY
		--EXEC [ThucChay_UpdateGiaTriThayDoi_HDHuy] @NgayThucHien, @NgayThucHien

		INSERT INTO dbo.Log_DuLieuRow_ThucChayDaTinh
		SELECT DmSanPhamREF, TenSanPham, TenViTri, DonViTinh, NgayThucHien, COUNT(ThucChayDaTinhID) SoLuongRow 
		, GETDATE() AS Created_At
		FROM dbo.ThucChayDaTinh
		WHERE 1=1 
		--AND DmSanPhamREF IN (231,238,339,240,598,613,370,680,735,5056,5299)
		AND (EXISTS(SELECT TOP (1) ch.ID FROM dbo.CauHinhNhomTinhDoanhSoThucChay ch 
																	WHERE ch.DmSanPhamREF = dbo.ThucChayDaTinh.DmSanPhamREF
																	AND ch.NhomTinhDoanhSoThucChay = 2 --Nhom Tinh Branding
																	AND ch.DeletedStatus = 0 ORDER BY ch.ID
							))
		AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, DonViTinh) = 3	 --Đơn vị của hình thức CPM, TRUE REACH
		AND NOT ( DmLoaiBannerREF IN (17,18)OR DmHinhThucQuangCao IN (13,42))
		AND CONVERT(date,NgayThucHien) = @NgayThucHien
		AND DonViTinh <> N'TRUE REACH'
		AND DotChayHopDong <> N'NGAY'
		AND CONVERT(DATE,CreatedAt) = CONVERT(DATE,GETDATE())
		GROUP BY  DmSanPhamREF, TenSanPham, TenViTri, DonViTinh, NgayThucHien

		set @NgayThucHien = dateadd(d,1,@NgayThucHien)

		delete from dbo.ThucChayTemp WHERE 1=1

	end 
	
	--SELECT '1'
END


--EXEC [ThucChay_ExcInsertThucChayDaTinh] '2021-04-21','2021-04-21'

```
