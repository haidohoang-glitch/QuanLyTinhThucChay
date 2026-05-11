# Function: `GetSoLuongDotChayThucTreoByHopDongChiTiet`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-06-25 10:49:03.967000
- **Ngày sửa cuối**: 2014-10-14 10:39:35.590000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author then 		<Author,,Name>
-- Create date then  <Create Date, ,>
-- Description then 	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[GetSoLuongDotChayThucTreoByHopDongChiTiet]
(
	-- Add the parameters for the function here
	@HopDongChiTietID INT
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Result INT
	SET @Result = 0
	SET @Result = (
	        SELECT SUM(ISNULL(DATEDIFF(DAY, tchdct.ThoiGianBatDau, tchdct.ThoiGianKetThuc) + 1,0))
	        FROM   ThucChayHopDongChiTiet tchdct
	        WHERE tchdct.HopDongChiTietREF = @HopDongChiTietID
	        AND tchdct.DeletedStatus = 0
	    )
	-- Return the result of the function
	RETURN @Result
END

```
