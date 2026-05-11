# Stored Procedure: `sp_nhung_TCDT_Banner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-24 15:35:30.513000
- **Ngày sửa cuối**: 2026-03-24 15:35:30.513000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmBannerREF` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_nhung_TCDT_Banner
    @DmBannerREF NVARCHAR(50)
AS
BEGIN
    SET NOCOUNT ON;

    ;WITH PR AS 
    (
        SELECT TOP (1)
            HopDongChiTietREF,
            DmBannerREF
        FROM dbo.ThucChayHopDongChiTiet
        WHERE DmBannerREF = @DmBannerREF
          AND DeletedStatus = 0
    ),
    MainData AS
    (
        SELECT
            tcdt.NgayThucHien,
            tcdt.ThucChayDaTinhID,
            tcdt.HopDongID,
            tcdt.HopDongChiTietREF,
            tcdt.DmSanPhamREF,
            tcdt.TenSanPham,
            tcdt.TenHinhThucQuangCao,
            tcdt.TenLoaiBanner,
            SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi)              AS SoLuongTC,
            SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS ThanhtienTC,
            SUM(tcdt.SoLuongThucChayKM + tcdt.SoLuongKMThayDoi)          AS SoLuongThucChayKM,
            SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi)                 AS ThanhTienKM
        FROM dbo.ThucChayDaTinh tcdt
        JOIN PR
          ON tcdt.HopDongChiTietREF = PR.HopDongChiTietREF
         AND TRY_CONVERT(INT, tcdt.DmBannerREF) = PR.DmBannerREF
        GROUP BY
            tcdt.NgayThucHien,
            tcdt.ThucChayDaTinhID,
            tcdt.HopDongID,
            tcdt.HopDongChiTietREF,
            tcdt.DmSanPhamREF,
            tcdt.TenSanPham,
            tcdt.TenHinhThucQuangCao,
            tcdt.TenLoaiBanner
    )

    SELECT
        NgayThucHien,
        ThucChayDaTinhID,
        HopDongID,
        HopDongChiTietREF,
        DmSanPhamREF,
        TenSanPham,
        TenHinhThucQuangCao,
        TenLoaiBanner,
        dbo.FormatNumber(SoLuongTC)         AS SoLuongTC,
        dbo.FormatNumber(ThanhtienTC)       AS ThanhtienTC,
        dbo.FormatNumber(SoLuongThucChayKM) AS SoLuongThucChayKM,
        dbo.FormatNumber(ThanhTienKM)       AS ThanhTienKM
    FROM
    (
        -- ===== DATA CHI TIẾT =====
        SELECT
            0 AS SortKey,
            *
        FROM MainData

        UNION ALL

        -- ===== DÒNG TỔNG =====
        SELECT
            1 AS SortKey,
            NULL AS NgayThucHien,
            NULL AS ThucChayDaTinhID,
            NULL AS HopDongID,
            NULL AS HopDongChiTietREF,
            NULL AS DmSanPhamREF,
            N'TỔNG' AS TenSanPham,
            NULL AS TenHinhThucQuangCao,
            NULL AS TenLoaiBanner,
            SUM(SoLuongTC),
            SUM(ThanhtienTC),
            SUM(SoLuongThucChayKM),
            SUM(ThanhTienKM)
        FROM MainData
    ) X
    ORDER BY
        X.SortKey,
        X.NgayThucHien DESC;
END;

```
