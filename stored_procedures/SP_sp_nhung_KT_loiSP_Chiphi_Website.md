# Stored Procedure: `sp_nhung_KT_loiSP_Chiphi_Website`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-27 14:46:13.447000
- **Ngày sửa cuối**: 2026-03-27 14:46:13.447000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `datetime(8)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.sp_nhung_KT_loiSP_Chiphi_Website
(
    @NgayBatDau DATETIME
)
AS
BEGIN
    SET NOCOUNT ON;

    ;WITH TTL_Latest AS (
        SELECT ThucChayHopDongChiTietID, LastModifiedAt, DmWebsiteREF
        FROM (
            SELECT 
                ThucChayHopDongChiTietID, 
                LastModifiedAt, 
                DmWebsiteREF,
                ROW_NUMBER() OVER (
                    PARTITION BY ThucChayHopDongChiTietID 
                    ORDER BY LastModifiedAt DESC
                ) AS rn
            FROM dbo.ThucChayHopDongChiTietLog WITH (NOLOCK)
        ) t
        WHERE rn = 1
    ),

    HDCT AS (
        SELECT 
            hd.SoHopDong,
            hd.HopDongID,
            hdct.HopDongChiTietID,
            hdct.DmSanPhamREF,
            hdct.TenSanPham,
            hdct.NhanHang,
            hdct.TenLoai,
            hdct.TenWebsite AS TenWebsite_HD,
            hdct.SoLuong AS SoLuongHĐ,
            hdct.ChietKhau,
            hdct.DonGia,
            CASE 
                WHEN hdct.ChietKhau = 100 THEN hdct.SoLuong * hdct.DonGia 
                ELSE hdct.ThanhTien 
            END AS ThanhTienHĐ
        FROM dbo.HopDongChiTiet hdct WITH (NOLOCK)
        INNER JOIN dbo.HopDong hd WITH (NOLOCK) 
            ON hd.HopDongID = hdct.HopDongFK
        WHERE hdct.DeletedStatus = 0
    ),

    TC_TREO AS (
        SELECT 
            tt.ThucChayHopDongChiTietID,
            tt.HopDongChiTietREF,
            tt.DmWebsiteREF,
            tt.TenWebsite AS TenWebsite_Treo
        FROM dbo.ThucChayHopDongChiTiet tt WITH (NOLOCK)
        INNER JOIN dbo.HopDong hd 
            ON tt.HopDongREF = hd.HopDongID AND hd.Nam >= 2024
        LEFT JOIN TTL_Latest ttl 
            ON ttl.ThucChayHopDongChiTietID = tt.ThucChayHopDongChiTietID
        WHERE 
            tt.DeletedStatus = 0
            AND tt.TrangThaiTreo = 2
            AND tt.DmSanPhamREF <> 5184
            AND tt.LoaiThucTreo = N'ChiPhi'
            AND (
                tt.CreatedAt >= @NgayBatDau
                OR (
                    tt.LastModifiedAt >= @NgayBatDau
                    AND ttl.LastModifiedAt >= @NgayBatDau
                    AND ttl.DmWebsiteREF IS NOT NULL
                    AND ttl.DmWebsiteREF > 0
                )
            )
    ),

    TCDT AS (
        SELECT         
            tcdt.TenWebsite AS TenWebsite_TC,
            TRY_CAST(tcdt.DotChayBooking AS INT) AS DotChayBooking_Int,
            SUM(ISNULL(tcdt.ThanhTienSauTrietKhauThucChay, 0) 
              + ISNULL(tcdt.GiaTriThayDoi, 0)) AS ThanhtienTC
        FROM dbo.ThucChayDaTinh tcdt WITH (NOLOCK)
        WHERE 
            TRY_CAST(tcdt.DotChayBooking AS INT) IS NOT NULL
            AND tcdt.NgayThucHien >= @NgayBatDau
        GROUP BY 
            tcdt.TenWebsite, 
            TRY_CAST(tcdt.DotChayBooking AS INT)
    ),

    WEBSITES AS (
        SELECT 
            ID,
            NAME   AS Website_Treo_Standard,
            DOMAIN AS Website_TC_Standard
        FROM ASDAG2.CONTRACT.dbo.WEBSITES
    ),

    MERGED AS (
        SELECT
            A.ThucChayHopDongChiTietID,
            A.HopDongChiTietREF,
            A.TenWebsite_Treo,
            A.DmWebsiteREF,
            B.DotChayBooking_Int,
            B.TenWebsite_TC,
            B.ThanhtienTC,
            C.SoHopDong,
            C.HopDongChiTietID,
            C.TenWebsite_HD,
            W.Website_Treo_Standard,
            W.Website_TC_Standard
        FROM TC_TREO A
        LEFT JOIN TCDT B 
            ON A.ThucChayHopDongChiTietID = B.DotChayBooking_Int
        LEFT JOIN HDCT C 
            ON C.HopDongChiTietID = A.HopDongChiTietREF
        LEFT JOIN WEBSITES W 
            ON A.DmWebsiteREF = W.ID
    ),

    MERGED_CLEANED AS (
        SELECT *,
            LOWER(TenWebsite_Treo) AS TenWebsite_Treo_Lower,
            LOWER(TenWebsite_TC) AS TenWebsite_TC_Lower,
            LOWER(Website_Treo_Standard) AS Website_Treo_Standard_Lower,
            LOWER(Website_TC_Standard) AS Website_TC_Standard_Lower
        FROM MERGED
    ),

    ID_CAN_XOA AS (
        SELECT ThucChayHopDongChiTietID
        FROM MERGED_CLEANED
        GROUP BY ThucChayHopDongChiTietID
        HAVING 
            SUM(CASE 
                    WHEN ThanhtienTC > 0 
                         AND TenWebsite_Treo_Lower = Website_Treo_Standard_Lower 
                         AND TenWebsite_TC_Lower = Website_TC_Standard_Lower 
                    THEN 1 ELSE 0 END
                ) > 0
            AND
            SUM(CASE 
                    WHEN ThanhtienTC < 0 
                         AND NOT (
                             TenWebsite_Treo_Lower = Website_Treo_Standard_Lower 
                             AND TenWebsite_TC_Lower = Website_TC_Standard_Lower
                         )
                    THEN 1 ELSE 0 END
                ) > 0
    )

    SELECT 
        SoHopDong,
        HopDongChiTietID,
        ThucChayHopDongChiTietID,
        DotChayBooking_Int AS DotChayBooking,
        TenWebsite_HD,
        DmWebsiteREF,
        TenWebsite_Treo,
        TenWebsite_TC,
        ThanhtienTC,
        CASE
            WHEN 
                TenWebsite_Treo_Lower = Website_Treo_Standard_Lower
                AND TenWebsite_TC_Lower = Website_TC_Standard_Lower
            THEN N'✅ Khớp theo chuẩn bảng WEBSITES'
            ELSE N'❌ Không khớp bảng WEBSITES'
        END AS GhiChu
    FROM MERGED_CLEANED
    WHERE 
        ThucChayHopDongChiTietID NOT IN (
            SELECT ThucChayHopDongChiTietID FROM ID_CAN_XOA
        )
        AND NOT (
            TenWebsite_Treo_Lower = Website_Treo_Standard_Lower
            AND TenWebsite_TC_Lower = Website_TC_Standard_Lower
        )
        AND TenWebsite_Treo_Lower <> TenWebsite_TC_Lower;

END

```
