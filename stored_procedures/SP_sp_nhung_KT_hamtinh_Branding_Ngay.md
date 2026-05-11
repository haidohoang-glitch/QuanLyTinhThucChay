# Stored Procedure: `sp_nhung_KT_hamtinh_Branding_Ngay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-20 08:56:18.747000
- **Ngày sửa cuối**: 2026-03-20 08:56:18.747000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_nhung_KT_hamtinh_Branding_Ngay
AS
BEGIN
    SET NOCOUNT ON;
	SELECT 'DonViNgay' Thieu_Branding_Ngay,C.SoHopDong,C.HopDongChiTietID,C.SoLuongHĐ,ROUND(C.DonGia, 0) DonGia,C.ChietKhau,
	CASE WHEN C.ChietKhau = 100 THEN ROUND(C.ThanhtienKM, 0) ELSE C.ThanhtienHD END thanhtienHĐ,C.SoLuongTreo,
	CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.SoluongKM, 0) ELSE ISNULL(D.SoluongTC, 0) END SoluongTC,
	CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM, 0) ELSE ISNULL(D.thanhtienTC, 0) END thanhtienTC
	FROM (	
		SELECT A.SoHopDong,A.HopDongChiTietID,DonGia, A.ChietKhau,ROUND(A.ThanhTien, 0) ThanhtienHD,SUM(B.SoLuongTreo) SoLuongTreo,A.ThanhtienKM, SUM(A.SoLuongDC) AS SoLuongHĐ
		FROM(
			SELECT DISTINCT (dchdct.BookingREF),hd.SoHopDong, hdct.HopDongChiTietID, hdct.SoLuong, hdct.ChietKhau, hdct.DonGia,hdct.ThanhTien,(hdct.SoLuong * hdct.DonGia) AS ThanhtienKM,     DATEDIFF(DAY, dchdct.ThoiGianBatDau, dchdct.ThoiGianKetThuc) + 1 AS SoLuongDC
			FROM dbo.HopDongChiTiet hdct
			INNER JOIN dbo.HopDong hd    ON hd.HopDongID = hdct.HopDongFK
			LEFT JOIN DotChayHopDongChiTiet dchdct  ON (  hdct.HopDongChiTietID = dchdct.HopDongChiTietREF  AND dchdct.DeletedStatus <> 1)
			WHERE hdct.DmSanPhamREF NOT IN ( 140, 228, 549, 385, 564, 5007, 5005, 736, 5082, 252, 5006 ) --sp không phải CPD 
			AND hd.Nam >= 2022 
			AND hdct.DonViTinhREF IN (3,4) -- đơn vị ngày, tuần	
		) A
		LEFT JOIN
		(
		SELECT DISTINCT (tchdct.BookingREF),                tchdct.ThoiGianBatDau,                tchdct.ThoiGianKetThuc,                tchdct.HopDongChiTietREF,
		CASE WHEN CONVERT(DATE, tchdct.ThoiGianKetThuc) > GETDATE() - 1 THEN DATEDIFF(DAY, tchdct.ThoiGianBatDau, GETDATE() - 1) + 1
		ELSE DATEDIFF(DAY, tchdct.ThoiGianBatDau, tchdct.ThoiGianKetThuc) + 1
		END AS SoLuongTreo
		--,DATEDIFF(DAY,tchdct.ThoiGianBatDau, tchdct.ThoiGianKetThuc)+1 AS SoLuongTreo  
		FROM ThucChayHopDongChiTiet tchdct
		WHERE tchdct.DeletedStatus = 0 --AND tchdct.HopDongChiTietREF  = '691701'
		AND NOT (CONVERT(DATE, tchdct.CreatedAt) > GETDATE() - 1 OR CONVERT(DATE, tchdct.LastModifiedAt) > GETDATE() - 1)
		) B
		ON A.HopDongChiTietID = B.HopDongChiTietREF
		AND A.BookingREF = B.BookingREF 
		WHERE B.SoLuongTreo > 0 GROUP BY A.SoHopDong,A.HopDongChiTietID,A.DonGia,A.ChietKhau,A.ThanhTien,A.ThanhtienKM
	) C LEFT JOIN (
		SELECT HopDongChiTietREF,
		SUM(SoLuongThucChay + SoLuongThayDoi) SoluongTC,
		SUM(SoLuongThucChayKM + SoLuongKMThayDoi) SoluongKM,
		ROUND(SUM(ThanhTienSauTrietKhauThucChay + GiaTriThayDoi), 0) thanhtienTC,
		ROUND(SUM(ThanhTienKM + GiaTriKMThayDoi), 0) thanhtienKM
		FROM ThucChayDaTinh 
		GROUP BY HopDongChiTietREF
	) D
	ON C.HopDongChiTietID = D.HopDongChiTietREF
	WHERE 1 = 1 
	AND (ABS( CASE WHEN C.ChietKhau = 100 THEN ROUND(C.ThanhtienKM, 0) ELSE C.ThanhtienHD END- CASE  WHEN C.ChietKhau = 100 THEN ISNULL(D.thanhtienKM, 0) ELSE ISNULL(D.thanhtienTC, 0) END)> 1000)
	ORDER BY C.SoHopDong;
END


```
