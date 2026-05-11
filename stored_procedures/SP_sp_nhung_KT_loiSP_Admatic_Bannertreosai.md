# Stored Procedure: `sp_nhung_KT_loiSP_Admatic_Bannertreosai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-20 09:35:29.463000
- **Ngày sửa cuối**: 2026-03-20 09:35:29.463000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_nhung_KT_loiSP_Admatic_Bannertreosai
AS
BEGIN
    SET NOCOUNT ON;
-- ===============================================
/* Bước 1: Tách sản phẩm treo theo banner */
WITH B_Split AS (
    SELECT 
        temp.HopDongChiTietREF,
        temp.DmBannerREF,
        temp.sohopdong,
        LTRIM(RTRIM(value)) AS DmSanPhamREF_raw
    FROM (
        SELECT 
            HopDongChiTietREF,
            DmBannerREF,
            dbo.GetSoHopDongByID(HopDongREF) AS sohopdong,
            CAST(DmSanPhamREF AS NVARCHAR(MAX)) AS DmSanPhamChuoi
        FROM dbo.ThucChayHopDongChiTiet
        WHERE 
            HopDongChiTietREF IN (
                SELECT HopDongChiTietID 
                FROM dbo.HopDongChiTiet 
                WHERE DeletedStatus = 0 
                      AND DmLoaiREF = 42 
                      AND DmSanPhamREF NOT IN (140, 549)
                      AND DmLoaiNenTangREF <> 9
            )
            AND HopDongREF IN (
                SELECT HopDongID 
                FROM dbo.HopDong 
                WHERE Nam >= 2024
            )
            AND DeletedStatus = 0
    ) AS temp
    CROSS APPLY STRING_SPLIT(temp.DmSanPhamChuoi, ',')
),

/* Bước 2: So sánh 3 nguồn, đồng thời LOẠI “Marketing fee – Chi phí marketing”
   khỏi nguồn Admatic (a.DmSanPhamREF) và nguồn Treo (b.DmSanPhamREF_raw) */
SoSanhLec AS (
    SELECT 
        a.SoHopDong,
        b.HopDongChiTietREF,
        a.DmBannerID,
        a.DmSanPhamREF                            AS SanPham_Admatic,
        TRY_CAST(b.DmSanPhamREF_raw AS INT)       AS SanPham_Treo,
        hdc.DmSanPhamREF                          AS SanPham_HD,
        ROW_NUMBER() OVER (
            PARTITION BY a.SoHopDong, b.HopDongChiTietREF, a.DmBannerID 
            ORDER BY TRY_CAST(b.DmSanPhamREF_raw AS INT)
        ) AS rn,
        hdc.TenSanPham                            AS TenSanPham_HĐ
    FROM dbo.ThucChay_ThanhTien_Admatic a
    JOIN B_Split b 
        ON a.DmBannerID = b.DmBannerREF
       AND a.SoHopDong = b.sohopdong
    JOIN dbo.HopDongChiTiet hdc 
        ON b.HopDongChiTietREF = hdc.HopDongChiTietID
    /* Join tên SP để lọc fee */
    LEFT JOIN dbo.DmSanPham spA ON spA.DmSanPhamID = a.DmSanPhamREF
    LEFT JOIN dbo.DmSanPham spT ON spT.DmSanPhamID = TRY_CAST(b.DmSanPhamREF_raw AS INT)
    WHERE 
        b.DmSanPhamREF_raw LIKE '%[0-9]%'
        AND TRY_CAST(b.DmSanPhamREF_raw AS INT) IS NOT NULL

        /* LOẠI Marketing fee ở nguồn Admatic và Treo */
        AND (spA.DmSanPhamID IS NULL 
             OR (spA.TenSanPham NOT LIKE N'%Marketing fee%' 
                 AND spA.TenSanPham NOT LIKE N'%Chi phí marketing%'))
        AND (spT.DmSanPhamID IS NULL 
             OR (spT.TenSanPham NOT LIKE N'%Marketing fee%' 
                 AND spT.TenSanPham NOT LIKE N'%Chi phí marketing%'))

        /* Điều kiện lệch (giữ nguyên ý tưởng ban đầu) */
        AND (
            (hdc.DmSanPhamREF <> 733 AND (
                a.DmSanPhamREF <> TRY_CAST(b.DmSanPhamREF_raw AS INT)
                OR a.DmSanPhamREF <> hdc.DmSanPhamREF
                OR TRY_CAST(b.DmSanPhamREF_raw AS INT) <> hdc.DmSanPhamREF
            ))
            OR (hdc.DmSanPhamREF = 733 
                AND a.DmSanPhamREF <> TRY_CAST(b.DmSanPhamREF_raw AS INT))
        )
)

/* Bước 3: Hiển thị 1 dòng duy nhất mỗi tổ hợp */
SELECT 
    s.SoHopDong,
    s.HopDongChiTietREF,
    s.DmBannerID,
    s.SanPham_Admatic,    
    s.SanPham_Treo,    
    s.SanPham_HD,
    sp2.TenSanPham AS TenSanPham_Treo,
    sp1.TenSanPham AS TenSanPham_Admatic,
    sp3.TenSanPham AS TenSanPham_HD
FROM SoSanhLec s
LEFT JOIN dbo.DmSanPham sp1 ON s.SanPham_Admatic = sp1.DmSanPhamID
LEFT JOIN dbo.DmSanPham sp2 ON s.SanPham_Treo = sp2.DmSanPhamID
LEFT JOIN dbo.DmSanPham sp3 ON s.SanPham_HD = sp3.DmSanPhamID
WHERE s.rn = 1
ORDER BY s.SoHopDong, s.HopDongChiTietREF, s.DmBannerID;


END;
```
