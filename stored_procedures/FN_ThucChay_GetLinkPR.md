# Function: `ThucChay_GetLinkPR`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-11-09 11:47:05.370000
- **Ngày sửa cuối**: 2014-11-19 12:17:40.547000

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
CREATE FUNCTION [dbo].[ThucChay_GetLinkPR]
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

	 
	SET @ReturnValue = (
	SELECT
		STUFF(
		(
			SELECT ';' + A.Link
			FROM ThucChayHopDongChiTietPR A
			WHERE A.HopDongChiTietREF = @HopDongChiTietREF 
				--and CONVERT(DATE,A.ThoiGianBatDau) BETWEEN @StartDate AND @EndDate
				AND A.ThucChayHopDongChiTietPRID IN (SELECT item FROM dbo.ArrayToTable(dbo.Array(@InputValue, ',') ))
			ORDER BY A.ThoiGianBatDau
		FOR XML PATH('') 
		), 1, 1, '') AS Link
	)

	-- Return the result of the function
	RETURN @ReturnValue

END

```
