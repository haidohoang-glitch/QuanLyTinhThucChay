# Stored Procedure: `Gen_InsertOrUpdate_ThucChay_v1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-06-01 15:41:00.200000
- **Ngày sửa cuối**: 2017-09-23 10:14:07.773000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@TypeProduct` | `int(4)` | No |

## Definition (Source Code)

```sql
/*
EXEC [dbo].[Gen_InsertOrUpdate_ThucChay_v1] 10
*/
CREATE PROCEDURE [dbo].[Gen_InsertOrUpdate_ThucChay_v1]
	@TypeProduct INT
AS
BEGIN
	DECLARE @SQL NVARCHAR(MAX) = '', @DauNhay NVARCHAR(100) = '"', @NgayThucHien DATETIME
	, @Count int= 0, @v_DmWebsiteREF int = 0, @v_TenWebsite nvarchar(1000)
	SET @NgayThucHien = 
	ISNULL((
		SELECT Dateadd(day,1,Isnull(Max([NgayThucHien]),'2016-12-31')) 
		FROM [dbo].[ThucChay] Where 1=1  and typeproduct = 10 and DeletedStatus <> 1
	),'2017-01-01')
	
	--SET @NgayThucHien = '2017-09-21'

	DECLARE @tb_ThucChay TABLE(
	[ThucChayID] [nvarchar](50) NOT NULL,
	[SoHopDong] [nvarchar](50) NULL,
	[DanhsachDmBookingREF] [varchar](4000) NULL,
	[DmSanPhamREF] [int] NULL,
	[TenSanPham] [nvarchar](255) NULL,
	[DmNhomWebsiteREF] [int] NULL,
	[TenNhomWebsite] [nvarchar](50) NULL,
	[DmWebsiteREF] [bigint] NULL,
	[TenWebsite] [nvarchar](1000) NULL,
	[DmChienDichREF] [int] NULL,
	[TenChienDich] [nvarchar](500) NULL,
	[DmBannerREF] [int] NULL,
	[TenBanner] [nvarchar](256) NULL,
	[NgayThucHien] [datetime] NULL,
	[TongViewThucChay] [float] NULL,
	[TongClickThucChay] [float] NULL,
	[CreatedBy] [nvarchar](50) NOT NULL,
	[CreatedAt] [datetime] NOT NULL,
	[LastModifiedBy] [nvarchar](50) NOT NULL,
	[LastModifiedAt] [datetime] NOT NULL,
	[DeletedStatus] [int] NOT NULL,
	[PrintStatus] [int] NOT NULL,
	[RecordStatus] [int] NOT NULL,
	[TongSoBaiViet] [float] NULL,
	[SoThuTuTheoNgay] [int] NULL,
	[TypeProduct] [int] NULL,
	[BannerType] [int] NULL,
	[UserName] [varchar](255) NULL,
	[SaleName] [varchar](255) NULL,
	[Email] [varchar](255) NULL,
	[LastTimeCalc] [datetime] NULL,
	[sys_date] [datetime] NULL,
	[IsReady] [int] NULL,
	[ProductUnitID] [int] NULL,
	[ProductUnitName] [nvarchar](1000) NULL,
	[BannerTypeName] [nvarchar](4000) NULL,
	[HopDongChiTietREF] [int] NULL,
	[CampainStatus] [nvarchar](50) NULL,
	[BannerStatus] [nvarchar](50) NULL,
	[IsNoiBo] [int] NULL)

	--XOA DU LIEU CUA NGAY TRUOC KHI LAY
	DELETE  FROM ThucChay
	WHERE NgayThucHien = @NgayThucHien
	AND TypeProduct = @TypeProduct

	SET @SQL = 'CALL SelectThucChayAll_ASD_By_Date_and_Typeproduct ('+ @DauNhay + CONVERT(NVARCHAR(20), @NgayThucHien, 120) + @DauNhay + ','  + CONVERT(NVARCHAR(20), @TypeProduct)  + ' );'
	SET @SQL = 
		'Select
    		hdct.*
		from openquery([ReportingDB],''' + @SQL + ''') hdct'
	print @SQL

	INSERT INTO @tb_ThucChay
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
	
	EXECUTE
	  (
		@SQL
	  )
	  declare @slsite int = 0
	  set @slsite = 
	  (
		  select count(distinct a.tenwebsite) from
		  (
			select [dbo].[GetWebsiteIDByDomainName](TenWebsite) DmWebsiteREF, TenWebsite from @tb_ThucChay
		  )a where a.DmWebsiteREF is null
	  )
	  ----CAP NHAT THONG TIN DMWEBSITE
	  if(@slsite >0)
		  while @Count < @slsite
		  begin
				set @v_TenWebsite = 
				(
				 select top 1 TenWebsite from
				  (
					select [dbo].[GetWebsiteIDByDomainName](TenWebsite) DmWebsiteREF, TenWebsite from @tb_ThucChay
				  )a where a.DmWebsiteREF is null
				)
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
				@v_TenWebsite,	-- TenWebsite - nvarchar(200)
				N'asd',	-- CreatedBy - nvarchar(50)
				GETDATE(),	-- CreatedAt - datetime
				N'asd',	-- LastModifiedBy - nvarchar(50)
				GETDATE(),	-- LastModifiedAt - datetime
				0,	-- DeletedStatus - int
				0,	-- PrintStatus - int
				0,	-- RecordStatus - int
				N'New' -- ID - nvarchar(50)
			  )		
			SET @v_DmWebsiteREF = @@IDENTITY

			update @tb_ThucChay
			set DmWebsiteREF = @v_DmWebsiteREF
			where TenWebsite = @v_TenWebsite

			set @v_DmWebsiteREF = 0
			set @v_TenWebsite =''

			set @Count = @Count + 1
		  end

	
	

		--INSERT THONG TIN THUC CHAY
		INSERT INTO dbo.ThucChay
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
				  HopDongChiTietREF ,
		          BannerTypeName ,
		          CampainStatus ,
		          BannerStatus ,
		          IsNoiBo
		        )
	
		  SELECT
		    [ThucChayID],
		    [SoHopDong],
		    [DanhsachDmBookingREF],
		    [DmSanPhamREF],
		    [TenSanPham],
		    [DmNhomWebsiteREF],
		    [TenNhomWebsite],
		    [dbo].[GetWebsiteIDByDomainName_v1]([TenWebsite]) [DmWebsiteREF],
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
		  FROM @tb_ThucChay
END
	
```
