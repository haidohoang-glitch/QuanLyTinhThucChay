# Stored Procedure: `sp_nhung_TCDT_Chiphi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-24 15:40:55.673000
- **Ngày sửa cuối**: 2026-03-24 15:40:55.673000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ThucChayHopDongChiTietID` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_nhung_TCDT_Chiphi
    @ThucChayHopDongChiTietID NVARCHAR(50)
AS
BEGIN
    SET NOCOUNT ON;

    ;WITH PR AS
    (
        SELECT TOP (1)
            HopDongREF,
            ThucChayHopDongChiTietID
        FROM dbo.ThucChayHopDongChiTiet
        WHERE ThucChayHopDongChiTietID = @ThucChayHopDongChiTietID
        --AND DeletedStatus = 0
    ),
    MainData AS
    (
        SELECT
            tcdt.NgayThucHien,
            tcdt.ThucChayDaTinhID,
            tcdt.HopDongID,
            tcdt.HopDongChiTietREF,
            tcdt.DotChayBooking,
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
          ON tcdt.HopDongID = PR.HopDongREF
         AND TRY_CONVERT(INT, LEFT(tcdt.DotChayBooking, CHARINDEX(':', tcdt.DotChayBooking + ':') - 1)) 
             = PR.ThucChayHopDongChiTietID
        GROUP BY
            tcdt.NgayThucHien,
            tcdt.ThucChayDaTinhID,
            tcdt.HopDongID,
            tcdt.HopDongChiTietREF,
            tcdt.DmSanPhamREF,
            tcdt.TenSanPham,
            tcdt.TenHinhThucQuangCao,
            tcdt.TenLoaiBanner,
            tcdt.DotChayBooking
    )

    -- ===== RESULT =====
    SELECT
        NgayThucHien,
        ThucChayDaTinhID,
        HopDongID,
        HopDongChiTietREF,
        DotChayBooking,
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
            NULL AS DotChayBooking,
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
