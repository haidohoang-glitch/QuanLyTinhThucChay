# Stored Procedure: `CheckThucChayVuotHopDongPerformancebase_v1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-10-29 09:08:35.170000
- **Ngày sửa cuối**: 2025-07-21 10:46:29.767000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[CheckThucChayVuotHopDongPerformancebase_v1]
AS
BEGIN	
-- Truy vấn 1: Thực chạy vượt phân bổ Admarket

DECLARE @MaxYear INT = (SELECT YEAR(MAX(NgayThucHien)) FROM dbo.ThucChayDaTinhAdmarket)
SELECT  
    tc.SoHopDong,
    tc.HopDongID,
    tc.HopDongChiTietREF AS HopDongChiTietID,
    tc.TenSanPham,
    NULL AS TenLoai,
    NULL AS TenBanner,
    NULL AS ChietKhau,
    NULL AS ThanhTienKM,
    NULL AS ThanhTien,
    tc.ThanhTienThucchay AS ThucChay,
    hdct.GiaTriPhanBo AS PhanBo,
    (tc.ThanhTienThucchay - hdct.GiaTriPhanBo) AS GiaTriVuot
FROM 
    (SELECT 
        SoHopDong,
        HopDongID,
        HopDongChiTietREF,
        TenSanPham,
        SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS ThanhTienThucchay,
        Nam
    FROM dbo.ThucChayDaTinhAdmarket
    WHERE 
        HopDongID <> 0
        AND DmSanPhamREF IN (144, 585, 628, 337)
        AND DmHinhThucQuangCao <> 42
        AND Nam >= (@MaxYear - 3)
    GROUP BY 
        SoHopDong,
        HopDongID,
        HopDongChiTietREF,
        TenSanPham,
        Nam
    ) AS tc
INNER JOIN 
    (SELECT 
        HopDongChiTietID,
        TK_AdMarket,
        TenLoaiBanner,
        ThanhTien AS GiaTriPhanBo
    FROM dbo.HopDongChiTiet
	WHERE DmSanPhamREF IN (144,585,628)
    ) AS hdct
ON tc.HopDongChiTietREF = hdct.HopDongChiTietID
WHERE (tc.ThanhTienThucchay - hdct.GiaTriPhanBo) > 100

UNION ALL

-- Truy vấn 2: Thực chạy vượt phân bổ Marketing fee
SELECT 
    A.SoHopDong,  
    NULL AS HopDongID,
    A.HopDongChiTietID,
    A.TenSanPham, 
    A.TenLoai, 
    A.TenBanner, 
    A.ChietKhau,
    A.ThanhTienKM,
    A.ThanhTien,
    (B.TTTC + B.TTKM) AS ThucChay,
    (A.ThanhTien + A.ThanhTienKM) AS PhanBo,
    (B.TTTC + B.TTKM - A.ThanhTien - A.ThanhTienKM) AS GiaTriVuot
FROM (
    SELECT 
        hd.SoHopDong,  
        hdct.HopDongChiTietID, 
        hdct.TenSanPham, 
        hdct.TenLoai, 
        hdct.TenBanner, 
        hdct.ChietKhau,
        CASE 
            WHEN hdct.ChietKhau = 100 THEN hdct.DonGia * hdct.SoLuong
            ELSE 0 
        END AS ThanhTienKM,
        CASE 
            WHEN hdct.ChietKhau <> 100 THEN hdct.DonGia * hdct.SoLuong * (1 - hdct.ChietKhau / 100.0)
            ELSE 0 
        END AS ThanhTien
    FROM dbo.HopDong hd
    INNER JOIN dbo.HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK
    WHERE 
        hd.NgayDanhSoHopDong >= '2025-07-05'
        AND hdct.DmLoaiREF = 5038
        AND hdct.DmSanPhamREF = 817
        AND hdct.DeletedStatus = 0
) A
INNER JOIN (
    SELECT 
        tcdt.SoHopDong, 
        tcdt.HopDongChiTietREF, 
        SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS TTTC,
        SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) AS TTKM
    FROM dbo.ThucChayDaTinh tcdt
    GROUP BY tcdt.SoHopDong, tcdt.HopDongChiTietREF
) B
ON B.SoHopDong = A.SoHopDong 
   AND B.HopDongChiTietREF = A.HopDongChiTietID
WHERE (B.TTTC + B.TTKM - A.ThanhTien - A.ThanhTienKM) > 0
END;

```
