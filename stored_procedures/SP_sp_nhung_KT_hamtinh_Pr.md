# Stored Procedure: `sp_nhung_KT_hamtinh_Pr`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-20 09:26:25.477000
- **Ngày sửa cuối**: 2026-03-20 09:26:25.477000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_nhung_KT_hamtinh_Pr
AS
BEGIN
    SET NOCOUNT ON;
-- ===============================================
-- 📌 Kiểm tra sự chênh lệch giữa PR, HĐ và DaTinh
-- ===============================================
WITH PR_CLEAN AS (
    SELECT 
        hd.SoHopDong,
        hd.HopDongID,
        hdct.DmSanPhamREF,
        hdct.HopDongChiTietID,
        hdct.SoLuong AS Soluong_HĐ,
        hdct.ThanhTien AS Thanhtien_HĐ,
        CASE WHEN hdct.ChietKhau = 100 THEN hdct.SoLuong * hdct.DonGia ELSE 0 END AS Thanhtien_KM_HĐ,
        tt.ThucChayHopDongChiTietPRID,
        tt.SoLuong,
        tt.GiaTien,
        hdct.ChietKhau,
        hdct.DonGia AS DongiaHĐ,
        CASE 
            WHEN tt.DeletedStatus = 0 THEN (CONVERT(FLOAT, tt.GiaTien) * tt.SoLuong * (100 - tt.ChietKhau) / 100)
            ELSE 0 
        END AS TTSauCk,
        CASE WHEN tt.ChietKhau = 100 THEN CONVERT(FLOAT, tt.GiaTien) * tt.SoLuong ELSE 0 END AS TT_KM,
        tt.Link,
        tt.ThucChayHopDongChiTietPrREF AS ttid_cha,
        hdct.DonViTinhREF,
        tt.GiaTien AS DongiaTreo,
        tt.DmHinhThucQuangCaoREF
    FROM dbo.ThucChayHopDongChiTietPR tt
    INNER JOIN dbo.HopDongChiTiet hdct ON hdct.HopDongChiTietID = tt.HopDongChiTietREF
    INNER JOIN dbo.HopDong hd ON hd.HopDongID = hdct.HopDongFK
    WHERE 
        hd.TrangThaiHopDong <> 3
        AND hdct.DeletedStatus = 0
        AND hd.Nam >= 2024
        AND hdct.DmSanPhamREF IN (141, 637, 305)
        AND NOT (hdct.DmLoaiREF = 13 OR hdct.DmLoaiBannerREF = 18)
        AND tt.DeletedStatus = 0
        AND tt.ThucChayHopDongChiTietPRID NOT IN (
            -- 👇 Danh sách PRID bỏ qua
            '768359','777070','768947','706580','705079','713681','705559','706580','706954','707019','737733','737735',
            '707018','705355','706953','705078','699746','703068','703090','703286','703721','704770','704900','709355',
            '709397','710025','713658','713663','710654','708602','708614','708910','709147','709395','710637','710690',
            '747742','752027','752253','752745','752746','759245','759617','760014','760016','761067','765982','768580',
            '774700','778722','786584','792592','793620','769049','737698','737814','737869','739679','739681','740677',
            '740702','729874','731049','732337','737818','740944','741260','741307','741310','740592','744784','744883',
            '744948','744977','745038','745042','745189','745848','745850','765958','744289','747136','747138','754815',
            '759791','760276','760306','760871','770552','765263','765369','803197','793176','793626','787134'
        )
),
CK_TREO AS (
    SELECT HopDongChiTietREF, AVG(CAST(ChietKhau AS FLOAT)) AS ChietKhauTreo
    FROM dbo.ThucChayHopDongChiTietPR
    WHERE DeletedStatus = 0
    GROUP BY HopDongChiTietREF
),
DA_TINH_DETAIL AS (
    SELECT 
        HopDongID,
        DmSanPhamREF AS DmSanPhamREF_tcdt,
        DotChayBooking,
        SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS tc,
        SUM(ThanhTienKM + GiaTriKMThayDoi) AS tc_km
    FROM dbo.ThucChayDaTinh
    WHERE 
        DmSanPhamREF IN (141, 637, 305)
        AND NOT (DmLoaiBannerREF = 18 OR DmHinhThucQuangCao = 13)
    GROUP BY HopDongID, DmSanPhamREF, DotChayBooking
    HAVING 
        ROUND(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi), 0) <> 0
        OR ROUND(SUM(ThanhTienKM + GiaTriKMThayDoi), 0) <> 0
),
DA_TINH_TONG AS (
    SELECT 
        HopDongChiTietREF,
        SUM(SoLuongThucChay + SoLuongThayDoi) AS sltc_ASD,
        SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS tcdt_ASD,
        SUM(SoLuongThucChayKM + SoLuongKMThayDoi) AS sltckm_ASD,
        SUM(ThanhTienKM + GiaTriKMThayDoi) AS tckm_ASD
    FROM dbo.ThucChayDaTinh
    GROUP BY HopDongChiTietREF
),
TONG_TREO AS (
    SELECT 
        HopDongChiTietREF,
        SUM(SoLuong) AS Soluong_treo,
        SUM(CONVERT(FLOAT, GiaTien) * SoLuong * (100 - ChietKhau) / 100) AS Tong_Thanhtien_treo_TC,
        SUM(CONVERT(FLOAT, GiaTien) * SoLuong) AS Tong_Thanhtien_Treo_KM
    FROM dbo.ThucChayHopDongChiTietPR
    WHERE DeletedStatus = 0
    GROUP BY HopDongChiTietREF
),
E AS (
    SELECT 
        A.*,
        ck.ChietKhauTreo,
        B.tc,
        B.tc_km,
        D.Soluong_treo,
        D.Tong_Thanhtien_treo_TC,
        D.Tong_Thanhtien_Treo_KM
    FROM PR_CLEAN A
    LEFT JOIN CK_TREO ck ON A.HopDongChiTietID = ck.HopDongChiTietREF
    LEFT JOIN DA_TINH_DETAIL B ON 
        A.HopDongID = B.HopDongID 
        AND A.DmSanPhamREF = B.DmSanPhamREF_tcdt
        AND CONVERT(NVARCHAR(100), A.ThucChayHopDongChiTietPRID) = B.DotChayBooking
    INNER JOIN TONG_TREO D ON A.HopDongChiTietID = D.HopDongChiTietREF
    WHERE 
        (ABS(ISNULL(A.TTSauCk,0) - ISNULL(B.tc,0)) > 10)
        OR (ABS(ISNULL(A.TT_KM,0) - ISNULL(B.tc_km,0)) > 10)
),
KQ AS (
    SELECT         
        E.SoHopDong, E.HopDongID, E.DmSanPhamREF, E.HopDongChiTietID, 
        E.ThucChayHopDongChiTietPRID, E.SoLuong, E.GiaTien, E.ChietKhau, 
        E.ChietKhauTreo, E.TTSauCk, E.TT_KM, E.Link, E.ttid_cha, E.DonViTinhREF,
        E.DongiaHĐ, E.DongiaTreo, E.Soluong_HĐ, E.Thanhtien_HĐ, E.Thanhtien_KM_HĐ,
        E.Soluong_treo, E.Tong_Thanhtien_treo_TC, E.Tong_Thanhtien_Treo_KM,
        F.sltc_ASD, F.tcdt_ASD, F.sltckm_ASD, F.tckm_ASD,
        E.DmHinhThucQuangCaoREF,
        CASE 
            WHEN E.DmHinhThucQuangCaoREF IS NULL THEN 
                N'⚠️ Thiếu hình thức quảng cáo - chưa thể kiểm tra chính xác'
            WHEN E.ChietKhau <> E.ChietKhauTreo THEN 
                CONCAT(N'PB ', E.HopDongChiTietID, N' có chiết khấu treo ', E.ChietKhauTreo, N'% khác với chiết khấu HĐ ', E.ChietKhau, N'%')
            WHEN E.ChietKhau <> 100 AND E.DonViTinhREF = 10 AND (ISNULL(F.tcdt_ASD,0) + ISNULL(E.TTSauCk,0)) > E.Thanhtien_HĐ THEN 
                CONCAT(N'PB ', E.HopDongChiTietID, N' ký ', dbo.FormatNumber(E.Thanhtien_HĐ), N' nhưng tổng tiền treo ', dbo.FormatNumber(E.Tong_Thanhtien_treo_TC))
            WHEN E.ChietKhau <> 100 AND E.DonViTinhREF <> 10 AND (ISNULL(F.sltc_ASD,0) + E.SoLuong) > E.Soluong_HĐ THEN 
                CONCAT(N'PB ', E.HopDongChiTietID, N' ký SL HĐ ', E.Soluong_HĐ, N' nhưng tổng SL treo ', E.Soluong_treo)
            WHEN E.ChietKhau = 100 AND E.DonViTinhREF = 10 AND (ISNULL(F.tckm_ASD,0) + ISNULL(E.TT_KM,0)) > E.Thanhtien_KM_HĐ THEN 
                CONCAT(N'PB ', E.HopDongChiTietID, N' ký ', dbo.FormatNumber(E.Thanhtien_KM_HĐ), N' nhưng tổng tiền treo ', dbo.FormatNumber(E.Tong_Thanhtien_Treo_KM))
            WHEN E.ChietKhau = 100 AND E.DonViTinhREF <> 10 AND (ISNULL(F.sltckm_ASD,0) + E.SoLuong) > E.Soluong_HĐ THEN 
                CONCAT(N'PB ', E.HopDongChiTietID, N' ký ', E.Soluong_HĐ, N' nhưng tổng SL treo ', E.Soluong_treo)
            WHEN E.DonViTinhREF <> 10 AND (E.DongiaHĐ - E.DongiaTreo) <> 0 THEN 
                CONCAT(N'PB ', E.HopDongChiTietID, N' ký DG ', dbo.FormatNumber(E.DongiaHĐ), N' nhưng tổng DG treo ', dbo.FormatNumber(E.DongiaTreo))
            WHEN (ISNULL(F.tcdt_ASD,0) + ISNULL(E.TTSauCk,0)) <= E.Thanhtien_HĐ OR 
                 (ISNULL(F.tckm_ASD,0) + ISNULL(E.TT_KM,0)) <= ISNULL(E.Thanhtien_KM_HĐ,0) THEN 
                N'1.Chưa được tính - Bị tính thiếu'
            ELSE 
                N'2.Chưa xác định'
        END AS Note
    FROM E
    LEFT JOIN DA_TINH_TONG F ON E.HopDongChiTietID = F.HopDongChiTietREF
)

-- Bước 8: Lọc các bản ghi cần kiểm tra
SELECT *
FROM KQ
WHERE Note IN (
    N'1.Chưa được tính - Bị tính thiếu',
    N'2.Chưa xác định'
   -- N'⚠️ Thiếu hình thức quảng cáo - chưa thể kiểm tra chính xác'
)
ORDER BY ChietKhau, Note;


END;
```
