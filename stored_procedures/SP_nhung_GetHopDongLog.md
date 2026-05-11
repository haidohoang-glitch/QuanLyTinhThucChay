# Stored Procedure: `nhung_GetHopDongLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 11:29:28.530000
- **Ngày sửa cuối**: 2026-03-05 11:29:28.530000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_GetHopDongLog
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT *
	FROM dbo.HopDongLog 
	WHERE HopDongID = (SELECT HopDongFK FROM dbo.HopDongChiTiet WHERE HopDongChiTietID = @HopDongChiTietID AND DeletedStatus=0 )
	AND DeletedStatus = 0;

END

```
