# Stored Procedure: `Rpt_NhanHang_BieuDo_DoanhThuTheoThucChay`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-22 17:42:30.280000
- **Ngày sửa cuối**: 2014-11-19 12:16:56.320000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@LabelId` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE  PROCEDURE [dbo].[Rpt_NhanHang_BieuDo_DoanhThuTheoThucChay] 
	@StartDate DATETIME,
	@EndDate DATETIME,
	@LabelId INT
AS
BEGIN
	DECLARE @Length INT
	SET @Length = 2
		
    -- Tong Doanh s? Th?c ch?y
	DECLARE @TongDoanhSoThucChay BIGINT		
	SET @TongDoanhSoThucChay = (
		SELECT SUM(DoanhSoThucChay) FROM dbo.RptNhanHangThucChayFull
		WHERE DmNhanHangREF = @LabelId AND CONVERT(Date, NgayThucHien) BETWEEN @StartDate AND @EndDate)
	SET @TongDoanhSoThucChay = ISNULL(@TongDoanhSoThucChay, 0)	
	
	SELECT CONVERT(NVARCHAR(10), TiLeDoanhSo) +  '% ' + Website AS Website, DoanhSoThucChay FROM (
		SELECT Website, SUM(ISNULL(TC.DoanhSoThucChay, 0)) DoanhSoThucChay,
		(
			CASE WHEN  SUM(DoanhSoThucChay) = 0 THEN 0
				WHEN ROUND(CONVERT(FLOAT, SUM(DoanhSoThucChay) / CONVERT(FLOAT,@TongDoanhSoThucChay)) * 100, @Length) > 100 THEN 100
				ELSE  ROUND(CONVERT(FLOAT, SUM(DoanhSoThucChay) / CONVERT(FLOAT,@TongDoanhSoThucChay)) * 100, @Length)
			END
		) AS TiLeDoanhSo 	
		FROM   
		(
			SELECT rnhttct.DoanhSoThucChay,
				(
					-- Doi voi cac san pham CPM 
					CASE 					
					   WHEN hdct.DmSanPhamREF IN (231, 238, 339, 342, 337, 240, 370) THEN 
							hdct.TenNhomWebsite
					   ELSE hdct.TenWebsite
					END
				) AS Website
			FROM RptNhanHangThucChayFull rnhttct
			INNER JOIN HopDongChiTiet hdct
			ON  hdct.HopDongChiTietID = rnhttct.HopDongChiTietREF	           
			WHERE DmNhanHangREF = @LabelId AND CONVERT(Date, rnhttct.NgayThucHien) BETWEEN @StartDate AND @EndDate
			AND hdct.DeletedStatus = 0
		) TC
		GROUP BY Website		
	) AS temp
	WHERE TiLeDoanhSo > 0	
END

```
