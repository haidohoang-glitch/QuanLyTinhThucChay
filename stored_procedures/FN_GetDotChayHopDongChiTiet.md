# Function: `GetDotChayHopDongChiTiet`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-09-28 15:30:26.593000
- **Ngày sửa cuối**: 2014-10-14 10:39:36.447000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[GetDotChayHopDongChiTiet]
(
	-- Add the parameters for the function here
	@HopDongChiTietID INT	
)
RETURNS NVARCHAR(4000)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Result NVARCHAR(4000)
	
	
	SET @Result = (
	
	SELECT
	REPLACE(
	    stuff((

        
 	SELECT ';' + CONVERT(NVARCHAR(50),B.ThoiGianBatDau,103) + '-' + CONVERT(NVARCHAR(50),B.ThoiGianKetThuc,103) FROM dbo.HopDongChiTiet A
	INNER JOIN dbo.DotChayHopDongChiTiet B ON A.HopDongChiTietID = B.HopDongChiTietREF
	WHERE A.HopDongChiTietID = @HopDongChiTietID	
	ORDER BY B.ThoiGianKetThuc ASC       
	
        for xml path('')
    ),1,1,'') 
    ,'-','-->'
    )
	)
	-- Return the result of the function
	
	IF(@Result IS NULL) SET @Result = 'NA'
	RETURN @Result

END

```
