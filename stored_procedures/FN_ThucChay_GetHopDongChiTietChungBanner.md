# Function: `ThucChay_GetHopDongChiTietChungBanner`

- **Loại**: SQL_INLINE_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2015-03-20 14:39:16.040000
- **Ngày sửa cuối**: 2015-04-16 16:44:08.307000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetHopDongChiTietChungBanner] 
(	
	-- Add the parameters for the function here
	@HopDongChiTietID INT
)
RETURNS TABLE 
AS
RETURN 
(
	-- Add the SELECT statement with parameter references here
	select distinct HopDongChiTietREF HopDongChiTietID from ThucChayHopDongChiTietAndBanner 
	where DmBannerID in (
	select  DmBannerID from ThucChayHopDongChiTietAndBanner
	where HopDongChiTietREF = @HopDongChiTietID)
	and HopDongREF = (select top 1 HopDongREF from ThucChayHopDongChiTietAndBanner
	where HopDongChiTietREF = @HopDongChiTietID)
)

```
