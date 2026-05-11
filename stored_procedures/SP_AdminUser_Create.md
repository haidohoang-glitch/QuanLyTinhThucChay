# Stored Procedure: `AdminUser_Create`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-06-05 16:15:44.450000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.770000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Username` | `nvarchar(500)` | No |
| `@Password` | `nvarchar(500)` | No |
| `@Email` | `nvarchar(500)` | No |
| `@FullName` | `nvarchar(500)` | No |
| `@Birthday` | `datetime(8)` | No |
| `@Gender` | `bit(1)` | No |
| `@Information` | `ntext(16)` | No |
| `@OxUserREF` | `int(4)` | No |
| `@Mobile` | `nvarchar(100)` | No |
| `@Status` | `int(4)` | No |
| `@SettingValues` | `nvarchar(256)` | No |
| `@CreatedOn` | `datetime(8)` | No |
| `@ModifiedOn` | `datetime(8)` | No |
| `@LastLoggedOn` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[AdminUser_Create]
(	
	@Username nvarchar (250),
	@Password nvarchar (250),
	@Email nvarchar (250),
	@FullName nvarchar (250),
	@Birthday datetime,
	@Gender bit,
	@Information ntext,
	@OxUserREF INT,
	@Mobile NVARCHAR(50),
	@Status int,
	@SettingValues NVARCHAR(128),
	@CreatedOn datetime,
	@ModifiedOn datetime,
	@LastLoggedOn datetime	
)
AS
INSERT INTO AdminUser
(	
	Username,
	[Password],
	Email,
	FullName,
	Birthday,
	Gender,
	Information,
	OxUserREF,
	Mobile,
	[Status],
	SettingValues,
	CreatedOn,
	ModifiedOn,
	LastLoggedOn
)
VALUES 
(
	@Username,
	@Password,
	@Email,
	@FullName,
	@Birthday,
	@Gender,
	@Information,
	@OxUserREF,
	@Mobile,
	@Status,
	@SettingValues,
	@CreatedOn,
	@ModifiedOn,
	@LastLoggedOn
)

-- Mapping Mobile to using OTP
--exec dbo.AdminMappingUserOTP @Username

DECLARE @ID INT SET @ID = SCOPE_IDENTITY();
SELECT @ID

```
