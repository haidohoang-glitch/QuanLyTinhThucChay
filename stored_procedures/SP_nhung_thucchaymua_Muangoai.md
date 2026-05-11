# Stored Procedure: `nhung_thucchaymua_Muangoai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 17:48:38.347000
- **Ngày sửa cuối**: 2026-03-06 17:48:38.347000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[nhung_thucchaymua_Muangoai]
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

SELECT 
    id,
    ThucChayMuaNgoaiChiTietID AS IDnguon,
    HopDongREF,
    HopDongChiTietREF,
    CASE 
        WHEN [Status] = 0 THEN N'0: Mới'
        WHEN [Status] = 1 THEN N'1: Gửi duyệt TT'
        WHEN [Status] = 2 THEN N'2: Duyệt TT ngày duyệt'
        WHEN [Status] = 3 THEN N'3: Gửi duyệt TC'
        WHEN [Status] = 4 THEN N'4: Duyệt TC Ngày Chốt'
        ELSE N'' 
    END AS TrangThaiDuyet,
    dbo.FormatNumber(ThanhTienThucChayBanSauCK) AS ThanhTienThucChayBanSauCK,
    soluongthucchay,
    ChietKhauMuaNgoai,
    dbo.FormatNumber(ThanhTienMuaNgoaiTruocCK) AS MuaTruocCK,
    dbo.FormatNumber(ThanhTienMuaNgoaiTruocCK * (100 - ChietKhauMuaNgoai) / 100) AS MuaSauCK,
    dbo.FormatNumber(ThanhTienLaiThucChaySauCK) AS Lai,
    TrangThaiTinhThucChay,
    DeletedStatus,
    CreatedAt,
    LastModifiedAt,
    CreatedBy,
    LastModifiedBy,
    NgayChot
FROM dbo.ThucChayMuaNgoaiChiTiet
WHERE DeletedStatus = 0
  AND HopDongChiTietREF = @HopDongChiTietID

UNION ALL

SELECT
    NULL AS id,
    NULL AS IDnguon,
    NULL AS HopDongREF,
    NULL AS HopDongChiTietREF,              -- ✅ FIX: dùng hằng số (vì đã filter)
    N'TỔNG CỘNG' AS TrangThaiDuyet,
    dbo.FormatNumber(SUM(ThanhTienThucChayBanSauCK)) AS ThanhTienThucChayBanSauCK,
    SUM(soluongthucchay) AS soluongthucchay,
    NULL AS ChietKhauMuaNgoai,
    dbo.FormatNumber(SUM(ThanhTienMuaNgoaiTruocCK)) AS MuaTruocCK,
    dbo.FormatNumber(SUM(ThanhTienMuaNgoaiTruocCK * (100 - ChietKhauMuaNgoai) / 100)) AS MuaSauCK,
    dbo.FormatNumber(SUM(ThanhTienLaiThucChaySauCK)) AS Lai,
    NULL AS TrangThaiTinhThucChay,
    0 AS DeletedStatus,
    NULL AS CreatedAt,
    NULL AS LastModifiedAt,
    NULL AS CreatedBy,
    NULL AS LastModifiedBy,
    NULL AS NgayChot
FROM dbo.ThucChayMuaNgoaiChiTiet
WHERE DeletedStatus = 0
  AND HopDongChiTietREF = @HopDongChiTietID

ORDER BY id DESC;


END 

```
