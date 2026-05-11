# Stored Procedure: `Rpt_NhanHang_ThongTinChung`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-22 17:42:36.553000
- **Ngày sửa cuối**: 2014-11-19 12:16:43.247000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@LabelId` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE  PROC [dbo].[Rpt_NhanHang_ThongTinChung]
(
	@StartDate	DATETIME,
	@EndDate	DATETIME,
	@LabelId	INT		
)
AS
BEGIN		
	SELECT N'Thông xoang tán' AS TenNhanHang,	
		   N'Ðang ch?y' AS TinhTrang,
		   N'Công ty TNHH Nam Du?c' AS CongTyChuSoHuu,
		   '0600338312' AS MaSoThue,
		   N'Lô M13, Khu dô th? Hòa xá, TP Nam Ð?nh, T?nh Nam Ð?nh' AS DiaChi,
		   '3503 671 932' AS SoDienThoai,
		   '942.200.000' AS TongDSKy2Dau,
		   10 AS SoLuongHopDong,
		   '100%' AS TyLeDSThucChay_DSKy2Dau, 
		   '5/200' AS NhanCuaNganh,
		   '305/3000' AS NhanDaKi,
		   '> 15%' AS SoVoiDoanhSoTB1NhanCuaNganh,
		   8 AS HopDongKinhTe,
		   2 AS HopDongHopTac
END

```
