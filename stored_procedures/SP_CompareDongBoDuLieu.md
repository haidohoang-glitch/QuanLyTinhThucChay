# Stored Procedure: `CompareDongBoDuLieu`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-11-07 15:18:33.270000
- **Ngày sửa cuối**: 2026-03-18 08:49:13.303000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayKetThuc` | `datetime(8)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[CompareDongBoDuLieu]
(    
    @NgayKetThuc   DATETIME
)
AS
BEGIN
    SET NOCOUNT ON;

    ------------------------------------------------------------
    -- 1. ThucChayDaTinh: So sánh DB Release vs DB Hiện Tại
    ------------------------------------------------------------
	DECLARE @NgayBatDau DATETIME
	SET @NgayBatDau = DATEFROMPARTS(YEAR(@NgayKetThuc), 1, 1)

    ;WITH TCDT_Release AS
    (
        SELECT
              t.DmSanPhamREF
            , t.TenSanPham
            , t.SoHopDong
            , t.HopDongID
            , t.HopDongChiTietREF
            , t.DonViTinh
            , t.DmHinhThucQuangCao
            , t.NgayThucHien
            , SUM(ISNULL(t.SoLuongThucChay, 0) + ISNULL(t.SoLuongThayDoi, 0))                       AS SoLuongThucChay
            , SUM(ISNULL(t.SoLuongThucChayKM, 0) + ISNULL(t.SoLuongKMThayDoi, 0))                    AS SoLuongKM
            , SUM(ISNULL(t.ThanhTienSauTrietKhauThucChay, 0))                                        AS ThanhTienSauTrietKhauThucChay
            , SUM(ISNULL(t.GiaTriThayDoi, 0))                                                        AS GiaTriThayDoi
            , SUM(ISNULL(t.ThanhTienKM, 0) + ISNULL(t.GiaTriKMThayDoi, 0))                           AS ThanhTienThucChayKM
            , SUM(ISNULL(t.ThanhTienLechTreoHa, 0))                                                  AS ThanhTienLechTreoHa
        FROM [ASDAG2].ABM_Data_Release.dbo.ThucChayDaTinh t
        WHERE t.NgayThucHien BETWEEN @NgayBatDau AND @NgayKetThuc
        GROUP BY
              t.DmSanPhamREF
            , t.TenSanPham
            , t.SoHopDong
            , t.NgayThucHien
            , t.HopDongID
            , t.HopDongChiTietREF
            , t.DonViTinh
            , t.DmHinhThucQuangCao
    ),
    TCDT_Current AS
    (
        SELECT
              t.DmSanPhamREF
            , t.TenSanPham
            , t.SoHopDong
            , t.HopDongID
            , t.HopDongChiTietREF
            , t.DonViTinh
            , t.DmHinhThucQuangCao
            , t.NgayThucHien
            , SUM(ISNULL(t.SoLuongThucChay, 0) + ISNULL(t.SoLuongThayDoi, 0))                       AS SoLuongThucChay
            , SUM(ISNULL(t.SoLuongThucChayKM, 0) + ISNULL(t.SoLuongKMThayDoi, 0))                    AS SoLuongKM
            , SUM(ISNULL(t.ThanhTienSauTrietKhauThucChay, 0))                                        AS ThanhTienSauTrietKhauThucChay
            , SUM(ISNULL(t.GiaTriThayDoi, 0))                                                        AS GiaTriThayDoi
            , SUM(ISNULL(t.ThanhTienKM, 0) + ISNULL(t.GiaTriKMThayDoi, 0))                           AS ThanhTienThucChayKM
            , SUM(ISNULL(t.ThanhTienLechTreoHa, 0))                                                  AS ThanhTienLechTreoHa
        FROM dbo.ThucChayDaTinh t
        WHERE t.NgayThucHien BETWEEN @NgayBatDau AND @NgayKetThuc
        GROUP BY
              t.DmSanPhamREF
            , t.TenSanPham
            , t.SoHopDong
            , t.NgayThucHien
            , t.HopDongID
            , t.HopDongChiTietREF
            , t.DonViTinh
            , t.DmHinhThucQuangCao
    )
    SELECT
          A.*
        , B.*
        , ISNULL(A.SoLuongThucChay, 0)           - ISNULL(B.SoLuongThucChay, 0)           AS LechSLTC
        , ISNULL(A.SoLuongKM, 0)                 - ISNULL(B.SoLuongKM, 0)                 AS LechSLKM
        , ISNULL(A.ThanhTienSauTrietKhauThucChay,0) - ISNULL(B.ThanhTienSauTrietKhauThucChay,0) AS LechTTSCK
        , ISNULL(A.GiaTriThayDoi, 0)             - ISNULL(B.GiaTriThayDoi, 0)             AS LechGTTD
        , ISNULL(A.ThanhTienThucChayKM, 0)       - ISNULL(B.ThanhTienThucChayKM, 0)       AS LechTTTCKM
        , ISNULL(A.ThanhTienLechTreoHa, 0)       - ISNULL(B.ThanhTienLechTreoHa, 0)       AS LechTTLechTreoHa
    FROM TCDT_Release A
    FULL OUTER JOIN TCDT_Current B
        ON  A.DmSanPhamREF        = B.DmSanPhamREF
        AND A.TenSanPham          = B.TenSanPham
        AND A.SoHopDong           = B.SoHopDong
        AND A.NgayThucHien        = B.NgayThucHien
        AND A.HopDongID           = B.HopDongID
        AND A.HopDongChiTietREF   = B.HopDongChiTietREF
        AND ISNULL(A.DonViTinh, '') = ISNULL(B.DonViTinh, '')
        AND A.DmHinhThucQuangCao  = B.DmHinhThucQuangCao
    WHERE
           ROUND(ISNULL(A.SoLuongThucChay, 0) - ISNULL(B.SoLuongThucChay, 0), 0) <> 0
        OR ROUND(ISNULL(A.SoLuongKM, 0)         - ISNULL(B.SoLuongKM, 0), 0)         <> 0
        OR ROUND(ISNULL(A.ThanhTienSauTrietKhauThucChay, 0)
                 - ISNULL(B.ThanhTienSauTrietKhauThucChay, 0), 0)                    <> 0
        OR ROUND(ISNULL(A.GiaTriThayDoi, 0), 0)
                 - ROUND(ISNULL(B.GiaTriThayDoi, 0), 0)                              <> 0
        OR ROUND(ISNULL(A.ThanhTienThucChayKM, 0)
                 - ISNULL(B.ThanhTienThucChayKM, 0), 0)                              <> 0
        OR A.DmSanPhamREF IS NULL
        OR B.DmSanPhamREF IS NULL
        OR A.SoHopDong   IS NULL
        OR B.SoHopDong   IS NULL;

    ------------------------------------------------------------
    -- 2. ThucChayDaTinhAdmarket
    ------------------------------------------------------------
    ;WITH TCDTAd_Release AS
    (
        SELECT
              t.DmSanPhamREF
            , t.TenSanPham
            , t.SoHopDong
            , t.NgayThucHien
            , SUM(ISNULL(t.SoLuongThucChay, 0) + ISNULL(t.SoLuongThayDoi, 0))       AS SoLuongThucChay
            , SUM(ISNULL(t.SoLuongThucChayKM, 0) + ISNULL(t.SoLuongKMThayDoi, 0))   AS SoLuongKM
            , SUM(ISNULL(t.ThanhTienSauTrietKhauThucChay, 0))                       AS ThanhTienSauTrietKhauThucChay
            , SUM(ISNULL(t.GiaTriThayDoi, 0))                                       AS GiaTriThayDoi
            , SUM(ISNULL(t.ThanhTienKM, 0) + ISNULL(t.GiaTriKMThayDoi, 0))          AS ThanhTienThucChayKM
        FROM [ASDAG2].ABM_Data_Release.dbo.ThucChayDaTinhAdmarket t
        WHERE t.NgayThucHien BETWEEN @NgayBatDau AND @NgayKetThuc
        GROUP BY
              t.DmSanPhamREF
            , t.TenSanPham
            , t.SoHopDong
            , t.NgayThucHien
    ),
    TCDTAd_Current AS
    (
        SELECT
              t.DmSanPhamREF
            , t.TenSanPham
            , t.SoHopDong
            , t.NgayThucHien
            , SUM(ISNULL(t.SoLuongThucChay, 0) + ISNULL(t.SoLuongThayDoi, 0))       AS SoLuongThucChay
            , SUM(ISNULL(t.SoLuongThucChayKM, 0) + ISNULL(t.SoLuongKMThayDoi, 0))   AS SoLuongKM
            , SUM(ISNULL(t.ThanhTienSauTrietKhauThucChay, 0))                       AS ThanhTienSauTrietKhauThucChay
            , SUM(ISNULL(t.GiaTriThayDoi, 0))                                       AS GiaTriThayDoi
            , SUM(ISNULL(t.ThanhTienKM, 0) + ISNULL(t.GiaTriKMThayDoi, 0))          AS ThanhTienThucChayKM
        FROM dbo.ThucChayDaTinhAdmarket t
        WHERE t.NgayThucHien BETWEEN @NgayBatDau AND @NgayKetThuc
        GROUP BY
              t.DmSanPhamREF
            , t.TenSanPham
            , t.SoHopDong
            , t.NgayThucHien
    )
    SELECT
          A.*
        , B.*
        , ISNULL(A.SoLuongThucChay, 0)           - ISNULL(B.SoLuongThucChay, 0)           AS LechSLTC
        , ISNULL(A.SoLuongKM, 0)                 - ISNULL(B.SoLuongKM, 0)                 AS LechSLKM
        , ISNULL(A.ThanhTienSauTrietKhauThucChay,0) - ISNULL(B.ThanhTienSauTrietKhauThucChay,0) AS LechTTSCK
        , ISNULL(A.GiaTriThayDoi, 0)             - ISNULL(B.GiaTriThayDoi, 0)             AS LechGTTD
        , ISNULL(A.ThanhTienThucChayKM, 0)       - ISNULL(B.ThanhTienThucChayKM, 0)       AS LechTTTCKM
    FROM TCDTAd_Release A
    FULL OUTER JOIN TCDTAd_Current B
        ON  A.DmSanPhamREF = B.DmSanPhamREF
        AND A.TenSanPham   = B.TenSanPham
        AND A.SoHopDong    = B.SoHopDong
        AND A.NgayThucHien = B.NgayThucHien
    WHERE
           ROUND(ISNULL(A.SoLuongThucChay, 0) - ISNULL(B.SoLuongThucChay, 0), 0) <> 0
        OR ROUND(ISNULL(A.SoLuongKM, 0)       - ISNULL(B.SoLuongKM, 0), 0)       <> 0
        OR ROUND(ISNULL(A.ThanhTienSauTrietKhauThucChay, 0)
                 - ISNULL(B.ThanhTienSauTrietKhauThucChay, 0), 0)                <> 0
        OR ROUND(ISNULL(A.GiaTriThayDoi, 0)   - ISNULL(B.GiaTriThayDoi, 0), 0)   <> 0
        OR ROUND(ISNULL(A.ThanhTienThucChayKM, 0)
                 - ISNULL(B.ThanhTienThucChayKM, 0), 0)                          <> 0
        OR A.DmSanPhamREF IS NULL
        OR B.DmSanPhamREF IS NULL
        OR A.SoHopDong    IS NULL
        OR B.SoHopDong    IS NULL;

    ------------------------------------------------------------
    -- 3. ABM_Data_Partner.ThucChayAdmarketPublisher
    ------------------------------------------------------------
    ;WITH Pub_Release AS
    (
        SELECT
              t.DmHinhThucQuangCao
            , t.DmSanPhamREF
            , t.TenSanPham
            , t.DmWebsiteREF
            , t.TenWebsite
            , t.NgayThucHien
            , SUM(ISNULL(t.ttClick, 0)) AS tc
            , SUM(ISNULL(t.ttView,  0)) AS tv
        FROM [ASDAG2].ABM_Data_Partner.dbo.ThucChayAdmarketPublisher t
        WHERE t.NgayThucHien BETWEEN @NgayBatDau AND @NgayKetThuc
        GROUP BY
              t.DmHinhThucQuangCao
            , t.DmSanPhamREF
            , t.TenSanPham
            , t.DmWebsiteREF
            , t.TenWebsite
            , t.NgayThucHien
    ),
    Pub_Current AS
    (
        SELECT
              t.DmHinhThucQuangCao
            , t.DmSanPhamREF
            , t.TenSanPham
            , t.DmWebsiteREF
            , t.TenWebsite
            , t.NgayThucHien
            , SUM(ISNULL(t.ttClick, 0)) AS tc
            , SUM(ISNULL(t.ttView,  0)) AS tv
        FROM ABM_Data_Partner.dbo.ThucChayAdmarketPublisher t
        WHERE t.NgayThucHien BETWEEN @NgayBatDau AND @NgayKetThuc
        GROUP BY
              t.DmHinhThucQuangCao
            , t.DmSanPhamREF
            , t.TenSanPham
            , t.DmWebsiteREF
            , t.TenWebsite
            , t.NgayThucHien
    )
    SELECT
          A.*
        , B.*
    FROM Pub_Release A
    FULL OUTER JOIN Pub_Current B
        ON  A.DmHinhThucQuangCao = B.DmHinhThucQuangCao
        AND A.DmWebsiteREF       = B.DmWebsiteREF
        AND A.DmSanPhamREF       = B.DmSanPhamREF
        AND A.TenWebsite         = B.TenWebsite
        AND A.TenSanPham         = B.TenSanPham
        AND A.NgayThucHien       = B.NgayThucHien
    WHERE
           ROUND(ISNULL(A.tc, 0) - ISNULL(B.tc, 0), 0) <> 0
        OR ROUND(ISNULL(A.tv, 0) - ISNULL(B.tv, 0), 0) <> 0
        OR A.DmSanPhamREF IS NULL
        OR B.DmSanPhamREF IS NULL
       AND A.DmWebsiteREF IN (85, 3144, 134, 3134, 182, 3136, 254, 3139);

    ------------------------------------------------------------
    -- 4. ThucChayDaTinh_MuaNgoai
    ------------------------------------------------------------
    ;WITH TCMuaNgoai_Release AS
    (
        SELECT
              t.ID
            , t.HopDongREF
            , t.SoHopDong
            , t.DmNhanVienREF
            , t.TenDangNhap
            , t.DmKhachHangREF
            , t.HopDongChiTietREF
            , t.LstDmNhanHangREF
            , t.DmHinhThucQuangCaoREF
            , t.DmSanPhamREF
            , t.DmLoaiBannerREF
            , t.ThucChayMuaNgoaiChiTietREF
            , t.DmWebsiteREF
            , t.NgayThucHien
            , SUM(ISNULL(t.SoLuongThucChay, 0) + ISNULL(t.SoLuongThayDoi, 0))                    AS SoLuongThucChay
            , SUM(ISNULL(t.SoLuongThucChayKM, 0) + ISNULL(t.SoLuongKMThayDoi, 0))                AS SoLuongKM
            , SUM(ISNULL(t.ThanhTienLaiThucChaySauCK, 0))                                        AS ThanhTienLaiThucChaySauCK
            , SUM(ISNULL(t.GiaTriThayDoiLaiSauCK, 0))                                            AS GiaTriThayDoiLai
            , SUM(ISNULL(t.ThanhTienLaiThucChayKM, 0) + ISNULL(t.GiaTriKMLaiThayDoi, 0))         AS ThanhTienLaiThucChayKM
        FROM [ASDAG2].ABM_Data_Release.dbo.ThucChayDaTinh_MuaNgoai t
        WHERE t.NgayThucHien BETWEEN @NgayBatDau AND @NgayKetThuc
        GROUP BY
              t.ID
            , t.HopDongREF
            , t.SoHopDong
            , t.DmNhanVienREF
            , t.TenDangNhap
            , t.DmKhachHangREF
            , t.HopDongChiTietREF
            , t.LstDmNhanHangREF
            , t.DmHinhThucQuangCaoREF
            , t.DmSanPhamREF
            , t.DmLoaiBannerREF
            , t.ThucChayMuaNgoaiChiTietREF
            , t.DmWebsiteREF
            , t.NgayThucHien
    ),
    TCMuaNgoai_Current AS
    (
        SELECT
              t.ID
            , t.HopDongREF
            , t.SoHopDong
            , t.DmNhanVienREF
            , t.TenDangNhap
            , t.DmKhachHangREF
            , t.HopDongChiTietREF
            , t.LstDmNhanHangREF
            , t.DmHinhThucQuangCaoREF
            , t.DmSanPhamREF
            , t.DmLoaiBannerREF
            , t.ThucChayMuaNgoaiChiTietREF
            , t.DmWebsiteREF
            , t.NgayThucHien
            , SUM(ISNULL(t.SoLuongThucChay, 0) + ISNULL(t.SoLuongThayDoi, 0))                    AS SoLuongThucChay
            , SUM(ISNULL(t.SoLuongThucChayKM, 0) + ISNULL(t.SoLuongKMThayDoi, 0))                AS SoLuongKM
            , SUM(ISNULL(t.ThanhTienLaiThucChaySauCK, 0))                                        AS ThanhTienLaiThucChaySauCK
            , SUM(ISNULL(t.GiaTriThayDoiLaiSauCK, 0))                                            AS GiaTriThayDoiLai
            , SUM(ISNULL(t.ThanhTienLaiThucChayKM, 0) + ISNULL(t.GiaTriKMLaiThayDoi, 0))         AS ThanhTienLaiThucChayKM
        FROM dbo.ThucChayDaTinh_MuaNgoai t
        WHERE t.NgayThucHien BETWEEN @NgayBatDau AND @NgayKetThuc
        GROUP BY
              t.ID
            , t.HopDongREF
            , t.SoHopDong
            , t.DmNhanVienREF
            , t.TenDangNhap
            , t.DmKhachHangREF
            , t.HopDongChiTietREF
            , t.LstDmNhanHangREF
            , t.DmHinhThucQuangCaoREF
            , t.DmSanPhamREF
            , t.DmLoaiBannerREF
            , t.ThucChayMuaNgoaiChiTietREF
            , t.DmWebsiteREF
            , t.NgayThucHien
    )
    SELECT
          A.*
        , B.*
        , ISNULL(A.SoLuongThucChay, 0)           - ISNULL(B.SoLuongThucChay, 0)           AS LechSLTC
        , ISNULL(A.SoLuongKM, 0)                 - ISNULL(B.SoLuongKM, 0)                 AS LechSLKM
        , ISNULL(A.ThanhTienLaiThucChaySauCK, 0) - ISNULL(B.ThanhTienLaiThucChaySauCK, 0) AS LechLaiSCK
        , ISNULL(A.GiaTriThayDoiLai, 0)          - ISNULL(B.GiaTriThayDoiLai, 0)          AS LechLaiGTTD
        , ISNULL(A.ThanhTienLaiThucChayKM, 0)    - ISNULL(B.ThanhTienLaiThucChayKM, 0)    AS LechLaiTCKM
    FROM TCMuaNgoai_Release A
    FULL OUTER JOIN TCMuaNgoai_Current B
        ON  A.ID                         = B.ID
        AND A.HopDongREF                 = B.HopDongREF
        AND A.SoHopDong                  = B.SoHopDong
        AND A.DmNhanVienREF              = B.DmNhanVienREF
        AND A.TenDangNhap                = B.TenDangNhap
        AND A.DmKhachHangREF             = B.DmKhachHangREF
        AND A.HopDongChiTietREF          = B.HopDongChiTietREF
        AND ISNULL(A.LstDmNhanHangREF,0) = ISNULL(B.LstDmNhanHangREF,0)
        AND A.DmHinhThucQuangCaoREF      = B.DmHinhThucQuangCaoREF
        AND A.DmLoaiBannerREF            = B.DmLoaiBannerREF
        AND A.ThucChayMuaNgoaiChiTietREF = B.ThucChayMuaNgoaiChiTietREF
        AND ISNULL(A.DmWebsiteREF,0)     = ISNULL(B.DmWebsiteREF,0)
        AND A.NgayThucHien               = B.NgayThucHien
        AND A.DmSanPhamREF               = B.DmSanPhamREF
    WHERE
           ROUND(ISNULL(A.SoLuongThucChay, 0)           - ISNULL(B.SoLuongThucChay, 0), 0)           <> 0
        OR ROUND(ISNULL(A.SoLuongKM, 0)                 - ISNULL(B.SoLuongKM, 0), 0)                 <> 0
        OR ROUND(ISNULL(A.ThanhTienLaiThucChaySauCK, 0) - ISNULL(B.ThanhTienLaiThucChaySauCK, 0), 0) <> 0
        OR ROUND(ISNULL(A.GiaTriThayDoiLai, 0), 0)
             - ROUND(ISNULL(B.GiaTriThayDoiLai, 0), 0)                                            <> 0
        OR ROUND(ISNULL(A.ThanhTienLaiThucChayKM, 0)    - ISNULL(B.ThanhTienLaiThucChayKM, 0), 0)    <> 0
        OR A.DmSanPhamREF               IS NULL
        OR B.DmSanPhamREF               IS NULL
        OR A.SoHopDong                  IS NULL
        OR B.SoHopDong                  IS NULL
        OR A.ThucChayMuaNgoaiChiTietREF IS NULL
        OR B.ThucChayMuaNgoaiChiTietREF IS NULL;

    ------------------------------------------------------------
    -- 5. WebsiteMapping_HDCN_Reporting
    ------------------------------------------------------------
    ;WITH WebMap_Release AS
    (
        SELECT DmWebsiteReportingdbID, TenWebsite
        FROM [ASDAG2].ABM_Data_Release.dbo.DmWebsiteReportingdb
        WHERE DeletedStatus = 0
    ),
    WebMap_Current AS
    (
        SELECT DmWebsiteReportingdbID, TenWebsite
        FROM dbo.DmWebsiteReportingdb
        WHERE DeletedStatus = 0
    )
    SELECT
          A.*
        , B.*
    FROM WebMap_Release A
    FULL OUTER JOIN WebMap_Current B
        ON  A.DmWebsiteReportingdbID = B.DmWebsiteReportingdbID
        AND A.TenWebsite             = B.TenWebsite
    WHERE
           A.DmWebsiteReportingdbID IS NULL
        OR B.DmWebsiteReportingdbID IS NULL
        OR A.TenWebsite             IS NULL
        OR B.TenWebsite             IS NULL;
END;

```
