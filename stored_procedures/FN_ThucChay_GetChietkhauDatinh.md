# Function: `ThucChay_GetChietkhauDatinh`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2024-08-21 16:24:16.630000
- **Ngày sửa cuối**: 2024-08-21 16:24:16.630000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `float(8)` | Yes |
| `@NgayThucHien` | `datetime(8)` | No |
| `@HopDongChiTietID` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE FUNCTION [dbo].[ThucChay_GetChietkhauDatinh]
(
	@NgayThucHien datetime,
	@HopDongChiTietID nvarchar(50)	
)
RETURNS FLOAT
AS
BEGIN
	DECLARE @ChietkhauTaiNgayThucHien FLOAT
	
	SELECT TOP (1) @ChietkhauTaiNgayThucHien = ChietKhau
	FROM dbo.thucchaydatinh
	WHERE NgayThucHien  = @NgayThucHien and
	      HopDongChiTietREF = @HopDongChiTietID
	ORDER BY LastModifiedAt desc
	-- Return the result of the function
	RETURN @ChietkhauTaiNgayThucHien

END

```
