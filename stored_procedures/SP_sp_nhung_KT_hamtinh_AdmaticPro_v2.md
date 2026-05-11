# Stored Procedure: `sp_nhung_KT_hamtinh_AdmaticPro_v2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-19 17:30:17.727000
- **Ngày sửa cuối**: 2026-03-27 09:35:22.693000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_nhung_KT_hamtinh_AdmaticPro_v2
AS
BEGIN
    SET NOCOUNT ON;

;WITH HD AS 
(
    SELECT  
        hd.SoHopDong,
        hdct.HopDongChiTietID,
        hdct.DonViTinhREF,
        hdct.DonViTinh,
        hdct.SoLuong AS SoLuongHD,
        hdct.ChietKhau,
        hdct.ThanhTien AS ThanhTienHD,
        hdct.DmSanPhamREF AS DmSanPhamREF_HD,
        hdct.DonGia,
        (hdct.SoLuong * hdct.DonGia) AS ThanhTienKM_HD
    FROM dbo.HopDong hd
    INNER JOIN dbo.HopDongChiTiet hdct 
        ON hd.HopDongID = hdct.HopDongFK
    WHERE 
        hdct.DmLoaiNenTangREF = 9
        AND hd.Nam >= 2020
        -- AND hdct.DmSanPhamREF = 817
        AND hdct.DmSanPhamREF NOT IN (637,141)
        AND NOT hdct.TenLoai LIKE N'Performance Package'
        AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18)
        AND NOT (
            hdct.DmSanPhamREF IN (306, 423, 5188) 
            OR hdct.DmViTriREF IN (100093, 100478, 100774)
        )
        -- AND hd.SoHopDong = 'QC4731025'
),

Treo AS 
(
    -- Gộp banner theo HopDongChiTietREF
    SELECT  
        t.HopDongChiTietREF,

        STUFF(
        (
            SELECT '/' + CAST(t2.DmBannerREF AS VARCHAR(50))
            FROM dbo.ThucChayHopDongChiTiet t2
            WHERE t2.HopDongChiTietREF = t.HopDongChiTietREF
            FOR XML PATH(''), TYPE
        ).value('.', 'nvarchar(max)'), 1, 1, '') AS DmBannerREF,

        MIN(t.DmSanPhamREF) AS DmSanPhamREF_Treo,

        MAX(CASE WHEN t.DeletedStatus = 0 THEN 1 ELSE 0 END) AS HasActiveBanner,
        MAX(CASE WHEN t.DeletedStatus = 1 THEN 1 ELSE 0 END) AS HasDeletedBanner,

        SUM(t.ThanhTien) AS ThanhTienTreo

    FROM dbo.ThucChayHopDongChiTiet t
    INNER JOIN HD h 
        ON h.HopDongChiTietID = t.HopDongChiTietREF
    GROUP BY 
        t.HopDongChiTietREF
),

TCDT AS 
(
    -- Gộp thực chạy (giới hạn theo HD)
    SELECT  
        x.HopDongChiTietREF,
        x.DmSanPhamREF AS DmSanPhamREF_Tinh,

        SUM(x.SoLuongThucChay + x.SoLuongThayDoi) AS SoLuongTC,
        SUM(x.ThanhTienSauTrietKhauThucChay + x.GiaTriThayDoi) AS ThanhTien_TC,

        SUM(x.SoLuongThucChayKM + x.SoLuongKMThayDoi) AS SoLuongKM,
        SUM(x.ThanhTienKM + x.GiaTriKMThayDoi) AS ThanhTien_KM

    FROM 
    (
        SELECT  
            t.HopDongChiTietREF,
            t.DmSanPhamREF,
            t.SoLuongThucChay,
            t.SoLuongThayDoi,
            t.ThanhTienSauTrietKhauThucChay,
            t.GiaTriThayDoi,
            t.SoLuongThucChayKM,
            t.SoLuongKMThayDoi,
            t.ThanhTienKM,
            t.GiaTriKMThayDoi
        FROM dbo.ThucChayDaTinh t
        INNER JOIN HD h 
            ON h.HopDongChiTietID = t.HopDongChiTietREF
        WHERE t.DmSanPhamREF NOT IN (585)

        UNION ALL

        SELECT  
            a.HopDongChiTietREF,
            a.DmSanPhamREF,
            a.SoLuongThucChay,
            a.SoLuongThayDoi,
            a.ThanhTienSauTrietKhauThucChay,
            a.GiaTriThayDoi,
            a.SoLuongThucChayKM,
            a.SoLuongKMThayDoi,
            a.ThanhTienKM,
            a.GiaTriKMThayDoi
        FROM dbo.ThucChayDaTinhAdmarket a
        INNER JOIN HD h 
            ON h.HopDongChiTietID = a.HopDongChiTietREF
        WHERE a.DmSanPhamREF IN (585)
    ) x

    GROUP BY 
        x.HopDongChiTietREF,
        x.DmSanPhamREF
),

