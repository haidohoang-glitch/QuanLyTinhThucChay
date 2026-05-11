# Stored Procedure: `nhung_ThucChayNguon_Muangoai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 17:42:56.423000
- **Ngày sửa cuối**: 2026-03-06 17:42:56.423000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[nhung_ThucChayNguon_Muangoai]
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

SELECT 
    N'ThucChay nguon' AS [ThucChay],
    Id,
    B_DuToan_ChiTiet_HopDongREF AS ID_DutoanMua,
    HopDongId,
    PhanBoId,
    TrangThai,
    D_DonViTinhREF,
    dbo.FormatNumber(SoLuongChay) AS SoLuongChay,
    dbo.FormatNumber(DonGia) AS DonGia,
    dbo.FormatNumber(ChietKhauMua) AS ChietKhauMua,
    dbo.FormatNumber(ThanhTien) AS ThanhTien,
    dbo.FormatNumber(SoLuongChay * DonGia * (100 - ChietKhauMua) / 100) AS ThanhTienSauCK,
    IsDeleted,
    NguoiGuiDuyet,
    NgayGuiDuyet,
    NguoiDuyet,
    CreationTime,
    CreatorUserId,
    LastModificationTime,
    LastModifierUserId,
    LinkNghiemThu
FROM [asdag2].pms.dbo.B_QuanLyThucChay
WHERE PhanBoId = @HopDongChiTietID
  AND IsDeleted = 0

UNION ALL

SELECT
    N'TỔNG' AS [ThucChay],
    NULL AS Id,
    NULL AS B_DuToan_ChiTiet_HopDongREF,
    NULL AS HopDongId,
    NULL AS PhanBoId,  
    NULL AS TrangThai,
    NULL AS D_DonViTinhREF,
    dbo.FormatNumber(SUM(SoLuongChay)) AS SoLuongChay,
    NULL AS DonGia,
    NULL AS ChietKhauMua,
    dbo.FormatNumber(SUM(ThanhTien)) AS ThanhTien,
    dbo.FormatNumber(SUM(SoLuongChay * DonGia * (100 - ChietKhauMua) / 100)) AS ThanhTienSauCK,
    0 AS IsDeleted,
    NULL AS NguoiGuiDuyet,
    NULL AS NgayGuiDuyet,
    NULL AS NguoiDuyet,
    NULL AS CreationTime,
    NULL AS CreatorUserId,
    NULL AS LastModificationTime,
    NULL AS LastModifierUserId,
    NULL AS LinkNghiemThu
FROM [asdag2].pms.dbo.B_QuanLyThucChay
WHERE PhanBoId = @HopDongChiTietID
  AND IsDeleted = 0

ORDER BY Id DESC;


END 

```
