# Stored Procedure: `nhung_GetHopDongChiTietnguon`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 11:40:55.043000
- **Ngày sửa cuối**: 2026-03-05 11:40:55.043000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_GetHopDongChiTietnguon
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT CONTRACT_ID AS HopDongFK,
		ID AS HopDongChiTietID,
		PRODUCT_ID AS DmSanPhamREF,
		dbo.FormatNumber(QUANTITY) AS soluong,
		PRODUCT_UNIT_ID AS DonViTinh,
		dbo.FormatNumber(PRICE) AS dongia,
		dbo.FormatNumber(PERCENT_DISCOUNT) AS chietkhau, 
		dbo.FormatNumber(MONEY_TURNOVER) AS thanhtien,
		dbo.FormatNumber(MONEY_DISCOUNT_TOTAL) AS giamgia,
		dbo.FormatNumber(vat) vat,
		dbo.FormatNumber(MONEY_REAL_RUNING) Thanhtien_TC,
		BANNER_ID,
		CREATED_AT,
		CREATED_BY,
		LAST_MODIFIED_AT,
		LAST_MODIFIED_BY
	FROM ASDAG2.CONTRACT.dbo.CONTRACT_DETAILS 
	WHERE ID =  @HopDongChiTietID;

END

```
