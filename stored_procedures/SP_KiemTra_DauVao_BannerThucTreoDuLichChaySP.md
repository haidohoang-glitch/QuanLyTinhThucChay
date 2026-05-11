# Stored Procedure: `KiemTra_DauVao_BannerThucTreoDuLichChaySP`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-18 11:15:28.047000
- **Ngày sửa cuối**: 2017-02-24 10:18:12.053000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

CREATE  PROCEDURE [dbo].[KiemTra_DauVao_BannerThucTreoDuLichChaySP] 
AS
BEGIN

	DECLARE @NgayThucHien DATETIME
	DECLARE @Nam_check INT = 2017
	---DANH SACH CAC HOP DONG CHI TIET CAN CHECK
	SELECT DISTINCT TT.SoHopDong, tt.HopDongREF, tt.HopDongChiTietREF, tt.DmBannerREF, TC.TenSanPham
	FROM
	(
		SELECT hd.SoHopDong, A.HopDongREF, A.HopDongChiTietREF, d.DmBannerREF, d.ThoiGianBatDau,d.ThoiGianKetThuc 
		FROM dbo.ThucChayHopDongChiTiet d
		INNER JOIN
		(
				SELECT ThucChayHopDongChiTietID, HopDongREF, HopDongChiTietREF FROM dbo.ThucChayHopDongChiTiet
				WHERE DeletedStatus = 0
				AND BookingREF <> 0
				AND NOT(YEAR(ThoiGianBatDau) > @Nam_check OR YEAR(ThoiGianKetThuc) <@Nam_check)
		)A ON d.ThucChayHopDongChiTietID = a.ThucChayHopDongChiTietID
		INNER JOIN dbo.HopDong hd ON d.HopDongREF = hd.HopDongID
		WHERE d.DmSanPhamREF IN (140,228,549,385)
	)TT
	INNER JOIN 
	(
		SELECT DISTINCT SoHopDong, DmBannerREF, TenSanPham, NgayThucHien,TongViewThucChay FROM dbo.ThucChay
		WHERE TypeProduct in (-3,-2)
		AND YEAR(NgayThucHien) = @Nam_check
	)TC ON tC.SoHopDong = TT.SoHopDong AND CONVERT(NVARCHAR(50),tc.DmBannerREF) = tt.DmBannerREF
	WHERE 1=1
	AND (TC.NgayThucHien <tt.ThoiGianBatDau OR tc.NgayThucHien > tt.ThoiGianKetThuc)


END

--EXEC [KiemTra_DauVao_CPD_SoLuongVaDotChayHDLechNhau]

```
