# Function: `ThucChay_IsDotChayDaCoThucTreo`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-06-10 10:04:01.010000
- **Ngày sửa cuối**: 2014-10-14 10:39:29.577000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@BookingREF` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-11-13
-- Description:	Check phân bổ là khuyến mại hay không
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_IsDotChayDaCoThucTreo] 
(
	@HopDongChiTietREF INT,
	@BookingREF INT
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @IsDotChayDaChay INT
	
	SET @IsDotChayDaChay = 0 --Dot chay cua hopdongchitiet chua co thuc treo, >0 da co thuc treo
	
	SET @IsDotChayDaChay =
	(
		SELECT count(tchdct.HopDongChiTietREF)
		  FROM ThucChayHopDongChiTiet tchdct
		INNER JOIN HopDongChiTiet hdct ON hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
		WHERE tchdct.DeletedStatus = 0
		AND hdct.DeletedStatus = 0
		AND tchdct.BookingREF = @BookingREF
		AND tchdct.HopDongChiTietREF = @HopDongChiTietREF	
	)
	SET @IsDotChayDaChay = ISNULL(@IsDotChayDaChay,0)

	-- Return the result of the function
	RETURN @IsDotChayDaChay

END

```
