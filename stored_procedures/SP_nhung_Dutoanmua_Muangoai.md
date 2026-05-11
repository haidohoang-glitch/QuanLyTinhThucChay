# Stored Procedure: `nhung_Dutoanmua_Muangoai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 17:45:45.690000
- **Ngày sửa cuối**: 2026-03-06 17:45:45.690000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[nhung_Dutoanmua_Muangoai]
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

SELECT ID
,SoHopDongMua
,HopDongChiTietID
,SoLuongMua
,dbo.FormatNumber(DonGiaMua) AS DonGiaMua
,ChietKhauMua
,dbo.FormatNumber(ThanhTienSauCKMua) as ThanhTienSauCKMua
,dbo.FormatNumber(ThanhTienBanSauCK) AS ThanhTienBanSauCK
,dbo.FormatNumber(ThanhTienLaiSauCK) AS ThanhTienLaiSauCK
,VAT
,DeletedStatus
,CreatedAt
,CreatedBy
,LastModifiedAt
,LastModifiedBy
FROM dbo.HopDongChiTiet_MuaNgoai WHERE HopDongChiTietID = @HopDongChiTietID


END 

```
