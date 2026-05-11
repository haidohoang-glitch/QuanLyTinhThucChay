# Stored Procedure: `ThucChay_GetBaoCaoLechTreoHaTest`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2013-09-12 11:01:24.753000
- **Ngày sửa cuối**: 2014-10-14 10:39:54.977000

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
-- Author:		<Author,,Name>
-- Create date: <Create Date,,>
-- Description:	<Description,,>
-- =============================================
CREATE PROCEDURE [dbo].[ThucChay_GetBaoCaoLechTreoHaTest] 
	-- Add the parameters for the stored procedure here
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
	
	
	SET @DauNhay = ''''
	
	SET @Sql = '
		SELECT TOP (' + CONVERT(NVARCHAR,@RecordCount) + ')
			T.SoHopDong, T.NgayLechTreoHa
			,(T.TongViewHopDong) AS TongViewHopDong
			,(T.TongViewThucChay) AS TongViewThucChay
			,(T.TongViewLechTreoHa) AS TongViewLechTreoHa
			,ROUND(T.ThanhTienThucChay,0) AS ThanhTienThucChay
			,ROUND(T.ThanhTienLechTreoHa,0) AS ThanhTienLechTreoHa
		FROM
		(
			SELECT 
				T1.SoHopDong, T1.NgayLechTreoHa
				,MAX(T1.TongViewHopDong) AS TongViewHopDong
				,SUM(T1.TongViewThucChay) AS TongViewThucChay
				,SUM(T1.TongViewLechTreoHa) AS TongViewLechTreoHa
				,ROUND(SUM(T1.ThanhTienThucChay),0) AS ThanhTienThucChay
				,ROUND(SUM(T1.ThanhTienLechTreoHa),0) AS ThanhTienLechTreoHa
				,ROW_NUMBER() OVER (ORDER BY T1.NgayLechTreoHa) AS num
			FROM
			('
				+ dbo.ThucChay_GenSQLCommandBaoCaoLechTreoHa(@StartDate,@EndDate,@ListDmSanPhamREF,@ListSoHopDong,@TenDangNhap) + 
			')T1
			GROUP BY T1.SoHopDong,T1.NgayLechTreoHa    
		)T
		WHERE num >' + CONVERT(VARCHAR,(@PageIndex-1)*@RecordCount) 
		
		PRINT @Sql
		EXEC (@Sql)
END

```
