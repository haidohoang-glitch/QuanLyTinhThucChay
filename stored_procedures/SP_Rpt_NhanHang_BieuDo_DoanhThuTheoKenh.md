# Stored Procedure: `Rpt_NhanHang_BieuDo_DoanhThuTheoKenh`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-22 17:42:30.533000
- **Ngày sửa cuối**: 2014-11-19 12:16:44.670000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@LabelId` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE  PROC [dbo].[Rpt_NhanHang_BieuDo_DoanhThuTheoKenh]
(
	@StartDate	DATETIME,
	@EndDate	DATETIME,
	@LabelId	INT		
)
AS
BEGIN		
	DECLARE @Length INT
	SET @Length = 2
		
    -- Tong Doanh s? ký hai d?u
	DECLARE @TongDoanhSoKyHaiDau BIGINT		
	SET @TongDoanhSoKyHaiDau = (
		SELECT SUM(DoanhSoKyHaiDau) FROM RptNhanHangKenh
		WHERE DmNhanHangREF = @LabelId AND CONVERT(Date, NgayThucHien) BETWEEN @StartDate AND @EndDate)
	SET @TongDoanhSoKyHaiDau = ISNULL(@TongDoanhSoKyHaiDau, 0)	
	
	SELECT CONVERT(NVARCHAR(10), TiLeDoanhSo) +  '% ' + TenKenh AS TenKenh, DoanhSoKyHaiDau FROM (
		SELECT TenKenh, SUM(DoanhSoKyHaiDau) DoanhSoKyHaiDau, 
		(
			CASE WHEN  SUM(DoanhSoKyHaiDau) = 0 THEN 0
				WHEN ROUND(CONVERT(FLOAT ,SUM(DoanhSoKyHaiDau) / CONVERT(FLOAT, @TongDoanhSoKyHaiDau)) * 100, @Length) > 100 THEN 100
				ELSE  ROUND(CONVERT(FLOAT, SUM(DoanhSoKyHaiDau) / CONVERT(FLOAT, @TongDoanhSoKyHaiDau)) * 100, @Length)
			END
		) AS TiLeDoanhSo
		FROM RptNhanHangKenh
		WHERE DmNhanHangREF = @LabelId AND CONVERT(Date, NgayThucHien) BETWEEN @StartDate AND @EndDate
		GROUP BY TenKenh		
	) AS temp
	WHERE TiLeDoanhSo > 0	
END

```
