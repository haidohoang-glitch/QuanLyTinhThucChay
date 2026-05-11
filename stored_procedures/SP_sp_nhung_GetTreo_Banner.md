# Stored Procedure: `sp_nhung_GetTreo_Banner`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-24 15:04:38.573000
- **Ngày sửa cuối**: 2026-03-24 15:04:38.573000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmBannerREFList` | `nvarchar` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_nhung_GetTreo_Banner
    @DmBannerREFList NVARCHAR(MAX) = '111209,111208' -- truyền dạng: '111209,111208'
AS
BEGIN
    SET NOCOUNT ON;

    SELECT 
        dbo.GetSoHopDongByID(HopDongREF) AS Sohopdong,
        ThucChayHopDongChiTietID AS IDtreo,
        HopDongREF,
        HopDongChiTietREF,
        DmSanPhamREF,
        DmBannerREF,
        TenHinhThucQuangCao,
        --Link,
        RecordStatus,
        DeletedStatus,
        CreatedAt,
        CreatedBy,
        LastModifiedAt,
        LastModifiedBy
    FROM dbo.ThucChayHopDongChiTiet
    WHERE DmBannerREF IN (
        SELECT value 
        FROM STRING_SPLIT(@DmBannerREFList, ',')
    )
    ORDER BY HopDongChiTietREF;
END;

```
