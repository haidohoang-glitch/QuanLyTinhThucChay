# Stored Procedure: `sp_nhung_KT_hamtinh_Branding_True_View`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-20 08:57:03.067000
- **Ngày sửa cuối**: 2026-03-20 08:57:03.067000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_nhung_KT_hamtinh_Branding_True_View
AS
BEGIN
    SET NOCOUNT ON;
	SELECT 'True_View' Thiếu_True_View, C.SoHopDong,C.DmSanPhamREF,C.HopDongChiTietID,dbo.formatnumber(C.SoluongHD) SLHĐ,C.ChietKhau,C.DonGia DonGiaHĐ
	,dbo.FormatNumber( CASE WHEN C.ChietKhau = 100 THEN C.ThanhtienKM ELSE C.ThanhTien END) AS ThanhtienHD
	--,ROUND(C.TongTrue_ViewThucChay,0) AS SoluongTool
	,dbo.FormatNumber(CASE WHEN C.ChietKhau = 100 THEN ROUND(C.TongTrue_ViewThucChay * C.DonGia,0) ELSE ROUND(C.TongTrue_ViewThucChay * C.DonGia * (100-C.ChietKhau)/100,0) END) Thanhtien_tool
	--,ROUND( CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.SLKM,0) ELSE ISNULL(D.SL,0) END,0) AS SoluongTC
	,dbo.FormatNumber( CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM,0)ELSE ISNULL(D.thanhtien,0) END) AS ThanhtienTC
	,ROUND(CASE WHEN C.ChietKhau = 100 THEN ROUND(C.TongTrue_ViewThucChay * C.DonGia,0) ELSE ROUND(C.TongTrue_ViewThucChay * C.DonGia * (100-C.ChietKhau)/100,0) END,0) - ROUND(CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM,0)ELSE ISNULL(D.thanhtien,0) END,0) Lech_SP_ASD
	,ROUND(CASE WHEN C.ChietKhau = 100 THEN C.ThanhtienKM ELSE C.ThanhTien END,0) - ROUND(CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM,0)ELSE ISNULL(D.thanhtien,0) END,0) Lech_HĐ_ASD
	FROM (
		SELECT * FROM (
			SELECT hd.SoHopDong,hdct.HopDongChiTietID,hdct.DonViTinhREF,hdct.DonViTinh
			,CASE WHEN hdct.DonViTinhREF = 1 THEN hdct.SoLuong*1000 ELSE hdct.SoLuong END AS SoluongHD
			,hdct.ChietKhau, hdct.ThanhTien,hdct.DmSanPhamREF ,hdct.DonGia,(hdct.SoLuong * hdct.DonGia ) ThanhtienKM
			FROM dbo.HopDong hd INNER JOIN dbo.HopDongChiTiet hdct 
			ON hd.HopDongID=hdct.HopDongFK
			WHERE hdct.DmSanPhamREF IN (339,240,598,342,505,733,5056,5299) 
			AND hdct.DonViTinhREF = 32
			AND hd.Nam >=2022 AND NOT hdct.DmLoaiNenTangREF = 9
			AND NOT hdct.DmLoaiREF = 42
			--AND hd.SoHopDong ='QC0580122'
		)A INNER JOIN(
			SELECT E.HopDongChiTietREF,SUM(TongTrue_ViewThucChay) TongTrue_ViewThucChay FROM (
			SELECT DISTINCT(DmBannerREF),HopDongChiTietREF FROM dbo.ThucChayHopDongChiTiet WHERE DeletedStatus = 0
			)E INNER JOIN (
			SELECT tc.bannerid,SUM(tc.True_View) TongTrue_ViewThucChay
			FROM dbo.ThucChayTrueView tc
			--WHERE tc.SoHopDong ='QC1960422'
			GROUP BY tc.bannerid
			)F 
			ON CONVERT(NVARCHAR(1000), E.DmBannerREF) = CONVERT(NVARCHAR(1000),F.bannerid)
			GROUP BY E.HopDongChiTietREF
		)B
		ON A.HopDongChiTietID=B.HopDongChiTietREF

	)C LEFT JOIN(
		SELECT TCDT.HopDongChiTietREF,SUM(TCDT.SoLuongThucChay+TCDT.SoLuongThayDoi) AS SL,SUM(TCDT.ThanhTienSauTrietKhauThucChay+TCDT.GiaTriThayDoi) AS thanhtien
		,SUM(TCDT.SoLuongThucChayKM + TCDT.SoLuongKMThayDoi) AS SLKM,SUM(TCDT.ThanhTienKM +TCDT.GiaTriKMThayDoi) AS thanhtienKM	
		FROM dbo.ThucChayDaTinh TCDT
		WHERE TCDT.DmHinhThucQuangCao NOT IN (13,42)
		AND TCDT.DmSanPhamREF IN (339,240,598,342,505,733,821,5133,5056)
		--AND YEAR(TCDT.NgayThucHien)= 2022
		GROUP BY TCDT.HopDongChiTietREF
	)D
	ON C.HopDongChiTietREF = D.HopDongChiTietREF
	WHERE 1=1
	AND NOT ROUND( CASE WHEN C.ChietKhau = 100 THEN C.ThanhtienKM ELSE C.ThanhTien END,0) = ROUND( CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM,0)ELSE ISNULL(D.thanhtien,0) END,0)
	AND NOT ROUND(C.TongTrue_ViewThucChay,0) = ROUND( CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.SLKM,0) ELSE ISNULL(D.SL,0) END,0)
	ORDER BY C.DmSanPhamREF
END


```
