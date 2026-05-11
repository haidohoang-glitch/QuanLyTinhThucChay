# Stored Procedure: `sp_nhung_KT_loiSP_Admatic_Bannerchuatreo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-20 09:38:53.217000
- **Ngày sửa cuối**: 2026-03-20 09:38:53.217000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_nhung_KT_loiSP_Admatic_Bannerchuatreo
AS
BEGIN
    SET NOCOUNT ON;
SELECT 
    Main.SoHopDong,
    N'Chưa treo' AS TrangThai,
    Main.NhanHopDong,
	-- Cột danh sách banner riêng lẻ (nếu cần nhìn nhanh)
    STUFF((
        SELECT ', ' + CAST(Sub.DmBannerREF AS NVARCHAR(MAX))
        FROM (
            SELECT tc2.SoHopDong, tc2.DmBannerID AS DmBannerREF
            FROM ThucChay_ThanhTien_Admatic tc2
            GROUP BY tc2.SoHopDong, tc2.DmBannerID
        ) Sub
        WHERE Sub.SoHopDong = Main.SoHopDong
        FOR XML PATH('')), 1, 2, '') AS DanhSachBanner,
    SUM(Main.SL_TC) AS Tong_SL_TC,
    dbo.FormatNumber(ROUND(SUM(Main.TT_TC), 0)) AS Tong_TT_TC,
    SUM(Main.SL_KM) AS Tong_SL_KM,
    dbo.FormatNumber(ROUND(SUM(Main.TT_KM), 0)) AS Tong_TT_KM,
    -- Cột Ghi chú để bạn copy gửi team
    N'Dear team check giúp mình SHĐ: ' + Main.SoHopDong + N' danh sách banner có thực chạy nhưng chưa treo: ' + 
    STUFF((
        SELECT ', ' + CAST(Sub.DmBannerREF AS NVARCHAR(MAX))
        FROM (
            SELECT tc2.SoHopDong, tc2.DmBannerID AS DmBannerREF
            FROM ThucChay_ThanhTien_Admatic tc2
            GROUP BY tc2.SoHopDong, tc2.DmBannerID
        ) Sub
        WHERE Sub.SoHopDong = Main.SoHopDong
        FOR XML PATH('')), 1, 2, '') AS GhiChu    
FROM (
    SELECT 
        A.SoHopDong, A.NhanHopDong, A.DmBannerREF, A.DmSanPhamREF,
        A.SL_TC, A.TT_TC, A.SL_KM, A.TT_KM
    FROM (
        SELECT 
            tc.SoHopDong, hd.NhanHopDong, tc.DmBannerID AS DmBannerREF, tc.DmSanPhamREF,
            SUM(tc.SoLuongThucChay) AS SL_TC, SUM(tc.ThanhTienThucChaySauCK_ChuaVAT) AS TT_TC,
            SUM(tc.SoLuongThucChayKM) AS SL_KM, SUM(tc.ThanhTienThucChayKM) AS TT_KM
        FROM ThucChay_ThanhTien_Admatic tc
        LEFT JOIN HopDong hd ON tc.SoHopDong = hd.SoHopDong
        WHERE tc.NgayThucHien >= '2021-01-01'
          AND hd.HopDongID IN (SELECT hdct.HopDongFK FROM dbo.HopDongChiTiet hdct WHERE NOT hdct.DonViTinhREF = 7)
          AND tc.SoHopDong NOT IN ('NB0340523', 'NB0350523', 'NB0180623', 'NB0190623', 'NB0200623', 'NB0250623','NB0300723', 'NB0310723', 'NB0330523', 'NB0160623', 'NB0280723', 'NB0220723')
        GROUP BY tc.SoHopDong, hd.NhanHopDong, tc.DmBannerID, tc.DmSanPhamREF
    ) A 
    LEFT JOIN (
        SELECT DISTINCT CONVERT(NVARCHAR(50), Banner_Id) AS DmBannerREF
        FROM [ASDAG2].ThucTreo.dbo.ThucTreo
        WHERE Product_Formality_Id = 42 AND Deleted_Status = 0 AND Contract_Detail_Id NOT IN (0, -1)
    ) B ON A.DmBannerREF = B.DmBannerREF
    WHERE B.DmBannerREF IS NULL
      AND A.DmBannerREF NOT IN ('80778', '89676', '88379', '88381', '84787')
      AND A.DmBannerREF NOT IN ('102036','102037','102038','102039','102040','102041','102042','102043','102044','102045','102046','101432','101433','101434','101435','101436','101437','101438','101439','101504','101505','101506','101541','101558','101559','101560','101575')
      AND NOT A.DmSanPhamREF IN (140, 549, 5312)
      AND A.SoHopDong NOT IN (SELECT Sohopdong FROM dbo.HopDong hd INNER JOIN dbo.HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK WHERE hdct.DmLoaiNenTangREF=9)
      AND A.SoHopDong NOT IN (SELECT Sohopdong FROM dbo.HopDong hd INNER JOIN dbo.HopDongChiTiet hdct ON hd.HopDongID = hdct.HopDongFK WHERE hdct.DonViTinhREF =7)
      AND NOT (A.SL_TC = 0 AND A.TT_TC = 0 AND A.SL_KM = 0 AND A.TT_KM = 0)
) Main
GROUP BY 
    Main.SoHopDong, 
    Main.NhanHopDong
ORDER BY 
    Main.SoHopDong;


END;
```
