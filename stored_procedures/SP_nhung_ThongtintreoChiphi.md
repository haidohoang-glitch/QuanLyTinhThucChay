# Stored Procedure: `nhung_ThongtintreoChiphi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 15:03:09.940000
- **Ngày sửa cuối**: 2026-03-06 15:03:09.940000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_ThongtintreoChiphi
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;

SELECT 
    ThucChayHopDongChiTietID,
    HopDongREF,
    HopDongChiTietREF,
    DmSanPhamREF,
    TenSanPham,
    DmNhanHangREF,
    NhanHang,
    SoLuongThucTreo,
    dbo.FormatNumber(DonGia)      AS DonGia,
    ChietKhau,
    dbo.FormatNumber(ThanhTien)  AS ThanhTien,
    DeletedStatus,
	CASE WHEN RecordStatus = 1 THEN N'1.Đã tính' ELSE N'0.Chưa tính' END   RecordStatus,
    LoaiThucTreo,
    CreatedAt,
    CreatedBy,
    LastModifiedAt,
    LastModifiedBy,
    Id
FROM dbo.ThucChayHopDongChiTiet
WHERE HopDongChiTietREF = @HopDongChiTietID
  AND DeletedStatus = 0

UNION ALL

SELECT
    NULL,
    NULL,
    NULL,                     -- ❌ bỏ HopDongChiTietREF
    NULL,
    N'TỔNG',
    NULL,
    NULL,
    SUM(SoLuongThucTreo),
    NULL,
    NULL,
    dbo.FormatNumber(SUM(ThanhTien)),
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL
FROM dbo.ThucChayHopDongChiTiet
WHERE HopDongChiTietREF = @HopDongChiTietID
  AND DeletedStatus = 0;

END 

```
