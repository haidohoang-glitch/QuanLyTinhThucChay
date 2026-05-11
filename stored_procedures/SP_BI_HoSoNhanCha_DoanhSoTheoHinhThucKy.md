# Stored Procedure: `BI_HoSoNhanCha_DoanhSoTheoHinhThucKy`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-25 16:17:14
- **Ngày sửa cuối**: 2015-06-25 16:17:14

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

--EXEC [dbo].[BI_HoSoNhanCha_DoanhSoTheoHinhThucKy] 1523,'2014-01-01','2015-01-01'

CREATE  PROCEDURE [dbo].[BI_HoSoNhanCha_DoanhSoTheoHinhThucKy] 
( 
	@DmNhanHangChaID INT,
	@FromDate DATETIME,
	@ToDate DATETIME
)
AS
BEGIN
	DECLARE @TongDoanhSo BIGINT
	
	--SELECT * FROM HoSoNhan_DoanhSoChiTiet
	SET @TongDoanhSo = 
	(
		SELECT SUM(nh.DoanhSoHaiDau) 
		FROM HoSoNhan_DoanhSoChiTiet nh 
		WHERE nh.NhanHangGocID = @DmNhanHangChaID
	)
	SET @TongDoanhSo = ISNULL(@TongDoanhSo,1)
	 
	--PRINT @TongDoanhSo
	SELECT A.*
	, (CONVERT(NVARCHAR(100),A.TiLe_DS2Dau_DsTong) + '%' + ' ' + A.HinhThucKy) TenTile 
	FROM 
	(
		SELECT 
		--A.HinhThucKyID, 
		A.HinhThucKy
		, A.DoanhSoKyHaiDau
		, round(CONVERT(FLOAT,A.DoanhSoKyHaiDau)/CONVERT(FLOAT,@TongDoanhSo)*100,3,3) TiLe_DS2Dau_DsTong 
		FROM 
		(	
			SELECT rnhhtk.HinhThucKyID, rnhhtk.HinhThucKy
			, SUM(rnhhtk.DoanhSoKyHaiDau)*1.1 DoanhSoKyHaiDau 
			FROM RptNhanHangHinhThucKy rnhhtk
			WHERE rnhhtk.DmNhanHangREF  IN
			( SELECT DISTINCT nh.DmNhanHangID FROM HoSoNhan_DoanhSoChiTiet nh WHERE nh.NhanHangGocID = @DmNhanHangChaID)
			AND CONVERT(date,rnhhtk.NgayThucHien) BETWEEN @FromDate AND @ToDate
			GROUP BY rnhhtk.HinhThucKyID, rnhhtk.HinhThucKy
		)A
	)A
	ORDER BY A.DoanhSoKyHaiDau	
END

--EXEC [dbo].[BI_HoSoNhanCha_DoanhSoTheoHinhThucKy] 4152,'2015-01-01','2014-01-01'

```
