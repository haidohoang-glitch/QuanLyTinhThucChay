# Stored Procedure: `BI_HoSoNhanCha_DoanhSoThucChayTheoWebsite`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-25 16:17:15.667000
- **Ngày sửa cuối**: 2015-06-25 16:17:15.667000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@DmNhanHangChaID` | `int(4)` | No |
| `@FromDate` | `datetime(8)` | No |
| `@ToDate` | `datetime(8)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================

--EXEC [dbo].[BI_HoSoNhanCha_DoanhSoThucChayTheoWebsite] 1523,'2014-01-01','2015-01-01'

CREATE  PROCEDURE [dbo].[BI_HoSoNhanCha_DoanhSoThucChayTheoWebsite] 
( 
	@DmNhanHangChaID INT,
	@FromDate DATETIME,
	@ToDate DATETIME
)
AS
BEGIN
	DECLARE @TongDoanhSoThucChay BIGINT, @TongDoanhSoTop BIGINT
	SET @TongDoanhSoThucChay = 
	(
		SELECT SUM(nh.ThucChay) 
		FROM HoSoNhan_DoanhSoChiTiet nh 
		WHERE nh.NhanHangGocID = @DmNhanHangChaID
	)
	SET @TongDoanhSoThucChay = ISNULL(@TongDoanhSoThucChay,1)
	
	SET @TongDoanhSoTop = 
	(
		SELECT SUM(A.DoanhSoThucChay) FROM 
		(
			SELECT TOP 10 A.DoanhSoThucChay
			FROM
			(
				SELECT A.DoanhSoThucChay
				FROM
				(
					SELECT TC.Website, SUM(ISNULL(TC.DoanhSoThucChay, 0))*1.1  DoanhSoThucChay
				FROM   
				(
					SELECT rnhttct.DoanhSoThucChay,
						(
							-- Doi voi cac san pham CPM 
							CASE 					
							   WHEN ISNULL(hdct.DmSanPhamREF,0) NOT IN (140,228,564,549,141) THEN 
									ISNULL(hdct.TenNhomWebsite,'Blank')
							   ELSE ISNULL(hdct.TenWebsite,'Blank')
							END
						) AS Website
					FROM RptNhanHangThucChayFull rnhttct
					INNER JOIN 
					(
						SELECT distinct hdct.* FROM RptNhanHangThongTinChiTiet hd INNER JOIN HopDongChiTiet hdct ON hd.HopDongREF = hdct.HopDongFK
						WHERE hd.NgayThucHien BETWEEN @FromDate AND @ToDate
					)hdct
					ON  hdct.HopDongChiTietID = rnhttct.HopDongChiTietREF AND hdct.DmSanPhamREF = rnhttct.DmSanPhamREF 	           
					WHERE rnhttct.DmNhanHangREF IN( SELECT DISTINCT nh.DmNhanHangID FROM HoSoNhan_DoanhSoChiTiet nh WHERE nh.NhanHangGocID = @DmNhanHangChaID) 
					AND CONVERT(Date, rnhttct.NgayThucHien) BETWEEN @FromDate AND @ToDate
					AND hdct.DeletedStatus = 0
				) TC
				GROUP BY  TC.Website
				)A
			)A
			ORDER BY A.DoanhSoThucChay DESC	
		)A
	)
	
	SELECT * FROM
	(
		SELECT A.* FROM
		(
			SELECT TOP 10 A.*
			, (CONVERT(nvarchar(100),A.Tile_DsTC_TongTC) + '%' + ' ' + A.Website) TenTile 
			FROM
			(
				SELECT A.Website
				, A.DoanhSoThucChay
				, round(CONVERT(FLOAT,A.DoanhSoThucChay)/CONVERT(FLOAT,@TongDoanhSoThucChay)*100,3,3) Tile_DsTC_TongTC 
				FROM
				(
					SELECT TC.Website, SUM(ISNULL(TC.DoanhSoThucChay, 0))*1.1  DoanhSoThucChay
				FROM   
				(
					SELECT rnhttct.DoanhSoThucChay,
						(
							-- Doi voi cac san pham CPM 
							CASE 					
							   WHEN ISNULL(hdct.DmSanPhamREF,0) NOT IN (140,228,564,549,141) THEN 
									ISNULL(hdct.TenNhomWebsite,'Blank')
							   ELSE ISNULL(hdct.TenWebsite,'Blank')
							END
						) AS Website
					FROM RptNhanHangThucChayFull rnhttct
					INNER JOIN 
					(
						SELECT distinct hdct.* FROM RptNhanHangThongTinChiTiet hd INNER JOIN HopDongChiTiet hdct ON hd.HopDongREF = hdct.HopDongFK
						WHERE hd.NgayThucHien BETWEEN @FromDate AND @ToDate
					)hdct
					ON  hdct.HopDongChiTietID = rnhttct.HopDongChiTietREF AND hdct.DmSanPhamREF = rnhttct.DmSanPhamREF 	           
					WHERE rnhttct.DmNhanHangREF IN( SELECT DISTINCT nh.DmNhanHangID FROM HoSoNhan_DoanhSoChiTiet nh WHERE nh.NhanHangGocID = @DmNhanHangChaID) 
					AND CONVERT(Date, rnhttct.NgayThucHien) BETWEEN @FromDate AND @ToDate
					AND hdct.DeletedStatus = 0
				) TC
				GROUP BY  TC.Website
				)A
			)A
			ORDER BY A.DoanhSoThucChay DESC
		)A
		UNION
		SELECT A.*
		, (CONVERT(nvarchar(100),A.Tile_DsTC_TongTC) + '%' + ' ' + A.Website) TenTile 
		FROM
		(
			SELECT 'Other' Website, (@TongDoanhSoThucChay - @TongDoanhSoTop)DoanhSoThucChay
			, round(CONVERT(FLOAT,(@TongDoanhSoThucChay - @TongDoanhSoTop))/CONVERT(FLOAT,@TongDoanhSoThucChay)*100,3,3) Tile_DsTC_TongTC
		)A
	)A
	WHERE (A.Tile_DsTC_TongTC <> 0 AND A.Tile_DsTC_TongTC <> -0)
	ORDER BY A.DoanhSoThucChay DESC
END

--EXEC [dbo].[BI_HoSoNhanCha_DoanhSoThucChayTheoWebsite] 4152,'2015-01-01','2014-01-01'

```
