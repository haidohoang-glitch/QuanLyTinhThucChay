# Stored Procedure: `RaSoat_DL_TongViTriPerformanceBase_Thang_PhanBo`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2024-04-17 11:45:05.943000
- **Ngày sửa cuối**: 2025-12-02 16:48:46.387000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Startdate` | `date(3)` | No |
| `@Todate` | `date(3)` | No |
| `@Type` | `tinyint(1)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[RaSoat_DL_TongViTriPerformanceBase_Thang_PhanBo]
    @Startdate DATE    = NULL,
    @Todate    DATE    = NULL,
    @Type      TINYINT = NULL   -- 1: đầu tháng -> 24, 2: đầu tháng -> cuối tháng
AS
BEGIN
    SET NOCOUNT ON;

    -------------------------------------------------------------------------
    -- Xử lý khoảng ngày theo @Type (tháng lấy theo ngày hôm trước)
    -------------------------------------------------------------------------
    IF @Type IN (1, 2)
    BEGIN
        DECLARE @BaseDate  DATE = DATEADD(DAY, -1, CAST(GETDATE() AS DATE)); -- Ngày hôm trước
        DECLARE @Year      INT  = YEAR(@BaseDate);
        DECLARE @Month     INT  = MONTH(@BaseDate);

        -- Đầu tháng kỳ báo cáo
        SET @Startdate = DATEFROMPARTS(@Year, @Month, 1);

        IF @Type = 1
        BEGIN
            SET @Todate = DATEFROMPARTS(@Year, @Month, 24);
        END
        ELSE IF @Type = 2
        BEGIN
            SET @Todate = EOMONTH(@BaseDate);
        END
    END

    -------------------------------------------------------------------------
    -- MainData CTE
    -------------------------------------------------------------------------
    ;WITH MainData AS (
        SELECT 
            B.TenSanPham,
            B.TenViTri,
            ISNULL(CONVERT(FLOAT, B.ThucChaySanPham_ChuaVAT), 0) AS ThucChaySanPham_ChuaVAT,
            ISNULL(B.ThanhTienThucChay_ChuaVAT, 0) AS ThanhTienThucChay_ChuaVAT,
            ISNULL(B.TDGPToltal, 0) AS TDGPToltal,
            ISNULL(CONVERT(FLOAT, C.ThanhTienThucChayHDNB_ChuaVAT), 0) AS TTThucChayHDNB_ChuaVAT,
            ISNULL(
                CONVERT(FLOAT, B.ThanhTienThucChay_ChuaVAT - ISNULL(C.ThanhTienThucChayHDNB_ChuaVAT, 0)),
                B.ThanhTienThucChay_ChuaVAT
            ) AS TTThucChayKhongHDNB_ChuaVAT
        FROM
        (
            SELECT 
                A.TenSanPham,
                A.TenViTri,
                A.DmViTriREF,
                A.DmSanPhamREF,
                A.ThanhTienThucChay_ChuaVAT,
                A.ThucChaySanPham_ChuaVAT,
                ISNULL(TDGPToltal.TDGPToltal, 0) AS TDGPToltal
            FROM
            (
                SELECT 
                    tcadmrket.TenSanPham,
                    tcadmrket.TenViTri,
                    tcadmrket.DmViTriREF,
                    tcadmrket.DmSanPhamREF,
                    tcadmrket.ThanhTienThucChay_ChuaVAT,
                    tcsp.ThucChaySanPham_ChuaVAT
                FROM
                (
                    SELECT 
                        TenSanPham,
                        TenViTri,
                        DmViTriREF,
                        DmSanPhamREF,
                        SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS ThanhTienThucChay_ChuaVAT
                    FROM dbo.ThucChayDaTinhAdmarket
                    WHERE NgayThucHien BETWEEN @Startdate AND @Todate
                        AND DmSanPhamREF IN (628, 144, 585)
                        AND DmHinhThucQuangCao <> 42
                    GROUP BY TenSanPham, TenViTri, DmViTriREF, DmSanPhamREF
                ) tcadmrket
                FULL JOIN
                (
                    SELECT 
                        TenSanPham,
                        TenViTri,
                        DmViTriREF,
                        ISNULL(SUM(CONVERT(FLOAT, domain_tt_money)), 0) AS ThucChaySanPham_ChuaVAT
                    FROM dbo.ThucChayAdmarket_PhanBo
                    WHERE NgayThucHien BETWEEN @Startdate AND @Todate
                    GROUP BY TenSanPham, TenViTri, DmViTriREF
                ) tcsp
                    ON tcsp.DmViTriREF = tcadmrket.DmViTriREF
            ) A
            FULL JOIN
            (
                SELECT 
                    ak.TenSanPham,
                    ak.DmSanPhamREF,
                    ak.TenViTri,
                    ak.DmViTriREF,
                    SUM(ak.ThanhTienSauTrietKhauThucChay + ak.GiaTriThayDoi) AS TDGPToltal
                FROM dbo.ThucChayDaTinhAdmarket ak
                WHERE ak.NgayThucHien BETWEEN @Startdate AND @Todate
                    AND ak.GhiChu LIKE '%ThangDuGP%'
                GROUP BY ak.TenSanPham, ak.DmSanPhamREF, ak.TenViTri, ak.DmViTriREF
            ) TDGPToltal
                ON A.DmViTriREF   = TDGPToltal.DmViTriREF
               AND A.TenViTri     = TDGPToltal.TenViTri
               AND A.DmSanPhamREF = TDGPToltal.DmSanPhamREF
        ) B
        FULL JOIN
        (
            SELECT 
                TenSanPham,
                TenViTri,
                DmViTriREF,
                DmSanPhamREF,
                ISNULL(SUM(CONVERT(FLOAT, ThanhTienSauTrietKhauThucChay + GiaTriThayDoi)), 0) AS ThanhTienThucChayHDNB_ChuaVAT
            FROM dbo.ThucChayDaTinhAdmarket
            WHERE NgayThucHien BETWEEN @Startdate AND @Todate
                AND DmSanPhamREF IN (628, 144, 585)
                AND DmHinhThucQuangCao <> 42
                AND DmMaHopDongREF IN (
                    SELECT DmLoaiHopDongREF 
                    FROM DmLoaiHopDongNoiBo 
                    WHERE DeletedStatus = 0
                )
            GROUP BY TenSanPham, TenViTri, DmViTriREF, DmSanPhamREF
        ) C
            ON C.DmViTriREF   = B.DmViTriREF
           AND C.TenViTri     = B.TenViTri
           AND C.DmSanPhamREF = B.DmSanPhamREF
    )

    -------------------------------------------------------------------------
    -- Result set 1: Data + dòng Tổng
    -------------------------------------------------------------------------
    SELECT 
        TenSanPham,
        TenViTri,
        dbo.FormatNumber(ThucChaySanPham_ChuaVAT)     AS ThucChaySanPham_ChuaVAT,
        dbo.FormatNumber(ThanhTienThucChay_ChuaVAT)   AS TTThucChayAllCaHDNB_ChuaVAT,
        dbo.FormatNumber(TDGPToltal)                  AS TDGPToltal,
        dbo.FormatNumber(TTThucChayHDNB_ChuaVAT)      AS TTThucChayHDNB_ChuaVAT,
        dbo.FormatNumber(TTThucChayKhongHDNB_ChuaVAT) AS TTThucChayKhongHDNB_ChuaVAT
    FROM MainData

    UNION ALL

    SELECT 
        N'Tổng',
        N'',
        dbo.FormatNumber(SUM(ThucChaySanPham_ChuaVAT)),
        dbo.FormatNumber(SUM(ThanhTienThucChay_ChuaVAT)),
        dbo.FormatNumber(SUM(TDGPToltal)),
        dbo.FormatNumber(SUM(TTThucChayHDNB_ChuaVAT)),
        dbo.FormatNumber(SUM(TTThucChayKhongHDNB_ChuaVAT))
    FROM MainData;

    -------------------------------------------------------------------------
    -- Result set 2: 1 dòng kỳ báo cáo (4 cột)
    -------------------------------------------------------------------------
    SELECT 
        @Startdate          AS DateFrom,
        @Todate             AS DateTo,
        MONTH(@Startdate)   AS ThangBaoCao,
        YEAR(@Startdate)    AS NamBaoCao;
END;

```
