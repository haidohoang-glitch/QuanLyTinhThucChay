# Stored Procedure: `sp_nhung_KT_hamtinh_PerformanceMKT`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-27 14:25:26.647000
- **Ngày sửa cuối**: 2026-03-31 10:56:13.010000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `date(3)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[sp_nhung_KT_hamtinh_PerformanceMKT]
(
    @NgayBatDau DATE
)
AS
BEGIN
    SET NOCOUNT ON;

    ;WITH DATA AS
    (
        SELECT 
            A.SoHopDong,
            A.HopDongChiTietREF,
            A.NgayThucHien,
            A.TongThucchay_SP,
            ISNULL(B.TongThucchay_ASD,0) AS TongThucchay_ASD,
            A.TongThucchay_SP - ISNULL(B.TongThucchay_ASD,0) AS ChenhLech

        FROM (
            SELECT 
                SoHopDong,
                HopDongChiTietREF,
                CONVERT(DATE, NgayThucHien) AS NgayThucHien,
                SUM(TongThucchay_SP) AS TongThucchay_SP
            FROM (
                SELECT 
                    CASE 
                        WHEN contract = '' OR contract = 'Blank' THEN N'KHÔNG XÁC ĐỊNH'
                        ELSE contract
                    END AS SoHopDong,
                    phanbo AS HopDongChiTietREF,
                    NgayThucHien,
                    SUM(CONVERT(FLOAT, balance)) AS TongThucchay_SP
                FROM dbo.ThucChayMarketingFee_PerformanceBaseFinal 
                WHERE NgayThucHien >= @NgayBatDau
                    AND DmSanPhamREF = 817
                GROUP BY 
                    CASE 
                        WHEN contract = '' OR contract = 'Blank' THEN N'KHÔNG XÁC ĐỊNH'
                        ELSE contract
                    END,
                    phanbo,
                    NgayThucHien

                UNION ALL

                SELECT 
                    SoHopDong,
                    HopDongChiTietREF,
                    CreatedAt,
                    SUM(SoTienThayDoi)
                FROM dbo.ThucChay_PerformanceBase_ThayDoi 
                WHERE CreatedAt >= @NgayBatDau
                    AND DmSanPhamREF = 817
                GROUP BY SoHopDong, HopDongChiTietREF, CreatedAt
            ) t
            GROUP BY SoHopDong, HopDongChiTietREF, CONVERT(DATE, NgayThucHien)
        ) A

        LEFT JOIN (
            SELECT 
                SoHopDong,
                HopDongChiTietREF,
                CONVERT(DATE, NgayThucHien) AS NgayThucHien,
                SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS TongThucchay_ASD
            FROM dbo.ThucChayDaTinh
            WHERE NgayThucHien >= @NgayBatDau
                AND DmSanPhamREF = 817
                AND DmHinhThucQuangCao <> 42
                AND NOT (SoHopDong = 'Blank' OR SoHopDong = '' OR HopDongChiTietREF = 0)
            GROUP BY SoHopDong, HopDongChiTietREF, CONVERT(DATE, NgayThucHien)
        ) B
            ON A.HopDongChiTietREF = B.HopDongChiTietREF
            AND A.NgayThucHien = B.NgayThucHien
    )

    -- ✅ Ẩn SortOrder bằng subquery
    SELECT 
        SoHopDong,
        HopDongChiTietREF,
        dbo.FormatNumber(TongThucchay_SP) AS TongThucchay_SP,
        dbo.FormatNumber(TongThucchay_ASD)  AS TongThucchay_ASD,
        dbo.FormatNumber(ChenhLech) AS ChenhLech
    FROM
    (
        SELECT 
            SoHopDong,
            HopDongChiTietREF,
            TongThucchay_SP,
            TongThucchay_ASD,
            ChenhLech,
            0 AS SortOrder
        FROM DATA
		where ChenhLech <> 0

        UNION ALL

        SELECT 
            N'TỔNG',
            NULL,
            SUM(TongThucchay_SP),
            SUM(TongThucchay_ASD),
            SUM(ChenhLech),
            1 AS SortOrder
        FROM DATA
    ) X

    ORDER BY SortOrder
        

END

```
