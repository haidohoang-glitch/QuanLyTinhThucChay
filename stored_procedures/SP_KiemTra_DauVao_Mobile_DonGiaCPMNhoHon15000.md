# Stored Procedure: `KiemTra_DauVao_Mobile_DonGiaCPMNhoHon15000`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-21 11:06:34.643000
- **Ngày sửa cuối**: 2016-11-21 11:06:34.643000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROC [dbo].[KiemTra_DauVao_Mobile_DonGiaCPMNhoHon15000]

AS
BEGIN

--Check đơn giá CPM, có nhỏ hơn 15000/cpm không
SELECT hd.SoHopDong, hdct.HopDongChiTietID,hdct.TenLoai AS HTQC
	,hdct.TenSanPham,hdct.DonViTinh,hdct.DonGia  
 FROM dbo.HopDong hd FULL OUTER JOIN 
	dbo.HopDongChiTiet hdct ON hd.HopDongID=hdct.HopDongFK 
 WHERE hdct.DonViTinh='CPM' AND hdct.DonGia<15000
	AND hdct.DmSanPhamREF=342
	AND hdct.DeletedStatus = 0
	AND hd.TrangThaiHopDong <> 3
	AND hd.NgayDanhSoHopDong >= '2015-01-01'

END
```
