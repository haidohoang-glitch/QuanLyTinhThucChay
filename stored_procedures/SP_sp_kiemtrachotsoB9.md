# Stored Procedure: `sp_kiemtrachotsoB9`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-17 17:43:29.357000
- **Ngày sửa cuối**: 2026-03-17 17:43:29.357000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NamBatDau` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.sp_kiemtrachotsoB9
    @NamBatDau INT = 2019
AS
BEGIN
    SET NOCOUNT ON;

    -----------------------------------------
    -- B9: Check giá trị âm (Thực chạy / KM)
    -----------------------------------------
    SELECT 
        SoHopDong,
        HopDongID,
        HopDongChiTietID,
        DmSanPhamREF,
        dbo.FormatNumber(SUM(ThanhTienThucChay)) AS ThanhTienThucChay,
        dbo.FormatNumber(SUM(ThanhTienThucChayKM)) AS ThanhTienThucChayKM
    FROM KS_ThucChay_TCDT
    WHERE Nam >= @NamBatDau
        AND HopDongChiTietID NOT IN (595304, 574735) -- loại ngoại lệ
    GROUP BY 
        SoHopDong, HopDongID, HopDongChiTietID, DmSanPhamREF
    HAVING 
        ROUND(SUM(ThanhTienThucChay), 0) < 0
        OR ROUND(SUM(ThanhTienThucChayKM), 0) < 0

    ORDER BY HopDongID, HopDongChiTietID

END

```
