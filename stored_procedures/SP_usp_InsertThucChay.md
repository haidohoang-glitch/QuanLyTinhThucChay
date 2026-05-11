# Stored Procedure: `usp_InsertThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-05-29 03:12:57.373000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.177000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayID` | `nvarchar(100)` | No |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@DanhsachDmBookingREF` | `nvarchar(200)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(510)` | No |
| `@DmNhomWebsiteREF` | `int(4)` | No |
| `@TenNhomWebsite` | `nvarchar(100)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(510)` | No |
| `@DmChienDichREF` | `int(4)` | No |
| `@TenChienDich` | `nvarchar(510)` | No |
| `@DmBannerREF` | `int(4)` | No |
| `@TenBanner` | `nvarchar(512)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@TongViewThucChay` | `float(8)` | No |
| `@TongClickThucChay` | `float(8)` | No |
| `@CreatedBy` | `nvarchar(100)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(100)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |
| `@SoThuTuTheoNgay` | `int(4)` | No |
| `@TypeProduct` | `int(4)` | No |
| `@BannerType` | `int(4)` | No |
| `@UserName` | `varchar(255)` | No |
| `@SaleName` | `varchar(255)` | No |
| `@Email` | `varchar(255)` | No |
| `@LastTimeCalc` | `datetime(8)` | No |
| `@sys_date` | `datetime(8)` | No |
| `@IsReady` | `int(4)` | No |
| `@ProductUnitID` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@ProductUnitName` | `nvarchar(100)` | No |
| `@BannerTypeName` | `nvarchar(100)` | No |
| `@CampainStatus` | `nvarchar(100)` | No |
| `@BannerStatus` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_InsertThucChay]
	@ThucChayID NVARCHAR(50),
	@SoHopDong NVARCHAR(50),
	@DanhsachDmBookingREF NVARCHAR(100),
	@DmSanPhamREF INT,
	@TenSanPham NVARCHAR(255),
	@DmNhomWebsiteREF INT,
	@TenNhomWebsite NVARCHAR(50),
	@DmWebsiteREF INT,
	@TenWebsite NVARCHAR(255),
	@DmChienDichREF INT,
	@TenChienDich NVARCHAR(255),
	@DmBannerREF INT,
	@TenBanner NVARCHAR(256),
	@NgayThucHien DATETIME,
	@TongViewThucChay FLOAT,
	@TongClickThucChay FLOAT,
	@CreatedBy NVARCHAR(50),
	@CreatedAt DATETIME,
	@LastModifiedBy NVARCHAR(50),
	@LastModifiedAt DATETIME,
	@DeletedStatus INT,
	@PrintStatus INT,
	@RecordStatus INT,
	@SoThuTuTheoNgay INT,
	@TypeProduct INT,
	@BannerType INT,
	@UserName VARCHAR(255),
	@SaleName VARCHAR(255),
	@Email VARCHAR(255),
	@LastTimeCalc datetime,
	@sys_date datetime,
	@IsReady int,
	@ProductUnitID int,
	@HopDongChiTietREF int,
	@ProductUnitName nvarchar(50),
	@BannerTypeName nvarchar(50),
	@CampainStatus nvarchar(50),
	@BannerStatus nvarchar(50)
AS
BEGIN
	SET @DmWebsiteREF = dbo.GetWebsiteIDByDomainName(@TenWebsite)
	
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
        [SoThuTuTheoNgay],
        [TypeProduct],
        [BannerType],
        [UserName],
        [SaleName],
        [Email],
	   [LastTimeCalc] ,
	   [sys_date] ,
	   [IsReady],
	   [ProductUnitID],
	   [ProductUnitName],
	   [BannerTypeName],
	   [HopDongChiTietREF],
	   [CampainStatus],
	   [BannerStatus]
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
        @SoThuTuTheoNgay,
        @TypeProduct,
        @BannerType,
        @UserName,
        @SaleName,
        @Email,
		@LastTimeCalc ,
		@sys_date ,
		@IsReady ,
		@ProductUnitID,
	    @ProductUnitName,
	    @BannerTypeName,
	    @HopDongChiTietREF,
	    @CampainStatus,
	    @BannerStatus   
      )

END

```
