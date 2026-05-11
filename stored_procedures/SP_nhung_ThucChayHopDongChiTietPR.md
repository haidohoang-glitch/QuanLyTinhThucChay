# Stored Procedure: `nhung_ThucChayHopDongChiTietPR`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 14:29:57.660000
- **Ngày sửa cuối**: 2026-03-05 14:29:57.660000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_ThucChayHopDongChiTietPR
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;

;WITH DATA AS
(
    SELECT
        ThucChayHopDongChiTietPRID AS ID_treo,
        HopDongREF,
        HopDongChiTietREF,
        DmSanPhamREF,
        DmNhanHangREF,
        NhanHang,
        SoLuong,
        GiaTien,
        ChietKhau,
        (SoLuong * GiaTien * (100 - ChietKhau) / 100.0) AS thanhtien,
        TenWebsite,
        Link,
        parent_id,
        RecordStatus,
        ChuyenMuc,
        CreatedAt,
        CreatedBy,
        LastModifiedAt,
        LastModifiedBy,
        TenViTri
    FROM dbo.ThucChayHopDongChiTietPR
    WHERE DeletedStatus = 0
    AND HopDongChiTietREF = @HopDongChiTietID
),

FINAL AS
(
    -- Chi tiết
    SELECT
        ID_treo,
        HopDongREF,
        HopDongChiTietREF,
        DmSanPhamREF,
        DmNhanHangREF,
        NhanHang,
        SoLuong,
        GiaTien,
        ChietKhau,
        thanhtien,
        TenWebsite,
        Link,
        parent_id,
        RecordStatus,
        ChuyenMuc,
        CreatedAt,
        CreatedBy,
        LastModifiedAt,
        LastModifiedBy,
        TenViTri
    FROM DATA

    UNION ALL

    -- Tổng
    SELECT
        NULL,
        NULL,
        NULL,
        NULL,
        NULL,
        N'TỔNG',
        NULL,
        NULL,
        NULL,
        SUM(thanhtien),
        NULL,
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
    HopDongREF,
    HopDongChiTietREF,
    DmSanPhamREF,
    DmNhanHangREF,
    NhanHang,
    SoLuong,
    dbo.FormatNumber(GiaTien) AS GiaTien,
    ChietKhau,
    dbo.FormatNumber(thanhtien) AS thanhtien,
    TenWebsite,
    Link,
    parent_id,
    RecordStatus,
    ChuyenMuc,
    CreatedAt,
    CreatedBy,
    LastModifiedAt,
    LastModifiedBy,
    TenViTri
FROM FINAL
ORDER BY 
    CASE WHEN NhanHang = N'TỔNG' THEN 1 ELSE 0 END,
    ID_treo DESC;

END

```
