# Stored Procedure: `nhung_GetHopDongChiTietByID`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 10:56:26.340000
- **Ngày sửa cuối**: 2026-03-05 10:56:26.340000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_GetHopDongChiTietByID
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT 
        HopDongFK,
        HopDongChiTietID,
        DmSanPhamREF,
        TenSanPham,
        TenLoai,
        SoLuong,
        DonViTinh,
        dbo.FormatNumber(DonGia) AS DonGia,
        ChietKhau,
        dbo.FormatNumber(ThanhTien) AS ThanhTien,
        DeletedStatus,
        DmLoaiREF,
        DmLoaiNenTangREF,
        DanhSachNhanHangREF,
        NhanHang,
        CreatedAt,
        LastModifiedAt
    FROM dbo.HopDongChiTiet
    WHERE HopDongChiTietID = @HopDongChiTietID;
END

```
