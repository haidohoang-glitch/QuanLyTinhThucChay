# Stored Procedure: `sp_TinhDonGiaNgayHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 16:11:15.097000
- **Ngày sửa cuối**: 2026-03-06 16:11:15.097000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.sp_TinhDonGiaNgayHopDong
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

    ;WITH TongNgay AS (
        SELECT 
            SUM(
                DATEDIFF(DAY,
                    TRY_CONVERT(DATETIME, ThoiGianBatDau),
                    TRY_CONVERT(DATETIME, ThoiGianKetThuc)
                ) + 1
            ) AS TongSoNgayDotchay
        FROM dbo.DotChayHopDongChiTiet
        WHERE HopDongChiTietREF = @HopDongChiTietID
          AND DeletedStatus = 0
    )
    SELECT
        dbo.FormatNumber(hdct.ThanhTien) AS ThanhTienHopDong,
        t.TongSoNgayDotchay AS TongSoNgay,

        -- Đơn giá 1 ngày
        dbo.FormatNumber(
            CASE 
                WHEN t.TongSoNgayDotchay > 0 
                THEN hdct.ThanhTien * 1.0 / t.TongSoNgayDotchay
                ELSE NULL
            END
        ) AS DonGia_1_Ngay

    FROM dbo.HopDongChiTiet hdct
    CROSS JOIN TongNgay t
    WHERE hdct.HopDongChiTietID = @HopDongChiTietID
      AND hdct.DeletedStatus = 0;

END

```
