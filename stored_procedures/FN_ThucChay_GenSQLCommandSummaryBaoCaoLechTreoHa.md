# Function: `ThucChay_GenSQLCommandSummaryBaoCaoLechTreoHa`

- **Loại**: SQL_SCALAR_FUNCTION
- **Ngày tạo**: 2013-09-11 15:05:12.190000
- **Ngày sửa cuối**: 2014-10-14 10:39:32.800000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `(Return Value)` | `nvarchar(8000)` | Yes |
| `@StartDate` | `datetime(8)` | No |
| `@EndDate` | `datetime(8)` | No |
| `@ListDmSanPhamREF` | `nvarchar(400)` | No |
| `@ListSoHopDong` | `nvarchar(4000)` | No |
| `@TenDangNhap` | `nvarchar(100)` | No |

## Definition (Source Code)

```sql
-- =============================================
-- Author:		NhatMQ
-- Create date: 2013-09-11
-- Description:	<Description, ,>
-- =============================================
CREATE FUNCTION [dbo].[ThucChay_GenSQLCommandSummaryBaoCaoLechTreoHa]
(
	-- Add the parameters for the function here
	@StartDate DATETIME,
	@EndDate DATETIME,
	@ListDmSanPhamREF NVARCHAR(200),
	@ListSoHopDong NVARCHAR(2000),
	@TenDangNhap NVARCHAR(50)
)
RETURNS NVARCHAR(4000)
AS
BEGIN
	-- Declare the return variable here
	DECLARE @Sql NVARCHAR(4000)
	DECLARE @DauNhay NVARCHAR(50)
	DECLARE @StartDateString NVARCHAR(100)
	DECLARE @EndDateString NVARCHAR(100)
	DECLARE @FillterBySanPham NVARCHAR(200)
	DECLARE @FillterByHopDong NVARCHAR(200)
	DECLARE @ListSanPham NVARCHAR(50)
	DECLARE @GroupPermission INT
	
	SET @DauNhay = ''''
	SET @StartDateString = @DauNhay + CONVERT(NVARCHAR(50),@StartDate) + @DauNhay
	SET @EndDateString = @DauNhay + CONVERT(NVARCHAR(50),@EndDate) + @DauNhay
	
	SET @GroupPermission = dbo.NhanSuCheckGroupPermisstion(@TenDangNhap)
	
	IF @GroupPermission = -1
		SET @TenDangNhap = ''
	
	IF @ListDmSanPhamREF = ''
		SET @ListDmSanPhamREF = '231,238,240,339,370'
	SET @ListSanPham = dbo.GetListSanPhamByNhanVien(@TenDangNhap)
	
	IF @ListSoHopDong = '' 
		SET @FillterByHopDong = ''
	ELSE
		SET @FillterByHopDong = ' AND A.SoHopDong IN (' + @ListSoHopDong + ')'


	SET @Sql = '
			SELECT
				A.DmSanPhamREF, A.TenSanPham, A.SoHopDong,A.HopDongChiTietREF, 
				MAX(B.NgayThucHien) AS NgayLechTreoHa,
				A.TenDangNhap,
				SUM(A.TongViewThucChay) AS TongViewThucChay,
				ISNULL(MAX(CAST(A.SoLuong AS BIGINT)),0) AS TongViewHopDong,
				SUM(A.SoLuongThucChayLechTreoHa) AS TongViewLechTreoHa,
				ISNULL(SUM(A.ThanhTienSauTrietKhauThucChay),0) + SUM(A.ThanhTienKM) AS ThanhTienThucChay,
				SUM(A.ThanhTienLechTreoHa) AS ThanhTienLechTreoHa
			FROM ThucChayDaTinh A
				INNER JOIN ThucChay_TienLechTreoHaTheoSanPham B ON B.SoHopDong = A.SoHopDong
			WHERE 1=1 and CONVERT(DATE,A.NgayThucHien) Between ' + @StartDateString + ' AND ' + @EndDateString + '
				AND A.TrangThaiHopDong <> 3 
				AND A.DmSanPhamREF IN (' + @ListDmSanPhamREF + ')' 
	SET @Sql +=  @FillterByHopDong
	IF @GroupPermission <> -1
		SET @Sql+= ' AND A.TenDangNhap = ' + @TenDangNhap 
		SET @Sql+= '
			GROUP BY 
				A.DmSanPhamREF, A.TenSanPham, A.SoHopDong,A.HopDongChiTietREF,B.NgayThucHien,A.TenDangNhap
			'
			
	-- Return the result of the function
	RETURN @Sql

END
```
