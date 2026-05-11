# Function: `GetIDByTenBoPhanNghiepVu`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-09 05:14:08.317000
- **Ngày sửa cuối**: 2014-10-14 10:39:36.223000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@DmBoPhanNghiepVuID` | `int(4)` | No |
| `@TenBoPhanNghiepVu` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION GetIDByTenBoPhanNghiepVu
(
	-- Add the parameters for the function here
	@DmBoPhanNghiepVuID int,
	@TenBoPhanNghiepVu nvarchar(50)

)
RETURNS int
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Result int ,@RecordCount int
	
	set @RecordCount = (Select count(*) DmPhongBanID from DmBoPhanNghiepVu where dbo.FormatStringUpper(TenBoPhanNghiepVu) =dbo.FormatStringUpper(@TenBoPhanNghiepVu))
	
	if(@RecordCount = 1)
		 set @DmBoPhanNghiepVuID = (Select DmBoPhanNghiepVuID from DmBoPhanNghiepVu where dbo.FormatStringUpper(TenBoPhanNghiepVu) =dbo.FormatStringUpper(@TenBoPhanNghiepVu))

	-- Return the result of the function
	RETURN @DmBoPhanNghiepVuID

END

```
