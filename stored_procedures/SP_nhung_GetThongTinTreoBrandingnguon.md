# Stored Procedure: `nhung_GetThongTinTreoBrandingnguon`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 11:48:25.810000
- **Ngày sửa cuối**: 2026-03-05 11:48:25.810000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_GetThongTinTreoBrandingnguon
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        -- 🔑 Khóa / Hợp đồng
        Id,
        Contract_Number,
        Contract_Id,
        Contract_Detail_Id,

        -- 📦 Sản phẩm / Hình thức / Banner
        Product_Id,
        Product_Formality_Id,
        Banner_Id,
        CASE 
            WHEN DonViTinh_Id = 1 THEN N'Views'
            ELSE N'Click'
        END AS DonViTinh,

        -- 📊 Số lượng & Giá
        SoLuong,
        dbo.FormatNumber(DonGia) AS DonGia,
        ChietKhau,
        ThanhTien,

        -- 🔗 Link
        Link,

        -- 🕒 Trạng thái & Audit
        Deleted_Status,
        Created_At,
        Created_By,
        Last_Modified_At,
        Last_Modified_By

    FROM ASDAG2.ThucTreo.dbo.ThucTreo
    WHERE Contract_Detail_Id = @HopDongChiTietID
      AND Deleted_Status = 0;

END

```
