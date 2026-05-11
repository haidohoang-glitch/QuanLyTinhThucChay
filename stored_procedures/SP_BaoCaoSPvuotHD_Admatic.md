# Stored Procedure: `BaoCaoSPvuotHD_Admatic`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-02-27 17:34:35.640000
- **Ngày sửa cuối**: 2026-03-02 14:54:32.453000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Nam` | `int(4)` | No |
| `@DmLoaiREF` | `int(4)` | No |
| `@VuotToiThieu` | `float(8)` | No |
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[BaoCaoSPvuotHD_Admatic]
(
    @Nam INT = 2025,
    @DmLoaiREF INT = 42,
    @VuotToiThieu FLOAT = 1000,
    @HopDongChiTietID INT = NULL
)
AS
BEGIN
    SET NOCOUNT ON;

    -- Xóa dữ liệu cũ của Admatic
    DELETE FROM dbo.BaoCaoSPvuotHD
    WHERE NguonSP = 'Admatic';

    WITH HDCT AS
    (
        SELECT 
            CONVERT(DATE, hd.CreatedAt) AS NgayDanhSo,
            hd.SoHopDong,
            hd.HopDongID,
            hdct.HopDongChiTietID,
            hdct.DmSanPhamREF,
            hdct.TenSanPham,
            hdct.TenLoaiBanner,
            hdct.TenLoai,
            hdct.SoLuong,
            hdct.DonGia,
            hdct.ChietKhau,
            hdct.DmLoaiREF,
            hdct.DmViTriREF,
            hdct.TenViTri,
            hdct.DonViTinh,

            CASE 
                WHEN hdct.ChietKhau = 100 
                    THEN hdct.SoLuong * hdct.DonGia
                ELSE hdct.ThanhTien
            END AS ThanhTien_HD

        FROM dbo.HopDongChiTiet hdct
        INNER JOIN dbo.HopDong hd 
            ON hd.HopDongID = hdct.HopDongFK

        WHERE hd.TrangThaiHopDong <> 3
            AND hdct.DeletedStatus = 0
            AND hdct.DmLoaiREF = @DmLoaiREF            
            AND hdct.DmSanPhamREF NOT IN (140,549,817)
            AND hd.Nam >= @Nam
            AND (@HopDongChiTietID IS NULL 
                 OR hdct.HopDongChiTietID = @HopDongChiTietID)
    )

    INSERT INTO dbo.BaoCaoSPvuotHD
    (
        NgayDanhso,
        SoHopDong,
        HopDongID,
        HopDongChiTietID,
        DmLoaiREF,
        htqc,
        DmSanPhamREF,
        TenSanPham,
        TenLoaiBanner,
        DmViTriREF,
        TenViTri,
        SoLuong,
        DonViTinh,
        DonGia,
        ChietKhau,
        ThanhTien,
        SoLuong_SP,
        ThucChayBanSP,
        Lech,
        TyLeVuot,
        CreatedDate,
        NguonSP
    )

    SELECT
        A.NgayDanhSo,
        A.SoHopDong,
        A.HopDongID,
        A.HopDongChiTietID,
        A.DmLoaiREF,
        A.TenLoai,
        A.DmSanPhamREF,
        A.TenSanPham,
        A.TenLoaiBanner,
        A.DmViTriREF,
        A.TenViTri,
        A.SoLuong,
        A.DonViTinh,
        A.DonGia,
        A.ChietKhau,

        Calc.ThanhTien_HD,
        Calc.SoLuong_SP,
        Calc.ThanhTien_SP,
        Calc.VuotHD,

        ROUND(
			(Calc.ThanhTien_SP - Calc.ThanhTien_HD) * 100.0 
			/ NULLIF(Calc.ThanhTien_HD,0)
		, 2) AS TyLeVuot,

        GETDATE(),
        'Admatic'

    FROM HDCT A

    INNER JOIN
    (
        SELECT  
            map.HopDongChiTietREF,
            SUM(CONVERT(FLOAT, t.SoLuongThucChay)) AS SLTC_SP,
            SUM(CONVERT(FLOAT, t.SoLuongThucChayKM)) AS SLKM_SP,
            SUM(CONVERT(FLOAT, t.ThanhTienThucChaySauCK_ChuaVAT)) AS TC_SP,
            SUM(CONVERT(FLOAT, t.ThanhTienThucChayKM)) AS KM_SP
        FROM dbo.ThucChay_ThanhTien_Admatic t
        INNER JOIN dbo.ThucChayHopDongChiTiet map 
            ON CAST(t.DmBannerID AS NVARCHAR(50)) = map.DmBannerREF
            AND map.DmSanPhamREF = t.DmSanPhamREF
            AND map.DeletedStatus = 0
            AND map.DmSanPhamREF NOT IN (140,549,817)
        GROUP BY map.HopDongChiTietREF
    ) B
        ON A.HopDongChiTietID = B.HopDongChiTietREF

    CROSS APPLY
    (
        SELECT
            ThanhTien_HD = A.ThanhTien_HD,

            SoLuong_SP =
                CASE WHEN A.ChietKhau = 100
                     THEN B.SLKM_SP
                     ELSE B.SLTC_SP
                END,

            ThanhTien_SP =
                CASE WHEN A.ChietKhau = 100
                     THEN B.KM_SP
                     ELSE B.TC_SP
                END,

            VuotHD =
                (CASE WHEN A.ChietKhau = 100
                      THEN B.KM_SP
                      ELSE B.TC_SP
                 END)
                - A.ThanhTien_HD
    ) Calc

    WHERE ROUND(Calc.VuotHD, 0) > @VuotToiThieu

END

```
