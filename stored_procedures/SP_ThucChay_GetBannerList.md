# Stored Procedure: `ThucChay_GetBannerList`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-10 11:28:44.040000
- **Ngày sửa cuối**: 2014-11-19 12:16:55.600000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

-- exec dbo.ThucChay_GetBannerList '2014-04-09', '2014-04-09',''
CREATE PROCEDURE [dbo].[ThucChay_GetBannerList] 
	-- Add the parameters for the stored procedure here
	@StartDate DATETIME,
	@EndDate DATETIME,
	@TenDangNhap NVARCHAR(50)
AS
BEGIN
	SELECT DISTINCT
		A.DmViTriREF AS ID,
		A.TenViTri AS Name
	FROM ThucChayDaTinh A
	WHERE A.NgayThucHien BETWEEN @StartDate AND @EndDate
		AND A.DmSanPhamREF IN (306, 423, 535)
		AND A.DmViTriREF > 0
	ORDER BY A.TenViTri
END

```
