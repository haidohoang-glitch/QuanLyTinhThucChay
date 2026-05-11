# Stored Procedure: `prc_asd_DongBoDuLieu`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-04-26 14:16:07.517000
- **Ngày sửa cuối**: 2017-04-27 09:43:19.807000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[prc_asd_DongBoDuLieu]
	-- Add the parameters for the stored procedure here
	@FromDate DATETIME,
	@ToDate DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	SET NOCOUNT ON;

    -- Insert statements for procedure here
	SELECT NgayThucHien, SoHopDong, HopDongChiTietREF, DmSanPhamREF
	FROM dbo.ThucChayDaTinh WHERE NgayThucHien BETWEEN @FromDate AND @ToDate
END




```
