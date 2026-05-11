# Function: `GetProductNameByTypeProduct`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-09-14 14:36:22.337000
- **Ngày sửa cuối**: 2019-03-06 16:46:52.390000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(100)` | Yes |
| `@TypeProduct` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author then 		<Author,,Name>
-- Create date then  <Create Date, ,>
-- Description then 	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[GetProductNameByTypeProduct]
(
	-- Add the parameters for the function here
	@TypeProduct int
)
RETURNS nvarchar(50)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Result nvarchar(50)
            
	-- Add the T-SQL statements to compute the return value here
	set @Result = case @TypeProduct
		when 1 then  N'Banner'
		when 2 then  N'Box App CPD'
		when 3 then  N'CPM Chuyên trang'
		when 4 then  N'CPM Mass'
		when 5 then  N'Balloon Ads'
		when 6 then  N'CPM mobile'
		when 7 then  N'CPM Admarket'
		when 8 then  N'TVC Online'
		when 9 then  N'Box App CPM'
		WHEN 10 THEN N'Mobile'
		WHEN 14 THEN N'King size'
		WHEN 15 THEN N'CPM Stick'
		WHEN 381 THEN N'SponsorPost'
		WHEN 16 THEN N'Brand Page'
		WHEN 17 THEN N'Content Network Sponsorship'
		WHEN 18 THEN N'Sponsor Page'
		WHEN 19 THEN N'Native ads'
		WHEN 585 THEN N'Adx'
		WHEN 5056 THEN N'Box Gallery Sản phẩm'
	end
	-- Return the result of the function
	RETURN @Result

END

```
