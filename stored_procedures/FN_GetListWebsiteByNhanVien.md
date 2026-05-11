# Function: `GetListWebsiteByNhanVien`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-09-03 01:44:15.567000
- **Ngày sửa cuối**: 2014-10-14 10:39:36.063000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@TenDangNhap` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-09-02
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[GetListWebsiteByNhanVien] 
(
	-- Add the parameters for the function here
	@TenDangNhap nvarchar(50)
)
RETURNS NVARCHAR(4000)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ReturnValue nvarchar(max)
	SET @ReturnValue = '';
	
	IF EXISTS(select A.DmWebsiteREF
				from AdminBoPhanWebsite A
				WHERE A.TenDangNhap = @TenDangNhap AND A.DmWebsiteREF > 0
				)
	BEGIN
		SET @ReturnValue = ISNULL((SELECT
		stuff(
		(
		select ',' + CONVERT(NVARCHAR(50),A.DmWebsiteREF)
		from AdminBoPhanWebsite A
		WHERE A.TenDangNhap = @TenDangNhap AND A.DmWebsiteREF > 0
		order by A.DmWebsiteREF
		for xml path('') 
		), 1, 1, '') AS DmWebsiteREF
		),'')
	END
	

	-- Return the result of the function
	RETURN @ReturnValue

END
```
