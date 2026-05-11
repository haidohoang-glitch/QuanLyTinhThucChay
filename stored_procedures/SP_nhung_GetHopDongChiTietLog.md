# Stored Procedure: `nhung_GetHopDongChiTietLog`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 11:20:45.913000
- **Ngày sửa cuối**: 2026-03-05 11:26:54.993000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_GetHopDongChiTietLog
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;    
    
	SELECT
		HopDongChiTietLogID,
		HopDongFK,
		HopDongChiTietREF,
		DmSanPhamREF,
		TenSanPham,
		DanhSachNhanHangREF,
		NhanHang,
		TenLoai,
		DmBannerREF,
		SoLuong,
		DonGia,
		ChietKhau,
		GiamGia,
		ThanhTien,
		CreatedAt,
		CreatedBy,
		LastModifiedAt,
		LastModifiedBy
		GhiChu
		FROM dbo.HopDongChiTietLog 
		WHERE HopDongChiTietREF = @HopDongChiTietID
		ORDER BY LastModifiedAt desc

END

```
