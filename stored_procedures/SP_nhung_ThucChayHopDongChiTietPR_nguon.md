# Stored Procedure: `nhung_ThucChayHopDongChiTietPR_nguon`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 14:32:04.270000
- **Ngày sửa cuối**: 2026-03-05 14:32:04.270000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_ThucChayHopDongChiTietPR_nguon
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;

    ;WITH DATA AS 
    (
        SELECT
            id AS ID_treo,
            Contract_Id,
            Contract_Detail_Id,
            Product_Id,
            NhanHang_Id,
            TenNhanHang,
            SoLuong,
            DonGia,
            ChietKhau,

            -- dùng ThanhTien có sẵn
            CAST(ThanhTien AS FLOAT) AS ThanhTien,

            Ten_Website,
            Link,
            Parent_id,
            TenChuyenMuc,
            Created_At,
            Created_By,
            Last_Modified_At,
            Last_Modified_By,
            ViTri

        FROM ASDAG2.ThucTreo.dbo.ThucTreo_PR
        WHERE Deleted_Status = 0
        AND Contract_Detail_Id = @HopDongChiTietID
    ),

    FINAL AS
    (
        -- Chi tiết
        SELECT
            0 AS SortKey,
            ID_treo,
            Contract_Id,
            Contract_Detail_Id,
            Product_Id,
            NhanHang_Id,
            TenNhanHang,
            SoLuong,
            DonGia,
            ChietKhau,
            ThanhTien,
            Ten_Website,
            Link,
            Parent_id,
            TenChuyenMuc,
            Created_At,
            Created_By,
            Last_Modified_At,
            Last_Modified_By,
            ViTri
        FROM DATA

        UNION ALL

        -- Tổng
        SELECT
            1,
            NULL,
            NULL,
            NULL,
            NULL,
            NULL,
            N'TỔNG',
            NULL,
            NULL,
            NULL,
            SUM(ThanhTien),
            NULL,
            NULL,
            NULL,
            NULL,
            NULL,
            NULL,
            NULL,
            NULL,
            NULL
        FROM DATA
    )

    SELECT
        ID_treo,
        Contract_Id,
        Contract_Detail_Id,
        Product_Id,
        NhanHang_Id,
        TenNhanHang,
        SoLuong,
        DonGia,
        ChietKhau,
        dbo.FormatNumber(ThanhTien) AS ThanhTien,
        Ten_Website,
        Link,
        Parent_id,
        TenChuyenMuc,
        Created_At,
        Created_By,
        Last_Modified_At,
        Last_Modified_By,
        ViTri
    FROM FINAL
    ORDER BY SortKey, ID_treo DESC;

END

```
