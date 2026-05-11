# Stored Procedure: `KiemTra_DaTinh_CPD_TinhDungDu_BySoHopDong`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-07-15 16:37:26.147000
- **Ngày sửa cuối**: 2020-11-13 16:51:10.250000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@SoHopDong` | `nvarchar(100)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[KiemTra_DaTinh_CPD_TinhDungDu_BySoHopDong]
	-- Add the parameters for the stored procedure here
	@SoHopDong nvarchar(50),
	@NgayThucHien DATETIME
    
AS
BEGIN
	DECLARE @HopDongID NVARCHAR(MAX)

--QC3180315 hd hủy
--SET @NgayThucHien = '2016-10-31'
SELECT tempt.*, (tempt.TienThucChaySauCK - tempt.TienThucChay_tcdt) AS Lech FROM
(
	SELECT 
	A.SoHopDong
	, A.HopDongChiTietID
	, A.TenSanPham
	, A.TenWebsite
	, A.SoLuongMua
	, A.SoLuongThucChay_DotChay	
	, A.SoLuongThucChay_KhongDotChay
	, A.ThanhTien
	/*
	, CASE 
	WHEN ISNULL(A.SoLuongThucChay_DotChay, 0) > 0 THEN  ROUND(A.DonGiaNgay*A.SoLuongThucChay_DotChay,0) 
	ELSE ROUND(A.DonGiaNgay*A.SoLuongThucChay_KhongDotChay,0)
	END TienThucChaySauCK
	*/ --tuyetnta sửa
	, CASE 
	WHEN ISNULL(A.SoLuongThucChay_DotChay, 0) > 0 THEN  ROUND(A.DonGiaNgay*A.SoLuongThucChay_KhongDotChay,0) 
	ELSE ROUND(A.DonGiaNgay*A.SoLuongThucChay_KhongDotChay,0)
	END TienThucChaySauCK

	, ISNULL(round(B.ThanhTienThucChay,0),0) AS TienThucChay_tcdt
	--, (ISNULL(round(A.TienThucChaySauCK,0),0) - ISNULL(round(B.ThanhTienThucChay,0),0)) AS TienLech 
	FROM
	(
		SELECT 
		hd.HopDongID
	, hd.SoHopDong
	, hdct.HopDongChiTietID
	, hdct.TenSanPham
	, hdct.TenWebsite
	, hdct.SoLuong
	, hdct.DonViTinh
	, isnull(dbo.ThucChay_GetSoLuongNgayDotChayHopDongChiTiet(hdct.SoLuong, hdct.DonViTinh, hdct.HopDongChiTietID),0) AS SoLuongMua
	, hdct.DonGia
	, (CASE WHEN hd.TrangThaiHopDong = 3 THEN 0 ELSE hdct.ThanhTien	 END)ThanhTien
	,(CASE WHEN  dbo.ThucChay_GetSoLuongNgayDotChayHopDongChiTiet(hdct.SoLuong, hdct.DonViTinh, hdct.HopDongChiTietID)<> 0 THEN
		 hdct.ThanhTien/dbo.ThucChay_GetSoLuongNgayDotChayHopDongChiTiet(hdct.SoLuong, hdct.DonViTinh, hdct.HopDongChiTietID)
		 ELSE - 1 END)
	 AS DonGiaNgay
	, dbo.ThucChay_GetSoLuongThucChayBooking_CPDDotChay(hdct.SoLuong, hdct.DonViTinh, hdct.HopDongChiTietID, @NgayThucHien) AS SoLuongThucChay_DotChay
	, dbo.ThucChay_GetSoLuongThucChayBooking_CPDKhongDotChay(hdct.SoLuong, hdct.DonViTinh, hdct.HopDongChiTietID, @NgayThucHien) AS SoLuongThucChay_KhongDotChay
		--, tchdct.ThoiGianBatDau
		--, tchdct.ThoiGianKetThuc
		FROM HopDong hd 
		INNER JOIN HopDongChiTiet hdct 
			ON ( hd.HopDongID = hdct.HopDongFK 
				AND hd.DeletedStatus = 0 AND hdct.DeletedStatus = 0
				--AND hd.HopDongID IN (SELECT LTRIM(RTRIM(item)) FROM dbo.ArrayToTable(dbo.Array(@HopDongID, ',')))
			)
		--LEFT JOIN ThucChayHopDongChiTiet tchdct ON hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
		WHERE 
		hdct.DmSanPhamREF IN (140, 385, 228,
											549, 5005, 5006, 5007, 5058)-- SP TMÐT
		AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, hdct.DonViTinh) = 1
		AND NOT  (hdct.DmLoaiBannerREF =18 or hdct.DmLoaiREF= 13)
		AND SoHopDong = @SoHopDong
		
	) A FULL OUTER JOIN
	(
		SELECT tcdt.HopDongID, tcdt.HopDongChiTietREF, SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS ThanhTienThucChay
		  FROM ThucChayDaTinh tcdt 
		WHERE --tcdt.HopDongID IN (SELECT LTRIM(RTRIM(item)) FROM dbo.ArrayToTable(dbo.Array(@HopDongID, ',')))	
		1=1 AND tcdt.DmSanPhamREF IN (140, 385, 228,
											549, 5005, 5006, 5007, 5058)-- SP TMÐT
		AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, tcdt.DonViTinh) = 1	
		AND tcdt.NgayThucHien <= @NgayThucHien				
		AND NOT ( tcdt.DmHinhThucQuangCao = 13	OR DmLoaiBannerREF = 18)			
		AND SoHopDong = @SoHopDong
		GROUP BY tcdt.HopDongID, tcdt.HopDongChiTietREF
	)B ON A.HopDongID = B.HopDongID AND A.HopDongChiTietID = B.HopDongChiTietREF
) tempt
 WHERE ABS((tempt.TienThucChaySauCK - tempt.TienThucChay_tcdt))>1
--select dbo.ThucChay_GetSoLuongThucChayBooking_CPDDotChay(hdct.SoLuong, hdct.DonViTinh, hdct.HopDongChiTietID, '2014-09-20')
--FROM HopDongChiTiet hdct WHERE hdct.HopDongChiTietID = 64388


END

```
