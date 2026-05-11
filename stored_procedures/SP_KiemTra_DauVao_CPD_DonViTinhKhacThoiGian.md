# Stored Procedure: `KiemTra_DauVao_CPD_DonViTinhKhacThoiGian`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-21 11:08:12.540000
- **Ngày sửa cuối**: 2016-11-24 18:17:35.270000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROC  [dbo].[KiemTra_DauVao_CPD_DonViTinhKhacThoiGian]

AS
BEGIN
--Check đơn vị tính CPD phải là  đơn vị thời gian
SELECT hd.SoHopDong,hd.HopDongID, hdct.HopDongChiTietID,
		hdct.TenLoai AS HTQC, hdct.DmLoaiBannerREF,hdct.TenSanPham,
		hdct.DonViTinh,hdct.DonGia, hdct.ThanhTien, hdct.ThanhtienThucChay,(hdct.ThanhTien- hdct.ThanhtienThucChay)lech 
 FROM dbo.HopDong hd INNER JOIN 
		dbo.HopDongChiTiet hdct ON hd.HopDongID=hdct.HopDongFK 
 WHERE 1=1
		AND  hdct.DonViTinh NOT IN(N'Ngày' ,N'Tuần' ,N'Tháng' ,N'Năm' )
		AND hdct.DmSanPhamREF IN(549,228,140,385)
		AND NOT hdct.DmLoaiBannerREF=17
		AND hdct.DeletedStatus = 0
		AND hd.TrangThaiHopDong <> 3
		AND hd.NgayDanhSoHopDong >= '2015-01-01'

END

```
