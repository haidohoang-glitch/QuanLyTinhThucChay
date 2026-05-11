# Stored Procedure: `nhung_TongHop_ThucChay_Performance`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 16:51:01.340000
- **Ngày sửa cuối**: 2026-03-05 16:51:01.340000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_TongHop_ThucChay_Performance
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @TongHDky FLOAT = ISNULL((
        SELECT ThanhTien
        FROM dbo.HopDongChiTiet
        WHERE HopDongChiTietID = @HopDongChiTietID
    ), 0);

    DECLARE @TongTCDT FLOAT = ISNULL((
        SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)
        FROM dbo.ThucChayDaTinh
        WHERE HopDongChiTietREF = @HopDongChiTietID
    ), 0);

    DECLARE @TongTCDTAdmarket FLOAT = ISNULL((
        SELECT SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)
        FROM dbo.ThucChayDaTinhAdmarket
        WHERE HopDongChiTietREF = @HopDongChiTietID
    ), 0);

    DECLARE @TongDieuChinh FLOAT, @KPI FLOAT;

    SELECT 
        @TongDieuChinh = ISNULL(SUM(SoTienThayDoi), 0),
        @KPI = ISNULL(SUM(TienThucChayKPI), 0)
    FROM dbo.ThucChay_PerformanceBase_ThayDoi
    WHERE HopDongChiTietREF = @HopDongChiTietID
        AND DeletedStatus = 0
        AND RecordStatus NOT IN (0,2);

    DECLARE @TongDomain FLOAT = ISNULL((
        SELECT SUM(CONVERT(FLOAT, domain_tt_money))
        FROM dbo.ThucChayAdmarket_PhanBo
        WHERE phanbo = @HopDongChiTietID
    ), 0);

    -- Xuất kết quả
    SELECT
        dbo.FormatNumber(@TongHDky) AS [HĐ ký],
        dbo.FormatNumber(@TongTCDT) AS [Tổng TCDT],
        dbo.FormatNumber(@TongTCDTAdmarket) AS [Tổng TCDT Admarket],
        dbo.FormatNumber(@TongDieuChinh) AS [Tổng Điều chỉnh],
        dbo.FormatNumber(@TongDomain) AS [Tổng Domain],
        dbo.FormatNumber(@KPI) AS [Tổng KPI],
        dbo.FormatNumber(@TongDieuChinh + @TongDomain) AS [Tổng Điều chỉnh + Domain],

        CASE         
            WHEN ABS(@TongTCDTAdmarket - @TongHDky) < 1
                THEN N'✅ Đủ thực chạy HĐ ký'
            WHEN ABS(@TongTCDTAdmarket - (@TongDieuChinh + @TongDomain)) < 1
                THEN N'✅ Đủ thực chạy với SP'
            WHEN (@TongDieuChinh + @TongDomain) > @TongHDky AND @TongTCDTAdmarket < @TongHDky
                THEN CONCAT(N'⚠️ Thiếu thực chạy với HĐ: ', dbo.FormatNumber(@TongHDky - @TongTCDTAdmarket))
            WHEN (@TongDieuChinh + @TongDomain) > @TongHDky AND @TongTCDTAdmarket > @TongHDky
                THEN CONCAT(N'⚠️ Vượt thực chạy với HĐ: ', dbo.FormatNumber(@TongTCDTAdmarket - @TongHDky))
            WHEN @TongTCDTAdmarket > (@TongDieuChinh + @TongDomain)
                THEN CONCAT(N'⚠️ Vượt thực chạy với SP: ', dbo.FormatNumber(@TongTCDTAdmarket - (@TongDieuChinh + @TongDomain)))
            WHEN @TongTCDTAdmarket < (@TongDieuChinh + @TongDomain)
                THEN CONCAT(N'⚠️ Thiếu thực chạy với SP: ', dbo.FormatNumber((@TongDieuChinh + @TongDomain) - @TongTCDTAdmarket))
            ELSE N'⚠️ Lệch'
        END AS [Ghi chú];

END

```
