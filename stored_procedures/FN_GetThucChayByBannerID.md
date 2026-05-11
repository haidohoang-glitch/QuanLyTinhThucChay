# Function: `GetThucChayByBannerID`

- **Loại**: SQL_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2013-09-25 17:01:09.487000
- **Ngày sửa cuối**: 2014-10-14 10:39:35.460000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@dtStart` | `datetime(8)` | No |
| `@dtEnd` | `datetime(8)` | No |
| `@DmBannerREFList` | `nvarchar(8000)` | No |
| `@SoHopDongList` | `varchar(4000)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--SELECT  * FROM [dbo].[GetThucChayByBookingID]('2013-09-01','2013-09-25','619,620,621,622,623','203663')

CREATE FUNCTION [dbo].[GetThucChayByBannerID]
(	
	@dtStart DATETIME,
	@dtEnd DATETIME,
	@DmBannerREFList NVARCHAR(4000),
	@SoHopDongList varchar(4000)
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
	
	IF(@SoHopDongList = '')
		Insert into @ThucChay
		SELECT *
		FROM [dbo].[ThucChay]	A
		WHERE 
		A.NgayThucHien BETWEEN @dtStart AND @dtEnd 
		AND
		DmBannerREF IN (SELECT item FROM dbo.ArrayToTable(dbo.Array(@DmBannerREFList ,',')))
	ELSE
		Insert into @ThucChay
		SELECT *
		FROM [dbo].[ThucChay]	A
		WHERE 
		A.NgayThucHien BETWEEN @dtStart AND @dtEnd 
		AND
		DmBannerREF IN (SELECT item FROM dbo.ArrayToTable(dbo.Array(@DmBannerREFList ,',')))
		AND SoHopDong IN (SELECT item FROM dbo.ArrayToTable(dbo.Array(@SoHopDongList ,',')))
		
			
	return 
End



```
