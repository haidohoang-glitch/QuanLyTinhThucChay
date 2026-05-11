# Stored Procedure: `KiemTraHopDongCPD`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2017-02-14 16:58:51.523000
- **Ngày sửa cuối**: 2017-02-14 16:58:51.523000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongID` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE KiemTraHopDongCPD 
	-- Add the parameters for the stored procedure here
	@HopDongID int , @NgayThucHien DATETIME
AS
BEGIN
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
	, CASE 
	WHEN ISNULL(A.SoLuongThucChay_DotChay, 0) > 0 THEN  ROUND(A.DonGiaNgay*A.SoLuongThucChay_DotChay,0) 
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
	, hdct.ThanhTien	
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
				AND hd.HopDongID IN 
				(SELECT LTRIM(RTRIM(item)) FROM dbo.ArrayToTable(dbo.Array(@HopDongID, ',')))
			)
		--LEFT JOIN ThucChayHopDongChiTiet tchdct ON hdct.HopDongChiTietID = tchdct.HopDongChiTietREF
		WHERE 
		hdct.DmSanPhamREF IN (140,228, 370, 241, 564, 549, 385, 
											264,300,268,248,270,243,244,249)-- SP TMĐT
		AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, hdct.DonViTinh) = 1
		AND hdct.DmLoaiBannerREF NOT IN (17,18)
		AND hdct.DmLoaiREF <> 13
	) A FULL OUTER JOIN
	(
		SELECT tcdt.HopDongID, tcdt.HopDongChiTietREF, SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS ThanhTienThucChay
		  FROM ThucChayDaTinh tcdt 
		WHERE tcdt.HopDongID IN (SELECT LTRIM(RTRIM(item)) FROM dbo.ArrayToTable(dbo.Array(@HopDongID, ',')))	
		AND tcdt.DmSanPhamREF IN (140,228, 370, 241, 564, 549, 385, 
											264,300,268,248,270,243,244,249)-- SP TMĐT
		AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, tcdt.DonViTinh) = 1	
		AND tcdt.NgayThucHien <= @NgayThucHien				
		AND tcdt.DmHinhThucQuangCao <> 13		
			AND tcdt.DmLoaiBannerREF NOT IN (17,18)			                               		
		GROUP BY tcdt.HopDongID, tcdt.HopDongChiTietREF
	)B ON A.HopDongID = B.HopDongID AND A.HopDongChiTietID = B.HopDongChiTietREF
) tempt

END

```
