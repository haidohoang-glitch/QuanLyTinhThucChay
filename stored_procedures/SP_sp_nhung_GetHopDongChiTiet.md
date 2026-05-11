# Stored Procedure: `sp_nhung_GetHopDongChiTiet`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-24 14:11:29.913000
- **Ngày sửa cuối**: 2026-03-24 15:10:12.047000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_nhung_GetHopDongChiTiet
    @HopDongChiTietID int
AS
BEGIN
    SET NOCOUNT ON;

 SELECT hd.SoHopDong
	,hd.HopDongID
	,hdct.HopDongChiTietID
	,hdct.TenSanPham
	,hdct.TenLoai
	,dbo.FormatNumber(hdct.SoLuong) SoLuong
	,hdct.DonViTinh
	,dbo.FormatNumber(hdct.DonGia) DonGia
	,hdct.ChietKhau
	,dbo.FormatNumber(hdct.ThanhTien) ThanhtienHĐ
	,hdct.TenLoaiNenTang
	,hd.NhanHopDong
	,hdct.NhanHang
	,hd.DmNhanGocREF
	,dbo.FormatNumber(hd.GiaTriHopDong) GiaTriHopDong
	,hdct.CreatedAt
	,hdct.CreatedBy
	,hdct.LastModifiedAt
	,hdct.LastModifiedBy
	FROM dbo.HopDongChiTiet hdct
	INNER JOIN dbo.HopDong hd
	ON hd.HopDongID = hdct.HopDongFK
	WHERE hdct.HopDongChiTietID= @HopDongChiTietID
	AND hdct.DeletedStatus = 0
end

```
