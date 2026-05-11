# Stored Procedure: `nhung_TCDTDotChayBooking`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 15:47:39.310000
- **Ngày sửa cuối**: 2026-03-06 16:33:12.233000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[nhung_TCDTChiphi_TheoTreo]
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;
SELECT
    tcdt.HopDongChiTietREF,
    LTRIM(RTRIM(
        CASE 
            WHEN CHARINDEX(':', DotChayBooking) > 0 
                THEN LEFT(DotChayBooking, CHARINDEX(':', DotChayBooking) - 1)
            ELSE DotChayBooking
        END
    )) AS DotChayBooking,
    dbo.FormatNumber(
        SUM(
            CASE 
                WHEN hdct.ChietKhau = 100
                    THEN (tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi)
                ELSE (tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)
            END
        )
    ) AS ThanhtienTC
FROM dbo.ThucChayDaTinh tcdt
INNER JOIN dbo.HopDongChiTiet hdct
    ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
WHERE hdct.HopDongChiTietID = @HopDongChiTietID
  AND hdct.DeletedStatus = 0
GROUP BY
    tcdt.HopDongChiTietREF,
    tcdt.DotChayBooking

UNION ALL

SELECT
    NULL AS HopDongChiTietREF,        -- ✅ bỏ cột gây lỗi
    N'TỔNG' AS DotChayBooking,
    dbo.FormatNumber(
        SUM(
            CASE 
                WHEN hdct.ChietKhau = 100
                    THEN (tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi)
                ELSE (tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)
            END
        )
    ) AS ThanhtienTC
FROM dbo.ThucChayDaTinh tcdt
INNER JOIN dbo.HopDongChiTiet hdct
    ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID
WHERE hdct.HopDongChiTietID = @HopDongChiTietID
  AND hdct.DeletedStatus = 0;
END 

```
