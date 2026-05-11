# Stored Procedure: `BaoCao6ChiSo_TheoSanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-12-03 08:19:13.647000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.517000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE proc [dbo].[BaoCao6ChiSo_TheoSanPham]
as
SELECT
tctd.TenSanPham AS N'Tên sản phẩm'
,dbo.formatnumber(sum( ((tctd.thanhtien/NULLIF( hdth.GiaTriHopDong,0))*hdth.TongTienKyHopDong))/1000000) as 'DS Ký'
,dbo.formatnumber(sum( ((tctd.thanhtien/NULLIF( hdth.GiaTriHopDong,0))*hdth.TongTienHaiDauHopDong))/1000000) as 'DS Hai dấu'
,dbo.formatnumber(sum( ((tctd.thanhtien/NULLIF( hdth.GiaTriHopDong,0))*hdth.TongTienThucChay))/1000000)  as 'DS Thực chạy'
,dbo.formatnumber(sum( ((tctd.thanhtien/NULLIF( hdth.GiaTriHopDong,0))*hdth.TongTienXuatHoaDon))/1000000)  as 'DS Hóa đơn'
,dbo.formatnumber(sum( ((tctd.thanhtien/NULLIF( hdth.GiaTriHopDong,0))*hdth.TongTienDaThanhToan))/1000000) as 'DS Tiền về'
,dbo.formatnumber(sum( ((tctd.thanhtien/NULLIF( hdth.GiaTriHopDong,0))*hdth.CongNo))/1000000)  as 'DS Công nợ'
from dbo. HopDongTongHop hdth
JOIN ThucChayTheoDoiHopDongChiTiet AS tctd
ON hdth.HopDongID= tctd.HopDongFK

where
year(hdth.NgayKyHopDong ) = 2013
and month (hdth.NgayKyHopDong) BETWEEN 1 AND 12 
AND  
tctd.TenSanPham in('Balloon Ads'
,'Banner',
'Box App CPD',
'Box App CPM',
'Box App self-serving',
'CPC',
'CPM 7000',
'CPM Admarket',
'CPM Mass',
'PR',
'Tin vip',
'TVC Online')

GROUP BY tctd.TenSanPham
ORDER BY tctd.tensanpham

```
