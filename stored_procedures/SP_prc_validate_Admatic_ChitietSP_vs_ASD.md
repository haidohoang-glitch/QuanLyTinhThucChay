# Stored Procedure: `prc_validate_Admatic_ChitietSP_vs_ASD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-11 16:30:24.387000
- **Ngày sửa cuối**: 2026-03-12 10:27:15.840000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `date(3)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[prc_validate_Admatic_ChitietSP_vs_ASD]
(
    @NgayThucHien DATE
)
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @StartDate DATE = DATEADD(DAY,-1,@NgayThucHien)

    IF EXISTS (
        SELECT 1
        FROM DataThucChay_Admatic_v2
        WHERE NgayThucHien = @StartDate
    )
    BEGIN
        ;WITH A AS
        (
            SELECT 
                DmSanPhamREF,
                MAX(TenSanPham) AS TenSanPham,
                ROUND(SUM(CONVERT(FLOAT, domain_tt_money) 
                     / (1 + CONVERT(FLOAT, vat) / 100.0)), 0) AS Tien_SP,
                ROUND(SUM(CONVERT(FLOAT, domain_tt_promotion) 
                     / (1 + CONVERT(FLOAT, vat) / 100.0)), 0) AS TienKM_SP
            FROM DataThucChay_Admatic_v2
            WHERE NgayThucHien = @StartDate
            GROUP BY DmSanPhamREF, vat
        ),

        A_Tong AS
        (
            SELECT 
                DmSanPhamREF,
                MAX(TenSanPham) AS TenSanPham,
                ROUND(SUM(Tien_SP),0)   AS Tien_SP,
                ROUND(SUM(TienKM_SP),0) AS TienKM_SP
            FROM A
            GROUP BY DmSanPhamREF
        ),

        B AS
        (
            SELECT 
                DmSanPhamREF,
                ROUND(SUM(ThanhTienThucChaySauCK_ChuaVAT),0) AS ThanhTien_ASD,
                ROUND(SUM(ThanhTienThucChayKM),0)            AS ThanhTienKM_ASD
            FROM dbo.ThucChay_ThanhTien_Admatic
            WHERE NgayThucHien = @StartDate
            GROUP BY DmSanPhamREF
        ),

        X AS
        (
            SELECT
                N'Admatic ChiTietSP va ChiTietASD' AS Admatic,
                A_Tong.DmSanPhamREF,
                A_Tong.TenSanPham,
                ROUND(ISNULL(A_Tong.Tien_SP,0),0)    AS TienSP_0,
                ROUND(ISNULL(B.ThanhTien_ASD,0),0)   AS TienASD_0,
                ROUND(ISNULL(A_Tong.TienKM_SP,0),0)  AS KMSP_0,
                ROUND(ISNULL(B.ThanhTienKM_ASD,0),0) AS KMASD_0
            FROM A_Tong
            LEFT JOIN B 
                ON A_Tong.DmSanPhamREF = B.DmSanPhamREF
        ),

        Y AS
        (
            SELECT
                *,
                CONCAT(
                    CASE 
                        WHEN ABS(TienASD_0 - TienSP_0) = 0 THEN N''
                        WHEN DmSanPhamREF IN (821,5133) AND TienASD_0 > TienSP_0 
                            THEN N'Bỏ qua ASD > SP do chạy cả tool Branding, '
                        ELSE N'Tiền, '
                    END,
                    CASE 
                        WHEN ABS(KMASD_0 - KMSP_0) <= 1000 THEN N''
                        ELSE N'KM, '
                    END
                ) AS LyDoLechRaw
            FROM X
        )

        SELECT
            Admatic,
            DmSanPhamREF,
            TenSanPham,

            CONCAT(
                CASE 
                    WHEN ABS(TienASD_0 - TienSP_0) = 0 THEN N'✅ '
                    WHEN DmSanPhamREF IN (821,5133) AND TienASD_0 > TienSP_0 THEN N'△ '
                    ELSE N'❌ '
                END,
                dbo.FormatNumber(TienSP_0),
                N' / ',
                dbo.FormatNumber(TienASD_0)
            ) AS [Tien (SP/ASD)],

            CONCAT(
                CASE 
                    WHEN ABS(KMASD_0 - KMSP_0) <= 1000 THEN N'✅ '
                    ELSE N'❌ '
                END,
                dbo.FormatNumber(KMSP_0),
                N' / ',
                dbo.FormatNumber(KMASD_0)
            ) AS [KM (SP/ASD)],

            CASE
                WHEN LyDoLechRaw = N'' THEN N'Khớp'
                ELSE CONCAT(
                    N'Lệch: ',
                    LEFT(LyDoLechRaw, LEN(LyDoLechRaw) - 2)
                )
            END AS TrangThai

        FROM Y
        ORDER BY DmSanPhamREF;

    END
    ELSE
    BEGIN
        SELECT N'❌ Không có dữ liệu cho ngày đã truyền' AS CanhBao;
    END
END

```
