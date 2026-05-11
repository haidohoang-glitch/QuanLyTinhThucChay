# Stored Procedure: `nhung_PerformanceBase_DieuChinh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 16:02:04.323000
- **Ngày sửa cuối**: 2026-04-02 10:29:56.243000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[nhung_PerformanceBase_DieuChinh]
    @HopDongChiTietID INT
AS
BEGIN
    SET NOCOUNT ON;

    ;WITH DATA AS (
        SELECT 
            ID,
            SoHopDong,
            HopDongChiTietREF,
            DmSanPhamREF,
            TK_Admarket,
            TenViTri,
            SoTienThayDoi,
            TienThucChayKPI,
            RecordStatus,
            NgayGhiNhanThayDoi,
            CreatedAt,
            CreatedBy,
            LastModifiedAt,
            LoaiGhiNhan,
            LyDoTuChoi
        FROM dbo.ThucChay_PerformanceBase_ThayDoi
        WHERE HopDongChiTietREF = @HopDongChiTietID
        AND DeletedStatus = 0
    ),
    FINAL AS (

        -- Chi tiết
        SELECT
            0 AS SortKey,
            ID,
            SoHopDong,
            HopDongChiTietREF,
            DmSanPhamREF,
            TK_Admarket,
            TenViTri,
            SoTienThayDoi,
            TienThucChayKPI,
            RecordStatus,
            CASE 
				WHEN RecordStatus = 0 THEN N'Chưa ghi nhận' 
				WHEN RecordStatus = 1 THEN N'Đã ghi nhận TC'  
				WHEN RecordStatus = 2 THEN N'Từ chối TC' 
				WHEN RecordStatus = 3 THEN N'Đã ghi nhận KPI' 
				WHEN RecordStatus = 4 THEN N'Từ chối KPI' 
				WHEN RecordStatus = 5 THEN N'TC OK, KPI lỗi' 
				WHEN RecordStatus = 6 THEN N'TC lỗi, KPI OK' 
				WHEN RecordStatus = 7 THEN N'TC lỗi, KPI lỗi' 
				WHEN RecordStatus = 8 THEN N'TC OK, KPI OK' 
			END AS trangthai_tinh,
            NgayGhiNhanThayDoi,
            CreatedAt,
            CreatedBy,
            LastModifiedAt,
            CASE 
                WHEN LoaiGhiNhan = 1 THEN N'Thặng dư' 
                WHEN LoaiGhiNhan = 0 THEN N'Thực chạy'
                WHEN LoaiGhiNhan = 2 THEN N'MKT Free'
                ELSE CAST(LoaiGhiNhan AS NVARCHAR(50))
            END AS Loai,
            LyDoTuChoi
        FROM DATA

        UNION ALL

        -- Dòng tổng
        SELECT
            1 AS SortKey,
            NULL,
            NULL,
            NULL,
            NULL,
            NULL,
            N'TỔNG',
            SUM(SoTienThayDoi),
            SUM(TienThucChayKPI),
            NULL,
            NULL,
            NULL,
            NULL,
            NULL,
            NULL,
            NULL,
            NULL
        FROM DATA
    )

    SELECT
        ID,
        SoHopDong,
        HopDongChiTietREF,
        DmSanPhamREF,
        TK_Admarket,
        TenViTri,
        dbo.FormatNumber(SoTienThayDoi) AS SoTienThayDoi,
        dbo.FormatNumber(TienThucChayKPI) AS TienThucChayKPI,
        RecordStatus,
        trangthai_tinh,
        NgayGhiNhanThayDoi,
        CreatedAt,
        CreatedBy,
        LastModifiedAt,
        Loai,
        LyDoTuChoi
    FROM FINAL
    ORDER BY SortKey, ID DESC

END

```
