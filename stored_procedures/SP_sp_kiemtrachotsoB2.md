# Stored Procedure: `sp_kiemtrachotsoB2`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-17 16:56:39.510000
- **Ngày sửa cuối**: 2026-03-17 17:14:53.593000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[sp_kiemtrachotsoB2]
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @NgayBatDau DATE,
            @nth2 DATE

    -- Lấy ngày đã chốt gần nhất từ DB release
    SELECT @NgayBatDau = MAX(NgayThucHien)
    FROM [ASDAG2].ABM_Data_Release.dbo.ThucChayDaTinh

    -- +2 ngày
    SET @nth2 = DATEADD(DAY, 2, @NgayBatDau)

    -----------------------------------------
    -- 1. ThucChayDaTinh
    -----------------------------------------
    SELECT 
        N'TCDT' AS Nguon,
        NgayThucHien,
        HopDongChiTietREF,
        TenSanPham,
        DmSanPhamREF,
        *
    FROM ThucChayDaTinh
    WHERE NgayThucHien <= @NgayBatDau
        AND CreatedAt >= @nth2

    -----------------------------------------
    -- 2. ThucChayDaTinhAdmarket
    -----------------------------------------
    SELECT 
        N'TCDT Admarket' AS Nguon,
        *
    FROM ThucChayDaTinhAdmarket
    WHERE NgayThucHien <= @NgayBatDau
        AND CreatedAt >= @nth2

    -----------------------------------------
    -- 3. ThucChayDaTinh_MuaNgoai
    -----------------------------------------
    SELECT 
        N'TCDT MuaNgoai' AS Nguon,
        *
    FROM dbo.ThucChayDaTinh_MuaNgoai
    WHERE NgayThucHien <= @NgayBatDau
        AND CreatedAt >= @nth2

END

```
