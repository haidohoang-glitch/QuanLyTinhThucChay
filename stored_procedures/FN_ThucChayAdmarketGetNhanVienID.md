# Function: `ThucChayAdmarketGetNhanVienID`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-12-25 17:19:22.040000
- **Ngày sửa cuối**: 2014-10-14 10:39:28.810000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `int(4)` | Yes |
| `@HoVaTen` | `nvarchar(100)` | No |
| `@Email` | `nvarchar(100)` | No |
| `@Phone` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhaMQ
-- Create date: 2013-12-06
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION dbo.ThucChayAdmarketGetNhanVienID 
(
	-- Add the parameters for the function here
	@HoVaTen NVARCHAR(50),
	@Email NVARCHAR(50),
	@Phone NVARCHAR(50)
)
RETURNS INT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @NhanVienID INT

	-- Add the T-SQL statements to compute the return value here
	SET @NhanVienID  = (SELECT TOP 1 A.NhanSuSoYeuLyLichID
						FROM NhanSuSoYeuLyLichFull A
						WHERE
							A.HoVaTen = @HoVaTen 
							OR A.Email = @Email
							OR A.DienThoai = @Phone
	)
	
	IF @NhanVienID IS NULL
		SET @NhanVienID = 0;

	-- Return the result of the function
	RETURN @NhanVienID

END

```
