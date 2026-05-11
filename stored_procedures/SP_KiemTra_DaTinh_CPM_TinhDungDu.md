# Stored Procedure: `KiemTra_DaTinh_CPM_TinhDungDu`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2016-11-21 11:22:05.513000
- **Ngày sửa cuối**: 2016-11-21 11:34:58.660000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@DmSanPhamREF` | `int(4)` | No |
| `@TypeProduct` | `int(4)` | No |

## Definition (Source Code)

```sql
--EXEC [KiemTra_DaTinh_CPM_TinhDungDu] '2015-01-01','2016-11-17',339,5
CREATE PROC  [dbo].[KiemTra_DaTinh_CPM_TinhDungDu]
@StartDate DATETIME,
@EndDate DATETIME, 
@DmSanPhamREF INT,
 @TypeProduct INT  
AS
BEGIN
--Sosanh thuc chay da tinh voi thuc chay
SELECT 
	TCDT.HopDongID,  TCDT.SoHopDong
	, TCDT.DmSanPhamREF
	, TCDT.TenSanPham
	, ISNULL(TCDT.SoLuongCPM,0)SoLuongCPM
	, ISNULL(TCDT.SoLuongCPC,0)SoLuongCPC
	, TC.cpmchay
	, TCDT.ThanhTien
	, TCDT.TienThucChay	
	, TC.cpmchay-TCDT.SoLuongCPM AS SLChenhLechCPM
	, TC.cpcchay-TCDT.SoLuongCPC AS SLChenhLechCPC 
	, TCDT.ThanhTien-TCDT.TienThucChay AS TienThieu
FROM
(
	SELECT
		tcdt.TenSanPham, tcdt.DmSanPhamREF, 
		(CASE
			when tcdt.DmSanPhamREF=231 then 3 
			when tcdt.DmSanPhamREF=238 then 4
			when tcdt.DmSanPhamREF=339 then 5
			when tcdt.DmSanPhamREF=239 then 6
			when tcdt.DmSanPhamREF=337 then 7
			when tcdt.DmSanPhamREF=240 then 8
			when tcdt.DmSanPhamREF=370 then 9
			WHEN tcdt.DmSanPhamREF=598 THEN 14
			WHEN tcdt.DmSanPhamREF=613 THEN 15				
			WHEN tcdt.DmSanPhamREF=680 THEN 16
		end) as TypeProduct
		, tcdt.HopDongID
		, tcdt.SoHopDong
		, ROUND(SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi),0) AS TienThucChay
		, ( SELECT SUM(hdct.SoLuong) FROM HopDongChiTiet hdct 
				WHERE hdct.HopDongFK = tcdt.HopDongID AND hdct.DmSanPhamREF = @DmSanPhamREF AND hdct.DonViTinhREF = 1 AND hdct.DeletedStatus = 0
		) AS SoLuongCPM
		, ( SELECT SUM(hdct.SoLuong) FROM HopDongChiTiet hdct 
				WHERE hdct.HopDongFK = tcdt.HopDongID AND hdct.DmSanPhamREF = @DmSanPhamREF AND hdct.DonViTinhREF = 2 AND hdct.DeletedStatus = 0
				
		) AS SoLuongCPC
		, ( SELECT SUM(hdct.ThanhTien) FROM HopDongChiTiet hdct 
				WHERE hdct.HopDongFK = tcdt.HopDongID AND hdct.DmSanPhamREF = @DmSanPhamREF AND hdct.DeletedStatus = 0
		) AS ThanhTien
		 
	FROM ThucChayDaTinh tcdt 
	WHERE CONVERT(date, tcdt.NgayThucHien) BETWEEN @StartDate AND @EndDate
		AND tcdt.DmSanPhamREF = @DmSanPhamREF 
		--IN (231, 238, 339, 240,370, 598,613)
		AND TrangThaiHopDong <> 3
	GROUP BY 
		tcdt.TenSanPham
		, tcdt.DmSanPhamREF
		, tcdt.SoHopDong
		, tcdt.HopDongID
) TCDT FULL OUTER JOIN 
(
	SELECT tc.TenSanPham 
		, tc.TypeProduct
		, tc.SoHopDong
		, ROUND(SUM(tc.TongViewThucChay)/1000,0) cpmchay	
		, ROUND(SUM(tc.TongClickThucChay),0) cpcchay	
	FROM ThucChay tc INNER JOIN HopDong hd ON tc.SoHopDong = hd.SoHopDong AND hd.TrangThaiHopDong <> 3 		
	WHERE 
		CONVERT(date, tc.NgayThucHien) BETWEEN @StartDate and @EndDate
		AND tc.TypeProduct = @TypeProduct
		--IN(5,8,9, 14,15)		
	GROUP BY tc.TenSanPham
		, tc.TypeProduct
		, tc.SoHopDong
) TC ON TC.SoHopDong = TCDT.SoHopDong AND TC.TypeProduct = TCDT.TypeProduct
WHERE
(TCDT.SoLuongCPM < TC.cpmchay AND TCDT.ThanhTien > TCDT.TienThucChay)
OR(TCDT.SoLuongCPC < TC.cpcchay AND TCDT.ThanhTien > TCDT.TienThucChay)
ORDER BY TCDT.HopDongID DESC 

	

END

```
