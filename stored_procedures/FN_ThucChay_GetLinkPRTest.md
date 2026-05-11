# Function: `ThucChay_GetLinkPRTest`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-12-07 11:37:33.957000
- **Ngày sửa cuối**: 2014-10-14 10:39:31.943000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(4000)` | Yes |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-10-29
-- Description:	Get link of PR
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetLinkPRTest]
(
	-- Add the parameters for the function here
	@HopDongChiTietREF int,
	@StartDate datetime,
	@EndDate datetime
)
RETURNS nvarchar(2000)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ReturnValue nvarchar(2000)
	DECLARE @InputValue NVARCHAR(2000)
	
	SET @InputValue = 
					(
					SELECT STUFF (
							(
									SELECT ',' + T.DotChayBooking  
									FROM ThucChayDaTinh T
									WHERE 	
										T.TrangThaiHopDong <> 3
										AND T.IsPheDuyet = 1
										AND T.HopDongChiTietREF = @HopDongChiTietREF									
										--AND T.DmSanPhamREF IN (141,245,250)
										AND T.DmSanPhamREF IN (141)
										AND CONVERT(DATE,T.NgayThucHien) BETWEEN @StartDate AND @EndDate
										AND (T.ThanhTienSauTrietKhauThucChay <> 0 OR T.ThanhTienKM <> 0)

							FOR XML PATH('') 
							), 1, 1, '') AS DotChayBooking 
					)

	SET @ReturnValue = '
		SELECT A.Link
			FROM ThucChayHopDongChiTietPR A
			WHERE A.HopDongChiTietREF = ' + CONVERT(varchar(50),@HopDongChiTietREF ) + '
				AND A.ThucChayHopDongChiTietPRID IN (' + @InputValue + ')
			ORDER BY A.ThoiGianBatDau
	'

	-- Return the result of the function
	RETURN @InputValue

END

--PRINT dbo.ThucChay_GetLinkPR(45335 ,'Sep  1 2013 12:00AM','Dec 15 2013 12:00AM') 
```
