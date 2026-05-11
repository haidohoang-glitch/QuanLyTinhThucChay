# Stored Procedure: `Gen_InsertOrUpdate_ThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-11 15:02:50.870000
- **Ngày sửa cuối**: 2017-09-15 10:37:19.580000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayID` | `nvarchar(400)` | No |
| `@SoHopDong` | `nvarchar(400)` | No |
| `@DanhsachDmBookingREF` | `nvarchar(400)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(400)` | No |
| `@DmNhomWebsiteREF` | `int(4)` | No |
| `@TenNhomWebsite` | `nvarchar(400)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(4000)` | No |
| `@DmChienDichREF` | `int(4)` | No |
| `@TenChienDich` | `nvarchar(1000)` | No |
| `@DmBannerREF` | `int(4)` | No |
| `@TenBanner` | `nvarchar(400)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@TongViewThucChay` | `int(4)` | No |
| `@TongClickThucChay` | `int(4)` | No |
| `@CreatedBy` | `nvarchar(400)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(400)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |
| `@TongSoBaiViet` | `int(4)` | No |
| `@SoThuTuTheoNgay` | `bigint(8)` | No |
| `@TypeProduct` | `int(4)` | No |
| `@bannertype` | `int(4)` | No |
| `@username` | `nvarchar(400)` | No |
| `@salename` | `nvarchar(400)` | No |
| `@email` | `nvarchar(400)` | No |
| `@LastTimeCalc` | `datetime(8)` | No |
| `@sys_date` | `datetime(8)` | No |
| `@IsReady` | `int(4)` | No |
| `@ProductUnitID` | `int(4)` | No |
| `@ProductUnitName` | `nvarchar(2000)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@BannerTypeName` | `nvarchar(400)` | No |
| `@CampainStatus` | `nvarchar(400)` | No |
| `@BannerStatus` | `nvarchar(400)` | No |
| `@IsNoiBo` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucChay]
	@ThucChayID NVARCHAR(200) ,
	@SoHopDong NVARCHAR(200) ,
	@DanhsachDmBookingREF NVARCHAR(200) ,
	@DmSanPhamREF INT ,
	@TenSanPham NVARCHAR(200) ,
	@DmNhomWebsiteREF INT ,
	@TenNhomWebsite NVARCHAR(200) ,
	@DmWebsiteREF INT ,
	@TenWebsite NVARCHAR(2000) ,
	@DmChienDichREF INT ,
	@TenChienDich NVARCHAR(500) ,
	@DmBannerREF INT ,
	@TenBanner NVARCHAR(200) ,
	@NgayThucHien DATETIME ,
	@TongViewThucChay INT ,
	@TongClickThucChay INT ,
	@CreatedBy NVARCHAR(200) ,
	@CreatedAt DATETIME ,
	@LastModifiedBy NVARCHAR(200) ,
	@LastModifiedAt DATETIME ,
	@DeletedStatus INT ,
	@PrintStatus INT ,
	@RecordStatus INT ,
	@TongSoBaiViet INT ,
	@SoThuTuTheoNgay BIGINT ,
	@TypeProduct INT ,
	@bannertype INT ,
	@username NVARCHAR(200) ,
	@salename NVARCHAR(200) ,
	@email NVARCHAR(200) ,
	@LastTimeCalc DATETIME ,
	@sys_date DATETIME ,
	@IsReady INT ,
	@ProductUnitID INT ,
	@ProductUnitName NVARCHAR(1000) ,
	@HopDongChiTietREF INT ,
	@BannerTypeName NVARCHAR(200) ,
	@CampainStatus NVARCHAR(200) ,
	@BannerStatus NVARCHAR(200) ,
	@IsNoiBo INT
AS
BEGIN
	--SET @DmWebsiteREF = dbo.GetWebsiteIDByDomainName(@TenWebsite)
	
	IF @DmWebsiteREF IS NULL
	BEGIN
	    INSERT INTO dbo.DmWebsiteReportingdb
	      (
	        TenWebsite,
	        CreatedBy,
	        CreatedAt,
	        LastModifiedBy,
	        LastModifiedAt,
	        DeletedStatus,
	        PrintStatus,
	        RecordStatus,
	        ID
	      )
	    VALUES
	      (
	        @TenWebsite,	-- TenWebsite - nvarchar(200)
	        N'asd',	-- CreatedBy - nvarchar(50)
	        GETDATE(),	-- CreatedAt - datetime
	        N'asd',	-- LastModifiedBy - nvarchar(50)
	        GETDATE(),	-- LastModifiedAt - datetime
	        0,	-- DeletedStatus - int
	        0,	-- PrintStatus - int
	        0,	-- RecordStatus - int
	        N'New' -- ID - nvarchar(50)
	      )		
	    SET @DmWebsiteREF = @@IDENTITY
	END	
	
	INSERT INTO [dbo].[ThucChay]
	  (
	    [ThucChayID],
	    [SoHopDong],
	    [DanhsachDmBookingREF],
	    [DmSanPhamREF],
	    [TenSanPham],
	    [DmNhomWebsiteREF],
	    [TenNhomWebsite],
	    [DmWebsiteREF],
	    [TenWebsite],
	    [DmChienDichREF],
	    [TenChienDich],
	    [DmBannerREF],
	    [TenBanner],
	    [NgayThucHien],
	    [TongViewThucChay],
	    [TongClickThucChay],
	    [CreatedBy],
	    [CreatedAt],
	    [LastModifiedBy],
	    [LastModifiedAt],
	    [DeletedStatus],
	    [PrintStatus],
	    [RecordStatus],
	    [TongSoBaiViet],
	    [SoThuTuTheoNgay],
	    [TypeProduct],
	    [bannertype],
	    [username],
	    [salename],
	    [email],
	    [LastTimeCalc],
	    [sys_date],
	    [IsReady],
	    [ProductUnitID],
	    [ProductUnitName],
	    [HopDongChiTietREF],
	    [BannerTypeName],
	    [CampainStatus],
	    [BannerStatus],
	    [IsNoiBo]
	  )
	VALUES
	  (
	    @ThucChayID,
	    @SoHopDong,
	    @DanhsachDmBookingREF,
	    @DmSanPhamREF,
	    @TenSanPham,
	    @DmNhomWebsiteREF,
	    @TenNhomWebsite,
	    @DmWebsiteREF,
	    @TenWebsite,
	    @DmChienDichREF,
	    @TenChienDich,
	    @DmBannerREF,
	    @TenBanner,
	    @NgayThucHien,
	    @TongViewThucChay,
	    @TongClickThucChay,
	    @CreatedBy,
	    @CreatedAt,
	    @LastModifiedBy,
	    @LastModifiedAt,
	    @DeletedStatus,
	    @PrintStatus,
	    @RecordStatus,
	    @TongSoBaiViet,
	    @SoThuTuTheoNgay,
	    @TypeProduct,
	    @bannertype,
	    @username,
	    @salename,
	    @email,
	    @LastTimeCalc,
	    @sys_date,
	    @IsReady,
	    @ProductUnitID,
	    @ProductUnitName,
	    @HopDongChiTietREF,
	    @BannerTypeName,
	    @CampainStatus,
	    @BannerStatus,
	    @IsNoiBo
	  )
END
	

```
