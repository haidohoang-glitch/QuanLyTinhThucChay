# Function: `GetDotChayBookingByHopDongChiTiet`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2017-09-11 15:02:49.770000
- **Ngày sửa cuối**: 2023-10-06 17:07:23.200000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(2000)` | Yes |
| `@HopDongChiTietID` | `int(4)` | No |
| `@LayDotChayYN` | `nvarchar(2)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author then 		<Author,,Name>
-- Create date then  <Create Date, ,>
-- Description then 	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[GetDotChayBookingByHopDongChiTiet]
(
	-- Add the parameters for the function here
	@HopDongChiTietID INT,
	@LayDotChayYN NVARCHAR(1)
)
RETURNS nvarchar(1000)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Result nvarchar(1000)
	SET @Result = ''
	SET @LayDotChayYN = UPPER(@LayDotChayYN)
	IF(@LayDotChayYN = 'Y')
		BEGIN
			SET @Result = (        
			-- Add the T-SQL statements to compute the return value here
				(SELECT STUFF(
					(
						SELECT (Convert(NVARCHAR(50),dchdct.BookingREF) + ' : ' 
									+ convert(NVARCHAR(10),dchdct.ThoiGianBatDau,101) + ' - ' 
									+ Convert(NVARCHAR(10), dchdct.ThoiGianKetThuc,101)) + CAST(';' AS VARCHAR(max)) 
							FROM DotChayHopDongChiTiet dchdct
							WHERE dchdct.HopDongChiTietREF = @HopDongChiTietID
							and dchdct.DeletedStatus = 0
							ORDER BY dchdct.BookingREF
							FOR XML PATH('')
					),1,0,'') AS dotchay
				)			
	
			)	
		END
	ELSE
		BEGIN
			--SET @Result = (
			--	(SELECT STUFF(
			--		( 
			--			SELECT (Convert(NVARCHAR(50),b.BookingID) + ' : ' 
			--					  + convert(NVARCHAR(10),b.NgayBatDau,101) + ' - ' 
			--					  + Convert(NVARCHAR(10), b.NgayKetThuc,101)) + CAST(';' AS VARCHAR(max)) 
			--				FROM DotChayHopDongChiTiet dchdct
			--				INNER JOIN Booking b ON b.BookingID = dchdct.BookingREF
			--				AND dchdct.HopDongChiTietREF = @HopDongChiTietID
			--				AND b.[Status] IN (2,3,5)
			--				ORDER BY b.BookingID
			--				FOR XML PATH('')
			--		),1,0,'') AS dotchay
			--	)
			--)	
			SET @Result = (
				(SELECT STUFF(
					( 
						SELECT (Convert(NVARCHAR(50),b.BookingREF) + ' : ' 
								  + convert(NVARCHAR(10),b.ThoiGianBatDau,101) + ' - ' 
								  + Convert(NVARCHAR(10), b.ThoiGianKetThuc,101)) + CAST(';' AS VARCHAR(max)) 
							FROM DotChayHopDongChiTiet dchdct
							INNER JOIN ThucChayHopDongChiTiet b ON b.HopDongChiTietREF = dchdct.HopDongChiTietREF 
							AND b.BookingREF = dchdct.BookingREF
							WHERE dchdct.HopDongChiTietREF = @HopDongChiTietID
							AND b.DeletedStatus = 0
							and dchdct.DeletedStatus = 0
							ORDER BY b.BookingREF
							FOR XML PATH('')
					),1,0,'') AS dotchay
				)
			)
		END
		-- Return the result of the function
	RETURN @Result

END

```
