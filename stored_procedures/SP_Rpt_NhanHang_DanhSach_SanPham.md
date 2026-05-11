# Stored Procedure: `Rpt_NhanHang_DanhSach_SanPham`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-22 17:42:33.987000
- **Ngày sửa cuối**: 2014-11-19 12:16:53.507000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@LabelId` | `int(4)` | No |

## Definition (Source Code)

```sql
CREATE  PROC [dbo].[Rpt_NhanHang_DanhSach_SanPham]
(
	@StartDate DATETIME,
	@EndDate DATETIME,
	@LabelId INT	
)
AS
BEGIN
	DECLARE @Length INT
	SET @Length = 2
			
	DECLARE @TongDSKy2Dau FLOAT 
	SET @TongDSKy2Dau = (
	        SELECT SUM(DoanhSoKyHaiDau)
	        FROM   RptNhanHangSanPham
	        WHERE  DmNhanHangREF = @LabelId
	               AND NgayThucHien BETWEEN @StartDate AND @EndDate
	    )
	
	SELECT B.TenSanPham,
	       B.TyLeDoanhSo,
	       [dbo].[Rpt_GetDoanhSoThucChayByNhanAndHopDongSanPham](@LabelId, 0, B.DmSanPhamREF, @StartDate, @EndDate) 
	       DoanhSoThucChay,
	       (
           CASE 
                WHEN B.TongDoanhSo = 0 THEN 0
                WHEN ROUND(CONVERT(FLOAT,[dbo].[Rpt_GetDoanhSoThucChayByNhanAndHopDongSanPham](@LabelId, 0, B.DmSanPhamREF, @StartDate, @EndDate)) / CONVERT(FLOAT, B.TongDoanhSo) * 100, @Length) >100 THEN 100
                ELSE ROUND(CONVERT(FLOAT,[dbo].[Rpt_GetDoanhSoThucChayByNhanAndHopDongSanPham](@LabelId, 0, B.DmSanPhamREF, @StartDate, @EndDate)) / CONVERT(FLOAT, B.TongDoanhSo) * 100, @Length) 
                     --ROUND(CAST ((CONVERT(FLOAT,[dbo].[Rpt_GetDoanhSoThucChayByNhanAndHopDongSanPham](A.DmNhanHangREF,A.HopDongREF,A.DmSanPhamREF,@StartDate, @EndDate))/convert(float,A.DoanhSoKy2Dau) *100,AS decimal (6,0)),2)
           END
	       ) TyLeDSThucChay_DSKy2Dau
	FROM   (
	           SELECT a.TenSanPham,
	                  A.DmSanPhamREF,
	                  ROUND(
	                      CAST(
	                          (SUM(a.DoanhSoKyHaiDau) / @TongDSKy2Dau) * 100 AS DECIMAL(6, 2)
	                      ),
	                      2
	                  ) AS TyLeDoanhSo,
	                  SUM(a.DoanhSoKyHaiDau) TongDoanhSo
	                  --ROUND(CAST ((
	                  --	CASE WHEN SUM(a.DoanhSoKyHaiDau) = 0 THEN 0
	                  --	ELSE SUM(a.DoanhSoThucChay) / sum(a.DoanhSoKyHaiDau) * 100
	                  --	END) AS DECIMAL (6,0)),2) AS TyLeDSThucChay_DSKy2Dau
	           FROM   RptNhanHangSanPham a
	           WHERE  a.DmNhanHangREF = @LabelId
	                  AND CONVERT(DATE, a.NgayThucHien) BETWEEN @StartDate AND @EndDate
	           GROUP BY
	                  a.TenSanPham,
	                  A.DmSanPhamREF
	       )B
END

```
