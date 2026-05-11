# Function: `GetIDByTenPhongBan`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-06-09 05:20:57.453000
- **Ngày sửa cuối**: 2014-10-14 10:39:36.193000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@DmPhongBanID` | `int(4)` | No |
| `@TenPhongBan` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
create FUNCTION GetIDByTenPhongBan
(
	-- Add the parameters for the function here
	@DmPhongBanID int,
	@TenPhongBan nvarchar(50)

)
RETURNS int
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Result int ,@RecordCount int
	
	set @RecordCount = (Select count(*) from DmPhongBan where dbo.FormatStringUpper(TenPhongBan) =dbo.FormatStringUpper(@TenPhongBan))
	
	if(@RecordCount = 1)
		 set @DmPhongBanID = (Select top 1 DmPhongBanID from DmPhongBan where dbo.FormatStringUpper(TenPhongBan) =dbo.FormatStringUpper(@TenPhongBan))

	-- Return the result of the function
	RETURN @DmPhongBanID

END

```
