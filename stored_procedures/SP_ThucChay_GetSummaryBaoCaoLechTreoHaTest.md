# Stored Procedure: `ThucChay_GetSummaryBaoCaoLechTreoHaTest`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-10 14:24:01.767000
- **Ngày sửa cuối**: 2014-11-19 12:16:57.313000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@PageIndex` | `int(4)` | No |
| `@RecordCount` | `int(4)` | No |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@ListDmSanPhamREF` | `nvarchar(400)` | No |
| `@ListSoHopDong` | `nvarchar(4000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-08-06
-- Description:	Lay thong tin thuc chay lech treo ha group theo nhom san pham
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_GetSummaryBaoCaoLechTreoHaTest]
	@PageIndex INT,
	@RecordCount INT,
	@StartDate DATETIME,
	@EndDate DATETIME,
	@ListDmSanPhamREF NVARCHAR(200),
	@ListSoHopDong NVARCHAR(2000),
	@TenDangNhap NVARCHAR(50)
AS
BEGIN
	DECLARE @Sql NVARCHAR(4000)
	DECLARE @DauNhay NVARCHAR(50)
	DECLARE @FillterBySanPham NVARCHAR(200)
	
	SET @DauNhay = ''''
	SET @FillterBySanPham =''
	
	--PRINT @ListDmSanPhamREF
	
	IF @ListDmSanPhamREF <> '' 
		SET @FillterBySanPham = 'AND T.DmSanPhamREF IN (' + CONVERT(NVARCHAR,@ListDmSanPhamREF) + ')'
	
	
	SET @Sql = '
		SELECT TOP (' + CONVERT(NVARCHAR,@RecordCount) + ')
			T.DmSanPhamREF
			,T.TenSanPham
			,T.TongViewHopDong
			,T.TongViewThucChay
			,T.TongViewLechTreoHa
			,T.ThanhTienThucChay
			,T.ThanhTienLechTreoHa
		FROM
		(
			SELECT 
				T2.DmSanPhamREF, T2.TenSanPham,
				SUM(TongViewHopDong) TongViewHopDong,
				SUM(TongViewThucChay) TongViewThucChay,
				SUM(TongViewLechTreoHa) TongViewLechTreoHa,
				SUM(ThanhTienThucChay) ThanhTienThucChay,
				SUM(ThanhTienLechTreoHa) ThanhTienLechTreoHa,
				ROW_NUMBER() OVER (ORDER BY T2.TenSanPham) AS num
			FROM
			(
				SELECT 
					T1.DmSanPhamREF
					,T1.TenSanPham
					,MAX(T1.TongViewHopDong) AS TongViewHopDong
					,SUM(T1.TongViewThucChay) AS TongViewThucChay
					,SUM(T1.TongViewLechTreoHa) AS TongViewLechTreoHa
					,ROUND(SUM(T1.ThanhTienThucChay),0) AS ThanhTienThucChay
					,ROUND(SUM(T1.ThanhTienLechTreoHa),0) AS ThanhTienLechTreoHa
				FROM
				(' 
					+ dbo.ThucChay_GenSQLCommandSummaryBaoCaoLechTreoHa(@StartDate,@EndDate,@ListDmSanPhamREF,@ListSoHopDong, @TenDangNhap) + 
				') T1 
				GROUP BY T1.TenSanPham,T1.DmSanPhamREF 
			)T2
			GROUP BY T2.TenSanPham,T2.DmSanPhamREF
		)T
		WHERE num > ' + CONVERT(VARCHAR,(@PageIndex-1)*@RecordCount) 
		
	PRINT @Sql
	EXEC (@Sql)
END

```
