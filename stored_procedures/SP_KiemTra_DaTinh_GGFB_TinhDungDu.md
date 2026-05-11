# Stored Procedure: `KiemTra_DaTinh_GGFB_TinhDungDu`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-23 09:47:54.403000
- **Ngày sửa cuối**: 2016-11-23 09:47:54.403000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@ngaythuchien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
CREATE PROC KiemTra_DaTinh_GGFB_TinhDungDu

 @ngaythuchien DATETIME
 AS
 
BEGIN
	SELECT IP.*, TC.* FROM 
--- ThucChayGGFBInput
	(
		SELECT C.SoHopDong,C.DmSanPhamREF,C.DmLoaiBannerREF,
		SUM(C.SoLuongThucChay) SoLuongThucChayIP,
		SUM(C.ThanhTienThucChay) ThanhTienThucChayIP 
		FROM (
			SELECT B.* FROM
		(SELECT SoHopDong, MAX(NgayThucHien) NgayThucHienMAx  FROM ThucChayGGFBInput
		GROUP BY SoHopDong
		)A
	LEFT JOIN 
		(SELECT tcg.SoHopDong, tcg.DmSanPhamREF, tcg.NhanHopDong, tcg.DonViTinh, tcg.DmLoaiBannerREF, tcg.TenLoaiBanner, 
		tcg.SoLuongThucChay, tcg.ThanhTienThucChay, tcg.NgayThucHien
		FROM ThucChayGGFBInput tcg)B
		ON A.SoHopDong =B.SoHopDong
		AND A.NgayThucHienMAx =B.NgayThucHien
		WHERE CONVERT (DATE,A.NgayThucHienMAx) =@ngaythuchien 
	--AND B.SoHopDong='QC1080416'
			)C 
		GROUP BY C.SoHopDong,C.DmSanPhamREF,C.DmLoaiBannerREF
		)IP
	LEFT JOIN
		(  
		SELECT tcdt.SoHopDong,tcdt.HopDongID,tcdt.DmSanPhamREF, tcdt.TenSanPham,tcdt.DmWebsiteREF,tcdt.TenWebsite, tcdt.DmLoaiBannerREF,tcdt.TenLoaiBanner,
		SUM(tcdt.SoLuongThucChay) SoLuongThucChay,
		SUM(tcdt.ThanhTienSauTrietKhauThucChay+tcdt.GiaTriThayDoi) ThanhTienTC
		FROM ThucChayDaTinh tcdt
		WHERE tcdt.DmSanPhamREF IN (423,306,535,251)
		AND tcdt.TrangThaiHopDong <> 3
     --AND tcdt.SoHopDong='QC1080416'
		AND NOT ( tcdt.DmHinhThucQuangCao =13 OR tcdt.DmLoaiBannerREF = 18)
		GROUP BY tcdt.SoHopDong,tcdt.HopDongID,tcdt.DmSanPhamREF, tcdt.TenSanPham,tcdt.DmWebsiteREF,tcdt.TenWebsite, tcdt.DmLoaiBannerREF,tcdt.TenLoaiBanner
		 )TC ON IP.SoHopDong = TC.SoHopDong AND TC.TenSanPham = IP.DmSanPhamREF AND IP.DmLoaiBannerREF=TC.DmLoaiBannerREF
		WHERE  ISNULL(ROUND(IP.ThanhTienThucChayIP, 0), 0) <> ISNULL(ROUND(TC.ThanhTienTC, 0), 0) AND IP.SoHopDong NOT IN ('QC1770516')
		ORDER BY  TC.SoHopDong

END
```
