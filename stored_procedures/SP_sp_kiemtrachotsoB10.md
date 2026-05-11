# Stored Procedure: `sp_kiemtrachotsoB10`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-17 17:50:29.503000
- **Ngày sửa cuối**: 2026-03-19 17:00:40.247000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `date(3)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.sp_kiemtrachotsoB10
    @NgayBatDau DATE
AS
BEGIN
    SET NOCOUNT ON;

    -----------------------------------------
    -- B10: Check Giá Trị Thay Đổi bất thường
    -----------------------------------------
    SELECT 
        SoHopDong,
        HopDongID,
        DmSanPhamREF,
        TenHinhThucQuangCao,
        TenSanPham,
        HopDongChiTietREF,

        -- Giá trị raw để sort / xử lý
        dbo.FormatNumber(SUM(t.GiaTriThayDoi)) AS TongThayDoi

    FROM dbo.ThucChayDaTinh t
    WHERE 
        t.GiaTriThayDoi <> 0
        AND t.NgayThucHien >= @NgayBatDau   -- tránh CONVERT để nhanh hơn
    GROUP BY 
        SoHopDong, HopDongID, DmSanPhamREF,
        TenSanPham, HopDongChiTietREF, TenHinhThucQuangCao
    HAVING 
        ABS(ROUND(SUM(t.GiaTriThayDoi), 0)) > 1000   -- tương đương NOT BETWEEN -1000 AND 1000

    ORDER BY ROUND(SUM(t.GiaTriThayDoi),0) ASC   -- sort đúng theo số

END

```
