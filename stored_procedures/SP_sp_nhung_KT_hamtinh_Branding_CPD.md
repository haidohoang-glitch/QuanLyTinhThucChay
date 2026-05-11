# Stored Procedure: `sp_nhung_KT_hamtinh_Branding_CPD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-20 08:58:13.190000
- **Ngày sửa cuối**: 2026-03-20 08:58:13.190000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_nhung_KT_hamtinh_Branding_CPD
AS
BEGIN
    SET NOCOUNT ON;
SELECT C.SoHopDong,C.HopDongChiTietID,C.DmSanPhamREF,C.TenSanPham,C.TenLoai,C.DonViTinhREF,C.DonViTinh, dbo.formatnumber(C.SoLuongHĐ) SoLuongDCHĐ
	,dbo.formatnumber(C.thanhtienHĐ / C.SoLuongHĐ) ĐonGia_1ngay,C.ChietKhau, dbo.formatnumber(C.thanhtienHĐ) thanhtienHĐ
	,C.SoLuongTreo,CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.SoluongKM,0) ELSE ISNULL(D.SoluongTC,0) END SoluongTC
	, dbo.formatnumber(CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.ThanhTienKM,0) ELSE  ISNULL(D.ThanhTienTC,0) END) thanhtienTC
	,dbo.formatnumber(CASE WHEN C.DonViTinhREF = 10 AND NOT C.SoLuongTreo is NULL THEN C.thanhtienHĐ ELSE  CASE WHEN ISNULL(C.SoLuongTreo,0) > C.SoLuongHĐ THEN C.SoLuongHĐ ELSE ISNULL(C.SoLuongTreo,0) END * (C.thanhtienHĐ / C.SoLuongHĐ) END ) TTTC_Mongmuon
	,dbo.formatnumber(CASE WHEN C.DonViTinhREF = 10 AND NOT C.SoLuongTreo is NULL THEN C.thanhtienHĐ ELSE C.SoLuongTreo * (C.thanhtienHĐ / C.SoLuongHĐ) END - CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.ThanhTienKM,0) ELSE  ISNULL(D.ThanhTienTC,0) END) Lệch
	,CASE  WHEN C.DonViTinhREF <> 10 and ROUND(C.SoLuongHĐ,0) <> ROUND(C.SoLuongTreo,0) THEN CONCAT( N'Số lượng ngày treo:', ROUND(C.SoLuongTreo,0), N' <> SL Đợt chạy HĐ:',ROUND(C.SoLuongHĐ,0))
		   WHEN ROUND(CASE WHEN C.DonViTinhREF = 10 AND NOT C.SoLuongTreo is NULL THEN C.thanhtienHĐ ELSE C.SoLuongTreo * (C.thanhtienHĐ / C.SoLuongHĐ) END - CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.ThanhTienKM,0) ELSE  ISNULL(D.ThanhTienTC,0) END,0) <> 0 THEN CONCAT(N'Phân bổ ghi nhận thiếu : ',dbo.FormatNumber(CASE WHEN C.DonViTinhREF = 10 THEN C.thanhtienHĐ ELSE C.SoLuongTreo * (C.thanhtienHĐ / C.SoLuongHĐ) END - CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.ThanhTienKM,0) ELSE  ISNULL(D.ThanhTienTC,0) END))
	ELSE N'' END GhiChu
	FROM (
	  SELECT A.HopDongID,A.SoHopDong,A.HopDongChiTietID,A.DonGia,A.ChietKhau, A.DonViTinhREF,A.DonViTinh,A.DmSanPhamREF,A.TenSanPham,
	  CASE WHEN A.ChietKhau = 100 THEN A.ThanhtienKM ELSE ROUND(A.ThanhTien,0) END thanhtienHĐ
	  ,SoLuongTreo,A.ThanhtienKM,A.SoLuongDC AS SoLuongHĐ,A.TenLoai
	  FROM (
		SELECT N.TenLoai,N.HopDongID,N.SoHopDong,N.HopDongChiTietID,N.SoLuong,N.ChietKhau,N.DonGia,N.ThanhTien ,N.ThanhtienKM,SUM(SoLuongDC) SoLuongDC,N.DonViTinhREF,N.DonViTinh,N.DmSanPhamREF,N.TenSanPham
			FROM(

			SELECT DISTINCT(dchdct.BookingREF),hd.HopDongID,hd.SoHopDong,hdct.HopDongChiTietID,hdct.SoLuong,hdct.ChietKhau,hdct.DonGia,hdct.ThanhTien 
			,(hdct.SoLuong*hdct.DonGia) AS ThanhtienKM,	DATEDIFF(DAY, dchdct.ThoiGianBatDau, dchdct.ThoiGianKetThuc)+1 AS SoLuongDC  
			,hdct.DonViTinhREF,hdct.DonViTinh,hdct.DmSanPhamREF,hdct.TenSanPham ,hdct.DmLoaiREF,hdct.TenLoai
			FROM dbo.HopDongChiTiet hdct
			INNER JOIN dbo.HopDong hd
			ON hd.HopDongID = hdct.HopDongFK
			LEFT JOIN DotChayHopDongChiTiet dchdct 
			ON (hdct.HopDongChiTietID = dchdct.HopDongChiTietREF AND dchdct.DeletedStatus <> 1)  
			WHERE hdct.DmSanPhamREF IN (140,228,549,385,564,5007,5005,736,5082,252,5006)
			AND DmLoaiBannerREF <> 5
			--AND hdct.HopDongChiTietID ='734084'
			AND hdct.DmLoaiREF <> 14
			AND hd.Nam > = 2022
		)N GROUP BY N.HopDongID,N.SoHopDong,N.HopDongChiTietID,N.SoLuong,N.ChietKhau,N.DonGia,N.ThanhTien ,N.ThanhtienKM,N.DonViTinhREF,N.DonViTinh,N.DmSanPhamREF,N.TenSanPham,N.TenLoai

	  ) A LEFT JOIN(
		SELECT Q.HopDongChiTietREF,SUM(Q.SoLuongTreo) SoLuongTreo FROM (
			SELECT DISTINCT(tchdct.BookingREF),tchdct.HopDongChiTietREF
			,CASE WHEN CONVERT(DATE,tchdct.ThoiGianKetThuc) > GETDATE()-1 
			THEN DATEDIFF(DAY,tchdct.ThoiGianBatDau, GETDATE()-1)+1 
			ELSE DATEDIFF(DAY,tchdct.ThoiGianBatDau, tchdct.ThoiGianKetThuc)+1 END AS SoLuongTreo 		
			FROM ThucChayHopDongChiTiet tchdct  
			WHERE tchdct.DeletedStatus = 0  
			--AND tchdct.HopDongChiTietREF ='684777'
			AND CASE WHEN CONVERT(DATE,tchdct.ThoiGianKetThuc) > GETDATE()-1 
					THEN DATEDIFF(DAY,tchdct.ThoiGianBatDau, GETDATE()-1)+1 
					ELSE DATEDIFF(DAY,tchdct.ThoiGianBatDau, tchdct.ThoiGianKetThuc)+1 END > 0
		)Q GROUP BY Q.HopDongChiTietREF
	  )B
	  ON A.HopDongChiTietID = B.HopDongChiTietREF  
	)C
	LEFT JOIN 
	( 
	  SELECT HopDongChiTietREF
	  ,SUM(SoLuongThucChay+SoLuongThayDoi) SoluongTC
	  ,SUM(SoLuongThucChayKM+SoLuongKMThayDoi) SoluongKM
	  ,ROUND(SUM(ThanhTienSauTrietKhauThucChay+GiaTriThayDoi),0) thanhtienTC
	  ,ROUND(SUM(ThanhTienKM+GiaTriKMThayDoi),0) thanhtienKM
	  FROM ThucChayDaTinh 
	  GROUP BY HopDongChiTietREF
	) D
	ON C.HopDongChiTietID = D.HopDongChiTietREF
	WHERE 1=1
	--AND C.HopDongChiTietID ='684777'
	AND ROUND(CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.ThanhTienKM,0) ELSE  ISNULL(D.ThanhTienTC,0) END,0) - ROUND(CASE WHEN C.DonViTinhREF = 10 AND NOT C.SoLuongTreo is NULL THEN C.thanhtienHĐ ELSE CASE WHEN C.SoLuongTreo > C.SoLuongHĐ THEN C.SoLuongHĐ ELSE C.SoLuongTreo end * (C.thanhtienHĐ / C.SoLuongHĐ) END,0) NOT BETWEEN -2 AND 2
	AND NOT (C.SoHopDong IN ('QC2601122','QC1261222','QC2370523','QC1790223','QC3260523','QC3901022','QC3800223','QC1480723')
	AND ROUND(C.thanhtienHĐ,0) = ROUND(CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.ThanhTienKM,0) ELSE  ISNULL(D.ThanhTienTC,0) END,0))
	AND NOT (C.SoHopDong IN ('NB0280322','QC4550923','QC1790223')
	AND ROUND(C.thanhtienHĐ,0) <> ROUND(CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.ThanhTienKM,0) ELSE  ISNULL(D.ThanhTienTC,0) END,0))
	ORDER BY GhiChu
END


```
