# Stored Procedure: `sp_Insert_ThucChaysp_AdmaticMKT`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-04-01 09:17:57.760000
- **Ngày sửa cuối**: 2026-04-01 09:35:38.493000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.sp_Insert_ThucChaysp_AdmaticMKT
( 
    @SoHopDong NVARCHAR(50)
)
AS
BEGIN
    SET NOCOUNT ON;

    -- Xóa dữ liệu cũ
    DELETE FROM ThucChay_ThanhTien_Admatic
    WHERE DmSanPhamREF = 817
      AND SoHopDong = @SoHopDong;

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
        contract_number AS SoHopDong,
        CONVERT(INT, DmSanPhamREF) AS TypeProduct,
        CONVERT(INT, DmSanPhamREF) AS DmSanPhamREF,
        TenSanPham,
        NhanHang,
        CONVERT(INT, ISNULL(NhanHangID,0)) AS DmNhanHangREF,
        CONVERT(INT, ISNULL(banner_id,0)) AS DmBannerID,
        ISNULL(dbo.GetWebsiteIDByDomainName(domain_name),0) AS DmWebsiteID,
        domain_name AS TenWebsite,
        CONVERT(INT, ISNULL(DmViTriREF,0)) AS DmViTriBannerSanPhamID,
        TenViTri,

        -- Số lượng thực chạy
        CASE 
            WHEN ProductUnitName = N'CPM' AND (CONVERT(FLOAT,domain_tt_money) <> 0)
                THEN CONVERT(BIGINT,ISNULL(domain_tt_view,0))
            WHEN ProductUnitName = N'CPC' AND (CONVERT(FLOAT,domain_tt_money) <> 0)
                THEN CONVERT(BIGINT,ISNULL(domain_tt_click,0))
            WHEN ProductUnitName IN (N'TRUEVIEW', N'TRUE VIEW') AND (CONVERT(FLOAT,domain_tt_money) <> 0)
                THEN CONVERT(BIGINT,ISNULL(domain_tt_view,0))
            ELSE 0
        END AS SoLuongThucChay,

        -- Số lượng KM
        CASE 
            WHEN ProductUnitName = N'CPM' AND (CONVERT(FLOAT,domain_tt_money) = 0 AND CONVERT(FLOAT,domain_tt_promotion) <> 0)
                THEN CONVERT(BIGINT,ISNULL(domain_tt_view,0))
            WHEN ProductUnitName = N'CPC' AND (CONVERT(FLOAT,domain_tt_money) = 0 AND CONVERT(FLOAT,domain_tt_promotion) <> 0)
                THEN CONVERT(BIGINT,ISNULL(domain_tt_click,0))
            WHEN ProductUnitName IN (N'TRUEVIEW', N'TRUE VIEW') AND (CONVERT(FLOAT,domain_tt_money) = 0 AND CONVERT(FLOAT,domain_tt_promotion) <> 0)
                THEN CONVERT(BIGINT,ISNULL(domain_tt_view,0))
            ELSE 0
        END AS SoLuongThucChayKM,

        -- Đơn vị tính
        CASE 
            WHEN ProductUnitName = N'CPM' THEN N'VIEW'
            WHEN ProductUnitName = N'CPC' THEN N'CLICK'
            WHEN ProductUnitName IN (N'TRUEVIEW', N'TRUE VIEW') THEN N'TRUE VIEW'
            ELSE N''
        END AS DonViTinh,
        CONVERT(FLOAT, ISNULL(domain_tt_money,0)) / (1 + ISNULL(vat,0) / 100.0) AS ThanhTienThucChaySauCK_ChuaVAT,
		CONVERT(FLOAT, ISNULL(domain_tt_promotion,0)) / (1 + ISNULL(vat,0) / 100.0) AS ThanhTienThucChayKM,
        NgayThucHien,
        GETDATE() AS CreatedAt,
        createdBy,
        GETDATE() AS LastModifiedAt,
        createdBy AS LastModifiedBy,
        0 AS DeletedStatus,
        vat,
        mktFeeAllocationId AS HopDongChiTietREF

    FROM dbo.DataThucChay_Admatic_v2_test
    WHERE contract_number = @SoHopDong
      AND DmSanPhamREF = 817;

END

```
