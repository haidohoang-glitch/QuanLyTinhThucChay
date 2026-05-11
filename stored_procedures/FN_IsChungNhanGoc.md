# Function: `IsChungNhanGoc`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2016-10-05 09:36:31.543000
- **Ngày sửa cuối**: 2016-10-05 09:58:48.557000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@IDNhan1` | `nvarchar(100)` | No |
| `@IDNhan2` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
--SELECT IsChungNhanGoc()
CREATE FUNCTION IsChungNhanGoc
(
	-- Add the parameters for the function here
	@IDNhan1 nvarchar(50),
	@IDNhan2 nvarchar(50)
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @IsNhanGoc int = 0
	DECLARE @NhanGoc1 int = 0, @NhanGoc2 int = 0 
	

	-- Add the T-SQL statements to compute the return value here
	SET @NhanGoc1 = (SELECT CONVERT(NVARCHAR(50),DmNhanHangGocREF) FROM ABM_Tuyetnta.dbo.DmCaseNhanHang WHERE DmNhanHangID = @IDNhan1)
	SET @NhanGoc2 = (SELECT CONVERT(NVARCHAR(50),DmNhanHangGocREF) FROM ABM_Tuyetnta.dbo.DmCaseNhanHang WHERE DmNhanHangID = @IDNhan2)

	IF @NhanGoc1 = @NhanGoc2 
		SET @IsNhanGoc = 1
	-- Return the result of the function
	RETURN @IsNhanGoc

END

```
