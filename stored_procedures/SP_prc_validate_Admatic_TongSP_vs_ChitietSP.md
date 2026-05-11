# Stored Procedure: `prc_validate_Admatic_TongSP_vs_ChitietSP`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-11 17:02:21.223000
- **Ngày sửa cuối**: 2026-03-11 17:02:21.223000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `date(3)` | No |

## Definition (Source Code)

```sql

CREATE  PROCEDURE dbo.prc_validate_Admatic_TongSP_vs_ChitietSP
(
    @NgayThucHien DATE
)
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @StartDate DATE = DATEADD(DAY,-1,@NgayThucHien)
    DECLARE @EndDate   DATE = DATEADD(DAY,1,@StartDate)

    IF EXISTS ( 
        SELECT 1
        FROM ThucChay_Total_Admatic A
        WHERE 
            A.NgayThucHien >= @StartDate
            AND A.NgayThucHien <  @EndDate
    )
    BEGIN
        ;WITH A AS
        (
            SELECT 
                DmSanPhamREF,
                TenSanPham,
                SUM(CONVERT(FLOAT, domain_tt_view))      AS domain_tt_view,
                SUM(CONVERT(FLOAT, domain_tt_click))     AS domain_tt_click,
                SUM(CONVERT(FLOAT, domain_tt_money))     AS domain_tt_money,
                SUM(CONVERT(FLOAT, domain_tt_promotion)) AS domain_tt_promotion
            FROM ThucChay_Total_Admatic
            WHERE 
                NgayThucHien >= @StartDate
                AND NgayThucHien <  @EndDate
            GROUP BY DmSanPhamREF, TenSanPham
        ),

        B AS
        (
            SELECT 
                DmSanPhamREF,
                SUM(CONVERT(FLOAT, domain_tt_view))      AS View_ASD,
                SUM(CONVERT(FLOAT, domain_tt_click))     AS Click_ASD,
                SUM(CONVERT(FLOAT, domain_tt_money))     AS Tien_ASD,
                SUM(CONVERT(FLOAT, domain_tt_promotion)) AS TienKM_ASD
            FROM DataThucChay_Admatic_v2
            WHERE 
                NgayThucHien >= @StartDate
                AND NgayThucHien <  @EndDate
            GROUP BY DmSanPhamREF
        )

        SELECT 
            N'Admatic TổngSP và Chi tiếtSP' AS Admatic,
            A.DmSanPhamREF,
            A.TenSanPham,

            CONCAT(
                CASE 
                    WHEN ROUND(ISNULL(A.domain_tt_view,0),0) = ROUND(ISNULL(B.View_ASD,0),0) THEN N'✅ '
                    ELSE N'❌ '
                END,
                FORMAT(ROUND(ISNULL(A.domain_tt_view,0),0),'N0'),
                N' / ',
                FORMAT(ROUND(ISNULL(B.View_ASD,0),0),'N0')
            ) AS [View (SP/ASD)],

            CONCAT(
                CASE 
                    WHEN ROUND(ISNULL(A.domain_tt_click,0),0) = ROUND(ISNULL(B.Click_ASD,0),0) THEN N'✅ '
                    ELSE N'❌ '
                END,
                FORMAT(ROUND(ISNULL(A.domain_tt_click,0),0),'N0'),
                N' / ',
                FORMAT(ROUND(ISNULL(B.Click_ASD,0),0),'N0')
            ) AS [Click (SP/ASD)],

            CONCAT(
                CASE 
                    WHEN ABS(ROUND(ISNULL(A.domain_tt_money,0) - ISNULL(B.Tien_ASD,0),0)) <= 1000 THEN N'✅ '
                    ELSE N'❌ '
                END,
                dbo.FormatNumber(ROUND(ISNULL(A.domain_tt_money,0),0)),
                N' / ',
                dbo.FormatNumber(ROUND(ISNULL(B.Tien_ASD,0),0))
            ) AS [Tien (SP/ASD)],

            CONCAT(
                CASE 
                    WHEN ABS(ROUND(ISNULL(A.domain_tt_promotion,0) - ISNULL(B.TienKM_ASD,0),0)) <= 1000 THEN N'✅ '
                    ELSE N'❌ '
                END,
                dbo.FormatNumber(ROUND(ISNULL(A.domain_tt_promotion,0),0)),
                N' / ',
                dbo.FormatNumber(ROUND(ISNULL(B.TienKM_ASD,0),0))
            ) AS [TienKM (SP/ASD)],

            CASE 
                WHEN 
                    ROUND(ISNULL(A.domain_tt_view,0),0)   = ROUND(ISNULL(B.View_ASD,0),0)
                AND ROUND(ISNULL(A.domain_tt_click,0),0)  = ROUND(ISNULL(B.Click_ASD,0),0)
                AND ABS(ROUND(ISNULL(A.domain_tt_money,0) - ISNULL(B.Tien_ASD,0),0)) <= 1000
                AND ABS(ROUND(ISNULL(A.domain_tt_promotion,0) - ISNULL(B.TienKM_ASD,0),0)) <= 1000
                    THEN N'✅ Khớp'
                ELSE CONCAT(
                    N'❌ Lệch: ',
                    LEFT(
                        CONCAT(
                            CASE WHEN ROUND(ISNULL(A.domain_tt_view,0),0) <> ROUND(ISNULL(B.View_ASD,0),0) THEN N'View, ' ELSE N'' END,
                            CASE WHEN ROUND(ISNULL(A.domain_tt_click,0),0) <> ROUND(ISNULL(B.Click_ASD,0),0) THEN N'Click, ' ELSE N'' END,
                            CASE WHEN ABS(ROUND(ISNULL(A.domain_tt_money,0) - ISNULL(B.Tien_ASD,0),0)) > 1000 THEN N'Tiền, ' ELSE N'' END,
                            CASE WHEN ABS(ROUND(ISNULL(A.domain_tt_promotion,0) - ISNULL(B.TienKM_ASD,0),0)) > 1000 THEN N'KM, ' ELSE N'' END
                        ),
                        LEN(
                            CONCAT(
                                CASE WHEN ROUND(ISNULL(A.domain_tt_view,0),0) <> ROUND(ISNULL(B.View_ASD,0),0) THEN N'View, ' ELSE N'' END,
                                CASE WHEN ROUND(ISNULL(A.domain_tt_click,0),0) <> ROUND(ISNULL(B.Click_ASD,0),0) THEN N'Click, ' ELSE N'' END,
                                CASE WHEN ABS(ROUND(ISNULL(A.domain_tt_money,0) - ISNULL(B.Tien_ASD,0),0)) > 1000 THEN N'Tiền, ' ELSE N'' END,
                                CASE WHEN ABS(ROUND(ISNULL(A.domain_tt_promotion,0) - ISNULL(B.TienKM_ASD,0),0)) > 1000 THEN N'KM, ' ELSE N'' END
                            )
                        ) - 2
                    )
                )
            END AS TrangThai

        FROM A
        LEFT JOIN B ON A.DmSanPhamREF = B.DmSanPhamREF
        ORDER BY A.DmSanPhamREF;

    END
    ELSE
    BEGIN
        SELECT N'❌ Không có dữ liệu thực chạy cho ngày đã truyền' AS CanhBao;
    END
END

```
