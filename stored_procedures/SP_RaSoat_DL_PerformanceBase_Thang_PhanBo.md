# Stored Procedure: `RaSoat_DL_PerformanceBase_Thang_PhanBo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-03-21 14:07:30.847000
- **Ngày sửa cuối**: 2024-08-02 15:55:49.473000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Startdate` | `date(3)` | No |
| `@Todate` | `date(3)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[RaSoat_DL_PerformanceBase_Thang_PhanBo]
    @Startdate DATE = NULL,
    @Todate DATE = NULL
AS
BEGIN
    SET NOCOUNT ON;
    SELECT tcdc.NgayThucHien,
           tcdc.SohopDong,
           tcdc.HopDongChiTietREF,
           tcdc.TK_AdMarket,
           tcdc.DmSanPhamREF,
           tcdc.DmViTriREF,
           tcdc.TenViTri,
           tcdc.ThanhTien,
           tctk.ThucchaySanPham,
           tcdc.ThanhTienThucChay,
           tcdc.TienKPI,
           tcdc.TienTDGP,
           tcdc.TienDCThucChay,
           tcdc.TienHDNB
    FROM
    (
        SELECT contract_number,
               phanbo,
               DmSanPhamREF,
               username,
               DmViTriREF,
               NgayThucHien,
               dbo.FormatNumber(ISNULL(SUM(CONVERT(FLOAT, domain_tt_money)) / 1, 0)) AS ThucchaySanPham
        FROM dbo.ThucChayAdmarket_PhanBo
        WHERE NgayThucHien
        BETWEEN @Startdate AND @Todate
        GROUP BY contract_number,
                 phanbo,
                 DmSanPhamREF,
                 DmViTriREF,
                 NgayThucHien,
                 username
    ) tctk
        FULL JOIN
        (
            SELECT CASE
                       WHEN T.SoHopDong IS NULL THEN
                           L.SoHopDong
                       ELSE
                           T.SoHopDong
                   END SohopDong,
                   CASE
                       WHEN T.HopDongChiTietREF IS NULL THEN
                           L.HopDongChiTietREF
                       ELSE
                           T.HopDongChiTietREF
                   END HopDongChiTietREF,
                   CASE
                       WHEN T.TK_AdMarket IS NULL THEN
                           L.TK_Admarket
                       ELSE
                           T.TK_AdMarket
                   END TK_AdMarket,
                   CASE
                       WHEN T.DmSanPhamREF IS NULL THEN
                           L.DmSanPhamREF
                       ELSE
                           T.DmSanPhamREF
                   END DmSanPhamREF,
                   CASE
                       WHEN T.DmViTriREF IS NULL THEN
                           L.DmViTriREF
                       ELSE
                           T.DmViTriREF
                   END DmViTriREF,
                   CASE
                       WHEN T.TenViTri IS NULL THEN
                           L.TenViTri
                       ELSE
                           T.TenViTri
                   END TenViTri,
                   CASE
                       WHEN T.NgayThucHien IS NULL THEN
                           L.NgayThucHien
                       ELSE
                           T.NgayThucHien
                   END NgayThucHien,
                   CASE
                       WHEN T.ThanhTien IS NULL THEN
                           L.ThanhTien
                       ELSE
                           T.ThanhTien
                   END ThanhTien,
                   ISNULL(T.ThanhTienThucChay, 0) ThanhTienThucChay,
                   ISNULL(L.TienKPI, 0) TienKPI,
                   ISNULL(L.TienHDNB, 0) TienHDNB,
                   ISNULL(L.TienDCThucChay, 0) TienDCThucChay,
                   ISNULL(L.TienTDGP, 0) TienTDGP
            FROM
            (
                SELECT tcad.SoHopDong,
                       tcad.HopDongChiTietREF,
                       HDCT.TK_AdMarket,
                       tcad.DmSanPhamREF,
                       tcad.DmViTriREF,
                       tcad.TenViTri,
                       tcad.NgayThucHien,
                       tcad.ThanhTien,
                       SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS ThanhTienThucChay
                FROM dbo.ThucChayDaTinhAdmarket tcad
                    INNER JOIN dbo.HopDongChiTiet HDCT
                        ON HDCT.HopDongChiTietID = tcad.HopDongChiTietREF
                WHERE tcad.NgayThucHien
                      BETWEEN @Startdate AND @Todate
                      AND tcad.DmHinhThucQuangCao <> 42
                GROUP BY tcad.SoHopDong,
                         tcad.HopDongChiTietREF,
                         tcad.DmSanPhamREF,
                         tcad.DmViTriREF,
                         tcad.TenViTri,
                         tcad.NgayThucHien,
                         tcad.ThanhTien,
                         HDCT.TK_AdMarket
            ) T
                FULL JOIN
                (
                    SELECT td.SoHopDong,
                           td.HopDongChiTietREF,
                           td.ThanhTien,
                           td.DmSanPhamREF,
                           td.TK_Admarket,
                           td.DmViTriREF,
                           td.TenViTri,
                           td.NgayThucHien,
                           SUM(td.TienTDGP) TienTDGP,
                           SUM(td.TienKPI) TienKPI,
                           SUM(td.TienHDNB) TienHDNB,
                           SUM(TienDCThucChay) TienDCThucChay
                    FROM
                    (
                        SELECT tcpbtd.SoHopDong,
                               tcpbtd.DmSanPhamREF,
                               tcpbtd.HopDongChiTietREF,
                               hdct.ThanhTien,
                               tcpbtd.DmViTriREF,
                               tcpbtd.TenViTri,
                               tcpbtd.TK_Admarket,
                               CONVERT(DATE, tcpbtd.LastModifiedAt) AS NgayThucHien,
                               (CASE
                                    WHEN
                                    (
                                        tcpbtd.LoaiGhiNhan = 1
                                        AND tcpbtd.SoTienThayDoi <> 0
                                    ) THEN
                                        tcpbtd.SoTienThayDoi
                                    ELSE
                                        0
                                END
                               ) TienTDGP,
                               (CASE
                                    WHEN
                                    (
                                        (
                                            tcpbtd.LoaiGhiNhan = 0
                                            OR tcpbtd.LoaiGhiNhan IS NULL
                                        )
                                        AND tcpbtd.TienThucChayKPI <> 0
                                    ) THEN
                                        TienThucChayKPI
                                    ELSE
                                        0
                                END
                               ) TienKPI,
                               (CASE
                                    WHEN
                                    (
                                        tcpbtd.LoaiGhiNhan = 0
                                        AND tcpbtd.SoTienThayDoi <> 0
                    AND EXISTS
                                            (
                                                SELECT MaLoaiHopDong
                                                FROM DmLoaiHopDongNoiBo
                                                WHERE SoHopDong LIKE MaLoaiHopDong + '%'
                                                      AND MaLoaiHopDong NOT IN ( 'nb', 'sh' )
                                            )
                                    ) THEN
                                        tcpbtd.SoTienThayDoi
                                    ELSE
                                        0
                                END
                               ) TienDCThucChay,
                               (CASE
                                    WHEN
                                    (
                                        (
                                            tcpbtd.LoaiGhiNhan = 0
                                            OR tcpbtd.LoaiGhiNhan IS NULL
                                        )
                                        AND tcpbtd.SoTienThayDoi <> 0      
                                    ) THEN
                                        SoTienThayDoi
                                    ELSE
                                        0
                                END
                               ) TienHDNB
                        FROM dbo.ThucChay_PerformanceBase_ThayDoi tcpbtd
                            INNER JOIN dbo.HopDongChiTiet hdct
                                ON hdct.HopDongChiTietID = tcpbtd.HopDongChiTietREF
                        WHERE tcpbtd.DeletedStatus = 0
                              AND
                              (
                                  tcpbtd.LoaiGhiNhan IN ( 0, 1 )
                                  OR tcpbtd.LoaiGhiNhan IS NULL
                              )
                              AND tcpbtd.DmSanPhamREF IN ( 585, 628, 144 )
                              AND tcpbtd.RecordStatus IN ( 1, 3, 8 )
                              AND (CONVERT(DATE, tcpbtd.LastModifiedAt)
                              BETWEEN @Startdate AND @Todate
                                  )
                    ) td
                    GROUP BY td.DmSanPhamREF,
                             td.DmViTriREF,
                             td.TenViTri,
                             td.NgayThucHien,
                             td.SoHopDong,
                             td.HopDongChiTietREF,
                             td.TK_Admarket,
                             td.ThanhTien
                ) L
                    ON L.HopDongChiTietREF = T.HopDongChiTietREF
                       AND L.DmSanPhamREF = T.DmSanPhamREF
                       AND L.NgayThucHien = T.NgayThucHien
                       AND L.DmViTriREF = T.DmViTriREF
                       AND L.SoHopDong = T.SoHopDong
                       AND L.TK_Admarket = T.TK_AdMarket
        ) tcdc
            ON tcdc.DmSanPhamREF = tctk.DmSanPhamREF
               AND tctk.contract_number = tcdc.SohopDong
               AND tctk.phanbo = tcdc.HopDongChiTietREF
               AND tcdc.NgayThucHien = tctk.NgayThucHien
               AND tcdc.TK_AdMarket = tctk.username
               AND tcdc.DmViTriREF = tctk.DmViTriREF
	WHERE tcdc.NgayThucHien IS NOT NULL
    ORDER BY tcdc.NgayThucHien DESC;
END;

```
