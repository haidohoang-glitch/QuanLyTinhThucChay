# Stored Procedure: `Gen_InsertOrUpdate_ThucChayTrueView`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-05-19 15:49:17.007000
- **Ngày sửa cuối**: 2017-05-19 16:06:43.100000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(400)` | No |
| `@TypeProduct` | `int(4)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(400)` | No |
| `@campaignid` | `bigint(8)` | No |
| `@bannerid` | `bigint(8)` | No |
| `@SiteName` | `nvarchar(400)` | No |
| `@SiteID` | `bigint(8)` | No |
| `@True_View` | `float(8)` | No |
| `@Views` | `float(8)` | No |
| `@Clicks` | `float(8)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucChayTrueView] 	
	@SoHopDong nvarchar (200) ,	
	@TypeProduct int ,	
	@DmSanPhamREF int ,	
	@TenSanPham nvarchar (200) ,	
	@campaignid bigint ,	
	@bannerid bigint ,	
	@SiteName nvarchar (200) ,	
	@SiteID bigint ,	
	@True_View float ,	
	@Views float ,	
	@Clicks float ,	
	@NgayThucHien datetime 	
As 	
BEGIN
	DECLARE @DmWebsiteREF INT =0

	SET @DmWebsiteREF = dbo.GetWebsiteIDByDomainName(@SiteName)
	
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
	        @SiteName,	-- TenWebsite - nvarchar(200)
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

    INSERT INTO [dbo].[ThucChayTrueView] (	
	[SoHopDong],	
	[TypeProduct],	
	[DmSanPhamREF],	
	[TenSanPham],	
	[campaignid],	
	[bannerid],	
	[SiteName],	
	[SiteID],	
	[True_View],	
	[Views],	
	[Clicks],	
	[NgayThucHien],
	CreatedBy , 
	CreatedAt ,
	LastModifiedBy , 
	LastModifiedAt , 
	DeletedStatus )	
	Values 	
	(	
	@SoHopDong,	
	@TypeProduct,	
	@DmSanPhamREF,	
	@TenSanPham,	
	@campaignid,	
	@bannerid,	
	@SiteName,	
	@DmWebsiteREF,	
	@True_View,	
	@Views,	
	@Clicks,	
	@NgayThucHien,
	'ASD',
	GETDATE(),
	'ASD',
	GETDATE(),
	0)
END

```
