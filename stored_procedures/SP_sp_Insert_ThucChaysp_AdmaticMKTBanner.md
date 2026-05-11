# Stored Procedure: `sp_Insert_ThucChaysp_AdmaticMKTBanner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-04-17 09:17:05.017000
- **Ngày sửa cuối**: 2026-04-17 09:17:05.017000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmBannerID` | `nvarchar` | No |

## Definition (Source Code)

```sql
Create PROCEDURE [dbo].[sp_Insert_ThucChaysp_AdmaticMKTBanner]
( 
    @DmBannerID NVARCHAR(MAX) -- ví dụ: '111,222,333'
)
AS
BEGIN
    SET NOCOUNT ON;

    -- Xóa dữ liệu cũ
    DELETE FROM ThucChay_ThanhTien_Admatic
    WHERE DmSanPhamREF = 817
      AND DmBannerID IN (
            SELECT TRY_CAST(value AS INT)
            FROM STRING_SPLIT(@DmBannerID, ',')
      );

    -- Insert lại dữ liệu
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
        VAT,
        HopDongChiTietREF
    )
    SELECT 
        contract_number,
        CONVERT(INT, DmSanPhamREF),
        CONVERT(INT, DmSanPhamREF),
        TenSanPham,
        NhanHang,
        CONVERT(INT, ISNULL(NhanHangID,0)),
        CONVERT(INT, ISNULL(banner_id,0)),
        ISNULL(dbo.GetWebsiteIDByDomainName(domain_name),0),
        domain_name,
        CONVERT(INT, ISNULL(DmViTriREF,0)),
        TenViTri,

        -- Số lượng thực chạy
        CASE 
            WHEN ProductUnitName = N'CPM' AND domain_tt_money <> 0
                THEN CONVERT(BIGINT,ISNULL(domain_tt_view,0))
            WHEN ProductUnitName = N'CPC' AND domain_tt_money <> 0
                THEN CONVERT(BIGINT,ISNULL(domain_tt_click,0))
            WHEN ProductUnitName IN (N'TRUEVIEW', N'TRUE VIEW') AND domain_tt_money <> 0
                THEN CONVERT(BIGINT,ISNULL(domain_tt_view,0))
            ELSE 0
        END,

        -- Số lượng KM
        CASE 
            WHEN ProductUnitName = N'CPM' AND domain_tt_money = 0 AND domain_tt_promotion <> 0
                THEN CONVERT(BIGINT,ISNULL(domain_tt_view,0))
            WHEN ProductUnitName = N'CPC' AND domain_tt_money = 0 AND domain_tt_promotion <> 0
                THEN CONVERT(BIGINT,ISNULL(domain_tt_click,0))
            WHEN ProductUnitName IN (N'TRUEVIEW', N'TRUE VIEW') AND domain_tt_money = 0 AND domain_tt_promotion <> 0
                THEN CONVERT(BIGINT,ISNULL(domain_tt_view,0))
            ELSE 0
        END,

        -- Đơn vị tính
        CASE 
            WHEN ProductUnitName = N'CPM' THEN N'VIEW'
            WHEN ProductUnitName = N'CPC' THEN N'CLICK'
            WHEN ProductUnitName IN (N'TRUEVIEW', N'TRUE VIEW') THEN N'TRUE VIEW'
            ELSE N''
        END,

        -- Tiền
        ISNULL(domain_tt_money,0) / (1 + ISNULL(vat,0) / 100.0),
        ISNULL(domain_tt_promotion,0) / (1 + ISNULL(vat,0) / 100.0),

        NgayThucHien,
        GETDATE(),
        createdBy,
        GETDATE(),
        createdBy,
        0,
        vat,
        mktFeeAllocationId

    FROM dbo.DataThucChay_Admatic_v2_test
    WHERE banner_id IN (
            SELECT TRY_CAST(value AS INT)
            FROM STRING_SPLIT(@DmBannerID, ',')
      )
      AND DmSanPhamREF = 817;

END
```
