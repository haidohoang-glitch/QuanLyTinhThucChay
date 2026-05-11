# Stored Procedure: `sp_nhung_KT_hamtinh_Branding_Bai`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2026-03-20 08:53:35.577000
- **Ngày sửa cuối**: 2026-03-20 08:53:35.577000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
CREATE PROCEDURE sp_nhung_KT_hamtinh_Branding_Bai
AS
BEGIN
    SET NOCOUNT ON;
	SELECT 'branding' branding_Bai,C.SoHopDong,C.HopDongID,C.HopDongChiTietID,C.DonViTinh,C.SoLuong,dbo.FormatNumber(C.DonGia) ĐonGiaHĐ,C.ChietKhau
	,dbo.FormatNumber(CASE WHEN C.ChietKhau = 100 THEN C.SoLuong*C.DonGia ELSE C.ThanhTien END) ThanhTienHĐ
	,ISNULL(C.Soluongtreo,0) Soluongtreo
	,dbo.FormatNumber(CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.SoluongTCKM,0) ELSE ISNULL(D.SoluongTC,0) END ) SoluongTC_ASD
	,dbo.FormatNumber(CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.ThanhtienTCKM,0) ELSE ISNULL(D.ThanhtienTC,0) END) ThanhtienTC_ASD
	FROM(
		SELECT A.*,B.Soluongtreo FROM(
			SELECT hd.HopDongID,hd.SoHopDong,hdct.HopDongChiTietID,hdct.DonViTinh,hdct.SoLuong,hdct.DonGia,hdct.ChietKhau,hdct.ThanhTien FROM dbo.HopDongChiTiet hdct
			INNER JOIN dbo.HopDong hd
			ON hd.HopDongID = hdct.HopDongFK
			WHERE 1=1 
			AND hdct.DmSanPhamREF IN (598) 
			AND hdct.DonViTinhREF IN (7)
			AND not hdct.DmLoaiREF = 42
			AND hd.DeletedStatus = 0
			AND hdct.DeletedStatus = 0
			AND hd.TrangThaiHopDong NOT IN (0,3)
			--and HopDongChiTietID ='744047'
		)A LEFT JOIN (
			SELECT COUNT(*) Soluongtreo,tt.HopDongChiTietREF
			FROM dbo.ThucChayHopDongChiTiet tt
			WHERE tt.DeletedStatus =0
			GROUP BY tt.HopDongChiTietREF
		)B ON A.HopDongChiTietID = B.HopDongChiTietREF
	)C LEFT JOIN (
		SELECT tcdt.HopDongChiTietREF
		,SUM(tcdt.SoLuongThucChay+tcdt.SoLuongThayDoi) SoluongTC
		,SUM(tcdt.SoLuongThucChayKM+tcdt.SoLuongKMThayDoi) SoluongTCKM
		,SUM(tcdt.ThanhTienSauTrietKhauThucChay+tcdt.GiaTriThayDoi) ThanhtienTC
		,SUM(tcdt.ThanhTienKM+tcdt.GiaTriKMThayDoi) ThanhtienTCKM
		FROM dbo.ThucChayDaTinh tcdt
		GROUP BY tcdt.HopDongChiTietREF
	)D ON C.HopDongChiTietID = D.HopDongChiTietREF
	WHERE 1=1
		And ISNULL(C.Soluongtreo,0) <= C.SoLuong
		AND ISNULL(C.Soluongtreo,0) <> CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.SoluongTCKM,0) ELSE ISNULL(D.SoluongTC,0) END 
		AND CASE WHEN C.ChietKhau = 100 THEN ISNULL(D.SoluongTCKM,0) ELSE ISNULL(D.SoluongTC,0) END <> C.SoLuong
		AND NOT C.SoHopDong IN ('QC2651220','QC0990221','QC2180822','QC3990922','QC3510521')
	ORDER BY C.HopDongID

END


```
