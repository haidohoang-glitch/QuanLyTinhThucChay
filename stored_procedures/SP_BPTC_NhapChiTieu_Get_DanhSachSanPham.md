# Stored Procedure: `BPTC_NhapChiTieu_Get_DanhSachSanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:51.407000
- **Ngày sửa cuối**: 2015-06-11 18:17:51.407000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

CREATE PROC [dbo].[BPTC_NhapChiTieu_Get_DanhSachSanPham]
AS 
    BEGIN
        SELECT  DmSanPhamREF AS Id,
                TenSanPham AS Name
        FROM    dbo.DmNhomSanPhamBaoCao
        ORDER BY TenSanPham
    END

```
