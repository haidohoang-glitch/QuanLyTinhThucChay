# Function: `GetSoLuongDotChayBookingByHopDongChiTiet`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2017-09-11 15:02:49.897000
- **Ngày sửa cuối**: 2017-09-11 15:02:49.897000

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
CREATE FUNCTION [dbo].[GetSoLuongDotChayBookingByHopDongChiTiet]
(
	-- Add the parameters for the function here
	@HopDongChiTietID INT
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Result INT
	SET @Result = (
	        SELECT SUM(ISNULL(DATEDIFF(DAY, b.NgayBatDau, b.NgayKetThuc) + 1,0))
	        FROM   DotChayHopDongChiTiet dchdct
	               INNER JOIN Booking b
	                    ON  b.BookingID = dchdct.BookingREF
	                    AND dchdct.HopDongChiTietREF = @HopDongChiTietID
	                    AND b.[Status] IN (2, 3, 5)
	    )
	-- Return the result of the function
	RETURN @Result
END

```
