# Stored Procedure: `sp_Nhung_CauHinhNhomTinhDoanhSoThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-01-12 10:24:21.210000
- **Ngày sửa cuối**: 2026-01-12 10:24:21.210000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmSanPhamREF` | `int(4)` | No |
| `@TenSanPham` | `nvarchar(400)` | No |

## Definition (Source Code)

```sql
CREATE PROCEDURE dbo.sp_Nhung_CauHinhNhomTinhDoanhSoThucChay
(
    @DmSanPhamREF    INT,
    @TenSanPham      NVARCHAR(200)
)
AS
BEGIN
    SET NOCOUNT ON;

    INSERT INTO dbo.CauHinhNhomTinhDoanhSoThucChay
    (
        DmSanPhamREF,
        TenSanPham,
        NhomTinhDoanhSoThucChay,
        ThongtinJobChay,
        DeletedStatus,
        RecordStatus,
        CreatedAt,
        CreatedBy,
        LastModifiedAt,
        LastModifiedBy
    )
    SELECT
        @DmSanPhamREF,
        @TenSanPham,
        NhomTinhDoanhSoThucChay,
        ThongtinJobChay,
        DeletedStatus,
        RecordStatus,
        GETDATE()        AS CreatedAt,
        CreatedBy,
        GETDATE()        AS LastModifiedAt,
        LastModifiedBy
    FROM ABM_Data_ThucChay.dbo.CauHinhNhomTinhDoanhSoThucChay
    WHERE ID = 94;
END

```
