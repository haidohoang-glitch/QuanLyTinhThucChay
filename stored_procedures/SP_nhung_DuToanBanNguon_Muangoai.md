# Stored Procedure: `nhung_DuToanBanNguon_Muangoai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 17:39:32.380000
- **Ngày sửa cuối**: 2026-03-06 17:39:32.380000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[nhung_DuToanBanNguon_Muangoai]
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

select 'DuToanBan nguon'[DuToanBan],
ID
,B_DuToanREF AS ID_Dutoandich,
PhanBoId
,D_SanPhamREF
,SoLuong
,dbo.FormatNumber(DonGia) AS DonGia
,ChietKhau
,dbo.FormatNumber(ThanhTien) AS ThanhTien
,dbo.FormatNumber(ChenhLech) AS ChenhLech
,CreationTime
,CreatorUserId
,LastModificationTime
,LastModifierUserId 
FROM [ASDAG2].PMS.dbo.B_DuToan_ChiTiet 
WHERE phanboid = @HopDongChiTietID and IsDeleted = 0-- du toan ban

END 

```
