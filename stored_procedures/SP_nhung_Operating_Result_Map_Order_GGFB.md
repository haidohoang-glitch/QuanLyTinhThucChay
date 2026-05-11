# Stored Procedure: `nhung_Operating_Result_Map_Order_GGFB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 17:04:54.953000
- **Ngày sửa cuối**: 2026-03-06 17:04:54.953000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE nhung_Operating_Result_Map_Order_GGFB
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

;WITH DATA AS (
    SELECT  
        Id,
        Operating_Order_Id,
        operating_Result_Id,
        Result,
        Sell_Money_VND,
        CreationTime,
        LastModificationTime,
        IsDeleted
    FROM [asdag2].ADS.dbo.Operating_Result_Map_Order
    WHERE Operating_Order_Id IN (
        SELECT id
        FROM [asdag2].ADS.dbo.Operating_Order
        WHERE Contract_Detail_Id = @HopDongChiTietID
          AND IsDeleted = 0
    )
      AND IsDeleted = 0
),
FINAL AS (
    -- Chi tiết
    SELECT
        0 AS SortKey,
        CAST(NULL AS NVARCHAR(20)) AS GhiChu,
        Id,
        Operating_Order_Id,
        operating_Result_Id,
        Result,
        Sell_Money_VND,
        CreationTime,
        LastModificationTime,
        IsDeleted
    FROM DATA

    UNION ALL

    -- Tổng
    SELECT
        1 AS SortKey,
        N'TỔNG' AS GhiChu,              -- ✅ hiện chữ TỔNG ở cột riêng
        NULL AS Id,
        NULL AS Operating_Order_Id,
        NULL AS operating_Result_Id,
        SUM(Result) AS Result,
        SUM(Sell_Money_VND) AS Sell_Money_VND,
        NULL AS CreationTime,
        NULL AS LastModificationTime,
        NULL AS IsDeleted

    FROM DATA
)
SELECT  
    GhiChu,
    Id,
    Operating_Order_Id,
    operating_Result_Id,
    dbo.FormatNumber(Result)         AS Soluong,
    dbo.FormatNumber(Sell_Money_VND) AS ThanhtienTC_Ban,
    CreationTime,
    LastModificationTime,
    IsDeleted

FROM FINAL
ORDER BY SortKey, Operating_Order_Id, Id;

END 

```
