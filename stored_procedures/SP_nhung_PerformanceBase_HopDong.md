# Stored Procedure: `nhung_PerformanceBase_HopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 16:10:05.957000
- **Ngày sửa cuối**: 2026-03-05 16:10:05.957000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE dbo.nhung_PerformanceBase_HopDong
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;

    ;WITH DATA AS
    (
        SELECT 
            ThucChay_PerformanceBase_ThayDoi_ID AS ID,
            HopDongID,
            HopDongChitietID,
            DmSanPhamID,
            TK_Admarket,
            TenViTri,
            CAST(TienThucChay_GhiNhan AS FLOAT) AS TienThucChay_GhiNhan,
            TienThucChayKPI,
            RecordStatus,
            NgayGhiNhanThayDoi,
            CreatedAt,
            CreatedBy,
            LastModifiedAt,
            CASE 
                WHEN LoaiGhiNhan = 1 THEN N'Thặng dư' 
                WHEN LoaiGhiNhan = 0 THEN N'Thực chạy'
                WHEN LoaiGhiNhan = 2 THEN N'MKTFree'
                ELSE CAST(LoaiGhiNhan AS NVARCHAR(50))
            END AS Loai,
            LyDoLoi
        FROM dbo.ThucChay_PerformanceBase_ThayDoi_HopDong
        WHERE HopDongChitietID = @HopDongChiTietID
    )

    -- 🔹 Chi tiết
    SELECT 
        ID,
        HopDongID,
        HopDongChitietID,
        DmSanPhamID,
        TK_Admarket,
        TenViTri,
        dbo.FormatNumber(TienThucChay_GhiNhan) AS TienThucChay_GhiNhan,
        TienThucChayKPI,
        RecordStatus,
        NgayGhiNhanThayDoi,
        CreatedAt,
        CreatedBy,
        LastModifiedAt,
        Loai,
        LyDoLoi
    FROM DATA

    UNION ALL

    -- 🔹 Dòng tổng
    SELECT
        NULL,
        NULL,
        NULL,
        NULL,
        NULL,
        N'TỔNG',
        dbo.FormatNumber(SUM(TienThucChay_GhiNhan)),
        NULL,
        NULL,
        NULL,
        NULL,
        NULL,
        NULL,
        NULL,
        NULL
    FROM DATA

END

```
