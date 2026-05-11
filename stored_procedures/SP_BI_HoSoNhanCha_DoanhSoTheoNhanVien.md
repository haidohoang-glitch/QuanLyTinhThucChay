# Stored Procedure: `BI_HoSoNhanCha_DoanhSoTheoNhanVien`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-25 16:17:13.880000
- **Ngày sửa cuối**: 2015-06-25 16:17:13.880000

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

--EXEC [dbo].[BI_HoSoNhanCha_DoanhSoTheoNhanVien] 2905,'2014-01-01','2015-04-24'

CREATE  PROCEDURE [dbo].[BI_HoSoNhanCha_DoanhSoTheoNhanVien] 
( 
	@DmNhanHangChaID INT,
	@FromDate DATETIME,
	@ToDate DATETIME
)
AS
BEGIN
	DECLARE @TongDoanhSo BIGINT, @TongDoanhSoTop BIGINT, @VitriTop INT
	SET @VitriTop = 10
	SET @TongDoanhSo = 
	(
		SELECT SUM(nh.DoanhSoHaiDau) 
		FROM HoSoNhan_DoanhSoChiTiet nh 
		WHERE nh.NhanHangGocID = @DmNhanHangChaID
	)
	
	SET @TongDoanhSo = ISNULL(@TongDoanhSo,1)
	
	SET @TongDoanhSoTop =
		(
			SELECT SUM(A.DoanhSoKyHaiDau) FROM
			(
				SELECT TOP 10 A.DoanhSoKyHaiDau
				FROM 
				(
					SELECT rnhns.DmNhanSuREF,rnhns.TenNhanSu
					,SUM(rnhns.DoanhSoKyHaiDau)*1.1 DoanhSoKyHaiDau 
					FROM RptNhanHangNhanSu rnhns
					WHERE rnhns.DmNhanHangREF IN 
					( SELECT DISTINCT nh.DmNhanHangID FROM HoSoNhan_DoanhSoChiTiet nh WHERE nh.NhanHangGocID = @DmNhanHangChaID)
					AND CONVERT(date,rnhns.NgayThucHien) BETWEEN @FromDate AND @ToDate
					GROUP BY rnhns.DmNhanSuREF,rnhns.TenNhanSu
				)A
				ORDER BY A.DoanhSoKyHaiDau DESC
			)A
		)
		
		SELECT * FROM 
		(
			SELECT A.* FROM
			(
				SELECT TOP 10 A.*
				, (CONVERT(NVARCHAR(100),A.Tile_DS2Dau_TongDs) + '%' + ' ' + A.TenNhanSu) TenTile 
				FROM
				(
					SELECT A.DmNhanSuREF, A.TenNhanSu
					, A.DoanhSoKyHaiDau
					, Round(CONVERT(FLOAT,A.DoanhSoKyHaiDau)/CONVERT(FLOAT,@TongDoanhSo)*100,3,3) Tile_DS2Dau_TongDs 
					FROM 
					(
						SELECT rnhns.DmNhanSuREF,rnhns.TenNhanSu
						,SUM(rnhns.DoanhSoKyHaiDau)*1.1 DoanhSoKyHaiDau 
						FROM RptNhanHangNhanSu rnhns
						WHERE rnhns.DmNhanHangREF IN 
						( SELECT DISTINCT nh.DmNhanHangID FROM HoSoNhan_DoanhSoChiTiet nh WHERE nh.NhanHangGocID = @DmNhanHangChaID)
						AND CONVERT(date,rnhns.NgayThucHien) BETWEEN @FromDate AND @ToDate
						GROUP BY rnhns.DmNhanSuREF,rnhns.TenNhanSu
					)A
				)A
				ORDER BY A.DoanhSoKyHaiDau DESC
			)A
			
			UNION
			(
				SELECT A.*
				,(CONVERT(NVARCHAR(100),A.Tile_DS2Dau_TongDs) + '%' + ' ' + A.TenNhanSu) TenTile  
				FROM
				(
				SELECT 0 DmNhanSuREF, 'Other' TenNhanSu
				, (@TongDoanhSo - @TongDoanhSoTop)DoanhSoKyHaiDau
				, Round(CONVERT(FLOAT,(@TongDoanhSo - @TongDoanhSoTop))/CONVERT(FLOAT,@TongDoanhSo)*100,3,3) Tile_DS2Dau_TongDs
				)A
			)
		)A
		WHERE (A.Tile_DS2Dau_TongDs <> 0 AND A.Tile_DS2Dau_TongDs <> -0)
		ORDER BY A.Tile_DS2Dau_TongDs DESC
	
END

--EXEC [dbo].[BI_HoSoNhanCha_DoanhSoTheoNhanVien] 4152,'2015-01-01','2014-01-01'

```
