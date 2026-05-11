# Stored Procedure: `sp_Insert_ThucChay_Admatic_TheoHD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-04-17 09:25:20.973000
- **Ngày sửa cuối**: 2026-04-17 09:30:46.023000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamREF` | `int(4)` | No |
| `@SoHopDong` | `nvarchar` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE [dbo].[sp_Insert_ThucChay_Admatic_TheoHD]
( 
    @DmSanPhamREF INT,
    @SoHopDong NVARCHAR(MAX)   -- 'QC0180425,QC0180426'
)
AS
BEGIN
    SET NOCOUNT ON;

    -- Xóa dữ liệu cũ
    DELETE FROM ThucChay_ThanhTien_Admatic
    WHERE DmSanPhamREF = @DmSanPhamREF
      AND SoHopDong IN (
            SELECT LTRIM(RTRIM(value))
            FROM STRING_SPLIT(@SoHopDong, ',')
      );

    -- Insert lại
    INSERT INTO dbo.ThucChay_ThanhTien_Admatic
    (
        SoHopDong,
        TypeProduct,
        DmSanPhamREF,
        TenSanPham,
        TenNhanHang,
        DmNhanHangREF,
        DmBannerID,
        DmWebsiteID,
        TenWebsite,
        DmViTriBannerSanPhamID,
        TenViTriBannerSanPham,
        SoLuongThucChay,
        SoLuongThucChayKM,
        DonViTinh,
        ThanhTienThucChaySauCK_ChuaVAT,
        ThanhTienThucChayKM,
        NgayThucHien,
        CreatedAt,
        CreatedBy,
        LastModifiedAt,
        LastModifiedBy,
        DeletedStatus,
        VAT
    )
    SELECT 
        d.contract_number,

        TRY_CAST(d.DmSanPhamREF AS INT),
        TRY_CAST(d.DmSanPhamREF AS INT),

        d.TenSanPham,
        d.NhanHang,

        TRY_CAST(ISNULL(d.NhanHangID,0) AS INT),
        TRY_CAST(ISNULL(d.banner_id,0) AS INT),

        ISNULL(dbo.GetWebsiteIDByDomainName(d.domain_name),0),
        d.domain_name,

        TRY_CAST(ISNULL(d.DmViTriREF,0) AS INT),
        d.TenViTri,

        -- Thực chạy
        CASE 
            WHEN d.ProductUnitName = N'CPM' AND x.money <> 0
                THEN TRY_CAST(ISNULL(d.domain_tt_view,0) AS BIGINT)

            WHEN d.ProductUnitName = N'CPC' AND x.money <> 0
                THEN TRY_CAST(ISNULL(d.domain_tt_click,0) AS BIGINT)

            WHEN d.ProductUnitName IN (N'TRUEVIEW', N'TRUE VIEW') AND x.money <> 0
                THEN TRY_CAST(ISNULL(d.domain_tt_view,0) AS BIGINT)

            ELSE 0
        END,

        -- Khuyến mãi
        CASE 
            WHEN d.ProductUnitName = N'CPM' AND x.money = 0 AND x.promo <> 0
                THEN TRY_CAST(ISNULL(d.domain_tt_view,0) AS BIGINT)

            WHEN d.ProductUnitName = N'CPC' AND x.money = 0 AND x.promo <> 0
                THEN TRY_CAST(ISNULL(d.domain_tt_click,0) AS BIGINT)

            WHEN d.ProductUnitName IN (N'TRUEVIEW', N'TRUE VIEW') AND x.money = 0 AND x.promo <> 0
                THEN TRY_CAST(ISNULL(d.domain_tt_view,0) AS BIGINT)

            ELSE 0
        END,

        -- Đơn vị
        CASE 
            WHEN d.ProductUnitName = N'CPM' THEN N'VIEW'
            WHEN d.ProductUnitName = N'CPC' THEN N'CLICK'
            WHEN d.ProductUnitName IN (N'TRUEVIEW', N'TRUE VIEW') THEN N'TRUE VIEW'
            ELSE N''
        END,

        -- Tiền (chuẩn, không lỗi)
        ISNULL(x.money,0) / NULLIF(1 + ISNULL(x.vat_val,0)/100.0,0),

        ISNULL(x.promo,0) / NULLIF(1 + ISNULL(x.vat_val,0)/100.0,0),

        d.NgayThucHien,
        GETDATE(),
        d.createdBy,
        GETDATE(),
        d.createdBy,
        0,
        x.vat_val

    FROM dbo.DataThucChay_Admatic_v2_test d

    CROSS APPLY (
        SELECT 
            TRY_CAST(d.domain_tt_money AS FLOAT) AS money,
            TRY_CAST(d.domain_tt_promotion AS FLOAT) AS promo,
            TRY_CAST(d.vat AS FLOAT) AS vat_val
    ) x

    WHERE TRY_CAST(d.DmSanPhamREF AS INT) = @DmSanPhamREF
      AND d.contract_number IN (
            SELECT LTRIM(RTRIM(value))
            FROM STRING_SPLIT(@SoHopDong, ',')
      );

END
```
