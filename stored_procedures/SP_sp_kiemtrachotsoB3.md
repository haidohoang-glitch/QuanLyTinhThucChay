# Stored Procedure: `sp_kiemtrachotsoB3`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-17 17:11:59.127000
- **Ngày sửa cuối**: 2026-03-18 09:18:05.870000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `date(3)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[sp_kiemtrachotsoB3]
	@NgayBatDau DATE
AS
BEGIN
    SET NOCOUNT ON;

       -----------------------------------------
    -- B3: Đếm số record theo ngày
    -----------------------------------------
    SELECT NgayThucHien,
        dbo.FormatNumber(COUNT(*)) AS Tong        
    FROM ThucChayDaTinh
    WHERE NgayThucHien >= @NgayBatDau
    GROUP BY NgayThucHien
    ORDER BY NgayThucHien

END

```
