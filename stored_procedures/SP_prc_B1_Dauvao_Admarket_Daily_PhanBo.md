# Stored Procedure: `prc_B1_Dauvao_Admarket_Daily_PhanBo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-03-02 10:45:26.860000
- **Ngày sửa cuối**: 2024-03-02 10:45:26.860000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `date(3)` | No |
| `@EndDate` | `date(3)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[prc_B1_Dauvao_Admarket_Daily_PhanBo]
		@StartDate DATE = null,
        @EndDate DATE = NULL        


AS
BEGIN
    SET NOCOUNT ON;
    WITH cte --Lấy ra các thuc chay update kpi
	AS (
		SELECT SoHopDong, HopDongChiTietREF FROM dbo.ThucChayDaTinh WHERE DmChienDichREF = 2 AND DmViTriREF = 0 
				  AND NgayThucHien
                  BETWEEN @StartDate AND @EndDate
                  AND TenMaHopDong NOT IN ( 'nb', 'sh' )
                  AND DmSanPhamREF IN ( 144, 628, 585 )
                  AND NOT ( DmHinhThucQuangCao IN ( 13, 42 )OR DmLoaiBannerREF = 18)
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
                   (CASE  WHEN (LoaiGhiNhan = 1  AND SoTienThayDoi <> 0 ) THEN   SoTienThayDoi  ELSE  0   END ) TienTDGP,
                   (CASE  WHEN (( LoaiGhiNhan = 0 OR LoaiGhiNhan IS NULL) AND TienThucChayKPI <> 0 ) THEN TienThucChayKPI ELSE 0 END) TienKPI,
                   (CASE  WHEN ((LoaiGhiNhan = 0 OR LoaiGhiNhan IS NULL) AND SoTienThayDoi <> 0
                   AND EXISTS (SELECT MaLoaiHopDong FROM DmLoaiHopDongNoiBo WHERE SoHopDong LIKE MaLoaiHopDong + '%' AND MaLoaiHopDong NOT IN ( 'nb', 'sh' ))) THEN SoTienThayDoi ELSE 0 END) TienHDNB
            FROM dbo.ThucChay_PerformanceBase_ThayDoi tcpbtd
            WHERE DeletedStatus = 0
                  AND (LoaiGhiNhan IN ( 0, 1 ) OR LoaiGhiNhan IS NULL)
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
                   (CASE WHEN( LoaiGhiNhan = 1 AND SoTienThayDoi <> 0) THEN SoTienThayDoi ELSE 0 END ) TienTDGP,
                   (CASE WHEN((LoaiGhiNhan = 0 OR LoaiGhiNhan IS NULL) AND TienThucChayKPI <> 0) THEN TienThucChayKPI ELSE 0 END ) TienKPI,
                   (CASE WHEN((LoaiGhiNhan = 0 OR LoaiGhiNhan IS NULL) AND SoTienThayDoi <> 0 AND EXISTS( SELECT MaLoaiHopDong FROM DmLoaiHopDongNoiBo WHERE SoHopDong LIKE MaLoaiHopDong + '%' AND MaLoaiHopDong NOT IN ( 'nb', 'sh' ))) THEN SoTienThayDoi  ELSE 0 END) TienHDNB
            FROM dbo.ThucChay_PerformanceBase_ThayDoi tcpbtd
            WHERE DeletedStatus = 0
                  AND(LoaiGhiNhan IN ( 0, 1 ) OR LoaiGhiNhan IS NULL)
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
               adx.TongTien TongTien_SP,
               a.TongTien AS TongTien,
               ROUND(adx.TongTien - a.TongTien, 0) AS ChenhLech
        FROM
        (
            SELECT DmSanPhamREF,
                   TenSanPham,
                   DmViTriREF,
                   TenViTri,
                   SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS TongTien
            FROM dbo.ThucChayDaTinh tbtcdt
            WHERE NgayThucHien
                  BETWEEN @StartDate AND @EndDate
                  AND TenMaHopDong NOT IN ( 'nb', 'sh' )
                  AND DmSanPhamREF IN ( 144, 628, 585 )
                  AND NOT ( DmHinhThucQuangCao IN ( 13, 42 ) OR DmLoaiBannerREF = 18)
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
            FROM dbo.ThucChayAdmarket_PhanBo a1
            WHERE NgayThucHien
                  BETWEEN @StartDate AND @EndDate
                  AND DmSanPhamREF IN ( 585, 144 )
                  AND ISNULL(isnoibo, 0) = 0
                  AND a.TenSanPham = a1.TenSanPham
                  AND a.TenViTri = a1.TenViTri
            GROUP BY TenSanPham,
                     TenViTri,
                     isnoibo
        ) adx),

	cttcdte --Lấy ra các thực chạy đã tính có các kpi
    AS (SELECT a.DmSanPhamREF,
               a.TenSanPham,
               a.DmViTriREF,
               a.TenViTri,
               adx.TongTien TongTien_SP,
               (a.TongTien) AS TongTien,
               ROUND(adx.TongTien - a.TongTien, 0) AS ChenhLech
        FROM
        (
            SELECT DmSanPhamREF,
                   TenSanPham,
                   DmViTriREF,
                   TenViTri,
                   SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)  AS TongTien
            FROM dbo.ThucChayDaTinh tbtcdt
            WHERE NgayThucHien
                  BETWEEN @StartDate AND @EndDate
                  AND TenMaHopDong NOT IN ( 'nb', 'sh' )
                  AND DmSanPhamREF IN ( 144, 628, 585 )
                  AND NOT ( DmHinhThucQuangCao IN ( 13, 42 )OR DmLoaiBannerREF = 18)
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
            FROM dbo.ThucChayAdmarket_PhanBo a1
            WHERE NgayThucHien
                  BETWEEN @StartDate AND @EndDate
                  AND DmSanPhamREF IN ( 585, 144 )
                  AND ISNULL(isnoibo, 0) = 0
                  AND a.TenSanPham = a1.TenSanPham
                  AND a.TenViTri = a1.TenViTri
            GROUP BY TenSanPham,
                     TenViTri,
                     isnoibo
        ) adx),


	ctTotalNoKPI -- tổng không có kpi
	AS (
	SELECT tcdt.DmSanPhamREF,
           tcdt.TenSanPham,
           tcdt.DmViTriREF,
           tcdt.TenViTri,
           ISNULL(tcdt.TongTien_SP, 0) AS TongTien_SP,
           ISNULL(tcdt.TongTien, 0) AS TongTien,
           ROUND((ISNULL(td.TienTDGP, 0) + ISNULL(td.TienKPI, 0) + ISNULL(td.TienHDNB, 0)) , 0) AS TongTienDieuChinh,
           ISNULL(tcdt.ChenhLech, 0) ChenhLech
    FROM cttcdta tcdt
        LEFT JOIN ctda td WITH (NOLOCK)
            ON tcdt.DmSanPhamREF = td.DmSanPhamREF
               AND tcdt.DmViTriREF = td.DmViTriREF
               AND tcdt.TenViTri = td.TenViTri
			 ),

	ctTotalInKPI -- tổng có kpi
	AS (
	SELECT tcdt.DmSanPhamREF,
           tcdt.TenSanPham,
           tcdt.DmViTriREF,
           tcdt.TenViTri,
           ISNULL(tcdt.TongTien_SP, 0) AS TongTien_SP,
           ISNULL(tcdt.TongTien, 0) AS TongTien,
           ROUND((ISNULL(td.TienTDGP, 0) + ISNULL(td.TienKPI, 0) + ISNULL(td.TienHDNB, 0)) , 0) AS TongTienDieuChinh,
           ISNULL(tcdt.ChenhLech, 0) ChenhLech
    FROM cttcdte tcdt
        LEFT JOIN ctde td WITH (NOLOCK)
            ON tcdt.DmSanPhamREF = td.DmSanPhamREF
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
    FROM dbo.ThucChayAdmarket_PhanBo
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
    FROM dbo.ThucChayAdmarket_PhanBo
    WHERE NgayThucHien
          BETWEEN @StartDate AND @EndDate
          AND DmSanPhamREF = 585
    GROUP BY TenSanPham,
             TenViTri,
             isnoibo
    ORDER BY TenViTri,
             isnoibo;
END;

```
