# Stored Procedure: `nhung_DuToanMuaNguon_Muangoai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 17:41:21.173000
- **Ngày sửa cuối**: 2026-03-06 17:41:21.173000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[nhung_DuToanMuaNguon_Muangoai]
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

SELECT
    0 AS SortOrder,
    N'DuToanMua nguon' AS [DuToanMua],
    Id,
    B_DuToan_ChiTiet_REF AS ID_dutoanban,
    SoHopDongMua,
    SoLuongMua,
    dbo.FormatNumber(DonGiaMua) AS DonGiaMua,
    ChietKhauMua,
    dbo.FormatNumber(PhaiTraNhaCungCap) AS ThanhtienMua,
    dbo.FormatNumber(TongChiPhi) AS TongChiPhiMua,
    Vat,
    dbo.FormatNumber(ThanhTienSauCK) AS ThanhTienCoVat,
    IsDeleted,
    CreationTime,
    CreatorUserId,
    LastModificationTime,
    LastModifierUserId
FROM [asdag2].PMS.dbo.B_DuToan_Chitiet_HopDong
WHERE B_DuToan_ChiTiet_REF IN (
    SELECT Id
    FROM [asdag2].PMS.dbo.B_DuToan_ChiTiet
    WHERE PhanBoId = @HopDongChiTietID
      AND IsDeleted = 0
)

UNION ALL

SELECT
    1 AS SortOrder,
    N'TỔNG' AS [DuToanMua],
    NULL AS Id,
    NULL AS ID_dutoanban,
    NULL AS SoHopDongMua,
    SUM(SoLuongMua) AS SoLuongMua,
    NULL AS DonGiaMua,
    NULL AS ChietKhauMua,
    dbo.FormatNumber(SUM(PhaiTraNhaCungCap)) AS ThanhtienMua,
    dbo.FormatNumber(SUM(TongChiPhi)) AS TongChiPhiMua,
    NULL AS Vat,
    dbo.FormatNumber(SUM(ThanhTienSauCK)) AS ThanhTienCoVat,
    0 AS IsDeleted,
    NULL AS CreationTime,
    NULL AS CreatorUserId,
    NULL AS LastModificationTime,
    NULL AS LastModifierUserId
FROM [asdag2].PMS.dbo.B_DuToan_Chitiet_HopDong
WHERE B_DuToan_ChiTiet_REF IN (
    SELECT Id
    FROM [asdag2].PMS.dbo.B_DuToan_ChiTiet
    WHERE PhanBoId = @HopDongChiTietID
      AND IsDeleted = 0
)

ORDER BY SortOrder, LastModificationTime;

END 

```
