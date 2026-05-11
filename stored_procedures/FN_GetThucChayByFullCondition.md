# Function: `GetThucChayByFullCondition`

- **Loại**: SQL_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2013-09-25 17:01:09.927000
- **Ngày sửa cuối**: 2014-10-14 10:39:35.333000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@dtStart` | `datetime(8)` | No |
| `@dtEnd` | `datetime(8)` | No |
| `@DanhsachDmBookingREFList` | `varchar(4000)` | No |
| `@DmBannerREFList` | `nvarchar(8000)` | No |
| `@SoHopDongList` | `nvarchar(8000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
-- 
--SELECT  * FROM [dbo].[GetThucChayByFullCondition]('2013-09-01','2013-09-25','','','')

CREATE FUNCTION [dbo].[GetThucChayByFullCondition]
(	
	@dtStart DATETIME,
	@dtEnd DATETIME,
	@DanhsachDmBookingREFList varchar(4000),
	@DmBannerREFList NVARCHAR(4000),
	@SoHopDongList NVARCHAR(4000)
)
RETURNS 
@ThucChay TABLE (
	[ThucChayID] [nvarchar](50) NOT NULL,
	[SoHopDong] [nvarchar](50) NULL,
	[DanhsachDmBookingREF] [varchar](4000) NULL,
	[DmSanPhamREF] [int] NULL,
	[TenSanPham] [nvarchar](255) NULL,
	[DmNhomWebsiteREF] [int] NULL,
	[TenNhomWebsite] [nvarchar](50) NULL,
	[DmWebsiteREF] [bigint] NULL,
	[TenWebsite] [nvarchar](255) NULL,
	[DmChienDichREF] [int] NULL,
	[TenChienDich] [nvarchar](255) NULL,
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
	[HopDongChiTietREF] [nvarchar](50) NULL,
	[SoThuTuTheoNgay] [int] NULL,
	[TypeProduct] [int] NULL
	)
AS
BEGIN
	
	if((@DanhsachDmBookingREFList = '' or @DanhsachDmBookingREFList is null) and (@DmBannerREFList = '' or @DmBannerREFList is null))
		Insert into @ThucChay select * from	dbo.GetThucChayByNoFilter(@dtStart,@dtEnd,@SoHopDongList)		
	else
	if(@DanhsachDmBookingREFList = '' or @DanhsachDmBookingREFList is null)
		Insert into @ThucChay select * from	dbo.GetThucChayByBannerID(@dtStart,@dtEnd,@DmBannerREFList,@SoHopDongList)
	else
	if(@DmBannerREFList = '' or @DmBannerREFList is null)
		Insert into @ThucChay select * from	dbo.GetThucChayByBookingID(@dtStart,@dtEnd,@DanhsachDmBookingREFList,@SoHopDongList)			
	else	
	if((@DanhsachDmBookingREFList <> '' and @DanhsachDmBookingREFList is not null) and (@DmBannerREFList <> '' and @DmBannerREFList is not null))
		Insert into @ThucChay select * from	dbo.GetThucChayByBookingIDAndBannerID(@dtStart,@dtEnd,@DanhsachDmBookingREFList,@DmBannerREFList,@SoHopDongList)		
	ELSE IF (@DanhsachDmBookingREFList <> '' AND @SoHopDongList <> '')
		INSERT INTO @ThucChay
		SELECT * 
		FROM dbo.GetThucChayByBookingIDAndSoHopDong(@dtStart, @dtEnd,@DanhsachDmBookingREFList, @DmBannerREFList, @SoHopDongList);		
		
	return 
End



```
