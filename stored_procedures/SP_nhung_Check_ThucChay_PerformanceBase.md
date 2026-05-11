# Stored Procedure: `nhung_Check_ThucChay_PerformanceBase`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-05 16:52:26.630000
- **Ngày sửa cuối**: 2026-03-05 16:59:55.593000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongChiTietID` | `int(4)` | No |

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[nhung_Check_ThucChay_PerformanceBase]
(
    @HopDongChiTietID INT
)
AS
BEGIN
    SET NOCOUNT ON;

    -- Danh sách HĐ nội bộ
    WITH LoaiHopDongNoiBo AS (
        SELECT MaLoaiHopDong
        FROM dbo.DmLoaiHopDongNoiBo
        WHERE DeletedStatus = 0
    ),

    -- TCDT
    TCDT AS (
        SELECT DotChayBooking,
               SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS Tien_TCDT
        FROM dbo.ThucChayDaTinh
        WHERE HopDongChiTietREF = @HopDongChiTietID
        GROUP BY DotChayBooking
    ),

    -- TCDT Admarket
    TCDT_Admarket AS (
        SELECT DotChayBooking,
               SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi) AS Tien_Admarket
        FROM dbo.ThucChayDaTinhAdmarket
        WHERE HopDongChiTietREF = @HopDongChiTietID
        GROUP BY DotChayBooking
    ),

    -- TCDT Mua Ngoài
    TCDT_MuaNgoai AS (
        SELECT ThucChayMuaNgoaiChiTietREF,
               SUM(ThanhTienLaiThucChaySauCK) AS Tien_MuaNgoai
        FROM dbo.ThucChayDaTinh_MuaNgoai
        WHERE HopDongChiTietREF = @HopDongChiTietID
        GROUP BY ThucChayMuaNgoaiChiTietREF
    ),

    DATA AS (
        SELECT     
            td.ID,

            CASE 
                WHEN td.LoaiGhiNhan = 1 THEN N'Thặng Dư' 
                ELSE N'Thực chạy' 
            END AS LoaiGhiNhan_SP,

            td.SoTienThayDoi,
            td.TienThucChayKPI,
            t1.Tien_TCDT,
            t2.Tien_Admarket,
            t3.Tien_MuaNgoai,

            CASE 
                WHEN lhb.MaLoaiHopDong IS NOT NULL
                     AND t1.DotChayBooking IS NOT NULL 
                     AND t2.DotChayBooking IS NOT NULL 
                     THEN N'✅ Thực chạy (HĐ nội bộ)'

                WHEN lhb.MaLoaiHopDong IS NOT NULL
                     THEN N'⚠️ Sai ghi nhận HĐ nội bộ (thiếu bảng)'

                WHEN td.TienThucChayKPI > 0
                     AND t1.DotChayBooking IS NOT NULL 
                     AND t2.DotChayBooking IS NOT NULL 
                     THEN N'✅ KPI'

                WHEN td.TienThucChayKPI > 0
                     THEN N'⚠️ Sai ghi nhận KPI (thiếu bảng)'

                WHEN td.LoaiGhiNhan = 1
                     AND t1.DotChayBooking IS NOT NULL 
                     AND t2.DotChayBooking IS NOT NULL 
                     AND t3.ThucChayMuaNgoaiChiTietREF IS NOT NULL
                     THEN N'✅ Thặng dư ghi nhận đúng 3 bảng'

                WHEN td.LoaiGhiNhan = 1
                     THEN N'⚠️ Thiếu dữ liệu thực chạy (Loại ghi nhận = 1)'

                WHEN td.LoaiGhiNhan = 0
                     AND t1.DotChayBooking IS NULL 
                     AND t2.DotChayBooking IS NOT NULL 
                     AND t3.ThucChayMuaNgoaiChiTietREF IS NULL
                     THEN N'✅ Thực chạy'

                WHEN td.LoaiGhiNhan = 0
                     THEN N'⚠️ Sai nguồn ghi nhận (Loại ghi nhận = 0)'

                ELSE N'⚠️ Không xác định'
            END AS GhiChu

        FROM dbo.ThucChay_PerformanceBase_ThayDoi td
        JOIN dbo.HopDong hd 
            ON td.SoHopDong = hd.SoHopDong

        LEFT JOIN LoaiHopDongNoiBo lhb 
            ON hd.TenMaHopDong = lhb.MaLoaiHopDong

        LEFT JOIN TCDT t1 
            ON td.ID = TRY_CAST(t1.DotChayBooking AS INT)

        LEFT JOIN TCDT_Admarket t2 
            ON td.ID = TRY_CAST(t2.DotChayBooking AS INT)

        LEFT JOIN TCDT_MuaNgoai t3 
            ON td.ID = t3.ThucChayMuaNgoaiChiTietREF

        WHERE td.HopDongChiTietREF = @HopDongChiTietID
          AND td.DeletedStatus = 0 
          AND td.RecordStatus NOT IN (0,2)
    )

    -- Kết quả + dòng tổng
    SELECT 
        CAST(ID AS NVARCHAR) AS ID,
        LoaiGhiNhan_SP,
        dbo.FormatNumber(SoTienThayDoi) AS SoTienThayDoi,
        dbo.FormatNumber(TienThucChayKPI) AS TienThucChayKPI,
        dbo.FormatNumber(Tien_TCDT) AS Tien_TCDT,
        dbo.FormatNumber(Tien_Admarket) AS Tien_Admarket,
        dbo.FormatNumber(Tien_MuaNgoai) AS Tien_MuaNgoai,
        GhiChu
    FROM DATA

    UNION ALL

    SELECT 
        N'TỔNG',
        NULL,
        dbo.FormatNumber(SUM(SoTienThayDoi)),
        dbo.FormatNumber(SUM(TienThucChayKPI)),
        dbo.FormatNumber(SUM(Tien_TCDT)),
        dbo.FormatNumber(SUM(Tien_Admarket)),
        dbo.FormatNumber(SUM(Tien_MuaNgoai)),
        NULL
    FROM DATA

END
```
