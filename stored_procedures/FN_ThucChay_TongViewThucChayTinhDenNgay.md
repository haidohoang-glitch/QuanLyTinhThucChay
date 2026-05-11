# Function: `ThucChay_TongViewThucChayTinhDenNgay`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-08-06 10:30:17.730000
- **Ngày sửa cuối**: 2014-10-14 10:39:29.033000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `bigint(8)` | Yes |
| `@SoHopDong` | `nvarchar(100)` | No |
| `@EndDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_TongViewThucChayTinhDenNgay]
(
	@SoHopDong NVARCHAR(50),
	@EndDate DATETIME
)
RETURNS BIGINT
AS
BEGIN
	DECLARE @RerurnValue BIGINT

	SET @RerurnValue = (SELECT CONVERT(BIGINT,SUM(isnull(TongViewThucChay,0))) FROM ThucChayDaTinh
						WHERE CONVERT(Date, NgayThucHien) <= CONVERT(NVARCHAR(50),@EndDate)
							AND SoHopDong = @SoHopDong
						)
	RETURN @RerurnValue

END

```
