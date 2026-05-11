# Stored Procedure: `nhung_ChitietGetHopDongByChiTietID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 10:48:12.640000
- **Ngày sửa cuối**: 2026-03-05 10:48:12.640000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_ChitietGetHopDongByChiTietID
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT 
        hd.SoHopDong,
        hd.HopDongID,
        hd.DmKhachHangREF,
        hd.TenKhachHang,
        hd.TrangThaiHopDong,
        hd.DmNhanGocREF,
        hd.TenNhanGoc,
        dbo.FormatNumber(hd.GiaTriHopDong) AS GiaTriHopDong,
        hd.CreatedAt,
        hd.LastModifiedAt
    FROM dbo.HopDong hd
    WHERE hd.HopDongID = (
        SELECT TOP 1 HopDongFK
        FROM dbo.HopDongChiTiet
        WHERE HopDongChiTietID = @HopDongChiTietID
              AND DeletedStatus = 0
    )
    AND hd.DeletedStatus = 0;
END

```
