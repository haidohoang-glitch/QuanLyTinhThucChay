# Stored Procedure: `sp_nhung_KT_hamtinh_Admatic_Bai_URL`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-19 17:21:20.943000
- **Ngày sửa cuối**: 2026-03-19 17:45:44.583000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_nhung_KT_hamtinh_Admatic_Bai_URL
AS
BEGIN
    SET NOCOUNT ON;
	SELECT  
    'Admatic' AS Admatic_Bai_URL,
    C.SoHopDong,
    C.HopDongID,
    C.HopDongChiTietID,
    C.DonViTinh,
    C.SoLuong,

    dbo.FormatNumber(C.DonGia) AS DonGiaHD,
    C.ChietKhau,

    dbo.FormatNumber(
        CASE 
            WHEN C.ChietKhau = 100 THEN C.SoLuong * C.DonGia 
            ELSE C.ThanhTien 
        END
    ) AS ThanhTienHD,

    ISNULL(C.Soluongtreo, 0) AS Soluongtreo,

    dbo.FormatNumber(
        CASE 
            WHEN C.ChietKhau = 100 THEN ISNULL(D.SoluongTCKM, 0) 
            ELSE ISNULL(D.SoluongTC, 0) 
        END
    ) AS SoluongTC_ASD,

    dbo.FormatNumber(
        CASE 
            WHEN C.ChietKhau = 100 THEN ISNULL(D.ThanhtienTCKM, 0) 
            ELSE ISNULL(D.ThanhtienTC, 0) 
        END
    ) AS ThanhtienTC_ASD

FROM 
(
    SELECT 
        A.*,
        B.Soluongtreo
    FROM 
    (
        SELECT  
            hd.HopDongID,
            hd.SoHopDong,
            hdct.HopDongChiTietID,
            hdct.DonViTinh,
            hdct.SoLuong,
            hdct.DonGia,
            hdct.ChietKhau,
            hdct.ThanhTien
        FROM dbo.HopDongChiTiet hdct
        INNER JOIN dbo.HopDong hd 
            ON hd.HopDongID = hdct.HopDongFK
        WHERE 
            1 = 1
            -- hdct.DmSanPhamREF IN (305, 5312, 598)
            AND hdct.DonViTinhREF IN (7, 84)
            AND hdct.DmLoaiREF = 42
            AND hd.DeletedStatus = 0
            AND hdct.DeletedStatus = 0
            AND hd.TrangThaiHopDong NOT IN (0, 3)
            -- AND HopDongChiTietID = '744047'
    ) A

    LEFT JOIN 
    (
        SELECT  
            COUNT(*) AS Soluongtreo,
            tt.HopDongChiTietREF
        FROM dbo.ThucChayHopDongChiTiet tt
        WHERE tt.DeletedStatus = 0
        GROUP BY tt.HopDongChiTietREF
    ) B
        ON A.HopDongChiTietID = B.HopDongChiTietREF
) C

LEFT JOIN 
(
    SELECT  
        tcdt.HopDongChiTietREF,
        SUM(tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi) AS SoluongTC,
        SUM(tcdt.SoLuongThucChayKM + tcdt.SoLuongKMThayDoi) AS SoluongTCKM,
        SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS ThanhtienTC,
        SUM(tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi) AS ThanhtienTCKM
    FROM dbo.ThucChayDaTinh tcdt
    GROUP BY tcdt.HopDongChiTietREF
) D
    ON C.HopDongChiTietID = D.HopDongChiTietREF

WHERE 
    1 = 1
    AND ISNULL(C.Soluongtreo, 0) <= C.SoLuong

    AND ISNULL(C.Soluongtreo, 0) <> 
        CASE 
            WHEN C.ChietKhau = 100 THEN ISNULL(D.SoluongTCKM, 0) 
            ELSE ISNULL(D.SoluongTC, 0) 
        END

    AND 
        CASE 
            WHEN C.ChietKhau = 100 THEN ISNULL(D.SoluongTCKM, 0) 
            ELSE ISNULL(D.SoluongTC, 0) 
        END <> C.SoLuong

    AND NOT C.SoHopDong IN 
        ('QC10331221', 'QC8240322', 'TR0010921', 'QC1400623', 'QC2050724')

ORDER BY 
    C.HopDongID;


	    
END


```
