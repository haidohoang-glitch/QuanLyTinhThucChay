# Function: `GetMaSoKhong`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2015-04-15 15:55:52.030000
- **Ngày sửa cuối**: 2015-04-15 15:55:52.030000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `varchar(50)` | Yes |
| `@MaKhachHang` | `int(4)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[GetMaSoKhong]
(
	-- Add the parameters for the function here
	@MaKhachHang INT 
)
RETURNS VARCHAR(50)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Result VARCHAR(50), @ThuongSo INT 
	SET @Result = ''
	
	 
	IF(@MaKhachHang>=100000)
		SET @Result = ''
	ELSE
		IF(@MaKhachHang>=10000)
			SET @Result = '0'		
		ELSE
			IF(@MaKhachHang>=1000)
				SET @Result = '00'	
			ELSE
				IF(@MaKhachHang>=100)
					SET @Result = '000'					
				ELSE
					IF(@MaKhachHang>=10)
						SET @Result = '0000'	
					ELSE
						SET @Result = '00000'																		
	-- Return the result of the function
	RETURN @Result

END

```
