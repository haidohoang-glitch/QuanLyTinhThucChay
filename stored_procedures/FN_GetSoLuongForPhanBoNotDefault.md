# Function: `GetSoLuongForPhanBoNotDefault`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2014-09-26 10:25:33.453000
- **Ngày sửa cuối**: 2014-10-14 10:39:35.557000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@IsKhuyenMai` | `int(4)` | No |
| `@ChietKhau` | `float(8)` | No |
| `@ProductUnitName` | `nvarchar(100)` | No |
| `@ThanhTien` | `float(8)` | No |
| `@SoLuong` | `float(8)` | No |
| `@DonGiaHD` | `float(8)` | No |
| `@DonGiaTheoDonVi` | `float(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date, ,>
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION GetSoLuongForPhanBoNotDefault 
(
	-- Add the parameters for the function here
	@IsKhuyenMai INT,
	@ChietKhau FLOAT,
	@ProductUnitName NVARCHAR(50),
	@ThanhTien FLOAT,
	@SoLuong FLOAT,
	@DonGiaHD FLOAT,
	@DonGiaTheoDonVi FLOAT	
)
RETURNS FLOAT
AS
BEGIN
	-- Declare the return variable here
	DECLARE @ResultValue FLOAT
	SET @ResultValue = 0;

	-- Add the T-SQL statements to compute the return value here
	SET @ResultValue = (select
			CASE 
				WHEN ((@IsKhuyenMai=0) AND (@ChietKhau <> 100) AND (UPPER(@ProductUnitName) = 'CPM')) then ISNULL(@ThanhTien*100/(@DonGiaTheoDonVi*(100-@ChietKhau)),0)*1000
				WHEN ((@IsKhuyenMai=0) AND (@ChietKhau <> 100) AND (UPPER(@ProductUnitName) = 'CPC')) then ISNULL(@ThanhTien*100/(@DonGiaTheoDonVi*(100-@ChietKhau)),0)
				WHEN (@IsKhuyenMai <> 0 AND (UPPER(@ProductUnitName) = 'CPM')) THEN (@SoLuong*@DonGiaHD/@DonGiaTheoDonVi)/1000
				WHEN (@IsKhuyenMai <> 0 AND (UPPER(@ProductUnitName) = 'CPC')) THEN (@SoLuong*@DonGiaHD/@DonGiaTheoDonVi)		  		  
				else 0
			 END
			)
	-- Return the result of the function
	RETURN @ResultValue;

END

```
