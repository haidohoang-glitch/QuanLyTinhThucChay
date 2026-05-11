# Stored Procedure: `sp_nhung_TCDT_SHĐ`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-24 15:25:19.370000
- **Ngày sửa cuối**: 2026-03-24 15:25:19.370000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_nhung_TCDT_SHĐ
    @SoHopDong NVARCHAR(50)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT 
        sohopdong,
        HopDongID,
        HopDongChiTietREF,
        DmSanPhamREF,
        TenSanPham,
        TenHinhThucQuangCao,
        TenLoaiBanner,
        SoLuongTC,
        ThanhtienTC,
        SoLuongThucChayKM,
        ThanhTienKM
    FROM
    (
        -- ===== DATA CHI TIẾT =====
        SELECT
            0 AS SortKey,
            sohopdong,
            HopDongID,
            HopDongChiTietREF,
            DmSanPhamREF,
            TenSanPham,
            TenHinhThucQuangCao,
            TenLoaiBanner,
            dbo.FormatNumber(SUM(SoLuongThucChay + SoLuongThayDoi))              AS SoLuongTC,
            dbo.FormatNumber(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)) AS ThanhtienTC,
            dbo.FormatNumber(SUM(SoLuongThucChayKM + SoLuongKMThayDoi))          AS SoLuongThucChayKM,
            dbo.FormatNumber(SUM(ThanhTienKM + GiaTriKMThayDoi))                AS ThanhTienKM
        FROM dbo.ThucChayDaTinh
        WHERE SoHopDong = @SoHopDong
        GROUP BY
            HopDongID,
            HopDongChiTietREF,
            DmSanPhamREF,
            TenSanPham,
            TenHinhThucQuangCao,
            TenLoaiBanner,
            sohopdong

        UNION ALL

        -- ===== DÒNG TỔNG =====
        SELECT
            1 AS SortKey,
            NULL AS sohopdong,
            NULL AS HopDongID,
            NULL AS HopDongChiTietREF,
            NULL AS DmSanPhamREF,
            N'TỔNG' AS TenSanPham,
            NULL AS TenHinhThucQuangCao,
            NULL AS TenLoaiBanner,
            dbo.FormatNumber(SUM(SoLuongThucChay + SoLuongThayDoi)),
            dbo.FormatNumber(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)),
            dbo.FormatNumber(SUM(SoLuongThucChayKM + SoLuongKMThayDoi)),
            dbo.FormatNumber(SUM(ThanhTienKM + GiaTriKMThayDoi))
        FROM dbo.ThucChayDaTinh
        WHERE SoHopDong = @SoHopDong
    ) X
    ORDER BY X.SortKey ASC;
END;

```
