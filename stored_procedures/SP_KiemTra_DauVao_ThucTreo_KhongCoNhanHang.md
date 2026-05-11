# Stored Procedure: `KiemTra_DauVao_ThucTreo_KhongCoNhanHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-21 11:09:05.527000
- **Ngày sửa cuối**: 2016-11-21 11:09:05.527000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

CREATE PROC [dbo].[KiemTra_DauVao_ThucTreo_KhongCoNhanHang]

AS
BEGIN
SELECT DISTINCT dbo.GetSoHopDongByID(HopDongREF) sohopdong, DmBannerREF, DmSanPhamREF, NhanHang, DmNhanHangREF, LastModifiedAt
FROM dbo.ThucChayHopDongChiTiet WHERE (DmNhanHangREF = '' OR DmNhanHangREF = 0)
AND DeletedStatus =0 

SELECT DISTINCT dbo.GetSoHopDongByID(HopDongREF) sohopdong, DmSanPhamREF, NhanHang, DmNhanHangREF, LastModifiedAt,HopDongREF, ThucChayHopDongChiTietPRID
FROM dbo.ThucChayHopDongChiTietPR WHERE (DmNhanHangREF = '' OR DmNhanHangREF = 0)
AND DeletedStatus =0 

END


```
