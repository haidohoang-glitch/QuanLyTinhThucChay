# Function: `ThucChay_GetThanhTienThucChayKenh`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-12-06 18:30:56.600000
- **Ngày sửa cuối**: 2014-10-14 10:39:29.673000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@SoHopDong` | `varchar(50)` | No |
| `@ThanhTienThucChay` | `float(8)` | No |
| `@TenDangNhap` | `varchar(50)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-12-03
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GetThanhTienThucChayKenh] 
(
	-- Add the parameters for the function here
	@SoHopDong VARCHAR(50),
	@ThanhTienThucChay FLOAT,
	@TenDangNhap VARCHAR(50)
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ReturnValue FLOAT = 0;
	DECLARE @SettingValue NVARCHAR(100);
	DECLARE @GroupID INT

	SET @SettingValue = (SELECT A.SettingValues
	FROM AdminUser A 
		INNER JOIN AdminGroupUser B ON B.AdminUserId = A.AdminUserId
	WHERE A.Username = @TenDangNhap)
	
	SET @GroupID = (SELECT B.AdminGroupId
	                FROM AdminUser A 
						INNER JOIN AdminGroupUser B ON B.AdminUserId = A.AdminUserId
	                WHERE A.Username = @TenDangNhap)
	
	--IF ((LOWER(@SettingValue) = 'null' OR @SettingValue IS NULL) AND (CHARINDEX('NB',@SoHopDong) > 0))
	--	SET @ReturnValue = 0
	--ELSE
	--	SET @ReturnValue = @ThanhTienThucChay
	
	IF (CHARINDEX('NB',@SoHopDong) > 0 AND (LOWER(@SettingValue) = 'null' OR @SettingValue IS NULL) AND @GroupID = 136)
		SET @ReturnValue = 0
	ELSE 
		SET @ReturnValue = @ThanhTienThucChay;

	-- Return the result of the function
	RETURN @ReturnValue

END

```
