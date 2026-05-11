# Stored Procedure: `ThucChay_CheckThucChayMobile`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-10-02 14:43:03.060000
- **Ngày sửa cuối**: 2014-11-19 12:24:52.693000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DonViTinh` | `nvarchar(100)` | No |
| `@IsKhuyenMai` | `int(4)` | No |
| `@NgayThucHien` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
--exec ThucChay_CheckThucChayMobile '-2',1,'2014-09-30'
CREATE PROCEDURE [dbo].[ThucChay_CheckThucChayMobile]
	-- Add the parameters for the stored procedure here
	@DonViTinh NVARCHAR(50), -- CPC, CPM, CPV, 
	                         -- -1: hop dong goi
	                         -- -2: hop dong co thuc chay 2013
	@IsKhuyenMai INT,
	@NgayThucHien DATETIME
AS
BEGIN
	-- SET NOCOUNT ON added to prevent extra result sets from
	-- interfering with SELECT statements.
	DECLARE @ProductUnit NVARCHAR(50)
	IF @DonViTinh IN ('CPC','CPM','CPV')
		BEGIN
			SELECT @ProductUnit = (CASE WHEN @DonViTinh = 'CPC' THEN 'CLICK'
									WHEN @DonViTinh = 'CPM' THEN 'VIEW'
									ELSE ''
							   END)		 
		 SELECT a.*,b.* ,(a.SoLuongTCSP - b.tong) Lech FROM 
			(
			  SELECT dbo.ThucChay_FormatSoHopDong(SoHopDong)SoHopDong, HopDongChiTietREF, tcmt.ProductUnitName, 
			  (CASE WHEN @DonViTinh = 'CPC' THEN SUM(TongClickThucChay)
					ELSE SUM(tcmt.TongViewThucChay) 
			  END) SoLuongTCSP
				FROM ThucChay tcmt  
			  WHERE tcmt.TypeProduct = 10 AND 
				    NgayThucHien    <= @NgayThucHien				    
					AND ProductUnitName  = @DonViTinh
					AND tcmt.HopDongChiTietREF IN (SELECT HopDongChiTietID FROM HopDongChiTiet hdct 
					                               WHERE tcmt.DmSanPhamREF = 342
												   AND hdct.IsKhuyenMai = @IsKhuyenMai AND hdct.DeletedStatus <> 1)
					 				
				GROUP BY dbo.ThucChay_FormatSoHopDong(SoHopDong),HopDongChiTietREF, tcmt.ProductUnitName
			)a 
		--FULL OUTER JOIN
		INNER JOIN
			( 
			  SELECT SoHopDong, HopDongChiTietREF, tcdtm.SoLuong, 
			  (CASE WHEN @IsKhuyenMai = 0 THEN SUM(SoLuongThucChay)
					ELSE SUM(tcdtm.SoLuongThucChayKM)
			   END) sltc,
			   (CASE WHEN @IsKhuyenMai = 0 THEN  sum(ISNULL(tcdtm.SoLuongThucChay,0) +ISNULL(tcdtm.SoLuongThucChayLechTreoHa,0))
					ELSE SUM(ISNULL(tcdtm.SoLuongThucChayKM,0) + ISNULL(tcdtm.SoLuongThucChayLechTreoHa,0))
			   END) tong
				FROM ThucChayDaTinhMobile tcdtm 
				WHERE tcdtm.NgayThucHien <= @NgayThucHien AND YEAR(tcdtm.NgayThucHien) = 2014
					AND tcdtm.DonViTinh   = @ProductUnit
					AND tcdtm.IsKhuyenMai = @IsKhuyenMai
				--	AND tcdtm.SoHopDong NOT IN (SELECT DISTINCT tcdtm.SoHopDong
				--FROM ThucChayDaTinhMobile tcdtm WHERE YEAR(tcdtm.NgayThucHien) = 2013)
				
				GROUP BY SoHopDong, tcdtm.HopDongChiTietREF, tcdtm.SoLuong
			 )b
		  ON (a.SoHopDong = b.SoHopDong AND 
			  a.HopDongChiTietREF = b.HopDongChiTietREF)			  
		  WHERE (a.SoLuongTCSP <> b.tong) OR (a.HopDongChiTietREF IS NULL) OR (b.HopDongChiTietREF IS NULL)
		 ORDER BY a.HopDongChiTietREF, b.HopDongChiTietREF
		END
	ELSE IF (@DonViTinh = '-1')
		BEGIN						
			SELECT a.*,b.* FROM (
			SELECT tcdtm.SoHopDong, tcdtm.HopDongChiTietREF,SUM(ISNULL(tcdtm.TongClickThucChay,0))TongClickThucChay
			  FROM ThucChay tcdtm 
			WHERE tcdtm.TypeProduct = 10  
				and tcdtm.HopDongChiTietREF IN (SELECT HopDongChiTietID
									  FROM HopDongChiTiet 
									  WHERE DmSanPhamREF = 342 AND DeletedStatus <> 1
										AND HopDongChiTiet.DonViTinh NOT IN ('CPC','CPM','CPV')) 
				and tcdtm.ProductUnitName ='CPC' 
				AND tcdtm.NgayThucHien <=@NgayThucHien		
			 GROUP BY tcdtm.SoHopDong, tcdtm.HopDongChiTietREF
			HAVING SUM(tcdtm.TongClickThucChay) > 0
			)a
			--FULL OUTER JOIN
			INNER JOIN
			(
			SELECT  tcdtm.SoHopDong, tcdtm.HopDongChiTietREF,SUM(ISNULL(tcdtm.TongClickThucChay,0))TongClickThucChay
			FROM ThucChayDaTinhMobile tcdtm 
			WHERE tcdtm.DonViTinh = 'CLICK'
			 AND tcdtm.NgayThucHien <= @NgayThucHien	
			 AND tcdtm.HopDongChiTietREF IN (SELECT HopDongChiTietID
									  FROM HopDongChiTiet 
									  WHERE DmSanPhamREF = 342 AND DeletedStatus <> 1
										AND HopDongChiTiet.DonViTinh NOT IN ('CPC','CPM','CPV'))
										
			 AND tcdtm.HopDongChiTietREF NOT IN (SELECT HopDongChiTietREF FROM ThucChayDaTinhMobile WHERE YEAR(NgayThucHien) = 2013)											
			GROUP BY SoHopDong,HopDongChiTietREF 
			)b
			ON (a.SoHopDong = b.SoHopDong AND
				a.HopDongChiTietREF = b.HopDongChiTietREF
			)
			WHERE (a.TongClickThucChay <> b.TongClickThucChay) OR (a.SoHopDong IS NULL) OR (b.SoHopDong IS NULL)
			ORDER BY a.HopDongChiTietREF		
		END
	ELSE IF (@DonViTinh = '-2')
		BEGIN
			SELECT TD.* FROM(
				SELECT a.SoHopDong shda, a.HopDongChiTietREF hdcta,b.SoHopDong shdb, b.HOpDongChiTietREF hdctb,
				ISNULL(a.tc*b.DonGiaTheoDonVi*(100-b.ChietKhau)/100,0) AS [TuTinh], 
				ISNULL((b.tt + b.lth),0) [tcdt]						
				FROM(			
				SELECT SoHopDong,tcmt.HopDongChiTietREF,tcmt.ProductUnitName,		
				(CASE WHEN tcmt.ProductUnitName = 'CPC' THEN SUM(tcmt.TongClickThucChay)		
				 ELSE SUM(tcmt.TongViewThucChay)								
				 END)tc								
					FROM ThucChay  tcmt	
					WHERE tcmt.HopDongChiTietREF IN (SELECT HopDongChiTietREF FROM ThucChayDaTinhMobile WHERE YEAR(NgayThucHien) = 2013)
					AND tcmt.TypeProduct = 10	
						AND tcmt.HopDongChiTietREF <> 0
						AND tcmt.NgayThucHien <=@NgayThucHien
					GROUP BY SoHopDong,tcmt.HopDongChiTietREF,tcmt.ProductUnitName	
				)a			
				--FULL OUTER JOIN	
				Inner join		
				(			
				SELECT tcdtm.SoHopDong,HOpDongChiTietREF,ThanhTien,tcdtm.DonGiaTheoDonVi,dongia, tcdtm.ChietKhau,			
				SUM(ISNULL(tcdtm.ThanhTienSauTrietKhauThucChay,0) + ISNULL(tcdtm.GiaTriThayDoi,0)) tt,			
				SUM(ISNULL(tcdtm.ThanhTienLechTreoHa,0)) lth			
				FROM ThucChayDaTinhMobile tcdtm			
				WHERE tcdtm.SoHopDong IN (SELECT SoHopDong FROM ThucChayDaTinhMobile WHERE YEAR(NgayThucHien) = 2013)			
				AND tcdtm.HopDongChiTietREF <> 0			
			
				AND tcdtm.NgayThucHien <=@NgayThucHien		
				AND YEAR(tcdtm.NgayThucHien) = 2014			
				GROUP BY tcdtm.SoHopDong,HOpDongChiTietREF,ThanhTien,tcdtm.DonGiaTheoDonVi, dongia,tcdtm.ChietKhau
				)b			
				ON (a.SoHopDong = b.SoHopDong AND			
					a.HopDongChiTietREF = b.HOpDongChiTietREF)				
					)TD where TD.TuTinh <> TD.tcdt
			ORDER BY TD.hdcta
		END
		
END

```
