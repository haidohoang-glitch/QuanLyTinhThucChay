# Stored Procedure: `sp_kiemtrachotsoB1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-17 16:21:08.813000
- **Ngày sửa cuối**: 2026-03-17 16:30:39.847000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `date(3)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[sp_kiemtrachotsoB1]
    @NgayBatDau DATE
AS
BEGIN
    SET NOCOUNT ON;

    -----------------------------------------
    -- B1: ThucChayDaTinh
    -----------------------------------------
    SELECT 
		'TCDT' TCDT,
        SoHopDong,
        HopDongID,
        HopDongChiTietREF,
        DmSanPhamref,
        DmLoaiBannerREF,
        CASE DmLoaiBannerREF 
            WHEN 17 THEN N'Chi phí'
            WHEN 18 THEN N'Mua ngoài'
            ELSE N'None'
        END AS LoaiBanner,
        DmHinhThucQuangCao,
        TenHinhThucQuangCao,
        NhanHang,
        TenKhachHang,
        SUM(ThanhTienSauTrietKhauThucChay) AS TienChinh,
        SUM(GiaTriThayDoi) AS TienThayDoi,
        NgayThucHien,
        N'ThucChayDaTinh' AS Nguon
    FROM ThucChayDaTinh
    WHERE Nam <= 2019
        AND NgayThucHien >= @NgayBatDau    
        AND HopDongID <> 0
    GROUP BY 
        SoHopDong, HopDongID, HopDongChiTietREF, DmSanPhamref,
        NgayThucHien, DmLoaiBannerREF, TenHinhThucQuangCao,
        DmHinhThucQuangCao, NhanHang, TenKhachHang
    

    -----------------------------------------
    -- B2: ThucChayDaTinhAdmarket
    -----------------------------------------
    SELECT 
		'TCDTAdmarket' TCDTAdmarket,
        SoHopDong,
        HopDongID,
        HopDongChiTietREF,
        DmSanPhamref,
        DmLoaiBannerREF,
        CASE DmLoaiBannerREF 
            WHEN 17 THEN N'Chi phí'
            WHEN 18 THEN N'Mua ngoài'
            ELSE N'None'
        END AS LoaiBanner,
        DmHinhThucQuangCao,
        TenHinhThucQuangCao,
        NhanHang,
        TenKhachHang,
        SUM(ThanhTienSauTrietKhauThucChay) AS TienChinh,
        SUM(GiaTriThayDoi) AS TienThayDoi,
        NgayThucHien,
        N'Admarket' AS Nguon
    FROM dbo.ThucChayDaTinhAdmarket
    WHERE Nam <= 2019
        AND NgayThucHien >= @NgayBatDau
        AND HopDongID <> 0
    GROUP BY 
        SoHopDong, HopDongID, HopDongChiTietREF, DmSanPhamref,
        NgayThucHien, DmLoaiBannerREF, TenHinhThucQuangCao,
        DmHinhThucQuangCao, NhanHang, TenKhachHang

    ORDER BY NgayThucHien
END

```
