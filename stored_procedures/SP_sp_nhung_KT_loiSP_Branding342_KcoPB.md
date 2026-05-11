# Stored Procedure: `sp_nhung_KT_loiSP_Branding342_KcoPB`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-27 14:15:42.420000
- **Ngày sửa cuối**: 2026-03-27 14:15:42.420000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayBatDau` | `date(3)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.sp_nhung_KT_loiSP_Branding342_KcoPB
(
    @NgayBatDau DATE
)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT 
        CONVERT(DATE, NgayThucHien) AS NgayThucHien,
        SoHopDong,
        DmBannerREF,
        HopDongChiTietREF,
        DmSanPhamREF,

        SUM(TongViewThucChay)  AS SLView,
        SUM(TongClickThucChay) AS SLClick

    FROM dbo.ThucChay 

    WHERE 
        DmSanPhamREF = 342 

        AND (
            HopDongChiTietREF IS NULL 
            OR HopDongChiTietREF = 0 
            OR HopDongChiTietREF = ''
        )

        AND CONVERT(DATE, NgayThucHien) >= @NgayBatDau

        AND SoHopDong <> 'TONGSANPHAM'

    GROUP BY 
        SoHopDong,
        DmBannerREF,
        HopDongChiTietREF,
        DmSanPhamREF,
        CONVERT(DATE, NgayThucHien)

    ORDER BY 
        NgayThucHien DESC;

END

```
