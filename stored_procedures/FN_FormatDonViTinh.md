# Function: `FormatDonViTinh`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-09 13:38:51.290000
- **Ngày sửa cuối**: 2022-10-05 15:37:44.567000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(100)` | Yes |
| `@DonViTinh` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[FormatDonViTinh]
(
	-- Add the parameters for the function here
	@DonViTinh nvarchar(50)
)
RETURNS nvarchar(50)
AS
BEGIN
	-- Declare the return variable here
	Declare @Result nvarchar(50)
	set @DonViTinh = dbo.FormatStringUpper(@DonViTinh)
	SET @Result = 
	CASE @DonViTinh
		 WHEN N'TUẦN' THEN 'NGÀY'
		 WHEN N'THÁNG' THEN 'NGÀY'
		 WHEN N'NĂM' THEN 'NGÀY'
		 WHEN 'CPC' THEN 'CLICK'
		 WHEN 'CPM' THEN 'VIEW'
		 WHEN N'GÓI' THEN N'GÓI'
		 ELSE @DonViTinh
	END	
		
		

	-- Return the result of the function
	RETURN @Result

END

```
