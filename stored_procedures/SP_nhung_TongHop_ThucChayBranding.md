# Stored Procedure: `nhung_TongHop_ThucChayBranding`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 17:08:23.570000
- **Ngày sửa cuối**: 2026-03-25 10:45:56.200000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_TongHop_ThucChayBranding
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;

    ;WITH TT AS (
        SELECT
            tt.HopDongChiTietREF,
            tt.DmBannerREF,
            hdct.DonViTinhREF,
			tt.DmDonViTinhREF,
			hdct.DmSanPhamREF AS DmSanPhamREFHD ,
            MAX(tt.DmSanPhamREF)                   AS DmSanPhamREF,
            SUM(ISNULL(tt.SoLuongThucTreo,0))      AS SoLuongThucTreo,
            MAX(ISNULL(hdct.DonGia,0))             AS DonGia,
			MAX(ISNULL(tt.DonGia,0))             AS DonGiatreo,
            MAX(ISNULL(hdct.ChietKhau,0))          AS ChietKhau
        FROM dbo.ThucChayHopDongChiTiet tt
        INNER JOIN dbo.HopDongChiTiet hdct
            ON tt.HopDongChiTietREF = hdct.HopDongChiTietID
        WHERE tt.DeletedStatus = 0
          AND tt.HopDongChiTietREF = @HopDongChiTietID
        GROUP BY
            tt.HopDongChiTietREF,
            tt.DmBannerREF,
            hdct.DonViTinhREF,
			tt.DmDonViTinhREF,
			hdct.DmSanPhamREF
    ),

    TC AS (
        SELECT
            t.DmBannerREF,
            SUM(ISNULL(t.TongViewThucChay,0))  AS TongViewThucChay,
            SUM(ISNULL(t.TongClickThucChay,0)) AS TongClickThucChay
        FROM dbo.ThucChay t
        WHERE t.DmBannerREF IN (
            SELECT DmBannerREF
            FROM dbo.ThucChayHopDongChiTiet
            WHERE DeletedStatus = 0
              AND HopDongChiTietREF = @HopDongChiTietID
        )
        GROUP BY t.DmBannerREF
    ),

    NA AS (
        SELECT
            n.DmBannerID,
            SUM(ISNULL(n.SoLuongThucChay,0))        AS SoLuongThucChay,
			SUM(ISNULL(n.SoLuongThucChayKM,0))        AS SoLuongKM,
            SUM(ISNULL(n.ThanhTienThucChaySauCK,0)) AS ThanhTienThucChaySauCK,
            SUM(ISNULL(n.ThanhTienThucChayKM,0))    AS ThanhTienKM
        FROM dbo.ThucChay_Native_Ads n
        WHERE n.DmBannerID IN (
            SELECT DmBannerREF
            FROM dbo.ThucChayHopDongChiTiet
            WHERE DeletedStatus = 0
              AND HopDongChiTietREF = @HopDongChiTietID
        )
        GROUP BY n.DmBannerID
    ),

	TCDT AS (
        SELECT DmBannerREF
		,SUM(SoLuongThucChay+SoLuongThayDoi) AS SoLuongTC
		,SUM(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi) AS ThanhtienTC
		,SUM(SoLuongThucChayKM+SoLuongKMThayDoi) AS SoLuongKM
		,SUM(ThanhTienKM+GiaTriKMThayDoi) AS ThanhtienKM
		FROM dbo.ThucChayDaTinh 
		WHERE HopDongChiTietREF= @HopDongChiTietID
		GROUP BY DmBannerREF
    ),

    DATA_NUM AS (
        SELECT
            CAST(tt.DmBannerREF AS NVARCHAR(50)) AS DmBannerREF,
            tt.DmSanPhamREF,
			CASE WHEN tt.DmSanPhamREFHD = 733 then tt.DmDonViTinhREF ELSE tt.DonViTinhREF END AS DonViTinhREF,
            tt.SoLuongThucTreo,            
			CASE WHEN tt.DmSanPhamREFHD = 733 then tt.DonGiatreo ELSE tt.DonGia END AS DonGia ,            
			tt.ChietKhau,
            ISNULL(tc.TongViewThucChay,0)       AS TongViewThucChay,
            ISNULL(tc.TongClickThucChay,0)      AS TongClickThucChay,
            ISNULL(na.SoLuongThucChay,0)        AS SoLuongThucChay,
            ISNULL(na.ThanhTienThucChaySauCK,0) AS ThanhTienThucChaySauCK,
			CASE WHEN tt.ChietKhau = 100 then tcdt.SoLuongKM ELSE tcdt.SoLuongTC END AS soluongTC_ASD,
			CASE WHEN tt.ChietKhau = 100 then tcdt.ThanhtienKM ELSE tcdt.ThanhtienTC END AS thanhtienTC_ASD,

			CASE 
                WHEN tt.DonViTinhREF = 1 AND tt.DmSanPhamREF NOT IN (821,5133,733) THEN ISNULL(tc.TongViewThucChay,0) 
                WHEN tt.DonViTinhREF = 2 AND tt.DmSanPhamREF NOT IN (821,5133,733) THEN ISNULL(tc.TongClickThucChay,0)
				---phân bổ ký Native as / Onimages
                WHEN tt.ChietKhau = 100 AND tt.DmSanPhamREF IN (821,5133) THEN ISNULL(na.SoLuongKM,0)
				WHEN tt.ChietKhau <> 100 AND tt.DmSanPhamREF IN (821,5133) THEN ISNULL(na.SoLuongThucChay,0)
				---phân bổ ký gói
				WHEN tt.DmDonViTinhREF = 1 AND tt.DmSanPhamREFHD = 733 THEN ISNULL(tc.TongViewThucChay,0) 
                WHEN tt.DmDonViTinhREF = 2 AND tt.DmSanPhamREFHD = 733 THEN ISNULL(tc.TongClickThucChay,0) 			
                ELSE 
                    0
            END AS SoluongTC_SP,

            CASE 
                WHEN tt.DonViTinhREF = 1 AND tt.DmSanPhamREF NOT IN (821,5133,733) THEN 
                    ISNULL(tc.TongViewThucChay,0) * tt.DonGia / 1000.0 * (100 - tt.ChietKhau) / 100.0
                WHEN tt.DonViTinhREF = 2 AND tt.DmSanPhamREF NOT IN (821,5133,733) THEN 
                    ISNULL(tc.TongClickThucChay,0) * tt.DonGia * (100 - tt.ChietKhau) / 100.0
				---phân bổ ký Native as / Onimages
                WHEN tt.ChietKhau = 100 AND tt.DmSanPhamREF IN (821,5133) THEN 
                    ISNULL(na.ThanhTienKM,0)
				WHEN tt.ChietKhau <> 100 AND tt.DmSanPhamREF IN (821,5133) THEN 
                    ISNULL(na.ThanhTienThucChaySauCK,0)
				---phân bổ ký gói
				WHEN tt.DmDonViTinhREF = 1 AND tt.DmSanPhamREFHD = 733 THEN 
                    ISNULL(tc.TongViewThucChay,0) * tt.DonGiatreo / 1000.0 * (100 - tt.ChietKhau) / 100.0
                WHEN tt.DmDonViTinhREF = 2 AND tt.DmSanPhamREFHD = 733 THEN 
                    ISNULL(tc.TongClickThucChay,0) * tt.DonGiatreo * (100 - tt.ChietKhau) / 100.0				
                ELSE 
                    0
            END AS ThanhtienTC_SP
        FROM TT tt
        LEFT JOIN TC tc ON tc.DmBannerREF = tt.DmBannerREF
        LEFT JOIN NA na ON na.DmBannerID = tt.DmBannerREF
		LEFT JOIN TCDT tcdt ON tt.DmBannerREF = tcdt.DmBannerREF
    ),

    FINAL AS (
        -- Chi tiết
        SELECT
            0 AS SortKey,
            DmBannerREF,
            DmSanPhamREF,
            DonViTinhREF,
            SoLuongThucTreo,
            DonGia,
            ChietKhau,
            TongViewThucChay,
            TongClickThucChay,
            SoLuongThucChay,
            ThanhTienThucChaySauCK,
			SoluongTC_SP,
            ThanhtienTC_SP,
			DATA_NUM.soluongTC_ASD,
			DATA_NUM.thanhtienTC_ASD
		FROM DATA_NUM

        UNION ALL

        -- Tổng
        SELECT
            1,
            N'TỔNG',
            NULL,
            NULL,
            SUM(SoLuongThucTreo),
            NULL,
            NULL,
            SUM(TongViewThucChay),
            SUM(TongClickThucChay),
            SUM(SoLuongThucChay),
            SUM(ThanhTienThucChaySauCK),
			Sum(SoluongTC_SP),
            SUM(ThanhtienTC_SP),
			SUM(soluongTC_ASD),
            SUM(thanhtienTC_ASD)
        FROM DATA_NUM
    )

    SELECT
        DmBannerREF,
        DmSanPhamREF,
        DonViTinhREF,
       -- dbo.FormatNumber(SoLuongThucTreo)        AS SoLuongThucTreo,
        dbo.FormatNumber(DonGia) AS DonGia,
        ChietKhau,
        --dbo.FormatNumber(TongViewThucChay)       AS TongView,
        --dbo.FormatNumber(TongClickThucChay)      AS TongClick,
        --dbo.FormatNumber(SoLuongThucChay)        AS SoLuongThucChay,
        --dbo.FormatNumber(ThanhTienThucChaySauCK) AS ThanhTienThucChaySauCK,
		dbo.FormatNumber(SoluongTC_SP) AS SoluongTC_SP,
        dbo.FormatNumber(ThanhtienTC_SP)         AS ThanhtienTC_SP,
		dbo.FormatNumber(soluongTC_ASD) AS soluongTC_ASD,
        dbo.FormatNumber(thanhtienTC_ASD)         AS thanhtienTC_ASD,
		dbo.FormatNumber(SoluongTC_SP - soluongTC_ASD) AS LechSLSP_ASD,
		dbo.FormatNumber(ThanhtienTC_SP - thanhtienTC_ASD) AS LechTienSP_ASD
    FROM FINAL
    ORDER BY SortKey, DmBannerREF;

END

```
