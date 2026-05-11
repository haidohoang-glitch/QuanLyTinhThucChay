# Function: `GetDotChayThucTreoByHopDongChiTiet`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-06-24 16:42:22.420000
- **Ngày sửa cuối**: 2014-10-14 10:39:36.417000

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
CREATE FUNCTION [dbo].[GetDotChayThucTreoByHopDongChiTiet]
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
				(SELECT STUFF(
					( 
						SELECT (Convert(NVARCHAR(50),b.BookingREF) + ' : ' 
								  + convert(NVARCHAR(10),b.ThoiGianBatDau,101) + ' - ' 
								  + Convert(NVARCHAR(10), b.ThoiGianKetThuc,101)) + CAST(';' AS VARCHAR(max)) 
							FROM ThucChayHopDongChiTiet b  
							WHERE b.HopDongChiTietREF = @HopDongChiTietID
							AND b.DeletedStatus = 0
							--AND b.RecordStatus = 0
							ORDER BY b.BookingREF
							FOR XML PATH('')
					),1,0,'') AS dotchay
				)
			)
			
		END
	ELSE
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
							AND dchdct.DeletedStatus = 0
							--AND dchdct.RecordStatus = 0
							ORDER BY dchdct.BookingREF
							FOR XML PATH('')
					),1,0,'') AS dotchay
				)			
	
			)	
		END
		-- Return the result of the function
	RETURN @Result

END

```
