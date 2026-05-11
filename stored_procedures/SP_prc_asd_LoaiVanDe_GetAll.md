# Stored Procedure: `prc_asd_LoaiVanDe_GetAll`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-04-14 11:58:24.980000
- **Ngày sửa cuối**: 2017-09-28 14:52:07.990000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

CREATE PROC [dbo].[prc_asd_LoaiVanDe_GetAll]
AS

BEGIN
	SELECT ID, TenLoiChiTiet Name, NhomSanPham, IDNhomSanPham FROM dbo.KiemSoatThucChay_DanhSachLoi
	ORDER BY IDNhomSanPham, TenLoiChiTiet
	
END
```
