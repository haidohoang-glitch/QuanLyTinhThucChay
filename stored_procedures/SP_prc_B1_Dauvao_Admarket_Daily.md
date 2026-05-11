# Stored Procedure: `prc_B1_Dauvao_Admarket_Daily`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2022-04-29 15:01:38.857000
- **Ngày sửa cuối**: 2023-07-20 09:58:56.730000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `date(3)` | No |
| `@EndDate` | `date(3)` | No |

## Definition (Source Code)

```sql

CREATE PROC [dbo].[prc_B1_Dauvao_Admarket_Daily]
--DECLARE @StartDate DATE = '2023-03-29',
--        @EndDate DATE = '2023-03-29';
		@StartDate DATE = null,
        @EndDate DATE = null
AS
BEGIN
    SET NOCOUNT ON;

    --   SELECT a.DmSanPhamREF,
    --          a.TenSanPham,
    --          a.DmViTriREF,
    --          a.TenViTri,
    --          dbo.FormatNumber(ROUND(   CASE
    --                                        WHEN a.DmSanPhamREF IN ( 585, 144 ) THEN
    --                                            adx.TongTien
    --                                        ELSE
    --                                            viewplus.TongTien
    --                                    END,
    --                                    0
    --                                )
    --                          ) TongTien_SP,
    --	   dbo.FormatNumber(ROUND(thayDoi.TienTDGP + thayDoi.TienKPI + thayDoi.TienHDNB, 0)) AS TongTienDieuChinh,
    --          dbo.FormatNumber(ROUND(a.TongTien, 0)) AS TongTien,
    --          IIF(a.TenSanPham = 'ADX', ROUND(adx.TongTien - a.TongTien, 0), ROUND(viewplus.TongTien - a.TongTien, 0)) AS ChenhLech
    --   FROM
    --   (
    --       SELECT DmSanPhamREF,
    --              TenSanPham,
    --              DmViTriREF,
    --              TenViTri,
    --              SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) * 1.08 AS TongTien
    --       FROM dbo.ThucChayDaTinh
    --       WHERE NgayThucHien
    --             BETWEEN @StartDate AND @EndDate
    --             AND TenMaHopDong NOT IN ( 'nb', 'sh' )
    --             AND DmSanPhamREF IN ( 144, 628, 585 )
    --             AND NOT (
    --                         DmHinhThucQuangCao IN ( 13, 42 )
    --                         OR DmLoaiBannerREF = 18
    --                     )
    --             AND GhiChu <> 'HDBAN_INVENTORY'
    --             AND GhiChu <> N'sp_TC_Insert_From_DataThucChay_Adx'
    --       GROUP BY DmSanPhamREF,
    --                TenSanPham,
    --                DmViTriREF,
    --                TenViTri
    --   ) a
    --       OUTER APPLY
    --   (
    --       SELECT TenSanPham,
    --              TenViTri,
    --              CONVERT(FLOAT, COUNT(DISTINCT username)) AS sluser,
    --              SUM(CONVERT(FLOAT, domain_tt_view)) TotalView,
    --              SUM(CONVERT(FLOAT, domain_tt_click)) TotalClick,
    --              SUM(CONVERT(FLOAT, domain_tt_money)) TongTien,
    --              SUM(CONVERT(FLOAT, domain_tt_promotion)) TongTienKhuyenMai,
    --              isnoibo
    --       FROM ThucChayAdmarket_ADX_CPC_HopDong a1
    --       WHERE NgayThucHien
    --             BETWEEN @StartDate AND @EndDate
    --             AND DmSanPhamREF IN ( 585, 144 )
    --             AND ISNULL(isnoibo, 0) = 0
    --             AND a.TenSanPham = a1.TenSanPham
    --             AND a.TenViTri = a1.TenViTri
    --       GROUP BY TenSanPham,
    --                TenViTri,
    --                isnoibo
    --   ) adx
    --       OUTER APPLY
    --   (
    --       SELECT TenSanPham,
    --              COUNT(DISTINCT username) AS sluser,
    --              SUM(CONVERT(FLOAT, domain_tt_view)) TotalView,
    --              SUM(CONVERT(FLOAT, domain_tt_click)) TotalClick,
    --              SUM(CONVERT(FLOAT, domain_money)) TongTien,
    --              SUM(CONVERT(FLOAT, domain_promotion)) TongTienKhuyenMai,
    --              isnoibo
    --       FROM ThucChayAdmarket_ViewPlus_HopDong a2
    --       WHERE NgayThucHien
    --             BETWEEN @StartDate AND @EndDate
    --             AND ISNULL(isnoibo, 0) = 0
    --             AND a.TenSanPham = a2.TenSanPham
    --       GROUP BY TenSanPham,
    --                isnoibo
    --   ) viewplus
    --OUTER APPLY
    --   (
    --       SELECT td.DmSanPhamREF,
    --              td.DmViTriREF,
    --              td.TenViTri,
    --              SUM(td.TienTDGP) TienTDGP,
    --              SUM(td.TienKPI) TienKPI,
    --              SUM(td.TienHDNB) TienHDNB
    --       FROM
    --       (
    --           SELECT DmSanPhamREF,
    --                  DmViTriREF,
    --                  TenViTri,
    --                  (CASE
    --                       WHEN
    --                       (
    --                           LoaiGhiNhan = 1
    --                           AND SoTienThayDoi <> 0
    --                       ) THEN
    --                           SoTienThayDoi
    --                       ELSE
    --                           0
    --                   END
    --                  ) TienTDGP,
    --                  (CASE
    --                       WHEN
    --                       (
    --                           (
    --                               LoaiGhiNhan = 0
    --                               OR LoaiGhiNhan IS NULL
    --                           )
    --                           AND TienThucChayKPI <> 0
    --                       ) THEN
    --                           TienThucChayKPI
    --                       ELSE
    --                           0
    --                   END
    --                  ) TienKPI,
    --                  (CASE
    --                       WHEN
    --                       (
    --                           (
    --                               LoaiGhiNhan = 0
    --                               OR LoaiGhiNhan IS NULL
    --                           )
    --                           AND SoTienThayDoi <> 0
    --                           AND EXISTS
    --                               (
    --                                   SELECT MaLoaiHopDong
    --                                   FROM DmLoaiHopDongNoiBo
    --                                   WHERE SoHopDong LIKE MaLoaiHopDong + '%'
    --                               )
    --                       ) THEN
    --                           SoTienThayDoi
    --                       ELSE
    --                           0
    --                   END
    --                  ) TienHDNB
    --           FROM dbo.ThucChay_PerformanceBase_ThayDoi
    --           WHERE DeletedStatus = 0
    --                 AND
    --                 (
    --                     LoaiGhiNhan IN ( 0, 1 )
    --                     OR LoaiGhiNhan IS NULL
    --                 )
    --                 AND DmSanPhamREF IN ( 585, 628, 144 )
    --                 AND RecordStatus IN ( 1, 3, 8 )
    --                 AND CAST(CreatedAt AS DATE)
    --                 BETWEEN @StartDate AND @EndDate
    --       ) td
    --	WHERE td.DmSanPhamREF = a.DmSanPhamREF
    --	AND td.DmViTriREF = a.DmViTriREF
    --	AND td.TenViTri = a.TenViTri
    --       GROUP BY DmSanPhamREF,
    --                DmViTriREF,
    --                TenViTri
    --   ) thayDoi
    --   ORDER BY a.TenSanPham,
    --            a.TenViTri;


    WITH cte --Lấy ra các thuc chay update kpi
	AS (
		SELECT SoHopDong, HopDongChiTietREF FROM dbo.ThucChayDaTinh WHERE DmChienDichREF = 2 AND DmViTriREF = 0 
				  AND NgayThucHien
                  BETWEEN @StartDate AND @EndDate
                  AND TenMaHopDong NOT IN ( 'nb', 'sh' )
                  AND DmSanPhamREF IN ( 144, 628, 585 )
                  AND NOT (
                              DmHinhThucQuangCao IN ( 13, 42 )
                              OR DmLoaiBannerREF = 18
                          )
                  AND GhiChu <> 'HDBAN_INVENTORY'
                  AND GhiChu <> N'sp_TC_Insert_From_DataThucChay_Adx'
	),
	ctda --Lấy ra các thực chạy thay đổi không có các kpi
    AS (SELECT td.DmSanPhamREF,
               td.DmViTriREF,
               td.TenViTri,
               SUM(td.TienTDGP) TienTDGP,
               SUM(td.TienKPI) TienKPI,
               SUM(td.TienHDNB) TienHDNB
        FROM
        (
            SELECT DmSanPhamREF,
                   DmViTriREF,
                   TenViTri,
                   (CASE
                        WHEN
                        (
                            LoaiGhiNhan = 1
                            AND SoTienThayDoi <> 0
                        ) THEN
                            SoTienThayDoi
                        ELSE
                            0
                    END
                   ) TienTDGP,
                   (CASE
                        WHEN
                        (
                            (
                                LoaiGhiNhan = 0
                                OR LoaiGhiNhan IS NULL
                            )
                            AND TienThucChayKPI <> 0
                        ) THEN
                            TienThucChayKPI
                        ELSE
                            0
                    END
                   ) TienKPI,
                   (CASE
                        WHEN
                        (
                            (
                                LoaiGhiNhan = 0
                                OR LoaiGhiNhan IS NULL
                            )
                            AND SoTienThayDoi <> 0
                            AND EXISTS
                                (
                                    SELECT MaLoaiHopDong
                                    FROM DmLoaiHopDongNoiBo
                                    WHERE SoHopDong LIKE MaLoaiHopDong + '%' AND MaLoaiHopDong NOT IN ( 'nb', 'sh' )
                                )
                        ) THEN
                            SoTienThayDoi
                        ELSE
                            0
                    END
                   ) TienHDNB
            FROM dbo.ThucChay_PerformanceBase_ThayDoi tcpbtd
            WHERE DeletedStatus = 0
                  AND
                  (
                      LoaiGhiNhan IN ( 0, 1 )
                      OR LoaiGhiNhan IS NULL
                  )
                  AND DmSanPhamREF IN ( 585, 628, 144 )
                  AND RecordStatus IN ( 1, 3, 8 )
                  AND CAST(CreatedAt AS DATE)
                  BETWEEN @StartDate AND @EndDate
				  AND NOT EXISTS(SELECT * FROM cte WHERE cte.SoHopDong = tcpbtd.SoHopDong AND cte.HopDongChiTietREF = tcpbtd.HopDongChiTietREF)
        ) td
        GROUP BY DmSanPhamREF,
                 DmViTriREF,
                 TenViTri),
	ctde --Lấy ra các thực chạy thay đổi có các kpi
    AS (SELECT td.DmSanPhamREF,
               td.DmViTriREF,
               td.TenViTri,
               SUM(td.TienTDGP) TienTDGP,
               SUM(td.TienKPI) TienKPI,
               SUM(td.TienHDNB) TienHDNB
        FROM
        (
            SELECT DmSanPhamREF,
                   DmViTriREF,
                   TenViTri,
                   (CASE
                        WHEN
                        (
                            LoaiGhiNhan = 1
                            AND SoTienThayDoi <> 0
                        ) THEN
                            SoTienThayDoi
                        ELSE
                            0
                    END
                   ) TienTDGP,
                   (CASE
                        WHEN
                        (
                            (
                                LoaiGhiNhan = 0
                                OR LoaiGhiNhan IS NULL
                            )
                            AND TienThucChayKPI <> 0
                        ) THEN
                            TienThucChayKPI
                        ELSE
                            0
                    END
                   ) TienKPI,
                   (CASE
                        WHEN
                        (
                            (
                                LoaiGhiNhan = 0
                                OR LoaiGhiNhan IS NULL
                            )
                            AND SoTienThayDoi <> 0
                            AND EXISTS
                                (
                                    SELECT MaLoaiHopDong
                                    FROM DmLoaiHopDongNoiBo
                                    WHERE SoHopDong LIKE MaLoaiHopDong + '%' AND MaLoaiHopDong NOT IN ( 'nb', 'sh' )
                                )
                        ) THEN
                            SoTienThayDoi
                        ELSE
                            0
                    END
                   ) TienHDNB
            FROM dbo.ThucChay_PerformanceBase_ThayDoi tcpbtd
            WHERE DeletedStatus = 0
                  AND
                  (
                      LoaiGhiNhan IN ( 0, 1 )
                      OR LoaiGhiNhan IS NULL
                  )
                  AND DmSanPhamREF IN ( 585, 628, 144 )
                  AND RecordStatus IN ( 1, 3, 8 )
                  AND CAST(CreatedAt AS DATE)
                  BETWEEN @StartDate AND @EndDate
				  AND EXISTS(SELECT * FROM cte WHERE cte.SoHopDong = tcpbtd.SoHopDong AND cte.HopDongChiTietREF = tcpbtd.HopDongChiTietREF)
        ) td
        GROUP BY DmSanPhamREF,
                 DmViTriREF,
                 TenViTri),
    cttcdta --Lấy ra các thực chạy đã tính không có các kpi
    AS (SELECT a.DmSanPhamREF,
               a.TenSanPham,
               a.DmViTriREF,
               a.TenViTri,
               (CASE
                    WHEN a.DmSanPhamREF IN ( 585, 144 ) THEN
                        adx.TongTien
                    ELSE
                        viewplus.TongTien
                END
               ) TongTien_SP,
               (a.TongTien) AS TongTien,
               IIF(a.TenSanPham = 'ADX', ROUND(adx.TongTien - a.TongTien, 0), ROUND(viewplus.TongTien - a.TongTien, 0)) AS ChenhLech
        FROM
        (
            SELECT DmSanPhamREF,
                   TenSanPham,
                   DmViTriREF,
                   TenViTri,
                   SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) * 1.08 AS TongTien
            FROM dbo.ThucChayDaTinh tbtcdt
            WHERE NgayThucHien
                  BETWEEN @StartDate AND @EndDate
                  AND TenMaHopDong NOT IN ( 'nb', 'sh' )
                  AND DmSanPhamREF IN ( 144, 628, 585 )
                  AND NOT (
                              DmHinhThucQuangCao IN ( 13, 42 )
                              OR DmLoaiBannerREF = 18
                          )
                  AND GhiChu <> 'HDBAN_INVENTORY'
                  AND GhiChu <> N'sp_TC_Insert_From_DataThucChay_Adx'
				  AND NOT EXISTS(SELECT * FROM cte WHERE cte.SoHopDong = tbtcdt.SoHopDong AND cte.HopDongChiTietREF = tbtcdt.HopDongChiTietREF)
            GROUP BY DmSanPhamREF,
                     TenSanPham,
                     DmViTriREF,
                     TenViTri
        ) a
            OUTER APPLY
        (
            SELECT TenSanPham,
                   TenViTri,
                   CONVERT(FLOAT, COUNT(DISTINCT username)) AS sluser,
                   SUM(CONVERT(FLOAT, domain_tt_view)) TotalView,
                   SUM(CONVERT(FLOAT, domain_tt_click)) TotalClick,
                   SUM(CONVERT(FLOAT, domain_tt_money)) TongTien,
                   SUM(CONVERT(FLOAT, domain_tt_promotion)) TongTienKhuyenMai,
                   isnoibo
            FROM ThucChayAdmarket_ADX_CPC_HopDong a1
            WHERE NgayThucHien
                  BETWEEN @StartDate AND @EndDate
                  AND DmSanPhamREF IN ( 585, 144 )
                  AND ISNULL(isnoibo, 0) = 0
                  AND a.TenSanPham = a1.TenSanPham
                  AND a.TenViTri = a1.TenViTri
            GROUP BY TenSanPham,
                     TenViTri,
                     isnoibo
        ) adx
            OUTER APPLY
        (
            SELECT TenSanPham,
                   COUNT(DISTINCT username) AS sluser,
                   SUM(CONVERT(FLOAT, domain_tt_view)) TotalView,
                   SUM(CONVERT(FLOAT, domain_tt_click)) TotalClick,
                   SUM(CONVERT(FLOAT, domain_money)) TongTien,
                   SUM(CONVERT(FLOAT, domain_promotion)) TongTienKhuyenMai,
                   isnoibo
            FROM ThucChayAdmarket_ViewPlus_HopDong a2
            WHERE NgayThucHien
                  BETWEEN @StartDate AND @EndDate
                  AND ISNULL(isnoibo, 0) = 0
                  AND a.TenSanPham = a2.TenSanPham
            GROUP BY TenSanPham,
                     isnoibo
        ) viewplus ),
	cttcdte --Lấy ra các thực chạy đã tính có các kpi
    AS (SELECT a.DmSanPhamREF,
               a.TenSanPham,
               a.DmViTriREF,
               a.TenViTri,
               (CASE
                    WHEN a.DmSanPhamREF IN ( 585, 144 ) THEN
                        adx.TongTien
                    ELSE
                        viewplus.TongTien
                END
               ) TongTien_SP,
               (a.TongTien) AS TongTien,
               IIF(a.TenSanPham = 'ADX', ROUND(adx.TongTien - a.TongTien, 0), ROUND(viewplus.TongTien - a.TongTien, 0)) AS ChenhLech
        FROM
        (
            SELECT DmSanPhamREF,
                   TenSanPham,
                   DmViTriREF,
                   TenViTri,
                   SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) * 1.08 AS TongTien
            FROM dbo.ThucChayDaTinh tbtcdt
            WHERE NgayThucHien
                  BETWEEN @StartDate AND @EndDate
                  AND TenMaHopDong NOT IN ( 'nb', 'sh' )
                  AND DmSanPhamREF IN ( 144, 628, 585 )
                  AND NOT (
                              DmHinhThucQuangCao IN ( 13, 42 )
                              OR DmLoaiBannerREF = 18
                          )
                  AND GhiChu <> 'HDBAN_INVENTORY'
                  AND GhiChu <> N'sp_TC_Insert_From_DataThucChay_Adx'
				  AND EXISTS(SELECT * FROM cte WHERE cte.SoHopDong = tbtcdt.SoHopDong AND cte.HopDongChiTietREF = tbtcdt.HopDongChiTietREF)
            GROUP BY DmSanPhamREF,
                     TenSanPham,
                     DmViTriREF,
                     TenViTri
        ) a
            OUTER APPLY
        (
            SELECT TenSanPham,
                   TenViTri,
                   CONVERT(FLOAT, COUNT(DISTINCT username)) AS sluser,
                   SUM(CONVERT(FLOAT, domain_tt_view)) TotalView,
                   SUM(CONVERT(FLOAT, domain_tt_click)) TotalClick,
                   SUM(CONVERT(FLOAT, domain_tt_money)) TongTien,
                   SUM(CONVERT(FLOAT, domain_tt_promotion)) TongTienKhuyenMai,
                   isnoibo
            FROM ThucChayAdmarket_ADX_CPC_HopDong a1
            WHERE NgayThucHien
                  BETWEEN @StartDate AND @EndDate
                  AND DmSanPhamREF IN ( 585, 144 )
                  AND ISNULL(isnoibo, 0) = 0
                  AND a.TenSanPham = a1.TenSanPham
                  AND a.TenViTri = a1.TenViTri
            GROUP BY TenSanPham,
                     TenViTri,
                     isnoibo
        ) adx
            OUTER APPLY
        (
            SELECT TenSanPham,
                   COUNT(DISTINCT username) AS sluser,
                   SUM(CONVERT(FLOAT, domain_tt_view)) TotalView,
                   SUM(CONVERT(FLOAT, domain_tt_click)) TotalClick,
                   SUM(CONVERT(FLOAT, domain_money)) TongTien,
                   SUM(CONVERT(FLOAT, domain_promotion)) TongTienKhuyenMai,
                   isnoibo
            FROM ThucChayAdmarket_ViewPlus_HopDong a2
            WHERE NgayThucHien
                  BETWEEN @StartDate AND @EndDate
                  AND ISNULL(isnoibo, 0) = 0
                  AND a.TenSanPham = a2.TenSanPham
            GROUP BY TenSanPham,
                     isnoibo
        ) viewplus ),
	ctTotalNoKPI -- tổng không có kpi
	AS (
	SELECT tcdt.DmSanPhamREF,
           tcdt.TenSanPham,
           tcdt.DmViTriREF,
           tcdt.TenViTri,
           ISNULL(tcdt.TongTien_SP, 0) AS TongTien_SP,
           ISNULL(tcdt.TongTien, 0) AS TongTien,
           ROUND((ISNULL(td.TienTDGP, 0) + ISNULL(td.TienKPI, 0) + ISNULL(td.TienHDNB, 0)) * 1.08, 0) AS TongTienDieuChinh,
           ISNULL(tcdt.ChenhLech, 0) ChenhLech
    FROM cttcdta tcdt
        LEFT JOIN ctda td WITH (NOLOCK)
            ON tcdt.DmSanPhamREF = td.DmSanPhamREF
               AND tcdt.DmViTriREF = td.DmViTriREF
               AND tcdt.TenViTri = td.TenViTri
    --ORDER BY tcdt.TenSanPham,
    --         tcdt.TenViTri
			 ),
	ctTotalInKPI -- tổng có kpi
	AS (
	SELECT tcdt.DmSanPhamREF,
           tcdt.TenSanPham,
           tcdt.DmViTriREF,
           tcdt.TenViTri,
           ISNULL(tcdt.TongTien_SP, 0) AS TongTien_SP,
           ISNULL(tcdt.TongTien, 0) AS TongTien,
           ROUND((ISNULL(td.TienTDGP, 0) + ISNULL(td.TienKPI, 0) + ISNULL(td.TienHDNB, 0)) * 1.08, 0) AS TongTienDieuChinh,
           ISNULL(tcdt.ChenhLech, 0) ChenhLech
    FROM cttcdte tcdt
        LEFT JOIN ctde td WITH (NOLOCK)
            ON tcdt.DmSanPhamREF = td.DmSanPhamREF
               --AND tcdt.DmViTriREF = td.DmViTriREF
               --AND tcdt.TenViTri = td.TenViTri
    --ORDER BY tcdt.TenSanPham,
    --         tcdt.TenViTri
			 )
	--Nối 2 tổng vào với nhau
	SELECT total.DmSanPhamREF, total.TenSanPham, total.DmViTriREF, total.TenViTri, dbo.FormatNumber(total.TongTien_SP) TongTien_SP, dbo.FormatNumber(total.TongTien) TongTien,
	dbo.FormatNumber(total.TongTienDieuChinh) TongTienDieuChinh, dbo.FormatNumber(total.TongTien_SP + total.TongTienDieuChinh - total.TongTien) ChenhLech
	FROM (
		SELECT * FROM ctTotalNoKPI
		UNION ALL
		SELECT * FROM ctTotalInKPI ) total
	ORDER BY total.TenSanPham,
             total.TenViTri
	;


    ------------ADMARKET---------------
    SELECT TenSanPham, --, NgayThucHien
           COUNT(DISTINCT username) AS sluser,
           dbo.FormatNumber(ROUND(SUM(CONVERT(FLOAT, domain_tt_view)), 0)) TotalView,
           dbo.FormatNumber(ROUND(SUM(CONVERT(FLOAT, domain_tt_click)), 0)) TotalClick,
           dbo.FormatNumber(ROUND(SUM(CONVERT(FLOAT, domain_tt_money)), 0)) TongTien,
           dbo.FormatNumber(ROUND(SUM(CONVERT(FLOAT, domain_tt_promotion)), 0)) TongTienKhuyenMai,
           isnoibo
    FROM ThucChayAdmarket_ADX_CPC_HopDong
    WHERE NgayThucHien
          BETWEEN @StartDate AND @EndDate
          AND DmSanPhamREF = 144
    GROUP BY TenSanPham,
             isnoibo;

    ---------------ADX -------------------
    SELECT TenSanPham,
           TenViTri,
           CONVERT(FLOAT, COUNT(DISTINCT username)) AS sluser,
           dbo.FormatNumber(ROUND(SUM(CONVERT(FLOAT, domain_tt_view)), 0)) TotalView,
           dbo.FormatNumber(ROUND(SUM(CONVERT(FLOAT, domain_tt_click)), 0)) TotalClick,
           dbo.FormatNumber(ROUND(SUM(CONVERT(FLOAT, domain_tt_money)), 0)) TongTien,
           dbo.FormatNumber(ROUND(SUM(CONVERT(FLOAT, domain_tt_promotion)), 0)) TongTienKhuyenMai,
           isnoibo
    FROM ThucChayAdmarket_ADX_CPC_HopDong
    WHERE NgayThucHien
          BETWEEN @StartDate AND @EndDate
          AND DmSanPhamREF = 585
    GROUP BY TenSanPham,
             TenViTri,
             isnoibo
    ORDER BY TenViTri,
             isnoibo;

    ----------ViewPlus---------------
    SELECT TenSanPham,
           COUNT(DISTINCT username) AS sluser,
           dbo.FormatNumber(ROUND(SUM(CONVERT(FLOAT, domain_tt_view)), 0)) TotalView,
           dbo.FormatNumber(ROUND(SUM(CONVERT(FLOAT, domain_tt_click)), 0)) TotalClick,
           dbo.FormatNumber(ROUND(SUM(CONVERT(FLOAT, domain_money)), 0)) TongTien,
           dbo.FormatNumber(ROUND(SUM(CONVERT(FLOAT, domain_promotion)), 0)) TongTienKhuyenMai,
           isnoibo
    FROM ThucChayAdmarket_ViewPlus_HopDong
    WHERE NgayThucHien
    BETWEEN @StartDate AND @EndDate
    GROUP BY TenSanPham,
             isnoibo
    ORDER BY isnoibo;

END;

```
