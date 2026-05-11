# Stored Procedure: `usp_InsertThucChayAdmarketPublisher`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-14 17:57:52.423000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.187000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(100)` | No |
| `@SiteID` | `int(4)` | No |
| `@SiteName` | `nvarchar(100)` | No |
| `@DmWebsiteREF` | `int(4)` | No |
| `@TenWebsite` | `nvarchar(100)` | No |
| `@ttClick` | `bigint(8)` | No |
| `@ttView` | `int(4)` | No |
| `@Price` | `float(8)` | No |
| `@NgayThucHien` | `datetime(8)` | No |
| `@IsPheDuyet` | `int(4)` | No |
| `@PheDuyetBy` | `nvarchar(100)` | No |
| `@PheDuyetAt` | `datetime(8)` | No |
| `@CreatedBy` | `nvarchar(2)` | No |
| `@CreatedAt` | `datetime(8)` | No |
| `@LastModifiedBy` | `nvarchar(2)` | No |
| `@LastModifiedAt` | `datetime(8)` | No |
| `@DeletedStatus` | `int(4)` | No |
| `@PrintStatus` | `int(4)` | No |
| `@RecordStatus` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[usp_InsertThucChayAdmarketPublisher]
(
	@DmSanPhamREF INT,
	@TenSanPham NVARCHAR(50),
	@SiteID int,
	@SiteName nvarchar(50),
	@DmWebsiteREF int,
	@TenWebsite nvarchar(50),
	@ttClick bigint,
	@ttView int,
	@Price float,
	@NgayThucHien datetime,
	@IsPheDuyet int,
	@PheDuyetBy nvarchar(50),
	@PheDuyetAt datetime,
	@CreatedBy nvarchar(1),
	@CreatedAt datetime,
	@LastModifiedBy nvarchar(1),
	@LastModifiedAt datetime,
	@DeletedStatus int,
	@PrintStatus int,
	@RecordStatus int
)
AS

SET NOCOUNT ON

SET @DmWebsiteREF = (SELECT TOP 1 A.DmWebsiteREF
                       FROM ThucChayDaTinh A WHERE A.TenWebsite = @SiteName)
SET @TenWebsite = @SiteName          

IF EXISTS(SELECT [SiteID]
          FROM ThucChayAdmarketPublisher 
          WHERE
			CONVERT(Date,[NgayThucHien]) = CONVERT(Date,@NgayThucHien) 
			AND [SiteID] = @SiteID
			AND [SiteName] = @SiteName
			AND [DmSanPhamREF] = @DmSanPhamREF)
	UPDATE [dbo].[ThucChayAdmarketPublisher] SET
		[DmSanPhamREF] = @DmSanPhamREF,
		[TenSanPham] = @TenSanPham,
		[SiteID] = @SiteID,
		[SiteName] = @SiteName,
		[DmWebsiteREF] = @DmWebsiteREF,
		[TenWebsite] = @TenWebsite,
		[ttClick] = @ttClick,
		[ttView] = @ttView,
		[Price] = @Price,
		[NgayThucHien] = @NgayThucHien,
		[IsPheDuyet] = @IsPheDuyet,
		[PheDuyetBy] = @PheDuyetBy,
		[PheDuyetAt] = @PheDuyetAt,
		[LastModifiedBy] = @LastModifiedBy,
		[LastModifiedAt] = @LastModifiedAt,
		[DeletedStatus] = @DeletedStatus,
		[PrintStatus] = @PrintStatus,
		[RecordStatus] = @RecordStatus
	WHERE
		CONVERT(Date,[NgayThucHien]) = CONVERT(Date,@NgayThucHien)
		AND [SiteID] = @SiteID
		AND [SiteName] = @SiteName
		AND [DmSanPhamREF] = @DmSanPhamREF
								
ELSE
	INSERT INTO [dbo].[ThucChayAdmarketPublisher] (	
		[DmSanPhamREF],
		[TenSanPham], 
		[SiteID],
		[SiteName],
		[DmWebsiteREF],
		[TenWebsite],
		[ttClick],
		[ttView],
		[Price],
		[NgayThucHien],
		[IsPheDuyet],
		[PheDuyetBy],
		[PheDuyetAt],
		[CreatedBy],
		[CreatedAt],
		[LastModifiedBy],
		[LastModifiedAt],
		[DeletedStatus],
		[PrintStatus],
		[RecordStatus]
	) VALUES (
		@DmSanPhamREF,
		@TenSanPham,
		@SiteID,
		@SiteName,
		@DmWebsiteREF,
		@TenWebsite,
		@ttClick,
		@ttView,
		@Price,
		@NgayThucHien,
		@IsPheDuyet,
		@PheDuyetBy,
		@PheDuyetAt,
		@CreatedBy,
		@CreatedAt,
		@LastModifiedBy,
		@LastModifiedAt,
		@DeletedStatus,
		@PrintStatus,
		@RecordStatus
	)

```
