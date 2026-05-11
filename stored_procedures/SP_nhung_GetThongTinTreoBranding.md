# Stored Procedure: `nhung_GetThongTinTreoBranding`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 11:44:37.813000
- **Ngày sửa cuối**: 2026-03-17 09:12:02.377000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_GetThongTinTreoBranding
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;

    SELECT  
        HopDongREF,
        HopDongChiTietREF,
        DmNhanHangREF,	
        NhanHang,	
        TenHinhThucQuangCao,
        DmSanPhamREF,
        DmBannerREF,	
        SoLuongThucTreo,

        CASE 
            WHEN dmdonvitinhref = 1 THEN N'CPM'
            WHEN dmdonvitinhref = 2 THEN N'CPC'
            ELSE CAST(dmdonvitinhref AS NVARCHAR(50)) 
        END AS DonGiaTheoDonVi,

        dbo.FormatNumber(DonGia) AS DonGia,
        ChietKhau,
        dbo.FormatNumber(ThanhTien) AS ThanhTien,
        Link,
        RecordStatus,
        DeletedStatus,
        CreatedAt,
		CreatedBy,
        LastModifiedAt,
		LastModifiedBy
FROM dbo.ThucChayHopDongChiTiet 
WHERE HopDongChiTietREF = @HopDongChiTietID
AND DeletedStatus = 0

UNION ALL

SELECT  
        NULL,
        NULL,
        NULL,
        N'TỔNG',
        NULL,
        NULL,
        NULL,
        SUM(SoLuongThucTreo),

        NULL,
        dbo.FormatNumber(SUM(DonGia)),
        NULL,
        dbo.FormatNumber(SUM(ThanhTien)),
        NULL,
        NULL,
        NULL,
        NULL,
		NULL,
        NULL,
		NULL
FROM dbo.ThucChayHopDongChiTiet 
WHERE HopDongChiTietREF = @HopDongChiTietID
AND DeletedStatus = 0;

END

```
