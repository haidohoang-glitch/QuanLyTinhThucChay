# Stored Procedure: `nhung_TCDT_Chiphi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 15:44:16.727000
- **Ngày sửa cuối**: 2026-03-06 15:44:16.727000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_TCDT_Chiphi
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;

    ;WITH hd AS (
        SELECT TOP 1
            HopDongChiTietID,
            TenSanPham,
            ChietKhau,
            SoLuong,
            DonGia,
            CASE 
                WHEN ChietKhau = 100 THEN SoLuong * DonGia
                ELSE ThanhTien
            END AS ThanhTienHD
        FROM dbo.HopDongChiTiet
        WHERE HopDongChiTietID = @HopDongChiTietID
          AND DeletedStatus = 0
    ),

    treo AS (
        SELECT
            tr.HopDongChiTietREF,
            SUM(
                CASE 
                    WHEN hdct.ChietKhau = 100
                        THEN tr.SoLuongThucTreo * tr.DonGia
                    ELSE tr.SoLuongThucTreo * tr.DonGia * (100 - hdct.ChietKhau) / 100.0
                END
            ) AS Thanhtien_Treo
        FROM dbo.ThucChayHopDongChiTiet tr
        INNER JOIN dbo.HopDongChiTiet hdct
            ON tr.HopDongChiTietREF = hdct.HopDongChiTietID
        WHERE tr.HopDongChiTietREF = @HopDongChiTietID
          AND tr.DeletedStatus = 0
          AND hdct.DeletedStatus = 0
        GROUP BY tr.HopDongChiTietREF
    ),

    tc AS (
        SELECT
            tcdt.HopDongChiTietREF,
            SUM(
                CASE 
                    WHEN hdct.ChietKhau = 100
                        THEN (tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi)
                    ELSE (tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)
                END
            ) AS ThanhtienTC
        FROM dbo.ThucChayDaTinh tcdt
        INNER JOIN dbo.HopDongChiTiet hdct
            ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
        WHERE hdct.HopDongChiTietID = @HopDongChiTietID
          AND hdct.DeletedStatus = 0
        GROUP BY tcdt.HopDongChiTietREF
    )

    SELECT
        hd.HopDongChiTietID,
        hd.TenSanPham,
        hd.ChietKhau,

        dbo.FormatNumber(hd.ThanhTienHD)                    AS ThanhtienHD,
        dbo.FormatNumber(COALESCE(treo.Thanhtien_Treo,0))   AS Thanhtien_Treo,
        dbo.FormatNumber(COALESCE(tc.ThanhtienTC,0))        AS ThanhtienTC,

        (
            CASE
                WHEN COALESCE(tc.ThanhtienTC,0) = COALESCE(hd.ThanhTienHD,0)
                    THEN N'HĐ: Đủ tiền'
                WHEN COALESCE(tc.ThanhtienTC,0) < COALESCE(hd.ThanhTienHD,0)
                    THEN N'HĐ: Thiếu '
                         + dbo.FormatNumber(COALESCE(hd.ThanhTienHD,0) - COALESCE(tc.ThanhtienTC,0))
                ELSE N'HĐ: Vượt '
                     + dbo.FormatNumber(COALESCE(tc.ThanhtienTC,0) - COALESCE(hd.ThanhTienHD,0))
            END
            + N' | ' +
            CASE
                WHEN COALESCE(treo.Thanhtien_Treo,0) = COALESCE(tc.ThanhtienTC,0)
                    THEN N'Treo: Đủ tiền'
                WHEN COALESCE(treo.Thanhtien_Treo,0) > COALESCE(tc.ThanhtienTC,0)
                    THEN N'Treo: Vượt '
                         + dbo.FormatNumber(COALESCE(treo.Thanhtien_Treo,0) - COALESCE(tc.ThanhtienTC,0))
                ELSE N'Treo: Thiếu '
                     + dbo.FormatNumber(COALESCE(tc.ThanhtienTC,0) - COALESCE(treo.Thanhtien_Treo,0))
            END
        ) AS GhiChu

    FROM hd
    LEFT JOIN treo ON treo.HopDongChiTietREF = hd.HopDongChiTietID
    LEFT JOIN tc   ON tc.HopDongChiTietREF   = hd.HopDongChiTietID;

END

```
