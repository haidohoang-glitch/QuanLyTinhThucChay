# Stored Procedure: `KiemTra_DauVao_CPM_HTQCLaCPM_DVTLaCPC`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-21 17:11:01.457000
- **Ngày sửa cuối**: 2016-11-22 15:29:44.413000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

CREATE PROC [dbo].[KiemTra_DauVao_CPM_HTQCLaCPM_DVTLaCPC]

AS
BEGIN
-- Đơn vị là CPC thì HTQC phải khác CPM

 SELECT hd.TenKhachHang, hd.HopDongID,hd.SoHopDong, hdct.HopDongChiTietID,hdct.TenLoai AS HTQC, hdct.TenBanner,
 hdct.DmSanPhamREF,
hdct.TenSanPham, hdct.DonViTinh, hdct.DonGia, hdct.ThanhTien, hdct.ThanhTienThucChay,ROUND(hdct.ThanhTien- hdct.ThanhTienThucChay,0)lechhdtc, hdct.GhiChu,hdct.CreatedBy NguoiTao, hdct.LastModifiedBy NguoiSuaCuoi
	FROM dbo.HopDong hd FULL OUTER JOIN 
		dbo.HopDongChiTiet hdct ON hd.HopDongID=hdct.HopDongFK
	WHERE (DonViTinh<>N'CPM' AND TenLoai=N'CPM' AND NOT(hdct.DmLoaiBannerREF = 17 OR hdct.DmLoaiNenTangREF = 8))
	AND hdct.DeletedStatus = 0
	AND hd.TrangThaiHopDong <> 3
	AND hdct.DmSanPhamREF <> 688 --Back fill
	AND hd.SoHopDong NOT IN ('QC3350315','QC2860116')
	AND hd.NgayDanhSoHopDong >= '2015-01-01'
ORDER BY ROUND(hdct.ThanhTien- hdct.ThanhTienThucChay,0)
END

```
