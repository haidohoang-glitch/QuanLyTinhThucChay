# Stored Procedure: `nhung_Thongtinlaichenhlechmuaban_GGFB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 17:06:11.050000
- **Ngày sửa cuối**: 2026-03-06 17:06:11.050000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE nhung_Thongtinlaichenhlechmuaban_GGFB
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

;WITH DATA AS (
    SELECT
        OD.Contract_Number,
        OD.Contract_Id,
        OD.Contract_Detail_Id,
        OD.Id AS Operating_Order_Id,
        OD.D_Units_Id AS Donvitinh,
        OD.Product_Id AS Sanpham,
        OD.Brand_id AS NhanHang,

        TC.Id,
        TC.operating_Result_Id,

        CAST(TC.Result AS FLOAT) AS Soluong,
        CAST(TC.Sell_Money_VND AS FLOAT) AS TienTC_Ban,
        CAST(TCC.Total_Money_VND AS FLOAT) AS Tien_mua,
        CAST(TC.Sell_Money_VND AS FLOAT) - CAST(TCC.Total_Money_VND AS FLOAT) AS LAI_CHENHLECH
    FROM [asdag2].ADS.dbo.Operating_Result_Map_Order TC
    INNER JOIN [asdag2].ADS.dbo.Operating_Order OD
        ON TC.Operating_Order_Id = OD.Id
    INNER JOIN [asdag2].ADS.dbo.Operating_Result TCC
        ON TC.operating_Result_Id = TCC.ID
    WHERE OD.Contract_Detail_Id = @HopDongChiTietID
),
FINAL AS (
    -- 🔹 Chi tiết
    SELECT
        0 AS SortKey,
        Contract_Number,
        Contract_Id,
        Contract_Detail_Id,
        Operating_Order_Id,
        Donvitinh,
        Sanpham,
        NhanHang,
        Id,
        operating_Result_Id,
        Soluong,
        TienTC_Ban,
        Tien_mua,
        LAI_CHENHLECH
    FROM DATA

    UNION ALL

    -- 🔹 Dòng TỔNG
    SELECT
        1 AS SortKey,
        NULL AS Contract_Number,
        NULL AS Contract_Id,
        NULL AS Contract_Detail_Id,
        NULL AS Operating_Order_Id,
        NULL AS Donvitinh,
        NULL AS Sanpham,
        NULL AS NhanHang,
        NULL AS Id,
        NULL AS operating_Result_Id,
        SUM(Soluong) AS Soluong,
        SUM(TienTC_Ban) AS TienTC_Ban,
        SUM(Tien_mua) AS Tien_mua,
        SUM(LAI_CHENHLECH) AS LAI_CHENHLECH
    FROM DATA
)

SELECT
    Contract_Number,
    Contract_Id,
    Contract_Detail_Id,
    Operating_Order_Id,
    Donvitinh,
    Sanpham,
    NhanHang,
    Id,
    operating_Result_Id,
    dbo.FormatNumber(Soluong) AS Soluong,
    dbo.FormatNumber(TienTC_Ban) AS TienTC_Ban,
    dbo.FormatNumber(Tien_mua) AS Tien_mua,
    dbo.FormatNumber(LAI_CHENHLECH) AS LAI_CHENHLECH
FROM FINAL
ORDER BY SortKey, Operating_Order_Id, Id;

END 

```
