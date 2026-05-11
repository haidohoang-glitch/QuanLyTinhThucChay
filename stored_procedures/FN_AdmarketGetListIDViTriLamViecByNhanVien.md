# Function: `AdmarketGetListIDViTriLamViecByNhanVien`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-12-25 17:19:27.157000
- **Ngày sửa cuối**: 2014-10-14 10:39:38.153000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar` | Yes |
| `@DmPhongBanREF` | `nvarchar(400)` | No |
| `@DmBoPhanREF` | `nvarchar(400)` | No |
| `@DmNhomlamViecREF` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-12-18
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[AdmarketGetListIDViTriLamViecByNhanVien] 
(
	-- Add the parameters for the function here
	@DmPhongBanREF	nvarchar(200),
	@DmBoPhanREF		nvarchar(200),
	@DmNhomlamViecREF nvarchar(200)
)
RETURNS nvarchar(max)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ReturnValue nvarchar(max);
	
	SET @ReturnValue = '';

	IF @DmPhongBanREF <> ''
		SET @ReturnValue = @DmPhongBanREF;

	IF @DmBoPhanREF <> '' 
		SET @ReturnValue += '-' + @DmBoPhanREF;

	IF @DmNhomlamViecREF <> '' 
		SET @ReturnValue += '-' + @DmNhomlamViecREF;

	-- Return the result of the function
	RETURN @ReturnValue;

END

```
