# Stored Procedure: `sp_nhung_KT_hamtinh_Admatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-19 17:17:06.753000
- **Ngày sửa cuối**: 2026-03-19 17:44:08.287000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_nhung_KT_hamtinh_Admatic
AS
BEGIN
    SET NOCOUNT ON;
	SELECT  
    'Admatic' AS Thieu_Admatic,
    C.SoHopDong,
    C.DmSanPhamREF,
    C.HopDongChiTietID,
    C.DonViTinh,
    dbo.formatnumber(C.SoluongHD) AS SLHD,
    C.ChietKhau,
    C.ThanhtienHD,

    ROUND(
        CASE 
            WHEN C.ChietKhau = 100 THEN C.SLKM_tool 
            ELSE C.SLTC_tool 
        END, 0
    ) AS SoluongTool,

    dbo.FormatNumber(
        CASE 
            WHEN C.ChietKhau = 100 THEN C.TTKM_tool 
            ELSE C.TTTC_tool 
        END
    ) AS ThanhTienTool,

     dbo.FormatNumber(
        CASE 
            WHEN C.ChietKhau = 100 THEN ISNULL(D.SLKM, 0) 
            ELSE ISNULL(D.SL, 0) 
        END
    ) AS SoluongTC,

     dbo.FormatNumber(
        CASE 
            WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM, 0)
            ELSE ISNULL(D.thanhtien, 0) 
        END
    ) AS ThanhtienTC,

    dbo.FormatNumber(
        ROUND(
            CASE 
                WHEN C.ChietKhau = 100 THEN C.TTKM_tool 
                ELSE C.TTTC_tool 
            END, 0
        ) 
        - 
        ROUND(
            CASE 
                WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM, 0)
                ELSE ISNULL(D.thanhtien, 0) 
            END, 0
        )
    ) AS LechSP_Tool,

    dbo.FormatNumber(
        C.ThanhtienHD 
        - 
        ROUND(
            CASE 
                WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM, 0)
                ELSE ISNULL(D.thanhtien, 0) 
            END, 0
        )
    ) AS LechHD_TC

FROM 
(
    SELECT *
    FROM 
    (
        SELECT  
            hd.SoHopDong,
            hdct.HopDongChiTietID,
            hdct.DonViTinh,

            CASE 
                WHEN hdct.DonViTinhREF = 1 THEN hdct.SoLuong * 1000 
                ELSE hdct.SoLuong 
            END AS SoluongHD,

            CASE 
                WHEN hdct.ChietKhau = 100 THEN hdct.SoLuong * hdct.DonGia 
                ELSE hdct.ThanhTien 
            END AS ThanhtienHD,

            hdct.ChietKhau,
            hdct.DonGia,
            hdct.ThanhTien,
            hdct.DmSanPhamREF,
            (hdct.SoLuong * hdct.DonGia) AS ThanhtienKM

        FROM dbo.HopDong hd
        INNER JOIN dbo.HopDongChiTiet hdct 
            ON hd.HopDongID = hdct.HopDongFK

        WHERE 
            hd.Nam >= 2022
            AND NOT hdct.DmLoaiNenTangREF = 9
            AND hdct.DmLoaiREF = 42
            AND NOT hdct.DmSanPhamREF IN (817, 140, 549)
            AND NOT hdct.DonViTinhREF IN (7, 84)
            -- AND hd.SoHopDong = 'QC6060822'
    ) A

    INNER JOIN
    (
        SELECT  
            E.HopDongChiTietREF,
            SUM(F.SLTC) AS SLTC_tool,
            SUM(F.TTTC) AS TTTC_tool,
            SUM(F.SLKM) AS SLKM_tool,
            SUM(F.TTKM) AS TTKM_tool

        FROM 
        (
            SELECT DISTINCT
                tchdct.DmBannerREF,
                dbo.GetSoHopDongByID(tchdct.HopDongREF) AS SoHopDong,
                tchdct.HopDongChiTietREF,
                tchdct.DmSanPhamREF
            FROM dbo.ThucChayHopDongChiTiet tchdct
            WHERE 
                tchdct.DeletedStatus = 0
                -- AND tchdct.HopDongChiTietREF = '752576'
        ) E

        LEFT JOIN
        (
            SELECT  
                tc.SoHopDong,
                tc.DmBannerID,
                tc.DmSanPhamREF,
                SUM(tc.SoLuongThucChay) AS SLTC,
                SUM(tc.ThanhTienThucChaySauCK_ChuaVAT) AS TTTC,
                SUM(tc.SoLuongThucChayKM) AS SLKM,
                SUM(tc.ThanhTienThucChayKM) AS TTKM
            FROM ThucChay_ThanhTien_Admatic tc
            WHERE 
                NOT tc.SoHopDong = 'HD DEMO'
                -- AND tc.DmBannerID IN ('89276','89277')
            GROUP BY 
                tc.DmBannerID,
                tc.SoHopDong,
                tc.DmSanPhamREF
        ) F
            ON CONVERT(NVARCHAR(500), E.DmBannerREF) = CONVERT(NVARCHAR(500), F.DmBannerID)
            AND E.SoHopDong = F.SoHopDong
            AND E.DmSanPhamREF = F.DmSanPhamREF

        GROUP BY 
            E.HopDongChiTietREF
    ) B
        ON A.HopDongChiTietID = B.HopDongChiTietREF
) C

LEFT JOIN
(
    SELECT  
        HopDongChiTietREF,
        SUM(SoLuongThucChay + SoLuongThayDoi) AS SL,
        SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS thanhtien,
        SUM(SoLuongThucChayKM + SoLuongKMThayDoi) AS SLKM,
        SUM(ThanhTienKM + GiaTriKMThayDoi) AS thanhtienKM
    FROM dbo.ThucChayDaTinh tcdt
    WHERE DmHinhThucQuangCao = 42
    GROUP BY HopDongChiTietREF
) D
    ON C.HopDongChiTietREF = D.HopDongChiTietREF

WHERE 
    1 = 1
    -- AND C.HopDongChiTietID = '773870'
    -- AND C.SoHopDong IN ('QC1770125')

    AND NOT ROUND(C.ThanhtienHD, 0) = 
        ROUND(
            CASE 
                WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM, 0)
                ELSE ISNULL(D.thanhtien, 0) 
            END, 0
        )

    AND NOT (
        ROUND(
            CASE 
                WHEN C.ChietKhau = 100 THEN C.TTKM_tool 
                ELSE C.TTTC_tool 
            END, 0
        )
        -
        ROUND(
            CASE 
                WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM, 0)
                ELSE ISNULL(D.thanhtien, 0) 
            END, 0
        ) 
        IN (-1, 0, 1)
    )

ORDER BY 
    C.DmSanPhamREF,
    C.ChietKhau DESC;


	    
END


```
