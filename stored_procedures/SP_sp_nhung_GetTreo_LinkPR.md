# Stored Procedure: `sp_nhung_GetTreo_LinkPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-24 15:16:41.060000
- **Ngày sửa cuối**: 2026-03-24 15:16:41.060000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Link` | `nvarchar` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_nhung_GetTreo_LinkPR
    @Link NVARCHAR(MAX)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT 
        dbo.GetSoHopDongByID(HopDongREF) AS Sohopdong,
        HopDongREF,
        HopDongChiTietREF,
        ThucChayHopDongChiTietPRID AS IDTreo,
        DmSanPhamREF,
        NhanHang,
        SoLuong,
        dbo.FormatNumber(GiaTien) AS DonGia,
        ChietKhau,
        dbo.FormatNumber(
            CASE 
                WHEN ChietKhau = 100 
                    THEN SoLuong * GiaTien 
                ELSE SoLuong * GiaTien * (100 - ChietKhau) / 100 
            END
        ) AS Thanhtien,
        Link,
        parent_id,
        RecordStatus,
        DeletedStatus,
        CreatedAt,
        CreatedBy,
        LastModifiedAt,
        LastModifiedBy
    FROM dbo.ThucChayHopDongChiTietPR
    WHERE Link LIKE @Link;
END;

```
