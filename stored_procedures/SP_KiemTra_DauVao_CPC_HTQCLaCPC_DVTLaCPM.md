# Stored Procedure: `KiemTra_DauVao_CPC_HTQCLaCPC_DVTLaCPM`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-21 11:04:10.503000
- **Ngày sửa cuối**: 2016-11-22 15:58:06.777000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

CREATE PROC [dbo].[KiemTra_DauVao_CPC_HTQCLaCPC_DVTLaCPM]

AS
BEGIN
  -- Đơn vị là CPM thì HTQC phải khác CPC

 SELECT hd.TenKhachHang, hd.HopDongID,hd.SoHopDong, hdct.HopDongChiTietID,hdct.TenLoai AS HTQC, hdct.TenBanner,
 hdct.DmSanPhamREF,
hdct.TenSanPham, hdct.DonViTinh, hdct.DonGia, hdct.ThanhTien, hdct.ThanhTienThucChay,ROUND(hdct.ThanhTien- hdct.ThanhTienThucChay,0)lechhdtc, hdct.GhiChu,hdct.CreatedBy NguoiTao, hdct.LastModifiedBy NguoiSuaCuoi
	FROM dbo.HopDong hd FULL OUTER JOIN 
		dbo.HopDongChiTiet hdct ON hd.HopDongID=hdct.HopDongFK
	WHERE (DonViTinh<>N'CPC' AND TenLoai=N'CPC' AND NOT(hdct.DmLoaiBannerREF = 17 OR hdct.DmLoaiNenTangREF = 8))
	AND hdct.DeletedStatus = 0
	AND hd.TrangThaiHopDong <> 3
	AND hdct.DmSanPhamREF NOT IN(688,306,423,144,628,585) --Back fill
	--AND hd.SoHopDong NOT IN ('QC3350315','QC2860116')
	AND hd.NgayDanhSoHopDong >= '2015-01-01'
ORDER BY ROUND(hdct.ThanhTien- hdct.ThanhTienThucChay,0)

END


```
