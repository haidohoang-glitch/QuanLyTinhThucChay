# Stored Procedure: `BI_HoSoNhanCha_DoanhSoHaiDauTheoKenh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-25 16:17:14.060000
- **Ngày sửa cuối**: 2015-06-25 16:17:14.060000

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

--EXEC [dbo].[BI_HoSoNhanCha_DoanhSoHaiDauTheoKenh] 1523,'2014-01-01','2015-01-01'

CREATE  PROCEDURE [dbo].[BI_HoSoNhanCha_DoanhSoHaiDauTheoKenh] 
( 
	@DmNhanHangChaID INT,
	@FromDate DATETIME,
	@ToDate DATETIME
)
AS
BEGIN
	DECLARE @TongDoanhSoHaiDau BIGINT, @TongDoanhSoTop BIGINT
	SET @TongDoanhSoHaiDau = 
	(
		SELECT SUM(nh.DoanhSoHaiDau) 
		FROM HoSoNhan_DoanhSoChiTiet nh 
		WHERE nh.NhanHangGocID = @DmNhanHangChaID
	)
	SET @TongDoanhSoHaiDau = ISNULL(@TongDoanhSoHaiDau,1)
	
	SET @TongDoanhSoTop = 
	(
		SELECT SUM(a.DoanhSoKyHaiDau) FROM
		(
			SELECT TOP 10  A.DoanhSoKyHaiDau
			FROM
			(
				SELECT A.DoanhSoKyHaiDau
				FROM
				(
					SELECT rnhk.DmKenhREF, rnhk.TenKenh, SUM(rnhk.DoanhSoKyHaiDau)*1.1 DoanhSoKyHaiDau
					FROM RptNhanHangKenh rnhk
					WHERE rnhk.DmNhanHangREF IN 
					( SELECT DISTINCT nh.DmNhanHangID FROM HoSoNhan_DoanhSoChiTiet nh WHERE nh.NhanHangGocID = @DmNhanHangChaID)
					AND CONVERT(Date, rnhk.NgayThucHien) BETWEEN @FromDate AND @ToDate
					GROUP BY rnhk.DmKenhREF, rnhk.TenKenh
				)A
			)A
			ORDER BY A.DoanhSoKyHaiDau DESC	
		)A
	)
	SELECT * FROM 
	(
		SELECT A.* FROM
		(
			SELECT TOP 10 A.*
			,(Convert(nvarchar(100),A.Tile_DS2Dau_TongDS) + '%' + ' ' + A.TenKenh) TenTiLe  
			FROM
			(
				SELECT A.DmKenhREF
				, A.TenKenh
				, A.DoanhSoKyHaiDau
				, Round(CONVERT(FLOAT,A.DoanhSoKyHaiDau)/CONVERT(FLOAT,@TongDoanhSoHaiDau)*100,3,3) Tile_DS2Dau_TongDS  
				FROM
				(
					SELECT rnhk.DmKenhREF, rnhk.TenKenh, SUM(rnhk.DoanhSoKyHaiDau)*1.1 DoanhSoKyHaiDau
					FROM RptNhanHangKenh rnhk
					WHERE rnhk.DmNhanHangREF IN 
					( SELECT DISTINCT nh.DmNhanHangID FROM HoSoNhan_DoanhSoChiTiet nh WHERE nh.NhanHangGocID = @DmNhanHangChaID)
					AND CONVERT(Date, rnhk.NgayThucHien) BETWEEN @FromDate AND @ToDate
					GROUP BY rnhk.DmKenhREF, rnhk.TenKenh
				)A
			)A
			ORDER BY A.DoanhSoKyHaiDau DESC
		)A
		UNION
		SELECT A.*
		, (Convert(nvarchar(100),A.Tile_DS2Dau_TongDS) + '%' + ' ' + A.TenKenh) TenTiLe   FROM
		(
			SELECT 0 DmKenhREF, 'Other' TenKenh, (@TongDoanhSoHaiDau - @TongDoanhSoTop)  DoanhSoKyHaiDau
			, Round(CONVERT(FLOAT,(@TongDoanhSoHaiDau - @TongDoanhSoTop))/CONVERT(FLOAT,@TongDoanhSoHaiDau)*100,3,3) Tile_DS2Dau_TongDS
		)A
	)A
	WHERE (A.Tile_DS2Dau_TongDS <> 0 AND A.Tile_DS2Dau_TongDS <> -0)
	ORDER BY A.DoanhSoKyHaiDau DESC	
END

--EXEC [dbo].[BI_HoSoNhanCha_DoanhSoThucChayTheoWebsite] 4152,'2015-01-01','2014-01-01'

```
