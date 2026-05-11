# Stored Procedure: `sp_BaoCaoSPvuotHD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-02-27 17:37:26.037000
- **Ngày sửa cuối**: 2026-03-03 16:54:31.690000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

CREATE PROCEDURE [dbo].[sp_BaoCaoSPvuotHD]
AS
BEGIN
    SET NOCOUNT ON;
	TRUNCATE TABLE BaoCaoSPvuotHD;  -- làm sạch trước

    EXEC dbo.BaoCaoSPvuotHD_GGFB;
    EXEC dbo.BaoCaoSPvuotHD_Branding;
    EXEC dbo.BaoCaoSPvuotHD_Admatic;
	EXEC dbo.BaoCaoSPvuotHD_PR;

END

```
