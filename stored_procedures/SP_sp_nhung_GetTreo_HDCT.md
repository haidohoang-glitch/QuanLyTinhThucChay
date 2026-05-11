# Stored Procedure: `sp_nhung_GetTreo_HDCT`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-24 15:13:25.297000
- **Ngày sửa cuối**: 2026-03-24 15:13:25.297000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_nhung_GetTreo_HDCT
    @HopDongChiTietID int
AS
BEGIN
    SET NOCOUNT ON;
	SELECT dbo.GetSoHopDongByID(HopDongREF) Sohopdong
	,ThucChayHopDongChiTietID AS IDtreo
	,HopDongREF
	,HopDongChiTietREF
	,DmSanPhamREF
	,TenHinhThucQuangCao
	,BookingREF
	,DmBannerREF
	,SoLuongThucTreo
	,DonViTinh
	,dbo.FormatNumber(DonGia) AS DonGia
	,ChietKhau
	,dbo.FormatNumber(ThanhTien) AS Thanhtien
	,DeletedStatus
	,RecordStatus
	,LoaiThucTreo
	,CreatedAt
	,CreatedBy
	,LastModifiedAt
	,LastModifiedBy
	FROM dbo.ThucChayHopDongChiTiet
	WHERE HopDongChiTietREF = @HopDongChiTietID
	ORDER BY DmBannerREF DESC
END;

```
