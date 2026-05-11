# Function: `GetListHopDongCheck`

- **Loại**: SQL_TABLE_VALUED_FUNCTION
- **Ngày tạo**: 2014-09-23 11:01:07
- **Ngày sửa cuối**: 2014-12-11 11:52:03.237000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--SELECT * FROM dbo.GetListHopDongCheck ('2014-09-21')
 
CREATE FUNCTION [dbo].[GetListHopDongCheck]
(
	@NgayThucHien DATETIME
)
RETURNS 
@ListHopDong TABLE 
(
	HopDongREF INT,
	HopDongChiTietREF int
)
AS
BEGIN
		INSERT INTO @ListHopDong
		SELECT 
		A.HopDongID
		, A.HopDongChiTietREF		
		FROM (
			----Get list hop dong CPD, TMDT phat sinh thuc chay 2014
			SELECT tcdt.HopDongID
				, tcdt.SoHopDong
				, tcdt.HopDongChiTietREF
				, MAX(tcdt.NgayThucHien) NgayThucHienMax
				, tcdt.DmSanPhamREF
				, tcdt.DmHinhThucQuangCao
				, ROUND(SUM(tcdt.ThanhTienSauTrietKhauThucChay + tcdt.GiaTriThayDoi),0) thanhtientc 
			FROM ThucChayDaTinh tcdt	
			WHERE 
				tcdt.DmSanPhamREF IN (140,228, 370, 241, 564, 549, 385, 
													264,300,268,248,270,243,244,249)-- SP TMÐT
				AND [dbo].[CheckDonViTinhHinhThucCPDAndNotCPD](0, tcdt.DonViTinh) = 1		
				AND tcdt.TrangThaiHopDong <> 3
			GROUP BY tcdt.HopDongID
				, tcdt.SoHopDong
				, tcdt.HopDongChiTietREF
				, tcdt.DmSanPhamREF
				, tcdt.DmHinhThucQuangCao
		)A LEFT JOIN (
			
			SELECT hd.HopDongID
				, hdct.HopDongChiTietID
				, tchdct.DmSanPhamREF
				, tchdct.DmHinhThucQuangCaoREF,
				CASE
				WHEN hd.TrangThaiHopDong = 3 THEN 0
				ELSE hdct.ThanhTien 
				END ThanhTien				
				, MAX(tchdct.ThoiGianKetThuc) AS ThoiGianKetThuc				
			FROM ThucChayHopDongChiTiet tchdct
				RIGHT JOIN HopDongChiTiet hdct ON tchdct.HopDongChiTietREF = hdct.HopDongChiTietID
				INNER JOIN HopDong hd ON hd.HopDongID = hdct.HopDongFK 
			WHERE		
				hdct.DmSanPhamREF IN (140, 370, 241, 564, 549, 385, 228,
										264,300,268,248,270,243,244,249)-- SP TMÐT 
				AND hd.TrangThaiHopDong <> 3	
				AND YEAR(hd.NgayDanhSoHopDong) >=2013
			GROUP BY 
				hd.HopDongID
				, hdct.HopDongChiTietID
				, hdct.ThanhTien
				, hd.TrangThaiHopDong
				, tchdct.DmSanPhamREF
				, tchdct.DmHinhThucQuangCaoREF
		)B
		ON a.HopDongID = b.HopDongID 
			AND a.HopDongChiTietREF = b.HopDongChiTietID 
			 
		WHERE 
		(			
			A.thanhtientc <> B.ThanhTien
		)
			AND YEAR(A.NgayThucHienMax) = 2014 
		ORDER BY A.HopDongID, A.HopDongChiTietREF	
	RETURN 
END

```
