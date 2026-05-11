# Stored Procedure: `nhung_TCDT_IDMapDotchayBooking_GGFB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 17:29:44.383000
- **Ngày sửa cuối**: 2026-03-06 17:29:44.383000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[nhung_TCDT_IDMapDotchayBooking_GGFB]
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

;WITH A AS (
    SELECT
        TC.Id,
        OD.Id AS Operating_Order_Id,
        TC.operating_Result_Id,
        OD.Brand_id,
        CAST(TC.Result AS FLOAT) AS soluong,
        CAST(TC.Sell_Money_VND AS FLOAT) AS TienTC_Ban,
        CAST(TCC.Total_Money_VND AS FLOAT) AS TienMua,
        CAST(TC.Sell_Money_VND AS FLOAT) - CAST(TCC.Total_Money_VND AS FLOAT) AS Lai
    FROM dbo.ADS_Operating_Result_Map_Order TC
    INNER JOIN dbo.ADS_Operating_Order OD
        ON TC.Operating_Order_Id = OD.Id
    INNER JOIN dbo.ADS_Operating_Result TCC
        ON TC.operating_Result_Id = TCC.ID
    WHERE OD.Contract_Detail_Id = @HopDongChiTietID
      AND OD.IsDeleted = 0
      AND TCC.IsDeleted = 0
),
B AS (
    SELECT
        TRY_CAST(
            LTRIM(RTRIM(LEFT(DotChayBooking, CHARINDEX(':', DotChayBooking + ':') - 1)))
            AS INT
        ) AS DotChayBooking,
        SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS ThanhtienTC
    FROM dbo.ThucChayDaTinh
    WHERE HopDongChiTietREF = @HopDongChiTietID
    GROUP BY TRY_CAST(
        LTRIM(RTRIM(LEFT(DotChayBooking, CHARINDEX(':', DotChayBooking + ':') - 1)))
        AS INT
    )
),
DATA AS (
    SELECT
        A.Id,
		B.DotChayBooking,
        A.Operating_Order_Id,
        A.operating_Result_Id,
        A.Brand_id,
        A.soluong,
        A.TienTC_Ban,
        A.TienMua,
        A.Lai,
        B.ThanhtienTC,
        CASE
            WHEN ROUND(ISNULL(A.TienTC_Ban,0),0) > ROUND(ISNULL(B.ThanhtienTC,0),0)
                THEN CONCAT(
                        N'Thiếu ghi nhận: ',
                        dbo.FormatNumber(
                            ROUND(ISNULL(A.TienTC_Ban,0),0)
                          - ROUND(ISNULL(B.ThanhtienTC,0),0)
                        )
                     )
            WHEN ROUND(ISNULL(A.TienTC_Ban,0),0) < ROUND(ISNULL(B.ThanhtienTC,0),0)
                THEN CONCAT(
                        N'Thừa ghi nhận: ',
                        dbo.FormatNumber(
                            ROUND(ISNULL(B.ThanhtienTC,0),0)
                          - ROUND(ISNULL(A.TienTC_Ban,0),0)
                        )
                     )
            WHEN ROUND(ISNULL(A.TienTC_Ban,0),0) = ROUND(ISNULL(B.ThanhtienTC,0),0)
                THEN N'Ghi nhận đủ'
            ELSE N''
        END AS GhiChu_TCDT
    FROM A
    LEFT JOIN B ON A.Id = B.DotChayBooking
),
FINAL AS (
    -- 🔹 Chi tiết
    SELECT
        0 AS SortKey,
        Id,
		DATA.DotChayBooking,
        Operating_Order_Id,
        operating_Result_Id,
        Brand_id,
        soluong,
        TienTC_Ban,
        TienMua,
        Lai,
        ThanhtienTC,
        GhiChu_TCDT
    FROM DATA

    UNION ALL

    -- 🔹 Dòng TỔNG
    SELECT
        1 AS SortKey,
        NULL AS Id,
		NULL AS DotChayBooking,
        NULL AS Operating_Order_Id,
        NULL AS operating_Result_Id,
        NULL AS Brand_id,
        SUM(soluong) AS soluong,
        SUM(TienTC_Ban) AS TienTC_Ban,
        SUM(TienMua) AS TienMua,
        SUM(Lai) AS Lai,
        SUM(ThanhtienTC) AS ThanhtienTC,
        N'TỔNG' AS GhiChu_TCDT
    FROM DATA
)

SELECT
    Id,
	DotChayBooking,
    Operating_Order_Id,
    operating_Result_Id,
    Brand_id,
    dbo.FormatNumber(soluong) AS soluong,
    dbo.FormatNumber(TienTC_Ban) AS TienTC_Ban,
    dbo.FormatNumber(TienMua) AS TienMua,
    dbo.FormatNumber(Lai) AS Lai,
    dbo.FormatNumber(ThanhtienTC) AS ThanhtienTC,
    GhiChu_TCDT
FROM FINAL
ORDER BY SortKey, Id DESC;

END 

```
