# Function: `GetValuesThucChayTestTinhByHopDongChiTietID`

- **Loại**: SQL_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2014-09-30 16:37:05.747000
- **Ngày sửa cuối**: 2014-09-30 16:37:05.747000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@HopDongREF` | `int(4)` | No |
| `@HopDongChiTietREF` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE FUNCTION GetValuesThucChayTestTinhByHopDongChiTietID
(
	@HopDongREF INT,
	@HopDongChiTietREF INT,
	@NgayThucHien DATETIME
)
RETURNS 
@ThucChayTestTinh TABLE 
(
	HopDongREF INT,
	SoHopDong NVARCHAR(50),
	HopDongChiTietREF INT,	
	SoLuongMua INT,
	--DonGiaNgay FLOAT,
	--SoLuongThucChay_DotChay INT,
	--SoLuongThucChay_KhongDotChay INT,
	ThanhTienHD FLOAT,
	TienThucChayTestTinh FLOAT,
	TienThucChay_tcdt FLOAT
)
AS
BEGIN	
	INSERT INTO @ThucChayTestTinh
	SELECT
	@HopDongREF	
	, tempt.SoHopDong
	, tempt.HopDongChiTietID
	, tempt.SoLuongMua
	, tempt.ThanhTien		
	, tempt.TienThucChaySauCK	
	, tempt.TienThucChay_tcdt
	--, (tempt.TienThucChaySauCK - tempt.TienThucChay_tcdt)
	--, '' 
	FROM
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
	, hdct.ThanhTien/ isnull(dbo.ThucChay_GetSoLuongNgayDotChayHopDongChiTiet(hdct.SoLuong, hdct.DonViTinh, hdct.HopDongChiTietID),0) AS DonGiaNgay
	, dbo.ThucChay_GetSoLuongThucChayBooking_CPDDotChay(hdct.SoLuong, hdct.DonViTinh, hdct.HopDongChiTietID, @NgayThucHien) AS SoLuongThucChay_DotChay
	, dbo.ThucChay_GetSoLuongThucChayBooking_CPDKhongDotChay(hdct.SoLuong, hdct.DonViTinh, hdct.HopDongChiTietID, @NgayThucHien) AS SoLuongThucChay_KhongDotChay
	--, tchdct.ThoiGianBatDau
	--, tchdct.ThoiGianKetThuc
	FROM HopDong hd 
	INNER JOIN HopDongChiTiet hdct 
	ON ( hd.HopDongID = hdct.HopDongFK 
	AND hd.DeletedStatus = 0 AND hdct.DeletedStatus = 0
	AND hd.HopDongID = @HopDongREF  
	AND hdct.HopDongChiTietID = @HopDongChiTietREF
	)			
	) A FULL OUTER JOIN
	(
	SELECT tcdt.HopDongID, tcdt.HopDongChiTietREF, SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi) AS ThanhTienThucChay
	FROM ThucChayDaTinh tcdt 
	WHERE tcdt.HopDongID = @HopDongREF
	AND tcdt.HopDongChiTietREF = @HopDongChiTietREF								                               		
	GROUP BY tcdt.HopDongID, tcdt.HopDongChiTietREF
	)B ON A.HopDongID = B.HopDongID AND A.HopDongChiTietID = B.HopDongChiTietREF
	) tempt	
	
	
	RETURN 
END

```
