# Stored Procedure: `KiemTra_DauVao_Mobile_DonGiaCPCLonHon10000`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-21 11:05:47.647000
- **Ngày sửa cuối**: 2016-11-21 11:05:47.647000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROC [dbo].[KiemTra_DauVao_Mobile_DonGiaCPCLonHon10000]
-- author Haunt
-- 2016-11-18
AS
BEGIN
-- Check đơn giá CPC, có lớn hơn 10k/cpc không
SELECT hd.SoHopDong, hdct.HopDongChiTietID,hdct.TenLoai AS HTQC,hdct.TenSanPham,
 hdct.DonViTinh,hdct.DonGia  FROM dbo.HopDong hd FULL OUTER JOIN 
 dbo.HopDongChiTiet hdct ON hd.HopDongID=hdct.HopDongFK WHERE hdct.DonViTinh='CPC' AND hdct.DonGia>10000
 AND hdct.DmSanPhamREF=342
   AND hdct.DeletedStatus = 0
 AND hd.TrangThaiHopDong <> 3
AND hd.NgayDanhSoHopDong >= '2015-01-01'
END

```
