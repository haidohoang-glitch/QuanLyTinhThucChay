# Stored Procedure: `nhung_TCDTMuaNgoai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 16:56:10.173000
- **Ngày sửa cuối**: 2026-03-06 16:56:10.173000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE nhung_TCDTMuaNgoai
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

;WITH DATA AS (
    SELECT
        NgayThucHien,
        ID,
        DmChienDichREF,
        ThanhTien,  -- tiền HĐ (không SUM)
        SoLuong + SoLuongThayDoi AS SoLuong_TC,
        SoLuongThucChayKM + SoLuongKMThayDoi AS SoLuongKM,
        ThanhTienLaiThucChaySauCK + GiaTriThayDoiLaiSauCK AS Thanhtienlai,
        ThanhTienLaiThucChayKM + GiaTriKMLaiThayDoi AS ThanhtienKMlai,
        GhiChu
    FROM dbo.ThucChayDaTinh_MuaNgoai
    WHERE HopDongChiTietREF = @HopDongChiTietID
),
FINAL AS (
    -- 🔹 Chi tiết
    SELECT
        0 AS SortKey,
        NgayThucHien,
        ID,
        DmChienDichREF,
        ThanhTien,
        SoLuong_TC,
        SoLuongKM,
        Thanhtienlai,
        ThanhtienKMlai,
        GhiChu
    FROM DATA

    UNION ALL

    -- 🔹 Dòng TỔNG
    SELECT
        1 AS SortKey,
        NULL AS NgayThucHien,
        NULL AS ID,
        NULL AS DmChienDichREF,
        NULL AS ThanhTien,
        SUM(SoLuong_TC)     AS SoLuong_TC,
        SUM(SoLuongKM)      AS SoLuongKM,
        SUM(Thanhtienlai)   AS Thanhtienlai,
        SUM(ThanhtienKMlai) AS ThanhtienKMlai,
        N'TỔNG' AS GhiChu
    FROM DATA
)

SELECT
    NgayThucHien,
    ID,
    DmChienDichREF,
    dbo.FormatNumber(ThanhTien)        AS Thanhtien_HĐ,
    dbo.FormatNumber(SoLuong_TC)       AS SoLuong,
    dbo.FormatNumber(SoLuongKM)        AS SoLuongKM,
    dbo.FormatNumber(Thanhtienlai)     AS Thanhtienlai,
    dbo.FormatNumber(ThanhtienKMlai)   AS ThanhtienKMlai,
    GhiChu
FROM FINAL
ORDER BY SortKey, NgayThucHien DESC;

END 

```
