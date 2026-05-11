# Stored Procedure: `nhung_TongTCDT_GGFB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-06 17:18:25.417000
- **Ngày sửa cuối**: 2026-03-06 17:18:25.417000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE nhung_TongTCDT_GGFB
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

SELECT
    HĐ.Sohopdong,
    HĐ.HopDongChiTietID,
    HĐ.TenSanPham,

    dbo.FormatNumber(HĐ.ThanhTienHĐ)      AS ThanhtienHD_Ky,
    dbo.FormatNumber(NS.NganSach)         AS NganSach_Order,

    dbo.FormatNumber(KQ.SoluongTC_SP)     AS SoluongTC_SP,
    dbo.FormatNumber(KQ.TongTienTC_BanSP) AS TongTienTC_BanSP,
    dbo.FormatNumber(KQ.TongTien_MuaSP)   AS TongTien_MuaSP,
    dbo.FormatNumber(KQ.LaiChenhLech)     AS LaiMM_SP,

    dbo.FormatNumber(X.TCMM_Num)          AS TCMM,

    dbo.FormatNumber(TCDT.SoluongTC)      AS SoluongTC_TCDT,
    dbo.FormatNumber(TCDT.ThanhtienTC)    AS ThanhtienTC_TCDT,

    dbo.FormatNumber(ASD.Lai_ASD)         AS Lai_TCDTMN,

    -- ✅ Ghi chú lãi
    CASE
        WHEN ROUND(ISNULL(KQ.LaiChenhLech,0),0) < ROUND(ISNULL(ASD.Lai_ASD,0),0)
            THEN CONCAT(N'Thừa tiền lãi: ',
                        dbo.FormatNumber(ROUND(ISNULL(ASD.Lai_ASD,0) - ISNULL(KQ.LaiChenhLech,0),0)))
        WHEN ROUND(ISNULL(KQ.LaiChenhLech,0),0) > ROUND(ISNULL(ASD.Lai_ASD,0),0)
            THEN CONCAT(N'Thiếu tiền lãi: ',
                        dbo.FormatNumber(ROUND(ISNULL(KQ.LaiChenhLech,0) - ISNULL(ASD.Lai_ASD,0),0)))
        WHEN ROUND(ISNULL(KQ.LaiChenhLech,0),0) = ROUND(ISNULL(ASD.Lai_ASD,0),0)
            THEN N'Đủ tiền lãi'
        ELSE N''
    END AS Ghichu_Lai,

    -- ✅ Ghi chú tiền TC (TCMM vs TCDT)
    CASE
        WHEN ROUND(ISNULL(X.TCMM_Num,0),0) < ROUND(ISNULL(TCDT.ThanhtienTC,0),0)
            THEN CONCAT(N'Thừa tiền TC: ',
                        dbo.FormatNumber(ROUND(ISNULL(TCDT.ThanhtienTC,0) - ISNULL(X.TCMM_Num,0),0)))
        WHEN ROUND(ISNULL(X.TCMM_Num,0),0) > ROUND(ISNULL(TCDT.ThanhtienTC,0),0)
            THEN CONCAT(N'Thiếu tiền TC: ',
                        dbo.FormatNumber(ROUND(ISNULL(X.TCMM_Num,0) - ISNULL(TCDT.ThanhtienTC,0),0)))
        WHEN ROUND(ISNULL(X.TCMM_Num,0),0) = ROUND(ISNULL(TCDT.ThanhtienTC,0),0)
            THEN N'Đủ tiền vs SP'
		WHEN ROUND(ISNULL(HĐ.ThanhTienHĐ,0),0) > ROUND(ISNULL(TCDT.ThanhtienTC,0),0)
            THEN CONCAT(N'Vượt tiền HĐ ký: ',
                        dbo.FormatNumber(ROUND(ISNULL(HĐ.ThanhTienHĐ,0) - ISNULL(TCDT.ThanhtienTC,0),0)))
        ELSE N''
    END AS GhichuTC

FROM
-- 1️⃣ HĐ ký
(
    SELECT
        dbo.GetSoHopDongByID(HopDongFK) AS Sohopdong,
        HopDongChiTietID,
        TenSanPham,
        ThanhTien AS ThanhTienHĐ
    FROM dbo.HopDongChiTiet
    WHERE HopDongChiTietID = @HopDongChiTietID
      AND DeletedStatus = 0
) HĐ

CROSS JOIN
-- 2️⃣ Ngân sách order
(
    SELECT SUM(Money_Turnover) AS NganSach
    FROM dbo.ADS_Operating_Order
    WHERE Contract_Detail_Id = @HopDongChiTietID
      AND IsDeleted = 0
) NS

CROSS JOIN
-- 3️⃣ Thực chạy bán (SP/ADS)
(
    SELECT
        SUM(TC.Result) AS SoluongTC_SP,
        SUM(TC.Sell_Money_VND) AS TongTienTC_BanSP,
        SUM(TCC.Total_Money_VND) AS TongTien_MuaSP,
        SUM(TC.Sell_Money_VND - TCC.Total_Money_VND) AS LaiChenhLech
    FROM dbo.ADS_Operating_Result_Map_Order TC
    INNER JOIN dbo.ADS_Operating_Order OD
        ON TC.Operating_Order_Id = OD.Id
    INNER JOIN dbo.ADS_Operating_Result TCC
        ON TC.operating_Result_Id = TCC.ID
    WHERE OD.Contract_Detail_Id = @HopDongChiTietID
) KQ

CROSS JOIN
-- 4️⃣ TCDT
(
    SELECT
        SUM(SoLuongThucChay + SoLuongThayDoi) AS SoluongTC,
        SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS ThanhtienTC
    FROM dbo.ThucChayDaTinh
    WHERE HopDongChiTietREF = @HopDongChiTietID
) TCDT

CROSS JOIN
-- 5️⃣ Lãi ASD (mua ngoài)
(
    SELECT
        SUM(ISNULL(ThanhTienLaiThucChaySauCK,0) + ISNULL(GiaTriThayDoiLaiSauCK,0)) AS Lai_ASD
    FROM dbo.ThucChayDaTinh_MuaNgoai
    WHERE HopDongChiTietREF = @HopDongChiTietID
) ASD

-- ✅ 6️⃣ Tính TCMM (PHẢI dùng CROSS APPLY để dùng được NS/KQ)
CROSS APPLY (
    SELECT
        CASE
            WHEN ISNULL(KQ.TongTienTC_BanSP,0) < ISNULL(NS.NganSach,0)
                THEN ISNULL(KQ.TongTienTC_BanSP,0)
            ELSE ISNULL(NS.NganSach,0)
        END AS TCMM_Num
) X;



END

```
