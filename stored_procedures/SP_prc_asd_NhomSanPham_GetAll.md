# Stored Procedure: `prc_asd_NhomSanPham_GetAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-09-11 11:15:46.740000
- **Ngày sửa cuối**: 2017-09-11 11:15:46.740000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
/****** Script for SelectTopNRows command from SSMS  ******/

CREATE PROC [dbo].[prc_asd_NhomSanPham_GetAll]
AS

BEGIN
SELECT DISTINCT
      [IDNhomSanPham] ID
      ,[NhomSanPham] Name
  FROM KiemSoatThucChay_DanhSachLoi;

END
  
```
