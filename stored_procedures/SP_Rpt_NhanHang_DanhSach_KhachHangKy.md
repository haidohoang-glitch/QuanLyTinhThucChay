# Stored Procedure: `Rpt_NhanHang_DanhSach_KhachHangKy`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2014-04-22 17:42:33.283000
- **Ngày sửa cuối**: 2014-11-19 12:16:53.523000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@LabelId` | `int(4)` | No |

## Definition (Source Code)

```sql
-- [Rpt_NhanHang_DanhSach_KhachHangKy] '2013-01-01', '2014-01-16', 1281
CREATE  PROC [dbo].[Rpt_NhanHang_DanhSach_KhachHangKy]
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
	SET @TongDSKy2Dau = (SELECT SUM(DoanhSoKyHaiDau) FROM RptNhanHangKhachHangKy WHERE DmNhanHangREF = @LabelId AND NgayThucHien BETWEEN @StartDate AND @EndDate)

	SELECT C.TenKhachHang, C.HinhThucKy, TyLeDoanhSo,
	[dbo].[Rpt_GetDoanhSoThucChayByNhanHangAndKhachHangKy](@LabelId, C.DmKhachHangREF, @StartDate, @EndDate) DoanhSoThucChay,
	C.TongDoanhSoKyHaiDau,
	(
		CASE WHEN C.TongDoanhSoKyHaiDau = 0 THEN 0
			 WHEN ROUND((CONVERT(FLOAT,[dbo].[Rpt_GetDoanhSoThucChayByNhanHangAndKhachHangKy](@LabelId,	C.DmKhachHangREF,@StartDate, @EndDate)) / CONVERT(FLOAT,C.TongDoanhSoKyHaiDau)) * 100, @Length) >100 THEN 100
		ELSE ROUND((CONVERT(FLOAT,[dbo].[Rpt_GetDoanhSoThucChayByNhanHangAndKhachHangKy](@LabelId,	C.DmKhachHangREF,@StartDate, @EndDate)) / CONVERT(FLOAT,C.TongDoanhSoKyHaiDau)) * 100 , @Length)
		END
	) TyLeDSThucChay_DSKy2Dau
	FROM
	(
		SELECT a.TenKhachHang,a.DmKhachHangREF,
		(
			CASE WHEN  b.Loai = 3 THEN N'Ð?i lý'
			ELSE N'Tr?c ti?p'
			END
		) AS HinhThucKy, 
		
			ROUND((CONVERT(FLOAT, SUM(a.DoanhSoKyHaiDau)) / CONVERT(FLOAT, @TongDSKy2Dau)) * 100 , @Length) AS TyLeDoanhSo,
			SUM(a.DoanhSoKyHaiDau) TongDoanhSoKyHaiDau,
			(
				CASE WHEN SUM(a.DoanhSoKyHaiDau) = 0 THEN 0
				ELSE round(CONVERT(FLOAT, SUM(a.DoanhSoThucChay)) / CONVERT(FLOAT, SUM(a.DoanhSoKyHaiDau)), @Length) * 100
				END
			) TyLeDSThucChay_DSKy2Dau 
		FROM RptNhanHangKhachHangKy a JOIN KhachHangFull b 
		ON a.DmKhachHangREF = b.KhachHangID 
		WHERE a.DmNhanHangREF = @LabelId AND CONVERT(DATE, a.NgayThucHien) BETWEEN @StartDate AND @EndDate
		GROUP BY a.TenKhachHang, a.DmKhachHangREF, b.Loai
	) C
END
--exec [dbo].[Rpt_NhanHang_DanhSach_KhachHangKy]'2013-01-01', '2013-12-31', 777

```
