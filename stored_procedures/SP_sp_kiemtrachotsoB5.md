# Stored Procedure: `sp_kiemtrachotsoB5`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-17 17:30:12.917000
- **Ngày sửa cuối**: 2026-03-26 10:26:35.390000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `date(3)` | No |
| `@NgayKetThuc` | `date(3)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE dbo.sp_kiemtrachotsoB5
    @NgayBatDau DATE,
    @NgayKetThuc DATE
AS
BEGIN
    SET NOCOUNT ON;

    SELECT 
        t.NgayThucHien,
        CASE 
            WHEN GROUPING(t.TenSanPham) = 1 THEN N'TỔNG'
            ELSE t.TenSanPham
        END AS TenSanPham,
        t.DmSanPhamREF,
        dbo.FormatNumber(SUM(t.ThanhTienSauTrietKhauThucChay + t.GiaTriThayDoi)) AS ThanhTien
    FROM ThucChayDaTinh t
    WHERE t.NgayThucHien BETWEEN @NgayBatDau AND @NgayKetThuc
        AND NOT EXISTS (
            SELECT 1 
            FROM DmLoaiHopDongNoiBo nb
            WHERE nb.MaLoaiHopDong = t.TenMaHopDong
              AND nb.DeletedStatus = 0
        )
    GROUP BY GROUPING SETS (
        (t.NgayThucHien, t.TenSanPham, t.DmSanPhamREF), -- chi tiết
        (t.NgayThucHien) -- tổng theo ngày
    )
    ORDER BY 
        t.NgayThucHien,
        CASE 
            WHEN GROUPING(t.TenSanPham) = 1 THEN 1
            ELSE 0
        END,
        t.TenSanPham
END
```
