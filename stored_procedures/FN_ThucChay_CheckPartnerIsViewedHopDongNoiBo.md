# Function: `ThucChay_CheckPartnerIsViewedHopDongNoiBo`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-11-21 16:28:42.100000
- **Ngày sửa cuối**: 2014-10-14 10:39:33.907000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@TenDangNhap` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-11-21
-- Description:	Check partner is show NoiBo contract
-- =============================================
CREATE FUNCTION dbo.ThucChay_CheckPartnerIsViewedHopDongNoiBo 
(
	@TenDangNhap nvarchar(50)
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ReturnValue INT
	DECLARE @IsPartner INT
	
	IF EXISTS (SELECT A.UserName
				FROM AdminUser A
					INNER JOIN AdminGroupUser B ON B.AdminUserId = A.AdminUserId AND B.AdminGroupId = 9999
				WHERE 
					A.Username = @TenDangNhap)
	BEGIN
		IF EXISTS (SELECT B.Username FROM AdminUser B WHERE B.Username = @TenDangNhap AND (B.SettingValues <> '' OR B.SettingValues IS NOT NULL))
			SET @ReturnValue = 1
		ELSE 
			SET @ReturnValue = 0
	END
	ELSE
		SET @ReturnValue = 1 
			
	-- Return the result of the function
	RETURN @ReturnValue

END

```
