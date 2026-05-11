# Stored Procedure: `nhung_TongTCDT_Muangoai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 17:35:58.020000
- **Ngày sửa cuối**: 2026-03-06 17:35:58.020000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[nhung_TongTCDT_Muangoai]
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

;WITH
HD AS (
    SELECT
        HopDongChiTietID,
        ChietKhau,
        CASE
            WHEN ChietKhau = 100 THEN SoLuong * DonGia
            ELSE ThanhTien
        END AS ThanhtienHD_raw
    FROM dbo.HopDongChiTiet
    WHERE HopDongChiTietID = @HopDongChiTietID
      AND DeletedStatus = 0
),
MUA AS (
    SELECT
        HopDongChiTietREF,
        SUM(ThanhTienThucChayBanSauCK) AS ThanhTienThucChayBanSauCK_raw,
        SUM(ThanhTienMuaNgoaiTruocCK * (100 - ChietKhauMuaNgoai) / 100) AS MuaSauCK_raw,
        SUM(ThanhTienLaiThucChaySauCK) AS Lai_raw
    FROM dbo.ThucChayMuaNgoaiChiTiet
    WHERE DeletedStatus = 0
      AND HopDongChiTietREF = @HopDongChiTietID
    GROUP BY HopDongChiTietREF
),
TC AS (
    SELECT
        HopDongChiTietREF,
        SUM(SoLuongThucChay + SoLuongThayDoi) AS soluongTC_raw,
        SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS ThanhtienTC_raw,
        SUM(SoLuongThucChayKM + SoLuongKMThayDoi) AS soluongKM_raw,
        SUM(ThanhTienKM + GiaTriKMThayDoi) AS ThanhtienKM_raw
    FROM dbo.ThucChayDaTinh
    WHERE HopDongChiTietREF = @HopDongChiTietID
    GROUP BY HopDongChiTietREF
),
LN AS (
    SELECT
        HopDongChiTietREF,
        SUM(ThanhTienLaiThucChaySauCK + GiaTriThayDoiLaiSauCK) AS Thanhtienlai_raw,
        SUM(ThanhTienLaiThucChayKM + GiaTriKMLaiThayDoi) AS ThanhtienKMlai_raw
    FROM dbo.ThucChayDaTinh_MuaNgoai
    WHERE HopDongChiTietREF = @HopDongChiTietID
    GROUP BY HopDongChiTietREF
)
SELECT
    HD.HopDongChiTietID,
    HD.ChietKhau,
    dbo.FormatNumber(HD.ThanhtienHD_raw) AS ThanhtienHD,

    dbo.FormatNumber(ISNULL(MUA.ThanhTienThucChayBanSauCK_raw, 0)) AS ThanhtienBan_SP,
    dbo.FormatNumber(ISNULL(MUA.MuaSauCK_raw, 0)) AS ThanhtienMua_SP,
    dbo.FormatNumber(ISNULL(MUA.Lai_raw, 0)) AS Lai_SP,

    CASE WHEN HD.ChietKhau = 100 THEN dbo.FormatNumber(ISNULL(TC.soluongKM_raw, 0))
         ELSE dbo.FormatNumber(ISNULL(TC.soluongTC_raw, 0)) END AS soluong_ASD,

    CASE WHEN HD.ChietKhau = 100 THEN dbo.FormatNumber(ISNULL(TC.ThanhtienKM_raw, 0))
         ELSE dbo.FormatNumber(ISNULL(TC.ThanhtienTC_raw, 0)) END AS Thanhtien_ASD,

    CASE WHEN HD.ChietKhau = 100 THEN dbo.FormatNumber(ISNULL(LN.ThanhtienKMlai_raw, 0))
         ELSE dbo.FormatNumber(ISNULL(LN.Thanhtienlai_raw, 0)) END AS Lai_ASD,

    --dbo.FormatNumber(CA.ChenhLechSP_raw) AS ChenhLechTien_SP,
    --dbo.FormatNumber(CA.ChenhLechHD_raw) AS ChenhLechTien_HD,
    --dbo.FormatNumber(CA.ChenhLechLai_raw) AS ChenhLechLai,

    CONCAT(
        -- So sánh TIỀN (SP vs TC)
        CASE
            WHEN ROUND(CA.BanSauCK_raw, 0) = ROUND(CA.TC_raw, 0) THEN N'SP: Đủ tiền'
            WHEN ROUND(CA.BanSauCK_raw, 0) < ROUND(CA.TC_raw, 0) THEN CONCAT(N'SP: Thừa ', dbo.FormatNumber(CA.ChenhLechSP_raw))
            WHEN ROUND(CA.BanSauCK_raw, 0) > ROUND(CA.TC_raw, 0) THEN CONCAT(N'SP: Thiếu ', dbo.FormatNumber(CA.ChenhLechSP_raw))
            ELSE N'SP: N/A'
        END,
        N' | ',
        -- So sánh TIỀN (HĐ vs TC)
        CASE
            WHEN ROUND(HD.ThanhtienHD_raw, 0) = ROUND(CA.TC_raw, 0) THEN N'HĐ: Đủ tiền'
            WHEN ROUND(HD.ThanhtienHD_raw, 0) < ROUND(CA.TC_raw, 0) THEN CONCAT(N'HĐ: Vượt ', dbo.FormatNumber(CA.ChenhLechHD_raw))
            WHEN ROUND(HD.ThanhtienHD_raw, 0) > ROUND(CA.TC_raw, 0) THEN CONCAT(N'HĐ: Thiếu ', dbo.FormatNumber(CA.ChenhLechHD_raw))
            ELSE N'HĐ: N/A'
        END,
        N' | ',
        -- ✅ So sánh LÃI (Lai_SP vs Lai_TC)
        CASE
            WHEN ROUND(CA.LaiSP_raw, 0) = ROUND(CA.LaiTC_raw, 0) THEN N'Lãi: Khớp'
            WHEN ROUND(CA.LaiSP_raw, 0) < ROUND(CA.LaiTC_raw, 0) THEN CONCAT(N'Lãi: Thừa', dbo.FormatNumber(CA.ChenhLechLai_raw))
            WHEN ROUND(CA.LaiSP_raw, 0) > ROUND(CA.LaiTC_raw, 0) THEN CONCAT(N'Lãi: Thiếu ', dbo.FormatNumber(CA.ChenhLechLai_raw))
            ELSE N'Lãi: N/A'
        END
    ) AS ghichu
