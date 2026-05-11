# Stored Procedure: `nhung_ADSResult_GGFB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 17:10:46.103000
- **Ngày sửa cuối**: 2026-03-06 17:10:46.103000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE nhung_ADSResult_GGFB
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

;WITH DATA AS (
    SELECT
        Id,
        Operating_Order_Id,
        Total_Money_VND,
        Sell_Money_VND,
        Campaign_Id,
        Campaign_Name,
        RESULT,
        Reach,
        Impression,
        Clicks,
        CreationTime,
        CreatedBy,
        LastModificationTime,
        LastModifiedBy
    FROM dbo.ADS_Operating_Result
    WHERE Operating_Order_Id IN (
        SELECT id
        FROM dbo.ADS_Operating_Order
        WHERE Contract_Detail_Id = @HopDongChiTietID
          AND IsDeleted = 0
    )
),
FINAL AS (
    -- 🔹 Chi tiết
    SELECT
        0 AS SortKey,
        Id,
        Operating_Order_Id,
        Total_Money_VND,
        Sell_Money_VND,
        Campaign_Id,
        Campaign_Name,
        Result,
        Reach,
        Impression,
        Clicks,
        CreationTime,
        CreatedBy,
        LastModificationTime,
        LastModifiedBy
    FROM DATA

    UNION ALL

    -- 🔹 Dòng TỔNG
    SELECT
        1 AS SortKey,
        NULL AS Id,
        NULL AS Operating_Order_Id,
        SUM(Total_Money_VND) AS Total_Money_VND,
        SUM(Sell_Money_VND)  AS Sell_Money_VND,
        NULL AS Campaign_Id,
        N'TỔNG' AS Campaign_Name,
        SUM(Result)     AS Result,
        SUM(Reach)      AS Reach,
        SUM(Impression) AS Impression,
        SUM(Clicks)     AS Clicks,
        NULL AS CreationTime,
        NULL AS CreatedBy,
        NULL AS LastModificationTime,
        NULL AS LastModifiedBy
    FROM DATA
)

SELECT
    Id,
    Operating_Order_Id,
    dbo.FormatNumber(Total_Money_VND) AS TienMua,
    dbo.FormatNumber(Sell_Money_VND)  AS TienTC_Ban,
    Campaign_Id,
    Campaign_Name,
    dbo.FormatNumber(Result)     AS Result,
    dbo.FormatNumber(Reach)      AS Reach,
    dbo.FormatNumber(Impression) AS Impression,
    dbo.FormatNumber(Clicks)     AS Clicks,
    CreationTime,
    CreatedBy,
    LastModificationTime,
    LastModifiedBy
FROM FINAL
ORDER BY SortKey, Operating_Order_Id, Id;

END

```
