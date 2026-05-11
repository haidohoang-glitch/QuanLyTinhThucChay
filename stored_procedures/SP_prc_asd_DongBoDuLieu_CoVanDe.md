# Stored Procedure: `prc_asd_DongBoDuLieu_CoVanDe`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-04-27 09:42:54.710000
- **Ngày sửa cuối**: 2017-04-27 09:42:54.710000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |
| `@HopDongChiTietREF` | `nvarchar` | No |

## Definition (Source Code)

```sql

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[prc_asd_DongBoDuLieu_CoVanDe]
	-- Add the parameters for the stored procedure here
	@FromDate DATETIME,
	@ToDate DATETIME,
	@HopDongChiTietREF NVARCHAR(max)
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT NgayThucHien, SoHopDong, HopDongChiTietREF, DmSanPhamREF
	FROM dbo.ThucChayDaTinh WHERE HopDongChiTietREF IN (SELECT VALUE FROM dbo.ASD_SPLIT(',',@HopDongChiTietREF))
	AND NgayThucHien BETWEEN @FromDate AND @ToDate
END




```
