# Function: `ThucChay_CheckIsInternalChanelVcc`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-07-17 12:22:54.350000
- **Ngày sửa cuối**: 2015-07-17 12:22:54.350000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@UserName` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2015-02-13
-- Description:	<Description, ,>
-- =============================================
/*
	PRINT dbo.ThucChay_CheckIsInternalChanelVcc('tungdanhnhu')
*/
CREATE FUNCTION [dbo].[ThucChay_CheckIsInternalChanelVcc]
(
	-- Add the parameters for the function here
	@UserName NVARCHAR(50)
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ReturnValue INT = 0

	-- Add the T-SQL statements to compute the return value here
	IF(EXISTS(SELECT TenDangNhap FROM AdminBoPhanWebsite A WHERE A.TenDangNhap = @UserName AND A.DmLoaiDoiTuongREF = 3)
	)
	BEGIN
		SET @ReturnValue = 1;
	END

	-- Return the result of the function
	RETURN @ReturnValue

END

```
