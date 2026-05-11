# Function: `FormatDonViTinh_ThanhTien_GGFB`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2020-08-17 15:09:39.573000
- **Ngày sửa cuối**: 2020-08-17 15:09:44.743000

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
CREATE FUNCTION [dbo].[FormatDonViTinh_ThanhTien_GGFB]
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
		 WHEN N'Engagement' THEN N'Engagement'
		 WHEN N'Impressions' THEN N'Impression'
		 WHEN N'Leads' THEN N'Lead'
		 WHEN N'Clicks' THEN N'CLICK'
		 WHEN N'Reach' THEN N'Reach'
		 WHEN N'Views' THEN N'VIEW'
		 ELSE @DonViTinh
	END	
		
		

	-- Return the result of the function
	RETURN @Result

END

```
