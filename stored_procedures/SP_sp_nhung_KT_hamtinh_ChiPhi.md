# Stored Procedure: `sp_nhung_KT_hamtinh_ChiPhi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-20 09:09:49.303000
- **Ngày sửa cuối**: 2026-03-20 09:09:49.303000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_nhung_KT_hamtinh_ChiPhi
AS
BEGIN
    SET NOCOUNT ON;

    -- ======================
    -- 📌 CTE 1: Dữ liệu treo theo Hợp đồng chi tiết
    -- ======================
    WITH TreoCTE AS
    (
        SELECT 
            tt.HopDongChiTietREF,
            SUM(tt.SoLuongThucTreo) AS SoLuongThucTreo,

            SUM
            (
                CASE 
                    WHEN hdct.ChietKhau = 100 
                        THEN tt.SoLuongThucTreo * tt.DonGia
                    ELSE tt.SoLuongThucTreo * tt.DonGia * (1 - hdct.ChietKhau / 100.0)
                END
            ) AS ThanhTien_treo

        FROM dbo.ThucChayHopDongChiTiet tt
        INNER JOIN dbo.HopDongChiTiet hdct
            ON tt.HopDongChiTietREF = hdct.HopDongChiTietID

        WHERE 
            tt.LoaiThucTreo LIKE N'%Chiphi%' 
            AND tt.DeletedStatus = 0
            AND tt.TrangThaiTreo = 2
            AND tt.DmSanPhamREF NOT IN (5184)
            AND CAST(tt.CreatedAt AS DATE) < CAST(GETDATE() AS DATE)

        GROUP BY 
            tt.HopDongChiTietREF
    ),

    -- ======================
    -- 📌 CTE 2: Thông tin HĐ gốc
    -- ======================
    HDCTE AS
    (
        SELECT 
            hd.SoHopDong,
            hdct.HopDongChiTietID,
            hdct.DmSanPhamREF,
            hdct.TenSanPham,
            hdct.SoLuong AS SoLuongHD,
            hdct.ChietKhau,
            hdct.DonGia,
            hd.CreatedAt,
            hdct.TenLoai,

            CASE 
                WHEN hdct.ChietKhau = 100 
                    THEN hdct.SoLuong * hdct.DonGia 
                ELSE hdct.ThanhTien 
            END AS ThanhTienHD

        FROM dbo.HopDongChiTiet hdct
        INNER JOIN dbo.HopDong hd
            ON hd.HopDongID = hdct.HopDongFK

        WHERE 
            hd.Nam >= 2023
            AND hdct.DeletedStatus = 0
            AND hdct.DmLoaiNenTangREF <> 9

            AND NOT 
            (
                hdct.DmSanPhamREF = 817
                AND hdct.TenLoai COLLATE SQL_Latin1_General_CP1_CI_AS LIKE '%Performance Base%'

                AND EXISTS 
                (
                    SELECT 1
                    FROM (VALUES
                        ('%Brand SAFETY%'),
                        ('%Content Insight%'),
                        ('%brand connection%'),
                        ('%Customize Segmention%')
                    ) AS pat(p)
                    WHERE hdct.TenBanner COLLATE SQL_Latin1_General_CP1_CI_AS LIKE pat.p
                )

                AND CONVERT(DATE, hd.CreatedAt) >= '2025-07-05'
            )

            AND hdct.DmSanPhamREF NOT IN 
            (
                141,140,585,549,240,339,370,342,613,423,306,144,375,628,598,
                228,381,241,385,733,735,564,720,722,680,821,637,305,5133,5056,
                624,5082,5184,5006,5151
            )
    ),

    -- ======================
    -- 📌 CTE 3: Dữ liệu thực chạy
    -- ======================
    TCDT AS
    (
        SELECT 
            tcdt.HopDongChiTietREF,

            SUM
            (
                CASE 
                    WHEN hdct.ChietKhau = 100 
                        THEN (tcdt.SoLuongThucChayKM + tcdt.SoLuongKMThayDoi)
                    ELSE (tcdt.SoLuongThucChay + tcdt.SoLuongThayDoi)
                END
            ) AS SoLuongTC,

            SUM
            (
                CASE 
                    WHEN hdct.ChietKhau = 100 
                        THEN (tcdt.ThanhTienKM + tcdt.GiaTriKMThayDoi)
                    ELSE (tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi)
                END
            ) AS ThanhTienTC

        FROM dbo.ThucChayDaTinh tcdt
        INNER JOIN dbo.HopDongChiTiet hdct
            ON tcdt.HopDongChiTietREF = hdct.HopDongChiTietID

        WHERE 
            tcdt.DmSanPhamREF NOT IN 
            (
                141,140,585,549,240,339,370,342,613,423,306,144,375,628,598,
                228,381,241,385,733,735,564,720,722,680,821,637,305,5133,5056,
                624,5082,5184,5006,5151
            )

            AND tcdt.DotChayHopDong NOT IN ('ThanhTien_GGFB', 'ThanhTien_GGFB_chot')

            AND NOT 
            (
                tcdt.DmHinhThucQuangCao = 13 
                OR hdct.DmLoaiBannerREF = 18
            )

            AND NOT 
            (
                hdct.DmSanPhamREF IN (306, 423) 
                OR hdct.DmViTriREF IN (100093, 100478)
            )

        GROUP BY 
            tcdt.HopDongChiTietREF
    )

    -- ======================
    -- 📌 TRUY VẤN CHÍNH
    -- ======================
    SELECT 
        hd.SoHopDong,
        hd.HopDongChiTietID,
        hd.DmSanPhamREF,
        hd.TenSanPham,
        hd.TenLoai,
        hd.ChietKhau,

        dbo.FormatNumber(hd.ThanhTienHD) AS ThanhTienHD,
        treo.SoLuongThucTreo,
        dbo.FormatNumber(treo.ThanhTien_treo) AS ThanhTien_Treo,

        dbo.FormatNumber(tcdt.SoLuongTC) AS SoLuong_TC,
        dbo.FormatNumber(tcdt.ThanhTienTC) AS ThanhTien_TC,

        -- 📍 Chênh lệch
        CASE 
            WHEN ROUND(treo.ThanhTien_treo, 0) <= ROUND(hd.ThanhTienHD, 0)
                THEN ROUND(treo.ThanhTien_treo, 0) - ROUND(ISNULL(tcdt.ThanhTienTC, 0), 0)
            ELSE ROUND(hd.ThanhTienHD, 0) - ROUND(ISNULL(tcdt.ThanhTienTC, 0), 0)
        END AS Chenh_Lech,

        -- 📍 Ghi chú
        CASE 
            WHEN ROUND(ISNULL(tcdt.ThanhTienTC, 0), 0) > ROUND(treo.ThanhTien_treo, 0)
                THEN N'TC vượt treo'

            WHEN ROUND(ISNULL(tcdt.ThanhTienTC, 0), 0) = 0
                 AND ROUND(treo.ThanhTien_treo, 0) <= ROUND(hd.ThanhTienHD, 0)
                THEN N'Chưa được tính'

            ELSE N'Ghi nhận sai'
        END AS Ghi_chu

    FROM TreoCTE treo
    INNER JOIN HDCTE hd 
        ON treo.HopDongChiTietREF = hd.HopDongChiTietID

    LEFT JOIN TCDT tcdt 
        ON treo.HopDongChiTietREF = tcdt.HopDongChiTietREF

    WHERE 
        ROUND(ISNULL(tcdt.ThanhTienTC, 0) - treo.ThanhTien_treo, 0) NOT BETWEEN -1 AND 1
        AND ROUND(treo.ThanhTien_treo, 0) <= ROUND(hd.ThanhTienHD, 0)

        AND hd.HopDongChiTietID NOT IN 
        (
            716568, 741531, 753700, 769213, 
            722697, 722698, 690297, 707662
        )

    ORDER BY 
        hd.SoHopDong;

END;
```
