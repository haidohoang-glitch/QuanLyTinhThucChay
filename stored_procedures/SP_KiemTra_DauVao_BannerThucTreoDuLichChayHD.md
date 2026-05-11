# Stored Procedure: `KiemTra_DauVao_BannerThucTreoDuLichChayHD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-18 11:15:18.820000
- **Ngày sửa cuối**: 2017-02-24 10:06:38.697000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE  PROCEDURE [dbo].[KiemTra_DauVao_BannerThucTreoDuLichChayHD] 
AS
BEGIN

DECLARE @NgayThucHien DATETIME
DECLARE @Nam_check INT = 2017
---DANH SACH CAC HOP DONG CHI TIET CAN CHECK
SELECT
A.*,(A.TongSoLuongThucTreo - A.SoLuongHDCT_QuyDoi)ChenhLech FROM
(
	SELECT hd.SoHopDong, a.HopDongFK, a.HopDongChiTietID,A.SoLuong--, A.DonViTinhREF
	, A.DonViTinh,a.DmSanPhamREF, A.TenSanPham,
	(	CASE A.DonViTinh
					WHEN N'NGÀY' THEN A.SoLuong
					WHEN N'TUẦN' THEN  A.SoLuong*7
					WHEN N'THÁNG' THEN A.SoLuong*30
					WHEN N'NĂM' THEN A.SoLuong*365
				ELSE 0
	END	)SoLuongHDCT_QuyDoi,
	(CASE WHEN A.DmLoaiBannerREF <> 5 THEN
	(
		SELECT ISNULL(sum(DATEDIFF(day, dchdct.ThoiGianBatDau, dchdct.ThoiGianKetThuc) + 1),0)
		FROM (SELECT DISTINCT dchdct.BookingREF, dchdct.ThoiGianBatDau, dchdct.ThoiGianKetThuc, dchdct.HopDongChiTietREF, dchdct.HopDongREF  
		FROM dbo.ThucChayHopDongChiTiet dchdct WHERE 1=1 AND dchdct.DeletedStatus = 0)dchdct
		WHERE dchdct.HopDongChiTietREF = a.HopDongChiTietID
		
	)
	ELSE (SELECT ISNULL(sum(DATEDIFF(day, dchdct.ThoiGianBatDau, dchdct.ThoiGianKetThuc) + 1),0)
		FROM (SELECT DISTINCT dchdct.ThoiGianBatDau, dchdct.ThoiGianKetThuc, dchdct.HopDongChiTietREF, dchdct.HopDongREF  
		FROM dbo.ThucChayHopDongChiTiet dchdct WHERE 1=1 AND dchdct.DeletedStatus = 0)dchdct
		WHERE dchdct.HopDongChiTietREF = a.HopDongChiTietID
		)
	END
	)TongSoLuongThucTreo
	FROM
	(
	SELECT HopDongChiTietID, HopDongFK, DmSanPhamREF, DmLoaiBannerREF, TenSanPham, SoLuong, DonViTinhREF, UPPER(DonViTinh)DonViTinh
	FROM dbo.HopDongChiTiet
	WHERE ThanhTien <> ThanhtienThucChay
	AND DeletedStatus = 0
	AND DmSanPhamREF IN (140,228,564,549) 
	AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, DonViTinh) = 1 --Đơn vị của hình thức CPD 
	AND NOT (DmLoaiREF = 13 OR DmLoaiBannerREF IN (17,18))
	)A
	INNER JOIN 
	(
		SELECT DISTINCT HopDongREF, HopDongChiTietREF FROM dbo.ThucChayHopDongChiTiet
		WHERE DeletedStatus = 0
		AND BookingREF <> 0
		AND NOT(YEAR(ThoiGianBatDau) > 2017 OR YEAR(ThoiGianKetThuc) <2017)
	
	)B ON a.HopDongChiTietID = B.HopDongChiTietREF
	INNER JOIN dbo.HopDong hd ON A.HopDongFK = hd.HopDongID
	WHERE hd.TrangThaiHopDong <> 3
)A
WHERE 1=1
AND(
	((A.TongSoLuongThucTreo - A.SoLuongHDCT_QuyDoi) > 0 AND (a.DonViTinh = N'TUẦN' OR a.DonViTinh =N'NGÀY'))
	OR ((A.TongSoLuongThucTreo - A.SoLuongHDCT_QuyDoi) > A.SoLuong*1 AND (a.DonViTinh = N'THÁNG'))
	OR ((A.TongSoLuongThucTreo - A.SoLuongHDCT_QuyDoi) > 1 AND (a.DonViTinh = N'NĂM'))
)

END

--EXEC [KiemTra_DauVao_CPD_SoLuongVaDotChayHDLechNhau]

```
