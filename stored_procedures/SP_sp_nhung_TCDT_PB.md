# Stored Procedure: `sp_nhung_TCDT_PB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-24 15:27:32.177000
- **Ngày sửa cuối**: 2026-03-24 15:27:32.177000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietREF` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_nhung_TCDT_PB
    @HopDongChiTietREF NVARCHAR(50)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT 
        NgayThucHien,
        ThucChayDaTinhID,
        SoHopDong,
        HopDongID,
        HopDongChiTietREF,
        DmSanPhamREF,
        TenSanPham,
        TenHinhThucQuangCao,
        TenLoaiBanner,
        SoLuongTC,
        ThanhtienTC,
        SoLuongThucChayKM,
        ThanhTienKM,
        X.GhiChu,
        DotChayBooking
    FROM
    (
        -- ===== DATA CHI TIẾT =====
        SELECT
            0 AS SortKey,
            NgayThucHien,
            ThucChayDaTinhID,
            SoHopDong,
            HopDongID,
            HopDongChiTietREF,
            DmSanPhamREF,
            TenSanPham,
            TenHinhThucQuangCao,
            TenLoaiBanner,
            dbo.FormatNumber(SUM(SoLuongThucChay + SoLuongThayDoi))              AS SoLuongTC,
            dbo.FormatNumber(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)) AS ThanhtienTC,
            dbo.FormatNumber(SUM(SoLuongThucChayKM + SoLuongKMThayDoi))          AS SoLuongThucChayKM,
            dbo.FormatNumber(SUM(ThanhTienKM + GiaTriKMThayDoi))                AS ThanhTienKM,
            GhiChu,
            DotChayBooking
        FROM dbo.ThucChayDaTinh
        WHERE HopDongChiTietREF = @HopDongChiTietREF
        GROUP BY
            NgayThucHien,
            ThucChayDaTinhID,
            HopDongID,
            HopDongChiTietREF,
            DmSanPhamREF,
            TenSanPham,
            TenHinhThucQuangCao,
            TenLoaiBanner,
            SoHopDong,
            GhiChu,
            DotChayBooking

        UNION ALL

        -- ===== DÒNG TỔNG =====
        SELECT
            1 AS SortKey,
            NULL AS NgayThucHien,
            NULL AS ThucChayDaTinhID,
            NULL AS SoHopDong,
            NULL AS HopDongID,
            NULL AS HopDongChiTietREF,
            NULL AS DmSanPhamREF,
            N'TỔNG' AS TenSanPham,
            NULL AS TenHinhThucQuangCao,
            NULL AS TenLoaiBanner,
            dbo.FormatNumber(SUM(SoLuongThucChay + SoLuongThayDoi)),
            dbo.FormatNumber(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)),
            dbo.FormatNumber(SUM(SoLuongThucChayKM + SoLuongKMThayDoi)),
            dbo.FormatNumber(SUM(ThanhTienKM + GiaTriKMThayDoi)),
            NULL AS GhiChu,
            NULL AS DotChayBooking
        FROM dbo.ThucChayDaTinh
        WHERE HopDongChiTietREF = @HopDongChiTietREF
    ) X
    ORDER BY
        X.SortKey,
        X.NgayThucHien DESC;
END;

```
