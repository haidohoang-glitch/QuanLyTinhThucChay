# Stored Procedure: `sp_nhung_KT_hamtinh_Muangoai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-20 09:25:06.033000
- **Ngày sửa cuối**: 2026-03-20 09:25:06.033000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_nhung_KT_hamtinh_Muangoai
AS
BEGIN
    SET NOCOUNT ON;
SELECT 
    tc.*
FROM (
    SELECT 
        TT.SHD,
        TT.HopDongFK,
        TT.HopDongChiTietID,
        TT.DmSanPhamREF,
        TT.SoLuong,
        TT.DonViTinh,
        TT.DonGia,
		TT.ChietKhau,
        TT.DuToanBan,		
        TT.DuToanMua,        
        TT.ThucChayMua,
        TT.ThucChayBan,        
        B.tc AS TCDT,
        (ISNULL(TT.ThucChayBan, 0) - ISNULL(B.tc, 0)) AS TinhThieu,
        (ISNULL(TT.DuToanBan, 0) - ISNULL(B.tc, 0)) AS LechPboThucchay,
		TT.NgaySua_DuToan,
        TT.NgaySua_ThucChay,
        TT.NgaySua_HopDongBan
    FROM (
        SELECT 
            A.SHD,
            A.HopDongFK,
            A.HopDongChiTietID,
            A.DmSanPhamREF,
            A.TenLoai,
            A.TenSanPham,
            A.TenWebsite,
            A.TenLoaiBanner,
            A.SoLuong,
            A.DonViTinh,
            A.DonGia,
            A.DuToanBan,
            A.DuToanMua,
            A.ChietKhau,
            SUM(A.ThucChayMua) AS ThucChayMua,
            ROUND(SUM(A.ThucChayBan), 0) AS ThucChayBan,
            MAX(A.dtmua) AS NgaySua_DuToan,
            MAX(A.tcmua) AS NgaySua_ThucChay,
            MAX(A.dtban) AS NgaySua_HopDongBan
        FROM (
            SELECT 
                dbo.GetSoHopDongByID(c.HopDongFK) AS SHD,
                c.HopDongFK,
                a.HopDongChiTietID,
                c.DmSanPhamREF,
                b.ThucChayMuaNgoaiChiTietID,
                c.TenLoai,
                c.TenSanPham,
                c.TenWebsite,
                c.TenLoaiBanner,
                c.SoLuong,
                c.DonViTinh,
				b.Status,
                c.DonGia,
                c.ThanhTien AS DuToanBan,
                a.ThanhTienSauCKMua AS DuToanMua,
				a.CreatedAt,
                -- Tính Thực chạy mua
                CASE 
                    WHEN b.Status IN (1, 2, 4) AND b.CreatedAt >= '2020-05-14' THEN 
                        b.ThanhTienMuaNgoaiTruocCK * (100 - b.ChietKhauMuaNgoai) / 100
                    WHEN b.CreatedAt < '2020-05-14' THEN 
                        b.ThanhTienMuaNgoaiTruocCK * (100 - b.ChietKhauMuaNgoai) / 100
                    ELSE 0 
                END AS ThucChayMua,

                -- Tính Thực chạy bán
                CASE 
                    WHEN a.ThanhTienSauCKMua = 0 THEN
                        b.ThanhTienMuaNgoaiTruocCK * (100 - b.ChietKhauMuaNgoai) / 100 
                        + b.ThanhTienLaiThucChaySauCK
                    ELSE
                        CASE 
                            WHEN b.Status IN (1, 2, 4) AND b.CreatedAt >= '2020-05-14' THEN 
                                b.ThanhTienMuaNgoaiTruocCK * (100 - b.ChietKhauMuaNgoai) / 100 
                                + (ThanhTienLaiSauCK * 
                                  (b.ThanhTienMuaNgoaiTruocCK * (100 - b.ChietKhauMuaNgoai) / 100) / a.ThanhTienSauCKMua)
                            WHEN b.CreatedAt < '2020-05-14' THEN 
                                b.ThanhTienMuaNgoaiTruocCK * (100 - b.ChietKhauMuaNgoai) / 100 
                                + (ThanhTienLaiSauCK * 
                                  (b.ThanhTienMuaNgoaiTruocCK * (100 - b.ChietKhauMuaNgoai) / 100) / a.ThanhTienSauCKMua)
                        END
                END AS ThucChayBan,
                a.LastModifiedAt AS dtmua,
                b.LastModifiedAt AS tcmua,
                c.LastModifiedAt AS dtban,
                c.ChietKhau
            FROM 
                HopDongChiTiet_MuaNgoai a
            LEFT JOIN 
                ThucChayMuaNgoaiChiTiet b 
                ON a.HopDongChiTietID = b.HopDongChiTietREF AND b.DeletedStatus = 0
            LEFT JOIN 
                HopDongChiTiet c 
                ON a.HopDongChiTietID = c.HopDongChiTietID AND c.ChietKhau <> 100
            WHERE 
                a.DeletedStatus = 0
                AND (c.DmLoaiREF = 13 OR c.DmLoaiBannerREF = 18)
                AND c.DeletedStatus = 0
                AND c.HopDongFK IN (SELECT HopDongID FROM HopDong WHERE Nam >= 2022)
				AND b.Status IN (1,2,4)
        ) A
        GROUP BY 
            A.SHD, A.HopDongFK, A.HopDongChiTietID, A.DmSanPhamREF,
            A.TenLoai, A.TenSanPham, A.TenWebsite, A.TenLoaiBanner,
            A.SoLuong, A.DonViTinh, A.DonGia, A.DuToanBan, A.DuToanMua, A.ChietKhau
    ) TT

    FULL OUTER JOIN (
        SELECT 
            SoHopDong,
            HopDongID,
            HopDongChiTietREF,
            DmSanPhamREF AS DmSanPhamREF_tcdt,
            ROUND(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi), 0) AS tc
        FROM 
            dbo.ThucChayDaTinh
        WHERE 
            (DmLoaiBannerREF = 18 OR DmHinhThucQuangCao = 13)
            AND TrangThaiHopDong <> 3
            AND Nam >= 2022
            AND DmChienDichREF = 0
        GROUP BY 
            SoHopDong, HopDongID, HopDongChiTietREF, DmSanPhamREF
        HAVING 
            ROUND(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi), 0) <> 0
    ) B ON TT.HopDongChiTietID = B.HopDongChiTietREF

    WHERE 
        (
            ABS(ISNULL(TT.ThucChayBan, 0) - ISNULL(B.tc, 0)) > 1000
            AND (
                YEAR(TT.NgaySua_DuToan) >= 2020
                OR YEAR(TT.NgaySua_ThucChay) >= 2020
                OR YEAR(TT.NgaySua_HopDongBan) >= 2020
            )
        )
        OR TT.HopDongFK IS NULL
) tc
ORDER BY 
    tc.HopDongFK DESC;

END;
```