FROM HD
LEFT JOIN MUA ON MUA.HopDongChiTietREF = HD.HopDongChiTietID
LEFT JOIN TC  ON TC.HopDongChiTietREF  = HD.HopDongChiTietID
LEFT JOIN LN  ON LN.HopDongChiTietREF  = HD.HopDongChiTietID
CROSS APPLY (
    SELECT
        ISNULL(MUA.ThanhTienThucChayBanSauCK_raw, 0) AS BanSauCK_raw,

        -- TC_raw: CK=100 thì lấy KM, ngược lại lấy TC
        CASE WHEN HD.ChietKhau = 100 THEN ISNULL(TC.ThanhtienKM_raw, 0)
             ELSE ISNULL(TC.ThanhtienTC_raw, 0) END AS TC_raw,

        -- Chênh lệch tiền SP: TC_raw - BanSauCK
        CASE WHEN HD.ChietKhau = 100 THEN ISNULL(TC.ThanhtienKM_raw, 0) - ISNULL(MUA.ThanhTienThucChayBanSauCK_raw, 0)
             ELSE ISNULL(TC.ThanhtienTC_raw, 0) - ISNULL(MUA.ThanhTienThucChayBanSauCK_raw, 0) END AS ChenhLechSP_raw,

        -- Chênh lệch tiền HĐ: TC_raw - HĐ
        CASE WHEN HD.ChietKhau = 100 THEN ISNULL(TC.ThanhtienKM_raw, 0) - ISNULL(HD.ThanhtienHD_raw, 0)
             ELSE ISNULL(TC.ThanhtienTC_raw, 0) - ISNULL(HD.ThanhtienHD_raw, 0) END AS ChenhLechHD_raw,

        -- ✅ Lãi SP / Lãi TC và chênh lệch
        ISNULL(MUA.Lai_raw, 0) AS LaiSP_raw,
        CASE WHEN HD.ChietKhau = 100 THEN ISNULL(LN.ThanhtienKMlai_raw, 0)
             ELSE ISNULL(LN.Thanhtienlai_raw, 0) END AS LaiTC_raw,

        CASE WHEN HD.ChietKhau = 100 THEN ISNULL(LN.ThanhtienKMlai_raw, 0) - ISNULL(MUA.Lai_raw, 0)
             ELSE ISNULL(LN.Thanhtienlai_raw, 0) - ISNULL(MUA.Lai_raw, 0) END AS ChenhLechLai_raw
) CA;


END 

```
