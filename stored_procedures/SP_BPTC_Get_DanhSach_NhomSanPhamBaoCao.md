# Stored Procedure: `BPTC_Get_DanhSach_NhomSanPhamBaoCao`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:50.923000
- **Ngày sửa cuối**: 2015-06-11 18:17:50.923000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

CREATE PROC [dbo].[BPTC_Get_DanhSach_NhomSanPhamBaoCao]
AS 
    BEGIN
        SELECT DISTINCT
                DmNhomSanPhamBaoCaoID AS Id,
                TenNhomSanPhamBaoCao AS Name
        FROM    dbo.DmNhomSanPhamBaoCao
    END

```