Data AS 
(
    SELECT  
        hd.SoHopDong,
        hd.HopDongChiTietID,
        hd.DonViTinhREF,
        hd.DonViTinh,

        ---------------------------------------------------
        -- DmSanPham gộp
        ---------------------------------------------------
        CASE 
            WHEN hd.DmSanPhamREF_HD = treo.DmSanPhamREF_Treo 
             AND hd.DmSanPhamREF_HD = tcdt.DmSanPhamREF_Tinh 
            THEN CAST(hd.DmSanPhamREF_HD AS VARCHAR(50))

            ELSE LTRIM(
                STUFF(
                    ISNULL('/' + CAST(hd.DmSanPhamREF_HD AS VARCHAR(50)), '') 
                    + CASE 
                        WHEN treo.DmSanPhamREF_Treo IS NOT NULL 
                         AND treo.DmSanPhamREF_Treo <> hd.DmSanPhamREF_HD
                        THEN '/' + CAST(treo.DmSanPhamREF_Treo AS VARCHAR(50)) 
                        ELSE '' 
                      END
                    + CASE 
                        WHEN tcdt.DmSanPhamREF_Tinh IS NOT NULL 
                         AND tcdt.DmSanPhamREF_Tinh NOT IN (hd.DmSanPhamREF_HD, treo.DmSanPhamREF_Treo)
                        THEN '/' + CAST(tcdt.DmSanPhamREF_Tinh AS VARCHAR(50)) 
                        ELSE '' 
                      END,
                1, 1, '')
            )
        END AS DmSanPham,

        hd.SoLuongHD,
        hd.DonGia,
        hd.ChietKhau,

        CASE 
            WHEN hd.ChietKhau = 100 THEN hd.SoLuongHD * hd.DonGia 
            ELSE hd.ThanhTienHD 
        END AS ThanhTienHD_ApDung,

        treo.DmBannerREF,
        treo.HasActiveBanner,
        treo.HasDeletedBanner,
        treo.ThanhTienTreo,

        CASE 
            WHEN hd.ChietKhau = 100 THEN tcdt.SoLuongKM 
            ELSE tcdt.SoLuongTC 
        END AS SoLuongTC_ApDung,

        CASE 
            WHEN hd.ChietKhau = 100 THEN tcdt.ThanhTien_KM 
            ELSE tcdt.ThanhTien_TC 
        END AS ThanhTienTC_ApDung

    FROM HD hd
    LEFT JOIN Treo treo 
        ON treo.HopDongChiTietREF = hd.HopDongChiTietID
    LEFT JOIN TCDT tcdt 
        ON tcdt.HopDongChiTietREF = hd.HopDongChiTietID
)

SELECT  
    SoHopDong,
    HopDongChiTietID,
    DonViTinhREF,
    DonViTinh,
    DmSanPham,

    dbo.FormatNumber(SoLuongHD) AS SoLuongHD,
    dbo.FormatNumber(DonGia) AS DonGia,
    dbo.FormatNumber(ThanhTienHD_ApDung) AS ThanhTienHD,

    DmBannerREF,
    dbo.FormatNumber(ThanhTienTreo) AS ThanhTienTreo,

    dbo.FormatNumber(SoLuongTC_ApDung) AS SoLuongTC,
    dbo.FormatNumber(ThanhTienTC_ApDung) AS ThanhTienTC,

    dbo.FormatNumber(ThanhTienHD_ApDung - ThanhTienTC_ApDung) AS LechTien,

    ---------------------------------------------------
    -- Ghi chú
    ---------------------------------------------------
    CASE 
        WHEN ThanhTienTreo IS NOT NULL 
         AND ThanhTienTreo > 0 
         AND ROUND(ThanhTienTreo,0) = ROUND(ThanhTienTC_ApDung,0)
            THEN N'Đã tính đủ theo treo'

        WHEN DmBannerREF IS NOT NULL 
         AND HasActiveBanner = 1 
         AND ROUND(ThanhTienHD_ApDung,0) = ROUND(ThanhTienTC_ApDung,0)
            THEN N'Đã ghi nhận đủ thực chạy'

        WHEN HasActiveBanner = 0 
         AND HasDeletedBanner = 1 
         AND COALESCE(ThanhTienTC_ApDung,0) > 0
            THEN N'Sai - Đã xóa treo nhưng vẫn có thực chạy'

        WHEN DmBannerREF IS NULL 
         AND COALESCE(ThanhTienTC_ApDung,0) > 0
            THEN N'Sai - Chưa treo mà có thực chạy'

        WHEN HasActiveBanner = 1 
         AND ROUND(ThanhTienHD_ApDung,0) > ROUND(ThanhTienTC_ApDung,0)
            THEN N'Sai - Chưa khớp tiền với HĐ ký'

        WHEN HasActiveBanner = 1 
         AND ROUND(ThanhTienHD_ApDung,0) < ROUND(ThanhTienTC_ApDung,0)
            THEN N'Sai - Vượt tiền với HĐ ký'

        WHEN HasActiveBanner = 0 
         AND HasDeletedBanner = 1 
         AND COALESCE(ThanhTienTC_ApDung,0) = 0
            THEN N'Đã ghi nhận đúng'

        ELSE NULL
    END AS GhiChu

FROM Data

WHERE NOT 
(
       (HasActiveBanner = 1 AND ROUND(ThanhTienHD_ApDung,0) = ROUND(ThanhTienTC_ApDung,0))
    OR (DmBannerREF IS NULL AND COALESCE(ThanhTienTC_ApDung,0) = 0)
    OR (HasActiveBanner = 0 AND HasDeletedBanner = 1 AND COALESCE(ThanhTienTC_ApDung,0) = 0)
    OR (ThanhTienTreo IS NOT NULL AND ThanhTienTreo > 0 AND ROUND(ThanhTienTreo,0) = ROUND(ThanhTienTC_ApDung,0))
)

AND Data.SoHopDong NOT IN 
(
    'NB0250623','NB0310723','NB0280723',
    'NB0160623','NB0220723','NB0330523',
    'NB0350523','NB0300723','NB0180623',
    'NB0340523','NB0200623',
    'QC6200922','QC7291022','QC0221220'
);
	    
END


```
