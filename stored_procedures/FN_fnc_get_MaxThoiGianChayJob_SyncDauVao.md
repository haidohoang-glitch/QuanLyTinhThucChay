# Function: `fnc_get_MaxThoiGianChayJob_SyncDauVao`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2026-03-10 11:31:56.620000
- **Ngày sửa cuối**: 2026-03-10 11:31:56.620000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `datetime(8)` | Yes |
| `@ngayKiemTra` | `date(3)` | No |
| `@loaiSanPhamCode` | `varchar(50)` | No |

## Definition (Source Code)

```sql

CREATE FUNCTION [dbo].[fnc_get_MaxThoiGianChayJob_SyncDauVao](
	@ngayKiemTra DATE,
	@loaiSanPhamCode VARCHAR(50)
)
RETURNS DATETIME
AS 
BEGIN
	DECLARE @ngayKiemTra1 DATE;
	DECLARE @result VARCHAR(100);

	IF(@ngayKiemTra IS NULL)
		SET @ngayKiemTra1 = GETDATE();
	ELSE 
		SET @ngayKiemTra1 = @ngayKiemTra;

	SELECT @result = CONVERT(VARCHAR(20), @ngayKiemTra1, 23) + ' ' + CONVERT(VARCHAR(20), ThoiGianBatDau,108)
	FROM dbo.QLTC_JobDongBoDuLieuDauVaoConfig
	WHERE LoaiSanPhamCode = @loaiSanPhamCode AND IsDeleted = 0

	RETURN CONVERT(DATETIME, @result)
END







```
