# Stored Procedure: `sp_nhung_KT_hamtinh_Performance`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-26 10:27:22.507000
- **Ngày sửa cuối**: 2026-03-27 15:43:36.787000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `date(3)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[sp_nhung_KT_hamtinh_Performance]
    @NgayBatDau DATE
AS
BEGIN
    SET NOCOUNT ON;
	;WITH A AS (
    SELECT 
        SoHopDong,
        HopDongChiTietREF,
        CONVERT(DATE, NgayThucHien) AS NgayThucHien,
        SUM(TongThucchay_SP) AS TongThucchay_SP
    FROM (
        SELECT 
            CASE 
				WHEN contract_number = '' OR contract_number = 'Blank' THEN N'KHÔNG XÁC ĐỊNH'
				ELSE contract_number
			END AS SoHopDong,
            phanbo AS HopDongChiTietREF,
            NgayThucHien,
            SUM(CONVERT(FLOAT, domain_tt_money)) AS TongThucchay_SP
        FROM dbo.ThucChayAdmarket_PhanBo 
        WHERE NgayThucHien = @NgayBatDau
            AND DmSanPhamREF <> 817
		GROUP BY CASE 
            WHEN contract_number = '' OR contract_number = 'Blank' THEN N'KHÔNG XÁC ĐỊNH'
            ELSE contract_number
        END, phanbo, NgayThucHien

        UNION ALL

        SELECT 
            SoHopDong,
            HopDongChiTietREF,
            CreatedAt,
            SUM(SoTienThayDoi) AS SoTienThayDoi
        FROM dbo.ThucChay_PerformanceBase_ThayDoi 
        WHERE CONVERT(DATE, CreatedAt) = @NgayBatDau
            AND DmSanPhamREF <> 817
		GROUP BY SoHopDong,
            HopDongChiTietREF,
            CreatedAt
    ) t
    GROUP BY SoHopDong, HopDongChiTietREF, CONVERT(DATE, NgayThucHien)
),

B AS (
    SELECT 
        SoHopDong,
        HopDongChiTietREF,
        CONVERT(DATE, NgayThucHien) AS NgayThucHien,
        SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS TongThucchay_ASD
    FROM dbo.ThucChayDaTinhAdmarket 
    WHERE CONVERT(DATE, NgayThucHien) = @NgayBatDau
        AND DmHinhThucQuangCao <> 42
		AND NOT (SoHopDong LIKE N'Blank' OR SoHopDong ='' OR HopDongChiTietREF = 0)
    GROUP BY SoHopDong, HopDongChiTietREF, CONVERT(DATE, NgayThucHien)
),

F AS (
    SELECT 
        SoLuongDotChayHD,
        SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS thanhtienonline
    FROM dbo.ThucChayDaTinhAdmarket
    WHERE CONVERT(DATE, NgayThucHien) = @NgayBatDau
        AND (GhiChu LIKE N'%Thuc_Chay_Admarket_PhanBo_online%' OR  GhiChu LIKE N'%trừ vào online%')
		AND SoLuongDotChayHD >1
    GROUP BY SoLuongDotChayHD
),

ONLINE AS (
    SELECT 
        CASE 
            WHEN SoHopDong = '' OR SoHopDong = 'Blank' OR SoHopDong = '-' THEN N'KHÔNG XÁC ĐỊNH'
            ELSE SoHopDong
        END AS SoHopDong,
        SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS OnlineNoSHD
    FROM dbo.ThucChayDaTinhAdmarket 
    WHERE CONVERT(DATE, NgayThucHien) = @NgayBatDau
        AND DotChayHopDong LIKE N'%online%'
        AND DotChayHopDong LIKE N'%online%' AND SoLuongDotChayHD = 0
    GROUP BY SoHopDong
),

DATA AS (
    SELECT 
        A.SoHopDong,
        A.HopDongChiTietREF,

        ISNULL(B.TongThucchay_ASD,0) AS Thucchay_ASD,
        ISNULL(F.thanhtienonline,0) AS OnlinePB_ASD,
        ISNULL(O.OnlineNoSHD,0) AS Online_NoSHD,

        ISNULL(B.TongThucchay_ASD,0) 
        + ISNULL(F.thanhtienonline,0)
        + ISNULL(O.OnlineNoSHD,0) AS Tongtien_ASD,

        A.TongThucchay_SP,

        A.TongThucchay_SP 
        - (
            ISNULL(B.TongThucchay_ASD,0) 
            + ISNULL(F.thanhtienonline,0)
            + ISNULL(O.OnlineNoSHD,0)
        ) AS chenhlech

    FROM A
    LEFT JOIN B 
        ON A.HopDongChiTietREF = B.HopDongChiTietREF
        AND A.NgayThucHien = B.NgayThucHien

    LEFT JOIN F 
        ON A.HopDongChiTietREF = F.SoLuongDotChayHD

    LEFT JOIN ONLINE O 
        ON A.SoHopDong = O.SoHopDong
)

-- =========================
-- DATA + DÒNG TỔNG
-- =========================
SELECT 
    SoHopDong,
    HopDongChiTietREF,
    dbo.FormatNumber(Thucchay_ASD) AS Thucchay_ASD,
    dbo.FormatNumber(OnlinePB_ASD) AS OnlinePB_ASD,
    dbo.FormatNumber(Online_NoSHD) AS Online_NoSHD,
    dbo.FormatNumber(Tongtien_ASD) AS Tongtien_ASD,
    dbo.FormatNumber(TongThucchay_SP) AS TongThucchay_SP,
    dbo.FormatNumber(chenhlech) AS chenhlech,
	CASE 
        WHEN chenhlech > 0 THEN N'Chưa ghi nhận đủ tiền SP'
        WHEN chenhlech < 0 THEN N'ASD đang ghi nhận dư'
        ELSE N'Khớp'
    END AS GhiChu
		
FROM DATA
WHERE chenhlech <> 0 

UNION ALL

-- 🔥 DÒNG TỔNG
SELECT 
    N'TỔNG',
    NULL,
    dbo.FormatNumber(SUM(Thucchay_ASD)),
    dbo.FormatNumber(SUM(OnlinePB_ASD)),
    dbo.FormatNumber(SUM(Online_NoSHD)),
    dbo.FormatNumber(SUM(Tongtien_ASD)),
    dbo.FormatNumber(SUM(TongThucchay_SP)),
    dbo.FormatNumber(SUM(chenhlech)),
	NULL
FROM DATA
--WHERE chenhlech <> 0 
END

```
