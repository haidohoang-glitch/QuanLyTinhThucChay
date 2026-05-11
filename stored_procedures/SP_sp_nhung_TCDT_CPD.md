# Stored Procedure: `sp_nhung_TCDT_CPD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-24 15:43:58.107000
- **Ngày sửa cuối**: 2026-03-24 15:43:58.107000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@BookingREF` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_nhung_TCDT_CPD
    @BookingREF INT
AS
BEGIN
    SET NOCOUNT ON;

    ;WITH PR AS
    (
        SELECT TOP (1)
            HopDongChiTietREF,
            TRY_CONVERT(INT, BookingREF) AS BookingREF
        FROM dbo.ThucChayHopDongChiTiet
        WHERE TRY_CONVERT(INT, BookingREF) = @BookingREF
          AND DeletedStatus = 0
        ORDER BY HopDongChiTietREF DESC
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
         AND TRY_CONVERT(INT, LEFT(tcdt.DotChayBooking, CHARINDEX(':', tcdt.DotChayBooking + ':') - 1)) 
             = @BookingREF
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

    -- ===== RESULT =====
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
        SELECT 0 AS SortKey, *
        FROM MainData

        UNION ALL

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
    ORDER BY X.SortKey, X.NgayThucHien DESC;
END;

```
