# Stored Procedure: `rptThucChay_getDataByFilterCondition`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-03-27 17:43:21.783000
- **Ngày sửa cuối**: 2015-03-27 17:43:21.783000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Sql` | `nvarchar` | No |
| `@sWhere` | `nvarchar` | No |
| `@DmSanPhamREFList` | `nvarchar(1024)` | No |
| `@DmWebsiteREFList` | `nvarchar(1024)` | No |
| `@SoHopDongList` | `nvarchar(1024)` | No |
| `@PhongBanREFList` | `nvarchar(1024)` | No |
| `@BoPhanREFList` | `nvarchar(1024)` | No |
| `@NhomREFList` | `nvarchar(1024)` | No |
| `@TenNhanVienList` | `nvarchar(1024)` | No |
| `@DmHinhThucQuangCaoList` | `nvarchar(400)` | No |
| `@DmBannerREFList` | `nvarchar(400)` | No |
| `@DonViTinhList` | `nvarchar(1024)` | No |
| `@sWhereSecurity` | `nvarchar(1024)` | No |
| `@sGroupBy` | `nvarchar(1024)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
---exec [dbo].[rptThucChay_getDataByFilterCondition] 'select tensanpham,dmsanphamref,sum(ThucChayPhatSinhTrongKy) from rptThucChay_SanPham_Ngay where ','1=1 ','','','','','','','','','','',' AND 1=1 ',' GROUP BY TenSanPham, DmSanPhamREF'
  
CREATE PROCEDURE [dbo].[rptThucChay_getDataByFilterCondition] 
	-- Add the parameters for the stored procedure here
	@Sql					NVARCHAR(MAX),
	@sWhere                 NVARCHAR(MAX),
    @DmSanPhamREFList		NVARCHAR(512),
	@DmWebsiteREFList		NVARCHAR(512),
	@SoHopDongList			NVARCHAR(512),
	@PhongBanREFList		NVARCHAR(512),
	@BoPhanREFList			NVARCHAR(512),
	@NhomREFList			NVARCHAR(512),
	@TenNhanVienList		NVARCHAR(512),
	@DmHinhThucQuangCaoList NVARCHAR(200),
	@DmBannerREFList		NVARCHAR(200),
	@DonViTinhList			NVARCHAR(512),
	@sWhereSecurity			NVARCHAR(512),
	@sGroupBy				NVARCHAR(512)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	DECLARE @sqlchay NVARCHAR(MAX)
	DECLARE @sWhereChay NVARCHAR(MAX)
    SET @sWhereChay = (SELECT [dbo].[fn_rptThucChay_GetStringWhereByFilterString](@sWhere, @DmSanPhamREFList,@DmWebsiteREFList,@SoHopDongList,
															 @PhongBanREFList,@BoPhanREFList,@NhomREFList,@TenNhanVienList,
															 @DmHinhThucQuangCaoList,@DmBannerREFList,@DonViTinhList,@sWhereSecurity)
															 )
	SET @sqlchay = @Sql + @sWhereChay + @sGroupBy
	PRINT(@sqlchay)
	EXECUTE(@sqlchay)
END

```
