# Stored Procedure: `API_InsertOrUpdate_PerformanceBase_bk1`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2021-06-16 16:34:21.003000
- **Ngày sửa cuối**: 2021-06-16 16:34:21.003000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PhanBoId` | `int(4)` | No |
| `@SanPhamId` | `int(4)` | No |
| `@ViTriId` | `int(4)` | No |
| `@TaiKhoan` | `nvarchar(1000)` | No |
| `@RequestKey` | `nvarchar(1000)` | No |
| `@TienThayDoi` | `float(8)` | No |
| `@NgayThayDoi` | `datetime(8)` | No |

## Definition (Source Code)

```sql

-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
create PROCEDURE [dbo].[API_InsertOrUpdate_PerformanceBase_bk1]
    -- Add the parameters for the stored procedure here
    @PhanBoId INT = NULL,
    @SanPhamId INT = NULL,
    @ViTriId INT = NULL,
    @TaiKhoan NVARCHAR(500),
    @RequestKey NVARCHAR(500),
    @TienThayDoi FLOAT,
    @NgayThayDoi DATETIME
AS
BEGIN
    IF EXISTS (SELECT 1 FROM dbo.ThucChay_PerformanceBase_ThayDoi WHERE UPPER(Request_key) = UPPER(@RequestKey)
              AND ISNULL(DeletedStatus, 0) = 0 )
    BEGIN
        UPDATE dbo.ThucChay_PerformanceBase_ThayDoi
        SET TK_Admarket = @TaiKhoan,
            SoTienThayDoi = @TienThayDoi,
            NgayGhiNhanThayDoi = @NgayThayDoi,
            LastModifiedAt = GETDATE(),
            LastModifiedBy = 'API_SanPham',
            HopDongChiTietREF = @PhanBoId,
            DmSanPhamREF = @SanPhamId,
            DmViTriREF = @ViTriId
        WHERE UPPER(Request_key) = UPPER(@RequestKey)
              AND ISNULL(DeletedStatus, 0) = 0;
			-- AND RecordStatus = 0 AND CONVERT(DATE,CreatedAt) = convert(DATE,GetDate())
    END;
    ELSE
    BEGIN
        INSERT INTO dbo.ThucChay_PerformanceBase_ThayDoi
        (
            Request_key,
            SoHopDong,
            HopDongID,
            HopDongChiTietREF,
            DmSanPhamREF,
            TenSanPham,
            TK_Admarket,
            ThanhTien,
            DmViTriREF,
            TenViTri,
            TienThucChayTong,
            TienThucChay,
            ThucChayDenNgay,
            SoTienThayDoi,
            NgayGhiNhanThayDoi,
            CreatedAt,
            CreatedBy,
            LastModifiedAt,
            LastModifiedBy,
            RecordStatus,
            LyDoTuChoi,
            DeletedStatus
        )
        VALUES
        (   @RequestKey,    -- Request_key - nvarchar(50)
            N'',            -- SoHopDong - nvarchar(50)
            (
				SELECT HopDongFK
				FROM dbo.HopDongChiTiet
				WHERE HopDongChiTietID = @PhanBoId
			),              -- HopDongID - int
            @PhanBoId,      -- HopDongChiTietREF - int
            @SanPhamId,     -- DmSanPhamREF - int
            N'',            -- TenSanPham - nvarchar(50)
            @TaiKhoan,      -- TK_Admarket - nvarchar(50)
            0.0,            -- ThanhTien - float
            @ViTriId,       -- DmViTriREF - int
            CASE
                WHEN @ViTriId = 1 THEN
                    'AdX'
                WHEN @ViTriId = 2 THEN
                    'AdX Mobile'
                WHEN @ViTriId = 3 THEN
                    'AdX Ecommerce'
                WHEN @ViTriId = 0 THEN
                    ''
                ELSE
                    ''
            END,            -- TenViTri - nvarchar(50)
            NULL,            -- TienThucChayTong - float
            NULL,            -- TienThucChay - float
            NULL,           -- ThucChayDenNgay - datetime
            @TienThayDoi,   -- SoTienThayDoi - float
            @NgayThayDoi,   -- NgayGhiNhanThayDoi - datetime
            GETDATE(),      -- CreatedAt - datetime
            N'API_SanPham', -- CreatedBy - nvarchar(50)
            GETDATE(),      -- LastModifiedAt - datetime
            N'API_SanPham', -- LastModifiedBy - nvarchar(50)
            0,              -- RecordStatus - int
            N'',            -- LyDoTuChoi - nvarchar(200)
            0               -- DeletedStatus - bit
            );
    END;

    SELECT 1 AS Id;
END;







```
