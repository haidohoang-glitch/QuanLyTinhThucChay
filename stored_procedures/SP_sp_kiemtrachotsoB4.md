# Stored Procedure: `sp_kiemtrachotsoB4`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-17 17:20:29.620000
- **Ngày sửa cuối**: 2026-03-17 17:20:29.620000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `date(3)` | No |

## Definition (Source Code)

```sql



CREATE PROCEDURE dbo.sp_kiemtrachotsoB4
    @NgayBatDau DATE   -- truyền ngày vào
AS
BEGIN
    SET NOCOUNT ON;

    -----------------------------------------
    -- B4: Check hợp đồng chi tiết bị = 0
    -----------------------------------------
    SELECT  
        t.HopDongChiTietREF,

        dbo.FormatNumber(SUM(
            t.SoLuongThucChay 
            + t.SoLuongThucChayKM 
            + t.SoLuongThayDoi 
            + t.SoLuongKMThayDoi
        )) AS SL,

        dbo.FormatNumber(SUM(
            t.ThanhTienSauTrietKhauThucChay 
            + t.GiaTriThayDoi 
            + t.ThanhTienKM 
            + t.GiaTriKMThayDoi
        )) AS Tien,

        dbo.FormatNumber(SUM(t.ThanhTienLechTreoHa)) AS ThanhTienLechTreoHa

    FROM ThucChayDaTinh t

    INNER JOIN HopDongChiTiet h 
        ON t.HopDongChiTietREF = h.HopDongChiTietID
        AND h.DeletedStatus = 1

    WHERE t.NgayThucHien >= @NgayBatDau

    GROUP BY t.HopDongChiTietREF

    HAVING ROUND(SUM(
            t.ThanhTienSauTrietKhauThucChay 
            + t.GiaTriThayDoi 
            + t.ThanhTienKM 
            + t.GiaTriKMThayDoi 
            + t.ThanhTienLechTreoHa
        ), 0) = 0

END

```
