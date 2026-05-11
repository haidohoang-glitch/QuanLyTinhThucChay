# Stored Procedure: `sp_nhung_GetTreo_SHD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-24 15:19:31.920000
- **Ngày sửa cuối**: 2026-03-24 15:19:31.920000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_nhung_GetTreo_SHD
    @SoHopDong NVARCHAR(MAX)
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
	WHERE HopDongREF = (SELECT HopDongID FROM dbo.HopDong WHERE SoHopDong = @SoHopDong)
	ORDER BY HopDongChiTietREF DESC
END;

```
