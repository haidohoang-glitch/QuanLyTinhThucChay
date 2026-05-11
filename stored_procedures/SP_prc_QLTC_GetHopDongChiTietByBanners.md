# Stored Procedure: `prc_QLTC_GetHopDongChiTietByBanners`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2023-07-05 15:56:56.327000
- **Ngày sửa cuối**: 2023-07-05 15:56:56.327000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Banners` | `nvarchar` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[prc_QLTC_GetHopDongChiTietByBanners]
	-- Add the parameters for the stored procedure here
	@Banners NVARCHAR(MAX) = '' 
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT HopDongChiTietREF, DmBannerREF FROM dbo.ThucChayHopDongChiTiet where DmBannerREF IN (SELECT Name FROM STRING_SPLIT_QLTC(@Banners)) order by id desc
END

```
