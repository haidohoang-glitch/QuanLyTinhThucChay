# Stored Procedure: `sp_InsertBaoCaoSPvuotHD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-02 10:59:17.607000
- **Ngày sửa cuối**: 2026-03-02 11:05:10.410000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE dbo.sp_InsertBaoCaoSPvuotHD
AS
BEGIN
    SET NOCOUNT ON;

    -- Xoá dữ liệu cũ
    TRUNCATE TABLE dbo.BaoCaoSPvuotHD;

    -- Gọi 3 SP đổ dữ liệu
    EXEC BaoCaoSPvuotHD_GGFB
    EXEC BaoCaoSPvuotHD_Branding
    EXEC BaoCaoSPvuotHD_Admatic

    -- Đánh lại STT theo ngày + hợp đồng
    ;WITH x AS
    (
        SELECT *,
               ROW_NUMBER() OVER 
               (
                   ORDER BY NgayDanhSo, SoHopDong
               ) AS STT_Moi
        FROM dbo.BaoCaoSPvuotHD
    )
    UPDATE x
    SET STT = STT_Moi;

END

```
