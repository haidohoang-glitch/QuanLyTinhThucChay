# Stored Procedure: `BI_HoSoNhanCha_TiLeDoanhSoCacNhanHang`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-25 16:17:15.600000
- **Ngày sửa cuối**: 2015-06-25 16:17:15.600000

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

--EXEC BI_HoSoNhanCha_TiLeDoanhSoCacNhanHang 41812,'2015-01-01','2015-04-21'

CREATE PROCEDURE [dbo].[BI_HoSoNhanCha_TiLeDoanhSoCacNhanHang] 
(@DmNhanHangChaID INT, @FromDate DATETIME, @ToDate DATETIME)
AS
BEGIN
	DECLARE @TongDoanhSo BIGINT
	SET @TongDoanhSo = (
		SELECT SUM(nh.DoanhSoHaiDau) 
		FROM HoSoNhan_DoanhSoChiTiet nh 
		WHERE nh.NhanHangGocID = @DmNhanHangChaID
	)
	SET @TongDoanhSo = ISNULL(@TongDoanhSo,1)
	
	SELECT A.*
	, (CONVERT(NVARCHAR(100),A.Tile_Ds2Dau_TongDs) + '%' + ' ' + A.TenNhanHang) TenTile 
	FROM
	(
		SELECT A.DmNhanHangID, A.TenNhanHang
		, A.DoanhSoHaiDau
		, Round(CONVERT(FLOAT,A.DoanhSoHaiDau)/CONVERT(FLOAT,@TongDoanhSo)*100,3,3) Tile_Ds2Dau_TongDs  
		FROM
		(
			SELECT DISTINCT
				   DmNhanHangID,
				   TenNhanHang,
				   [dbo].[fn_GetDmNganhHangIDGoc](DmNhanHangID, @DmNhanHangChaID, Levels, @FromDate, @ToDate) AS DoanhSoHaiDau
			FROM   [dbo].[HoSoNhan_DoanhSoChiTiet]
			WHERE  NhanHangGocID = @DmNhanHangChaID
				   AND levels <  = 1
		)A
		WHERE A.DoanhSoHaiDau <>0
	)A  
	ORDER BY A.DoanhSoHaiDau DESC  
END

--EXEC [dbo].[BI_HoSoNhanCha_TiLeDoanhSoCacNhanHang] 4152,'2015-01-01','2014-01-01'

```
