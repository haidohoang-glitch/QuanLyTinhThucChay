# Stored Procedure: `sp_nhung_KT_loiSP_Admatic_Bannertreo2PB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-20 09:33:29.040000
- **Ngày sửa cuối**: 2026-04-15 09:40:53.810000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[sp_nhung_KT_loiSP_Admatic_Bannertreo2PB]
AS
BEGIN
    SET NOCOUNT ON;

    -- 🔹 Base data (lọc chuẩn 1 lần)
    WITH Base AS (
        SELECT 
            tt.DmBannerREF,
            tt.HopDongREF,
            tt.HopDongChiTietREF,
            hd.SoHopDong
        FROM ThucChayHopDongChiTiet tt
        INNER JOIN HopDongChiTiet hdct
            ON tt.HopDongChiTietREF = hdct.HopDongChiTietID
           AND hdct.DeletedStatus = 0
        INNER JOIN HopDong hd
            ON tt.HopDongREF = hd.HopDongID
        WHERE 
            tt.DmHinhThucQuangCaoREF = 42
            AND tt.DeletedStatus = 0
            AND tt.DmBannerREF IS NOT NULL
            AND tt.DmBannerREF <> 0
            AND tt.DmSanPhamREF NOT IN (817,140,560,549)
            AND hd.NgayDanhSoHopDong >= '2020-07-22'
            AND hd.Nam >= '2023'
            AND hd.SoHopDong NOT IN ('QC3820421')
    ),

    -- 🔹 Tính số HĐ & phân bổ theo banner
    BannerCheck AS (
        SELECT  
            DmBannerREF,
            COUNT(DISTINCT HopDongREF) AS SoHopDong,
            COUNT(DISTINCT HopDongChiTietREF) AS SoPhanBo
        FROM Base
        GROUP BY DmBannerREF
        HAVING 
            COUNT(DISTINCT HopDongREF) > 1
            OR COUNT(DISTINCT HopDongChiTietREF) > 1
    ),

    -- 🔹 Gắn danh sách HĐ & PB cho từng banner
    BannerDetail AS (
        SELECT
            bc.DmBannerREF,
            bc.SoHopDong,
            bc.SoPhanBo,

            -- Danh sách HĐ
            STUFF((
                SELECT DISTINCT '; ' + b2.SoHopDong
                FROM Base b2
                WHERE b2.DmBannerREF = bc.DmBannerREF
                FOR XML PATH('')
            ), 1, 2, '') AS DanhSachHopDong,

            -- Danh sách phân bổ
            STUFF((
                SELECT DISTINCT '; ' + CAST(b2.HopDongChiTietREF AS VARCHAR)
                FROM Base b2
                WHERE b2.DmBannerREF = bc.DmBannerREF
                FOR XML PATH('')
            ), 1, 2, '') AS DanhSachPhanBo

        FROM BannerCheck bc
    )

    -- 🔥 FINAL: GOM NHÓM CÁC BANNER CÙNG LỖI
    SELECT
        bd.SoHopDong,
        bd.SoPhanBo,
        bd.DanhSachHopDong,
        bd.DanhSachPhanBo,

        -- 🔹 Gom danh sách banner
        STUFF((
            SELECT '; ' + CAST(b2.DmBannerREF AS VARCHAR)
            FROM BannerDetail b2
            WHERE 
                b2.DanhSachHopDong = bd.DanhSachHopDong
                AND b2.DanhSachPhanBo = bd.DanhSachPhanBo
            FOR XML PATH('')
        ), 1, 2, '') AS DanhSachBanner,

        -- 🔥 Message gửi team
        N'Dear Team, các banner [' + 
        STUFF((
            SELECT '; ' + CAST(b3.DmBannerREF AS VARCHAR)
            FROM BannerDetail b3
            WHERE 
                b3.DanhSachHopDong = bd.DanhSachHopDong
                AND b3.DanhSachPhanBo = bd.DanhSachPhanBo
            FOR XML PATH('')
        ), 1, 2, '') 
        + N'] đang gắn với ' + CAST(bd.SoPhanBo AS NVARCHAR) 
        + N' phân bổ thuộc ' + CAST(bd.SoHopDong AS NVARCHAR) 
        + N' hợp đồng khác nhau'
        + N' | HĐ: ' + bd.DanhSachHopDong
        + N' | PB: ' + bd.DanhSachPhanBo
        AS GhiChu

    FROM BannerDetail bd

    GROUP BY 
        bd.SoHopDong,
        bd.SoPhanBo,
        bd.DanhSachHopDong,
        bd.DanhSachPhanBo

    ORDER BY bd.DanhSachHopDong

END
```
