# Stored Procedure: `sp_nhung_GetSoHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-24 15:07:40.320000
- **Ngày sửa cuối**: 2026-03-24 15:07:40.320000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_nhung_GetSoHopDong
    @SoHopDong NVARCHAR(50)
AS
BEGIN
    SET NOCOUNT ON;

    -- ===== DỮ LIỆU CHI TIẾT =====
    SELECT 
        hd.SoHopDong,
        hd.HopDongID,
        hdct.HopDongChiTietID,
        hdct.TenSanPham,
        hdct.TenLoai,
        dbo.FormatNumber(hdct.SoLuong) AS SoLuong,
        hdct.DonViTinh,
        dbo.FormatNumber(hdct.DonGia) AS DonGia,
        hdct.ChietKhau,
        dbo.FormatNumber(hdct.ThanhTien) AS ThanhtienHĐ,
        hdct.TenLoaiNenTang,
        hd.NhanHopDong,
        hdct.NhanHang,
        hd.DmNhanGocREF,
        dbo.FormatNumber(hd.GiaTriHopDong) AS GiaTriHopDong,
        hdct.CreatedAt,
        hdct.CreatedBy,
        hdct.LastModifiedAt,
        hdct.LastModifiedBy
    FROM dbo.HopDongChiTiet hdct
    INNER JOIN dbo.HopDong hd
        ON hd.HopDongID = hdct.HopDongFK
    WHERE hd.SoHopDong = @SoHopDong
      AND hdct.DeletedStatus = 0

    UNION ALL

    -- ===== DÒNG TỔNG =====
    SELECT
        N'TỔNG' AS SoHopDong,
        NULL AS HopDongID,
        NULL AS HopDongChiTietID,
        NULL AS TenSanPham,
        NULL AS TenLoai,
        dbo.FormatNumber(SUM(hdct.SoLuong)) AS SoLuong,
        NULL AS DonViTinh,
        NULL AS DonGia,
        NULL AS ChietKhau,
        dbo.FormatNumber(SUM(hdct.ThanhTien)) AS ThanhtienHĐ,
        NULL AS TenLoaiNenTang,
        NULL AS NhanHopDong,
        NULL AS NhanHang,
        NULL AS DmNhanGocREF,
        NULL AS GiaTriHopDong,
        NULL AS CreatedAt,
        NULL AS CreatedBy,
        NULL AS LastModifiedAt,
        NULL AS LastModifiedBy
    FROM dbo.HopDongChiTiet hdct
    INNER JOIN dbo.HopDong hd
        ON hd.HopDongID = hdct.HopDongFK
    WHERE hd.SoHopDong = @SoHopDong
      AND hdct.DeletedStatus = 0;
END;

```
