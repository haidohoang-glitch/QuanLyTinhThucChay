# Stored Procedure: `ThucChay_ExcInsertThucChayDaTinhBySoHopDong_ThieuBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-03-17 09:21:25.730000
- **Ngày sửa cuối**: 2018-08-28 11:38:47.447000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DmSanPhamID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--EXEC [ThucChay_ExcInsertThucChayDaTinhBySoHopDong_ThieuBanner] '2014-05-17','2014-05-17', 'QC1500514', 339

CREATE PROCEDURE [dbo].[ThucChay_ExcInsertThucChayDaTinhBySoHopDong_ThieuBanner] 
	@StartDate datetime,
	@EndDate DATETIME,
	@SoHopDong NVARCHAR(50),
	@DmSanPhamID INT
AS
BEGIN
	DECLARE @NgayThucHien DATETIME
	DECLARE @TypeProduct INT, @HDLechGiaYN NVARCHAR(50), @TenWebsite NVARCHAR(50), @DmWebsiteREF INT
	set @NgayThucHien = @StartDate
	delete from dbo.ThucChayTemp
	--Xoa du lieu ThucChayDaTinh truoc khi tinh
	DELETE FROM ThucChayDaTinh_ThieuBanner
	WHERE convert(date,NgayThucHien) BETWEEN @StartDate AND @EndDate
	AND DmSanPhamREF = @DmSanPhamID 
	AND SoHopDong = @SoHopDong
	
	while(@NgayThucHien <= @EndDate)
	Begin

		Insert into dbo.ThucChayTemp
		(
		    ThucChayID,
		    SoHopDong,
		    DanhsachDmBookingREF,
		    DmSanPhamREF,
		    TenSanPham,
		    DmNhomWebsiteREF,
		    TenNhomWebsite,
		    DmWebsiteREF,
		    TenWebsite,
		    DmChienDichREF,
		    TenChienDich,
		    DmBannerREF,
		    TenBanner,
		    NgayThucHien,
		    TongViewThucChay,
		    TongClickThucChay,
		    CreatedBy,
		    CreatedAt,
		    LastModifiedBy,
		    LastModifiedAt,
		    DeletedStatus,
		    PrintStatus,
		    RecordStatus,
		    TongSoBaiViet,
		    SoThuTuTheoNgay,
		    TypeProduct,
		    BannerType,
		    UserName,
		    SaleName,
		    Email,
		    LastTimeCalc,
		    sys_date,
		    IsReady,
		    ProductUnitID,
		    ProductUnitName,
		    BannerTypeName,
		    HopDongChiTietREF,
		    CampainStatus,
		    BannerStatus,
		    IsNoiBo
		)
		
		select  ThucChayID,
		    SoHopDong,
		    DanhsachDmBookingREF,
		    DmSanPhamREF,
		    TenSanPham,
		    DmNhomWebsiteREF,
		    TenNhomWebsite,
		    DmWebsiteREF,
		    TenWebsite,
		    DmChienDichREF,
		    TenChienDich,
		    DmBannerREF,
		    TenBanner,
		    NgayThucHien,
		    TongViewThucChay,
		    TongClickThucChay,
		    CreatedBy,
		    CreatedAt,
		    LastModifiedBy,
		    LastModifiedAt,
		    DeletedStatus,
		    PrintStatus,
		    RecordStatus,
		    TongSoBaiViet,
		    SoThuTuTheoNgay,
		    TypeProduct,
		    BannerType,
		    UserName,
		    SaleName,
		    Email,
		    LastTimeCalc,
		    sys_date,
		    IsReady,
		    ProductUnitID,
		    ProductUnitName,
		    BannerTypeName,
		    HopDongChiTietREF,
		    CampainStatus,
		    BannerStatus,
		    IsNoiBo from dbo.ThucChay 
		where Convert(date,NgayThucHien) = @NgayThucHien
		AND TypeProduct = dbo.GetDmSanPhamIDByTypeProductID(@DmSanPhamID)
		AND DmWebsiteREF != 0
		AND SoHopDong = @SoHopDong
		
		DECLARE Record_Cursor CURSOR FOR 
		SELECT distinct A.SoHopDong,A.TypeProduct,A.DmWebsiteREF, A.TenWebsite ,A.HDLechGiaYN
		  FROM
			(
				SELECT tct.SoHopDong,tct.TypeProduct, tct.DmWebsiteREF, tct.TenWebsite
				--,dbo.ThucChay_CheckHopDongCoSanPhamLechDonGiaYN(tct.TypeProduct,tct.SoHopDong) HDLechGiaYN 
				,'Y' HDLechGiaYN 
				FROM ThucChayTemp tct
			)A
		ORDER BY A.SoHopDong, A.TypeProduct	
		--WHERE A.HDLechGiaYN = 'Y'
		OPEN Record_Cursor

		-- Perform the first fetch.
		FETCH NEXT FROM Record_Cursor into @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @HDLechGiaYN
			
		WHILE @@FETCH_STATUS = 0
			BEGIN
			IF(@HDLechGiaYN = 'Y')
				BEGIN
					EXEC ThucChay_InsertThucChayDaTinh @NgayThucHien, @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite
				END
			ELSE
				BEGIN
					EXEC ThucChay_InsertThucChayDaTinh_ByHDLoaiSP @NgayThucHien, @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite
				END
			
			FETCH NEXT FROM Record_Cursor into @SoHopDong, @TypeProduct, @DmWebsiteREF, @TenWebsite, @HDLechGiaYN
			END

		CLOSE Record_Cursor
		DEALLOCATE Record_Cursor
		
		set @NgayThucHien = dateadd(d,1,@NgayThucHien)
		delete from dbo.ThucChayTemp
		PRINT @NgayThucHien
		PRINT @HDLechGiaYN
	end 
	
	SELECT '1'
END

```
